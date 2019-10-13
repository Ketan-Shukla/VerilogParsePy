class Utilities(object):
    dict1=dict()
    nets = ['input', 'output', 'wire', 'reg']

    @property
    def module_list(self):
        return list(self.dict1.keys())

    def to_list(self, ipdict = None):
        mod_dict = ipdict or self.dict1
        if isinstance(mod_dict, dict):
            return list(mod_dict.items())
        else:
            return mod_dict
    def to_dict(self,tup_list):
        mods_dict = dict(tup_list)
        return mods_dict

    def instance_list(self, module=None):

        return list(module or self.dict1.keys())
