# pkg_stats
Util to download contents index from Debian mirror and display statistics.

## install
This was developed using Python 3.7.2
```
virtualenv -p python3 env
source env/bin/activate
```
This was implemented in pure Python. No need to install deps.

## Usage

```
python package_statistics (arch_type)
```
Where `arch_type` is one of:

* amd64
* arm64
* armel
* armhf
* i386
* mips
* mips64el
* mipsel
* ppc64el
* s390x

This will download the contents file in to your current working directory. If
the file already exists, downloading will be skipped and parsing will happen
immediately.

## tests

You can run the tests from the root dir as follows:

```
pip install nose
...
nosetests
```
