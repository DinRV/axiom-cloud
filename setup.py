from setuptools import setup, find_packages

setup(
    name="axiom-cloud",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "boto3>=1.26.0"
    ],
    entry_points={
        "console_scripts": [
            "axiom=axiom.cli:main",
        ],
    },
    description="Lightweight AWS CLI alternative",
    author="Axiom Labs",
)
