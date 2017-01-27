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
su vagrant -c "touch /home/vagrant/.ssh/known_hosts"

# Update mlocate database
updatedb

# Output installed python packages
echo "Installed Python Packages:"
pip freeze

# End bootstrap
echo "Bootstrap Complete!"
