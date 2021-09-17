===============
brightway-olca
===============


A small library that connects brightway to the openLCA IPC Server.

Installation
============

Install this library from github using

    pip install git+https://github.com/brightway-lca/brightway-olca.git

Setup
=====

In order to use this library, [openLCA](https://www.openlca.org/) needs to be running and the openLCA IPC Server needs to be active.
The server can be activated in openLCA under Tools>Developer Tools>IPC Server.

Usage
=====

This library exposes the `OLCAClient` class that can be used to read the database currently opened in openLCA.

    get_olca_database_by_type(exchange_types: ExchangeType)

This method returns a list of exchanges by type that can be used for integration of the openLCA database into brightway.

Example usage:

    from bw_olca import olca_client
    
    from bw_olca.exchange_types import ExchangeType


    client = olca_cilent.OLCAClient()
    
    types_list = [ExchangeType.PROCESS]
    
    results = client.get_olca_database_by_type(types_list, verbose=True)


Use the Example Notebook in the docs folder for an in-depth example of how to use this library.

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.0.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
