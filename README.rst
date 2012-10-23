Overview
========

Isilon is a storage appliance that can provide block devices on-demand. It can
be controlled via Web interface or command-line via SSH connection. Block
devices are exported via iSCSI.

This nova-volume driver uses SSH connection to Isilon appliance (using Paramiko
library) to issue specific ``isi`` commands to create new block devices and let
compute nodes access them via iSCSI.

Requirements
============

* OpenStack Nova (tested with 2012.1)
* paramiko (as required by nova-volume SAN driver)

Installation
============

Just run ``python setup.py`` or use your favorite Python package manager (like
pip)

Settings
========

* ``volume_driver`` should be ``nova_isilon.IsilonDriver``
* ``san_ip`` should be set to the IP address of your Isilon appliance
* ``san_login`` should be set to the name of user on Isilon appliance that can
  run isi utility and manage LUNs.
* ``san_password`` that user's password
* ``isilon_isi_cmd`` can be set to ``sudo isi`` if your appliance is configured
  to allow user run ``isi`` only with ``sudo``, defaults to ``isi``
* ``isilon_target_iqn_prefix`` a prefix used to build a full IQN from target
  name, should be like ``iqn.2001-07.com.isilon:smth:``

Notes
=====

* https://review.openstack.org/14491 needs to be merged in for the driver to
  work correctly
