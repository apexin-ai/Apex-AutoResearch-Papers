"""
running the task generation
"""


from env.file_read_write import read_keys, write_data_file, read_data_file, load_env_vars
from env.variables import OPENAI_MODEL_COST_PER_1M_TOKENS
from env.generation import task_generation

import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run task generation")
    # openai variables
    parser.add_argument("--metadata_dir",               type=str,   default="metadata",                             help="directory where metadata such as keys and cost are stored")
    parser.add_argument("--openai_api_key",             type=str,   default="not_a_key",                            help="openai api key, if inputted, system will use this over the api key in the file")
    parser.add_argument("--gpt_model",                  type=str,   default="gpt-4.1-mini",                          help="GPT model of the generation model: gpt-4o gpt-4o-mini")
    parser.add_argument("--temperature",                type=float, default=0.4,                                    help="temperature of GPT, higher = more random")
    parser.add_argument("--top_p",                      type=float, default=1.0,                                    help="limiting the vocabulary of the LLM, high = more random")
    parser.add_argument("--max_tokens",                 type=int,   default=2000,                                   help="maximum number of xompletion tokens for any one generation")
    # generation variables
    parser.add_argument("--domain_str",                 type=str,   default="bank",                                 help="default domain to ru nthe generation on")
    parser.add_argument("--default_dependency_option",  type=str,   default="full", choices=["required", "full"],   help="default dependencies of the other actions besides the target action")
    parser.add_argument("--generation_limit",           type=int,   default=4,                                      help="number of times the AI should regenerate before raising an error")
    parser.add_argument("--autogen_manfix",             action="store_true",                                        help="during the task generation phase, enable the option to automatically generate with manual fixing")
    parser.add_argument("--gen_fulldeptasks",           action="store_true",                                        help="during the task generation phase, filter out all tasks without full depenedneciedependencies")
    parser.add_argument("--debug_mode",                 action="store_true",                                        help="enables debug mode for task generation, printing the intermediate steps of generation")
    parser.add_argument("--testing_mode",               action="store_true",                                        help="enables testing mode for task generation, testing case by case, printing everything")
    parser.add_argument("--testing_mode_last_task",     action="store_true",                                        help="only the tasks with the last correct dep are tested")
    parser.add_argument("--testing_mode_user_goal",     type=str,   default="transfer_funds",                       help="which method to test during testing mode")
    # diagnostics
    parser.add_argument("--print_pipeline_disable",     action="store_false",                                       help="determines if the pipeline progress steps are printed")
    parser.add_argument("--print_test_domain",          action="store_true",                                        help="enables print statements from the domain-specific tests")
    parser.add_argument("--test_domain",                action="store_true",                                        help="enables the ai assistant tests for each domain (may take some time)")
    # directories
    parser.add_argument("--cost_file",                  type=str,   default="cost.txt",                             help="filename of a record of current costs")
    parser.add_argument("--domains_dir",                type=str,   default=os.path.join("env", "domains"),         help="directory where the domains are located")
    # output controllers
    parser.add_argument("--write_output_disable",       action="store_false",                                       help="determines if the experiment will print to an output file or not")
    parser.add_argument("--data_dir",                   type=str,   default="data",                                 help="where the written data will be stored")
    parser.add_argument("--indent_amount",              type=int,   default=2,                                      help="controls the indent amount when writing to a file")

    # calling the generation
    args = parser.parse_args()
    if args.openai_api_key =[REDACTED] "not_a_key":
        # First try to load from swarm/.env file
        env_file_path = os.path.join("swarm", ".env")
        env_vars = load_env_vars(env_file_path)
        if "OPENAI_API_KEY" in env_vars:
            args.openai_api_key = [REDACTED]"OPENAI_API_KEY"]
            print("Using OpenAI API key from swarm/.env file")
        else:
            raise ValueError("No OpenAI API key found!")
    all_run_usage = task_generation(args)
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