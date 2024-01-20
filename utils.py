import yaml


def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = yaml.safe_load(fp)
    return data
