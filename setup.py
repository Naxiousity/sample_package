# setup.py

from setuptools import setup, find_packages

setup(
    name='sample_package',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python package with simple classes and functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/sample_package',  # Update with your GitHub repo URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
