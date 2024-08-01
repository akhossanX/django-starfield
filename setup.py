import os
from setuptools import setup

MYDIR = os.path.dirname(__file__)

setup(
    name='django-starfield',
    version='1.0.post2',
    keywords = ['django', 'forms', 'widget', 'rating'],
    description = 'A no-frills Django form widget for rating stars',
    long_description = open(os.path.join(MYDIR, "README.rst"), "r", encoding="utf-8").read(),
    url = 'https://edugit.org/AlekSIS/libs/django-starfield',
    author='Dominik George',
    author_email='dominik.george@teckids.org',
    packages=['django_starfield'],
    include_package_data=True,
    install_requires=['Django>=1.11'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
