# %%
from satcfdi.cfdi import CFDI
from satcfdi import render
import glob
import awkward as ak
import pandas as pd

# %%
xml_file_paths = glob.glob("xml-bills/**/*.xml")
# %%
cfdi_list = []
for fp in xml_file_paths:
    invoice = CFDI.from_file(fp)
    cfdi_list.append(ak.from_json(render.json_str(invoice)))
# %%
cfdis = ak.Array(cfdi_list)
# %%
receptor_df = ak.to_dataframe(cfdis["Receptor"])
receptor_df.replace(to_replace="nan", value=pd.NA).dropna().drop_duplicates(
    subset=[
        "Rfc",
        "Nombre",
    ]
).to_excel("cfdi_receptors.xlsx")
