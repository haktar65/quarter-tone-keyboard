"""Transaction helpers for commands that change a FreeCAD document."""

from contextlib import contextmanager
from functools import wraps

import FreeCAD as App


def get_document(document=None):
    """Return an explicit document or the current active document."""
    document = document or App.ActiveDocument
    if document is None:
        raise RuntimeError("No active FreeCAD document.")
    return document


@contextmanager
def transaction(name, document=None, recompute=True):
    """Run document changes as one undoable FreeCAD transaction."""
    document = get_document(document)
    document.openTransaction(name)
    try:
        yield document
        if recompute:
            document.recompute()
    except Exception:
        document.abortTransaction()
        raise
    else:
        document.commitTransaction()


def transactional(name=None, recompute=True):
    """Decorate a command with a transaction and final recompute.

    Decorated functions must accept ``document=None`` as a keyword argument.
    """
    def decorator(function):
        transaction_name = name or function.__name__

        @wraps(function)
        def wrapped(*args, **kwargs):
            document = get_document(kwargs.get("document"))
            kwargs["document"] = document
            with transaction(transaction_name, document, recompute=recompute):
                return function(*args, **kwargs)

        return wrapped

    return decorator