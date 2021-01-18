#!/usr/bin/env python
import os
import sys
import pickle
from utils import text_process


def importPipelines():
    pipeline = pickle.load(open('textClf.pkl', 'rb'))

    return pipeline


if __name__ == '__main__':
    pipeline = importPipelines()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spamdetection.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
