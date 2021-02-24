import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as reqs:
    requirements = reqs.read().split("\n")

setuptools.setup(
    name="libmaths",
    version="0.1.6",
    author="Vinay Venkatesh",
    author_email="vinayven01@gmail.com",
    description="LibMaths is a Python library created to assist programmers with complex mathematical functions as well as for learning more about Python.",
    long_description=long_description,
    keywords=["Machine Learning", "Math", "Python"],
    install_requires=requirements,
    long_description_content_type="text/markdown",
    url="https://github.com/Simple2006/libmaths",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3',
)
