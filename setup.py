from setuptools import setup

setup(
    name='QuickTry',
    version='0.1',
    long_description=__doc__,
    packages=['quicktry'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.11.1',
        'PyYaml==3.11',
        'docker-py==1.9.0'
    ]
)