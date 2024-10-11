from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''This functions returns requirements'''
    requirements=[]
    with open(file_path) as file_obj:
      requirements=file_obj.readlines ()
      requirements=[req.replace("\n","") for req in requirements]
    if '-e .' in requirements:
        requirements.remove('-e .')
    print("requirements in setup.py")
    print(requirements)
    return requirements

setup(
name='mymlproject',
version='0.0.1',
author='Ravali',
author_email='kanduriravali@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)