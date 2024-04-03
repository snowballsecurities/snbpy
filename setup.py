from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='snbpy',

    version='1.0.6',

    description='snbpy',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://www.snowballsecurities.com',

    author='SNB',

    author_email='service@xueqiu.com',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='snbpy',
    package_dir={'snbpy': 'src/snbpy'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['requests'],
    py_modules=['snbpy'],
    project_urls={
        'Bug Reports': 'https://github.com/snowballsecurities/snbpy/issues',
        'Funding': 'https://www.snowballsecurities.com',
        'Say Thanks!': 'https://www.snowballsecurities.com',
        'Source': 'https://github.com/snowballsecurities/snbpy',
    },
)
