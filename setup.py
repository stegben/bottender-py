from pathlib import Path
from setuptools import setup, find_packages

readme = Path(__file__).parent.joinpath('README.md')
if readme.exists():
    with readme.open() as f:
        long_description = f.read()
        try:
            from pypandoc import convert_text
            long_description = convert_text(
                long_description, 'rst', format='md')
        except ImportError:
            print("warning: pypandoc module not found, could not convert Markdown to RST")
else:
    long_description = '-'

REQUIRED_PACKAGES = []


setup(
    name="bottender",
    version="0.0.2",
    description=long_description,
    author="cph",
    author_email="stegben.benjamin@gmail.com",
    url="https://github.com/stegben/bottender-py",
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
)
