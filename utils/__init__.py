import os
import sys

def getToken() -> str:
    if not os.path.isfile("token"):
        print("No token file found. Provide one or supply the token using the -t flag.", file=sys.stderr)
        sys.exit(1)

    with open("token", "r") as f:
        token = f.read().strip()

    return token
