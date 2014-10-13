import unittest

from silhouette import utils


class TestUtils(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(utils.normalize('MyNameToNormalize'), 'my_name_to_normalize')
