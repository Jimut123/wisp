import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wisp",
    version="0.0.8-b",
    author="Jimut Bahan Pal",
    author_email="jimutbahanpal@yahoo.com",
    description="A preference based location finder application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jimut123/wisp",
    install_requires=['requests', 'pandas','folium','geopy','numpy','wget','datetime','IPython','pip'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

