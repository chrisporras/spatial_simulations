#!python3
"""
    Parses SLiM time series output into .csv format
"""
import numpy as np
import click

@click.command()
@click.option('--slimoutputfile',default = '',help = 'SLiM output file')
@click.option('--out',default = '',help = 'Parsed .csv output')

def timeseries_parser(slimoutputfile, out):
    numdemes = int(slimoutputfile.split("numdemes_")[1].split("_")[0])
    with open(slimoutputfile) as input_data:
        freqvec =[]
        valueline = 0
        for line in input_data:
            # Skips text before the beginning of the genomes block:
            if len(line.split(": ")) > 1 :
                if line.split(": ")[0] != "#Elapsed time":
                    valueline = 1
                    continue
            # Collect total mutation freqs from input_data and append to freqvec
            if valueline == 1:
                freqslist = line.split()
                freq = []
                if "float(0)" in freqslist:
                    # Convert str to float
                    if len(freqslist) == 1:
                        freq = float(0)
                    else:
                        # Bad line crash and burn
                        print("Warning bad line:")
                        print(freqslist)
                        exit(1)
                else:
                    freq = np.sum([float(i) for i in freqslist],axis=0)
                freqvec.append(freq)
                valueline = 0
    # Reshape freqvec into matrix indexed by time and deme
    freqmat = np.reshape(freqvec,((len(freqvec)//numdemes,numdemes)))
    # Write freqmat as .csv
    np.savetxt(out, freqmat, delimiter=",")

if __name__ == "__main__":
    timeseries_parser()
