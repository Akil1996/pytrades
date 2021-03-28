from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='pytraders',
    version='0.0.1',
    description="A Python package to get trading indicators.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='git@github.com:Akil1996/pytraderr',  
    author='Akil Thangavel',
    author_email='akilh4@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)