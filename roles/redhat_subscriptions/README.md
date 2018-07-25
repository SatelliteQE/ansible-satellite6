Ansible Role for Registering and Subscribing content
====================================================

This Ansible role registers and subscribes Satellite6 node with RHN.

Requirements
------------

No Requirements are required for this role.

Role Variables
--------------

Requires redhat_subscriptions_rhsm_username and redhat_subscriptions_rhsm_password to be set if using internal_repo or CDN.

Requires redhat_subscriptions_activation_key and redhat_subscriptions_organization to be set if using internal_ak.

Dependencies
------------

This role is not dependent upon any galaxy roles.

Example Playbook
----------------

Here is a simple example of partitioning-disk role:

- hosts: localhost
  roles:
    - redhat_subscriptions

License
-------

 GNU GENERAL PUBLIC LICENSE

    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.


Author Information
------------------

This is developed by Satellite QE team, irc: #robottelo on Freenode
