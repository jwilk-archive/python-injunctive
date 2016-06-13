'''
*injunctive* provides Perl6 style junctions_ (``all``, ``any``, ``one``, ``none``).

.. _junctions: https://www.perl6.org/archive/doc/design/exe/E06.html#The%20Wonderful%20World%20of%20Junctions
'''

classifiers = '''
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
'''.strip().splitlines()

import distutils.core

distutils.core.setup(
    name='injunctive',
    version='0.1',
    license='MIT',
    platforms=['any'],
    description='Perl6 style junctions',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='https://github.com/jwilk/python-injunctive',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['injunctive']
)

# vim:ts=4 sts=4 sw=4 et
