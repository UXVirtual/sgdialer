__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

# must wrap setup.py in this if statement or sphinx-build will throw errors as it tries to read setup.py
if __name__ == "__main__":

    from distutils.core import setup
    setup(name='sgdialer',
          version='1.0',
          packages=['sgdialer','co.hazardmedia.sgdialer']
          )