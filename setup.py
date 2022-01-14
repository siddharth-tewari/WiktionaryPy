from distutils.core import setup
setup(
  name = 'WiktionaryPy',         # How you named your package folder (MyLib)
  packages = ['WiktionaryPy'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Wiktionary Dictionary. Enter the word and get opened the Wiktionary url in your default browser.',   # Give a short description about your library
  author = 'Siddharth Tewari',                   # Type in your name
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/siddharth-tewari/WiktionaryPy/archive/v_0.1.tar.gz',    # I explain this later on
  keywords = ['Python Dictionary', 'Wiktionary', 'Dictionary'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
