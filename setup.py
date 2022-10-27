from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="dtn_doc_converter",
    version="0.1.0",
    description="A Python CLI converting DTN doc and docx files to Matatika dataset format.",
    author="DanielPDWalker",
    url="https://www.matatika.com/",
    entry_points="""
        [console_scripts]
        doc-converter=dtn_doc_converter.cli.commands.root:convert
    """,
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
