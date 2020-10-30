################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
	],
	description = "This python module provides various utility functions and classes.",
	include_package_data = False,
	install_requires = [
		"sh",
		"sortedcontainers",
		"jk_simpleexec",
		"jk_logging",
		"netifaces",
	],
	keywords = [
		"utilities",
	],
	license = "Apache2",
	name = "jk_utils",
	packages = [
		"jk_utils",
		"jk_utils.async",
		"jk_utils.color",
		"jk_utils.datetime",
		"jk_utils.tokenizer2",
	],
	version = "0.2020.10.30",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
