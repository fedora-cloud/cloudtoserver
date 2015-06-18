Cloud to Server
===============

A small script which will convert your Fedora cloud instance into a Fedora Server instance. It works on Fedora 21 and above.


Usage
------

$ ./cloudtoserver --help
usage: cloudtoserver [-h] [-d] [-v] [-y]

optional arguments:
    -h, --help    show this help message and exit
    -d, --disable-cloud-service
                          Disable cloud-init service
    -v, --version         Prints the version of the tool
    -y, --no-confirm      Do not prompt for confirmation

Remember to pass -d or --disable-cloud-service to disable cloud-init service by default.
