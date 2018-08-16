# ansible-satellite6

Ansible playbooks for Satellite 6 systems' management.

## Setup

### Prerequisities

This repository will be Python3.6 based.

You need Ansible 2.5.0+ installed.

We also recommend to install yamllint, ansible-lint and ansible-review.

### Configuration

Befor running any Satellite6 playbooks,

1. Check and Install dependent roles from ansible galaxy and [mazer](https://galaxy.ansible.com/docs/mazer/install.html), if any

   ```
   # ansible-galaxy install -r requirements.yml
   # mazer install --namespace forklift git+https://github.com/theforeman/forklift
   ```

2. Check and configure required variables in `satellite_common.local.yml`
   by first making a copy of it.
   (i.e RHSM Credentials, Satellite setup links and so on).

   ```
   cp satellite_common.yml satellite_common.local.yml
   ```

3. Make a copy of inventory from inventory.sample file. 

   ```
   # cp inventory.sample inventory
   ```

4. Make sure that SSH Keys are exchanged and placed for the user root.

   ```
   # ssh-copy-id root@sat63-rhel7.example.com
   ```

## Usage

### To Install and configure Satellite6:

```
$ ansible-playbook -i inventory playbooks/install/satellite_63.yml
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/SatelliteQE/ansible-satellite6/blob/master/CONTRIBUTING.md) if you wish to contribute.

## License

ansible-satellite6 is licensed under [GPL version 3](https://github.com/SatelliteQE/ansible-satellite6/blob/master/LICENSE).
