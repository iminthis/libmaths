import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="funcMath",
    version="0.1.0",
    author="Vinay Venkatesh",
    author_email="vinayven01@gmail.com",
    description="A Python library created to assist programmers with complex mathematical functions as well as for learning more about Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simple2006/funcMath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)