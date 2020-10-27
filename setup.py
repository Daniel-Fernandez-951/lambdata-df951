import setuptools

REQUIRED = ['numpy', 'pandas', 'tabulate']

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="lamdata-df951", # Replace with your own username
    version="0.0.2",
    author="Daniel-Fernandez-951",
    description="Example Collection of DS Modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Daniel-Fernandez-951/lambdata-df951",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
