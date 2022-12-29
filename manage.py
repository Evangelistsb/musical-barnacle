#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import filesystem
import sysadmin
import utils


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def tracker():
    if utils[0].length > 0:
        

if __name__ == '__main__':
    main()
