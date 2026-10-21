"""
File to hold helper functions for task_generation that could be used elsewhere
"""

import re
import copy
import itertools
import inspect
import json
from collections import deque
from difflib import SequenceMatcher
from textwrap import dedent


"""basic helper functions"""

class InvalidConstraintOption(Exception): pass

# inverses the string of the single constraint
def inv_constr(constr_str:str)->str:
    return f"not {constr_str}" if "not " not in constr_str else constr_str[constr_str.find("not ")+len("not "):]

# recursively inverses the dependency, basically DeMorgan's Law; special case "chain", where we only flip the last element
def inv_dep(dep:tuple, cl_handle:bool=False)->tuple:
    if not dep: return None
    dep_new = None
    match dep[0]:
        case "single": dep_new = ("single", inv_constr(dep[1]), dep[2])
        case "and" | "or": dep_new = ("or" if dep[0] == "and" else "and", [inv_dep(ele, cl_handle) for ele in dep[1]])
        case "chain" | "gate":
            if not cl_handle: dep_new = ("gate" if dep[0] == "chain" else "chain", [inv_dep(dep[1][i], cl_handle) for i in range(len(dep[1]))])
            else: dep_new = (dep[0], [dep[1][i] if i < len(dep[1])-1 else inv_dep(dep[1][i], cl_handle) for i in range(len(dep[1]))])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return dep_new

# modifies a formatted prompt to strip and remove the new lines in between each line
def modify_prompt(prompt:str)->str:
    prompt = re.sub(r"\n\s\s\s\s", ' ', dedent(prompt.strip()))
    remove_nl_pos = [i for i in range(1, len(prompt)) if prompt[i] == '\n' and prompt[i-1] != '\n'] # new line positions we want to remove'
    prompt_modified = prompt[:remove_nl_pos[0]]
    for i in range(1, len(remove_nl_pos)): prompt_modified += prompt[remove_nl_pos[i-1]+1:remove_nl_pos[i]]
    if remove_nl_pos[-1] < len(prompt)-1: prompt_modified += prompt[remove_nl_pos[-1]+1:]
    return prompt_modified

# combines the descriptions for the action and the return
def get_action_full_description(action_descriptions:dict, action_returns:dict, action_str:str)->str:
    return f"{action_descriptions[action_str]} {action_returns[action_str]}"

# puts none for all dependencies if no dependencies are specified
def get_domain_dependency_none(class_name:str)->dict:
    return {func:None for func in dir(class_name) if callable(getattr(class_name, func))}

# gets the action parameters for the actions of the domain
def get_action_parameters(domain_system, domain_assistant)->dict:
    list_action_name = [func for func in dir(domain_system)
        if callable(getattr(domain_system, func)) and not func.startswith("_") and not func.startswith("evaluation_")]
    action_parameters = {}
    for action_name in list_action_name:
        signature = inspect.signature(getattr(domain_system, action_name))
        action_params = {name for name, param in signature.parameters.items()
            if param.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)}
        if hasattr(domain_assistant, "action_params_user_not_needed")\
            and action_name in domain_assistant.action_params_user_not_needed:
            action_params -= set(domain_assistant.action_params_user_not_needed[action_name])
        action_parameters[action_name] = action_params
    return action_parameters


"""converts a constraint to and from a hashable tuple"""

# turns a dict into a hashable tuple
def dict_to_tuple(dic:dict)->tuple:
    if not dic: return ()
    sorted_items = sorted(dic.items(), key=lambda item: item[0])
    dep_params_list = []
    for dict_item in sorted_items: dep_params_list.extend(dict_item)
    return tuple(dep_params_list)

# turns a tuple of values into a dictionary
def tuple_to_dict(tup:tuple)->dict:
    if not tup: return {}
    return {tup[i]: tup[i+1] for i in range(0, len(tup)-1, 2)}

# turns a constraint into a hashable tuple
def hashable_dep(dep:tuple)->tuple:
    if not dep: return None
    if dep[0] == "single": return ("single", dep[1], dict_to_tuple(dep[2]))
    if dep[0] not in ["and", "or", "chain", "gate"]: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    dep_list = [hashable_dep(ele_dep) for ele_dep in dep[1]]
    if dep[0] in ["and", "or"]: dep_list = sorted(dep_list)
    return (dep[0], tuple(dep_list))

# turns a hashable constraint into its original state
def orig_dep(dep:tuple)->tuple:
    if not dep: return None
    if dep[0] == "single": return ("single", dep[1], tuple_to_dict(dep[2]))
    if dep[0] not in ["and", "or", "chain", "gate"]: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return (dep[0], tuple([orig_dep(ele_dep) for ele_dep in dep[1]]))


"""pruning the dependency or process tree"""

# used for pruning the dependency
asc_order_restr = ["chain", "and", "gate", "or"]

# check if the dep is directly seen or is encapsulated by another dependency, no exact matched found at this point, orig_dep_rel is not "single"
# "and" seen dep is True, "or" seen dep is False
def check_dep_seen_or_encapsulated(dep:tuple, seen_hashed_dep_set:set, orig_dep_rel:str)->bool:
    # dep directly seen before
    hashed_dep = hashable_dep(dep)
    if hashed_dep in seen_hashed_dep_set: return True
    # if not, then encapsulation detection method is needed
    global asc_order_restr
    pos_orig_dep_rel:int = asc_order_restr.index(orig_dep_rel)
    pos_dep_rel:int = asc_order_restr.index(dep[0]) if dep[0] != "single" else pos_orig_dep_rel # chain single == chain chain single
    dep_set:set = set(hashed_dep[1]) if dep[0] != "single" else {hashed_dep} # set of deps that dep represents
    encap_dep_found:bool = False
    for seen_hashed_dep in seen_hashed_dep_set:
        pos_seen_dep_rel:int = asc_order_restr.index(seen_hashed_dep[0]) if seen_hashed_dep[0] != "single" else pos_orig_dep_rel
        # check if the relations are equivalent in type and if the seen dep encapsulates the current dep
        rel_a, rel_b = (pos_seen_dep_rel, pos_dep_rel) if pos_orig_dep_rel < 1.5 else (pos_dep_rel, pos_seen_dep_rel)
        rel_equiv:bool = ((rel_a <= 1.5) == (rel_b <= 1.5)) # same type of relation
        rel_encap:bool = rel_a <= rel_b # one relation encapsulates the other
        if not rel_encap: continue
        # check if seen dep has a subset of current dep if relations are the same type, otherwise check or intersection
        seen_dep_set:set = set(seen_hashed_dep[1]) if seen_hashed_dep[0] != "single" else {seen_hashed_dep}
        depset_subset_inter:bool = not bool(dep_set - seen_dep_set) if rel_equiv else bool(seen_dep_set & dep_set)
        if not depset_subset_inter: continue
        # encapsulating dependency found
        encap_dep_found = True
        break
    return encap_dep_found

# removes dependencies if certain dependencies from the higher tiers have been seen
def dfsremove_if_unnecessary(dep:tuple, seen_hashed_dep_set:set, orig_dep_rel:str, inco_dep_rel:str,
    force_remove:bool=False)->tuple|bool:
    # None case
    if not dep: return dep
    global asc_order_restr
    # check if dependency is seen at the highest level
    pos_orig_dep_rel:int = asc_order_restr.index(orig_dep_rel)
    pos_inco_dep_rel:int = asc_order_restr.index(inco_dep_rel)
    if check_dep_seen_or_encapsulated(dep, seen_hashed_dep_set, orig_dep_rel)\
        and not (pos_orig_dep_rel // 2 == pos_inco_dep_rel // 2 and pos_inco_dep_rel < pos_orig_dep_rel):
        return pos_orig_dep_rel // 2 == 0
    # if not seen before
    if dep[0] == "single": return dep
    pos_dep_rel:int = asc_order_restr.index(dep[0])
    and_rel:bool = pos_dep_rel // 2 == 0 # True for "and", False for "or"
    dep_list_new = []
    for dep_part in dep[1]:
        dep_part = dfsremove_if_unnecessary(dep_part, seen_hashed_dep_set, orig_dep_rel, dep[0])
        # if dep_part is: bool (return a bool or remove), tuple (add into original list)
        if isinstance(dep_part, bool) and not force_remove and and_rel != dep_part: return dep_part
        elif isinstance(dep_part, tuple): dep_list_new.append(dep_part)
    return (dep[0], dep_list_new)

# collapses dependencies if there is only one dependency left in the "and" or "or"
def dfscollapse_dep(dep:tuple)->tuple:
    if dep[0] == "single": return dep
    dep_list_new = []
    for dep_part in dep[1]:
        dep_part = dfscollapse_dep(dep_part)
        if not dep_part: continue
        if dep[0] != dep_part[0]: dep_list_new.append(dep_part)
        else: dep_list_new.extend(dep_part[1])
    return (dep[0], dep_list_new) if len(dep_list_new) > 1 else\
        dep_list_new[0] if len(dep_list_new) == 1 else None

# prunes the dependency, nested "and" and "or", consider both True and False cases for simple constraints
def dfsprune_dep_pro(dep:tuple)->tuple:
    # base cases
    if not dep: return None
    elif dep[0] == "single": return dep
    # returns a set of dependencies that may be removed from elsewhere in the wider dependency, mainly handling "chain" and "gate"
    def dep_set_add_chaingate_ele(dep_part:tuple, dep_rel:str)->set:
        # if the dependency is "single" no additional elements added
        if dep_part[0] == "single": return set()
        global asc_order_restr
        # if the relation is not "chain" or "gate", no further actions required, else, add the "and" and "or" relation, respetively
        pos_dep_part_rel = asc_order_restr.index(dep_part[0])
        if not (pos_dep_part_rel % 2 == 0): return set()
        dep_set = {hashable_dep((asc_order_restr[pos_dep_part_rel+1], dep_part[1]))}
        # wider relation "chain" or "and" and "gate" or "or" matches "chain" and "gate" respectively
        pos_dep_rel = asc_order_restr.index(dep_rel)
        if pos_dep_part_rel // 2 == pos_dep_rel // 2:
            for dep_part_part in dep_part[1]: dep_set.add(hashable_dep(dep_part_part))
        return dep_set
    # prune the parts of the dependency, remove redundant constraints, once for each direction
    dep_list = []
    seen_dep_set = set()
    global asc_order_restr
    for dep_part in dep[1]:
        # prune and hash to check for identical
        dep_part = dfsprune_dep_pro(dep_part)
        hashed_dep_part = hashable_dep(dep_part)
        if not dep_part or hashed_dep_part in seen_dep_set: continue
        dep_list.append(dep_part)
        # update the set
        dep_part_set = {hashed_dep_part} | dep_set_add_chaingate_ele(dep_part, dep[0])
        seen_dep_set |= dep_part_set
    # remove identical dependencies in reverse
    rev_dep_list = dep_list[::-1]
    dep_list = []
    seen_dep_set = set()
    list_seen_dep_part_set = []
    for dep_part in rev_dep_list:
        # no None and already pruned
        hashed_dep_part = hashable_dep(dep_part)
        if hashed_dep_part in seen_dep_set: continue
        dep_list.append(dep_part)
        # update the set
        dep_part_set = {hashed_dep_part} | dep_set_add_chaingate_ele(dep_part, dep[0])
        seen_dep_set |= dep_part_set
        list_seen_dep_part_set.append(dep_part_set)
    dep_list = dep_list[::-1]
    list_seen_dep_part_set = list_seen_dep_part_set[::-1]
    # remove each part from the other parts depending on restrictiveness, 0 for forward and 1 for backward
    for ind_trav_type in range(2):
        ind_trav = range(len(dep_list)) if ind_trav_type == 0 else range(len(dep_list)-1, -1, -1)
        for i in ind_trav:
            # check for redundencies
            seen_dep_set_oneless = seen_dep_set.copy()
            seen_dep_set_oneless -= list_seen_dep_part_set[i]
            dep_part_old = dep_list[i]
            dep_list[i] = dfsremove_if_unnecessary(dep_list[i], seen_dep_set_oneless, dep[0], dep[0])
            # if the dependency changed, update the overarching set of seen dependencies
            if dep_part_old != dep_list[i]:
                if isinstance(dep_list[i], bool): list_seen_dep_part_set[i] = dep_list[i]
                else: list_seen_dep_part_set[i] = {hashable_dep(dep_list[i])} | dep_set_add_chaingate_ele(dep_list[i], dep[0])
                seen_dep_set = set.union(*[list_seen_dep_part_set[i] for i in range(len(dep_list)) if not isinstance(dep_list[i], bool)])
        dep_list = [ele for ele in dep_list if not isinstance(ele, bool)]
        list_seen_dep_part_set = [ele for ele in list_seen_dep_part_set if not isinstance(ele, bool)]
    # collapse if there is only one dependency part left
    dep_new = dfscollapse_dep((dep[0], dep_list))
    # return the new dependency, prune again for unseen corner cases
    if hashable_dep(dep) != hashable_dep(dep_new): dep_new = dfsprune_dep_pro(dep_new)
    return dep_new


"""basic dependency actions"""

# replace the keys of d1 in the values of d2 with the values of d1: d2[key] = d1[d2[key]]
def get_new_param_mapping(d1:dict, d2:dict)->dict:
    d = copy.deepcopy(d2)
    for key in d:
        if d[key] in d1: d[key] = d1[d[key]]
    return d

# returns a set of single constraints, removing the "not"
def dfsgather_constr_singles_dep_set(dep:tuple)->set:
    constr_set = set()
    if not dep: return constr_set
    match dep[0]:
        case "single":
            constr_set = {(dep[0], re.sub("not ", "", dep[1]), dict_to_tuple(dep[2]))}
        case "and" | "or" | "chain" | "gate":
            for ele in dep[1]: constr_set = constr_set | dfsgather_constr_singles_dep_set(ele)
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return constr_set

# returns a list of single constraints, preserving the order, removing the "not"
def dfsgather_constr_singles_dep_list_recur(dep:tuple)->list:
    constr_list, constr_set = [], set()
    if not dep: return constr_list, constr_set
    match dep[0]:
        case "single":
            constr_tuple = (dep[0], re.sub("not ", "", dep[1]), dict_to_tuple(dep[2]))
            constr_list = [constr_tuple]
            constr_set = {constr_tuple}
        case "and" | "or" | "chain" | "gate":
            for ele in dep[1]:
                constr_list_part, constr_set_part = dfsgather_constr_singles_dep_list_recur(ele)
                constr_set_part_new = constr_set_part - constr_set
                constr_list = constr_list + [elem for elem in constr_list_part if elem in constr_set_part_new]
                constr_set |= constr_set_part_new
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return constr_list, constr_set
def dfsgather_constr_singles_dep_list(dep:tuple)->list:
    constr_list, _ = dfsgather_constr_singles_dep_list_recur(dep)
    return constr_list

# dfs gather the parameter values in a dependency
def dfsgather_param_names_dep(dep:tuple)->set:
    params_set = set()
    if not dep: return params_set
    match dep[0]:
        case "single":
            if dep[2]: params_set = set(ele for ele in dep[2].values() if "value " not in ele)
        case "and" | "or" | "chain" | "gate":
            for ele in dep[1]: params_set = params_set | dfsgather_param_names_dep(ele)
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return params_set


"""retrieves the default dependencies, inserts the constraint dependencies"""

# dfs replaces param keys found in dep parameter values with the param values
def dfsplace_param_names(dep:tuple, params:dict)->tuple:
    if not dep: return None
    elif dep[0] == "single":
        params_new = copy.deepcopy(dep[2]) if dep[2] else {}
        for k in params_new:
            if params_new[k] in params: params_new[k] = params[params_new[k]]
        return dep[0], dep[1], params_new if params_new else None
    list_dep = []
    for dep_ele in dep[1]: list_dep.append(dfsplace_param_names(dep_ele, params))
    return dep[0], list_dep

# incorporates the constraint dependencies into the action dependency
def dfsins_constr_deps(dep:tuple, act_deps:dict, constr_deps:dict)->tuple:
    if not dep: return None
    dep_new = None
    match dep[0]:
        case "single":
            constr_str = re.sub("not ", "", dep[1])
            if not (constr_str in constr_deps and constr_deps[constr_str]): return dep
            constr_dep = dfsins_constr_deps(constr_deps[constr_str], act_deps, constr_deps)
            constr_dep = dfsplace_param_names(constr_dep, dep[2])
            dep_new = ("chain", [constr_dep, dep]) if "not " not in dep[1] else ("gate", [inv_dep(constr_dep), dep])
        case "and" | "or" | "chain" | "gate" :
            dep_new = (dep[0], [dfsins_constr_deps(dep_part, act_deps, constr_deps) for dep_part in dep[1]])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return dfsprune_dep_pro(dep_new)

# gathers the default dependencies for each action
def gather_action_default_dependencies(action_required_dependencies:dict, action_customizable_dependencies:dict,
    constraint_dependencies:dict=None, default_dependency_option:str="required")->dict[str:tuple]:
    default_dep_full = copy.deepcopy(action_required_dependencies)
    if default_dependency_option == "full":
        for action in default_dep_full:
            action_cust_dep = copy.deepcopy(action_customizable_dependencies[action])
            if action_cust_dep and isinstance(action_cust_dep, list): action_cust_dep = ("and", action_cust_dep)
            if default_dep_full[action] and action_cust_dep:
                default_dep_full[action] = ("and", [default_dep_full[action], action_cust_dep])
            elif action_cust_dep: default_dep_full[action] = action_cust_dep
    if constraint_dependencies:
        default_dep_full = {action: dfsins_constr_deps(default_dep_full[action], default_dep_full, constraint_dependencies) for action in default_dep_full}
    return {action: dfsprune_dep_pro(default_dep_full[action]) for action in default_dep_full}

# dfs insert the innate dependencies
def dfsins_innate_deps(dep:tuple, aid:dict)->tuple:
    if not dep: return None
    dep_new = None
    match dep[0]:
        case "single":
            constr_str = re.sub("not ", "", dep[1])
            if not (constr_str in aid and aid[constr_str]): return dep
            dep_part = dfsins_innate_deps(aid[constr_str], aid)
            dep_part = dfsplace_param_names(dep_part, dep[2])
            dep_new = ("chain", [dep_part, dep]) if "not " not in dep[1] else ("gate", [inv_dep(dep_part), dep])
        case "and" | "or" | "chain" | "gate":
            dep_new = (dep[0], [dfsins_innate_deps(dep_part, aid) for dep_part in dep[1]])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return dfsprune_dep_pro(dep_new)


"""gathers the action dependency with information needed (constraints) in mind"""

# given the constraint and the constr_str_seen, the function gives the proper function call (parameters previously found or brand new)
def get_cl_param_mapping(constr:tuple, constr_links:dict, action_parameters:dict[str:set], constr_str_seen:dict[str:dict[tuple:dict]]={}):
    constr_str, constr_param_mapping = constr
    # parse the contraint link action and parameter mapping
    cl_action, cl_param_mapping = copy.deepcopy(constr_links[constr_str]) if isinstance(constr_links[constr_str], tuple) else\
        (copy.deepcopy(constr_links[constr_str]), {})
    cl_param_mapping = cl_param_mapping if cl_param_mapping else {}
    for key in cl_param_mapping:
        if constr_param_mapping and cl_param_mapping[key] in constr_param_mapping: cl_param_mapping[key] = constr_param_mapping[cl_param_mapping[key]]
    # find the parameters of the current dependency and the linked action depedency
    constr_param_values = set(constr_param_mapping.values())
    depnew_param_values_new = copy.deepcopy(action_parameters[cl_action])
    for key in cl_param_mapping: depnew_param_values_new.remove(key)
    # load and/or record the correct parameter mapping
    key_param = tuple(sorted(list(constr_param_values)))
    if constr_str not in constr_str_seen:
        value_param_mapping = {key:key for key in depnew_param_values_new}
        constr_str_seen[constr_str] = {key_param: value_param_mapping}
    elif key_param not in constr_str_seen[constr_str]:
        # new mapping determined by count, could also do it by the constr params
        dpvn_param_mapping = {}
        for param_value in depnew_param_values_new:
            param_value_variations = [constr_str_seen[constr_str][kp_other][param_value] for kp_other in constr_str_seen[constr_str]]
            pvv_counts = [int(re.sub(param_value, "", pvv)) for pvv in param_value_variations if pvv != param_value]
            new_count = (max(pvv_counts) + 1) if pvv_counts else 0
            dpvn_param_mapping[param_value] = param_value + str(new_count)
        constr_str_seen[constr_str][key_param] = dpvn_param_mapping
    cl_param_mapping |= constr_str_seen[constr_str][key_param]
    # return the action
    return cl_action, cl_param_mapping

# dfs insert the constraint links: replaces the original constraint with the constraints of the linked action
# constr_str_seen key constr_str and value dict, dict key params tuple and value dict of param mappings to new params from the dep
def dfsins_constr_links(dep:tuple, constraint_links:dict, default_deps:dict, action_parameters:dict,
    constr_str_seen:dict[str:dict[tuple:dict]]={})->tuple:
    if not dep: return None
    dep_new = dep
    match dep[0]:
        case "single":
            constr_str = re.sub("not ", "", dep[1])
            cl = constraint_links
            if not (constr_str in cl and cl[constr_str]): return dep
            # parse the contraint link action and parameter mapping
            cl_action, cl_param_mapping = get_cl_param_mapping((constr_str, dep[2]), cl, action_parameters, constr_str_seen)
            # process the dependency
            cl_action_dep = copy.deepcopy(default_deps[cl_action])
            dep_part = dfsplace_param_names(cl_action_dep, cl_param_mapping)
            dep_part = dfsins_constr_links(dep_part, constraint_links, default_deps, action_parameters, constr_str_seen) # only recurse on the part that was inserted
            action_constr = ("single", cl_action, cl_param_mapping)
            dep_new = ("chain", [dep_part, action_constr]) if dep_part else action_constr
            if "not " in dep[1]: dep_new = inv_dep(dep_new) 
        case "and" | "or" | "chain" | "gate":
            dep_new = (dep[0], [dfsins_constr_links(dep_part, constraint_links, default_deps, action_parameters, constr_str_seen) for dep_part in dep[1]])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return dfsprune_dep_pro(dep_new)

# recursively inserts constraint links, constraint dependencies, and action innate dependencies
# default deps already has constraint dependencies, inversing a chain is only inverting the last element
def dfsins_cl_cd_aid(dep:tuple, constr_links:dict, act_innate_deps:dict, act_def_deps:dict, constr_deps:dict, action_parameters:dict,
    constr_str_seen:dict[str:dict[tuple:dict]]={})->tuple:
    if not dep: return None
    dep_new = None
    cl, aid, ad, cd = constr_links, act_innate_deps, act_def_deps, constr_deps
    match dep[0]:
        case "single":
            constr_str = re.sub("not ", "", dep[1])
            # constraint is in constraint links
            if constr_str in cl and cl[constr_str]:
                cl_action, cl_action_params = get_cl_param_mapping((constr_str, dep[2]), constr_links, action_parameters, constr_str_seen)
                constr_single = ("single", cl_action if "not " not in dep[1] else ("not " + cl_action), cl_action_params)
                dep_new = dfsins_cl_cd_aid(constr_single, cl, aid, ad, cd, action_parameters, constr_str_seen)
            # constraint (is an action) seen in action innate dependencies or seen in constraint processes
            else:
                constr_locs = [aid, ad, cd]
                dep_new_chain = []
                for constr_loc in constr_locs:
                    if not(constr_str in constr_loc and constr_loc[constr_str]): continue
                    dep_new_prev = dfsplace_param_names(constr_loc[constr_str], dep[2])
                    dep_new_prev = dfsins_cl_cd_aid(dep_new_prev, cl, aid, ad, cd, action_parameters, constr_str_seen)
                    if dep_new_prev: dep_new_chain.append(dep_new_prev if "not " not in dep[1] else inv_dep(dep_new_prev))
                dep_new_chain.append(dep)
                dep_new = ("chain" if "not " not in dep[1] else "gate", dep_new_chain) if len(dep_new_chain) > 1 else dep_new_chain[0]
        case "and" | "or" | "chain" | "gate":
            dep_new = (dep[0], [dfsins_cl_cd_aid(dep_part, cl, aid, ad, cd, action_parameters, constr_str_seen) for dep_part in dep[1]])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return dfsprune_dep_pro(dep_new)


"""retrieves the only the actions required to fullfill a dependency"""

# merges two lists, keeping the relative order
def merge_sequences(seq1, seq2)->list:
    sm = SequenceMatcher(a=seq1, b=seq2)
    res = []
    for (op, start1, end1, start2, end2) in sm.get_opcodes():
        # This range appears in both sequences, or only in the first one.
        if op == 'equal' or op == 'delete': res += seq1[start1:end1]
        # This range appears in only the second sequence.
        elif op == 'insert': res += seq2[start2:end2]
        # There are different ranges in each sequence - add both.
        elif op == 'replace':
            res += seq1[start1:end1]
            res += seq2[start2:end2]
    return res

# dfs gathers actions required to be called
def dfsgather_actions_required(dep_perm:tuple, hashed_cl_funcs:set)->list:
    if not dep_perm: return []
    deps_to_loop = []
    actions_required = []
    if dep_perm[0] == "single":
        func_str = re.sub("not ", "", dep_perm[1])
        func_params_to_find = {key: key for key in dep_perm[2]} if dep_perm[2] else None
        if (func_str, dict_to_tuple(func_params_to_find)) in hashed_cl_funcs:
            actions_required = [(func_str, dict_to_tuple(dep_perm[2]))]
    else: deps_to_loop = dep_perm[1]
    for dep_perm_part in deps_to_loop:
        actions_required = merge_sequences(actions_required, dfsgather_actions_required(dep_perm_part, hashed_cl_funcs))
    return actions_required


"""gather the functional call graph"""

# gathers all functions called later down the graph
def dfsgather_setfunccall_ifg(inv_func_graph:dict, ind:int, set_func_call:set=set())->set:
    if not isinstance(inv_func_graph["nodes"][ind], str): return {inv_func_graph["nodes"][ind][0]}
    ifg_conns = set((ind1, ind2) for ind1 in range(len(inv_func_graph["connections"])) for ind2 in inv_func_graph["connections"][ind1])
    for ind_from, ind_to in ifg_conns:
        if ind_from != ind or ind_to in set_func_call: continue
        set_func_call |= dfsgather_setfunccall_ifg(inv_func_graph, ind_to, set_func_call)
    return set_func_call

# updates the graph for a singular function call
def update_inv_func_graph_single(inv_func_graph:dict, func_str:str, func_params:dict, link_to_prev_root:bool)->dict:
    hashable_func = (func_str, dict_to_tuple(func_params))
    if hashable_func in inv_func_graph["inv_nodes"]: return inv_func_graph
    inv_func_graph["nodes"].append((func_str, func_params if func_params else {}))
    inv_func_graph["connections"].append(set())
    node_index = len(inv_func_graph["nodes"]) - 1
    inv_func_graph["inv_nodes"][hashable_func] = node_index
    if link_to_prev_root: inv_func_graph["connections"][node_index].add(inv_func_graph["root_ind"])
    inv_func_graph["root_ind"] = node_index
    return inv_func_graph

# hashes the node
def hash_node(node:tuple|str): return (node[0], dict_to_tuple(node[1])) if not isinstance(node, str) else node

# checks if two nodes are identical, checks nodes in a relation with every node of the other relation, connections need to be in set form
def dfscheck_same_andornode(inv_func_graph:dict, inv_func_graph_part:dict, ifg_node_ind:int, ifgp_node_ind:int, seen_inds:list=[set(), set()])->bool:
    # updating seen indicies to not loop
    seen_inds = copy.deepcopy(seen_inds)
    seen_inds[0].add(ifg_node_ind)
    seen_inds[1].add(ifgp_node_ind)
    # parsing the parameters
    ifg_nodes = inv_func_graph["nodes"]
    ifgp_nodes = inv_func_graph_part["nodes"]
    ifg_node = ifg_nodes[ifg_node_ind]
    ifgp_node = ifgp_nodes[ifgp_node_ind]
    ifg_node_conns = inv_func_graph["connections"][ifg_node_ind]
    ifgp_node_conns = inv_func_graph_part["connections"][ifgp_node_ind]
    # check for node type
    if isinstance(ifg_node, str) != isinstance(ifgp_node, str): return False
    # check function nodes, no node connections
    if not isinstance(ifg_node, str) and not ifg_node_conns and not ifgp_node_conns:
        return ifg_node[0] == ifgp_node[0] and ifg_node[1] == ifgp_node[1]
    # check both are "and", "or", or actions with connections
    if ifg_node != ifgp_node: return False
    if len(ifg_node_conns) != len(ifgp_node_conns): return False
    # check their connections
    conn_pairs = set(itertools.product(ifg_node_conns, ifgp_node_conns))
    ifg_ifgp_mapping = {}
    for ifg_conn, ifgp_conn in conn_pairs:
        if ifg_conn in seen_inds[0] or ifgp_conn in seen_inds[1]: continue
        same_andornode = dfscheck_same_andornode(inv_func_graph, inv_func_graph_part, ifg_conn, ifgp_conn, seen_inds)
        if ifg_conn not in ifg_ifgp_mapping and same_andornode: ifg_ifgp_mapping[ifg_conn] = ifgp_conn
    return ifg_node_conns == set(ifg_ifgp_mapping.keys()) and ifgp_node_conns == set(ifg_ifgp_mapping.values())

# returns the position of the inv_func_graph_part node in the inv_func_graph
def ifg_pos_of_node(inv_func_graph:dict, inv_func_graph_part:dict, ifgp_node_ind:int)->int:
    ifgp_node = inv_func_graph_part["nodes"][ifgp_node_ind]
    if not isinstance(ifgp_node, str):
        hashed_node = hash_node(ifgp_node)
        return inv_func_graph["inv_nodes"][hashed_node] if hashed_node in inv_func_graph["inv_nodes"] else -1
    else:
        for i in range(len(inv_func_graph["nodes"])):
            ifg_node = inv_func_graph["nodes"][i]
            if (isinstance(ifg_node, str)
                and dfscheck_same_andornode(inv_func_graph, inv_func_graph_part, i, ifgp_node_ind)):
                return i
        return -1

# updating the inv_func_graph with a part, connecting A nodes to B nodes
def update_inv_func_graph(inv_func_graph:dict, inv_func_graph_part:dict)->dict:
    # find the mapping of indicies from inv_func_graph_part to inv_func_graph, inserting nodes and inv_nodes
    ifgp_to_ifg_mapping = []
    for ifgp_node_ind in range(len(inv_func_graph_part["nodes"])):
        node = inv_func_graph_part["nodes"][ifgp_node_ind]
        ifg_node_ind = ifg_pos_of_node(inv_func_graph, inv_func_graph_part, ifgp_node_ind)
        if ifg_node_ind >= 0: ifgp_to_ifg_mapping.append(ifg_node_ind)
        else:
            inv_func_graph["nodes"].append(node)
            inv_func_graph["connections"].append(set())
            if not isinstance(node, str): inv_func_graph["inv_nodes"][hash_node(node)] = len(inv_func_graph["nodes"]) - 1
            ifgp_to_ifg_mapping.append(len(inv_func_graph["nodes"]) - 1)
    # inserting the new connections
    for ind_from in range(len(inv_func_graph_part["connections"])):
        inv_func_graph["connections"][ifgp_to_ifg_mapping[ind_from]] |=\
            set(ifgp_to_ifg_mapping[ind_dest] for ind_dest in inv_func_graph_part["connections"][ind_from])   
    # if the entire tree part is not seen before, connect it to the overarching node
    # else, set a new root node with a new overarching node (old overarching node guaranteed to be "and" or "or")
    ifg_to_ifgp_mapping = [-1 for _ in range(len(inv_func_graph["nodes"]))] # will contain more or equal to the number of nodes ifgp has
    for i in range(len(ifgp_to_ifg_mapping)): ifg_to_ifgp_mapping[ifgp_to_ifg_mapping[i]] = i
    if ifg_to_ifgp_mapping[inv_func_graph["root_ind"]] < 0:
        inv_func_graph["connections"][inv_func_graph["root_ind"]].add(ifgp_to_ifg_mapping[inv_func_graph_part["root_ind"]])
    else:
        prev_root_ind = inv_func_graph["root_ind"]
        inv_func_graph["root_ind"] = ifgp_to_ifg_mapping[inv_func_graph_part["root_ind"]]
        # new parent is not the same overarching node
        if inv_func_graph["nodes"][prev_root_ind] != inv_func_graph["nodes"][inv_func_graph["root_ind"]]:
            inv_func_graph["nodes"].append(inv_func_graph["nodes"][prev_root_ind]) # should be an immutable string
            inv_func_graph["connections"].append({inv_func_graph["root_ind"]})
            inv_func_graph["root_ind"] = len(inv_func_graph["nodes"]) - 1
        # add the connection if it wasn't there before, duplicates will not be added to the set
        if inv_func_graph["root_ind"] != prev_root_ind: inv_func_graph["connections"][inv_func_graph["root_ind"]].add(prev_root_ind)
    # returning the result
    return inv_func_graph

# gathers the inverse function call graph represented by the process, constraint processes, and default dependency
def dfsgather_inv_func_graph_process(pro:tuple, constr_links:dict, constr_pros:dict, act_def_deps:dict, action_parameters:dict,
    constr_str_seen:dict[str:dict[tuple:dict]]={}, prev_func_call:tuple=None):
    inv_func_graph = {"nodes": [], "connections": [], "inv_nodes":{}, "root_ind": -1}
    if not pro: return inv_func_graph
    # singular action
    if pro[0] == "single":
        if act_def_deps[pro[1]]:
            action_dep = dfsplace_param_names(act_def_deps[pro[1]], pro[2])
            # action is guaranteed to be in action dependencies
            inv_func_graph = dfsgather_inv_func_graph_dependency(action_dep, constr_links, constr_pros,
                act_def_deps, action_parameters, constr_str_seen)
        # chain the previous graph to this action if need be
        inv_func_graph = update_inv_func_graph_single(inv_func_graph, pro[1], pro[2], bool(act_def_deps[pro[1]]))
        return inv_func_graph
    # "and" or "or"
    inv_func_graph["nodes"].append(pro[0])
    inv_func_graph["connections"].append(set())
    inv_func_graph["root_ind"] = len(inv_func_graph["nodes"]) - 1 # guaranteed to be 0
    for pro_part in pro[1]:
        inv_func_graph_part = dfsgather_inv_func_graph_process(pro_part, constr_links, constr_pros,
            act_def_deps, action_parameters, constr_str_seen, prev_func_call)
        if inv_func_graph_part["nodes"]: inv_func_graph = update_inv_func_graph(inv_func_graph, inv_func_graph_part)
    return inv_func_graph

# helper function that returns the connections between functions, may have loops
# processing actions in a chain, need actions from both ends
# "nodes" with functions or "and" or "or", "connections" with index pairs, "inv_nodes" that link function calls with an index
# connecting nodes backwards and forwards
def dfsgather_inv_func_graph_dependency(dep_orig:tuple,
    constr_links:dict, constr_pros:dict, action_default_deps_orig:dict, action_parameters:dict,
    constr_str_seen:dict[str:dict[tuple:dict]]={})->dict:
    inv_func_graph = {"nodes": [], "connections": [], "inv_nodes":{}, "root_ind": -1}
    # single case, constraints are guaranteed to be in constraint links or constraint processes
    if not dep_orig: return inv_func_graph
    elif dep_orig[0] == "single":
        constr_str = re.sub("not ", "", dep_orig[1])
        if constr_str in constr_links:
            action_name, action_params = get_cl_param_mapping((constr_str, dep_orig[2]), constr_links, action_parameters, constr_str_seen)
            action = ("single", action_name, action_params)
            inv_func_graph = dfsgather_inv_func_graph_process(action, constr_links, constr_pros,
                action_default_deps_orig, action_parameters, constr_str_seen)
        else:
            constr_pro = dfsplace_param_names(constr_pros[constr_str], dep_orig[2])
            action = ("single", dep_orig[1], dep_orig[2])
            inv_func_graph = dfsgather_inv_func_graph_process(constr_pro, constr_links, constr_pros,
                action_default_deps_orig, action_parameters, constr_str_seen, action)
        return inv_func_graph
    # initialize the multiple function call
    inds = None
    node_type = None
    match dep_orig[0]:
        case "and" | "or": node_type = dep_orig[0]
        case "chain" | "gate": node_type = "and" if dep_orig[0] == "chain" else "or"
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep_orig[0]}")
    inv_func_graph["nodes"].append(node_type)
    inv_func_graph["connections"].append(set())
    inv_func_graph["root_ind"] = len(inv_func_graph["nodes"]) - 1 # should be 0
    inds = range(len(dep_orig[1]))
    # loop through all indicies
    for i in inds:
        dep_perm_part = dep_orig[1][i]
        # process the sub part
        inv_func_graph_part = dfsgather_inv_func_graph_dependency(dep_perm_part, constr_links, constr_pros,
            action_default_deps_orig, action_parameters, constr_str_seen)
        # update the graph accordingly, connecting the functions accordingly, guaranteed to be "and" or "or"
        if inv_func_graph_part["nodes"]: inv_func_graph = update_inv_func_graph(inv_func_graph, inv_func_graph_part)
    # removing a node if there is only one action in the "and" or "or", subtracting one from all indicies
    root_old_ind = inv_func_graph["root_ind"]
    if isinstance(inv_func_graph["nodes"][root_old_ind], str) and len(inv_func_graph["connections"][root_old_ind]) == 1:
        # update the new root
        inv_func_graph["root_ind"] = list(inv_func_graph["connections"][root_old_ind])[0]
        if inv_func_graph["root_ind"] > root_old_ind: inv_func_graph["root_ind"] -= 1
        # edit the node list
        inv_func_graph["nodes"].pop(root_old_ind)
        ifg_conns = inv_func_graph["connections"]
        ifg_conns.pop(root_old_ind)
        inv_func_graph["connections"] = [set(ind_dest-1 if ind_dest > root_old_ind else ind_dest for ind_dest in ifg_conns[ind_sour]) for ind_sour in range(len(ifg_conns))]
        inv_func_graph["inv_nodes"] = {key: (inv_func_graph["inv_nodes"][key]-1) if inv_func_graph["inv_nodes"][key] > root_old_ind else inv_func_graph["inv_nodes"][key]
            for key in inv_func_graph["inv_nodes"]
            if inv_func_graph["inv_nodes"][key] != root_old_ind}
    # return the graph
    return inv_func_graph

# converts the list of tuple connections to a list of sets (indexed by node indicies)
def convert_ifg_connections_list_to_set(connections:list)->list:
    if not connections or connections and isinstance(connections[0], set): return copy.deepcopy(connections)
    node_inds = set()
    for node_from, node_to in connections: node_inds |= {node_from, node_to}
    max_node_ind = max(node_inds)
    connections_new = [set() for _ in range(max_node_ind+1)] # could be list, worse for comparision later
    for conn_from, conn_to in connections: connections_new[conn_from].add(conn_to)
    return connections_new

# converts a list of sets (indexed by node indicies) to a list of tuple connections
def convert_ifg_connections_set_to_list(connections:set)->list:
    if not connections or connections and isinstance(connections[0], tuple): return connections
    connections_new = [(ind_sour, ind_dest)
        for ind_sour in range(len(connections))
        for ind_dest in connections[ind_sour]]
    return connections_new

# renumbering the indicies for better readability, prioritizing the longest distance from the start
def change_nodeorder_invfuncgraph(inv_func_graph:dict, root_ind:int,
    in_conn_list_form_bool:bool=False, out_conn_list_form_bool:bool=True)->dict:
    # convert the connections from list of tuples to a list of sets
    if in_conn_list_form_bool:
        inv_func_graph["connections"] = convert_ifg_connections_list_to_set(inv_func_graph["connections"])
    # renumbering the indicies for better readability, prioritizing the longest distance from the start
    dir_graph_branches = inv_func_graph["connections"]
    renumber_mapping = [-1 for _ in range(len(inv_func_graph["nodes"]))]
    queue_ind = deque([(root_ind, 0)]) # insert right because stack
    branches = [set()] # each path through the graph has a chain, tracks visited node indicies
    counter_dist = 0
    while queue_ind:
        ind, branch_num = queue_ind.popleft()
        # cycle prevention
        if ind in branches[branch_num]: continue
        branches[branch_num].add(ind)
        # pushes "and" and "or" nodes towards the end of the numbering
        neighbor_inds = []
        neighbors_andor_startpos = 0
        for neighbor_ind in dir_graph_branches[ind]:
            if not isinstance(inv_func_graph["nodes"][neighbor_ind], str):
                neighbor_inds.insert(neighbors_andor_startpos, neighbor_ind)
                neighbors_andor_startpos += 1
            else: neighbor_inds.append(neighbor_ind)
        # extend the queue with the neighboring indexes, keep track of visited nodes
        if neighbor_inds:
            neighbors_ind_branchnum = [(neighbor_inds[0], branch_num)]
            for i in range(1, len(neighbor_inds)):
                branches.append(branches[branch_num].copy())
                neighbors_ind_branchnum.append((neighbor_inds[i], len(branches)-1))
            queue_ind.extend(neighbors_ind_branchnum)
        # recording the distance in the chain from the start
        renumber_mapping[ind] = counter_dist
        counter_dist += 1
    renumber_mapping_sorted_dest = sorted([(renumber_mapping[ind], ind) for ind in range(len(renumber_mapping))])
    mapping_new_to_old = [old_ind for _, old_ind in renumber_mapping_sorted_dest]
    mapping_old_to_new = [-1 for _ in range(len(mapping_new_to_old))]
    for i in range(len(mapping_new_to_old)): mapping_old_to_new[mapping_new_to_old[i]] = i
    # mapping from old indicies to new indicies
    ifg_old = inv_func_graph
    inv_func_graph = {"nodes": [-1 for _ in range(len(ifg_old["nodes"]))], "connections": [set() for _ in range(len(ifg_old["nodes"]))]}
    for old_ind in range(len(mapping_old_to_new)): inv_func_graph["nodes"][mapping_old_to_new[old_ind]] = ifg_old["nodes"][old_ind]
    for old_ind1 in range(len(ifg_old["connections"])):
        inv_func_graph["connections"][mapping_old_to_new[old_ind1]] =\
            sorted(list(mapping_old_to_new[old_ind2] for old_ind2 in ifg_old["connections"][old_ind1]))
    # list of connections
    if out_conn_list_form_bool:
        inv_func_graph["connections"] = convert_ifg_connections_set_to_list(inv_func_graph["connections"])
    # small sanity check: self loops
    for ind_sour, ind_dest in inv_func_graph["connections"]:
        if ind_sour == ind_dest: raise InvalidGraphSelfLoop("node self-loop detected in the inverse function call graph")
    # return the graph
    return inv_func_graph

# dfs gathers the inverse function call directed graph, passed in dependency has the constraint links and dependencies inserted
class InvalidGraphSelfLoop(Exception): pass
def dfsgather_invfunccalldirgraph(dep_orig:tuple,
    constr_links:dict, constr_pros:dict, action_default_deps_orig:dict, action_parameters:dict,
    action_user_goal:tuple)->dict[str:list]:
    # find the connections that make up the function call graph
    connections = dfsgather_inv_func_graph_dependency(dep_orig, constr_links, constr_pros, action_default_deps_orig, action_parameters)
    # adding the user_goal into the front
    inv_func_graph = copy.deepcopy(connections)
    if not inv_func_graph["nodes"] or action_user_goal[0] != inv_func_graph["nodes"][inv_func_graph["root_ind"]][0]:
        inv_func_graph["nodes"].append(action_user_goal)
        if inv_func_graph["root_ind"] >= 0: inv_func_graph["connections"].append({inv_func_graph["root_ind"]})
        else: inv_func_graph["connections"].append(set())
    del inv_func_graph["inv_nodes"]
    del inv_func_graph["root_ind"]
    # renumbering the indicies for better readability, prioritizing the longest distance from the start
    return change_nodeorder_invfuncgraph(inv_func_graph, len(inv_func_graph["nodes"])-1)

# renumber nodes, some nodes are "removed" because their node index has None
def renumber_nodes(nodes:list, conns:list, root_ind:int, node_mapping:list)->tuple:
    nodes_new, conns_new = [], []
    offset = 0
    offsets = [] # records how much the node index needs to be offset based on which nodes were removed
    for node in nodes:
        if not node:
            offset += 1
            offsets.append(-1)
        else: offsets.append(offset)
    for node_ind in range(len(nodes)):
        if not nodes[node_ind]: continue
        nodes_new.append(nodes[node_ind])
        conns_new_node = set()
        for node_ind_to in conns[node_ind]:
            node_ind_to = node_mapping[node_ind_to]
            conns_new_node.add(node_ind_to - offsets[node_ind_to])
        conns_new.append(conns_new_node)
    root_ind = node_mapping[root_ind] - offsets[node_mapping[root_ind]]
    return nodes_new, conns_new, root_ind

# compare every node with every other node, pruning the graph of duplicate nodes
def prune_ifg(inv_func_graph:dict, root_ind:int=0)->dict:
    nodes, conns = inv_func_graph["nodes"], inv_func_graph["connections"]
    conns = convert_ifg_connections_list_to_set(conns)
    if not conns: conns = [set() for _ in nodes]
    inv_func_graph["connections"] = conns
    # bfs start from root, check for node duplicates (duplicate function name, even with different parameters)
    seen_nodes = set()
    node_mapping = [i for i in range(len(nodes))] # maps the duplicates to their original
    q = deque([root_ind])
    while q:
        node = q.popleft()
        if node in seen_nodes: continue
        seen_nodes.add(node)
        for i in range(len(nodes)):
            if i in seen_nodes: continue
            if not dfscheck_same_andornode(inv_func_graph, inv_func_graph, node, i): continue
            node_mapping[i] = node
            nodes[i], conns[i] = None, None
            seen_nodes.add(i)
        q.extend(conns[node])
    # renumber nodes
    nodes, conns, root_ind = renumber_nodes(nodes, conns, root_ind, node_mapping)
    # prune relation nodes with only one node
    node_mapping = [i for i in range(len(nodes))]
    q = deque([root_ind])
    while q:
        node = q.popleft()
        if not nodes[node]: continue
        if isinstance(nodes[node], str) and len(conns[node])==1:
            # should reassign the connections and root_ind during renumbering with this mapping
            node_mapping[node] = next(iter(conns[node]))
            nodes[node], conns[node] = None, None
            q.append(node_mapping[node])
        else:
            for node_next in conns[node]: q.append(node_next)
    # renumber nodes
    nodes, conns, root_ind = renumber_nodes(nodes, conns, root_ind, node_mapping)
    inv_func_graph["nodes"] = nodes
    inv_func_graph["connections"] = conns
    return change_nodeorder_invfuncgraph(inv_func_graph, root_ind)


"""converts tree to inverse function graph, and vice versa"""

# converts the inverse function call graph into a tree, like a dependency
def bfsconvert_ifg_to_tree(inv_func_graph:dict)->tuple:
    nodes = inv_func_graph["nodes"]
    if len(nodes) == 1: return "None"
    connections, _ = get_ifg_connections_invnodes(inv_func_graph)
    # constructs the process from the node in the graph
    def get_node_pointer(nodes:list, node_pos:int)->tuple:
        return (nodes[node_pos], []) if isinstance(nodes[node_pos], str) else ("single", *nodes[node_pos])
    # based on the current position within the process, returns the proper next position
    def get_pro_pos(current_position:str|list, relative_position:list)->list:
        if isinstance(current_position, str): return relative_position
        next_position = current_position.copy()
        next_position.extend(relative_position)
        return next_position
    # gets the nested value in a list based on the list of indicies
    def get_nested_value(data, indices):
        current = data
        for index in indices:
            try: current = current[index]
            except (IndexError, TypeError): return None
        return current
    # sets the nested value
    def set_nested_value(data, indices, data_part):
        current = data
        for i in range(len(indices)-1):
            index = indices[i]
            try: current = current[index]
            except (IndexError, TypeError): return
        try: current[indices[-1]] = data_part
        except (IndexError, TypeError): pass
    # bfs traversing the graph to construct the tree
    root_rel_pos = next(iter(connections[0])) # skipping the target function
    root_node = get_node_pointer(nodes, root_rel_pos)
    root_node_pro_pos = "root"
    process = (root_node)
    # keeping track of three things: process construction, current process location, and position within the ifg nodes
    queue_ind = deque([(root_node_pro_pos, root_rel_pos)]) # insert right because stack
    while queue_ind:
        node_pro_pos, node_pos = queue_ind.popleft() # pointer (position in the process), node index
        node_pointer = process if isinstance(node_pro_pos, str) else get_nested_value(process, node_pro_pos)
        # insert the current node's connections
        if isinstance(nodes[node_pos], str):
            counter = 0
            for node_part_pos in connections[node_pos]:
                node_part_pointer = get_node_pointer(nodes, node_part_pos)
                node_pointer[1].append(node_part_pointer)
                node_part_pro_pos = get_pro_pos(node_pro_pos, [1, counter])
                queue_ind.append((node_part_pro_pos, node_part_pos))
                counter += 1
        else:
            if connections[node_pos]:
                node_part_pos = next(iter(connections[node_pos]))
                node_part_pointer = get_node_pointer(nodes, node_part_pos)
                # functions reversed to better match the meaning of chain
                set_nested_value(process, node_pro_pos, ("chain", [node_part_pointer, node_pointer]))
                node_part_pro_pos = get_pro_pos(node_pro_pos, [1, 0])
                queue_ind.append((node_part_pro_pos, node_part_pos))
    return process

# converts the dependency into a graph, like a inverse function call graph, no gate
def bfsconvert_tree_to_ifg(dep:tuple, action_user_goal:tuple=None)->dict:
    # finds the leaves of the graph, returns a list of indicies
    def gather_ifg_leaves(ifg:dict)->list[int]:
        conns = convert_ifg_connections_list_to_set(ifg["connections"])
        if not conns: conns = [set() for _ in ifg["nodes"]]
        return [i for i in range(len(ifg["nodes"])) if not conns[i]]
    # integrates the chain stucture into the inverse function graph
    def integrate_chain_into_ifg(nodes:list, connections:list, node_prev:int, dep_part:tuple):
        prev_forw_conns = [node_prev]
        for i in range(len(dep_part[1])-1, -1, -1):
            # gather the chain link tree
            dep_part_part = dep_part[1][i]
            ifg_dpp = bfsconvert_tree_to_ifg(dep_part_part)
            if i > 0: ifg_dpp_leaves = gather_ifg_leaves(ifg_dpp)
            # add the respective nodes and connections
            offset = len(nodes)
            nodes.extend(ifg_dpp["nodes"])
            for a, b in ifg_dpp["connections"]: connections.append((a+offset, b+offset))
            if not (i == len(dep_part[1])-1 and node_prev < 0):
                connections.extend(list(itertools.product(prev_forw_conns, [offset])))
            if i > 0: prev_forw_conns = [node_leaf+offset for node_leaf in ifg_dpp_leaves]
    # construct the ifg with no regard for duplicates
    nodes, connections = [action_user_goal] if action_user_goal else [], []
    q = deque()
    if dep: q = deque([(0 if action_user_goal else -1, dep)])
    while q:
        node_prev, dep_part = q.popleft()
        match dep_part[0]:
            case "single":
                nodes.append((dep_part[1], dep_part[2]))
                if node_prev >= 0: connections.append((node_prev, len(nodes)-1))
            case "and" | "or" | "gate":
                if dep_part[0] == "gate": nodes.append("or")
                else: nodes.append(dep_part[0])
                if node_prev >= 0: connections.append((node_prev, len(nodes)-1))
                for dep_part_part in dep_part[1]: q.append((len(nodes)-1, dep_part_part))
            case "chain":
                integrate_chain_into_ifg(nodes, connections, node_prev, dep_part)
            case _: raise InvalidConstraintOption(f"invalid option in tree when constructing the graph: {dep_part}")
    inv_func_graph = {"nodes": nodes, "connections": connections}
    # prune, change the node order, and return
    return prune_ifg(inv_func_graph)


"""useful functions for printing information"""

# formats the title to have a constant length
def get_title_str(title:str, title_length:int=64)->str:
    if len(title) > title_length-2-2: return f"- {title} -"
    side_length = (title_length - len(title) - 2) // 2
    return ('-' * side_length) + f" {title} " + ('-' * (title_length - (len(title)+2) - side_length))

# prints the dictionary in a pretty format, excludes keys on the very top level
def get_dict_str(d:dict, excluded_keys:set=set())->str:
    if not d: return
    keys = sorted([(key, str(key)) for key in d], key=lambda x: x[1])
    max_key_len = max([len(str(key)) for key in d])
    dict_str = ""
    for key, _ in keys:
        if key in excluded_keys: continue
        dict_str += '{0:{align}{max_key_len}} {b}\n'.format(str(key), b=str(d[key]), align="<", max_key_len=max_key_len)
    return dict_str[:-1]

# prints the dictionary in a pretty json format, excludes keys on the very top level
def get_dict_json_str(d:dict, excluded_keys:set=set(), indent_amount:int=2)->str:
    if not d: return
    keys = sorted([(key, str(key)) for key in d], key=lambda x: x[1])
    max_key_len = max([len(str(key)) for key in d])
    indent_str = '\n' + ' ' * (max_key_len+1)
    dict_str = ""
    for key, _ in keys:
        if key in excluded_keys: continue
        value_str = json.dumps(d[key], indent=indent_amount)
        value_str = re.sub('\n', indent_str, value_str)
        dict_str += '{0:{align}{max_key_len}} {b}\n'.format(str(key), b=value_str, align="<", max_key_len=max_key_len)
    return dict_str[:-1]


"""functions that are not used for task_generation, but are highly relevant and are used elsewhere"""

# gets the connections (position to multiple positions) and inverse nodes (function name to position)
def get_ifg_connections_invnodes(inv_func_call_graph:dict)->tuple[list[list],dict]:
    ifg_n = inv_func_call_graph["nodes"]
    ifg_c = inv_func_call_graph["connections"]
    # put the connections into a 2D list
    connections = convert_ifg_connections_list_to_set(ifg_c) # fills in connections to the indicies it sees
    for _ in range(len(ifg_n)-len(connections)): connections.append(set())
    # inverse nodes to quickly find certain functions
    inv_nodes = {}
    for i in range(len(ifg_n)):
        node = ifg_n[i]
        if isinstance(node, str): continue
        fname = node[0]
        if fname not in inv_nodes: inv_nodes[fname] = i
    # return the connectiosn and inverse nodes
    return connections, inv_nodes

# gathers the inverse function call directed graph for a function of a domain, given that the action is a part of the domain
def dfsgather_ifg_func(domain_system, domain_assistant:dict, action:str, default_dependency_option:str,
    ifg_processed_conns:bool=True)->dict|tuple[list,list,dict]:
    if action not in domain_assistant.action_descriptions: return None
    # variable loading
    ard = domain_assistant.action_required_dependencies
    acd = domain_assistant.action_customizable_dependencies
    cl = domain_assistant.constraint_links
    cp = domain_assistant.constraint_processes
    action_default_dep_orig = gather_action_default_dependencies(ard, acd, default_dependency_option=default_dependency_option)
    action_parameters = get_action_parameters(domain_system, domain_assistant)
    # process the graph
    dep_orig = action_default_dep_orig[action]
    user_goal_node = (action, {key: key for key in action_parameters[action]})
    inv_func_call_graph = dfsgather_invfunccalldirgraph(dep_orig, cl, cp, action_default_dep_orig, action_parameters, user_goal_node)    
    if not ifg_processed_conns: return inv_func_call_graph
    nodes = inv_func_call_graph["nodes"]
    connections, inv_nodes = get_ifg_connections_invnodes(inv_func_call_graph)
    return nodes, connections, inv_nodes