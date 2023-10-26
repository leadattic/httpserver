import setup



def open_file_get_string(path): # Open file, read file, return string
    file = open(setup.get_files_path()+path, "r")
    file_content = file.read()
    file.close()
    return file_content
read_file = open_file_get_string # TODO: what alias to use?
