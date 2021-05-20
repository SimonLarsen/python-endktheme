from setuptools import setup, find_packages
import endktheme

setup(
    name="endktheme",
    description="Visualization themes following Energinet's design guide.",
    version=endktheme.__version__,
    author="Simon J. Larsen",
    author_email="simonhffh@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
)
