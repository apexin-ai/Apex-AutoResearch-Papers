"""
This file is for manual operations, manually editting data or manually performing some action.
"""

from env.check_data_sanity import domain_test_keys, run_domain_tests
from env.file_read_write import read_data_file, write_data_file
from env.variables import domain_keys, domain_assistant_keys
from env.helpers import get_action_parameters, dict_to_tuple, tuple_to_dict, hashable_dep, orig_dep,\
    gather_action_default_dependencies, dfsgather_actions_required, dfsins_cl_cd_aid, dfsgather_invfunccalldirgraph
from env.generation import verify_database_format, verify_gen_succ, get_dict_str, dfsgather_dep_tree_vis
from env.generation_test import generation_testing
from env.evaluator_test import evaluator_testing
from env.paper.paper_display_info import paper_display_info

import json
import copy

from openai.types.beta.threads.run import Usage


"""helper functions"""

# reads the dataset, performs an operation, writes back to the dataset with the change
def read_operation_write(operation:callable):
    def wrapper(data_dir:str, domain_str:str, indent_amount:int, *args, **kwargs):
        # open and read the file
        tasks_filename = f"{domain_str}_tasks.json"
        intermediate_tasks_filename = f"{domain_str}_intermediate_tasks.json"
        tasks = json.loads(read_data_file(data_dir, tasks_filename))
        intermediate_tasks = json.loads(read_data_file(data_dir, intermediate_tasks_filename))
        # perform some sort of operation
        tasks, intermediate_tasks = operation(domain_str, tasks, intermediate_tasks, *args, **kwargs)
        # write back to the file
        def write_datafile_formatted(tasks:dict, filename:str):
            first_bool = True
            for user_goal in tasks:
                dict_key_str = f",\n\"{user_goal}\": " if not first_bool else f"{{\n\"{user_goal}\": "
                write_data_file(data_dir, filename,
                    dict_key_str+json.dumps(tasks[user_goal], indent=indent_amount), option="a" if not first_bool else 'w')
                first_bool = False
            write_data_file(data_dir, filename, "\n}", option="a")
        write_datafile_formatted(tasks, tasks_filename)
        write_datafile_formatted(intermediate_tasks, intermediate_tasks_filename)
    return wrapper


"""running the domain tests"""

# runs the domain tests of every domain
# def run_all_domain_tests(print_test_domain:bool, test_domain_assistant:bool, data_dir:str, assistant_file:str, openai_api_key:[REDACTED], gpt_model:str,
#     dependency_location:str, default_dependency:str, print_pipeline:bool, shuffle_assfun:bool):
#     all_run_usage = []
#     for key in domain_test_keys:
#         _, _, test_run_usage = run_domain_tests(key, print_test_domain, test_domain_assistant,
#             data_dir, assistant_file, openai_api_key, gpt_model,
#             dependency_location, default_dependency, print_pipeline, shuffle_assfun)
#         all_run_usage.extend(test_run_usage)
#     return all_run_usage


"""a set of operations that deal with the tasks dataset"""

# finds how many tasks of each action need fixing
@read_operation_write
def find_manfix_params(domain_str:str, tasks:dict, intermediate_tasks:dict):
    manfix_counters = {}
    for user_goal in tasks:
        for task in tasks[user_goal]:
            if "manfix_id" not in task and "manfix_constrs" not in task: continue
            if user_goal not in manfix_counters: manfix_counters[user_goal] = 1
            else: manfix_counters[user_goal] += 1
    if manfix_counters:
        print("list of actions and their manfix counters:")
        print(get_dict_str(manfix_counters))
        print("ctrl+f \"manfix_id\" to find them in the data")
    else: print("no methods to fix")
    return tasks, intermediate_tasks

# cleans the manfix parameters
@read_operation_write
def clean_manfix_params(domain_str:str, tasks:dict, intermediate_tasks:dict):
    for user_goal in tasks:
        for task in tasks[user_goal]:
            if "manfix_id" in task: del task["manfix_id"]
            if "manfix_constrs" in task: del task["manfix_constrs"]
    return tasks, intermediate_tasks

# 0 for correct, 1 for database mismatch, 2 for user known mismatch, 3 for constraints not followed
def verify_task(user_goal:str, domain_str:str, task:dict, intermediate_task:dict, example_database:dict, example_dep_params:dict,
    aid:dict, cl:dict, cd:dict, ad:dict, action_default_dep_orig:dict,
    action_parameters:dict, hashed_cl_funcs:dict)->tuple[int,dict]:
    dep, dep_perm, task_succ = task["constraints"], intermediate_task["dependency_permutation"], task["action_should_succeed"]
    # verification of json parsing error
    if (isinstance(task["initial_database"], str)
        or isinstance(task["constraint_parameters"], str)
        or isinstance(task["user_known"], str)):
        return 2, None
    # verification of database and user_known format
    database_format_match_bool, initial_database = verify_database_format(task["initial_database"], example_database)
    if not database_format_match_bool: return 3, None
    else: task["initial_database"] = initial_database
    dep_params = task["constraint_parameters"]
    matching_keys_dep_params = set(example_dep_params.keys()) == set(dep_params.keys())
    matching_keys_user_known = set(intermediate_task["user_params"]) == set(task["user_known"].keys())
    if not matching_keys_dep_params or not matching_keys_user_known: return 4, None
    # variable formatting
    class Task_Imitator:
        def __init__(self, initial_database:dict, dependency_parameters:dict, user_known:dict):
            self.initial_database_str = json.dumps(initial_database)
            self.dependency_parameters_str = json.dumps(dependency_parameters)
            self.user_known_str = json.dumps(user_known)
    task_obj = Task_Imitator(task["initial_database"], task["constraint_parameters"], task["user_known"])
    task_single = {}
    for i in range(len(intermediate_task["inv_task_single"])):
        exp_res = i if i < 2 else -1
        for constr in intermediate_task["inv_task_single"][i]:
            task_single[hashable_dep(constr)] = exp_res
    # task verification
    actions_required = dfsgather_actions_required(dep_perm, hashed_cl_funcs) # derive the actions required through the constraint links
    actions_required = [(func_str, tuple_to_dict(hashed_func_params)) for func_str, hashed_func_params in actions_required]
    actions_required.append((user_goal, {func_param: func_param for func_param in action_parameters[user_goal]}))
    all_def_dep_perm = copy.deepcopy(action_default_dep_orig) # preparing the default permutation dependencies
    all_def_dep_perm = {key: dfsins_cl_cd_aid(all_def_dep_perm[key], cl, aid, ad, cd, action_parameters) for key in all_def_dep_perm}
    constraints_followed, verification_result = verify_gen_succ(task_obj, dep, dep_perm, domain_str, user_goal,
        aid, ad, all_def_dep_perm, actions_required, task_single, bool(task_succ), cl, cd, action_parameters)
    return 0 if constraints_followed else 1, verification_result

# calculates and writes into the file which tasks need to be manually fixed
@read_operation_write
def calc_manfix_params(domain_str:str, tasks:dict, intermediate_tasks:dict, default_dependency_option:str):
    # domain data
    dss = domain_keys[domain_str+"_strict"]()
    ds = dss.evaluation_get_domain_system()
    example_database = dss.evaluation_get_database()
    example_dep_params = dss.evaluation_get_dependency_parameters()
    # domain assistant data
    aid = domain_assistant_keys[domain_str].action_innate_dependencies
    ard = domain_assistant_keys[domain_str].action_required_dependencies
    acd = domain_assistant_keys[domain_str].action_customizable_dependencies
    cl = domain_assistant_keys[domain_str].constraint_links
    cd = domain_assistant_keys[domain_str].constraint_dependencies
    ad = gather_action_default_dependencies(ard, acd, cd, default_dependency_option)
    action_default_dep_orig = gather_action_default_dependencies(ard, acd, default_dependency_option=default_dependency_option)
    # derived data
    action_parameters = get_action_parameters(ds, domain_assistant_keys[domain_str])
    hashed_cl_funcs = {(cl[constr][0], dict_to_tuple({func_param: func_param for func_param in action_parameters[cl[constr][0]]})) for constr in cl}
    # looping through the tasks
    for user_goal in tasks:
        manfix_counter = 0
        for i in range(len(tasks[user_goal])):
            task, intermediate_task = tasks[user_goal][i], intermediate_tasks[user_goal][i]
            # verification
            res, vr = verify_task(user_goal, domain_str, task, intermediate_task, example_database, example_dep_params,
                aid, cl, cd, ad, action_default_dep_orig, action_parameters, hashed_cl_funcs)
            # error writing
            match res:
                case 0: continue
                case 1: manfix_constrs = [(f"exp {vr[hc][0]} act {vr[hc][1]}", orig_dep(hc)) for hc in vr]
                case 2: manfix_constrs = ["json error"]
                case 3: manfix_constrs = ["database format mismatch"]
                case 4: manfix_constrs = ["user_known or dependency_parameters key mismatch"]
            manfix = {"manfix_id": f"{user_goal}_{manfix_counter}", "manfix_constrs": manfix_constrs}
            task.update(manfix)
            manfix_counter += 1
    return tasks, intermediate_tasks


"""temporary actions that are not needed with the finished task generation pipeline"""

# adds the actions required into the intermediate tasks after task generation
@read_operation_write
def add_actions_required_intertasks(domain_str:str, tasks:dict, intermediate_tasks:dict, default_dependency_option:str):
    dss = domain_keys[domain_str+"_strict"]()
    ds = dss.evaluation_get_domain_system()
    # assistant variable loading
    aid = domain_assistant_keys[domain_str].action_innate_dependencies
    ard = domain_assistant_keys[domain_str].action_required_dependencies
    acd = domain_assistant_keys[domain_str].action_customizable_dependencies
    cl = domain_assistant_keys[domain_str].constraint_links
    cd = domain_assistant_keys[domain_str].constraint_dependencies
    ad = gather_action_default_dependencies(ard, acd, cd, default_dependency_option)
    # derived variables
    action_parameters = get_action_parameters(ds, domain_assistant_keys[domain_str])
    hashed_cl_funcs = {(cl[constr][0], dict_to_tuple({func_param: func_param for func_param in action_parameters[cl[constr][0]]})) for constr in cl}
    # loop through all tasks
    for user_goal in tasks:
        for i in range(len(tasks[user_goal])):
            dep_orig = tasks[user_goal][i]["constraints_original"]
            dep_perm = dfsins_cl_cd_aid(dep_orig, cl, aid, ad, cd, action_parameters)
            actions_required = dfsgather_actions_required(dep_perm, hashed_cl_funcs)
            actions_required = [(func_str, tuple_to_dict(hashed_func_params)) for func_str, hashed_func_params in actions_required]
            actions_required.append((user_goal, {func_param: func_param for func_param in action_parameters[user_goal]}))
            intermediate_tasks[user_goal][i]["actions_required"] = actions_required
    return tasks, intermediate_tasks

# adds the inverse function call graph into the task
@read_operation_write
def add_invfunccallgraph_tasks(domain_str:str, tasks:dict, intermediate_tasks:dict, default_dependency_option:str):
    # domain data
    dss = domain_keys[domain_str+"_strict"]()
    ds = dss.evaluation_get_domain_system()
    # domain assistant data
    ard = domain_assistant_keys[domain_str].action_required_dependencies
    acd = domain_assistant_keys[domain_str].action_customizable_dependencies
    cl = domain_assistant_keys[domain_str].constraint_links
    cp = domain_assistant_keys[domain_str].constraint_processes
    action_default_dep_orig = gather_action_default_dependencies(ard, acd, default_dependency_option=default_dependency_option)
    # derived data
    action_parameters = get_action_parameters(ds, domain_assistant_keys[domain_str])
    # loop through all user goals and tasks
    for user_goal in tasks:
        for i in range(len(tasks[user_goal])):
            # gather information from the task
            dep_orig = tasks[user_goal][i]["constraints_original"]
            # find the inverse function call graph
            user_goal_node = (user_goal, {key: key for key in action_parameters[user_goal]})
            inv_func_call_graph = dfsgather_invfunccalldirgraph(dep_orig, cl, cp, action_default_dep_orig, action_parameters, user_goal_node)
            # assign the graph
            tasks[user_goal][i]["inv_func_call_graph"] = inv_func_call_graph
    return tasks, intermediate_tasks


"""list of all manual opertion options"""

# chooses which manual operation to perform
def manual_operation(args)->list[Usage]:
    all_run_usage = []
    match args.manual_option:
        # running tests: domain, task_generation
        # case 0: all_run_usage = run_all_domain_tests(args.print_test_domain, args.test_domain, args.data_dir, args.assistant_file,
        #     args.openai_api_key, args.gpt_model, args.dependency_location, args.default_dependency_option,
        #     args.print_pipeline_disable, args.shuffle_assfun_disable)
        case 1:
            generation_testing()
            evaluator_testing()
        # manually fixing the data
        case 2: find_manfix_params(args.data_dir, args.domain_str, args.indent_amount)
        case 3: clean_manfix_params(args.data_dir, args.domain_str, args.indent_amount)
        case 4: calc_manfix_params(args.data_dir, args.domain_str, args.indent_amount, args.default_dependency_option)
        case 5:
            clean_manfix_params(args.data_dir, args.domain_str, args.indent_amount)
            calc_manfix_params(args.data_dir, args.domain_str, args.indent_amount, args.default_dependency_option)
            find_manfix_params(args.data_dir, args.domain_str, args.indent_amount)
        # temporary operations
        case 6: add_actions_required_intertasks(args.data_dir, args.domain_str, args.indent_amount, args.default_dependency_option)
        case 7: add_invfunccallgraph_tasks(args.data_dir, args.domain_str, args.indent_amount, args.default_dependency_option)
        # display information for the paper
        case 8: paper_display_info(args)
        # invalid option selected
        case _: print("no valid manual option selected")
    return all_run_usage