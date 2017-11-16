from setuptools import setup

opts = dict(name='futurefish',
            description='Dashboard for climate projection impact on NW fish',
            url='',
            version='0.0.1',
            packages=['futurefish'],
            install_requires=['numpy', 'pandas']
            )


if __name__ == '__main__':
    setup(**opts)
