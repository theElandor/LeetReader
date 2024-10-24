import os
def read_nodes(filename):
    filename = os.path.join("data", filename)
    with open(filename) as f:        
        nodes = eval(f.read().strip().replace("null", "None"))
        return nodes