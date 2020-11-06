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

    return argParser.parse_args()

def _main():
    args = _handleArgs()
    
    
    patcher = APKProxyHelper(apk_path=args.apk)
    patcher.patch_apk()

if __name__ == "__main__":
    _main()