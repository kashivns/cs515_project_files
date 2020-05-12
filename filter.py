import pandas as pd
import sys, getopt

def main(argv):
    input_csv = argv[0]

    dt = pd.read_csv(input_csv)
    # This is used to filter repo with same name, from different users
    dt = dt.drop_duplicates(subset=['RepoName', 'PostId'])
    dt = dt.drop_duplicates(subset=['PostId', 'FileId'])
    dt.to_csv(input_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("Usage: filter.py 'full file path to csv'")
