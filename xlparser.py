#!/usr/bin/python3

import sys
import json
import pandas as pd

SRC = "source"
TRG = "target"

## Program Path
args = sys.argv
if(len(args) < 2):
    print("No Excel Path Given.")
    exit()

path = args[1]
outfile = args[2]

def write_out(data, of=outfile, mode="w+"):
    with open(of, mode) as fp:
        json.dump(data, fp)
    return

def main():
    df 		= pd.read_excel(path)
    bams 	= df[TRG.capitalize()]
    fr 		= df[SRC.capitalize()]

    mlen 	= min(len(bams), len(fr))

    out_dict = {}

    for i in range(mlen):
        frline = str(fr[i]).replace('\n', '').strip()
        bmline = str(bams[i]).replace('\n', '').strip()
        out_dict[i] = {
            "fr": frline,
            "bam": bmline
        }

    write_out(out_dict, outfile)

if __name__ == "__main__":
    main()

