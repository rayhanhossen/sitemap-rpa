import pandas as pd
import xml.dom.minidom as md
from datetime import date


def xml_to_csv(file_name_input):
    file_name = f"../xml_files/{file_name_input}"
    file = md.parse(file_name)
    loc = file.getElementsByTagName("loc")

    cols = ["URL"]
    rows = []

    # printing the first name
    for i in range(len(loc)):
        print(loc[i].firstChild.nodeValue)
        rows.append({"URL": loc[i].firstChild.nodeValue})

    df = pd.DataFrame(rows, columns=cols)

    # working with date
    today = date.today()
    # Writing dataframe to csv
    df.to_csv(f"../csv_files/goldengal_indexing_{today.year}{today.month}{today.day}.csv", index=False)
