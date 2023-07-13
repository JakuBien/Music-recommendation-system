import processData as pd
import recommendationEngine as re

class DataProcessor():
    def __init__(self, parent=None):
        super(DataProcessor, self).__init__(parent)
        
        self.music_directory = "audioset_v1_embeddings/eval"
        self.labels_directory = "class_labels_indices.csv"
        self.json_file_name = "music_set.json"

    def startProcessing(self):
        # Processing data files (learning)
        pd.enable_eager()
        audios = pd.get_music_dataset(self.music_directory, self.labels_directory)
        pd.store_json_in_file(self.json_file_name, audios)

        # Processing data file (search algorythm)
        music_dict = re.create_music_dictionary(self.labels_directory)
        music_dataset = re.read_json_dataset(self.json_file_name)
        re.dataset_size(music_dataset)
        re.annoy_algorythm(music_dataset, music_dict)