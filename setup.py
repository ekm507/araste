import setuptools
from araste import __version__

with open("README_EN.md") as readme:
    long_description = readme.read()

setuptools.setup(
    name="araste",
    version=__version__,
    description="Convert persian text to ascii art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erfan Kheirollahi",
    author_email="ekm507@gmail.com",
    keywords="figlet",
    url="https://github.com/ekm507/araste",
    install_requires=["requests"],
    classifiers=[],
    packages=["araste"],
    package_dir={"araste": "araste"},
    include_package_data=True,
    scripts=[
        "bin/araste",
        "bin/araste-get",
    ],
)
