import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

from allauth_bs import __version__


class Tox(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


TESTS_REQUIRE = ['tox >= 2.3']


setup(
    name='django-allauth-bs',
    version=__version__,
    author='InQuant GmbH',
    author_email='info@inquant.de',
    packages=['allauth_bs'],
    url='https://github.com/InQuant/django-allauth-bs',
    license='MIT',
    description='Bootstrap forms for allauth',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.md'], },
    install_requires=['django', 'django-allauth'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    tests_require=TESTS_REQUIRE,
    extras_require={
        'test': TESTS_REQUIRE,
    },
    cmdclass={'test': Tox}
)