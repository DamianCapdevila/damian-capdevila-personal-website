import sys
import os
import pytest
from forms.contact import contact_form
from utilities.helper import footer

def test_contact_form():
    assert callable(contact_form)

def test_footer():
    assert callable(footer)