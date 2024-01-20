import yaml


def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = yaml.safe_load(fp)
    return data


def split_file_title_type(file_name):
    splited = file_name.split('.')

    file_type = splited[-1]
    file_titles = splited[:-1]
    file_title = '.'.join(file_titles)

    return file_title, file_type
