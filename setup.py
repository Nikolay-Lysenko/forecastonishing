"""
Just a regular `setup.py` file.

@author: Nikolay Lysenko
"""


import os
from setuptools import setup, find_packages


current_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='forecastonishing',
    version='0.1a',
    description='A set of tools for forecasting',
    long_description=long_description,
    url='https://github.com/osahp/forecastonishing',
    author='Nikolay Lysenko',
    author_email='nikolay-lysenco@yandex.ru',
    license='MIT',
    keywords='machine_learning forecasting adaptive_models',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.5',
    install_requires=['numpy', 'pandas', 'scikit-learn', 'pathos', 'tqdm']
)
