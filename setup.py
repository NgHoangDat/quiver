import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awesome_quiver",
    packages=setuptools.find_packages(),
    version="0.1.1",
    author="nghoangdat",
    author_email="18.hoang.dat.12@gmail.com",
    description="quiver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NgHoangDat/awesome_quiver.git",
    download_url="https://github.com/NgHoangDat/awesome_quiver/archive/v0.1.1.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'dataclasses; python_version=="3.6"',
        'msgpack',
        'python-dateutil',
        'pyyaml',
        'toolz'
    ]
)