import os
import unittest
from config_pkg import PKG


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_merge(self):
        os.environ['STAGE'] = 'test'
        os.environ['CONFIG_PATH'] = 'configuration'
        
        pkg = PKG()
        pkg.load()

        self.assertEqual(pkg.get_all(),
                         {
                           "key": "value",
                           "key2": "value2",
                           "key3": "value3",
                            "extra": {
                                "key": "value_overwrite",
                                "key2": "value_overwrite2",
                                "key3": "value_overwrite3",
                                "key4": [1, 2, 3, 5, 6]
                            },
                           "key4": "value4",
                           "key5": "value5",
                           "key6": "value6"
                         }
                         )

    def test_defaults_stage(self):
        os.environ['STAGE'] = 'defaults'
        os.environ['CONFIG_PATH'] = 'configuration'
        
        pkg = PKG()
        pkg.load()
        
        self.assertEqual(pkg.get_all(),
                         {
                             "key": "value",
                             "key2": "value2",
                             "key3": "value3",
                             "extra": {
                                 "key": "value",
                                 "key2": "value2",
                                 "key3": "value3",
                                 "key4": [1, 2, 3]
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

