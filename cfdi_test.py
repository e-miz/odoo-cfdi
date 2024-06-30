# %%
from satcfdi.cfdi import CFDI
from satcfdi import render
import glob
import awkward as ak

# %%
xml_file_paths = glob.glob("xml-bills/*.xml")
# %%
cfdi_list = []
for fp in xml_file_paths:
    invoice = CFDI.from_file(fp)
    cfdi_list.append(ak.from_json(render.json_str(invoice)))
# %%
cfdis = ak.Array(cfdi_list)
cfdis.Emisor.Nombre
