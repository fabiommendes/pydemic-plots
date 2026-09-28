.. warning::

   This repository is archived. It was part of a COVID-19 modelling project (2020–2022), now concluded. Archived for reference.

=============
Pydemic plots
=============

Re-usable plot functions for Pydemic projects. Some functions are fairly generic (e.g., population
pyramid plots) and hence there is a chance other projects will find something useful here too.

Usage
=====

Install it using ``pip install pydemic-plots`` or your method of choice. Import the
plot provider you want and get to work!

>>> from pydemic_plots import mpl as plt  # drop-in replacement for matplotlib.pyplot
>>> plt.population_pyramid(data)
>>> plt.title("Population pyramid")
>>> plt.show()