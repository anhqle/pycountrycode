from distutils.core import setup

setup(
    name='countrycode',
    version='0.2',
    author='Vincent Arel-Bundock',
    author_email='varel@umich.edu',
    packages=['countrycode'],
    #scripts=[],
    url='http://umich.edu/~varel',
    license='LICENSE.txt',
    description='Convert country names and country codes',
    long_description=open('README.txt').read(),
    package_data={'countrycode': ['data/countrycode_data.csv']}
)
