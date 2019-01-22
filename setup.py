# coding=utf-8
import glob

from setuptools import setup, find_packages

from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))
base = here


with open(path.join(base, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="behavior3py",
    version="0.1.0",
    install_requires=['docutils>=0.3',
            'setuptools',
        ],
    packages=find_packages('src'),  # include all packages under src
    package_dir={'': 'src'},  # tell distutils packages are under src

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        'behavior3py': ['*.json', '*.png', '*.md'],
    },

    entry_points={
        'console_scripts': [

        ],
        'gui_scripts': [

        ]
    },

    # metadata to display on PyPI
    author="Renato de Pontes Pereira",
    author_email="renato.ppontes@gmail.com",
    maintainer='mikepsn',
    maintainer_email='mikepsn@users.noreply.github.com',
    description="Behavior Tree library ported to Python 3.x",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='behavior tree ai agent programming',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url="https://github.com/mikepsn/behavior3py",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/mikepsn/behavior3py",
        "Documentation": "https://github.com/mikepsn/behavior3py",
        "Source Code": "https://github.com/mikepsn/behavior3py",
    }

    # could also include long_description, download_url, classifiers, etc.
)