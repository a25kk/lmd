# buildout

## Plone Site Landmetzgerei Dichtl

* `Source code @ GitHub <https://github.com/a25kk/lmd>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/lmd>`_
* `Documentation @ ReadTheDocs <http://lmd.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/kreativkombinat/lmd>`_

## How it works

This project templates provides a full blown Plone project environment. It comes with a preconfigured project specific theme package located under the _src_ directory.

## Installation

This buildout is intended to be used via the development profile to provide
a ready to work on setup. To get started with a new development environment
clone the buildout to your local machine and initialize the buildout:

``` bash
$ git clone git@github.com:username/lmd.git
$ cd ./lmd
$ virtualenv-2.7 .
$ ./bin/pip install zc.buildout
$ bin/buildout -Nc development.cfg
```

## Configuration

The generated buildout asumes that the developer has setup a local egg cache and therefore provides a buildout 'default.cfg' containing:

``` ini
[buildout]
eggs-directory      = /home/yourusername/.buildout/eggs
download-cache      = /home/yourusername/.buildout/downloads
extends-cache       = /home/yourusername/.buildout/extends

socket-timeout      = 3

[fabric]
username            = yourusername
```
