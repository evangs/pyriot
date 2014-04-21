from distutils.core import setup
setup(name='pyriot',
      version='2.0.2',
      description='python wrapper for riot league of legends api',
      author='Evan Sailer',
      author_email='esailer@asu.edu',
      url='http://ehom.co',
      packages=['pyriot'],
      install_requires=['requests==2.1.0','pytz==2013.8',],
      )