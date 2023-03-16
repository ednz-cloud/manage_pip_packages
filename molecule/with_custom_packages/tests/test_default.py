"""Role testing files using testinfra."""
import json

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_python_pip_packages_installed(host):
    """Validate python3 and pip are installed"""
    apt_package_python3 = host.package("python3")
    apt_package_pip = host.package("python3-pip")
    assert apt_package_python3.is_installed
    assert apt_package_pip.is_installed

def test_packages_not_installed(host):
    """Validate vim is installed"""
    pip_packages_list = host.pip_package.get_packages(pip_path='pip')
    assert pip_packages_list['pip']
    assert pip_packages_list['docker']
    assert pip_packages_list['zeubi']
    print(pip_packages_list)

