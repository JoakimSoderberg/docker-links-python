# -*- coding: utf-8 -*-

# legacy distutils
from distutils.core import setup
# try the new one
try:
    from setuptools import setup
except:
    pass

long_description = open('README.md').read()

setup(name='docker-links-python',
      version='0.1.0',
      description='A helper for parsing Docker link environment variables',
      long_description=long_description,
      author='Joakim Söderberg',
      license='MIT',
      url='https://github.com/JoakimSoderberg/docker-links-python',
      py_modules=['docker_links'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Langugae :: Python :: 2.6',
          'Programming Langugae :: Python :: 2.7',
          'Programming Langugae :: Python :: 3',
          'Programming Langugae :: Python :: 3.2',
          'Programming Langugae :: Python :: 3.3',
          'Programming Langugae :: Python :: 3.4',
          'Programming Langugae :: Python :: 3.4',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
     )
