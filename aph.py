#
#
#
#
#

import argparse
from APKProxyHelper import *

def _handleArgs():
    argParser = argparse.ArgumentParser(prog="APKProxyHelper")
    argParser.add_argument("--apk", "-a", help="The path to the apk file", required=True)
    argParser.add_argument("--apktool", "-atv", help="apktool version 2.4.1 or 2.5.0", default="2.4.1")

    return argParser.parse_args()

def _main():
    args = _handleArgs()
    
    patcher = APKProxyHelper(apk_path=args.apk, apktool_version=args.apktool)
    patcher.patch_apk()

if __name__ == "__main__":
    _main()