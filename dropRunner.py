#!/usr/bin/env python

import os
import argparse
from droprunner import configurator

if __name__ == '__main__':

    work_dir = os.getcwd()

    parser = argparse.ArgumentParser()
    
    # Required
    parser.add_argument('--R1', type=str, help='Absolute path to gzipped read 1 fastq file (comma-delimited list of files if multiple.) REQUIRED')
    parser.add_argument('--R2', type=str, help='Absolute path to gzipped read 2 fastq file (comma-delimited list of files if multiple.) REQUIRED')
    parser.add_argument('--indeces', type=str, help='Name of indeces directory made by makeref.py')
    parser.add_argument('--protocol', type=str, help='Single cell protocol used to produce data. Options: drop, 10x-v2, 10x-v3')
    parser.add_argument('--cluster', action='store_true', help='Provide this flag if this job should be run on the cluster.')
    parser.add_argument('--sample', type=str, help='sample name. Optional.')
    
    args = parser.parse_args()

    if args.R1 == None or args.R2 == None or args.indeces == None or args.protocol == None:
         raise Exception('Required arguments not provided. Please provide R1, R2, an indeces folder name, and a protocol')
    
    assert os.path.isfile(args.R1), "Please provide a gzipped fastq file for read 1"
    assert os.path.isfile(args.R2), "Please provide a gzipped fastq files for read 2."
    assert os.path.isdir(args.indeces), 'Please provide indeces made by the makeref.py function!'
    assert args.protocol in ['drop', '10x-v2', '10x-v3'], 'Please provide a valid protocol! Options are drop, 10x-v2, or 10x-v3'
    
    if args.cluster == None:
        args.cluster = False
    if args.sample == None:
        args.sample = f'{args.protocol}-experiment'

    R1, R2, indeces, protocol, cluster, sample = args.R1, args.R2, args.indeces, args.protocol, args.cluster, args.sample
    configurator.main(R1=R1, 
                      R2=R2, 
                      indeces=indeces, 
                      protocol=protocol, 
                      cluster=cluster, 
                      sample=sample,
                      work_dir=work_dir)