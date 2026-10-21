"""
task generation based on the domain to test domain functions

Problems with the current domain setup (none of which are present in the current domains, though it is theoretically possible):

Two key problems relating action_dep_links (not a problem for action_constraint_dependencies):
During parameter list discovery for the user_known, and when constructing the function call tree,
when linking a dependency to an action, the action will require more parameters than the dependency,
and the new additional parameters in the action compared to the dependency are not updated accordingly.
Case in point:
Action transfer_funds needs user1 and user2 to both login.
The constraint to check is logged_in_user with usernames.
The new and unique identification parameters for each user is not discovered.

Problem with action_dep_link:
More than one action may change the state of the domain.

Problem with directed graph construction:
Depending on the constraint, some actions may not need to be called to verify the constraint if the constraint is "or".
"""


"""imports"""

from env.check_data_sanity import recur_data_consistency, check_data_sanity, run_domain_tests
from env.variables import domain_keys, domain_assistant_keys
from env.dep_eval import Dependency_Evaluator_Verify
from env.file_read_write import write_tasks

import inspect
import copy
import json
import re
import string
import random
from tqdm import tqdm
from textwrap import dedent
from itertools import chain, combinations, product
from collections import deque


from openai import OpenAI, LengthFinishReasonError
from openai.types.beta.threads.run import Usage
from pydantic import BaseModel, Field, model_validator


"""generates permutations of the constraints to create dependencies for each task"""

from env.helpers import InvalidConstraintOption,\
    inv_constr, inv_dep, modify_prompt, get_action_full_description, get_domain_dependency_none, get_action_parameters,\
    dict_to_tuple, tuple_to_dict, hashable_dep, orig_dep

from env.helpers import\
    check_dep_seen_or_encapsulated, dfsremove_if_unnecessary, dfscollapse_dep, dfsprune_dep_pro,\
    get_new_param_mapping, dfsgather_constr_singles_dep_set, dfsgather_constr_singles_dep_list, dfsgather_param_names_dep,\
    dfsplace_param_names, dfsins_constr_deps, gather_action_default_dependencies, dfsins_innate_deps,\
    get_cl_param_mapping, dfsins_constr_links, dfsins_cl_cd_aid

# specifically checks for xor or xnor cases, where we need to allow for k = max
def check_xor_xnor(dep:tuple)->bool:
    if not dep or dep[0] != "or" or len(dep[1]) != 2: return False
    if dep[1][0][0] != "and" or dep[1][1][0] != "and" or len(dep[1][0][1]) != 2 or len(dep[1][1][1]) != 2: return False
    and0_dep0 = hashable_dep(dep[1][0][1][0])
    and0_dep1 = hashable_dep(dep[1][0][1][1])
    and1_invdep0 = hashable_dep(inv_dep(dep[1][1][1][0], True))
    and1_invdep1 = hashable_dep(inv_dep(dep[1][1][1][1], True))
    return and0_dep0 == and1_invdep0 and and0_dep1 == and1_invdep1 or and0_dep0 == and1_invdep1 and and0_dep1 == and1_invdep0

# finds the number of permutations in a permutation dictionary
def num_permutations(perm_dict:dict)->int: return len(perm_dict[list(perm_dict.keys())[0]])

# given the True/False of each dep in the list and the ind_perm denoting which is T/F, we construct the constraint permutation
def get_dep_combs(dep:tuple, list_dep_perms_part:list, set_dep_perms_part_constr:set, ind_fail:tuple, ind_skip:tuple=tuple())->dict[tuple:list]:
    # making sure ind_fail and ind_skip are mutually exclusive, prioritizing ind_fail
    ind_skip = tuple([item for item in ind_skip if item not in ind_fail])
    # add the appropriate permutation for these indicies
    list_dep_part = []
    ind_fail_counter, ind_skip_counter = 0, 0
    for i in range(len(dep[1])):
        # True case: not in fail nor skip
        if not (ind_fail_counter < len(ind_fail) and i == ind_fail[ind_fail_counter]
            or ind_skip_counter < len(ind_skip) and i == ind_skip[ind_skip_counter]):
            list_dep_part.append(copy.deepcopy(list_dep_perms_part[i][True]))
        # False case: in fail
        elif ind_fail_counter < len(ind_fail) and i == ind_fail[ind_fail_counter]:
            list_dep_part.append(copy.deepcopy(list_dep_perms_part[i][False]))
            ind_fail_counter += 1
        # Skip case: in skip
        else:
            list_dep_part.append({key:[-1] for key in list_dep_perms_part[i][True]})
            ind_skip_counter += 1
    # find the lengths of the sets for each dep in this list, index combinations
    list_dep_part_length_range = [list(range(num_permutations(ele_dep_part))) for ele_dep_part in list_dep_part]
    list_dep_ind_comb = list(product(*list_dep_part_length_range))
    # combine the constraints, detecting conflicts
    list_dep_comb = {key:[] for key in set_dep_perms_part_constr}
    for dep_ind_comb in list_dep_ind_comb:
        dep_comb = {}
        conflict_bool = False
        for i in range(len(list_dep_part)):
            for key in list_dep_part[i]:
                if key not in dep_comb or dep_comb[key] < 0: dep_comb[key] = list_dep_part[i][key][dep_ind_comb[i]]
                else: conflict_bool = list_dep_part[i][key][dep_ind_comb[i]] >= 0 and dep_comb[key] != list_dep_part[i][key][dep_ind_comb[i]]
                if conflict_bool: break
            if conflict_bool: break
        if conflict_bool: continue
        for key in list_dep_comb: list_dep_comb[key].append(dep_comb[key])
    # return the result
    return list_dep_comb

# given a dependency, returns a dictionary of success and failure cases of all possible permutations of of the constraints in this dependency
# p choose k failures in "and" (one success case) and successes in "or" (one failure case), -1 means maximum permutation
# rang denotes only k specifically, or in a range [0, k], False / True
def get_dep_perms(dep:tuple, k:int=-1, range_bool:bool=True)->dict[bool:dict]:
    if k <= -1: range_bool = True
    # base case None and single
    if not dep: return None
    if dep[0] == "single":
        dep_perm = None
        not_in_constr = "not " in dep[1]
        constr_str = re.sub("not ", "", dep[1])
        if not_in_constr: dep = ("single", constr_str, dep[2])
        dep_perm = {not not_in_constr: {hashable_dep(dep):[1]}, not_in_constr: {hashable_dep(dep):[0]}}
        return dep_perm
    # process sub-permuations
    xor_or_xnor_bool = check_xor_xnor(dep)
    if xor_or_xnor_bool: k = -1
    list_dep_perms_part = [get_dep_perms(dep=ele_dep, k=k, range_bool=range_bool) for ele_dep in dep[1]]
    set_dep_perms_part_constr = set()
    for dep_perms_part in list_dep_perms_part: set_dep_perms_part_constr.update(dep_perms_part[True].keys())
    # recursive case of all types of permutations    
    dep_perms = {True: {key:[] for key in set_dep_perms_part_constr}, False: {key:[] for key in set_dep_perms_part_constr}}
    match dep[0]:
        # both cases need permutations of success and failure
        case "and" | "or":
            and_bool = dep[0] == "and"
            # control the range of k needed for the appropriate cases
            def n_choose_k_indices(n, k): return list(combinations(range(n), k))
            max_k = len(dep[1]) if k <= -1 or len(dep[1]) <= k else min(len(dep[1]), k)
            min_k = 0 if range_bool else max_k
            k_values = list(range(min_k, max_k+1))
            if min_k != 0 and range_bool: k_values.insert(0, 0) # add the success case of "and" and the failure case of "or" if we have not already
            if xor_or_xnor_bool: k_values.append(len(dep[1])) # add the all fail (and) and all success (or) case, for xor calculations
            # process the permutations, for each k chosen elements, "and" k failures, "or" k successes
            for k_i in k_values:
                k_fails = k_i if and_bool else len(dep[1]) - k_i
                list_index_permutation = n_choose_k_indices(len(dep[1]), k_fails) # indicies of the constraints to fail
                for ind_fail in list_index_permutation:
                    # get the constraint cobinations based on the T/F of each dependency in the list, and the ind_perm
                    list_dep_comb = get_dep_combs(dep, list_dep_perms_part, set_dep_perms_part_constr, ind_fail)
                    # this is a success or failure case based on if this is "and" or "or"
                    succ_or_fail = and_bool ^ (k_i != 0)
                    for key in list_dep_comb: dep_perms[succ_or_fail][key].extend(list_dep_comb[key])
        case "chain" | "gate":
            chain_bool = dep[0] == "chain"
            def ith_pos_chosen(i:int, not_flip_bool:bool)->tuple: return (i,) if not_flip_bool else (range(i))
            list_index_permutation = [ith_pos_chosen(i, chain_bool) for i in range(len(dep[1])+1)] # index of failure for "chain" or success for "gate"
            #list_index_permutation.append(tuple())
            list_skip_permutation = [tuple([j for j in range(i+1, len(dep[1]))]) for i in range(len(dep[1])+1)]
            #list_skip_permutation.append(tuple())
            for i in range(len(list_index_permutation)):
                ind_fail = list_index_permutation[i]
                ind_skip = list_skip_permutation[i]
                list_dep_comb = get_dep_combs(dep, list_dep_perms_part, set_dep_perms_part_constr, ind_fail, ind_skip)
                succ_or_fail = chain_bool == (i == len(list_index_permutation) - 1)
                for key in list_dep_comb: dep_perms[succ_or_fail][key].extend(list_dep_comb[key])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return dep_perms

# limits the number of tasks to at most some constant, the keys of adt at this point are the hashed constraints
def limit_num_tasks(action_dep_tasks:dict, n:int=4)->dict:
    adt = action_dep_tasks.copy()
    if num_permutations(action_dep_tasks) <= n: return adt
    rand_inds = set(random.sample(range(0, num_permutations(action_dep_tasks)), n))
    return {hashed_constr: [adt[hashed_constr][i] for i in range(len(adt[hashed_constr])) if i in rand_inds] for hashed_constr in adt}

# determines if the values at the common keys are the same
def check_dict_common_values(d1:dict, d2:dict)->bool:
    common_keys = set(d1.keys()) & set(d2.keys())
    num_matches = 0
    for key in common_keys: num_matches += d1[key] == d2[key] or d1[key] < 0 or d2[key] < 0
    return len(common_keys) == num_matches

# finds a suitable constraint combination that works with the other constraint combination
def find_suitable_constr_comb(acdt:dict, action_req_dep_tasks_succ:dict)->dict:
    # tries to find a match among the other successful req_dep
    num_perms = num_permutations(action_req_dep_tasks_succ)
    for ind in range(num_perms):
        ardt = {key: action_req_dep_tasks_succ[key][ind] for key in action_req_dep_tasks_succ}
        if check_dict_common_values(acdt, ardt): return ardt
    # cannot find a match
    return None

# combines the constraint values of the action_req_dep_tasks and action_cus_dep_tasks, chain relation between req and cus
def combine_req_cus_dep_tasks(action_req_dep_tasks_succ:dict, action_cus_dep_tasks:dict)->dict:
    action_dep_tasks = {}
    added_task_bool = False
    for succ_fail in action_cus_dep_tasks:
        action_dep_tasks[succ_fail] = {key:[] for key in set(action_req_dep_tasks_succ.keys()) | set(action_cus_dep_tasks[succ_fail].keys())}
        num_perms = num_permutations(action_cus_dep_tasks[succ_fail])
        for i in range(num_perms):
            acdt = {key: action_cus_dep_tasks[succ_fail][key][i] for key in action_cus_dep_tasks[succ_fail]}
            ardt_succ = find_suitable_constr_comb(acdt, action_req_dep_tasks_succ)
            if not ardt_succ: continue
            added_task_bool = True
            action_dep_task = {key: ardt_succ[key] if key not in acdt or key in ardt_succ and ardt_succ[key] > -1 else acdt[key]
                for key in set(ardt_succ.keys()) | set(acdt.keys())}
            for key in action_dep_tasks[succ_fail]: action_dep_tasks[succ_fail][key].append(action_dep_task[key])
    return action_dep_tasks if added_task_bool else None

# calculates the permutations of dependencies for tasks
# inserts the innate dependencies for permutation calculation, then removes them for later functional graph calculation
def dependency_permutations(user_goal:str, aid:dict, ard:dict, acd:dict,
    constr_links:dict, constr_deps:dict, act_def_deps:dict, action_parameters:dict={},
    k:int=1)->list[tuple[tuple,tuple,tuple,dict]]:
    # for each permutation of dependencies between required and customizable, generate the task, with failing conditions
    action_req_dep = ard[user_goal]
    action_cus_dep = None
    if isinstance(acd[user_goal], list): action_cus_dep = acd[user_goal]
    elif acd[user_goal]: action_cus_dep = [acd[user_goal]]
    action_dependencies = [] # includes req_dep failures, and then permutations of req and cust success and failures
    if not action_req_dep and not action_cus_dep: return [(None, None, None, {True:{None:[1]}, False:{None:[]}})]
    # create the customizable dependency permutations
    list_action_cus_dep = []
    def all_subsets(ss): return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1))) if ss else []
    for subset in all_subsets(action_cus_dep):
        subset = list(subset)
        if len(subset) == 0: continue
        elif len(subset) == 1: list_action_cus_dep.append(subset[0])
        else: list_action_cus_dep.append(("and", subset))
    # insert constraint dependencies
    action_req_dep_actu = dfsins_constr_deps(action_req_dep, act_def_deps, constr_deps)
    action_req_dep_perm = dfsins_cl_cd_aid(action_req_dep, constr_links, aid, act_def_deps, constr_deps, action_parameters)
    if aid[user_goal]:
        action_req_dep_inna = dfsins_cl_cd_aid(aid[user_goal], constr_links, aid, act_def_deps, constr_deps, action_parameters)
        if action_req_dep_perm: action_req_dep_perm = ("and", [action_req_dep_inna, action_req_dep_perm])
        else: action_req_dep_perm = action_req_dep_inna
    list_action_cus_dep_actu = [dfsins_constr_deps(action_cus_dep, act_def_deps, constr_deps)
        for action_cus_dep in list_action_cus_dep]
    list_action_cus_dep_perm = [dfsins_cl_cd_aid(action_cus_dep, constr_links, aid, act_def_deps, constr_deps, action_parameters)
        for action_cus_dep in list_action_cus_dep]
    # get the action_req_dep dependency permutations
    action_req_dep_tasks = get_dep_perms(action_req_dep_perm, k, range_bool=True)
    if action_req_dep: action_dependencies.append((action_req_dep, action_req_dep_actu, action_req_dep_perm, action_req_dep_tasks))
    if action_req_dep and not action_req_dep_tasks[True]:
        action_req_dep_tasks = get_dep_perms(action_req_dep_perm)
        action_req_dep_tasks[True] = limit_num_tasks(action_req_dep_tasks[True])
        action_req_dep_tasks[False] = limit_num_tasks(action_req_dep_tasks[False])
    # connecting the a suitable action_req_dep with action_cust_dep permutations
    for i in range(len(list_action_cus_dep)):
        # get the customizable constraint permutations
        action_cus_dep = list_action_cus_dep[i]
        action_cus_dep_actu = list_action_cus_dep_actu[i]
        action_cus_dep_perm = list_action_cus_dep_perm[i]
        action_cus_dep_tasks = get_dep_perms(action_cus_dep_perm, k, range_bool=True)
        if not action_req_dep_perm:
            action_dependencies.append((action_cus_dep, action_cus_dep_actu, action_cus_dep_perm, action_cus_dep_tasks))
            continue
        if not action_req_dep_tasks[True]: continue
        # combine the required and customizable tasks, trying all possibilities if it fails (the nuclear option)
        action_dep_tasks = combine_req_cus_dep_tasks(action_req_dep_tasks[True], action_cus_dep_tasks)
        if not action_dep_tasks or not num_permutations(action_dep_tasks[True]) or not num_permutations(action_dep_tasks[False]):
            action_req_dep_tasks_all = get_dep_perms(action_req_dep_perm)
            action_cus_dep_tasks_all = get_dep_perms(action_cus_dep_perm)
            action_dep_tasks = combine_req_cus_dep_tasks(action_req_dep_tasks_all[True], action_cus_dep_tasks_all)
            if num_permutations(action_dep_tasks[True]) or num_permutations(action_dep_tasks[False]):
                action_dep_tasks[True] = limit_num_tasks(action_dep_tasks[True])
                action_dep_tasks[False] = limit_num_tasks(action_dep_tasks[False])
            else: continue
        # record the results
        action_dep_orig =   dfsprune_dep_pro(("and", [action_req_dep, action_cus_dep]))             if action_req_dep else action_cus_dep
        action_dep =        dfsprune_dep_pro(("and", [action_req_dep_actu, action_cus_dep_actu]))   if action_req_dep_actu else action_cus_dep
        action_dep_perm =   dfsprune_dep_pro(("and", [action_req_dep_perm, action_cus_dep_perm]))
        action_dependencies.append((action_dep_orig, action_dep, action_dep_perm, action_dep_tasks))
    # returning a list of tuples with the dependency and the contraint permutations
    return action_dependencies

# removing tasks with the call_ constraints set to false
def remove_call_constr_false(action_dependencies:list[tuple])->list[tuple]:
    counter_act_deps = 0
    while counter_act_deps < len(action_dependencies):
        dep_orig, _, _, task = action_dependencies[counter_act_deps]
        if not dep_orig:
            counter_act_deps += 1
            continue
        call_constrs = dfsgather_constr_singles_dep_set(dep_orig)
        call_constrs = set(call_constr for call_constr in call_constrs if call_constr[1].startswith("call_"))
        dep_has_task_bool:bool = False
        for succ_or_fail in task:
            # gather the indicies with call constraint failures and remove the call constraints
            pos_call_fails = set()
            for h_cc in call_constrs:
                pos_call_fails |= set(i for i in range(len(task[succ_or_fail][h_cc])) if not task[succ_or_fail][h_cc][i])
            # remove the tasks with those
            for hashed_constr in task[succ_or_fail]:
                task[succ_or_fail][hashed_constr] = [task[succ_or_fail][hashed_constr][i]
                    for i in range(len(task[succ_or_fail][hashed_constr])) if i not in pos_call_fails]
            # record if the dependency still has tasks
            if not dep_has_task_bool and task[succ_or_fail] and num_permutations(task[succ_or_fail]) > 0: dep_has_task_bool = True
        if dep_has_task_bool: counter_act_deps += 1
        else: action_dependencies.pop(counter_act_deps)
    return action_dependencies

"""gathering dependency information"""

# verbalizes a list or set into English
def verbalized_list_values(list_values:str|list[str]|set[str], add_quotations:bool=True)->str: # verbalizes lists of values
    if isinstance(list_values, str): return list_values
    def aqs(s:str, add_quotations:bool): # add_quotation_str, adds quotations around strings
        return f"\"{s}\"" if add_quotations else f"{s}"
    list_values_copy = list_values if isinstance(list_values, list) else list(list_values)
    if not list_values_copy: return "" # ideally will not hit
    if len(list_values_copy) == 1: return f"{aqs(list_values_copy[0],add_quotations)}"
    if len(list_values_copy) == 2: return f"{aqs(list_values_copy[0],add_quotations)} and {aqs(list_values_copy[1],add_quotations)}"
    res = f"{aqs(list_values_copy[0],add_quotations)},"
    for i in range(1, len(list_values_copy)-1): res += f" {aqs(list_values_copy[i],add_quotations)},"
    res += f" and {aqs(list_values_copy[-1],add_quotations)}"
    return res

# dfs find the needed parameters for this dependency
# problem: does not consider when two different constraints have the same variable names, like two users must be logged in
def dfsgather_params_task(task:dict)->set:
    user_params = set()
    for key in task:
        if task[key] < 0: continue
        constr = orig_dep(key)
        if constr: user_params = user_params.union({value for value in constr[2].values() if "value " not in value})
    return user_params

# gathers the verbalized constraints
def gather_verb_constrs(task_single:dict, pcd:dict, ncd:dict,
    example_dep_param:dict, set_state_tracker_constr_str:set, verification_result_collective:dict={})->str:
    verb_constrs = ""
    constr_counter = 1
    for key in task_single:
        if task_single[key] < 0: continue
        # constraint extraction
        constr = orig_dep(key)
        if not constr: continue
        constr_str = re.sub("not ", "", constr[1])
        # variable mapping
        variable_mapping = copy.deepcopy(constr[2])
        for vm_key in variable_mapping:
            variable_mapping[vm_key] = variable_mapping[vm_key]\
                if "value " not in variable_mapping[vm_key] else ("the literal value " + re.sub("value ", "", variable_mapping[vm_key]))
        variable_mapping.update({key:key for key in example_dep_param}) # circular logic if we plug in values
        # gather parameters needed
        constr_params = [constr[2][key] for key in constr[2] if "value " not in constr[2][key]]
        verb_constr_params = f"Consider the parameter(s) {verbalized_list_values(constr_params)}." if constr_params else "No parameters."
        if False and constr_str in set_state_tracker_constr_str: # not perfect as there are state tracker constraints that don't use the dep_params
            verb_constr_params += " Perhaps consider the dependency parameters."
        # getting the appropriate description
        verb_constr = ""
        if task_single[key]: verb_constr = pcd[constr_str]
        else: verb_constr = ncd[constr_str]
        # emphasizing strength
        emphasize_strength = int(verification_result_collective[key]**1.3) if key in verification_result_collective else 0
        emphasize_str = "(importance weight " + str(emphasize_strength) + ") " if emphasize_strength > 0 else ""
        # overarching string construction
        verb_constrs += f"{constr_counter}. {emphasize_str}{verb_constr.format(**variable_mapping)} {verb_constr_params}\n"
        constr_counter += 1
    return verb_constrs[:-1] if verb_constrs else "No constraints to consider."

# gathers the action parameter types from the large list of types
def gather_action_parameter_types(domain_str:str)->dict:
    actions = domain_assistant_keys[domain_str].actions
    action_parameter_types = {}
    for action in actions:
        properties = action["parameters"]["properties"]
        for prop in properties:
            list_type = None
            if "type" in properties[prop]: list_type = properties[prop]["type"]
            else: list_type = [d["type"] for d in properties[prop]["anyOf"]]
            action_parameter_types[prop] = list_type
    return action_parameter_types


"""AI task generation"""

# output parser for the tast
class Task(BaseModel):
    initial_database_str:str = Field(description="json formatted python dict, initial existing database,"\
        + " you must not modify the python dictionary keys, only the necessary values, use double quotes for strings")
    user_known_str:str = Field(description="json formatted python dict, limited user known parameter values,"\
        + " combined with the user goal and initial database to reach the desired outcome, use double quotes for strings")
    dependency_parameters_str:str = Field(description="the dependency parameters to influence the dependencies,"\
        + " you must not modify the python dictionary keys, only the necessary values, use double quotes for strings")
    @model_validator(mode="before")
    @classmethod
    def check_task(cls, values: dict) -> dict:
        try:
            _ = json.loads(values["initial_database_str"])
        except json.decoder.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data for initial_database_str: {e.msg}\nDocument: {e.doc}\nPosition: {e.pos}\nData: {values['initial_database_str']}") from e
        try:
            _ = json.loads(values["dependency_parameters_str"])
        except json.decoder.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data for dependency_parameters_str: {e.msg}\nDocument: {e.doc}\nPosition: {e.pos}\nData: {values['dependency_parameters_str']}") from e
        try:
            _ = json.loads(values["user_known_str"])
        except json.decoder.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data for user_known_str: {e.msg}\nDocument: {e.doc}\nPosition: {e.pos}\nData: {values['user_known_str']}") from e
        return values
def task_obj_str(task_obj:Task)->str:
    res = json.dumps(json.loads(task_obj.initial_database_str), indent=2)
    res += '\n' + json.dumps(json.loads(task_obj.dependency_parameters_str), indent=2)
    res += '\n' + json.dumps(json.loads(task_obj.user_known_str), indent=2)
    return res

# replace the unknown or wrong parameters in the initial database
replaceable_words = ["unknown", "wrong", "non_existent", "nonexistent"]
def dfsreplace_placeholder(input_dict:dict|list|str)->dict|str:
    global replaceable_words
    if not isinstance(input_dict, str) and not isinstance(input_dict, dict) and not isinstance(input_dict, list): return input_dict
    elif isinstance(input_dict, str):
        if any(word in input_dict.lower() for word in replaceable_words):
            return ''.join(random.choices(string.ascii_letters, k=len(input_dict)))
        return input_dict
    if isinstance(input_dict, dict):
        input_dict = {key:dfsreplace_placeholder(input_dict[key]) for key in input_dict}
    else: input_dict = [dfsreplace_placeholder(ele) for ele in input_dict]
    return input_dict


"""verification and post generation processing"""

from env.helpers import merge_sequences, dfsgather_actions_required

# verifies that the formats between the initial and example database are the same, returns the new database if fitting was needed
def verify_database_format(initial_database:dict, example_database:dict)->tuple[bool,str]:
    if not recur_data_consistency(initial_database, example_database):
        example_database_copy = copy.deepcopy(example_database)
        for key in initial_database: example_database_copy[key] = copy.deepcopy(initial_database[key])
        if not recur_data_consistency(example_database_copy, example_database):
            return False, None
        else: initial_database = example_database_copy
    return True, initial_database

# returns a copy of a parameter dict with values from a larger dict
def configure_func_parameters(input_params:dict, func_param_names:set)->dict:
    return {param_name:input_params[param_name] for param_name in func_param_names if param_name in input_params}

# returns a set of constraints with result -1 based on the dictionary of constraint results and chain/gate relations
def gather_undetermined_constr_set_recur(dep:tuple, constr_results:dict)->tuple[set,int]:
    constr_set, dep_result = set(), -1
    if not dep: return constr_set
    match dep[0]:
        case "single":
            constr_tuple = (dep[0], re.sub("not ", "", dep[1]), dict_to_tuple(dep[2]))
            if constr_tuple in constr_results: dep_result = constr_results[constr_tuple]
        case "and" | "or":
            and_bool:bool = dep[0] == "and"
            for ele in dep[1]:
                constr_set_part, dep_result_part = gather_undetermined_constr_set_recur(ele, constr_results)
                constr_set |= constr_set_part
                # records the "and" True and "or" False once, opposite results multiple times
                if dep_result_part > -1 and (and_bool != dep_result_part or dep_result == -1): dep_result = dep_result_part
        case "chain" | "gate":
            and_bool:bool = dep[0] == "chain"
            i:int = 0
            # loop through the list
            while i < len(dep[1]):
                constr_set_part, dep_result_part = gather_undetermined_constr_set_recur(dep[1][i], constr_results)
                constr_set |= constr_set_part
                if dep_result_part > -1:
                    if and_bool != dep_result_part: break
                    dep_result = dep_result_part
                i += 1
            # check if the list is fully traversed
            if i == len(dep[1]): return constr_set, dep_result
            dep_result = not and_bool
            for j in range(i+1, len(dep[1])): constr_set |= dfsgather_constr_singles_dep_set(dep[1][j])
        case _: raise InvalidConstraintOption(f"invalid dependency option selected: {dep[0]}")
    return constr_set, dep_result
def gather_undetermined_constr_set(dep:tuple, constr_results:dict)->set:
    constr_set, _ = gather_undetermined_constr_set_recur(dep, constr_results)
    return constr_set

# verifies the success of the AI generation with respect to the dependency, actions required determined by constraint links
class VerifierDiscrepancy(Exception): pass
def verify_gen_succ(task_obj:Task, dep:tuple, dep_perm:tuple, domain_str:str, user_goal:str,
    act_innate_deps:dict[str:tuple], act_def_deps:dict[str:tuple], act_def_dep_perms:dict,
    actions_required:list, task_single:dict, task_succ:bool,
    cl:dict, cd:dict, action_parameters:dict)->tuple[bool,dict]:
    # initialize the variables to the verifying process
    all_dep = copy.deepcopy(act_def_deps)
    all_dep[user_goal] = dep
    data = json.loads(task_obj.initial_database_str)
    dep_params = json.loads(task_obj.dependency_parameters_str)
    domain_system_strict = domain_keys[domain_str+"_strict"](data, act_innate_deps, all_dep, dep_params)
    domain_system = domain_system_strict.evaluation_get_domain_system()
    dependency_evaluator = domain_system_strict.evaluation_get_dependency_evaluator()
    state_tracker = domain_system_strict.evaluation_get_state_tracker()
    user_known = json.loads(task_obj.user_known_str)
    # initialize the constraint verifier to check if the generated scenario follows the constraints
    all_dep_perm = copy.deepcopy(act_def_dep_perms)
    all_dep_perm[user_goal] = dep_perm
    act_innate_dep_perms = {key: dfsins_cl_cd_aid(act_innate_deps[key], cl, act_innate_deps, act_def_deps, cd, action_parameters) for key in act_innate_deps}
    domain_system_perm = domain_keys[domain_str](copy.deepcopy(data), act_innate_dep_perms, dep_params)
    domain_dep_ver = Dependency_Evaluator_Verify(database=domain_system_perm, state_tracker=copy.deepcopy(state_tracker),
        all_dep=all_dep_perm, constraint_values=task_single)
    # run through the required actions, making sure the constraints in task_single are satisfied
    constr_values_fully_followed = True
    user_goal_succ_verified = not bool(actions_required)
    dss_pass = True
    dependency_evaluator_before_ug = dependency_evaluator
    for action, action_params in actions_required:
        action_params = get_new_param_mapping(user_known, action_params)
        signature = inspect.signature(getattr(domain_system, action))
        action_param_names = {k for k, v in signature.parameters.items()
            if v.default is inspect.Parameter.empty and v.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)}
        missing_param_names = action_param_names - set(action_params.keys())
        # check if the constraints match what we expect
        func_dep_pass, func_dep_follow_constr_values = domain_dep_ver.process(action, **user_known) # states in the state tracker are irrelevant
        if missing_param_names: ds_perm_res = False
        elif func_dep_pass: ds_perm_res = getattr(domain_system_perm, action)(**get_new_param_mapping(user_known, {key: key for key in action_parameters[action]}))
        func_dep_pass = func_dep_pass and (ds_perm_res if isinstance(ds_perm_res, bool) else ds_perm_res[0])
        if action == user_goal: dependency_evaluator_before_ug = copy.deepcopy(dependency_evaluator) # copying constraints before user_goal action
        # call the domain to change the state tracker and verify
        if missing_param_names: dss_pass = False
        elif dss_pass and constr_values_fully_followed: dss_pass = getattr(domain_system_strict, action)(**action_params)
        if isinstance(dss_pass, tuple): dss_pass = dss_pass[0]
        # sanity and final result check
        if func_dep_pass != dss_pass and constr_values_fully_followed:
            error_str = f"func_dep_pass {func_dep_pass} dss_pass {dss_pass} constr_values_fully_followed {constr_values_fully_followed}"\
                + f"\naction {action} action_params {action_params}"
            raise VerifierDiscrepancy(f"discrepancy found between the domain system strict and the domain dependency verifier\n{error_str}")
        constr_values_fully_followed = constr_values_fully_followed and func_dep_follow_constr_values
        if action == user_goal and func_dep_pass == task_succ: user_goal_succ_verified = True 
    # calculate the actual results, useful for diagnostics, after actions taken
    single_constrs_ordered = dfsgather_constr_singles_dep_list(dep_perm)
    actual_results = {}
    for key in single_constrs_ordered:
        target_result = task_single[key]
        if key in actual_results: continue
        dep_perm_single = dfsins_cl_cd_aid(orig_dep(key), cl, act_innate_deps, act_def_deps, cd, action_parameters)
        actual_result = int(dependency_evaluator_before_ug._process(dep_perm_single, **user_known)) if task_single[key] >= 0 else target_result
        actual_results[key] = actual_result
        undetermined_constr_set:set = gather_undetermined_constr_set(dep_perm, actual_results)
        for ele in undetermined_constr_set: actual_results[ele] = -1
    # return the verification result and diagnostics, verification results has (target_result, actual_result) tuples as values
    verification_results = {key: (task_single[key], actual_results[key]) for key in single_constrs_ordered}
    return constr_values_fully_followed and user_goal_succ_verified, verification_results


"""post processing functions"""

from env.helpers import\
    dfsgather_setfunccall_ifg, update_inv_func_graph_single, hash_node, dfscheck_same_andornode, ifg_pos_of_node, update_inv_func_graph,\
    dfsgather_inv_func_graph_process, dfsgather_inv_func_graph_dependency,\
    convert_ifg_connections_set_to_list, convert_ifg_connections_list_to_set, change_nodeorder_invfuncgraph,\
    dfsgather_invfunccalldirgraph, renumber_nodes, prune_ifg,\
    bfsconvert_ifg_to_tree, bfsconvert_tree_to_ifg

# generates a verbalization of the user goal with parameters added in
prompt_ugv_template = """
    Task: Generate a simple statement on and describe what I, the user, am trying to do with this action and information.
    I am the user. Please address me in the second person, as "you".
    I only know the action name and am not fully aware of the details of the action description.
    Below, there is the action description, describing what the action I am trying to do, and relevent parameters for this action in parameter descriptions.
    Incorporate as many of the parameters as you can in the statement to enhance the statement.
    No explanation, just a simple statement of one or two sentences.
    \n\nData:
    \nAction description: {user_goal_desc}
    \nParameter descriptions: {param_descs}
    \n\nMy goal:
"""
def generate_verb_user_goal(user_goal_desc:str, param_descs:str,
    client:OpenAI, gpt_model:str, temperature:float, max_completion_tokens:int)->str:
    prompt_verb_user_goal = modify_prompt(prompt_ugv_template).format(
        user_goal_desc=user_goal_desc, param_descs=param_descs)
    messages = [{"role": "system", "content": dedent(system_prompt)}, {"role": "user", "content": prompt_verb_user_goal}]
    completion_verb_user_goal = client.beta.chat.completions.parse(messages=messages,
         model=gpt_model,temperature=temperature, max_completion_tokens=max_completion_tokens)
    verb_user_goal = completion_verb_user_goal.choices[0].message.content
    return verb_user_goal, completion_verb_user_goal.usage

# generates a verbalized user goal with all necessary information embedded in the prompt
prompt_ugvor_template = """
    Roleplay as a user to interact with the {domain_str} system.
    You should roleplay as a user has requests within the {domain_str} domain.
    \nYour goal is: {verb_user_goal}
    \nYour information that you know: {verb_user_known}
    \nEnsure that you include ALL and ONLY these requests and the information in a single message.
    \n\nYour message:
"""
def generate_verb_user_goal_oneround(verb_user_goal:str, user_known:dict, domain_str:str,
    client:OpenAI, gpt_model:str, temperature:float, max_completion_tokens:int)->str:
    # constructing the verbalized user known information
    verb_user_known = ""
    for parameter in user_known: verb_user_known += f"\"{parameter}\" is \"{user_known[parameter]}\". "
    verb_user_known = verb_user_known[:-1]
    # prompting the llm
    prompt_verb_user_goal_oneround = modify_prompt(prompt_ugvor_template).format(
        verb_user_goal=verb_user_goal, verb_user_known=verb_user_known, domain_str=domain_str)
    messages = [{"role": "system", "content": dedent(system_prompt)}, {"role": "user", "content": prompt_verb_user_goal_oneround}]
    completion_verb_user_goal_oneround = client.beta.chat.completions.parse(messages=messages,
         model=gpt_model,temperature=temperature, max_completion_tokens=max_completion_tokens)
    verb_user_goal_oneround = completion_verb_user_goal_oneround.choices[0].message.content
    return verb_user_goal_oneround, completion_verb_user_goal_oneround.usage


"""miscellaneous and diagnostic functions"""

from env.helpers import get_title_str, get_dict_str, get_ifg_connections_invnodes, dfsgather_ifg_func

# visualizes the dependency or process by dfs gathering  all needed action dependencies
def dfsgather_dep_tree_vis(dependency:tuple, user_goal:str="",
    constr_links:dict={}, action_deps:dict={}, constr_deps:dict={}, indent_amount:int=4)->str:
    indent_amount = max(indent_amount, 1)
    indent = ' ' * indent_amount
    direct_indent = '+' + '-' * (indent_amount-1)
    # none case
    if not dependency: return "None"
    # single and recursive case
    single_constraint = dependency[0] == "single"
    action_dep_tree = ""
    deps_to_loop = []
    if single_constraint:
        dependency_not = re.sub("not ", "", dependency[1])
        if dependency_not in constr_deps and constr_deps[dependency_not]: deps_to_loop.append((constr_deps[dependency_not], user_goal))
        if dependency_not in constr_links and constr_links[dependency_not]:
            user_goal_new = constr_links[dependency_not][0] if isinstance(constr_links[dependency_not], tuple) else constr_links[dependency_not]
            # assumes only gathering required dependencies, should be action_dependencies during simulation time
            deps_to_loop.append((action_deps[user_goal_new], user_goal_new))
    else: deps_to_loop.extend((dep, user_goal) for dep in dependency[1])
    for i in range(len(deps_to_loop)-1,-1,-1):
        dep, ug = deps_to_loop[i]
        action_dep_tree_part = dfsgather_dep_tree_vis(dep, ug, constr_links, action_deps, constr_deps)
        # constructing the tree
        action_dep_tree_part = re.sub('\n', f"\n{indent}", action_dep_tree_part)\
            if i==len(deps_to_loop)-1 else re.sub('\n', f"\n|{indent[:-1]}", action_dep_tree_part)
        action_dep_tree = f"\n{direct_indent}" + action_dep_tree_part + action_dep_tree
    action_dep_tree_beg = dependency[0] if not single_constraint\
        else f"{dependency[1]} {dependency[2]}"\
            if not action_dep_tree else f"{dependency[1]} {dependency[2]} (prereq)"
    action_dep_tree = action_dep_tree_beg + action_dep_tree
    # returns dependency tree string
    return action_dep_tree

# gets the string of a dependency and its tasks
def get_dep_task_str(dep_task:dict)->str:
    keys = None
    if True in dep_task and False in dep_task: keys = sorted(list(dep_task[True].keys()))
    else: keys = sorted(list(dep_task.keys()))
    dep_task_str = "keys"
    for key in keys: dep_task_str += f"\n{key}"
    if True in dep_task and False in dep_task:
        dep_task_str += f"\nsuccesses"
        for key in keys: dep_task_str += f"\n{dep_task[True][key]}"
        dep_task_str += f"\nfailures"
        for key in keys: dep_task_str += f"\n{dep_task[False][key]}"
    else:
        dep_task_str += f"\nvalues"
        for key in keys: dep_task_str += f"\n{dep_task[key]}"
    return dep_task_str

# string representation of the inverse function call graph
def get_inv_func_graph_str(inv_func_graph:dict)->str:
    inv_func_graph_nodes_str = '\n'.join([f"{i} {inv_func_graph['nodes'][i]}" for i in range(len(inv_func_graph["nodes"]))])
    inv_func_graph_connections_str = '\n'.join([str(conn) for conn in inv_func_graph["connections"]])
    inv_func_graph_str = f"nodes\n{inv_func_graph_nodes_str}\nconnections\n{inv_func_graph_connections_str}"
    return inv_func_graph_str

# visualization of the inverse function call graph
"""
Visualization Toolset:
Horizontal Line         ─   \u2500
Vertical Line           │   \u2502
Right Branching         ├   \u251C
Left Branching          ┤   \u2524
Down Branching          ┬   \u252C
Up Branching            ┴   \u2534
Top-Left Corner         ┌   \u250C
Top-Right Corner        ┐   \u2510
Bottom-Left Corner      └   \u2514
Bottom-Right Corner     ┘   \u2518
All Branching           ┼   \u253C
"""
def gather_ifg_graph_vis(inv_func_graph:dict, transpose_bool:bool=False)->str:
    nodes, conns_orig = inv_func_graph["nodes"], inv_func_graph["connections"] # index to node
    conns, _ = get_ifg_connections_invnodes(inv_func_graph) # node from to node to
    # Section: bfs calculate the levels of the graph, with the base level at the leaves
    # each level determined by distance to root or leaves, whichever is closer
    inv_conns = [set() for _ in range(len(conns))]
    for node_ind_from in range(len(conns)):
        node_conns = conns[node_ind_from]
        for node_ind_to in node_conns: inv_conns[node_ind_to].add(node_ind_from)
    node_to_level = [-1 for _ in nodes] # denotes the level that each node is on, with 0 at the leaves
    leaf_inds = [node_ind for node_ind in range(len(conns)) if not conns[node_ind]]
    for leaf_ind in leaf_inds: node_to_level[leaf_ind] = 0
    queue_ind = deque(leaf_inds) # adding the leaves
    while queue_ind:
        node_ind = queue_ind.popleft()
        for node_ind_from in inv_conns[node_ind]:
            node_to_level[node_ind_from] = node_to_level[node_ind]+1 if node_to_level[node_ind] >= 0 else 0
        queue_ind.extend(inv_conns[node_ind])
    queue_ind = deque([0]) # adding the root
    node_to_level[0] = -1
    pref_leaves = 3 # bigger the value, the "midpoint" will be closer to the leaves, preferring leaves
    while queue_ind:
        node_ind = queue_ind.popleft()
        for node_ind_from in conns[node_ind]:
            if -(node_to_level[node_ind]-1) < node_to_level[node_ind_from]+pref_leaves: node_to_level[node_ind_from] = node_to_level[node_ind]-1
        queue_ind.extend(conns[node_ind])
    max_level = max(0, *node_to_level) # longest distance from the leaves
    min_level = min(node_to_level) # longest distance from the root
    node_to_level = [level if level >= 0 else (level - min_level + max_level + 1) for level in node_to_level]
    max_level = max(node_to_level) # longest distance from the leaves
    # Section: lightly sorting the nodes of the same level, putting the boolean relations ahead of the actions
    level_to_order_to_node = [[] for _ in range(max_level+1)]
    for node_ind in range(len(node_to_level)): level_to_order_to_node[node_to_level[node_ind]].append(node_ind)
    def sort_tuples(tuple_list, index=0, reverse=False):
        if not tuple_list: return tuple_list
        return sorted(tuple_list, key=lambda x: x[index], reverse=reverse)
    def sort_nodes_rel_first(nodes:list, node_inds:list[int])->list[int]:
        # put the relations ahead
        pos_first_non_rel = -1
        i = 0
        while i < len(node_inds):
            if isinstance(nodes[node_inds[i]], str):
                if pos_first_non_rel >= 0:
                    ele = node_inds.pop(i)
                    node_inds.insert(pos_first_non_rel, ele)
                    pos_first_non_rel += 1
            else:
                if pos_first_non_rel < 0: pos_first_non_rel = i
            i += 1
        # sorted the relations based on alphabetical order
        if pos_first_non_rel < 0: pos_first_non_rel = len(node_inds)
        tuple_list = [(node_ind, nodes[node_ind]) for node_ind in node_inds[:pos_first_non_rel]]
        node_inds[:pos_first_non_rel] = [a for a, _ in sort_tuples(tuple_list, 1)]
        # sorting the other nodes based on alphabetical action name
        tuple_list = [(node_ind, nodes[node_ind][0]) for node_ind in node_inds[pos_first_non_rel:]]
        node_inds[pos_first_non_rel:] = [a for a, _ in sort_tuples(tuple_list, 1)]
        return node_inds 
    for i in range(len(level_to_order_to_node)): level_to_order_to_node[i] = sort_nodes_rel_first(nodes, level_to_order_to_node[i])
    node_to_y = [-1 for _ in nodes]
    for order_to_node in level_to_order_to_node:
        for order in range(len(order_to_node)): node_to_y[order_to_node[order]] = order
    # Section: calculating at which y (position top to bottom) should each node connection reside
    # nodes at each level are shifted to the top, connections do not cross nodes nor other connections
    # the offeset progenitor characters (point in the graph where each node receives and outputs all connections) are already considered
    connsorig_to_y = {conn_orig: -1 for conn_orig in conns_orig}
    levelnc_to_setyblocked = [] # level_to_y_to_nc: level 0 is root, maps the level to y to node/connection
    for i in range(max_level*2+1):
        level_appended = set(list(range(len(level_to_order_to_node[len(level_to_order_to_node)-1-i//2])))) if i % 2 == 0 else set()
        levelnc_to_setyblocked.append(level_appended)
    levelnc_to_nextavaispot = [len(ele) for ele in levelnc_to_setyblocked]
    # finds a suitable y for this connection to reside across these levels given these nodes and connections at various values of y
    def find_levelnc_ideal(levelnc_to_setyblocked:list, levelnc_fromto:tuple, levelnc_to_nextavaispot:list, levelncfrom_tempblocked:set, y_to:int)->int:
        set_y_blocked = set.union(levelncfrom_tempblocked, *levelnc_to_setyblocked[levelnc_fromto[0]:levelnc_fromto[1]+1])
        y_ideal = max(y_to, *levelnc_to_nextavaispot[levelnc_fromto[0]:levelnc_fromto[1]+1]) if levelnc_fromto[1]-levelnc_fromto[0] > 0 else y_to
        while y_ideal in set_y_blocked: y_ideal += 1 # guaranteed to stop
        return y_ideal
    # returns the filled levels with the new connection y
    def fill_with_connection(levelnc_to_setyblocked:list, levelnc_fromto:tuple, levelnc_to_nextavaispot:list, y_ideal:int)->tuple[list,list]:
        for levelnc in range(levelnc_fromto[0], levelnc_fromto[1]+1):
            levelnc_to_setyblocked[levelnc].add(y_ideal)
            while levelnc_to_nextavaispot[levelnc] in levelnc_to_setyblocked[levelnc]: levelnc_to_nextavaispot[levelnc] += 1
        return levelnc_to_setyblocked, levelnc_to_nextavaispot
    # each level with nodes and connections
    for level in range(len(level_to_order_to_node)-1, 0, -1):
        levelnc = (max_level - level) * 2 # levelnc of node_from
        levelncfrom_tempblocked = set([order for order in range(len(level_to_order_to_node[level])) if conns[level_to_order_to_node[level][order]]])
        # each node of the level
        for order in range(len(level_to_order_to_node[level])):
            node_from = level_to_order_to_node[level][order]
            levelncfrom_tempblocked.discard(order)
            # each connection of the node
            for node_to in conns[node_from]:
                levelnc_nt = (max_level - node_to_level[node_to]) * 2 # levelnc of node_to
                y_ideal = find_levelnc_ideal(levelnc_to_setyblocked, (levelnc+1, levelnc_nt-1), levelnc_to_nextavaispot, set(levelncfrom_tempblocked), node_to_y[node_to])
                levelnc_to_setyblocked, levelnc_to_nextavaispot = fill_with_connection(levelnc_to_setyblocked, (levelnc+1, levelnc_nt-1), levelnc_to_nextavaispot, y_ideal)
                connsorig_to_y[(node_from, node_to)] = y_ideal
    max_y = max(list(connsorig_to_y.values()), default=0)
    # Section: calculating the x +/- offset relative to the node layer of each progenitor node based on if it needs connections below its y position
    # checks if the progenitor node has a connection down, returns True if true
    def check_proge_connoverlap(connsorig_to_y:dict, prev_node:int, prev_node_conns:set, prev_y:int, curr_node:int, curr_node_conns:set, curr_y:int, from_to_bool:bool)->bool:
        prev_node_conn_tuple = [(prev_node, node_to) if from_to_bool else (node_to, prev_node) for node_to in prev_node_conns]
        curr_node_conn_tuple = [(curr_node, node_to) if from_to_bool else (node_to, curr_node) for node_to in curr_node_conns]
        prev_node_conn_range = [prev_y, *[connsorig_to_y[conn] for conn in prev_node_conn_tuple]]
        curr_node_conn_range = [curr_y, *[connsorig_to_y[conn] for conn in curr_node_conn_tuple]]
        prev_min_y, prev_max_y = min(prev_node_conn_range), max(prev_node_conn_range)
        curr_min_y, curr_max_y = min(curr_node_conn_range), max(curr_node_conn_range)
        return not (prev_max_y < curr_min_y or curr_max_y < prev_min_y) # second condition should be theoretically impossible
    levelp_to_proge_to_offset = [[] for _ in range(len(levelnc_to_setyblocked)-1)] # levelnc % 2 == 0 True (from progenitor) False (to progenitor), -1 means no proge node
    for levelnc in range(len(levelp_to_proge_to_offset)):
        from_to_bool:bool = levelnc % 2 == 0 # True for from, False for to
        levelp = max_level-(levelnc+1)//2
        for proge in range(0, len(level_to_order_to_node[levelp])):
            curr_node = level_to_order_to_node[levelp][proge]
            curr_node_conns = conns[curr_node] if from_to_bool else inv_conns[curr_node]
            if not curr_node_conns:
                levelp_to_proge_to_offset[levelnc].append(-1)
                continue
            elif proge == 0:
                levelp_to_proge_to_offset[levelnc].append(0)
                continue
            prev_node = level_to_order_to_node[levelp][proge-1]
            prev_node_conns = conns[prev_node] if from_to_bool else inv_conns[prev_node]
            proge_offset = 0
            if check_proge_connoverlap(connsorig_to_y, prev_node, prev_node_conns, proge-1, curr_node, curr_node_conns, proge, from_to_bool): proge_offset = 1
            levelp_to_proge_to_offset[levelnc].append(max(levelp_to_proge_to_offset[levelnc][:proge]) + proge_offset)
    # Section: calculate the max width and height of each string block
    # calculating the max width and height for each column and row of nodes, each node block will have the action followed by a list of the parameter mapping
    space = ' '
    levelr_to_order_to_node = list(reversed(level_to_order_to_node)) # reversed for convenience
    def transpose_blockstr(blockstr:str|list)->str|list:
        list_line = blockstr.split('\n') if isinstance(blockstr, str) else blockstr
        list_line_transposed = []
        for x in range(len(list_line[0])):
            line_transposed = ""
            for y in range(len(list_line)): line_transposed += list_line[y][x]
            list_line_transposed.append(line_transposed)
        return '\n'.join(list_line_transposed) if isinstance(blockstr, str) else list_line_transposed
    def get_block_str(action:tuple|str)->str:
        if isinstance(action, str): return f"{action}\n{space * len(action)}" if not transpose_bool else f"{transpose_blockstr(action)}\n{space}"
        if not action[1]: return f"{action[0]}\n{space * len(action[0])}" if not transpose_bool else f"{transpose_blockstr(action[0])}\n{space}"
        list_line = [action[0], *(str(action[1])[1:-1].split(", "))]
        max_line_len = max([len(line) for line in list_line])
        list_line = [line + space * (max_line_len-len(line)) for line in list_line]
        if transpose_bool:
            list_line = transpose_blockstr(list_line)
            max_line_len = len(list_line[0])
        list_line.append(space * max_line_len) # a line of space for readability
        return '\n'.join(list_line)
    node_to_blockstr = [get_block_str(node) for node in nodes]
    levelr_to_maxwidth = [1 for _ in levelr_to_order_to_node]
    y_to_maxheight = [1 for _ in range(max_y+1)]
    def calc_block_size(blockstr:str)->tuple:
        list_line = blockstr.split('\n')
        return len(list_line[0]), len(list_line)
    for levelr in range(len(levelr_to_order_to_node)):
        for order in range(len(levelr_to_order_to_node[levelr])):
            width, height = calc_block_size(node_to_blockstr[levelr_to_order_to_node[levelr][order]])
            if width > levelr_to_maxwidth[levelr]: levelr_to_maxwidth[levelr] = width
            if height > y_to_maxheight[order]: y_to_maxheight[order] = height
    # calculating the max widths of each progenitor block
    levelp_to_maxwidth = [(max([offset for offset in proge_to_offset])+1) if proge_to_offset else 0 for proge_to_offset in levelp_to_proge_to_offset]
    # Section: prettily display the graph using the previously calculated information: level_to_order_to_node, connsorig_to_y, levelp_to_proge_to_offset
    # fill with nodes, progenitor nodes, and blank blocks (everything but connections)
    ifg_grid = [["" for _ in range((len(levelr_to_order_to_node) - 1) * 4 + 1)] for _ in range(max_y+1)]
    def get_blank_blockstr(dim:tuple)->str: return '\n'.join([space * dim[0] for _ in range(dim[1])])
    def pad_with_spaces(blockstr:str, dim:tuple)->str:
        list_line = blockstr.split('\n')
        for y in range(len(list_line)): list_line[y] = list_line[y] + (space * (dim[0]-len(list_line[y])))
        for _ in range(dim[1] - len(list_line)): list_line.append(space * dim[0])
        return '\n'.join(list_line)
    for levelr in range(len(levelr_to_order_to_node)): # adding nodes
        for order in range(len(levelr_to_order_to_node[levelr])):
            ifg_grid[order][4*levelr] = pad_with_spaces(node_to_blockstr[levelr_to_order_to_node[levelr][order]], (levelr_to_maxwidth[levelr], y_to_maxheight[order]))
    for levelp in range(len(levelp_to_proge_to_offset)): # adding progenitor nodes
        for proge in range(len(levelp_to_proge_to_offset[levelp])):
            blockstr = get_blank_blockstr((levelp_to_maxwidth[levelp], y_to_maxheight[proge]))
            ifg_grid[proge][2*levelp + 1] = blockstr
    for y in range(len(ifg_grid)): # adding blank spaces in between
        for x in range(len(ifg_grid[y])):
            if ifg_grid[y][x]: continue
            height = y_to_maxheight[y]
            width = 0
            if x % 4 == 0: width = levelr_to_maxwidth[x//4]
            elif x % 2 == 1: width = levelp_to_maxwidth[(x-1)//2]
            else: width = 1 # one space between progenitor blocks
            ifg_grid[y][x] = get_blank_blockstr((width, height))
    # adding the connections, finding the connections of each progenitor
    levelp_to_pind_to_cind_to_y = [] # pind is progenitor index, cind is connection index
    for levelp in range(len(levelp_to_proge_to_offset)):
        pind_to_cind_to_y = []
        for proge in range(len(levelp_to_proge_to_offset[levelp])):
            node = levelr_to_order_to_node[(levelp+1)//2][proge]
            from_to_bool:bool = levelp % 2 == 0
            node_conns = conns[node] if from_to_bool else inv_conns[node]
            cind_to_y = sorted([connsorig_to_y[(node, node_to) if from_to_bool else (node_to, node)] for node_to in node_conns])
            pind_to_cind_to_y.append(cind_to_y)
        levelp_to_pind_to_cind_to_y.append(pind_to_cind_to_y)
    # inserts the vertical (branching) connector
    def insert_vertb_into_blockstr(blockstr:str,
        offset:int, proge_top_mid_bot_not:int, from_to_bool:bool, first_line_addconn:bool=False)->str:
        list_lines = blockstr.split('\n')
        connecting_char = None
        match proge_top_mid_bot_not:
            case 0: connecting_char = '+' if from_to_bool else '-'  # progenitor
            case 1: connecting_char = '┌' if from_to_bool else '┐'  # top
            case 2: connecting_char = '├' if from_to_bool else '┤'  # middle
            case 3: connecting_char = '└' if from_to_bool else '┘'  # bottom
            case 4: connecting_char = '│'                           # not a branching connector
        list_lines[0] = f"{list_lines[0][:offset]}{connecting_char}{list_lines[0][offset+1:]}"
        if proge_top_mid_bot_not == 0 and not first_line_addconn or proge_top_mid_bot_not == 3: return '\n'.join(list_lines)
        for line_ind in range(1, len(list_lines)):
            list_lines[line_ind] = f"{list_lines[line_ind][:offset]}│{list_lines[line_ind][offset+1:]}"
        return '\n'.join(list_lines)
    # loop through every connection of every progenitor node to insert vertical connectors
    for levelp in range(len(levelp_to_pind_to_cind_to_y)):
        pind_to_cind_to_y = levelp_to_pind_to_cind_to_y[levelp]
        from_to_bool:bool = levelp % 2 == 0
        for pind in range(len(pind_to_cind_to_y)):
            cind_to_y = pind_to_cind_to_y[pind]
            offset = levelp_to_proge_to_offset[levelp][pind]
            if not cind_to_y: continue # no connections at this progenitor node
            # adding the vertical connections
            cind = 0
            beg_y = min(pind, cind_to_y[0])
            end_y = max(pind, cind_to_y[-1])
            for y in range(beg_y, end_y+1):
                top_mid_bot_not = 4
                if cind < len(cind_to_y) and y == cind_to_y[cind]:
                    if y == pind: top_mid_bot_not = 0
                    elif y == beg_y: top_mid_bot_not = 1
                    elif cind == len(cind_to_y)-1: top_mid_bot_not = 3
                    else: top_mid_bot_not = 2
                    cind += 1
                elif y == pind: top_mid_bot_not = 0
                first_line_addconn:bool = (top_mid_bot_not == 0)\
                    and (cind < len(cind_to_y) and y <= cind_to_y[cind])\
                    and not (cind == len(cind_to_y)-1 and y == cind_to_y[cind])
                ifg_grid[y][2*levelp+1] = insert_vertb_into_blockstr(ifg_grid[y][2*levelp+1],
                    offset, top_mid_bot_not, from_to_bool, first_line_addconn)
    # inserts the horizonatal connector
    def insert_hori_into_blockstr(blockstr:str, offset:int=-1, start_end:bool=False)->str:
        list_lines = blockstr.split('\n')
        block_width = len(list_lines[0])
        start_line = list_lines[0]
        if offset > -1:
            if start_end: start_line = start_line[:offset+1] + ('─' * (block_width - offset - 1))
            else: start_line = ('─' * offset) + start_line[offset:]
        else: start_line = '─' * block_width
        list_lines[0] = start_line
        return '\n'.join(list_lines)
    # loop through the connections to add the horizontal connectors, only the "from" progenitor nodes
    progefrom_to_offset = [-2 for _ in nodes]
    progeto_to_offset = [-2 for _ in nodes]
    for levelr in range(len(levelr_to_order_to_node)):
        for order in range(len(levelr_to_order_to_node[levelr])):
            node = levelr_to_order_to_node[levelr][order]
            if levelr < len(levelr_to_order_to_node)-1:
                offset = levelp_to_proge_to_offset[2 * levelr][order]
                progefrom_to_offset[node] = offset
            if 0 < levelr:
                offset = levelp_to_proge_to_offset[2 * levelr - 1][order]
                progeto_to_offset[node] = offset
    for levelp in range(0, len(levelp_to_pind_to_cind_to_y), 2):
        pind_to_cind_to_y = levelp_to_pind_to_cind_to_y[levelp]
        for pind in range(len(pind_to_cind_to_y)):
            node_from = levelr_to_order_to_node[levelp//2][pind]
            pf_x = 2 * levelp + 1 # x coordinate of the progenitor node in the grid
            pf_offset = progefrom_to_offset[node_from]
            for node_to in conns[node_from]:
                y = connsorig_to_y[(node_from, node_to)]
                pt_levelp = 2 * (max_level - node_to_level[node_to]) - 1
                pt_x = 2 * pt_levelp + 1
                pt_offset = progeto_to_offset[node_to]
                ifg_grid[y][pf_x] = insert_hori_into_blockstr(ifg_grid[y][pf_x], pf_offset, True) # beginning block
                ifg_grid[y][pt_x] = insert_hori_into_blockstr(ifg_grid[y][pt_x], pt_offset, False) # ending block
                for x in range(pf_x + 1, pt_x): ifg_grid[y][x] = insert_hori_into_blockstr(ifg_grid[y][x])
    # Section: assembling the grid and returning the string
    def transpose_grid_str(ifg_grid_str:str|list)->str|list:
        list_line = ifg_grid_str.split('\n') if isinstance(ifg_grid_str, str) else blockstr
        list_line_transposed = []
        for x in range(len(list_line[0])):
            line_transposed = ""
            for y in range(len(list_line)):
                char_t = list_line[y][x]
                match char_t:
                    case '─': char_t = '│'
                    case '│': char_t = '─'
                    case '├': char_t = '┬'
                    case '┤': char_t = '┴'
                    case '┌': char_t = '┌'
                    case '┐': char_t = '└'
                    case '└': char_t = '┐'
                    case '┘': char_t = '┘'
                    case _: pass
                line_transposed += char_t
            list_line_transposed.append(line_transposed)
        return '\n'.join(list_line_transposed) if isinstance(ifg_grid_str, str) else list_line_transposed
    def assemble_ifg_grid(ifg_grid:list[list[str]])->str:
        grid_lines = []
        for y in range(len(ifg_grid)):
            grid_y = ["" for _ in range(len(ifg_grid[y][0].split('\n')))]
            for x in range(len(ifg_grid[y])):
                grid_yx = ifg_grid[y][x].split('\n')
                for line_ind in range(len(grid_yx)): grid_y[line_ind] += grid_yx[line_ind]
            grid_lines.extend(grid_y)
        return '\n'.join(grid_lines)
    ifg_grid_str = assemble_ifg_grid(ifg_grid)
    if transpose_bool: ifg_grid_str = transpose_grid_str(ifg_grid_str)
    return ifg_grid_str
    
# calculates the number of tasks for each action
def calc_num_tasks(domain_str:str, action:str, default_dependency_option:str, gen_fulldeptasks:bool, all_generated_dependencies:set=set())->tuple[int,set]:
    # gathering the permutations of constraints for each task dependency
    aid = domain_assistant_keys[domain_str].action_innate_dependencies
    ard = domain_assistant_keys[domain_str].action_required_dependencies
    acd = domain_assistant_keys[domain_str].action_customizable_dependencies
    cl = domain_assistant_keys[domain_str].constraint_links
    cd = domain_assistant_keys[domain_str].constraint_dependencies
    ad = gather_action_default_dependencies(ard, acd, cd, default_dependency_option)
    # gathering the permutations
    ds = domain_keys[domain_str]()
    list_action_name = [func for func in dir(ds)
        if callable(getattr(ds, func)) and not func.startswith("_") and not func.startswith("evaluation_")]
    action_parameters = {}
    for action_name in list_action_name:
        signature = inspect.signature(getattr(ds, action_name))
        action_params = {k for k, _ in signature.parameters.items()}
        if hasattr(domain_assistant_keys[domain_str], "action_params_user_not_needed")\
            and action_name in domain_assistant_keys[domain_str].action_params_user_not_needed:
            action_params -= set(domain_assistant_keys[domain_str].action_params_user_not_needed[action_name])
        action_parameters[action_name] = action_params
    # calculate the action dependencies
    action_dependencies_tasks = dependency_permutations(action, aid, ard, acd, cl, cd, ad, action_parameters)
    action_dependencies_tasks = remove_call_constr_false(action_dependencies_tasks) # removing tasks with the call_ constraints set to false
    if gen_fulldeptasks: action_dependencies_tasks = [do_d_dp_t for do_d_dp_t in action_dependencies_tasks if do_d_dp_t[1] == ad[action]] # filter for the tasks with the full dep
    # constraint redundancy reduction, keeps the last dependency
    i = 0
    while i < len(action_dependencies_tasks) and len(action_dependencies_tasks) > 1:
        _, dep, _, _ = action_dependencies_tasks[i]
        if hashable_dep(dep) in all_generated_dependencies: action_dependencies_tasks.pop(i)
        else: i += 1
    # return the number of tasks and set of generated dependencies
    num_tasks = int(sum([num_permutations(task[key]) for _, _, _, task in action_dependencies_tasks for key in task]))
    generated_dependencies = set(hashable_dep(dep) for _, dep, _, _ in action_dependencies_tasks)
    return num_tasks, generated_dependencies

# calculates the number of tasks for the entire domain
def calc_total_num_tasks(domain_str:str, actions:list, default_dependency_option:str, gen_fulldeptasks:bool=False, actions_skip:set=set())->int:
    total_num_tasks = 0
    all_gen_dep = set()
    for action in actions:
        num_tasks, gen_dep = calc_num_tasks(domain_str, action, default_dependency_option, gen_fulldeptasks, all_gen_dep)
        total_num_tasks += num_tasks
        if action not in actions_skip: all_gen_dep = all_gen_dep | gen_dep
    return int(total_num_tasks)


"""generates the tasks for each action in the domain"""

system_prompt = "Please listen to the user's instructions meticulously and carefully."
prompt_task_template = """
    Task: Generate values for initial database (unknown to the user), user known parameter values, and dependency parameters
    such that every listed dependency and constraint description would be satisfied for the action \"{user_goal}\" to succeed.
    These values should be believable and indistinguishable from a real world example.
    Generate these Python dictionaries in a json format with json values.
    The entire dependency description and constraint description list of constraints **MUST ALWAYS ALL** be fulfilled.
    If given, pay attention to the importance weight (higher is more significant) of certain constraints.
    Base your generation and consider the dependency and every constraint on the given data:
    dependency description or constraint descriptions, example database, example dependency parameters, and user parameter names.
    \n\nData:
    \nMethod: {user_goal}
    \nMethod Description: {user_goal_desc}
    \n\n**Important Dependency Description and Constraint Descriptions**:
    \n{verb_constrs}
    \n\nInstructions:
    \n1. Analyze, carefully, each constraint to make the entire dependency and each constraint true.
    \n2. Perform each of these tasks to make the initial database, user known parameter values, and dependency parameters.
    When combined, they will make the overall listed dependency true. Please do not modify the data unless absolutely necessary.
    \n\ta. Change the initial database as necessary, leaving the rest of the data untouched if they are not relevant.
    You must not, do not, and can not change the initial database python dictionary keys, only the values.
    You must return the complete updated database, except for the modified parameters.
    \nHere is descriptions of the database fields:
    \n{example_database_descriptions}
    \nHere is an example initial existing database:
    \n{example_database}
    \n\tb. Modify the dependency parameter values as needed. You must not change the dependency parameter python dictionary keys, only the values.
    The key(s) are {example_dep_param_keys}. An example dependency parameter is shown: {example_dep_param}
    \n\tc. Generate the user known parameter values, {verb_user_param_strs_with_type}.
    {verb_user_param_descs}.
    Please generate each user known parameter in the order that it is shown.
    If a user parameter is unknown to the user or the user knows the wrong or incorrect word or phrase,
    please put "UNKNOWN_PLACEHOLDER" in its place.
    Do not modify parameter values from the database unless absolutely necessary due to constraints.
"""
def generate_action_task(domain_str:str, user_goal:str, default_dependency_option:str,
    client:OpenAI, temperature:float, max_completion_tokens:int, gpt_model:str, generation_limit:int,
    all_generated_dependencies:set=set(), autogen_manfix:bool=False, gen_fulldeptasks:bool=False,
    debug_mode:bool=False, testing_mode:bool=False, testing_mode_last_task:bool=False,
    indent_amount:int=2)->tuple[list[Task],list[dict],list[dict],list[Usage]]:
    # return variable initialization
    list_task_obj = []
    list_task_info = []
    list_inter_info = []
    manfix_counter = 0 # manual fixing for later
    run_usage = []
    if debug_mode or testing_mode: print(f"user_goal {user_goal}")
    if not testing_mode: testing_mode_last_task = False
    # gathering the required information for this user_goal
    act_des = domain_assistant_keys[domain_str].action_descriptions
    act_ret = domain_assistant_keys[domain_str].action_returns
    apd = domain_assistant_keys[domain_str].action_param_descriptions
    pcd = domain_assistant_keys[domain_str].positive_constraint_descriptions
    ncd = domain_assistant_keys[domain_str].negative_constraint_descriptions
    user_goal_desc = f"{act_des[user_goal]} {act_ret[user_goal]}"
    example_domain_system_strict = domain_keys[domain_str+"_strict"]()
    example_domain_system = example_domain_system_strict.evaluation_get_domain_system()
    example_database = example_domain_system_strict.evaluation_get_database()
    example_database_descriptions = example_domain_system_strict.evaluation_get_database_descriptions()
    example_dep_params = example_domain_system_strict.evaluation_get_dependency_parameters()
    example_state_tracker = example_domain_system_strict.evaluation_get_state_tracker()
    # gathering the permutations of constraints for each task dependency
    aid = domain_assistant_keys[domain_str].action_innate_dependencies
    ard = domain_assistant_keys[domain_str].action_required_dependencies
    acd = domain_assistant_keys[domain_str].action_customizable_dependencies
    cl = domain_assistant_keys[domain_str].constraint_links
    cd = domain_assistant_keys[domain_str].constraint_dependencies
    cp = domain_assistant_keys[domain_str].constraint_processes
    ad = gather_action_default_dependencies(ard, acd, cd, default_dependency_option)
    action_default_dep_orig = gather_action_default_dependencies(ard, acd, default_dependency_option=default_dependency_option) # used for verification and inv func graph
    # gathering the permutations
    action_parameters = get_action_parameters(example_domain_system, domain_assistant_keys[domain_str])
    action_dependencies_tasks = dependency_permutations(user_goal, aid, ard, acd, cl, cd, ad, action_parameters)
    hashed_cl_funcs = {(cl[constr][0], dict_to_tuple({func_param: func_param for func_param in action_parameters[cl[constr][0]]})) for constr in cl}
    action_dependencies_tasks = remove_call_constr_false(action_dependencies_tasks) # removing tasks with the call_ constraints set to false
    if gen_fulldeptasks: action_dependencies_tasks = [do_d_dp_t for do_d_dp_t in action_dependencies_tasks if do_d_dp_t[1] == ad[user_goal]] # filter for the tasks with the full dep
    # gathers the action parameter types for LLM user known generation
    action_parameter_types = gather_action_parameter_types(domain_str)
    for key in action_parameter_types: # assumes all type "object" are just dictionaries
        if isinstance(action_parameter_types[key], str):
            if action_parameter_types[key] == "object": action_parameter_types[key] = "dictionary"
            continue
        list_parameter_type = []
        for k in range(len(action_parameter_types[key])):
            list_parameter_type.append(action_parameter_types[key][k] if action_parameter_types[key][k] != "object" else "dictionary")
        action_parameter_types[key] = list_parameter_type
    # constraint redundancy reduction, keeps the last dependency
    i = 0
    while i < len(action_dependencies_tasks) and len(action_dependencies_tasks) > 1:
        _, dep, _, _ = action_dependencies_tasks[i]
        if hashable_dep(dep) in all_generated_dependencies: action_dependencies_tasks.pop(i)
        else: i += 1
    generated_dependencies = set(hashable_dep(dep) for _, dep, _, _ in action_dependencies_tasks)
    # derived variabled that is constant for this user goal
    action_params = action_parameters[user_goal]
    if hasattr(domain_assistant_keys[domain_str], "action_params_user_not_needed")\
        and user_goal in domain_assistant_keys[domain_str].action_params_user_not_needed:
        action_params -= set(domain_assistant_keys[domain_str].action_params_user_not_needed[user_goal])
    set_state_tracker_constr_str = set(func for func in dir(example_state_tracker)
        if callable(getattr(example_state_tracker, func)) and not func.startswith("_"))
    # looping through each dependency, generating the initial variables needed for this task
    for i in range(len(action_dependencies_tasks)):
        dep_orig, dep, dep_perm, task = action_dependencies_tasks[i]
        if testing_mode_last_task and i < len(action_dependencies_tasks)-1: continue
        if testing_mode:
            print(dfsgather_dep_tree_vis(dep_orig))
            print(dfsgather_dep_tree_vis(dep))
            print(dfsgather_dep_tree_vis(dep_perm))
            # print(dfsgather_dep_tree_vis(dep, user_goal, cl, action_default_dep, cd))
            print(get_dep_task_str(task)) 
        # configuring the task into one long array, with a field to indicate success
        configured_tasks = {key:[] for key in task[True]}
        task_successes = []
        for key in task[True]: configured_tasks[key].extend(task[True][key])
        task_successes.extend([1 for _ in range(num_permutations(configured_tasks)-len(task_successes))])
        for key in task[False]: configured_tasks[key].extend(task[False][key])
        task_successes.extend([0 for _ in range(num_permutations(configured_tasks)-len(task_successes))])
        # initialization of post processing variables
        inv_func_call_graph, verb_user_goal = None, None
        # loop through all tasks
        for j in range(len(task_successes)):
            if testing_mode_last_task and j < len(task_successes)-1: continue
            task_single = {key: configured_tasks[key][j] for key in configured_tasks}
            task_succ = task_successes[j]
            if testing_mode: print(get_dict_str(task_single))
            # LLM generation information dynamic to the task_single
            user_params = dfsgather_params_task(task_single) # params in this dependency
            user_params = user_params | action_params
            user_param_descs = {} # user_known
            for param in user_params:
                param_desc = apd[param] if isinstance(apd[param], str) else f"[{'] or ['.join(apd[param])}]"
                user_param_descs[param] = param_desc
            verb_user_param_descs = f"Here are the user known parameters and their descriptions: {str(user_param_descs)}"\
                if user_param_descs else "There are no parameter descriptions"
            user_param_strs_with_type = [f"{param} ({verbalized_list_values(action_parameter_types[param])})" for param in user_params] # parameters and their types
            verb_user_param_strs_with_type = f"which should only contain parameter(s) {verbalized_list_values(user_param_strs_with_type)}"\
                if user_param_strs_with_type else "there are no user-known parameters, please just generate an empty dictionary: {}"
            # start to generate here to edit the constraints, update the database, and update the dep_param
            task_obj_best = None
            veri_res_best = None
            veri_res_coll = {key: 0 for key in task_single} # the constraints that have failed over a series of generation attempts
            task_obj_best_nfails = -1 # counts the number of constraint mismatches the task_obj_best has
            generate_task_again = True
            gen_task_fail_counter = 0
            while generate_task_again and gen_task_fail_counter < generation_limit:
                # change the prompt every loop with improved items
                task_constrs, database_prompt_template, dep_params_prompt_template = task_single, example_database, example_dep_params
                if task_obj_best:
                    task_constrs = {key: task_single[key] for key in veri_res_coll if veri_res_coll[key] > 0}
                    database_prompt_template = json.loads(task_obj_best.initial_database_str)
                    dep_params_prompt_template = json.loads(task_obj_best.dependency_parameters_str)
                verb_constrs = gather_verb_constrs(task_constrs, pcd, ncd, example_dep_params, set_state_tracker_constr_str, veri_res_coll)
                dep_param_keys_prompt_template = [f"{dep_param} ({type(dep_params_prompt_template[dep_param]).__name__})" for dep_param in dep_params_prompt_template]
                # prompt setup
                prompt_task_vars = {
                    "verb_constrs":                 verb_constrs,
                    "verb_user_param_descs":        verb_user_param_descs,
                    "verb_user_param_strs_with_type":verb_user_param_strs_with_type,
                    "user_goal":                    user_goal,
                    "user_goal_desc":               user_goal_desc,
                    "example_database":             json.dumps(database_prompt_template, indent=indent_amount),
                    "example_dep_param":            dep_params_prompt_template,
                    "example_dep_param_keys":       verbalized_list_values(dep_param_keys_prompt_template),
                    "example_database_descriptions":json.dumps(example_database_descriptions, indent=indent_amount),
                }
                global system_prompt
                prompt_task = modify_prompt(prompt_task_template).format(**prompt_task_vars)
                if testing_mode: print(prompt_task)
                messages = [{"role": "system", "content": dedent(system_prompt)}, {"role": "user", "content": prompt_task}]
                # LLM generation, regenerate until success
                try:
                    completion_task = client.beta.chat.completions.parse(messages=messages, model=gpt_model, response_format=Task,
                        temperature=temperature, max_completion_tokens=max_completion_tokens)
                except json.decoder.JSONDecodeError as e:
                    gen_task_fail_counter += 1
                    print(e)
                    continue
                except Exception as e:
                    gen_task_fail_counter += 1
                    print("generation error:", e)
                    continue
                task_obj = completion_task.choices[0].message.parsed
                run_usage.append(completion_task.usage)
                # replace placeholder values
                user_known = json.loads(task_obj.user_known_str)
                task_obj.user_known_str = json.dumps(dfsreplace_placeholder(user_known))
                initial_database = json.loads(task_obj.initial_database_str)
                task_obj.initial_database_str = json.dumps(dfsreplace_placeholder(initial_database))
                if testing_mode: print(task_obj_str(task_obj))
                # verification of database format and user known keys
                database_format_match_bool, initial_database = verify_database_format(json.loads(task_obj.initial_database_str), example_database)
                if not database_format_match_bool:
                    gen_task_fail_counter += 1
                    if testing_mode: print("generated task did not fit the format")
                    continue
                else: task_obj.initial_database_str = json.dumps(initial_database)
                dep_params = json.loads(task_obj.dependency_parameters_str)
                matching_keys_dep_params = set(dep_params_prompt_template.keys()) == set(dep_params.keys())
                matching_keys_user_known = user_params == set(user_known.keys())
                if not matching_keys_dep_params or not matching_keys_user_known:
                    gen_task_fail_counter += 1
                    if testing_mode: print("generated dependency parameters or user known did not match the expected keys")
                    continue
                openai_type_conversion = {"number":(float, int), "string":str, "object":dict, "dictionary":dict, "array":list, "boolean":bool, "integer":int}
                num_type_matches = 0
                for key in user_known:
                    apts_key = action_parameter_types[key]
                    types_to_match = openai_type_conversion[apts_key] if isinstance(apts_key, str) else\
                        tuple(openai_type_conversion[apt_key] for apt_key in apts_key)
                    num_type_matches += int(isinstance(user_known[key], types_to_match)) 
                if num_type_matches < len(user_known):
                    gen_task_fail_counter += 1
                    if testing_mode: print("generated user known did not have the correct types")
                    continue
                # verification of if the generated data followed the constraints as we expect
                actions_required = dfsgather_actions_required(dep_perm, hashed_cl_funcs) # derive the actions required through the constraint links
                actions_required = [(func_str, tuple_to_dict(hashed_func_params)) for func_str, hashed_func_params in actions_required]
                actions_required.append((user_goal, {func_param: func_param for func_param in action_parameters[user_goal]}))
                all_def_dep_perm = copy.deepcopy(action_default_dep_orig) # preparing the default permutation dependencies
                all_def_dep_perm = {key: dfsins_cl_cd_aid(all_def_dep_perm[key], cl, aid, ad, cd, action_parameters) for key in all_def_dep_perm}
                constraints_followed, verification_result = verify_gen_succ(task_obj, dep, dep_perm, domain_str, user_goal,
                    aid, ad, all_def_dep_perm, actions_required, task_single, bool(task_succ), cl, cd, action_parameters)
                # iterative improvement
                veri_res_set = set(key for key in verification_result if verification_result[key][0] > -1 and verification_result[key][0] != verification_result[key][1])
                for key in veri_res_set: veri_res_coll[key] += 1
                min_importance_value = min([veri_res_coll[key] for key in veri_res_coll if veri_res_coll[key] > 0]) if veri_res_set else 0
                if min_importance_value > 1:
                    for key in veri_res_coll: veri_res_coll[key] -= (min_importance_value - 1) if veri_res_coll[key] > 0 else 0
                if task_obj_best_nfails < 0 or len(veri_res_set) <= task_obj_best_nfails:
                    task_obj_best = task_obj
                    veri_res_best = verification_result
                task_obj_best_nfails = len(veri_res_set) if task_obj_best_nfails < 0 else min(task_obj_best_nfails, len(veri_res_set))
                if not constraints_followed:
                    gen_task_fail_counter += 1
                    if testing_mode:
                        print("generated task did not follow the constraints as listed")
                        print("constraint (target result, actual result), including constraint dependencies")
                        print(get_dict_str(verification_result))
                    continue
                generate_task_again = False
            if not generate_task_again:
                if testing_mode: print("task generation success")
            else:
                if not autogen_manfix:
                    raise ValueError(f"generated the {user_goal} task {gen_task_fail_counter} times unsuccessfully")
            # post generation processing, finding the inverse function call directed graph, generates once for the dependency
            if not inv_func_call_graph:
                user_goal_node = (user_goal, {key: key for key in action_parameters[user_goal]})
                inv_func_call_graph = dfsgather_invfunccalldirgraph(dep_orig, cl, cp, action_default_dep_orig, action_parameters, user_goal_node)
            if testing_mode: print(gather_ifg_graph_vis(inv_func_call_graph, True)) # get_inv_func_graph_str displays the raw information
            # user goal verbalization, generated once for each dep because it's not dependent on the actual values of the user known
            if not verb_user_goal:
                verb_user_goal, verb_user_goal_usage = generate_verb_user_goal(
                    user_goal_desc, verb_user_param_descs,
                    client, gpt_model, temperature, max_completion_tokens)
                run_usage.append(verb_user_goal_usage)
            if testing_mode: print(verb_user_goal)
            # user prompt generation for a single round, unique to each task
            verb_user_goal_oneround, verb_user_goal_oneround_usage = generate_verb_user_goal_oneround(
                verb_user_goal, user_known, domain_str,
                client, gpt_model, temperature, max_completion_tokens)
            run_usage.append(verb_user_goal_oneround_usage)
            if testing_mode: print(verb_user_goal_oneround)
            # converting the single task into a 2D list sorted by outcome
            inv_task_single = [[], [], []] # 2 is the new -1
            for hashed_constr in task_single:
                constr_result = task_single[hashed_constr]
                inv_task_single[constr_result if constr_result >= 0 else 2].append(orig_dep(hashed_constr))
            # parsing and recording all the variables, also for manual fixing
            list_task_obj.append(task_obj_best)
            task_info = {
                "constraints":               dep,
                "constraints_original":      dep_orig,
                "action_should_succeed":    task_succ,
                "directed_action_graph":      inv_func_call_graph,
                "user_instruction":           verb_user_goal,
                "user_prompt":  verb_user_goal_oneround,
            }
            list_task_info.append(task_info)
            inter_info = {
                "dependency_permutation":   dep_perm,
                "inv_task_single":          inv_task_single,
                "user_params":              list(user_params),
                "actions_required":         actions_required,
            }
            list_inter_info.append(inter_info)
            # manual fixing
            if generate_task_again:
                if veri_res_best:
                    manfix_constrs = [(f"exp {veri_res_best[hc][0]} act {veri_res_best[hc][1]}", orig_dep(hc)) for hc in veri_res_best]
                else: manfix_constrs = ["json error, database format mismatch, or user_known mismatch"]
                manfix = {"manfix_id": f"{user_goal}_{manfix_counter}", "manfix_constrs": manfix_constrs}
                task_info.update(manfix)
                manfix_counter += 1
    if debug_mode or testing_mode:
        total_num_tasks = sum([num_permutations(task[key]) for _, _, _, task in action_dependencies_tasks for key in task])
        print(user_goal, len(list_task_obj)-manfix_counter, "tasks successfully generated out of", total_num_tasks)
    # return the intermediate tasks, tasks, and run_usage
    return list_task_obj, list_task_info, list_inter_info, generated_dependencies, manfix_counter, run_usage


"""main function to generate the task data, consisting of database system actions, using the least amount of AI as possible"""

def task_generation(args):
    write_output_bool = args.write_output_disable
    print_pipeline = args.print_pipeline_disable
    # initializing variables and model
    client = OpenAI(api_key=[REDACTED]
    all_run_usage = []
    # running tests
    failures = check_data_sanity(args.domains_dir, args.domain_str) # not functional right now
    if False and print_pipeline:
        if len(failures)==0: print("data check success")
        else:
            print("data check failure")
            for failure in failures: print(failure)
    
    # tests, test_results, test_run_usage = run_domain_tests(args.domain_str, args.print_test_domain, args.test_domain, args.data_dir, args.assistant_file,
    #     args.openai_api_key, args.gpt_model, args.dependency_location, args.default_dependency_option, print_pipeline, args.shuffle_assfun_disable)
    # if print_pipeline: print(f"{sum([int(ele) for ele in test_results])} number of successes out of {len(tests)} tests")
    # all_run_usage.extend(test_run_usage)
    
    # reading in the database file with rule-based dependencies, gathering all and evaluated method names
    domain_system = domain_keys[args.domain_str]()
    domain_system_strict = domain_keys[args.domain_str+"_strict"]()
    ds_method_name_list = [func for func in dir(domain_system)
        if callable(getattr(domain_system, func)) and not func.startswith("_")]
    dss_method_name_list = [func for func in dir(domain_system_strict)
        if callable(getattr(domain_system_strict, func)) and not func.startswith("_")]
    both_ds_method_name_set = set(ds_method_name_list) | set(dss_method_name_list)
    eval_ds_method_name_set = both_ds_method_name_set.copy()
    for method_name in both_ds_method_name_set:
        if method_name.startswith("internal_") or method_name.startswith("evaluation_"):
            eval_ds_method_name_set.remove(method_name)
    if args.testing_mode: eval_ds_method_name_set = set([args.testing_mode_user_goal])\
        if args.testing_mode_user_goal in eval_ds_method_name_set else set([random.choice(list(eval_ds_method_name_set))])
    eval_ds_method_name_list = sorted(list(eval_ds_method_name_set)) # sort it to keep number of tasks constant from the dep remembering
    # parsing output variables
    data_dir = args.data_dir # f"{args.domains_dir}/{args.domain_str}" writing data directly into the domain
    tasks_filename = f"{args.domain_str}_tasks.json"
    intermediate_tasks_filename = f"{args.domain_str}_intermediate_tasks.json"
    # for each method, construct the outcomes, decision tree, then the task with user known parameters, initial database, and user goal
    tasks, intermediate_tasks = {}, {}
    temperature = args.temperature
    max_completion_tokens = args.max_tokens
    all_generated_dependencies = set()
    skipped_methods = set()
    manfix_counters = {}
    pbar = tqdm(total=calc_total_num_tasks(args.domain_str, eval_ds_method_name_list, args.default_dependency_option, args.gen_fulldeptasks), disable=not print_pipeline)
    for user_goal in eval_ds_method_name_list:
        # generate the task: 1. gather information, 2. use LLM to generate the data, 3. verify the correctness
        list_task_obj, list_task_info, list_inter_info, manfix_counter, run_usage = None, None, None, -1, None
        gen_task_fail_counter = 0 # counter to count the number of generation failures for the task
        while not run_usage and gen_task_fail_counter < args.generation_limit:
            try:
                list_task_obj, list_task_info, list_inter_info, generated_dependences, manfix_counter, run_usage =\
                    generate_action_task(args.domain_str, user_goal, args.default_dependency_option,
                    client, temperature, max_completion_tokens, args.gpt_model, args.generation_limit,
                    all_generated_dependencies, args.autogen_manfix, args.gen_fulldeptasks,
                    args.debug_mode, args.testing_mode, args.testing_mode_last_task,
                    args.indent_amount)
            except ValueError as e:
                if print_pipeline: print("Error:", e)
            except LengthFinishReasonError:
                if print_pipeline: print("Error: generation response exceeded max number of tokens")
            gen_task_fail_counter += 1
            if args.testing_mode: break
        if not run_usage:
            skipped_methods.add(user_goal)
            num_skipped_tasks = calc_num_tasks(args.domain_str, user_goal, args.default_dependency_option, all_generated_dependencies)[0]
            pbar.total = calc_total_num_tasks(args.domain_str, eval_ds_method_name_list, args.default_dependency_option, skipped_methods)
            pbar.update(num_skipped_tasks)
            continue
        else: all_generated_dependencies = all_generated_dependencies | generated_dependences
        all_run_usage.extend(run_usage)
        # gather the data
        tasks[user_goal] = []
        intermediate_tasks[user_goal] = []
        for i in range(len(list_task_obj)):
            task_obj = list_task_obj[i]
            task = {}
            try: task["initial_database"] = json.loads(task_obj.initial_database_str)
            except json.decoder.JSONDecodeError as e: task["initial_database"] = task_obj.initial_database_str
            try: task["constraint_parameters"] = json.loads(task_obj.dependency_parameters_str)
            except json.decoder.JSONDecodeError as e: task["constraint_parameters"] = task_obj.dependency_parameters_str
            try: task["user_known"] = json.loads(task_obj.user_known_str)
            except json.decoder.JSONDecodeError as e: task["user_known"] = task_obj.user_known_str
            task.update(list_task_info[i])
            tasks[user_goal].append(task)
            intermediate_tasks[user_goal].append(list_inter_info[i])
        if manfix_counter > 0: manfix_counters[user_goal] = manfix_counter
        # writing the partial tasks data just in case of failure
        if write_output_bool:
            write_tasks(tasks, data_dir, tasks_filename, args.indent_amount)
            write_tasks(intermediate_tasks, data_dir, intermediate_tasks_filename, args.indent_amount)
        # update the progress bar
        pbar.update(int(len(list_task_obj)))
    pbar.close()
    # print diagnostic information
    if print_pipeline:
        skipped_methods_report_str = f"methods skipped due to error: {skipped_methods}" if skipped_methods else "no methods skipped"
        print(skipped_methods_report_str)
        num_tasks = 0
        for user_goal in tasks: num_tasks += len(tasks[user_goal])
        print(f"total number of tasks for the {args.domain_str} domain:", num_tasks)
    if print_pipeline and args.autogen_manfix:
        if manfix_counters:
            print("list of actions and their manfix counters:")
            print(get_dict_str(manfix_counters))
            print("ctrl+f \"manfix_id\" to find them in the data")
        else: print("no methods to fix")
    # return the openai usage
    return all_run_usage