#!python3
"""
    Writes .csv file for SLiM 1D stepping-stone model with parameters
    for symmetric migration between demes.
"""

import numpy as np
import csv
# import sys
import click

@click.command()
@click.option('--numdemes', default = 1, help = 'Number of demes to simulate')
@click.option('--demepopsize', default = 0, help = 'Number of individuals within each deme')
@click.option('--m', default = 0.0, help = 'Symmetric migration rate across demes')
@click.option('--mu',default = 0.0, help = 'Symmetric mutation rate')
@click.option('--s',default = 0.0, help = 'Selection coefficient')
@click.option('--label',default = '',help = 'Identifier label for filenames')
@click.option('--out',default = '',help = 'OUTPUT')

def migcsvwriter(numdemes, demepopsize, m, mu, s, label, out):
    paramstring = (("// , %s, %s, %s, %s, numdemes, demempopsize, mu, s\n")%(numdemes,demepopsize,mu,s))
    # Nearest-neighbor migration in forwards direction
    migmat = np.diag(np.ones(numdemes-1),1)
    # Periodic boundary conditions
    migmat[0,-1] = 1
    # Nearest-neighbor migration in backwards direction
    migmat += migmat.T
    #Get source and destination indices and convert to base 1
    migposs = np.where(migmat != 0)
    srcposs = migposs[0] + 1
    destposs = migposs[1] + 1
    with open(out, 'w', newline='') as csvfile:
        csvfile.write(paramstring)
        fieldnames = ['<src>', '<dest>','<m>']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if numdemes > 2:
            for source,dest in zip(srcposs,destposs):
                writer.writerow({fieldnames[0]: source, fieldnames[1]: dest,fieldnames[2]: str(m)})
        # For case when numdemes =< 2, removes redundancy in dictionary
        else:
            for i in np.arange(numdemes):
                writer.writerow({fieldnames[0]: srcposs[i], fieldnames[1]: destposs[i],fieldnames[2]: str(m)})

if __name__ == '__main__':
    migcsvwriter()
