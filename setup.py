
from setuptools import setup

setup(
    name='openmrsapi',
    version='0.1',
    description='a library for interacting with openmrs api in python',
    url='https://github.com/isears/openmrsapi',
    author='Isaac Sears',
    author_email='isaac.j.sears@gmail.com',
    license='MIT',
    packages=['openmrsapi'],
    zip_safe=False,
    install_requires=[
        'requests'
    ]
)