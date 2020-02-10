import argparse
from model.LinuxHost import LinuxHost
from utils.utils import *


def create_parser():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-n', '--name', help="VM name to get JSON from", dest='name', action='store')
    cli_parser.add_argument('-c', help="Count amount of cores", dest='cpu_count', action='store')
    return cli_parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    cli_line = 'export KUBECONFIG=/home/igor/oc4/working/auth/kubeconfig; ' \
               # 'oc login -u kubeadmin -p $(cat ~/oc4/working/auth/kubeadmin-password);'

    # exec_cli(cli_line)

    print(args)
    if args.name:
        cli_line += 'oc get vmi ' + args.name + ' -o json'
    else:
        exit_method(-1, "No VM name was provided")

    cli_result = exec_cli(cli_line)
    # cli_result = clear_string(cli_result, '\n')
    # if args.c:
    #     print(args.c)

    # j = openjson("vm_new.json")
    json_obj = convert_to_json(cli_result)
    print(json_obj)
    myHost = LinuxHost(json_obj)

    print(myHost)
    # print(myHost.volumes_list)

    # print(json.dumps(myHost))
