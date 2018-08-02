Ansible Role for Registering and Subscribing content
====================================================

This Ansible role manages disabling and enabling of repositories for Satellite6.

Requirements
------------

No Requirements are required for this role.

Role Variables
--------------

Requires satellite_distribution to be set.
The valid values for satellite_distribution are internal_repo, internal_ak and cdn.

Requires satellite_version value correctly set.

Requires satellite6_repositories_satellite_reponame and satellite6_repositories_satellite_repourl to be set, if using internal_repo.

Dependencies
------------

This role is not dependent upon any galaxy roles.

Example Playbook
----------------

Here is a simple example of satellite6_repositories role:

- hosts: localhost
  roles:
    - redhat_subscriptions
    - satellite6_repositories

License
-------

 GNU GENERAL PUBLIC LICENSE

    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.


Author Information
------------------

This is developed by Satellite QE team, irc: #robottelo on Freenode
