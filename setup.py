import setuptools


setuptools.setup(
    name='hrml',
    version='1.0.0',
    author='RimoChan',
    author_email='the@librian.net',
    description='hrml',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/hrml',
    packages=['hrml'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'fire>=0.3.1',
    ],
    python_requires='>=3.5',
)