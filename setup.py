from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='0.1',
    description='script cleans folder',
    author='Yaroslav',
    classifiers=[
            'License '   
            'Programming language Python 3.10'
        ],   
    packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,    
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean_folder:__main__',
        ],
    }
)
