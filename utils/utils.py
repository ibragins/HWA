import json
import os
import re


def openfile(filename):
    f = open(filename, 'r')
    return f


def open_json(filename):
    with open(filename) as json_file:
        try:
            return json.load(json_file)
        except:
            return None
    # j = json.loads(openfile(filename))
    # return j


def convert_to_json(json_obj):
    try:
        return json.loads(json_obj)
    except:
        exit_method(-1, 'Json not loaded!')
        return None


def exit_method(code, msg=''):
    print(msg)
    exit(code)


def exec_cli(cli):
    stream = os.popen(cli)
    return stream.read()


def clear_string(string, mask):
    string = re.sub(mask, '', string)
    return string
