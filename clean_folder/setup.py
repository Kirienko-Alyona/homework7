from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1',
    author= 'Kirienko Alyona'
    description='Sorted files for extensions',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:start_terminal']}
    )
    