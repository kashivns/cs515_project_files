import pandas as pd

import os

df = pd.read_csv("./filedata.csv")
k = "output-filedata"
filepaths = df["FilePath"]
index = 0
for fp in filepaths:
    print("print" + fp)
    out = fp.split("/")
    if not(os.path.isdir(os.path.join(k,out[1]))):
        os.mkdir(os.path.join(k,out[1]))
    if not(os.path.isdir(os.path.join(k,out[1],out[2]))):
        os.mkdir(os.path.join(k,out[1],out[2]))

    for dir in os.listdir(fp):
        if os.path.isdir(os.path.join(fp,dir)):
            if not(os.path.isdir(os.path.join(k,out[1],out[2],dir))):
                os.mkdir(os.path.join(k,out[1],out[2],dir))

            inp_fld = os.path.join(fp, dir)
            print("inp_fld", inp_fld)
            out_fld = inp_fld.replace("final/","")
            print(os.system("java -jar DesigniteJava.jar -i " + inp_fld + " -o " + "./output-filedata/"+ out_fld + "/"))

