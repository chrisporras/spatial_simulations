#!python3
"""
    Simulates a Wright-Fisher process in a Stepping-Stone
    spatial lattice. Stores every 1/s generation.
    Takes the following parameters:
"""
import numpy as np
import click
from scipy.ndimage.filters import laplace

@click.command()
@click.option('--pop_size', default = 1e3, help = 'Number of individuals within each deme')
@click.option('--mu',default = 1e-5, help = 'Symmetric mutation rate')
@click.option('--s',default = 1e-2, help = 'Selection coefficient')
@click.option('--m', default = 1e-1, help = 'Symmetric migration rate across demes')
@click.option('--num_intervals', default = 1, help = 'Number of 1/s intervals to store')
@click.option('--dims', default = (1,1),type=click.Tuple([int, int]), help = 'Dimensions of spatial lattice as tuple')
@click.option('--out',default = 'default_outfile',help = 'Path and filename for output')

def downsample_f(pop_size,mu,s,m,num_intervals,dims,out):
    output = np.zeros(tuple([num_intervals])+dims)
    if s > 0:
        interval = int(1/s)
    else:
        interval = 100
    num_gens = interval * num_intervals
    f = np.zeros(dims)
    f[tuple(np.array(f.shape)-1)] = 1/pop_size
    ## pre-allocate list of when reset happens
    reset_gens = []
    for i in range(num_gens):
        ## update frequencies:
        ## Wright-Fisher diffusion w/Stepping Stone migration
        df = mu*(1-2*f)-s*f*(1-f) \
        +m*laplace(f,mode='wrap')
        ## bounds allele frequencies
        p = np.clip(a= f + df ,a_min=0,a_max=1)
        ## genetic drift sampling
        new_f = np.random.binomial(pop_size,p)/pop_size
        ## Check for implicit mu simulation and extinct allele
        if mu==0 and np.all(new_f==0):
            ## if extinct, store previous freqs and reset
            reset_gens.append(i)
            ## Add 1 allele to single element of
            ## an artbitrarily sized array
            new_f[tuple(np.array(new_f.shape)-1)] = 1/pop_size
        ## Assign next frequencies
        f = new_f
        ## choose freqs every 1/s and before reset happens
        if (i + 1) % interval == 0:
            output[i//interval] = f
    # Write freqmat as .npy
    np.save(out,output)


if __name__ == "__main__":
    downsample_f()
