import pandas as pd

output = pd.read_csv("./filedata.csv")
# add latest_lcom, added_lcom, firsl_lcom 
#output.assign()
output['pre_LCOM'] = ""
output['post_LCOM'] = ""
output['latest_LCOM'] = ""


appended = pd.read_csv("./app-filedata.csv")

for index, row in output.iterrows():
    #k = appended['Path'] == row['FilePath'].replace('final/','')
    #print(appended['Path'])
    #print(row['FilePath'].replace()
    versions = appended[appended['Path'] == row['FilePath'].replace('final/','')] 
    #print(versions)
    print(versions[versions['Project Name'] == 1])
    print(versions[versions['Project Name']==row['Found in']])
    print(versions[versions['Project Name'] == int(row['Found in'])+1])
    
    latest_LCOM = versions[versions['Project Name'] == 1].iloc[0]['LCOM']
    post_LCOM = versions[versions['Project Name']==row['Found in']].iloc[0]['LCOM']
    try:
    	pre_LCOM = versions[versions['Project Name'] == int(row['Found in'])+1].iloc[0]['LCOM']
    except:
        print("Exception")
        continue
    print(f'latest:{latest_LCOM}, pre:{pre_LCOM}, post:{post_LCOM}')
    print(type(latest_LCOM))
    output.at[index,'pre_LCOM'] = pre_LCOM
    output.at[index,'post_LCOM'] = post_LCOM
    output.at[index,'latest_LCOM'] = latest_LCOM
print(output)
print(output.info())
output.to_csv('./pooled-data2.csv')

#for row in output:
#	
#	get all the rows from appended where file paths match
#	
#	get the values of:
#		1
#		output['version']
#		last version
#		
#	append all these values to the output df 
#	
#write it back to the output.csv
