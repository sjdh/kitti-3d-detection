from config import parse

class App():
    """Kitti 3d detection application"""
    def __init__(self, config_file='config.yaml'):
        configs = parse(config_file)
        for name, config in configs.items():
            setattr(self, name, config)
        
app = App()
