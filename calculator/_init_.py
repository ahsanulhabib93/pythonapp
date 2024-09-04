# mypackage/__init__.py

# Importing specific functions or classes to be accessible at the package level
from .module import some_function, SomeClass

# Defining what is publicly available in the package namespace
__all__ = ['some_function', 'SomeClass']
