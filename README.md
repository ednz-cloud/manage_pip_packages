# **Manage pip packages**

This role enables you to manage python packages on **debian-based** distributions. It can be used on its own , or be called by other roles the install/remove packages on demand.

## **Requirements**

None.

## **Role Variables**

```yaml
manage_pip_packages_install_prereqs: true
```

Whether or not the role should install the necessary dependencies to function correctly (python3, python3-pip, python3-venv if installing in a venv).This requires the [ednz_cloud.manage_apt_packages](https://github.com/ednz-cloud/manage_apt_packages) to also be installed.

```yaml
manage_pip_packages_list:
  - name: nginx
    version_constraint: latest
    state: absent
  - name: ...
```

A list of packages, with their name, desired version and state. `version_constraint` can be multiple constraints,separated by commas (example: `>1.10`, `>1.10,<1.15,!=1.12`,`==1.13`).

```yaml
manage_pip_packages_break_system_packages: false
```

This variable allow you to pass the `--break-system-packages` option to pip.

> **Warning**
> This is not recommended, and is only here if you have no other choice to install packages that aren't supported by the package manager, on distros that enforce the [PEP668](https://peps.python.org/pep-0668/). Chances are you can probably installyour packages in virtual environments, avoiding the potential damages to your system.

```yaml
manage_pip_packages_create_venv: false
```

Whether to install the packages in a virtual environment (will be created if it does not exist)

```yaml
manage_pip_packages_venv_path: /tmp/venv
```

The path to the virtual environment if using one.

```yaml
manage_pip_packages_venv_inherit_global: false
```

Whether the virtual environment should inherit global system packages.

## **Dependencies**

`ednz_cloud.manage_apt_packages` to install python3, python3-pip, and python3-venv (if selected).

## **Example Playbook**

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

## **License**

MIT / BSD

## **Author Information**

This role was created by Bertrand Lanson in 2023.
