Cloud to Server
===============

A small script which will convert your Fedora cloud instance into a Fedora Server instance.
Currently it works Fedora 21 and above.

Usage
------

$ ./cloudtoserver --help
usage: cloudtoserver [-h] [-s]

optional arguments:
  -h, --help    show this help message and exit
  -d, --disable-cloud-service Disable cloud-init service

Remember to pass -d or --disable-cloud-service to disable cloud-init service by default.
