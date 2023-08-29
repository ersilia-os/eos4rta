# imports
import os
import csv
import sys
import joblib

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

MODELPATH = os.path.join(root, "..", "..", "checkpoints")

# my model
def my_model(smiles_list):
    mdl1 = joblib.load(os.path.join(MODELPATH, "ic50_nf54_ldh_72h_1uM_morgan.joblib"))
    mdl2 = joblib.load(os.path.join(MODELPATH, "perc_nf54_ldh_72h_50_morgan.joblib"))
    mdl3 = joblib.load(os.path.join(MODELPATH, "perc_nf54_lum_72h_50_unders_morgan.joblib"))

    y_pred1 = mdl1.predict_proba(smiles_list)[:,1]
    y_pred2 = mdl2.predict_proba(smiles_list)[:,1]
    y_pred3 = mdl3.predict_proba(smiles_list)[:,1]

    return y_pred1, y_pred2, y_pred3


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output1, output2, output3 = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["NF54_IC50_72h_1uM", "NF54_50PercInh_LDH", "NF54_50PercInh_LUM"])  # header with column names
    for o1, o2, o3 in zip(output1, output2, output3):
        writer.writerow([o1, o2, o3])
