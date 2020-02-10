import json


def openfile(filename):
    f = open(filename, 'r')
    return f


def openjson(filename):
    with open(filename) as json_file:
        return json.load(json_file)
    # j = json.loads(openfile(filename))
    # return j


def exit_method(code, msg=''):
    print(msg)
    exit(code)
