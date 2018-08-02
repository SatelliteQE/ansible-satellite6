Ansible Role for updating OS packages. 
================================================

This Ansible role for updating OS packages.

Requirements
------------

No Requirements are required for this role.

Role Variables
--------------

No Variables required for this role.

Dependencies
------------

This role is not dependent upon any galaxy roles.

Example Playbook
----------------

Here is a simple example of install_satellite6 role:

- hosts: localhost
  roles:
    - redhat_subscriptions
    - satellite6_repositories
    - update_os_packages

License
-------

 GNU GENERAL PUBLIC LICENSE

    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.


Author Information
------------------

This is developed by Satellite QE team, irc: #robottelo on Freenode
