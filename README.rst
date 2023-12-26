fake_flames
============
This repository collects code used in the SFH analysis of FIRE data

Data
----
The original FIRE data used in this analysis can be found at the following URL::

    www.insert.actual.url.here


Installation
------------
To install fake_flames into your environment from the source code::

    $ cd /path/to/root/fake_flames
    $ pip install .


Testing
-------
To run the suite of unit tests::

    $ cd /path/to/root/fake_flames
    $ pytest

To build html of test coverage::

    $ pytest -v --cov --cov-report html
    $ open htmlcov/index.html

