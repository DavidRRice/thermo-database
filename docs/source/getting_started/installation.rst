Installation
============

This guide describes the minimum steps required to obtain a working copy
of the PEARL backend.

Prerequisites
-------------

PEARL is written in Python and depends primarily on the standard scientific
Python ecosystem. At a minimum, you will need:

* Python 3
* pandas
* matplotlib

Most scientific Python environments already satisfy these requirements.
If you already have a working environment with these packages installed,
you can simply clone the repository and begin using PEARL. In that case,
the sections on creating a virtual environment and installing dependencies
can be skipped.

Obtaining the source code
-------------------------

Clone the repository from GitHub::

    git clone https://github.com/an0wen/thermo-database

Move into the repository::

    cd thermo-database

Creating a virtual environment (recommended)
--------------------------------------------

Although optional, we strongly recommend working inside a dedicated virtual
environment. This avoids version conflicts with other Python projects.

Create a virtual environment::

    python -m venv .venv

Activate it.

On Linux or macOS::

    source .venv/bin/activate

On Windows::

    .venv\Scripts\activate

Installing the dependencies
---------------------------

Install all required Python packages with::

    pip install -r requirements.txt

If you plan to build the documentation locally, also install the
documentation requirements::

    pip install -r requirements-docs.txt

Verifying the installation
--------------------------

Open a Python interpreter from the repository directory and verify that
the main dependencies can be imported::

    >>> import pandas
    >>> import matplotlib

If no errors are reported, your environment is ready to use PEARL.

Next steps
----------

You are now ready to work with the PEARL backend.

Continue with:

* :doc:`repository_structure`
* :doc:`dependencies`
* The User Guide for loading databases and manipulating data.