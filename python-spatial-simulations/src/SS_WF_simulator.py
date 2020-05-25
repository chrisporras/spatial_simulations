#!python3
"""
    Simulates a Wright-Fisher process in a Stepping-Stone
    spatial lattice. Takes the following parameters:
"""
import numpy as np
import click
from scipy.ndimage.filters import laplace

@click.command()
@click.option('--pop_size', default = 1e3, help = 'Number of individuals within each deme')
@click.option('--mu',default = 1e-5, help = 'Symmetric mutation rate')
@click.option('--s',default = 1e-2, help = 'Selection coefficient')
@click.option('--m', default = 1e-1, help = 'Symmetric migration rate across demes')
@click.option('--num_reps', default = 1, help = 'Number of independent replicates')
@click.option('--num_gen', default = 1, help = 'Number of generations simulated')
@click.option('--dims', default = (1,1),type=click.Tuple([int, int]), help = 'Dimensions of spatial lattice as tuple')
@click.option('--out',default = 'default_outfile',help = 'Path and filename for output')

def SS_WF_sim(pop_size,mu,s,m,num_reps,num_gen,dims,out):
    #Pre-allocate and initialize
    f = np.zeros((num_gen,num_reps)+dims)
    f[0] = 1/pop_size
    for j in range(num_gen-1):
        #Wright-Fisher diffusion w/Stepping Stone migration
        df = mu*(1-2*f[j])-s*f[j]*(1-f[j]) \
        +m*laplace(f[j],mode='wrap')
        #bounds allele frequencies
        p = np.clip(a= f[j] + df ,a_min=0,a_max=1)
        #genetic drift sampling
        f[j+1]= np.random.binomial(pop_size,p)/pop_size
    # Write freqmat as .npy
    np.save(out,f)

if __name__ == "__main__":
    SS_WF_sim()
