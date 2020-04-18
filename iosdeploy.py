#!/usr/bin/env python3

import os, errno, sys, subprocess, shutil, argparse

script_directory = os.path.dirname(os.path.relpath(__file__))
root_directory = os.path.abspath(os.path.join(script_directory, os.pardir))
build_directory = os.path.join(root_directory, 'build')


def is_ios_deploy_installed():
    cmd = ['ios-deploy', '--version', 'tail', '-f', '/tmp/file']
    from subprocess import Popen, PIPE, STDOUT
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    count = 0

    for line in p.stdout:
        count = count+1

    if count == 0:
        print('Please install ios-deploy, use \'brew install ios-deploy\' to install')


def install_app(app_path):
    # ios-deploy --justlaunch --debug --bundle app_path --no-wifi
    fullPath = "/" + app_path
    cmd = ['ios-deploy', '--justlaunch', '--debug', '--bundle', fullPath, '--no-wifi']
    ret = perform_action(cmd)
    print("Install Application: " + str(ret))
    return ret


def uninstall_app(app_id):
    # ios-deploy --uninstall_only --bundle_id appId
    cmd = ['ios-deploy', '--uninstall_only', '--bundle_id', app_id, '--no-wifi']
    ret = perform_action(cmd)
    print("Un-installation of App : " + str(ret))
    return ret


def dump_document_dir(app_id, destination_dir):
    # ios-deploy --bundle_id appId --download --to destination_dir
    fullPath = "/" + destination_dir
    cmd = ['ios-deploy', '--bundle_id', app_id, '--download', '--to', fullPath, '--no-wifi']
    ret = perform_action(cmd)
    print("Dump Container: " + str(ret))
    return ret


def is_app_installed(app_id):
    cmd = ['ios-deploy', "--exists", "--bundle_id", app_id]
    ret = perform_action(cmd)
    return ret


def perform_action(cmd):
    ios_deploy_log = 'ios-deploy.log'
    from subprocess import Popen, PIPE, STDOUT
    logfile = open(ios_deploy_log, "w")
    p = Popen(cmd, shell=False, universal_newlines=True, stdout=logfile, stderr=STDOUT)
    ret_code = p.wait()
    logfile.flush()
    return ret_code

#
# def parseArguments():
#     p = argparse.ArgumentParser(description='Pass Args')
#     p.add_argument('-install', type=str, help="install app")
#     p.add_argument('-uninstall', type=str, help='app id')
#
#     return p.parse_args()
#
#
# def main():
#
#     install_app("AWBrowser.ipa")
#     #uninstall_app("com.air-watch.secure.browser")
#     # arg = parseArguments()
#     #
#     # if arg.install:
#     #     app_path = arg.install
#     #     install_app(app_path)
#     #
#     # if arg.uninstall:
#     #     app_id = arg.uninstall
#     #     uninstall_app(app_id)
#
#
# # Entry point
# if __name__ == "__main__":
#     main()
