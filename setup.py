from setuptools import setup, find_packages 
setup(
    name="Spark-ESGI", 
    version="0.1", 
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get 
    # installed or upgraded on the target machine 
    install_requires=["docutils>=0.3"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        "hello": ["*.msg"],
    },

    # metadata to display on PyPI
    author="Kevin Monclaire",
    author_email="monclaire.kevin@gmail.com", 
    description="This is an Example Package",

    # could also include long_description, download_url, etc.
)