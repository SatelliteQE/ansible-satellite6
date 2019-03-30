Ansible Role for Configuring NTP using chrony
==================================

This Ansible role installs the chrony and ensures desired configuration.

Requirements
------------

No Requirements are required for this role.

Role Variables
--------------

No variables required for this role.

Dependencies
------------

This role is dependent on Galaxy oasis-roles.chrony role.

Example Playbook
----------------

Here is a simple example of chrony role:

- hosts: localhost
  remote_user: root
  roles:
    - chrony

License
-------

 GNU GENERAL PUBLIC LICENSE

    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.


Author Information
------------------

This is developed by Satellite QE team, irc: #robottelo on Freenode
