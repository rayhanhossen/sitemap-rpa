import pandas as pd
import xml.dom.minidom as md

file_name = "../xml_files/sitemap_2023131.xml"
file = md.parse(file_name)
loc = file.getElementsByTagName("loc")

cols = ["URL"]
rows = []

# printing the first name
for i in range(len(loc)):
    print(loc[i].firstChild.nodeValue)
    rows.append({"URL": loc[i].firstChild.nodeValue})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
create_file_name = file_name.split('/')[-1]
df.to_csv(f"../csv_files/{create_file_name.split('.')[0]}.csv", index=False)
