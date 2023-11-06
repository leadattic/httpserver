import setup

cache = {} # TODO: consider moving variable


def open_file_get_string(path, USE_CACHING=setup.USE_CACHING, file_content=""): # Open file, read file, return string 
    
    if USE_CACHING:
        if path in cache.keys(): # Check if file is in cache
            file_content = cache.get(path)
        else: # Add file to cache
            file = open(setup.FILES_PATH+path, "r", encoding="utf-8")
            file_content = file.read()
            cache[path] = file_content
            file.close()
    else:
        file = open(setup.FILES_PATH+path, "r", encoding="utf-8")
        file_content = file.read()
        file.close()
        print(file_content)

    return file_content


read_file = open_file_get_string # TODO: what alias to use?
