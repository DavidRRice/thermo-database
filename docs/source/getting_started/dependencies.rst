Dependencies
============

PEARL relies on a small number of widely used scientific Python libraries.
Whenever possible, dependencies are kept to a minimum to simplify installation,
maximize compatibility, and ensure the long-term maintainability of the project.

The complete list of required packages is provided in
``requirements.txt``. This page briefly describes the role of the main
dependencies.

Core dependencies
-----------------

Python
^^^^^^

PEARL requires Python 3.

pandas
^^^^^^

The backend is built around the :mod:`pandas` library. Scientific data,
metadata, and equations of state are represented internally as
:class:`pandas.DataFrame` objects, making it easy to manipulate, filter,
merge, and export tabular data.

matplotlib
^^^^^^^^^^

The :mod:`matplotlib` library is used for generating publication-quality
figures and static visualizations of thermodynamic data and equations of
state.

Additional dependencies
-----------------------

Depending on the functionality used, PEARL may also rely on additional
scientific Python libraries. These are installed automatically through
``requirements.txt`` when required.

Documentation
-------------

The documentation is built using the `Sphinx <https://www.sphinx-doc.org/>`_
documentation generator.

The additional packages required to build the documentation are listed in
``requirements-docs.txt``.

Adding new dependencies
-----------------------

New dependencies should only be introduced when they provide significant
benefits that cannot reasonably be achieved using the existing software
stack.

When proposing a new dependency, developpers are encouraged to consider:

* Is the functionality already available in an existing dependency?
* Is the new package actively maintained?
* Does it introduce a large number of additional dependencies?
* Is it widely used within the scientific Python community?
* Does it improve the maintainability or readability of the code?

Keeping the dependency list small helps ensure that PEARL remains portable,
easy to install, and suitable for long-term scientific use.