import yaml
from dataclasses import dataclass

_configs = {}

def register_config(cls):
    """Regiser config class by name"""
    _configs[cls.__name__] = cls


class Meta(type):
    """Meta class for configuration classes"""
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_config(cls)
        return cls

class Config(metaclass=Meta):
    """Parent class for configuration subclasses"""
    pass

@dataclass
class DataConfig(Config):
    image_dir: str = None
    label_dir: str = None
    calibration_dir: str = None


def parse(fname):
    """Config parser for yaml config files that contain multiple config sections"""
    with open(fname) as f:
        all_configs = yaml.load(f, Loader=yaml.Loader)
        configs = {}
        for config_class, content in all_configs.items():
            if config_class in _configs:
                configs[config_class] = _configs[config_class](**content)
    return configs

