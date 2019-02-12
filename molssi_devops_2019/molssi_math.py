"""
molssi_math.py
A sample repo for the 2019 MolSSI Software Fellows Bootcamp.

Handles the primary functions
"""
import numpy

def mean(numlist):
    """
    Computes the mean of a list of numbers

    """
    # Check to see that input is type numlis
    if not isinstance(numlist, list):
        raise TypeError('Invalid input must be type list.')

    if len(numlist) == 0:
        raise ZeroDivisionError('Cannot calculate the mean of an empty list.')

    total = 0
    for num in numlist:
        total = total + num
    average = total/len(numlist)
    return average


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
