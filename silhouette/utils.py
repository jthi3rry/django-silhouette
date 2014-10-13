import re


def normalize(name):
    return re.sub('(((?<=[a-z])[A-Z1-9])|([A-Z1-9](?![A-Z1-9]|$)))', '_\\1', name).strip('_').lower()
