from common.common_methods import Utilities
from parse_netlist import ParseNetlist


class ParseModules(Utilities):
    """
    Parses Modules
    Parsers module list and stores it file or prints it on console
    """
    output_file_path = "files/parsed_files/ModuleCount.txt"

    def __init__(self):
        self.modules = dict()
        self.pn_obj = ParseNetlist()
        self.dict1 = self.pn_obj.module_list

    @property
    def primitives(self):
        primitives = []
        for mods in self.to_list():
            for instances in mods[1]:
                if instances not in self.module_list and instances not in primitives and instances:
                    primitives.append(instances)
        # print(primitives)
        return primitives

    def parse_modules(self, dict_file):
        """
        This file takes input a dictionary file with instance list and time of occurrence of each instance
        :param dict_file:
        :return dictionary with all primitives list + module list:
        """

        primitive_list = [instans for instans in self.to_list(dict_file) if instans[0] in self.primitives]
        # if all are primitives - return dict as it is
        if len(primitive_list) == len(self.instance_list(dict_file)):
            self.modules = dict_file
            return dict_file

        module_list = [instans for instans in self.to_list(dict_file) if instans[0] not in self.primitives]
        instance_list = []
        for inst in module_list:
            ins = self.to_list(self.parse_modules(self.dict1[inst[0]]))
            for i in range(0, len(ins)):
                ins[i] = list(ins[i])

            for i in ins:
                i[1] = inst[1]*i[1]

            for i in range(0, len(ins)):
                ins[i] = tuple(ins[i])
            instance_list += ins

        instance_list += primitive_list + module_list
        self.modules = dict()

        for ins in instance_list:
            if ins[0] not in self.modules:
                self.modules[ins[0]] = ins[1]
            else:
                self.modules[ins[0]] += ins[1]

        return instance_list + primitive_list

    def print_netlist(self, ipdict=None):
        modules = ipdict or self.dict1
        for sub_modules in modules:
            print(f"{sub_modules}".ljust(15)+f": {modules[sub_modules]} placements")

    def generate_and_print_netlist(self):
        """
        First generates module list and then prints it on console.
        :return:
        """
        for mod in self.module_list:
            print(f'\noutput for counting all of the instances in "{mod}" hierarchy:')
            self.parse_modules(self.dict1[mod])
            self.print_netlist(self.modules)

    def generate_and_store_netlist(self):
        """
        Generates and stores modules in "ModuleCount.txt".
        """
        net_list_file = open(self.output_file_path, "w")
        for mod in self.module_list:
            net_list_file.write(f'\nOutput for counting all of the instances in "{mod}" hierarchy:\n')
            self.parse_modules(self.dict1[mod])
            for sub_modules in self.modules:
                net_list_file.write(f"{sub_modules}".ljust(15)+f": {self.modules[sub_modules]} placements\n")

        net_list_file.close()


if __name__ == "__main__":
    np = NetlistParser()
    np.generate_and_print_netlist()
    np.generate_and_store_netlist()
