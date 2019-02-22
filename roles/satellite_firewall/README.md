Role Name
=========

This Ansible role configures firewall on a server running Satellite 6, and opens ports required by Satellite to function. 
List of ports is taken from Satellite documentation 

https://access.redhat.com/documentation/en-us/red_hat_satellite/6.3/html/installation_guide/preparing_your_environment_for_installation#ports_prerequisites

and from automation-tools available at 

https://github.com/SatelliteQE/automation-tools/blob/master/automation_tools/__init__.py#L623-L664   

Requirements
------------

No requirements are required for this role.

Role Variables
--------------

Requires lists of ports to open in the following wariables:
- *common_ports*
- *satellite_ports*
- *capsule_ports*

Format of the item contained in the port list is as follows:

*\- {proto: '\<protocol\>', port: \<port number\>}*

For example to open the port 22 for TCP:

\- {proto: 'tcp', port: 22}

See the current list of ports to open in the global *vars/satellite_common.yml* file. 

As a Satellite 6 server contains an integrated capsule, we should open both satellite and capsule ports.
A role configuring firewall for a server running only stand-alone capsule should use only *common_ports* and
*capsule_ports* variables.   
  
Dependencies
------------

This role is not dependent upon any galaxy roles.

Example Playbook
----------------

Here is a simple example of satellite_firewall role:

- hosts: localhost
  roles:
    - satellite_firewall

License
-------

 GNU GENERAL PUBLIC LICENSE

    Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc.

Author Information
------------------

This is developed by Satellite QE team, irc: #robottelo on Freenode
