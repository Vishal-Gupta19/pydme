"""
AutoDME - Creating middleware to use Python Bindings provided by pydme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Autodme is a wrapper over pydme infra which can be used as a backend to any front-end applications as well as test automation scripts.
"""

__title__ = 'autodme'
__version__ = '1.0'
__build__ = 1
__author__ = 'Vishal Gupta'


from .core import DeviceConnection
# import pydme.options
# import pydme.filters
