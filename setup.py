from setuptools import setup
from setuptools import find_packages

setup(
    name='noccelerator',
    version='0.1.0',
    author='Jan Moritz Joseph, Yue Pan',
    author_email='joseph@ice.rwth-aachen.de',
    description='Spiking NN models with ratatoskr.',
    url='https://github.com/ratatoskr-project/noccelerator',
    license='MIT',
    packages=find_packages(exclude=['docs*', 'tests*']),
    package_data={
        'ratatoskr_tools.networkconfig': ['*.ini']
    },
    entry_points={
        'console_scripts': ['']
    },

)
