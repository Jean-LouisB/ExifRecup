from setuptools import setup, find_packages

setup(
    name="Export exif",
    version="2.0.0",
    packages=find_packages(),
    install_requires=["exif"],
    author="Fabrice Kopf",
    description="Pour exporter les exifs d'un dossier de photos",
)