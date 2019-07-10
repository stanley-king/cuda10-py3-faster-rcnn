
import unittest

import _init_paths
from datasets.pascal_voc import pascal_voc

class MyTestCase(unittest.TestCase):
    def test_pascal_voc(self):
        d = pascal_voc('trainval', '2007')
        res = d.roidb
        from IPython import embed
        embed()

if __name__ == '__main__':
    unittest.main()
