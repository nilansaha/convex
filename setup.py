from setuptools import setup

with open('README.md') as f:
	long_description = f.read()

with open('requirements.txt') as f:
	requirements = f.readlines()

setup(
	name='convex',
	version='0.0.1',
	author='Nilan Saha',
	description = 'A Light-weight Python NLP Library',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/nilansaha/convex',
	license = 'Apache 2.0',
	packages = ['convex'],
	install_requires = requirements,
	python_requires='>=3.6',
	classifiers = [
		'Programming Language :: Python'
	]
)
