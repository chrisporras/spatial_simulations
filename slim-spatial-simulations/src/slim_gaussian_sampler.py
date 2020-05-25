#!python3
"""
    Takes concatenated array of frequencies (size: numreps X numdemes).
    Calculates average observed frequency given sampling width sigma for
    Gaussian sampling distribution.
"""
import numpy as np
from scipy.ndimage import gaussian_filter1d
import click


# Used to calculate average observed frequency

@click.command()
@click.option('--freqfilename',default = '',help = 'concat_reps file name')
@click.option('--sigma', default = 1, help = "Sampling distribution width")
@click.option('--out',default = '',help = 'OUTPUT')

def sampling_calc(freqfilename, sigma, out):
    freq_arr= genfromtxt(freqfilename,delimiter=",")
    # gaussian sampling from freq_arr with width sigma
    F = gaussian_filter1d(freq_arr,sigma=sigma,mode = "wrap")
    # Prepare output format
    header = (("sigma=%d")%(sigma))
    np.savetxt(out, F, delimiter=",",header=header)

if __name__ == "__main__":
    sampling_calc()
