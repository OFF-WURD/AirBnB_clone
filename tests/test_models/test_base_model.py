#!/usr/bin/python3
"""Test for required behaviour and documentation"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__

if __name__ == '__main__':
    unittest.main()
