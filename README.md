Manage pip packages
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role enables you to manage python packages on **debian-based** distributions. It can be used on its own , or be called by other roles the install/remove packages on demand.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/manage_pip_packages.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
manage_pip_packages_install_prereqs: true # by default, set to true
```
```yaml
manage_pip_packages_list: # by default, not defined
  - name: nginx
    version_constraint: latest # Leaving empty or setting '' will be considered as latest
    state: absent
  - name: ...
```
This variable is a list of packages, with their name, desired version and state. `version_constraint` can be multiple constraints,separated by commas (example: `>1.10`, `>1.10,<1.15,!=1.12`,`==1.13`).

Dependencies
------------

This role has a task that installs its own dependencies located in `task/prerequisites.yml`, so that you don't need to manage them. This role requires `ednxzu.manage_apt_packages` to install python3 and pip. If you already installed python and pip, you can skip dependencies by setting `manage_pip_packages_install_prereqs` to `false`.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.manage_pip_packages
```

```yaml
# calling the role inside a playbook and injecting variables (in another role for example)
- hosts: servers
  tasks:
    - name: "Install ansible with pip"
      ansible.builtin.include_role:
        name: ednxzu.manage_pip_packages
      vars:
        manage_pip_packages_install_prereqs: false
        manage_pip_packages_list:
          - name: ansible-core
            version_constraint: latest
            state: present
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.