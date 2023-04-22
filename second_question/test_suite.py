import unittest

loader = unittest.TestLoader()
suite = loader.discover(start_dir='./tests', pattern='*_test.py')
runner = unittest.TextTestRunner()
result = runner.run(suite)