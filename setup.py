from setuptools import setup

name = 'example.packagerepo'
version = 0.1

# get packages from the package name: '1.2.3' -> ['1','1.2','1.2.3']
packages = [name.rsplit('.')[x] for x in range(len(name.split('.')))],

setup(name=name,
    version=version,
    description="Example package repository, containing one egg",
    #long_description=open("README.txt").read() + "\n" +
    #                 open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [],
    keywords='',
    author='Florian Friesdorf',
    author_email='flo@chaoflow.net',
    url='',
    license='',
    packages = packages,
    package_dir = {'': 'src'},
    # all except the last are treated as namespace_packages
    namespace_packages=packages[:-1],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        # -*- Entry points: -*-
    """,
    )
