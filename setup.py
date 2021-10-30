import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("version", "r", encoding="utf-8") as f:
    version_info = f.read()

setuptools.setup(
    name="coin-pkg-saynot",
    version=version_info,
    author="SAYNOT",
    author_email="jehyun9027@gmail.com",
    description="A Simple Coin Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SCPJaehyeon/coin",
    project_urls={
        "Bug Tracker": "https://github.com/SCPJaehyeon/coin/issues",
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)