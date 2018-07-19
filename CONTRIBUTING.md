Contributing to Ansible-Satellite6
==================================

To contribute to ansible-satellite6, please use pull requests on a branch of your own fork.

After creating your fork on github, you can do:
```
git clone git@github.com:yourname/ansible-satellite6
cd ansible-satellite6
git checkout -b your-branch-name
DO SOME CODING HERE
git add your new files
git commit
git push origin your-branch-name
```
You will then be able to create a pull request from your commit. 

All fixes or new addition to the project should be accompanied by tests that 
should PASS. Run the role/playbook twice, to make sure it's idempotent.

Feel free to raise issues in the repo if you feel a fix or new feature support is needed.

Standards
=========

Install and Run [ansible-lint](https://github.com/willthames/ansible-lint) against your code.

```
ansible-lint playbooks/install/satellite_63.yml
```

Install and Run [ansible-review](https://github.com/willthames/ansible-review) against your code.

```
git ls-files | grep -i yml | xargs ansible-review -d rules/ansible-review/
```

Probably you may also want to run yamllint.

```
git ls-files | grep -i yml | xargs yamllint
```

Some Best Practices
===================

Some Best Practices to follow while writing roles/tasks,

1. Ansible Roles:

   a. Avoid one huge role.

   b. One Role, One Goal.

   c. Avoid various tasks within a role, that are not related.

   d. Use `ansible-galaxy init role_name` to begin with roles.

   e. Following the ansible-galaxy pattern for roles would later help make
      the roles push to ansible-galaxy or make use of the role elsewhere easily

   f. Include/Update the requirements.yml file for any external roles used in
      the project.

   g. Make sure there is a Readme.md file for each role created.

   h. Test/Run the role at-least twice, to make sure it's idempotent.
      (i.e, the role/playbook should not fail upon re-running it for the same
       host.)

2. Ansible Vars:

   a. Set a default value for every variable, they are like examples.

   b. Prefer scalar variables over dictionary type variables as much as
      possible.

3. Use Multi Line YAML notation, instead of key=value

   Vertical code is easier to read and maintain.

4. Use ansible-vault for secret passwords

   Example: Ec2, subscriptions password

5. Always seek out an ansible module first, instead of running a command as
   part of roles/tasks.

   a. If you ever need to use "command", try to make the command module
      idempotent. In order to achieve idempotence, you could use the attributes
      "creates" and "removes".

   b. Avoid shell module as far as possible and should be used only for I/O
      redirect if in case required.

   c. Idempotence: An operation is idempotent if the result of performing it
      once is exactly the same as the result of performing it repeatedly
      without any intervening actions.

6. Have consistency in Naming Convention:

   a. Tasks, playbooks, Variables, Roles and Tags.

   b. Directory Structure/layout.

7. Use handlers while restarting services.

8. Make use of the ansible_variables (i.e facts fetched from host by setup module ) as
   much as possible.
