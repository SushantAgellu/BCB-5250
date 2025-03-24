#!/usr/bin/env python3
import argparse
from Bio import SeqIO

def interleave_fastq(forward_file, reverse_file, output_file):
    #Interleaves two paired-end FASTQ files and writes them to an output file.
    #Parameters:
    #forward_file (str): Path to the forward reads FASTQ file.
    #reverse_file (str): Path to the reverse reads FASTQ file.
    #output_file (str): Path to the output interleaved FASTQ file.

    # Opens the input and the output files
    with open(forward_file, "r") as fwd, open(reverse_file, "r") as rev, open(output_file, "w") as out:

        # Parse the FASTQ files using SeqIO
        forward_reads = SeqIO.parse(fwd, "fastq")
        reverse_reads = SeqIO.parse(rev, "fastq")

        # Iterate through both files and write interleaved reads
        for fwd_read, rev_read in zip(forward_reads, reverse_reads):
            SeqIO.write(fwd_read, out, "fastq")
            SeqIO.write(rev_read, out, "fastq")

    print(f" Interleaved FASTQ file saved as: {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Interleave Paired-End FASTQ Files')
    parser.add_argument('forward_file', help='Forward reads FASTQ file (e.g., bacterium_R1.fastq)')
    parser.add_argument('reverse_file', help='Reverse reads FASTQ file (e.g., bacterium_R2.fastq)')
    parser.add_argument('output_file', help='Output interleaved FASTQ file (e.g., bacterium_R1_R2_interleaved.fastq)')
    
    args = parser.parse_args()


    interleave_fastq(args.forward_file, args.reverse_file, args.output_file)
