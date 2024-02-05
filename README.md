manage_pip_packages
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

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

```yaml
manage_pip_packages_allow_break_system_packages: false # by default, set to false
```
This variable allow you to pass the `--break_system_packages` to pip.

> **Warning**
> This is not recommended, and is only here if you have no other choice to install packages that aren't supported by the package manager, on distros that enforce the [PEP668](https://peps.python.org/pep-0668/). Chances are you can probably use [manage_pipx_packages](https://github.com/ednz_cloud/manage_pipx_packages) to install packages using pipx, avoiding the potential damages to your system.

Dependencies
------------

`ednz_cloud.manage_apt_packages` to install python3 and pip (if selected).

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.manage_pip_packages
```

```yaml
# calling the role inside a playbook and injecting variables (in another role for example)
- hosts: servers
  tasks:
    - name: "Install ansible with pip"
      ansible.builtin.include_role:
        name: ednz_cloud.manage_pip_packages
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
