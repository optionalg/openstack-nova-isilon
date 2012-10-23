import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(name="openstack-nova-isilon",
      version="0.1",
      description='Isilon volume driver for OpenStack Nova',
      long_description=README,
      py_modules=["nova_isilon"],
      test_suite="nose.collector",
      install_requires=[
          "nova", "paramiko",
      ],
)

