from setuptools import setup, find_packages


setup(
    name='fsm_effective_stress',
    version='1.0.0',
    url='https://github.com/petarmaric/fsm_effective_stress',
    license='BSD',
    author='Petar Maric',
    author_email='petarmaric@uns.ac.rs',
    description='Python library that uses the rheological-dynamical analogy '\
                '(RDA) to compute damage and effective buckling stress in '\
                'prismatic shell structures.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    platforms='any',
    py_modules=['fsm_effective_stress'],
)
