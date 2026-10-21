"""
file that handles the read and write of external files, such as data inputs and output conversations
"""


import os
import math
import re
import json


# reading the keys from a separate file
def read_keys(keypath="keys")->dict:
    key_filenames = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(keypath) for f in filenames]
    if len(key_filenames) == 0:
        print("no keys read")
        return {"not_a_key": "not_a_key"}
    keys = {}
    for key_filename in key_filenames:
        # opening the key file
        key_file = open(key_filename, 'r', encoding='utf-8', errors='ignore')
        key = key_file.readline()
        if '\n' in key: key = key[:-1]
        key_file.close()
        # adding to the key dictionary
        key_name = key_filename[key_filename.find(keypath)+len(keypath)+1:key_filename.find(".txt")]
        keys[key_name] = key
    return keys

# loads environment variables from a .env file
def load_env_vars(env_file_path:str)->dict:
    """
    Load environment variables from a .env file
    
    Args:
        env_file_path (str): Path to the .env file
        
    Returns:
        dict: Dictionary of environment variables
    """
    if not os.path.exists(env_file_path):
        print(f"Warning: Environment file {env_file_path} not found")
        return {}
    
    env_vars = {}
    with open(env_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            key, value = line.split('=', 1)
            env_vars[key.strip()] = value.strip().strip('"\'')
            
            # Optionally set environment variables
            os.environ[key.strip()] = value.strip().strip('"\'')
            
    return env_vars

# returns the str data in a file
def read_data_file(data_dir:str, document_name:str)->str:
    res = None
    with open(os.path.join(data_dir, document_name), 'r', encoding='utf-8', errors='ignore') as f:
        res = f.read()
    return res

# writes to a file
def write_data_file(data_dir:str, document_name:str, data:str, option:str='w'):
    with open(os.path.join(data_dir, document_name), option, encoding='utf-8', errors='ignore') as f:
        f.write(data)

# obtains a list of filenames within a directory
def obtain_data_filenames(search_dir:str="data")->list[str]:
    res = []
    for item in os.listdir(search_dir):
        if os.path.isfile(os.path.join(search_dir, item)):
            res.append(item)
    return res

# makes a new run directory for the next available run count
def mkdir_newrun(output_dir:str="output", max_num_runs:int=10)->int:
    if max_num_runs <= 1: max_num_runs = 10
    run_num_next = -1
    max_num_runs_numchars = int(math.ceil(math.log(max_num_runs,10)))
    # check if output directory exists or not
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    run_num_currmax = -1
    search_dir = output_dir
    for item in os.listdir(search_dir):
        matches = re.search(r"\d+", item)
        if os.path.isdir(os.path.join(search_dir, item)) and int(matches.group(0)) > run_num_currmax:
            run_num_currmax = int(matches.group(0))
    if run_num_currmax >= max_num_runs-1: raise Exception("next run number exceeds max number runs")
    run_num_next = run_num_currmax + 1
    run_num_next_numchars = int(math.floor(math.log(max(run_num_next,1),10))) + 1
    run_str = "run" + "0" * (max_num_runs_numchars - run_num_next_numchars) + str(run_num_next)
    os.makedirs(os.path.join(output_dir, run_str))
    return run_num_next

# makes the next available run and interaction count if not specified
def write_output(output_dir:str="output", filename_full:str="inter",
    run_num:int=None, max_num_runs:int=10,
    interaction_num:int=None, max_num_interactions:int=10,
    output:str=None)->tuple[int, int]:
    filetype = filename_full[filename_full.find('.'):] if '.' in filename_full else None
    filename = filename_full if not filetype else filename_full[:filename_full.find('.')]
    # find number of characters the number needs
    if max_num_runs <= 1: max_num_runs = 10
    if max_num_interactions <= 1: max_num_interactions = 10
    max_num_runs_numchars = int(math.ceil(math.log(max_num_runs,10)))
    max_num_interactions_numchars = int(math.ceil(math.log(max_num_interactions,10)))
    # finds the run directory string, makes the output and run directories if not specified or does not exist
    if run_num is None: run_num = mkdir_newrun(output_dir, max_num_runs)
    run_num_numchars = int(math.floor(math.log(max(run_num,1),10))) + 1
    run_str = "run" + "0" * (max_num_runs_numchars - run_num_numchars) + str(run_num)
    search_dir = os.path.join(output_dir, run_str)
    if not os.path.exists(search_dir): os.makedirs(search_dir)
    # make a new output interaction file if not specified
    if not interaction_num:
        interaction_num_currmax = -1
        search_dir = os.path.join(output_dir, run_str)
        for item in os.listdir(search_dir):
            filename_matches = re.search(rf"{filename}\d+", item)
            number_matches = re.search(r"\d+", item)
            if os.path.isfile(os.path.join(search_dir, item))\
                and filename_matches and int(number_matches.group(0)) > interaction_num_currmax:
                interaction_num_currmax = int(number_matches.group(0))
        interaction_num = interaction_num_currmax + 1
    interaction_num_numchars = int(math.floor(math.log(max(interaction_num,1),10))) + 1
    interaction_filename = filename + "0" * (max_num_interactions_numchars - interaction_num_numchars) + str(interaction_num)
    # appending to the contents of the file
    interaction_filename_full = interaction_filename + ".txt" if not filetype else interaction_filename + filetype
    with open(os.path.join(output_dir, run_str, interaction_filename_full), 'a', encoding='utf-8', errors='ignore') as f:
        f.write(output)
    # return the run number an interaction number for future reference
    return run_num, interaction_num

# renumbers the run numbers if there are increments missing in between
def renumber_runs(output_dir:str="output", max_num_runs:int=10):
    if max_num_runs <= 1: max_num_runs = 10
    max_num_runs_numchars = int(math.ceil(math.log(max_num_runs,10)))
    # finding the run numbers and sorting, assumes all items in output_dir are run directories
    run_nums = []
    for item in os.listdir(output_dir):
        matches = re.search(r"\d+", item)
        if os.path.isdir(os.path.join(output_dir, item)): run_nums.append(int(matches.group(0)))
    run_nums.sort()
    # renumbering if the numbers are not consecutive
    for i in range(len(run_nums)):
        run_num = run_nums[i]
        if i == run_num: continue
        run_num_wrong_numchars = int(math.floor(math.log(max(run_num,1),10))) + 1
        run_wrong_str = "run" + "0" * (max_num_runs_numchars - run_num_wrong_numchars) + str(run_num)
        run_num_corr_numchars = int(math.floor(math.log(max(i,1),10))) + 1
        run_corr_str = "run" + "0" * (max_num_runs_numchars - run_num_corr_numchars) + str(i)
        os.rename(os.path.join(output_dir, run_wrong_str), os.path.join(output_dir, run_corr_str))
        
# finds the proper run_dir given the output_dir and run_num
def get_rundir(output_dir:str, run_num:int, run_dirname:str="run")->str:
    for item in os.listdir(output_dir):
        matches = re.search(r"\d+", item)
        if os.path.isdir(os.path.join(output_dir, item)) and matches\
            and run_num == int(matches.group(0)) and run_dirname in item:
            return item
    return None
        
# gets the full list of log of interactions in a run
def read_all_interaction_log(output_dir:str, run_num:int, run_dirname:str="run", log_filename:str="log.json")->dict[str:dict]:
    run_dir = get_rundir(output_dir, run_num, run_dirname)
    if not run_dir: return None
    # accessing each log in order, indicies should be consecutive
    search_dir = os.path.join(output_dir, run_dir)
    dot_pos = log_filename.find('.')
    search_template = rf"{log_filename[:dot_pos]}\d+{log_filename[dot_pos:]}"
    log_files = []
    for item in os.listdir(search_dir):
        matches = re.search(search_template, item)
        if os.path.isfile(os.path.join(search_dir, item)) and matches: log_files.append(matches.group(0))
    log_files.sort()
    # reading dead log file
    all_interaction_log = {}
    for log_file in log_files:
        all_interaction_log[log_file] = json.loads(read_data_file(search_dir, log_file))
    return all_interaction_log

# writes the evaluation results into the logs and interaction file
def write_all_evaluation_result(log_filenames:list[str], aer:list[dict], aers:list[str], output_dir:str, run_num:int, run_dirname:str="run", inter_filename:str="inter.txt"):
    run_dir = get_rundir(output_dir, run_num, run_dirname)
    # writing the evaluation results into each log and interaction
    search_dir = os.path.join(output_dir, run_dir)
    dot_pos = inter_filename.find('.')
    for i in range(len(log_filenames)):
        log_file = log_filenames[i]
        evaluation_result = aer[i]
        evaluation_result_str = aers[i]
        # write the evaluation into the log file
        log_output = json.loads(read_data_file(search_dir, log_file))
        log_output["evaluation_result"] = evaluation_result
        with open(os.path.join(search_dir, log_file), 'w', encoding='utf-8', errors='ignore') as f:
            f.write(json.dumps(log_output, indent=4))
        # write the evaluation into the interaction file
        num_str = re.search(r"\d+", log_file).group(0)
        inter_file = f"{inter_filename[:dot_pos]}{num_str}{inter_filename[dot_pos:]}"
        with open(os.path.join(search_dir, inter_file), 'a', encoding='utf-8', errors='ignore') as f:
            f.write("\n\n\n" + evaluation_result_str)

# reads and returns the filenames in a directory
def read_filenames_in_dir(search_dir:str, ignore_filetypes=["statistics_"])->list[str]:
    filenames = []
    for item in os.listdir(search_dir):
        if not any(item.find(word)==0 for word in ignore_filetypes)\
            and os.path.isfile(os.path.join(search_dir, item)): filenames.append(item)
    return filenames

# writes the data to the data directory, writes the dictionary without the first indent
def write_tasks(tasks:dict, domain_system_dir:str, tasks_filename:str, indent_amount:int):
    first_bool = True
    for user_goal in tasks:
        dict_key_str = f",\n\"{user_goal}\": " if not first_bool else f"{{\n\"{user_goal}\": "
        write_data_file(domain_system_dir, tasks_filename,
            dict_key_str+json.dumps(tasks[user_goal], indent=indent_amount), option="a" if not first_bool else 'w')
        first_bool = False
    write_data_file(domain_system_dir, tasks_filename, "\n}", option="a")