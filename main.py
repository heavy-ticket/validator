import os
from dataset import Dataset

dataset = Dataset('../cave_annotations')
print('train: ', dataset.config.train)
print('val: ', dataset.config.val)
print('test: ', dataset.config.test)
print('nc: ', dataset.config.nc)
print('names:', dataset.config.names)
