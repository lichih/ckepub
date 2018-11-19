from setuptools import setup

setup(
    name='ckepub',
    version='0.1.0',
    description='ck101 novel to epub',
    author='Li-chih Wu',
    author_email='lichihwu@gmail.com',
    packages=['ckepub'],
    include_package_data=True,
    install_requires=[
        'pyquery',
    ]
)
