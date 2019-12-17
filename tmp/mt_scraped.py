import pandas as pd
import os
import sys

# types = [30,31,33,35,36,37,60,70,80]
types = [35]

for type_id in types:
    csv_path = '/home/jetze/Downloads/examples_shiptype_'+str(type_id)+'_new.csv'
    csv_file = pd.read_csv(csv_path)
#     prev_mmsi = None
#     path = '/home/jetze/Downloads/examples/'+str(type_id)
#     if not os.path.exists(path):
#         os.makedirs(path)
    for i,row in csv_file.iterrows():
        mmsi = row['mmsi']
#         if mmsi == prev_mmsi:
#             continue
        photoid = row['url'].split('=')[-1][:-4]
        shiptype = row['type']
        name = str(mmsi)+'_'+str(shiptype)+'_'+str(photoid)
        dest = name+'.jpg'
        command = f"gsutil cp {row['url']} gs://marine-net/shiptype/{type_id}/{dest}"
        os.system(command)
