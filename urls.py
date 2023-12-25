from funcs import read_file
import funcs
import setup

def get_body_from_path(path):
    print(path)
    encoding = "utf-8"  # by defauld encode to utf-8
    body = ""  # Better way to do this than to define
    path = path.split("?")[0]
    paramaters = ""
    try:
        paramaters = path.split("?")
    except Exception:
        print("No paramaters")
    body = "" # Better way to do this than to define

    try:
        if path == "/":
            body = read_file("index.html")
        elif path.startswith("/static/"):
            encoding = funcs.get_static(path)
            fl = open(setup.FILES_PATH + path, encoding=encoding)
            body = fl.read()
            fl.close()
        else:  # If
            body = read_file("errors/404.html")

    except Exception as e:

        print(e)
        body = read_file("errors/500.html")
    print(body)
    print(bytes(body, mode="utf-8"))
    return bytes(body, mode="utf-8")  # encoding now converted to bytes here


# Please put your own functions here :)


# TODO: Check for errors


# Shorthands:
get_body = get_body_from_path

GB = get_body_from_path
