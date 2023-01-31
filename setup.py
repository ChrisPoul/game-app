from setuptools import setup

setup(
    name='Chat',
    packages=['Chat'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-socketio'
    ],
)
