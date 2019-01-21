import os
import glob
import yaml
import copy
import logging


class PKG(object):
    def __init__(self, config_path: str=None, stage: str=None, logger=None):
        self.__config_path = config_path or os.getenv('CONFIG_PATH', '/configuration') 
        self.__stage = stage or os.getenv('STAGE', 'defaults')
        
        self.__logger = logger or logging.getLogger('dummy')
        
        self.__logger.info('CONFIG_PATH: %s' % config_path)
        self.__logger.info('STAGE: %s' % stage)

    @property
    def config_path(self):
        return self.__config_path

    @property
    def stage(self):
        return self.__stage

    def load(self):
        """Initialize all the magic down here"""

        self.__config = self.__merge(self.__load_defaults(), self.__load_stage())

    def get(self, key: str, default=None):
        """Get's a value from config by dot notation
        
        E.g get('x.y', 'foo') => returns the value of config['x']['y']
        And if not exist, return 'foo'
        """
        
        config = self.__config

        for item in key.split('.'):
            config = copy.deepcopy(config.get(item))
            if config is None:
                return default

        return config

    def get_all(self) -> dict:
        """Gets all the tree config"""

        return self.__config

    def __load_defaults(self) -> dict:
        return self.__parse_configuration()

    def __load_stage(self):
        return self.__parse_configuration(self.__stage)

    def __parse_configuration(self, stage: str='defaults') -> dict:
        """Parses configuration and makes a tree of it"""

        config_path = os.path.join(self.__config_path, stage)
        
        if os.path.exists(config_path) and glob.glob(config_path + '/*.yaml') != []:
            file_list = glob.glob(config_path + '/*.yaml')
        else:
            self.__logger.info('Path not found')
            raise FileNotFoundError

        config = {}

        for _file in file_list:
            yaml_content = self.__parse_yaml_file(_file, stage)
            if yaml_content is None:
                self.__logger.info('Incorrect yaml content: %s' % _file)
                raise ValueError
            
            config = self.__merge(config, yaml_content)
        return config

    def __merge(self, default_config: dict, stage_config: dict) -> dict:
        """Merges any number of arrays/parameters recursively.
        
        Replacing entries with string keys with values from latter arrays.
        If the entry or the next value to be assigned is an array, then it
        automagically treats both arguments as an array.
        Numeric entries are appended, not replaced, but only if they are unique"""

        for key in default_config:
            if type(default_config[key]) is dict:
                if key in stage_config:
                    default_config[key] = self.__merge(default_config[key], stage_config[key])
            else:
                if key in stage_config:
                    default_config[key] = stage_config[key]
        for key in stage_config:
            if key not in default_config:
                default_config[key] = stage_config[key]
        
        return default_config

    @staticmethod
    def __parse_yaml_file(path: str, stage: str):
        """Parses the yaml file"""

        try:
            return yaml.load(open(path, 'r')).get(stage, None)
        except:
            return None
