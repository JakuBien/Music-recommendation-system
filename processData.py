import numpy as np
import json
import tensorflow as tf
import os
import pandas as pd

def enable_eager():
    tf.compat.v1.enable_eager_execution()

def get_data(directory):
    dataset = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".tfrecord"):
            dataset.append(os.path.join(directory, file_name))
    return dataset

def convert_data_to_tf(dataset):
    return tf.data.TFRecordDataset(dataset)

def get_music_label_list(directory):
    class_labels = pd.read_csv(directory)
    music_class = class_labels[class_labels['display_name'].str.contains('Music', case=False)]
    return music_class['index'].tolist()

def get_music_dataset(music_directory, labels_directory):
    audios = []
    counter = 0
    NUM_SECONDS = 12

    dataset = get_data(music_directory)
    raw_dataset = convert_data_to_tf(dataset)
    music_labels = get_music_label_list(labels_directory)

    for raw_record in raw_dataset:
        example = tf.train.SequenceExample()
        example.ParseFromString(raw_record.numpy())
        
        # Audio Meta data
        audio_labels = example.context.feature['labels'].int64_list.value
        start_time = example.context.feature['start_time_seconds'].float_list.value
        end_time = example.context.feature['end_time_seconds'].float_list.value
        video_id = example.context.feature['video_id'].bytes_list.value
        
        if not (set(music_labels) & set(audio_labels)):
            continue

        # Audio Feature
        feature_list = example.feature_lists.feature_list['audio_embedding'].feature
        final_features = [list(feature.bytes_list.value[0]) for feature in feature_list]
        audio_embedding = [item for sublist in final_features[:NUM_SECONDS] for item in sublist]
        
        if len(final_features) < NUM_SECONDS:
            continue
        
        audio = {
            'label': audio_labels,
            'video_id': video_id[0],
            'start_time': start_time[0],
            'end_time': end_time[0],
            'data': audio_embedding
        }
        
        audios.append(audio)
        
        #To do wyjebania po testach
        counter += 1
        if counter % 100 == 0:
            print(f"Processing {counter}th file ...")
        #--------------------------
    return audios

        

def store_json_in_file(file_name, audios):
    with open(file_name, 'w') as file:
        str_audio = repr(audios)
        json.dump(str_audio, file)