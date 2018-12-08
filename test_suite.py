import sys
import unittest

from osgeo import gdal
from qgis.PyQt import Qt
from qgis.core import Qgis


def _run_tests(test_suite, package_name):
    """Core function to test a test suite.

    :param test_suite: Unittest test suite
    """
    count = test_suite.countTestCases()
    print('########')
    print('%s tests has been discovered in %s' % (count, package_name))
    print('QGIS : %s' % Qgis.QGIS_VERSION_INT)
    print('Python GDAL : %s' % gdal.VersionInfo('VERSION_NUM'))
    print('QT : %s' % Qt.QT_VERSION_STR)
    print('########')
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)


def test_package(package=''):
    """Test package.
    This function is called by travis without arguments.

    :param package: The package to test.
    :type package: str
    """
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover(package)
    _run_tests(test_suite, package)


if __name__ == '__main__':
    test_package()
