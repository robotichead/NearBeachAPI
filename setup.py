import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NearBeachAPI",
    version="0.0.1",
    author="Luke Christopher Clarke",
    author_email="luke@nearbeach.org",
    description="The optional API module for NearBeach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robotichead/NearBeachAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)