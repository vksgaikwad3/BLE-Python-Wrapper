# BLE-Python-Wrapper
Working with Bluetooth Low Energy with Python 

A BLE abstraction layer for Python inspired by pygattlib. Currently only supports Linux, with experimental support for Mac OS X.


## Current Support

1. Discovering devices
2. Reading advertising data
3. Connecting to devices
4. Discovering services, characteristics and descriptors
5. Read from characteristics

## Installation

### Linux

First, install my fork of pygattlib and its dependencies:


```bash
sudo apt-get install libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev
```

You should also make sure that your version of libbluetooth is at least 4.101:

```bash
apt-cache policy libbluetooth-dev | grep Installed
```

Then, clone the repository, and install the python package.

```bash
git clone https://github.com/matthewelse/pygattlib.git
cd pygattlib
sudo python setup.py install
```

This will build the dynamic library, and install the python package.

### Descriptions: 

This python BLE wrapper works with hcitoo and Gatttoolwith the help of [subprocess](http://www.bogotobogo.com/python/python_subprocess_module.php)  module and can perform operations more reliably.


### Useful Functionality

[nRF()](https://github.com/vksgaikwad3/BLE-Python-Wrapper/blob/master/nRFLE.py) is python class, supports parameters which allow you to specify which BLE device to connect to (ignored on OSes other than Linux), how long to sample for, as well as a function which returns a characterstics Read/write responses, allowing you to cherry-pick your devices.


### ToDo :

1. Creating a log of sensor data 
2. Performing a analytics on log files.




