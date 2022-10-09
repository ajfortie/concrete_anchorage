import json
import os

const_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

f = open(const_path + "\\anchors.json","r")
anchor_dict = json.load(f)
f.close()

f = open(const_path + "\\matlgrade.json","r")
matl_dict = json.load(f)
f.close()
