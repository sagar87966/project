from setuptools import setup,find_packages
import pip;
setup(
    name='same-app',
    version='2.0.0',
    description='project no 1',
    url='http://bitbucket.org/avily/sample-app',
    author='sagar',
    author_email='sagar.deotale@afourtech.com',
    license='MIT',
    packages=find_packages(exclude=['sample_app.test']),
    install_requires=['colored'],
    entry_points = {
     'console_scripts':[
         'sapp=sample_app.sample_app:main'
     ]
    }
)