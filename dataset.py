import os
from dataclasses import dataclass
from utils import load_yaml


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
