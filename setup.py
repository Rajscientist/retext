from setuptools import setup, find_packages

setup(
    name='retext',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    author='RS',
    description='A simple Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
