import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='juster',
    version='0.1.2',
    author="streanger",
    author_email="divisionexe@gmail.com",
    description="justification script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streanger/juster",
    packages=['juster',],
    license='MIT',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)