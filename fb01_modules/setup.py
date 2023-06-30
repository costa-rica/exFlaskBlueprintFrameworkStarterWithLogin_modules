from setuptools import setup

setup (
    name="fb01-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "fb stands for FlaskBlueprints. This is a started modules kit",
    packages=['fb01_config','fb01_models'],
    python_requires=">=3.6",
    )