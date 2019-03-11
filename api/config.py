import configparser

config = configparser.ConfigParser()
config.read("../script-generator.properties")

def get(section, key):
    return config[section].get(key, '')