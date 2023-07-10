import processData as pd
import recommendationEngine as re

def main():
    # Consts
    music_directory = "audioset_v1_embeddings/eval"
    labels_directory = "class_labels_indices.csv"
    json_file_name = "music_set.json"

    # Processing data files (learning)
    pd.enable_eager()
    audios = pd.get_music_dataset(music_directory, labels_directory)
    pd.store_json_in_file(json_file_name, audios)

    # Processing data file (search algorythm)
    music_dict = re.create_music_dictionary(labels_directory)
    music_dataset = re.read_json_dataset(json_file_name)
    re.dataset_size(music_dataset)
    re.annoy_algorythm(music_dataset, music_dict)


if __name__ == "__main__":
    main()