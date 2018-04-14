
from setuptools import setup

setup(
    name='pyopenmrs',
    version='0.1',
    description='a library for interacting with openmrs api in python',
    url='https://github.com/fortitudoinc/pyopenmrs',
    author='Isaac Sears',
    author_email='isaac.j.sears@gmail.com',
    license='MIT',
    packages=['pyopenmrs'],
    zip_safe=False,
    install_requires=[
        'requests'
    ]
)