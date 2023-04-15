from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.1",
    packages=find_packages(),
    description='script cleans folder',
    classifiers=[
          'License '   
          'Programming language Python 3.10'
    ],
    entry_points={
        "console_scripts": [
            "clean-folder = clean_folder.clean:main"
        ]
    },
    python_requires='>=3.5',
    include_package_data=True
)
