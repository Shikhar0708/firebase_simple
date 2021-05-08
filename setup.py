import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="firebase_simple", # Replace with your own username
    version="0.0.1",
    author="Mangekyo 07081999",
    author_email="shikharsinha34920@gmail.com",
    description="Experience firebase with hustle free declaration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shikhar0708/firebase_simple",
    project_urls={
        "Bug Tracker": "https://github.com/Shikhar0708/firebase_simple/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)