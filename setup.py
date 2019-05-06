import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuaidier",
    version="0.0.1",
    author="Alan Lee",
    author_email="secsilm@outlook.com",
    description="A package for notifying you by email when something is done",
    url="https://github.com/secsilm/kuaidier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
