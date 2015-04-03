import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

version = '0.1.0'


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

setup(name='genstrings_swift',
      version=version,
      description=('genstrings commandline tool for Swift'),
      long_description='\n\n'.join((read('README.md'), read('CHANGELOG'))),
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Intended Audience :: Developers',
          'Programming Language :: Python'],
      author='Keepsafe',
      author_email='support@getkeepsafe.com',
      url='https://github.com/KeepSafe/genstrings_swift/',
      license='Apache',
      py_modules=['genstrings_swift', 'genstrings_merge'],
      package_data={},
      namespace_packages=[],
      entry_points={
          'console_scripts': [
              'genstrings_swift = genstrings_swift:main',
              'genstrings_merge = genstrings_merge:main']
      },
      include_package_data = False)
