import setup
import sys

cache = {}  # TODO: consider moving variable


def open_file_get_string(path, use_caching=setup.USE_CACHING, file_content=""):  # Open file, read file, return string

    if use_caching:
        if path in cache.keys():  # Check if file is in cache
            file_content = cache.get(path)
        else:  # Add file to cache
            file = open(setup.FILES_PATH + path, "r")
            file_content = file.read()
            print(path.split(".")[::-1][0])
            if not path.split(".")[::-1][0] in setup.CACHE_DISALLOW and sys.getsizeof(cache) + len(file_content.encode('utf-8')) <= setup.CACHE_LIMIT * 1000000:  # TODO: make sure all math and funcs are correct
                cache[path] = file_content

            file.close()
    else:
        file = open(setup.FILES_PATH + path, "r")
        file_content = file.read()
        file.close()

    return file_content


read_file = open_file_get_string  # TODO: what alias to use?
