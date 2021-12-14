import sys
import os

# Exists to make importing from parent directory easier.
def config_parent_import():
    current = os.path.dirname(os.path.realpath(__file__))

    parent = os.path.dirname(current)

    sys.path.append(parent)