import sys
import os
import pytest
from forms.contact import contact_form
from utilities.footer import footer

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



def test_contact_form():
    # Check if the contact_form function is callable
    assert callable(contact_form)

def test_footer():
    # Check if the footer function is callable
    assert callable(footer)