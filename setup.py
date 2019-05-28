import os
from setuptools import setup,find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "BroadworksOCIP",
    version = "0.0.1",
    author = "Aaron Parfitt",
    author_email = "aaronparfitt123@gmail.com",
    description = ("Broadworks Open Command Interface Client"),
    license = "BSD",
    keywords = "Broadworks",
    packages=find_packages(),
    long_description=read('README.md'),
    scripts=['scripts/bw-ocip'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
    ],
)
