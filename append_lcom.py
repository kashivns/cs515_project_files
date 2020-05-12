import os
import pandas as pd

import os

rootdir = "/home/kashivns/soft-good/output-filedata/"
df = pd.DataFrame(columns=["Project Name","Package Name","Type Name","NOF","NOPF","NOM","NOPM","LOC","WMC","NC","DIT","LCOM","FANIN","FANOUT","Path"])
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        #print(file)
        filepath = subdir + os.sep + file
        #print(filepath)
        if filepath.endswith("typeMetrics.csv"):
            print (filepath)
            df1 = pd.read_csv(filepath)
            df1 = df1.assign(Path = [filepath]*len(df1))
            df = df.append(df1, ignore_index=True)
df.to_csv("/home/kashivns/soft-good/appended-filedata.csv", index=False)

