from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in academia/__init__.py
from academia import __version__ as version

setup(
	name="academia",
	version=version,
	description="An app developed for school/institute to manage their task in efficient way",
	author="stackinfo",
	author_email="info@stackinfo.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
