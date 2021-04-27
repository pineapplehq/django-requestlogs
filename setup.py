from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

requirements = (
    'Django>=1.11,<4.0',
    'djangorestframework>=3.0,<4.0',
    'setuptools',
)

dev_requirements = (
    'pytest',
)

setup(
    name='welcome-django-requestlogs',
    zip_safe=False,
    version='0.0.3',
    description='Audit logging for Django and Django Rest Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[],
    keywords=['django', 'log', 'logging'],
    author='Welcome Engineering',
    author_email='platform@heywelcome.com',
    url='https://github.com/pineapplehq/django-requestlogs',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements
    },
)
