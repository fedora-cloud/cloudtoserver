#!/usr/bin/env python
"""Setup script"""
from setuptools import setup

setup(name='cloudtoserver',
      version='0.1',
      description="Converts Fedora Cloud instance to Fedora Server instance.",
      long_description = "Converts Fedora Cloud instance to Fedora Server instance.",
      platforms = ["Linux"],
      author="Kushal Das",
      author_email="kdas@redhat.com",
      url="https://github.com/fedora-cloud/cloudtoserver",
      license = "http://www.gnu.org/copyleft/gpl.html",
      scripts = ['cloudtoserver']
      )
