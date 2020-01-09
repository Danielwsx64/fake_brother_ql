# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

LDESC = 'A fake lib to mock brother_ql for marvin tests'

setup(name='fake_brother_ql',
        version = '0.9.dev0',
        description = LDESC,
        long_description = LDESC,
        author = 'Daniel',
        author_email = 'daniel@brainn.co',
        url = 'https://github.com/danielws/fake_brother_ql',
        license = 'GPL',
        packages = ['fake_brother_ql'],
        entry_points = {
            'console_scripts': [
                'fake_brother_ql = fake_brother_ql.cli:cli',
                ],
            },
        include_package_data = False,
        zip_safe = True,
        platforms = 'any',
        install_requires = [
            "click",
            'typing;python_version<"3.5"',
            'enum34;python_version<"3.4"',
            ],
        extras_require = {
            #'brother_ql_analyse':  ["matplotlib",],
            #'brother_ql_create' :  ["matplotlib",],
            },
        keywords = 'Fake BrotherQL',
        classifiers = [ 'Development Status :: 4 - Beta' ]
        )



