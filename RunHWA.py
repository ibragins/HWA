import argparse
from model.LinuxHost import LinuxHost
from utils.utils import *


def create_parser():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-n', '--name', help="VM name to get JSON from", dest='name', action='store')
    cli_parser.add_argument('-c', help="Count amount of cores", dest='string', action='store')
    return cli_parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    print(args)
    if args.name:
        pass
    else:
        exit_method(-1, "No VM name was provided")
    # if args.c:
    #     print(args.c)

    j = openjson("vm_new.json")
    myHost = LinuxHost(j)

    print(myHost)
    # print(myHost.volumes_list)

    # print(json.dumps(myHost))
