from setuptools import setup, find_packages
 
classifiers = []
 
setup(
  name='metasearch',
  version='5.1',
  description='Pre built metasearch repository for easy uses.',
  long_description=open('pypisupport.md').read() + "\n#### pog",
  long_description_content_type='text/markdown',
  url='https://github.com/dumb-stuff/Meta-search',  
  author='Rukchad Wongprayoon',
  author_email='contact@biomooping.tk',
  license='MIT', 
  classifiers=classifiers,
  keywords='Tools', 
  packages=find_packages(),
  install_requires=["flask","requests","googlesearch-python","asgiref"],
  entry_points={
    'console_scripts': ['metasearch=metasearch.__init__:launch']
  }
)