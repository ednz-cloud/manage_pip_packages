"""Role testing files using testinfra."""
from packaging import version


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

def test_pip_installed_latest(host):
    """Validate pip is installed and up-to-date"""
    pip_packages_list = host.pip.get_packages(pip_path='pip')
    pip_outdated_list = host.pip.get_outdated_packages(pip_path='pip')
    assert 'pip' in pip_packages_list
    assert 'pip' not in pip_outdated_list

def test_packages_installed(host):
    """Validate docker, yamllint and vault-cli are installed"""
    pip_packages_list = host.pip.get_packages(pip_path='pip')
    pip_outdated_list = host.pip.get_outdated_packages(pip_path='pip')
    assert 'docker' in pip_packages_list
    assert 'docker' not in  pip_outdated_list
    assert 'yamllint' in pip_packages_list
    assert 'yamllint' in  pip_outdated_list
    assert version.parse(pip_packages_list['yamllint']['version']) == version.parse("1.24")
    assert 'vault-cli' in pip_packages_list
    assert 'vault-cli' in  pip_outdated_list
    assert version.parse(pip_packages_list['vault-cli']['version']) < version.parse("3.1.0")
