import os
import unittest
from config_pkg import PKG


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_init_from_env(self):
        os.environ['CONFIG_PATH'] = 'configuration'
        os.environ['STAGE'] = 'test'

        pkg = PKG()
        pkg.load()

        self.assertEqual(pkg.config_path, 'configuration')
        self.assertEqual(pkg.stage, 'test')
    
    def test_init_from_params(self):
        pkg = PKG('configuration', 'test')
        pkg.load()

        self.assertEqual(pkg.config_path, 'configuration')
        self.assertEqual(pkg.stage, 'test')

    def test_merge(self):
        pkg = PKG('configuration', 'test')
        pkg.load()

        self.assertEqual(pkg.get_all(), {
                'info': {
                    'about': 'about',
                    'use': True
                },
                "key": "value",
                "key2": "value2",
                "key3": "value3",
                "extra": {
                    "key": "value_overwrite",
                    "key2": "value_overwrite2",
                    "key3": "value_overwrite3",
                    "key4": [1, 5, 6],
                    "empty_arr": [1]
                },
                "key4": "value4",
                "key5": "value5",
                "key6": "value6"
            }
        )

    def test_defaults_stage(self):
        pkg = PKG('configuration', 'defaults')
        pkg.load()
        
        self.assertEqual(pkg.get_all(), {
                'info': {
                    'about': 'about',
                    'use': False
                },
                "key": "value",
                "key2": "value2",
                "key3": "value3",
                "extra": {
                    "key": "value",
                    "key2": "value2",
                    "key3": "value3",
                    "key4": [1, 2, 3],
                    "empty_arr": []
                },
            }
        )

    def test_file_not_found(self):
        os.environ['CONFIG_PATH'] = 'bad_path'
        pkg = PKG()

        self.assertRaises(FileNotFoundError, pkg.load)
    
    def test_bad_yaml_content(self):
        os.environ['STAGE'] = 'bad_yaml'
        os.environ['CONFIG_PATH'] = 'configuration'
        
        pkg = PKG()
        self.assertRaises(ValueError, pkg.load)

