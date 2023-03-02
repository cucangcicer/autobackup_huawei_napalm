# autobackup_huawei_napalm

This is huawei autobackup configuration using napalm. There are some requirement you have to build in your environment;

Python: Python 3
Python Module;
- napalm
- napalm-huawei-vrp
- ncclient

I recomend to you install those modules in the virtualenv.

There are two files and 1 file folder in this repo. The autobackup_huawei_napalm.py is the main application, which you can specify your host information there. The device_list is your device list, which you can use ip/hostname to define your host. The Backup folder is where your backup file placed.
Ty.
