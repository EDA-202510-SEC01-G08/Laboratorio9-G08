def new_map():
    return {"root": None}

def rotate_left(node_rbt):
    new_right =  node_rbt["right"]["left"]
    new_root = node_rbt["right"]
    node_rbt["right"] = new_right
    new_root["left"] = node_rbt
    return new_root

def rotate_right(node_rbt):
    new_root = node_rbt["left"]
    new_left = new_root["right"]
    node_rbt["left"] = new_left
    new_root["right"] = node_rbt

def flip_node_color(node_rbt):
    if node_rbt["color"] == "RED":
        node_rbt["color"] = "BLACK"
    elif node_rbt["color"] == "BLACK":
        node_rbt["color"] = "RED"
    return node_rbt