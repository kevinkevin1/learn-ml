import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


setuptools.setup(
    name="learn-ml",
    version="0.0.1",
    author="kevinkevin1",
    author_email="yohpaulkevin@gmail.com",
    description="A library capturing all things that Kevin has learned about",
    long_description=long_description,
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
        "matplotlib==3.5.1",
        "numpy==1.22.2",
        "pandas==1.4.1",
        "scikit-learn==1.0.2",
        "scipy==1.8.0",
        "seaborn==0.11.2",
    ],
    python_requires=">=3.6",
)
