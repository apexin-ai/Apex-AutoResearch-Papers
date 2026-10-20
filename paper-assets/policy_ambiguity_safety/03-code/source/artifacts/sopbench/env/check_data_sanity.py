"""
checks the data sanity of the assistants
should be universal across all domains
"""


from env.variables import domain_keys
from env.file_read_write import read_data_file

import json

from openai.types.beta.threads.run import Usage


# base cases for fail: one is a value and one is an instance, parameter within a parameter, either could be None
# recursive cases for fail: two instance formats differ, two of the same parameter formats differ
def recur_data_consistency(d1, d2)->bool:
    if not d1 or not d2 or not isinstance(d1, dict) and not isinstance(d2, dict):
        return True # neither are instances (always dict)
    res = True
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    for d1_key in d1_keys:
        # keys are the different: d1 and d2 are parameters
        if d1_keys != d2_keys:
            for d2_key in d2_keys:
                if ((isinstance(d1[d1_key], dict) and isinstance(d2[d2_key], dict) and d1[d1_key].keys() != d2[d2_key].keys())
                    or (isinstance(d1[d1_key], dict) or isinstance(d2[d2_key], dict)) and type(d1[d1_key]) != type(d2[d2_key])):
                    return False # parameter within a parameter case
                res = res and recur_data_consistency(d1[d1_key], d2[d2_key])
        # keys are the same: d1 and d2 are instances
        else:
            if (isinstance(d1[d1_key], dict) or isinstance(d2[d1_key], dict)) and type(d1[d1_key]) != type(d2[d1_key]):
                return True # instances could have parameters with different types dict and str
            res = res and recur_data_consistency(d1[d1_key], d2[d1_key])
    return res
# test for the data consistency of the default data and the initial data for the domain system
def test_default_and_initial_data_consistency(domain_dir:str, domain_str:str)->list[str]:
    default_data = domain_keys[domain_str]().data
    initial_data = json.loads(read_data_file(f"{domain_dir}\\{domain_str}", f"{domain_str}_data.json"))
    failures = [] if recur_data_consistency(default_data, initial_data) else ["default and initial data format do not match"]
    return failures

# checks for data sanity, True for success, False for failure (with a string error message)
def check_data_sanity(domain_dir:str, domain_str:str)->list[tuple[bool, str]]:
    failures = []
    
    return failures


"""section for collecting the domain tests"""

# from env.domains.test.test_test import test_test
domain_test_keys = {
    "bank": None,
    "dmv": None,
    "healthcare": None,
    "online_market": None,
    "library": None
}

def run_domain_tests(domain_str:str, print_test_domain:bool, test_domain_assistant:bool, data_dir:str, assistant_file:str, openai_api_key:[REDACTED], gpt_model:str,
    dependency_location:str, default_dependency:str, print_pipeline:bool, shuffle_assfun:bool)->tuple[list[callable],list[bool],list[Usage]]:
    if not domain_test_keys[domain_str]: return [], [], []
    return domain_test_keys[domain_str](print_test_domain, test_domain_assistant, data_dir, assistant_file, openai_api_key, gpt_model,
        dependency_location, default_dependency, print_pipeline, shuffle_assfun)