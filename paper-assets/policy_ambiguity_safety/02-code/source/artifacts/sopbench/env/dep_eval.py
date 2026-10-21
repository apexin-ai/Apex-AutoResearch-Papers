"""
holds the functionalities for dynamic domain dependencies

Inference time for this object:
initial variables: username = alice
conditionals: balance < 200
output: true or false

Input:
variables: {"username":"alice", "balance": 150, "owed balance": 150}
conditions: ("chain", [("single", "logged_in"), ("single", "owed balance < 100")])
"""

import re
from env.helpers import InvalidConstraintOption, hashable_dep

class Dependency_Evaluator:
    def __init__(self, database, state_tracker, all_dep:dict):
        self.database = database # called for innate constraints
        self.state_tracker = state_tracker # called for specific state-based constraints
        self.all_dep = all_dep # full dictionary of dependency functions for each action
    def process(self, method_str:str, **all_input_kwargs)->bool:
        if method_str not in self.all_dep or not self.all_dep[method_str]: return method_str in self.all_dep
        return self._process(self.all_dep[method_str], **all_input_kwargs)
    def _process(self, dep:tuple, **all_input_kwargs)->bool:
        if not dep: return True
        res = None
        match dep[0]:
            case "single":  res = self._single(dep[1], dep[2], **all_input_kwargs)
            case "and":     res = self._and(dep[1], **all_input_kwargs)
            case "or":      res = self._or(dep[1], **all_input_kwargs)
            case "chain":   res = self._chain(dep[1], **all_input_kwargs)
            case "gate":    res = self._gate(dep[1], **all_input_kwargs)
            case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
        return res
    def _single(self, func:str, param_mapping:dict[str:str], **all_input_kwargs)->bool:
        pos_not = func.find("not ")
        if pos_not > -1: func = func[pos_not+len("not "):]
        dep_obj = None
        if self.state_tracker and hasattr(self.state_tracker, func): dep_obj = self.state_tracker
        elif self.database: dep_obj = self.database
        else: return False
        if not param_mapping: param_mapping = {}
        func_params = {}
        for key in param_mapping:
            if "value " not in param_mapping[key]: func_params[key] = all_input_kwargs[param_mapping[key]]
            else: func_params[key] = eval(re.sub("value ", "", param_mapping[key]))
        func_response = getattr(dep_obj, func)(**func_params)
        func_response = func_response if isinstance(func_response, bool) else func_response[1]
        return (pos_not <= -1) == func_response
    def _and(self, deps:list, **all_input_kwargs)->bool:
        success = True
        for dep in deps:
            if success and not self._process(dep, **all_input_kwargs): success = False
        return success
    def _or(self, deps:list, **all_input_kwargs)->bool:
        success = False
        for dep in deps:
            if not success and self._process(dep, **all_input_kwargs): success = True
        return success
    def _chain(self, deps:list, **all_input_kwargs)->bool:
        for dep in deps:
            if not self._process(dep, **all_input_kwargs): return False
        return True
    def _gate(self, deps:list, **all_input_kwargs)->bool:
        for dep in deps:
            if self._process(dep, **all_input_kwargs): return True
        return False

# dependency check here is given that there is a violating dependency somewhere
class Dependency_Evaluator_Verify:
    def __init__(self, database=None, state_tracker=None, all_dep:dict=None,
        domain_dep:Dependency_Evaluator=None, constraint_values:dict={}):
        self.database = database            if not domain_dep else domain_dep.database
        self.state_tracker = state_tracker  if not domain_dep else domain_dep.state_tracker
        self.all_dep = all_dep              if not domain_dep else domain_dep.all_dep
        self.constraint_values = constraint_values
    def process(self, method_str:str, **all_input_kwargs)->tuple[bool,bool]:
        if method_str not in self.all_dep or not self.all_dep[method_str]: return method_str in self.all_dep, True
        return self._process(self.all_dep[method_str], **all_input_kwargs)
    def _process(self, dep:tuple, **all_input_kwargs)->tuple[bool,bool]:
        if not dep: return True, True
        res = None
        match dep[0]:
            case "single":
                res = self._single(dep[1], dep[2], **all_input_kwargs)
                constr_str = re.sub("not ", "", dep[1])
                constr_key = hashable_dep(("single", constr_str, dep[2]))
                res = (res, (self.constraint_values[constr_key] < 0
                    or (("not " in dep[1]) != res) == bool(self.constraint_values[constr_key])))
            case "and":     res = self._and(dep[1], **all_input_kwargs)
            case "or":      res = self._or(dep[1], **all_input_kwargs)
            case "chain":   res = self._chain(dep[1], **all_input_kwargs)
            case "gate":    res = self._gate(dep[1], **all_input_kwargs)
            case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
        return res
    def _single(self, func:str, param_mapping:dict[str:str], **all_input_kwargs)->tuple[bool,bool]:
        pos_not = func.find("not ")
        if pos_not > -1: func = func[pos_not+len("not "):]
        dep_obj = None
        if self.state_tracker and hasattr(self.state_tracker, func): dep_obj = self.state_tracker
        elif self.database: dep_obj = self.database
        else: return False
        if not param_mapping: param_mapping = {}
        func_params = {}
        for key in param_mapping:
            if param_mapping[key] not in all_input_kwargs: return not (pos_not <= -1)
            if "value " not in param_mapping[key]: func_params[key] = all_input_kwargs[param_mapping[key]]
            else: func_params[key] = eval(re.sub("value ", "", param_mapping[key]))
        func_response = getattr(dep_obj, func)(**func_params)
        func_response = func_response if isinstance(func_response, bool) else func_response[1]
        return (pos_not <= -1) == func_response
    def _and(self, deps:list, **all_input_kwargs)->tuple[bool,bool]:
        success = True
        constr_values_followed = True
        for dep in deps:
            suc_part, cvf_part = self._process(dep, **all_input_kwargs)
            if success and not suc_part: success = False
            if constr_values_followed and not cvf_part: constr_values_followed = False
        return success, constr_values_followed
    def _or(self, deps:list, **all_input_kwargs)->tuple[bool,bool]:
        success = False
        constr_values_followed = True
        for dep in deps:
            suc_part, cvf_part = self._process(dep, **all_input_kwargs)
            if not success and suc_part: success = True
            if constr_values_followed and not cvf_part: constr_values_followed = False
        return success, constr_values_followed
    def _chain(self, deps:list, **all_input_kwargs)->tuple[bool,bool]:
        constr_values_followed = True
        for dep in deps:
            suc_part, cvf_part = self._process(dep, **all_input_kwargs)
            if constr_values_followed and not cvf_part: constr_values_followed = False
            if not suc_part: return False, constr_values_followed
        return True, constr_values_followed
    def _gate(self, deps:list, **all_input_kwargs)->tuple[bool,bool]:
        constr_values_followed = True
        for dep in deps:
            suc_part, cvf_part = self._process(dep, **all_input_kwargs)
            if constr_values_followed and not cvf_part: constr_values_followed = False
            if suc_part: return True, constr_values_followed
        return False, constr_values_followed