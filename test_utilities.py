import unittest
from os import listdir


class UtilityTest(unittest.TestCase):

    def setUp(self) -> None:
        """Sets some preconditions to the test scenario."""
        pass

    def test_list_dir(self):
        dirs = listdir("/home/musashi")
        clean_dirs = filter(lambda c_dir: c_dir[0] != '.', dirs)
        for file_or_dir in clean_dirs:
            print(f"Nombre de archivo {file_or_dir}, del tipo {type(file_or_dir)}")
            self.assertIsNotNone(file_or_dir)

        system_files = [file for file in clean_dirs if file[0] == '.']
        self.assertTrue(len(system_files) == 0)
