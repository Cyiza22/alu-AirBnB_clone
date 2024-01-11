#!/usr/bin/python3
"""This is the initi file for the models directory"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
