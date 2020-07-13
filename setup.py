from setuptools import setup, find_packages

with open("requirements.txt") as req:
    install_requires = req.read()

setup(
    name='client-manager',
    version='0.0.1',
    description='',
    url='https://github.com/ymussi/client-manager.git',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    packages=find_packages(),
    zip_safe=False
),