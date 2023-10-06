from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    
    try:
        with open("requirements.txt", "r") as files:
            requirements = [file.replace("\n", "") for file in files.readlines() if "-e ." not in file]
            return requirements
    except Exception as e:
        return str(f"The error that occured is: {e}")

#get_requirements()
setup(
    name = "Flight_Delay",
    version = "0.0.0.1",
    description = "Flight Delay Prediction",
    author = "Victor Oshionwu",
    author_email = "victoropeyemi97@outlook.com",
    url = "https://github.com/omolevictor97/Flight_Delay",
    packages = find_packages(),
    license = "Apache License",
    install_requires = get_requirements()
)
