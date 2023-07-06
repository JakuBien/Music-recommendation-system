import processData as pd

def main():
    pd.enable_eager()
    music_directory = "audioset_v1_embeddings/eval"
    labels_directory = "class_labels_indices.csv"
    audios = pd.get_music_dataset(music_directory, labels_directory)
    json_file_name = "music_set.json"
    pd.store_json_in_file(json_file_name, audios)


if __name__ == "__main__":
    main()