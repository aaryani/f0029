import argparse
import os.path
import time
import pandas as pd

parser = argparse.ArgumentParser(description='Export node_orcid_ringold.csv from activities.csv')
parser.add_argument('file', help="the CSV input file")
args = parser.parse_args()
start_time = time.time()

def create_output_csv():
   """ Add code here to
   process activities.csv and
   create node_orcid_ringold.csv """

def main():
    """Main Process"""
    if os.path.isfile(args.file):
        create_output_csv()
        elapsed_time = time.time() - start_time
        print("Job completed in {}m".format(elapsed_time / 60))
    else:
        raise Exception('Could not find ' + args.file)


if __name__ == '__main__':
    main()
