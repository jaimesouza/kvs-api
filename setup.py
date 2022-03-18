import versioneer
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md") as f:
    readme = f.read()

setup(
    name="kvs",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Simple REST API for a key-value store using Python FastAPI framework.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/jaimesouza/kvs-api',
    author="Jaime Freire de Souza",
    author_email="jaimefreire.souza@gmail.com",
    license="GPL-3.0 License",
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',            
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)