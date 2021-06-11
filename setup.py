import os
import setuptools
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 2 - Pre-Alpha',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
  'Programming Language :: Python :: 3',
]

with open('README.md') as f:
    long_description = f.read()


if os.getenv("READTHEDOCS") == "True":
    INSTALL_REQUIRES = []
else:
    with open("requirements.txt") as f:
        INSTALL_REQUIRES = [line.strip() for line in f.readlines()]
        
setup(
  name='my_project_banbar',
  version='0.0.93',
  description='A package to do arithmetics',
  long_description=long_description,
  long_description_content_type='text/markdown',  
  author='banbar',
  author_email='banbar@hacettepe.edu.tr',
  license='GNU General Public License v2.0', 
  classifiers=classifiers,
  keywords=['math'], 
  packages=["my_project_banbar",
            "my_project_banbar.tests"],
  python_requires=">=3.6",
  package_data={"my_project_banbar": ['data/*']},
  install_requires=INSTALL_REQUIRES
)

# package_dir={"": "src"}, - 1+ packages - put package directories under src

#include_package_data=True,
#package_data={"geopandas": data_files},
# install_requires=['numpy >= 1.19.3'],
# get all data dirs in the datasets module
# data_files = []

# Once we have data?
# for item in os.listdir("geopandas/datasets"):
#     if not item.startswith("__"):
#         if os.path.isdir(os.path.join("geopandas/datasets/", item)):
#             data_files.append(os.path.join("datasets", item, "*"))
#         elif item.endswith(".zip"):
#             data_files.append(os.path.join("datasets", item))

#data_files.append("tests/*")