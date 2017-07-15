#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "megpack",
  version = "1.0",
  packages = [],
  scripts = ["scripts/megpack"],
  install_requires = ["docopt"],
  author = "Felix \"KoffeinFlummi\" Wiegand",
  author_email = "koffeinflummi@protonmail.com",
  description = "Packer for .meg files used in Petroglyph games.",
  long_description = read("README.md"),
  license = "MIT",
  keywords = "",
  url = "",
  classifiers=[
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Utilities"
  ]
)
