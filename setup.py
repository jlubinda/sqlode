import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlubinda", # Replace with your own username
    version="0.0.1",
    author="Joseph Lubinda",
    author_email="jlubinda@gmail.com",
    description="A package the aims at making it easier and quicker to perform database operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jlubinda/sqlode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)