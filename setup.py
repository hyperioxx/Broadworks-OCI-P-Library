import os
from setuptools import setup,find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "BroadworksOCIP",
    version = "0.0.4",
    author = "Aaron Parfitt",
    author_email = "aaronparfitt123@gmail.com",
    description = ("Broadworks Open Client Interface Client"),
    license = "BSD",
    keywords = "Broadworks",
    packages=find_packages(),
    install_requires = ['zeep',],
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    scripts=['scripts/bw-ocip'],
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
