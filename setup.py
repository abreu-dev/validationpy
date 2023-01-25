import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="validationpy",
    version="0.0.1",
    author="Gabriel de Abreu",
    description="The fundamental package for building strongly-typed validation with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    py_modules=["validationpy"],
    install_requires=[]
)