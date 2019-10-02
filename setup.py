import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gravify",
    version="0.3.0",
    author="Benjamin Soyka",
    author_email="bensoyka@icloud.com",
    description="A simple package to generate a Gravatar URL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsoyka/gravify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
    python_requires='>=3.6',
)
