#!/usr/bin/env python

import argparse
import os

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

args = parser.parse_args()

def parse_config_array(config_array):
    # Parses out commented lines and empty newlines
    parsed_list = [i for i in config_array if not(i.startswith("#")) and i != "\n"]
    return parsed_list

def main():
    with open(args.config_file, 'r') as template_file:
        parameter_list = template_file.readlines()

    parsed_list = parse_config_array(parameter_list)

    print(parsed_list)

main()
