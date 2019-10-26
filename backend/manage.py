#!/usr/bin/env python
import os
import sys
import logging as log

if __name__ == '__main__':
    logger = log.getLogger('kodan_backend')
    logger.setLevel(log.DEBUG)
    fh = log.FileHandler('kodan.log')
    fh.setLevel(log.DEBUG)
    logger.addHandler(fh)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')
    try:
        from django.core.management import execute_from_command_line
        log.info("Django successfully loaded!")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
