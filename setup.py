from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()
    
setup(
    name="automacao_atas_models",
    version="0.1.0",
    description="""
Modelos de classes usando BaseModel do modulo pydantic para representar as estrtuturas
e entidades dentro do documento da ATA.
    """,
    author="Henrique Façanha Dutra",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[ 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)