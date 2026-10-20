"""
main file to run our pipeline
"""


"""imports"""
from env.file_read_write import read_keys, write_data_file, read_data_file
from env.variables import OPENAI_MODEL_COST_PER_1M_TOKENS
from env.operation import manual_operation

import argparse
import os


"""main function"""

if __name__ == "__main__":
    # parsing arguments
    parser = argparse.ArgumentParser(description="Run task (0) simulation, (1) generation, (2) evaluation, or (3) manual operation")
    # openai variables
    parser.add_argument("--metadata_dir",               type=str,   default="metadata",                             help="directory where metadata such as keys and cost are stored")
    parser.add_argument("--openai_api_key",             type=str,   default="not_a_key",                            help="openai api key, if inputted, system will use this over the api key in the file")
    parser.add_argument("--key_file",                   type=str,   default="key_todsafety",                        help="<filename>.txt with the api key that we want to use")
    parser.add_argument("--gpt_model",                  type=str,   default="gpt-4o-mini",                          help="GPT model of the generation model: gpt-4o gpt-4o-mini")
    # generation variables
    parser.add_argument("--domain_str",                 type=str,   default="bank",                                 help="default domain to ru nthe generation on")
    parser.add_argument("--default_dependency_option",  type=str,   default="full", choices=["required", "full"],   help="default dependencies of the other actions besides the target action")
    # generation variables
    parser.add_argument("--manual_option",              type=int,   default=1,                                      help="manual operation options, (1) for functional testing, and etcetera")
    # directories
    parser.add_argument("--cost_file",                  type=str,   default="cost.txt",                             help="filename of a record of current costs")
    parser.add_argument("--domains_dir",                type=str,   default=os.path.join("env", "domains"),         help="directory where the domains are located")
    # output controllers
    parser.add_argument("--indent_amount",              type=int,   default=2,                                      help="controls the indent amount when writing to a file")
    parser.add_argument("--data_dir",                   type=str,   default="data",                                 help="where the written data will be stored")
    
    # calling the operation
    args = parser.parse_args()
    if args.openai_api_key =[REDACTED] "not_a_key":
        keydir_path = os.path.join(args.metadata_dir, "keys")
        args.openai_api_key = [REDACTED]
    all_run_usage = manual_operation(args)
    # cost calculation
    total_usage = {"prompt_tokens": 0, "completion_tokens": 0}
    for run_usage in all_run_usage:
        total_usage["prompt_tokens"] += run_usage.prompt_tokens
        total_usage["completion_tokens"] += run_usage.completion_tokens
    cost_dict = OPENAI_MODEL_COST_PER_1M_TOKENS
    total_cost = (cost_dict[args.gpt_model] * total_usage["prompt_tokens"]\
        + cost_dict[args.gpt_model+"-completion"] * total_usage["completion_tokens"]) / 10**6
    print(f"Total Tokens: {total_usage['prompt_tokens'] + total_usage['completion_tokens']}")
    print(f"Prompt Tokens: {total_usage['prompt_tokens']}")
    print(f"Completion Tokens: {total_usage['completion_tokens']}")
    print(f"Total Cost (USD): ${round(total_cost, 5)}")
    if round(total_cost, 5) > 0: write_data_file(args.metadata_dir, args.cost_file, str(round(total_cost, 5))+'\n', 'a')
    cost_list_str = read_data_file(args.metadata_dir, args.cost_file) if os.path.exists(os.path.join(args.metadata_dir, args.cost_file)) else "0\n"
    all_exper_cost = sum(list(map(float, cost_list_str[:-1].split('\n'))))
    print(f"All Exper. Cost (USD): ${round(all_exper_cost, 5)}")