import argparse
import pathlib
import sys
import os
# import numpy as np
#
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Provide source and destination paths.")
#     else:
#         arg1, arg2 = sys.argv[1], sys.argv[2]
#         print(arg1, arg2)


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", type=pathlib.Path, required=True, help="provide image for ocr")
parser.add_argument("-o", "--output", type=pathlib.Path, required=True, help="output text file to save ocred text.")
args = parser.parse_args()

if args.input and args.output:
    if os.path.isfile(args.input) and os.path.isfile(args.output):
        print(args.input, args.output)
    else:
        print("Provide input and output files. The paths you provide has issues.")
else:
    print("please provide input image and output text file.")
