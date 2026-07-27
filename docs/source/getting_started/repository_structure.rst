Repository Structure
====================

The PEARL backend is organized into a small number of directories, each
serving a distinct purpose. The repository layout is shown below::

    repository/
    ├── data/
    ├── docs/
    ├── examples/
    ├── modules/
    ├── tests/
    ├── README.md
    ├── requirements.txt
    └── requirements-docs.txt

The purpose of each directory is described in the following sections.

Source code
-----------

The ``modules/`` directory contains the Python source code that implements
the PEARL backend.

Its central component is the :class:`EOSDatabase` class, which provides the
main interface for loading, manipulating, searching, plotting, and exporting
database contents. Additional modules implement specialized functionality,
such as data loading, plotting routines, validation, or utility functions.

Scientific database
-------------------

The ``data/`` directory contains the scientific content of PEARL,
including thermodynamic datasets, equations of state, metadata, and any
associated files required by the backend.

Unlike the Python source code, these files represent the scientific products
distributed with the project. Their organization and format are described in
the User Guide.

Documentation
-------------

The ``docs/`` directory contains the Sphinx documentation.

This documentation is divided into four main sections:

* Getting Started
* User Guide
* Contributor Guide
* Developer Guide

The API Reference is generated automatically from the Python docstrings.

.. Examples
.. --------

.. The ``examples/`` directory contains standalone scripts demonstrating common
.. tasks performed with the PEARL backend.

.. These scripts are intended as practical examples rather than exhaustive
.. documentation.

Tests
-----

The ``tests/`` directory contains the automated test suite used to verify the
correctness and stability of the backend.

New functionality should, whenever possible, be accompanied by corresponding
tests.

Requirements
------------

The repository includes separate requirement files for different purposes.

``requirements.txt``
    Runtime dependencies required to use the backend.

``requirements-docs.txt``
    Additional packages required to build the documentation.

Further Reading
---------------

The following pages describe the repository in more detail:

* :doc:`dependencies`
.. * :doc:`../developer_guide/architecture`
