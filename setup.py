from setuptools import setup

setup(
  name='eclipsegen_cli',
  version='0.1.0',
  description='Generate Eclipse instances from a single command-line call',
  url='http://github.com/Gohla/eclipsegen_cli',
  author='Gabriel Konat',
  author_email='gabrielkonat@gmail.com',
  license='Apache 2.0',
  packages=['eclipsegen_cli'],
  install_requires=['eclipsegen>=0.2.0', 'plumbum>=1.6.2'],
  entry_points={
    'console_scripts': [
      'eclipsegen = eclipsegen_cli.main:main'
    ],
  }
)
