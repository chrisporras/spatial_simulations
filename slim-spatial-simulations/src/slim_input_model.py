#!python3
"""
    Writes eidos script for SLiM 1D stepping-stone model with
    parameters for symmetric migration between a ring of demes.
"""
import numpy as np
# import csv
# import sys
import click

@click.command()
@click.option('--template',default = '',help = 'SLiM script template file')
@click.option('--migfilename', default = '', help = "Migration csv filename")
@click.option('--out',default = '',help = 'OUTPUT')

def modelfilewriter(template, migfilename, out):
    with open(template) as template_file:
        template_lines = template_file.readlines()
    template_lines.insert(1, " filename = \'{}\';\n".format(migfilename))
    modelstring = ("".join(template_lines))
    modeltxtfile = open(out, "w")
    modeltxtfile.write(modelstring)
    modeltxtfile.close()

if __name__ == "__main__":
    modelfilewriter()
