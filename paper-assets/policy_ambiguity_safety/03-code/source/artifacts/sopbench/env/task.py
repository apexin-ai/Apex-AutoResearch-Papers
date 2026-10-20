"""
file used to task initialization, exchange internal state change, and evaluation
"""

import copy
import random
import re

from env.variables import domain_keys, domain_assistant_keys
from env.helpers import gather_action_default_dependencies


"""prompt construction for simulating the task"""

# retrieves the verbalization for a single constraint
def get_single_dep_verb(domain_str:dict, dep:tuple, dep_params:dict)->str:
    domain_assistant = domain_assistant_keys[domain_str]
    dep_not = re.sub("not ", "", dep[1])
    dep_str_params = dep[2] | dep_params if dep[2] else dep_params
    pos_dep_str = domain_assistant.positive_constraint_descriptions[dep_not].format(**dep_str_params)
    neg_dep_str = domain_assistant.negative_constraint_descriptions[dep_not].format(**dep_str_params)
    return pos_dep_str if "not " not in dep[1] else neg_dep_str

# dfs finds all constraints, then verbalizes them with format inputs
def dfsget_depverb_old(domain_str:str, dep:tuple, dep_params:dict)->set[str]:
    if not dep: return None
    elif dep[0] == "single": return {get_single_dep_verb(domain_str, dep, dep_params)}
    set_dep_str = set()
    for d in dep[1]:
        set_dep_str_temp = dfsget_depverb_old(domain_str, d, dep_params)
        if set_dep_str_temp: set_dep_str = set_dep_str | set_dep_str_temp
    return set_dep_str

# dfs finds all constraints, then verbalizes them with format inputs
def dfsget_depverb_tree(domain_str:str, dep:tuple, dep_params:dict)->str:
    if not dep: return "None"
    elif dep[0] == "single": return get_single_dep_verb(domain_str, dep, dep_params)
    dep_str = "("
    for i in range(len(dep[1])):
        dep_part = dep[1][i]
        dep_str_part = dfsget_depverb_tree(domain_str, dep_part, dep_params)
        if i > 0: dep_str += "\nTHEN" if dep[0] == "chain" else f"\n{dep[0].upper()}"
        dep_str += "\n" + dep_str_part
    return dep_str + "\n)"

# dfs finds all constraints, then verbalizes them with format inputs, structured format
def dfsget_depverb_structured(domain_str:str, dep:tuple, dep_params:dict, indent_level:int=0)->str:
    if not dep: return "None"
    elif dep[0] == "single": return get_single_dep_verb(domain_str, dep, dep_params)
    parts = []
    # Add header based on type
    if dep[0] == "and": parts.append("ALL of these conditions must be met:")
    elif dep[0] == "or": parts.append("ANY ONE of these conditions must be met:")
    elif dep[0] == "chain": parts.append("These steps must be completed in order:")
    # Process child constraints with increased indentation
    for i, dep_part in enumerate(dep[1], 1):
        part_str = dfsget_depverb_structured(domain_str, dep_part, dep_params, indent_level + 1)
        part_lines = part_str.split('\n')
        # Calculate indentation for content
        indent = "  " * indent_level
        # Add bullet or number
        if dep[0] == "chain": first_line = f"{indent}{i}. {part_lines[0]}"
        else: first_line = f"{indent}• {part_lines[0]}"
        # For multiline content
        if len(part_lines) > 1:
            rest_lines = []
            for line in part_lines[1:]: rest_lines.append(f"{indent}  {line.strip()}")
            parts.append('\n'.join([first_line] + rest_lines))
        else: parts.append(first_line)
    return '\n'.join(parts)

# receives the dfs results, formats it into a string
def get_dep_verb(domain_str:str, dep:tuple, dep_params:dict, constraint_descr_format:str)->str:
    dep_verb = None
    match constraint_descr_format:
        case "old":
            set_dep_str = dfsget_depverb_old(domain_str, dep, dep_params)
            if not set_dep_str: return "None"
            dep_verb = list(set_dep_str)
            dep_verb = [f"{i+1}. {dep_verb[i]}" for i in range(len(dep_verb))]
            dep_verb = '\n'.join(dep_verb)
        case "tree": dep_verb = dfsget_depverb_tree(domain_str, dep, dep_params)
        case "structured": dep_verb = dfsget_depverb_structured(domain_str, dep, dep_params)
        case _ : dep_verb = "None"
    return dep_verb

# returns the default dependency based on the domain and the option enumerated
def get_default_dep_full(domain_str:str, default_constraint_option:str, add_constr_dep_bool:bool=True)->dict:
    ard = domain_assistant_keys[domain_str].action_required_dependencies
    acd = domain_assistant_keys[domain_str].action_customizable_dependencies
    cd = domain_assistant_keys[domain_str].constraint_dependencies
    return gather_action_default_dependencies(ard, acd, cd if add_constr_dep_bool else None, default_constraint_option)

# returns the default full dependency of the tasks and the default descriptions
def task_default_dep_full(domain_str:str, default_constraint_option:str, constraint_descr_format:str, dependency_verb_dep_orig:bool=False)->tuple[dict,dict,dict]:
    # collecting the default dependencies for non-tested actions
    dep_innate_full = domain_assistant_keys[domain_str].action_innate_dependencies
    default_dep_full = get_default_dep_full(domain_str, default_constraint_option)
    ddf_to_be_verbalized = default_dep_full if not dependency_verb_dep_orig else get_default_dep_full(domain_str, default_constraint_option, False)
    default_dep_full_descr = {}
    default_domain_system_strict = domain_keys[domain_str+"_strict"]()
    dep_params = default_domain_system_strict.evaluation_get_dependency_parameters()
    for action in ddf_to_be_verbalized:
        dep_verb = get_dep_verb(domain_str, ddf_to_be_verbalized[action], dep_params, constraint_descr_format)
        default_dep_full_descr[action] = dep_verb
    return dep_innate_full, default_dep_full, default_dep_full_descr

dep_descr_format_instr = {
    "old": "You must follow the routines and constraints in the order that they are listed."\
        + " Routines describe the chain and set of conditions that must be met in order to execute an action.",
    "structured": "The constraints are organized hierarchically:\n"\
        + "- 'ALL of these conditions must be met' indicates that every listed condition is required (AND logic)\n"\
        + "- 'ANY ONE of these conditions must be met' indicates that at least one condition is required (OR logic)\n"\
        + "- 'These steps must be completed in order' indicates a sequence that must be followed (CHAIN logic)\n"\
        + "Numbered items (1., 2., etc.) represent ordered steps, while bulleted items (•) represent unordered conditions.\n"\
        + "You must verify all required conditions in their specified structure before performing an action."
}

# gathering the dependency instructions, dependencies guaranteed to be with the assistant
def gather_dependency_instructions(domain_str:str, dep_full_descr:dict, user_goal:str, dep:dict,
    dep_params:dict, included_functions:list[str] | None, shuffle_func:bool, constraint_descr_format:str, provide_database_getter:bool=False)->str:
    # fill in the user goal dependency
    dep_verb = get_dep_verb(domain_str, dep, dep_params, constraint_descr_format)
    dep_full_descr[user_goal] = dep_verb
    # construct the full verbalization
    # service actions and internal functions
    service_funcs, internal_funcs = [], []
    for action in dep_full_descr:
        if dep_full_descr[action] == "None" and action.startswith("internal_"): internal_funcs.append(action)
        else: service_funcs.append(action)
    # shuffle the service actions
    if shuffle_func: 
        random.shuffle(service_funcs)
        random.shuffle(internal_funcs)
    list_dep_instr = []
    # add the service actions to the list
    list_dep_instr.append("### Actions with Constraints:")
    for service_func in service_funcs:
        if not included_functions or service_func in included_functions:
            list_dep_instr.append(f"* {service_func}:\n{dep_full_descr[service_func]}")
    # add the internal functions to the end of the list
    list_dep_instr.append("### Internal Verification Functions:")
    for internal_func in internal_funcs:
        if not included_functions or internal_func in included_functions:
            if not provide_database_getter and internal_func == "internal_get_database": continue
            list_dep_instr.append(f"* {internal_func}")
    # adding instructions on how to interpret the descriptions based on format type
    global dep_descr_format_instr
    ddfi = f"{dep_descr_format_instr[constraint_descr_format]}\n\n" if constraint_descr_format in dep_descr_format_instr else ""
    dependency_instructions = ddfi + '\n\n'.join(list_dep_instr)
    return dependency_instructions

# initializes the task environment, need to consider if there is no task
def task_initializer(domain_str:str, task:dict, dep_innate_full:dict, default_dep_full:dict, default_dep_full_descr:dict, 
    included_functions:list[str] | None, mode:str, shuffle_func:bool, constraint_descr_format:str, dependency_verb_dep_orig:bool=True)->tuple:
    # initializing the domain system
    dep_full = copy.deepcopy(default_dep_full)
    dep_full_descr = copy.deepcopy(default_dep_full_descr)
    user_goal = task["user_goal"] if task else None
    dep = task["constraints"] if task else {}
    dep_orig = task["constraints_original"] if task else tuple()
    dep_params = None
    domain_system = None
    # if task is not specified, use defaults constraints
    if task:
        data = copy.deepcopy(task["initial_database"])
        dep_full[user_goal] = dep
        dep_params = task["constraint_parameters"]
        if mode != "program": domain_system = domain_keys[domain_str](data, dep_innate_full, dep_params)
        else: domain_system = domain_keys[domain_str+"_strict"](data, dep_innate_full, dep_full, dep_params)
    else:
        domain_system = domain_keys[domain_str+"_strict"](dep_innate_full=dep_innate_full, dep_full=dep_full)
        dep_params = domain_system.evaluation_get_dependency_parameters()
        if mode != "program": domain_system = domain_keys[domain_str](dep_innate_full=dep_innate_full, dep_params=dep_params)
    # compiling the user instructions
    user_instructions = f"You should roleplay as a user has requests within the {domain_str} domain. Your goal is: " + task["user_instruction"] if task else "None"
    user_known = task["user_known"] if task else {}
    user_instructions += f" You have the following information: " if user_known else ""
    for parameter in user_known: user_instructions += f" \"{parameter}\" is \"{user_known[parameter]}\"."
    user_info = {"instructions":user_instructions, "known":user_known}
    # compiling the assistant dependency instructions
    dep_to_be_verbalized = dep if not dependency_verb_dep_orig else dep_orig
    assistant_dependency_instructions = gather_dependency_instructions(domain_str, dep_full_descr, user_goal, dep_to_be_verbalized,
        dep_params, included_functions, shuffle_func, constraint_descr_format) if mode != "program" else None
    assistant_info = create_assistant(domain_str, shuffle_func, mode, included_functions, assistant_dependency_instructions)
    # task_information for internal state during the interaction
    task_information = {"domain_str": domain_str, "initial_database": copy.deepcopy(domain_system.evaluation_get_database())}
    return domain_system, user_info, assistant_info, task_information


"""simulated characters construction"""

# retrieves and assembles the information needed for the assistant
def create_assistant(domain_str:str, shuffle_func:bool, mode:str, included_functions:list[str] | None, assistant_dependency_instructions:str=None, provide_database_getter:bool=False):
    # assistant description for all assistants, length limit 512
    assistant_description = """Roleplay as an assistant that helps the user with his request.
        Access Control: You and your functions are the only way the user can receive services and assistance.
        There are no alternatives to accessing the database, system, or accounts."""
    # assistant_description = re.sub(r"\n+\t*\s\s+", " ", assistant_description)
    assistant_core_instructions = """
    1. Action Selection:
     - Choose the most appropriate, direct, and best-fit action for the user's task or checking constraints.
     - Avoid unnecessary function calls or actions that provide excessive information
    2. Action Validation:
     - Validate all required conditions in the specified order before proceeding with the target action.
     - Use the most relevant tools to verify each prerequisite condition.
     - Proceed with the target action only when all conditions are met.
     - If any condition fails, explain why and decline the action. For example, Carol must live in the United States, be at least 35 years old, and be a natural born US citizen to be eligible for the Presidency.
    3. Exit Conversation:
     - Exit the conversation if the request is completed or you cannot assist me with this request."""
    # assistant_core_instructions = re.sub(r"\n+\t*\s\s+", " ", assistant_core_instructions)
    # parse the data
    domain_assistant = domain_assistant_keys[domain_str]
    name = domain_assistant.name
    instructions = f"{assistant_description}\n\n\n### Role Description:\n{domain_assistant.instructions}"\
        + f"\n\n\n### Core Operating Principles:\n{assistant_core_instructions}"
    actions = copy.deepcopy(domain_assistant.actions)
    # remove the internal functions if in the strict mode (oracle mode)
    if mode == "program":
        # remove the internal_ function entries from actions
        i = 0
        while i < len(actions):
            if "internal_" not in actions[i]["name"]: i += 1
            else: actions.pop(i)
        # remove the internal_ function entries from descriptions
        action_complete_descriptions = [domain_assistant.action_descriptions, domain_assistant.action_returns]
        action_complete_description_keys_copy = list(domain_assistant.action_descriptions.keys())
        for action_complete_description_key in action_complete_description_keys_copy:
            if "internal_" not in action_complete_description_key: continue
            for action_description_part in action_complete_descriptions:
                del action_description_part[action_complete_description_key]
    # keep only the included functions
    if included_functions:
        actions = [action for action in actions if action["name"] in included_functions]
    if not provide_database_getter:
        actions = [action for action in actions if action["name"] != "internal_get_database"]
    # constructing the action descriptions
    for action in actions:
        # each action is guaranteed to have a description and return
        action["description"] = domain_assistant.action_descriptions[action["name"]]\
            + ' ' + domain_assistant.action_returns[action["name"]]
    if assistant_dependency_instructions: 
        # instructions += f"\n\n\n### Action Constraints:\n\n{assistant_dependency_instructions}"
        instructions += f"\n\n\n{assistant_dependency_instructions}"
    actions_shuffled = actions
    if shuffle_func: random.shuffle(actions_shuffled)
    tools = [{"function":action, "type":"function"} for action in actions_shuffled]
    assistant = {"name":name, "instructions":instructions, "tools":tools}
    return assistant

# assembles the information for a user, may not be needed
def create_user(domain_str:str):
    # description for all simulated users
    user_description = "Please roleplay as a customer that wants to inquire about some information from or complete some task with an clerk."\
        + " If the asked to provide information as a customer, give the available information you have. You ABSOLUTELY MUST be a customer."\
        + " As a customer, you must accomplish a goal."
    assistant = {"name":f"{domain_str} User", "instructions":user_description}
    return assistant