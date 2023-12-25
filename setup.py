import os
"""
SETUP
"""

PORT = 80

USE_CACHING = False  # TODO: remove after dev
CACHE_LIMIT = 1024  # The maximum allowed size of cache in MB
CACHE_DISALLOW = []  # Disallowed file extensions (for cache)

FILES_PATH = os.getcwd() + "/files/"

