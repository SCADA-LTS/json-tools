import json
import copy
''''
input file extracted from scada working in production
'''
path_tofile = ""


src_view_name = "RüB Foetz Wartung"
src_view_xid = "cokolwiek"

out_view_name = ""
out_view_xid  = ""

'''
Open input json file and load data
'''

with open(path_tofile) as json_file:
    src_data = json.load(json_file)

try:
    '''
    Extract source view json from all exported views
    '''
    data = copy.deepcopy(src_data)
    data["graphicalViews"] = [x for x in data["graphicalViews"] if x["name"] == src_view_name and x["xid"] ==src_view_xid]
    if len(src_data["graphicalViews"]) == 0:
        raise ValueError('Given view name do not exist')
except:
    print('Warining: Type correct view name')
else:
    with open(out_view_name, "w") as text_file:
        text_file.write(json.dumps(data, indent=4, sort_keys=True))