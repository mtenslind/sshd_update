# sshd_update
Script for updating a remote hosts' sshd config from a template config file

This script:

- Gets the applied lines from the template
- Gets existing lines from the remote host
- Applies changes to the remote host

## Requirements

- Paramiko installed
- Access to the remote host
- The destination host user must have passwordless sudo configured

## Usage
```
usage: sshd_update.py [-h] [-c CONFIG_FILE] [-u USER] [-f] host

This script takes an sshd configuration template, compares it agianst the specified remote
host and inserts the differences

positional arguments:
  host                  Remote host to check

options:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config_file CONFIG_FILE
                        configuration file location. Defaults to sshd_config in the current
                        working directory
  -u USER, --user USER  User to use for SSH connection. Defaults to root
  -f, --force           Do not ask for confirmation before applying options
```
