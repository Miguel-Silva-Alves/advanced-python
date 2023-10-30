import sys

def receving_parameters(args: list, keywords: list):
    dic = {}
    for key in keywords:
        dic[key] = args[args.index(key) + 1] if key in args else None
    return dic

#opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])

args = sys.argv[1:]
keywords = ["-f", "-m"]

print(receving_parameters(args, keywords))
