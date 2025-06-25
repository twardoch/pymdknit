__author__ = "jschulz"

__all__ = ["pymdknit", "render"]

from .pymdknit import PyMdKnit


def render(filename, output=None):
    """Convert the filename to the given output format(s).

    Returns
    -------
    converted_docs : list
        List of filenames for the converted documents

    """
    kp = PyMdKnit()
    return kp.render(filename, output=output)
