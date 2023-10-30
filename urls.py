from funcs import read_file


def get_body_from_path(path):
    body = ""  # Better way to do this than to define

    try:
        if path == "/":
            body = read_file("index.html")
        else:  # If
            body = read_file("errors/404.html")

    except Exception as e:

        print(e)
        body = read_file("errors/500.html")

    return bytes(body, 'utf-8')  # String now converted to bytes here


# Please put your own functions here :)


# TODO: Check for errors


# Shorthands:
get_body = get_body_from_path

GB = get_body_from_path
