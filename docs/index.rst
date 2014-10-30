.. IEPY documentation master file, created by
   sphinx-quickstart on Wed Apr 23 20:02:15 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to IEPY's documentation!
================================

IEPY is an open source tool for
`Information Extraction <http://en.wikipedia.org/wiki/Information_extraction>`_
focused on Relation Extraction.

To give an example of Relation Extraction, if we are trying to find a
birth date in:

    `"John von Neumann (December 28, 1903 – February 8, 1957) was a Hungarian and
    American pure and applied mathematician, physicist, inventor and polymath."`

then IEPY's task is to identify "``John von Neumann``" and
"``December 28, 1903``" as the subject and object entities of the "``was born in``"
relation.

It's aimed at:
    - `users <http://iepy.readthedocs.org/en/latest/active_learning_tutorial.html>`_
      needing to perform Information Extraction on a large dataset.
    - `scientists <http://iepy.readthedocs.org/en/latest/how_to_hack.html>`_
      wanting to experiment with new IE algorithms.

Features
--------

    - `A corpus annotation tool <http://iepy.readthedocs.org/en/latest/corpus_labeling.html>`_
      with a `web-based UI <http://iepy.readthedocs.org/en/latest/corpus_labeling.html#document-based-labeling>`_
    - `An active learning relation extraction tool <http://iepy.readthedocs.org/en/latest/active_learning_tutorial.html>`_
      pre-configured with convenient defaults.
    - `A rule based relation extraction tool <http://iepy.readthedocs.org/en/latest/rules_tutorial.html>`_
      for cases where the documents are semi-structured or high precision is required.
    - A web-based user interface that:
        - Allows layman users to control some aspects of IEPY.
        - Allows decentralization of human input.
    - A shallow entity ontology with coreference resolution via `Stanford CoreNLP <http://nlp.stanford.edu/software/corenlp.shtml>`_
    - `An easily hack-able active learning core <http://iepy.readthedocs.org/en/latest/how_to_hack.html>`_,
      ideal for scientist wanting to experiment with new algorithms.


Contents:
---------

.. toctree::
   :maxdepth: 2

   installation
   tutorial
   instantiation
   active_learning_tutorial
   rules_tutorial
   preprocess
   corpus_labeling


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

