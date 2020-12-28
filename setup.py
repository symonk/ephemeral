#!/usr/bin/env python

"""The setup script."""
from typing import List

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements: List = []

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest>=3"]

setup(
    author="Simon Kerr",
    author_email="jackofspaces@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Port scanning made easy with python",
    entry_points={"console_scripts": ["ephemeral=ephemeral.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="ephemeral",
    name="ephemeral",
    packages=find_packages(include=["ephemeral", "ephemeral.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/symonk/ephemeral",
    version="0.1.0",
    zip_safe=False,
)
