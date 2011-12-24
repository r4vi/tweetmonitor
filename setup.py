from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tweetmonitor',
      version=version,
      description="Use twitter's streaming api to watch for tweets mentioning a search term and log them to a couchdb database (realtime)",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='twitter streaming couchdb search',
      author='Ravi Kotecha',
      author_email='kotecha.ravi+tweetmonitor@gmail.com',
      url='http://github.com/r4vi/tweetmonitor',
      license='WTFPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
