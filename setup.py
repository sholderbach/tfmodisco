from distutils.core import setup

if __name__== '__main__':
    setup(include_package_data=True,
          description='MOtif Discovery from Importance SCOres',
          url='NA',
          download_url='NA',
          version='0.1',
          packages=['modisco', 'modisco.util'],
          setup_requires=[],
          install_requires=['numpy>=1.9', 'theano>=0.8'],
          scripts=[],
          name='modisco')
