Distributable django app boilerplate
====================================

Simple way to make your django app distributable. Can be adapted to work with pure python packages, as well.


Configuration instructions
==========================

In order to fully configure the boilerplate you should edit the following files:

* setup.py
* config.py
* testconf/settings.py
* testconf/urls.py
* run_tests.sh


Edit ``setup.py``
-----------------

You should edit the ``classifiers``.
    
Edit ``config.py``
------------------

Edit everything to match your project
    
Edit ``testconf/settings.py``
-----------------------------

Edit ``INSTALLED_APPS`` and ``TEST_APPS``

Edit ``testconf/urls.py``
-------------------------

Edit the urls to match your django project.
    
Edit ``run_tests.sh``
---------------------

Edit ``OMIT`` and ``SOURCE``. Replace ``your_package`` with the name of your package.

