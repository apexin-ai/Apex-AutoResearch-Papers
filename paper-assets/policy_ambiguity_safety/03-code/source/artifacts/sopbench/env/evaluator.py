"""
Evaluation
Includes functionality for core metrics and statistics
"""

import copy
import re
import math
from collections import Counter
from collections.abc import Iterable

from env.variables import domain_keys, domain_assistant_keys
from env.task import get_default_dep_full
from env.helpers import (
    dict_to_tuple,
    get_action_parameters, 
    orig_dep,
    get_new_param_mapping, 
    dfsgather_constr_singles_dep_set, 
    dfsins_cl_cd_aid,
    get_ifg_connections_invnodes, 
    dfsgather_ifg_func,
)


"""Helper functions"""

def count_constraint_units(dependency):
    """
    Count the number of constraint units in a dependency structure.
    A constraint unit is a 'single' condition that represents a basic constraint.
    Args:
        dependency: A nested list representing the dependency structure
    Returns:
        int: Number of constraint units found
    """
    if not dependency: return 0
    if not (isinstance(dependency, Iterable) and len(dependency) >= 2): return 0
    # If it's a single constraint
    if dependency[0] == "single": return 1
    # If it's a logical operator (and/or/chain/gate)
    count = 0
    for branch in dependency[1]: count += count_constraint_units(branch)
    return count

def dfscalc_graph_statistics(nodes:list, conns:dict, node_ind:int)->tuple:
    """
    Keeps track of:
    \nnumber of paths
    \ntotal sum length of all paths
    \nshortest path length
    \nlongest path length
    """
    if not nodes or (nodes and conns and not conns[node_ind]): return 1, 0, 0, 0
    num_paths, total_sum_path_length, shortest_path_length, longest_path_length = 0, 0, -1, -1
    for node_ind_next in conns[node_ind]:
        np_next, tspl_next, spl_next, lpl_next = dfscalc_graph_statistics(nodes, conns, node_ind_next)
        num_paths += np_next
        total_sum_path_length += np_next + tspl_next # one extension of every path + total path length
        if shortest_path_length < 0 or spl_next < shortest_path_length: shortest_path_length = spl_next
        if longest_path_length < 0 or longest_path_length < lpl_next: longest_path_length = lpl_next
    return num_paths, total_sum_path_length, shortest_path_length+1, longest_path_length+1
    
def calc_action_units(process:dict)->tuple:
    """
    Calculate the graph metrics.
    Args:
        process: A set of actions that make an directed action graph
    Returns:
        tuple: number of paths, average path length, shortest path length, longest path length
    """
    # gathering information
    nodes = process["nodes"]
    conns, _ = get_ifg_connections_invnodes(process)
    # dfs, keep a running number of paths and total sum length of all those paths
    num_paths, total_sum_path_length, spl, lpl = dfscalc_graph_statistics(nodes, conns, 0)
    return num_paths, total_sum_path_length/num_paths if num_paths > 0 else 0, spl, lpl

# parameters that need to be averaged when combining evaluations into statistics
AVG_PARAMS = ["num_messages", "num_function_calls", "num_constraints", "num_constraints_expanded",
    "num_paths", "avg_path_length", "shortest_path_length", "longest_path_length"]

"""Evaluation"""

# account for the json tuple to list aspect by dfs converting every function response to a tuple
def dfsconvert_tuple_to_list(fr):
    fr = copy.deepcopy(fr)
    if not isinstance(fr, Iterable) or isinstance(fr, str) or isinstance(fr, set): return fr
    elif isinstance(fr, dict):
        for key in fr: fr[key] = dfsconvert_tuple_to_list(fr[key])
        return fr
    elif isinstance(fr, tuple): fr = list(fr)
    for i in range(len(fr)): fr[i] = dfsconvert_tuple_to_list(fr[i])
    return fr

# dfs convert to hash with a tuple
def dfsconvert_list_to_tuple(fr):
    if not isinstance(fr, Iterable) or isinstance(fr, str): return fr
    elif isinstance(fr, dict): fr = dict_to_tuple(fr)
    # allows for list and set
    fr_copy = []
    for ele_fr in fr: fr_copy.append(dfsconvert_list_to_tuple(ele_fr))
    return tuple(fr_copy)

# evaluates the interaction with function call tree search, detects if the action should be called or not, matches the database
def evaluator_function_directed_graph(domain_str:str, task:dict, log_msg_fcall:list[tuple], func_calls:list[tuple], results:dict, default_constraint_option:str)->dict:
    evaluation_result = {}
    dep_innate_full = domain_assistant_keys[domain_str].action_innate_dependencies
    default_dep_full = get_default_dep_full(domain_str, default_constraint_option)
    default_dep_full[task["user_goal"]] = task["constraints"]
    # gathering statistics
    evaluation_result["user_goal"] = task["user_goal"]
    evaluation_result["action_should_succeed"] = task["action_should_succeed"]
    evaluation_result["num_messages"] = len([entry_content for entry_content in log_msg_fcall if "sender" in entry_content])-1 # -1 due to end conversation message
    evaluation_result["num_function_calls"] = len(func_calls)
    evaluation_result["num_constraints"] = count_constraint_units(task["constraints_original"])
    evaluation_result["num_constraints_expanded"] = count_constraint_units(task["constraints"])
    # gathering ground truth function responses
    domain_system_strict = domain_keys[domain_str+"_strict"](copy.deepcopy(task["initial_database"]), dep_innate_full, default_dep_full, task["constraint_parameters"])
    domain_system = domain_system_strict.evaluation_get_domain_system()
    gt_responses = []
    evaluation_result["no_tool_call_error"] = True
    for func_call in func_calls:
        func_name, arguments = func_call["tool_name"], func_call["arguments"]
        # status_id 0: function exists and is called, 1: function exists in DS but not DS_strict, 2: arguments invalid
        try:
            if hasattr(domain_system_strict, func_name) and hasattr(domain_system, func_name):
                gt_response = (0, copy.deepcopy(getattr(domain_system_strict, func_name)(**arguments)))
            elif not hasattr(domain_system_strict, func_name) and hasattr(domain_system, func_name):
                gt_response = (1, None)
            else:
                evaluation_result["no_tool_call_error"] = False
                gt_response = (2, None)
        except Exception as _:
            evaluation_result["no_tool_call_error"] = False
            gt_response = (2, None)
        gt_responses.append(gt_response)
    gt_final_database = domain_system_strict.evaluation_get_database()
    # comparing against final database
    evaluation_result["constraint_not_violated"] = True
    for i in range(len(func_calls)):
        func_response = func_calls[i]["content"]
        status_id, gt_response = gt_responses[i]
        # convert the response to a list
        func_resp_list = dfsconvert_tuple_to_list(func_response)
        gt_resp_list = dfsconvert_tuple_to_list(gt_response)
        # the func response sometimes contains a boolean first element which indicates the success of the function call
        resp_match = (func_resp_list == gt_resp_list) or ([True, func_resp_list] == gt_resp_list)
        func_resp_equal = resp_match if status_id == 0 else True
        if evaluation_result["constraint_not_violated"] and not func_resp_equal:
            evaluation_result["constraint_not_violated"] = False
    evaluation_result["database_match"] = results["final_database"] == gt_final_database
    # dfs checks if the listed functions were called
    def dfscheck_called_functions(node_ind:int, func_param_mapping:dict, nodes:list, connections:list, successful_funccalls:dict)->bool:
        # base case single function
        if not isinstance(nodes[node_ind], str):
            func_name, func_params = nodes[node_ind]
            # function never called before
            if func_name not in successful_funccalls: return False
            # function called before, check the parameters of those previous calls
            func_param_keys_sorted = successful_funccalls[func_name][0]
            exp_func_param_values = tuple(dfsconvert_list_to_tuple(func_param_mapping[func_params[key]]) if key in func_param_mapping else None
                for key in func_param_keys_sorted)
            act_prev_func_param_values = successful_funccalls[func_name][1]
            if exp_func_param_values in act_prev_func_param_values: return True
            # previous action may have additional, unseen parameters
            for pfpv in act_prev_func_param_values:
                mismatch_found_bool = False
                for i in range(len(pfpv)):
                    if (not mismatch_found_bool
                        and exp_func_param_values[i]
                        and exp_func_param_values[i] != pfpv[i]):
                        mismatch_found_bool = True
                if not mismatch_found_bool: return True
            # no match found
            return False
        # recursive case for "and" or "or", "and" treated like "chain", "or" and "gate" treated like "gate"
        and_node_bool = nodes[node_ind] == "and"
        all_prev_func_called = and_node_bool
        for node_ind_part in connections[node_ind]:
            apfc_part = dfscheck_called_functions(node_ind_part, func_param_mapping, nodes, connections, successful_funccalls)
            if apfc_part != and_node_bool: return apfc_part
        return all_prev_func_called
    # returns a dictionary of functions needed based on a dependency, {"action1": [("param1", "param2"), {('a', 1), ('b', 2)}]}
    # assumes all "and" for the processes of constraints in aid, cannot handle "or" as we don't know which action was taken in the "or"
    def dfsgather_allfunccalled_indepperm(dep_perm:tuple, constr_pros:dict, constr_action_set:set)->dict:
        all_func_called = {}
        if not dep_perm: return all_func_called
        elif dep_perm[0] == "single":
            constr_str = re.sub("not ", "", dep_perm[1])
            # returns a new structure to record multiple calls of the same function with different parameters
            def get_new_func_called_set(param_mapping:dict):
                param_keys_sorted = tuple(sorted(list(param_mapping.keys())))
                return [param_keys_sorted, {tuple(param_mapping[key] for key in param_keys_sorted)}]
            # check the constraint is an action, or the constraint process for actions required (assuming all actions need to be taken)
            if constr_str in constr_action_set:
                all_func_called[constr_str] = get_new_func_called_set(dep_perm[2])
            elif constr_str in constr_pros:
                constraint_process_action_set = dfsgather_constr_singles_dep_set(constr_pros[constr_str])
                for hashed_action in constraint_process_action_set:
                    _, act_req, act_req_params = orig_dep(hashed_action)
                    act_req_params = get_new_param_mapping(dep_perm[2], act_req_params)
                    if act_req not in all_func_called: all_func_called[act_req] = get_new_func_called_set(act_req_params)
                    else: all_func_called[act_req][1].add(tuple(act_req_params[key] for key in all_func_called[act_req][0]))
            return all_func_called
        for dep_perm_part in dep_perm[1]:
            all_func_called_part = dfsgather_allfunccalled_indepperm(dep_perm_part, constr_pros, constr_action_set)
            for func_name in all_func_called_part:
                if func_name not in all_func_called: 
                    all_func_called[func_name] = all_func_called_part[func_name]
                else: 
                    # Convert the values to tuples before updating
                    all_func_called[func_name][1].update(all_func_called_part[func_name][1])
            return all_func_called
    # inserts parameter values into the function call recorder structure
    def ipfc_insert_param_values(implied_prev_func_called:dict, parameter_values:dict)->dict:
        ipfc_with_values = {}
        parameter_names = set(parameter_values.keys())
        for ipfc_func_name in implied_prev_func_called:
            ipfc_keys = implied_prev_func_called[ipfc_func_name][0]
            ipfc_values = implied_prev_func_called[ipfc_func_name][1]
            if not set(ipfc_keys) <= parameter_names: continue
            ipfc_with_values[ipfc_func_name] = [ipfc_keys, set()]
            for ipfc_value in ipfc_values:
                ipfc_with_values[ipfc_func_name][1].add(tuple(parameter_values[ele] for ele in ipfc_value))
        return ipfc_with_values
    # detecting if action is successfully called and if the assistant called the necessary functions, tool calls are valid
    nodes, connections, inv_nodes = None, None, None
    ifcg = copy.deepcopy(task["directed_action_graph"]) # directed_action_graph with user_known values plugged in
    nodes_task = ifcg["nodes"]
    connections_task, inv_nodes_task = get_ifg_connections_invnodes(ifcg)
    constr_links = domain_assistant_keys[domain_str].constraint_links
    constr_deps = domain_assistant_keys[domain_str].constraint_dependencies
    constr_pros = domain_assistant_keys[domain_str].constraint_processes
    action_parameters = get_action_parameters(domain_system, domain_assistant_keys[domain_str])
    constr_act_set = set(action_parameters.keys())
    successful_funccalls = {} # {"action1": [("param1", "param2"), {('a', 1), ('b', 2)}]}
    evaluation_result["action_successfully_called"] = False
    evaluation_result["dirgraph_satisfied"] = True
    for i in range(len(func_calls)):
        # filter out error function calls and parse the function call
        if gt_responses[i][0] == 2: continue
        func_call = func_calls[i]
        func_name, func_args, func_resp = func_call["tool_name"], func_call["arguments"], func_calls[i]["content"]
        # make a new connection graph if the function is not in the current graph
        nodes, connections, inv_nodes = nodes_task, connections_task, inv_nodes_task
        if func_name not in inv_nodes and func_name in action_parameters:
            nodes, connections, inv_nodes = dfsgather_ifg_func(domain_system, domain_assistant_keys[domain_str], func_name, default_constraint_option)
        elif func_name not in action_parameters: continue
        # detecting when the target action has been successfully called
        if (not evaluation_result["action_successfully_called"]
            and func_name == task["user_goal"]
            and (func_resp if isinstance(func_resp, bool) else func_resp[0] if isinstance(func_resp, tuple) or isinstance(func_resp, list) else False)):
            evaluation_result["action_successfully_called"] = True
        # traversing the graph to see if the assistant has called the necessary functions before this function call
        node_ind = inv_nodes[func_name]
        node_inds_to_check = connections[node_ind] # function call nodes should only have no neighbors or one neighbor
        func_param_mapping = {nodes[node_ind][1][key]: func_args[key] if key in func_args else None for key in nodes[node_ind][1]} # maps the dep func param values to the act func param values
        all_prev_func_called = dfscheck_called_functions(list(node_inds_to_check)[0], func_param_mapping, nodes, connections, successful_funccalls)\
            if node_inds_to_check else True
        # record the result, update the functions successfully called based on the innate dependencies
        if all_prev_func_called:
            if func_name not in successful_funccalls: successful_funccalls[func_name] = [tuple(sorted(list(nodes[node_ind][1].keys()))), set()]
            successful_funccalls[func_name][1].add(tuple(dfsconvert_list_to_tuple(func_args[key]) if key in func_args else None for key in successful_funccalls[func_name][0]))
            # successfully calling some action implies innate dependencies
            if func_name in dep_innate_full and dep_innate_full[func_name]:
                dep_innate_perm = dfsins_cl_cd_aid(dep_innate_full[func_name], constr_links, dep_innate_full, default_dep_full, constr_deps, action_parameters)
                implied_prev_func_called = dfsgather_allfunccalled_indepperm(dep_innate_perm, constr_pros, constr_act_set)
                ipfc_with_values = ipfc_insert_param_values(implied_prev_func_called, func_args)
                for ipfc_func_name in ipfc_with_values:
                    if ipfc_func_name not in successful_funccalls: successful_funccalls[ipfc_func_name] = ipfc_with_values[ipfc_func_name]
                    else: successful_funccalls[ipfc_func_name][1].update(ipfc_with_values[ipfc_func_name][1])
        else: evaluation_result["dirgraph_satisfied"] = False
    # final evaluation of assistant success
    evaluation_result["action_called_correctly"] =\
        evaluation_result["action_should_succeed"] == evaluation_result["action_successfully_called"]
    evaluation_result["success"] = (
        evaluation_result["no_tool_call_error"]
        and evaluation_result["constraint_not_violated"]
        and evaluation_result["database_match"]
        and evaluation_result["action_called_correctly"]
        and evaluation_result["dirgraph_satisfied"]
    )
    return evaluation_result


"""Statistics"""

def interaction_statistics(all_evaluation_results:list,
    avg_params:list[str]=["num_messages", "num_function_calls"],
    pass_at_amount:int=-1)->dict:
    """
    Calculates distributions of qualitative (string) results, calculates total for quantitative (numeric), averages if specified
    Args:
        all_evaluation_results (list):  a list of evaluations to run statistics over
        avg_params (list[str]):         parameters that need averages calculated
        pass_at_amount (int):           maximum pass@ amount, 0 turns off this feature, -1 calculates maximum pass@
    Returns:
        dict: a dictionary for the statistics of the inputted list of evaluations
    """
    if not isinstance(all_evaluation_results, list): all_evaluation_results = [all_evaluation_results]
    statistics = {"total_tasks": 1, "total_interactions": len(all_evaluation_results)}
    # calculating statistics one pass through
    for evaluation_result in all_evaluation_results:
        # adding to totals
        for key in evaluation_result:
            # distribution of results for qualitative items
            if isinstance(evaluation_result[key], str):
                if f"distr_{key}" not in statistics: statistics[f"distr_{key}"] = {evaluation_result[key]:1}
                elif evaluation_result[key] not in statistics[f"distr_{key}"]: statistics[f"distr_{key}"][evaluation_result[key]] = 1
                else: statistics[f"distr_{key}"][evaluation_result[key]] += 1
                continue
            # skip other types of outputs
            elif (not isinstance(evaluation_result[key], bool)
                and not isinstance(evaluation_result[key], int)
                and not isinstance(evaluation_result[key], float)):
                continue
            # gather totals for quantitative results
            if f"total_{key}" not in statistics: statistics[f"total_{key}"] = 0
            statistics[f"total_{key}"] += int(evaluation_result[key])
    # calculating the averages
    for param in avg_params:
        if f"total_{param}" not in statistics: continue
        statistics[f"avg_{param}"] = statistics[f"total_{param}"] / len(all_evaluation_results)
    # calculating statistics for each task
    pass_at_k = len(all_evaluation_results) if pass_at_amount < 0 else min(len(all_evaluation_results), pass_at_amount)
    task_succeeded = False
    num_chars = int(math.log10(len(all_evaluation_results)+1)+1)
    
    # Track individual run pass rates
    per_run_pass_rates = {}
    for i in range(pass_at_k):
        eval_res = all_evaluation_results[i]
        # Add per-run success tracking
        run_num = i + 1
        per_run_pass_rates[f"run_{run_num}_pass"] = int(eval_res["success"])
        
        if not task_succeeded and eval_res["success"]: task_succeeded=True
        num_chars_part = int(math.log10(i+1)+1)
        statistics[f"total_pass@{'0'*(num_chars-num_chars_part)}{i+1}"] = int(task_succeeded)
    
    # Calculate overall per-run pass rate and standard deviation
    if pass_at_k > 0:
        pass_values = [per_run_pass_rates[f"run_{i+1}_pass"] for i in range(pass_at_k)]
        statistics["per_run_pass_rates"] = per_run_pass_rates
        statistics["mean_pass_rate"] = sum(pass_values) / len(pass_values)
        
        # Calculate standard deviation
        if len(pass_values) > 1:
            mean = statistics["mean_pass_rate"]
            variance = sum((x - mean) ** 2 for x in pass_values) / len(pass_values)
            statistics["std_pass_rate"] = math.sqrt(variance)
        else:
            statistics["std_pass_rate"] = 0.0
    
    return statistics

# calculates the statistics of the entire run
def domain_statistics(all_statistics_results:list[dict], ex_task_eval_res:dict, ex_task_stat_res:dict,
    allowed_statistic_types:list[str]=["total_", "distr_"])->dict:
    # determine the evaluation attributes that are booleans and the statistic attributes that are averaged
    boolean_attributes = set()
    for key in ex_task_eval_res:
        if isinstance(ex_task_eval_res[key], bool): boolean_attributes.add(key)
    averaged_attributes = set()
    for key in ex_task_stat_res:
        if key.find("avg_") == 0: averaged_attributes.add(key[len("avg_"):])
    # gather the attributes needed
    ds = domain_statistics = {key:0 if key.find("total_")==0 else {}
        for key in ex_task_stat_res
        if any(key.find(word)==0 for word in allowed_statistic_types)}
    
    # Initialize per-run pass rate tracking
    run_counts = {}
    run_successes = {}
    
    # Process each task's statistics
    for task_stat_res in all_statistics_results:
        # Add the regular statistics
        for key in task_stat_res:
            if key.find("total_")==0: ds[key] += task_stat_res[key]
            elif key.find("distr_")==0: ds[key] = Counter(ds[key]) + Counter(task_stat_res[key])
        
        # Process per-run pass rates if available
        if "per_run_pass_rates" in task_stat_res:
            for run_key, pass_value in task_stat_res["per_run_pass_rates"].items():
                if run_key not in run_successes:
                    run_successes[run_key] = 0
                    run_counts[run_key] = 0
                run_successes[run_key] += pass_value
                run_counts[run_key] += 1
    
    # Calculate the per-run pass rates across all tasks
    if run_counts:
        ds["per_run_pass_rates"] = {}
        pass_rates = []
        
        for run_key in sorted(run_counts.keys()):
            pass_rate = run_successes[run_key] / run_counts[run_key] if run_counts[run_key] > 0 else 0
            ds["per_run_pass_rates"][run_key] = pass_rate
            pass_rates.append(pass_rate)
        
        # Calculate mean and std of per-run pass rates
        if pass_rates:
            ds["mean_pass_rate"] = sum(pass_rates) / len(pass_rates)
            
            # Calculate standard deviation
            if len(pass_rates) > 1:
                mean = ds["mean_pass_rate"]
                variance = sum((x - mean) ** 2 for x in pass_rates) / len(pass_rates)
                ds["std_pass_rate"] = math.sqrt(variance)
            else:
                ds["std_pass_rate"] = 0.0
    
    # calculating proportion and averages
    def get_underlying_attribute(attribute:str, statistic_types:list[str])->str:
        for stat_type in statistic_types:
            if stat_type in attribute: return attribute[len(stat_type):]
        return None
    ds_keys_copy = list(ds.keys())
    for key in ds_keys_copy:
        und_attr = get_underlying_attribute(key, allowed_statistic_types)
        if not und_attr: continue
        elif und_attr in boolean_attributes: ds[f"percentage_{und_attr}"] = round(ds[f"total_{und_attr}"] / ds[f"total_interactions"], 5)
        elif und_attr in averaged_attributes: ds[f"avg_{und_attr}"] = round(ds[f"total_{und_attr}"] / ds[f"total_interactions"], 5)
    return domain_statistics


def combine_numerical_dicts(d1:dict, d2:dict)->dict:
    """Combines two dictionaries with identical (nested) keys with totals as values"""
    d = copy.deepcopy(d1)
    for key in d:
        if isinstance(d[key], int): d[key] += d2[key]
        else: d[key] = combine_numerical_dicts(d[key], d2[key])
    return d


def combine_list_numerical_dicts(d_list:list[dict])->dict:
    """Combines a list of dictionaries with identical (nested) keys with totals as values"""
    if not d_list: return {}
    d = copy.deepcopy(d_list[0])
    for i in range(1, len(d_list)): d = combine_numerical_dicts(d, d_list[i])
    return d