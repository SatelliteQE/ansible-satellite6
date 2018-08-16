Ansible Role for Enabling FIPS
==============================

This Ansible role downloads and runs a script apply a set of patches for installing Satellite on a FIPS-enabled machine.

Requirements
------------

No Requirements are required for this role.

Role Variables
--------------

fips_script: link to workaround script for installing FIPS

Dependencies
------------

This role is not dependent upon any galaxy roles.

Example Playbook
----------------

Here is a simple example of fips_workaround role:

- hosts: localhost
  remote_user: root
  roles:
    - fips_workaround

License
-------

 GNU GENERAL PUBLIC LICENSE

    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.


Author Information
------------------

This is developed by Satellite QE team, irc: #robottelo on Freenode
