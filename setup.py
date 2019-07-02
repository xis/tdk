import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tdk_w",
    version="1.0.0",
    author="Enes Furkan Olcay",
    author_email="dandikbirdalga@gmail.com",
    description="tdk api yan sanayisi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xepea/tdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)