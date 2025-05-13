#!/usr/bin/env python

import argparse
import os
import paramiko
import getpass

parser = argparse.ArgumentParser(
    prog="sshd_update.py",
    description="This script takes an sshd configuration template, compares it agianst the specified remote host and inserts the differences"
)

parser.add_argument(
    "host",
    help="Remote host to check"
)
parser.add_argument(
    "-c",
    "--config_file",
    help="configuration file location. Defaults to sshd_config in the current working directory",
    default=os.getcwd() + "/sshd_config",
)
parser.add_argument(
    "-u",
    "--user",
    help="User to use for SSH connection. Defaults to root",
    default="root"
)
parser.add_argument(
    "-f",
    "--force",
    help="Do not ask for confirmation before applying options",
    action="store_true"
)

args = parser.parse_args()

def parse_config_array(config_array):
    # Parses out commented lines and empty newlines
    parsed_list = [i for i in config_array if not(i.startswith("#")) and i != "\n"]
    return parsed_list

def paramiko_connect(host, user):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    try:
        client.connect(host, port=22, username=user)
    except:
        user_password = getpass.getpass(f"Key failed, insert password for {user}: ")
        client.connect(host, port=22, username=user, password=user_password)
    return client

def main():
    with open(args.config_file, 'r') as template_file:
        local_parameter_list = template_file.readlines()

    local_parsed_list = parse_config_array(local_parameter_list)

    connection = paramiko_connect(args.host, args.user)
    sftp = paramiko.SFTPClient.from_transport(connection.get_transport())
    with sftp.open("/etc/ssh/sshd_config") as host_sshd:
        remote_parameter_list = host_sshd.readlines()
    sftp.close()

    remote_parsed_list = parse_config_array(remote_parameter_list)

    applicable_options = []

    for setting in local_parsed_list:
        if setting not in remote_parsed_list:
            print(f"The line '{setting[:-1]}' not found on the remote host")
            if not args.force:
                confirmation = input("Confirm? [Y/N] ")
                if confirmation.lower() in ('y', 'yes'):
                    applicable_options.append(setting)
            else: applicable_options.append(setting)

    if not applicable_options:
        print("No options to apply")
    else:
        print("Applying options")
        for option in applicable_options:
            cmd = f"echo {option[:-1]} >> /etc/ssh/sshd_config"
            (stdin, stdout, err) = connection.exec_command(cmd)

    connection.close()

main()
