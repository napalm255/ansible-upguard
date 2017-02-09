#!/usr/bin/env bash

# EPEL required for 'sshpass'
yum install -y epel-release

# Required packages for development, ansible, pip, build paramiko/cryptography
yum install -y \
  git vim \
  sshpass libselinux-python \
  python-setuptools python-devel \
  gcc libffi-devel openssl-devel \
  man bind-utils mlocate

# Clean up yum
yum clean -y all

# Install latest pip
easy_install pip

# Install python requirements
pip install -r /vagrant/requirements_dev.txt

# Touch known_hosts of vagrant user
# NOTE: Found weird bug where ansible ssh fails
#       without known_hosts existing.
su - vagrant -c "touch /home/vagrant/.ssh/known_hosts"

# clone ansible-devel
echo "Setting up ansible-devel:"
su - vagrant -c "rm -Rf /home/vagrant/ansible-devel"
su - vagrant -c "git clone https://github.com/ansible/ansible.git /home/vagrant/ansible-devel"
su - vagrant -c "mkdir -p /home/vagrant/ansible-devel/lib/ansible/modules/custom"
su - vagrant -c "ln -s /vagrant/library/* /home/vagrant/ansible-devel/lib/ansible/modules/custom"

# Update mlocate database
updatedb

# Output installed python packages
echo "Installed Python Packages:"
python --version
pip list --format=columns

# End bootstrap
echo "Bootstrap Complete!"
