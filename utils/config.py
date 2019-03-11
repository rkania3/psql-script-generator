import configparser

config = configparser.ConfigParser()
config.read("../properties/script-generator.properties")

def get(section, key):
    return config[section].get(key, '')