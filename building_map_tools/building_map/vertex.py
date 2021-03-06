from .param_value import ParamValue


class Vertex:
    def __init__(self, yaml_node):
        self.x = yaml_node[0]
        self.y = -yaml_node[1]
        self.z = yaml_node[2]  # currently always 0
        self.name = yaml_node[3]

        self.params = {}
        if len(yaml_node) > 4 and len(yaml_node[4]) > 0:
            for param_name, param_yaml in yaml_node[4].items():
                self.params[param_name] = ParamValue(param_yaml)
