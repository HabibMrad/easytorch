import pathlib
import pkg_resources
import subprocess

from setuptools import setup

# The directory containing this file
_HERE = pathlib.Path(__file__).parent

# The text of the README file
_README = (_HERE / "README.md").read_text()

# Requirements
_requires = ['numpy',
             'scipy',
             'scikit-learn',
             'scikit-image',
             'pillow',
             'matplotlib',
             'pandas',
             'seaborn']

try:
    pkg_resources.get_distribution('opencv-contrib-python')
    subprocess.call(["pip", "uninstall", "opencv-contrib-python", "-y"])
except:
    _requires.append('opencv-python-headless')

# This call to setup() does all the work
setup(
    name="easytorch",
    version="3.3.0",
    description="Easy Neural Network Experiments with pytorch",
    long_description=_README,
    long_description_content_type="text/markdown",
    url="https://github.com/sraashis/easytorch",
    author="Aashis Khana1",
    author_email="sraashis@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['easytorch', 'easytorch.config', 'easytorch.data', 'easytorch.metrics', 'easytorch.utils',
              'easytorch.vision'],
    include_package_data=True,
    install_requires=_requires
)
