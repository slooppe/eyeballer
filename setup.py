from setuptools import find_packages, setup

setup(
    name='eyeballer',
    version='0.0.1',
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/BishopFox/eyeballer',
    license='GNU General Public License v3.0',
    author='Bishop Fox',
    author_email='',
    description='',
    entry_points={
        'console_scripts': [
            'eyeballer = eyeballer.eyeballer:cli'
        ]
    },
    install_requires=[
        'Augmentor',
        'click',
        'matplotlib',
        'numpy',
        'pandas',
        'pillow',
        'sklearn',
        'tensorflow-gpu',
        'keras',
    ],
    dependency_links=[
    ],
)
