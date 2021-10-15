# Transformation: data averaged by fish species
import pandas as pd
import math
import statistics as st



def get_species(csv_file):
    set_of_species = set({})
    df = pd.DataFrame(csv_file, columns=['Species'])
    for item in df["Species"]:
        set_of_species.add(item)
    return set_of_species


def get_avg(csv_file):
    df = pd.DataFrame(csv_file)
    return df.groupby("Species").mean()


def get_avg_total(df1, df2, df3):
    result = pd.concat([df1, df2, df3])
    return result.groupby("Species").mean()

# def get_avg(csv_file, column: str):
#     df = pd.DataFrame(csv_file, columns=['Species', column])
#     set_of_species = get_species(csv_file)
#     new_dict = {key: [] for key in set_of_species}
#
#     for i in df.values:
#         row = " ".join(str(x) for x in i)
#         row = row.split(" ")
#         species = str(row[0])
#         column_value = float(row[1])
#         new_dict[species].append(column_value)
#
#     return dict_mean(new_dict)
