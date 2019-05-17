import json
import copy
from view_clone.global_components_group import *

''''
input file extracted from scada working in production
'''
path_tofile = "input_instances/lu.json"

src_view_name = "RüB Foetz Wartung"
src_view_xid = "GV_990226"

out_view_name = "RüB XZY Wartung"
out_view_xid = "GV_990226"

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
    data["graphicalViews"] = [x for x in data["graphicalViews"] if
                              x["name"] == src_view_name and x["xid"] == src_view_xid]
    if len(src_data["graphicalViews"]) == 0:
        raise ValueError('Given view name do not exist')
    view_to_edit = data
except:
    print('Warining: Type correct view name')
else:
    change_xid(view_to_edit["graphicalViews"][0], out_view_xid)
    change_name(view_to_edit["graphicalViews"][0], out_view_name)
    view_to_edit["graphicalViews"][0]["viewComponents"] = remove_xid_dependency(
        view_to_edit["graphicalViews"][0]["viewComponents"])
    make_importable_for_local_scada(view_to_edit["graphicalViews"][0])
    navigation_buttons_equals(view_to_edit["graphicalViews"][0], 50, 180)
    navigation_links_equals(view_to_edit["graphicalViews"][0], 1040, 180)
    alarm_table_locate(view_to_edit["graphicalViews"][0])
    with open('output_to_scada_json/' + out_view_name, "w") as text_file:
        text_file.write(json.dumps(view_to_edit, indent=4, sort_keys=True))
