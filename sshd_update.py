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


def main():
    print(args.host)
    print(args.config_file)
    print(args.user)

main()
