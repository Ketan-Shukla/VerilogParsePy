import re
from common.common_methods import Utilities


class ParseNetlist(Utilities):
    """
    Reads verilog file and parses module list and netlist.
    netlist stored for future use in a text file
    """

    module_list = dict()
    module_name = ""
    netlist = ""
    output_file_path = "files/verilog/TopCell.v"

    def __init__(self):
        self.parse_netlist("./files/verilog/TopCell.v")
        self.store_netlist_file()

    def store_netlist_file(self):
        """
        stores net list in "NetList.txt" for future use
        """
        net_list_file = open("files/parsed_files/NetList.txt", "w")
        net_list_file.write(self.netlist)
        net_list_file.close()

    def parse_netlist(self, file):
        """
        parses netlist from the .v file
        generates netlist and module list stores it in the class variables
        """
        submodules = dict()
        with open(file, 'r') as vfile:
            for line in vfile:
                line = line.strip('\n')

                if "endmodule" in line:
                    self.module_list[self.module_name] = submodules
                    submodules = {}
                    continue

                if "module" in line:
                    self.module_name = re.split(r"\s", line)[2]
                    continue

                # skips the input, output and wires and comments
                if any(word in line for word in self.nets) or not line.strip() or re.match(r"^\s*/", line):
                    continue

                if re.match(r"^\s*\.", line):
                    self.netlist += line.strip()
                else:
                    self.netlist += "\n"+line.strip() if self.netlist else line.strip()

                # skips string starting with "."
                if re.match(r"^\s*\.", line):
                    continue

                # skips string starting with " "
                if not re.match(r"^\s*\b", line):
                    continue

                submodules = self.parse_instances_from_netlist(line, submodules)
        vfile.close()

    @staticmethod
    def parse_instances_from_netlist(line, submodules):
        """
        Takes input as netlist and returns instances
        :param line: netlist from where we will extract submodules
        :param submodules: dictinary where we store name and number of instances
        :return:
        """

        instance = re.split(r"\s", line.strip())[0]
        if instance in submodules:
            submodules[instance] += 1
        else:
            submodules[instance] = 1
        return submodules


if __name__ == "__main__":
    pn = ParseNetlist()
    print(pn.netlist)
    print(pn.module_list)
