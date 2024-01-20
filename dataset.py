import os
from dataclasses import dataclass

import cv2
from utils import load_yaml, split_file_title_type
from bbox import BBox


@dataclass(frozen=True)
class DatasetConfig:
    train: str
    val: str
    test: str
    nc: int
    names: list


class Dataset:

    def __init__(self, dataset_path):
        self.load(dataset_path)

    def load(self, folder_path):
        config_path = os.path.join(folder_path, 'data.yaml')
        self.config = DatasetConfig(**load_yaml(config_path))

    def load_dataset_train_item(self, image_name):

        image_title, image_type = split_file_title_type(image_name)
        label_name = image_title + '.txt'

        label_path = os.path.join(self.config.train, 'labels', label_name)
        image_path = os.path.join(self.config.train, 'images', image_name)

        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape
        original_size = (image_width, image_height)

        bboxes = list(BBox.from_label_file(label_path, original_size))
        return image, bboxes
