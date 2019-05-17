import re


def remove_xid_dependency(components):
    '''

    :param view:
    :return:
    '''
    for component in components:
        component["dataPointXid"] = None
    return components


def change_xid(view, new_xid: str):
    view['xid'] = new_xid
    return view


def change_name(view, new_name: str):
    view['name'] = new_name
    return view


def make_importable_for_local_scada(view):
    '''
    Initial scada BR based on github, dont have all images etc...
    :param view:
    :return:
    '''
    view["sharingUsers"] = None
    view["viewComponents"] = [component for component in view["viewComponents"] if
                              component["type"] != "MULTISTATE_GRAPHIC" and component["type"] != "BINARY_GRAPHIC"]
    return view


def navigation_buttons_equals(view, x_first, y_first):
    for component in view["viewComponents"]:
        if component["type"] == "HTML":
            component_content = component["content"]
            x = re.findall("Scada\/.*\.gif", component_content)
            component_center_distance = 30
            if len(x) != 0:
                button_name = x[0][6:-4]
                if button_name == "FRButton":
                    component["y"] = y_first
                    component["x"] = x_first
                elif button_name == "PrevButton":
                    component["y"] = y_first
                    component["x"] = x_first + component_center_distance
                elif button_name == "ReloadButton":
                    component["y"] = y_first
                    component["x"] = x_first + 2 * component_center_distance
                elif button_name == "SivecButton":
                    component["y"] = y_first
                    component["x"] = x_first + 3 * component_center_distance
                elif button_name == "LogoutButton":
                    component["y"] = y_first
                    component["x"] = x_first + 4 * component_center_distance
                elif button_name == "NextButton":
                    component["y"] = y_first
                    component["x"] = x_first + 5 * component_center_distance
                elif button_name == "FFButton":
                    component["y"] = y_first
                    component["x"] = x_first + 6 * component_center_distance


def navigation_links_equals(view, x_first: int, y_first: int):
    '''
    TODO More intelligent way to find links to another views
    :param view:
    :param x_first:
    :param y_first:
    :return:
    '''
    i = 0
    for component in view["viewComponents"]:
        if component["type"] == "LINK":
            component["y"] = y_first + i * 15
            component["x"] = x_first
            i = i + 1
def alarm_table_locate(view):
    for component in view["viewComponents"]:
        if component["type"] == "ALARMLIST":
            component["y"] = 5 #make scadaLu wisible
            component["x"] = 0