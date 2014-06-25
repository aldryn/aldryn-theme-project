=================
{{ PROJECTNAME }}
=================


Setup
=====

#. run ``make install`` to initialize
#. run ``make pulldata SOURCE=live`` to download and load the **live** database (optional)


Running
=======

.. NOTE:: make sure the requirements from "Installation" below are installed before compiling css.

#. run ``make all`` to run the local server and compile css

OR

#. run ``make run`` to start the local server
#. run ``make run PORT=8001`` run on a separate port
#. open ``http://localhost:8000`` in a browser to view the project
#. run ``make css`` to watch and compile css on the fly


Maintanance
===========

#. run ``make update`` to regularily update
#. run ``make update BRANCH=master`` to update from a different branch
#. run ``make update UPGRADE=true`` to force --upgrade


Installation
============

Please make sure you have the following packages installed:

#. sass: ``sudo gem install sass -v '>=3.3.0alpha' --pre``
#. compass: ``sudo gem install compass -v '>=1.0.0alpha' --pre``
#. bootstrap: ``sudo gem install bootstrap-sass``
#. node.js, npm, gupl from **osx-bootstrap** together with the core setup