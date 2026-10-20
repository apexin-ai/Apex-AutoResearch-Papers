import os
import copy
import argparse
import json
import re
from tqdm import tqdm
from env.variables import domain_keys
from env.helpers import get_title_str, get_dict_str, get_dict_json_str
from env.evaluator import AVG_PARAMS, evaluator_function_directed_graph, interaction_statistics, domain_statistics, combine_list_numerical_dicts


"""Evaluation helper functions"""

# Define sort key function for constraint groups
def constraint_group_sort_key(item):
    key = item[0]
    if key == "6+": return 6  # Make "6+" sort after 5
    return int(key) # Convert other keys to integers

def try_eval(x):
    try: return eval(x)
    except: return x

def save_results(output_file, results, verbose=False):
    """
    Save results to a JSON file.
    Args:
        output_file (str): Path to the output file
        results (list): List of task simulation results to save
        verbose (bool): Whether to print saving status
    """
    try:
        # Add debug print before saving
        has_evaluations = False
        if results and len(results) > 0:
            has_evaluations = 'evaluations' in results[0]
        print(f"Saving {len(results)} results. First result has evaluations: {has_evaluations}")
        
        with open(output_file, 'w', encoding='utf-8') as f: json.dump(results, f, indent=4)
        if verbose: print(f"Results saved successfully to {output_file}")
    except Exception as e: print(f"Error saving results to {output_file}: {str(e)}")

def load_existing_results(output_file):
    """
    Load existing results from a JSON file or return empty list if file doesn't exist.
    Args:
        output_file (str): Path to the output file
    Returns:
        list: List of task simulation results
    """
    try:
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as f:
                results = json.load(f)
                print(f"Loaded {len(results)} results from {output_file}")  # Add debug print
                return results
        else: print(f"File {output_file} does not exist!")
    except Exception as e: print(f"Error loading results from {output_file}: {str(e)}")
    return []

def get_domain_results_str(domain:str, domain_stats:dict, indent_amount:int=2,
    separate_out_keys:list[str]=["distr_user_goal", "goal_statistics", "group_statistics", "error_statistics", "per_run_pass_rates"])->str:
    """
    Returns the string of a nicely formatted domain statistics results
    Args:
        domain (str): domain of the current statistics, could be all
        domain_stats (dict): statistics to show
        indent_amount (int): amount of indentation if printing in a json format
        separate_out_keys (list[str]): list of keys that we want to separately print in separate tables
    Returns:
        list: List of task simulation results
    """
    domain_results_str = get_title_str(f"Overall domain statistics for {domain}")\
        +f"\n{get_dict_str(domain_stats, separate_out_keys)}"
    for key in separate_out_keys:
        if key in domain_stats:
            title_word_list = [w[0].upper() + w[1:] for w in key.split('_')]
            title_str = ' '.join(title_word_list)
            
            # Add special formatting for per-run pass rates
            if key == "per_run_pass_rates":
                pass_rates_str = json.dumps(domain_stats[key], indent=indent_amount)
                mean_rate = domain_stats.get("mean_pass_rate", "N/A")
                std_rate = domain_stats.get("std_pass_rate", "N/A")
                domain_results_str += f"\n\n{get_title_str(title_str)}"\
                    + f"\n{pass_rates_str}"\
                    + f"\nMean Pass Rate: {mean_rate:.4f}"\
                    + f"\nStandard Deviation: {std_rate:.4f}"
            # Add special formatting for goal statistics to show success rate per user goal
            elif key == "goal_statistics":
                domain_results_str += f"\n\n{get_title_str(title_str)}"\
                    + f"\n{get_dict_json_str(domain_stats[key], indent_amount=indent_amount)}"
                # Add success rate per user goal
                domain_results_str += f"\n\n{get_title_str('Success Rate Per User Goal')}"
                success_rates = {}
                for goal, stats in domain_stats[key].items():
                    success_rates[goal] = stats.get("success_rate", 0)
                domain_results_str += f"\n{json.dumps(success_rates, indent=indent_amount)}"
            else:
                domain_results_str += f"\n\n{get_title_str(title_str)}"\
                    +f"\n{get_dict_json_str(domain_stats[key], indent_amount=indent_amount)}"
    return domain_results_str


"""Parse the arguments and run the evaluation"""

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    # Model settings
    parser.add_argument("--user_model", type=str, default=None, help="Model to use for the user agent")
    parser.add_argument("--assistant_model", type=str, default="gpt-4o-mini", help="Model to use for the assistant agent")
    # Evaluation settings
    parser.add_argument("--tool_call_mode", type=str, default="fc", choices=["fc", "act-only", "react", "react-v"], help="Tool call mode for the assistant model")
    parser.add_argument("--tool_list", type=str, default="oracle", choices=["full", "oracle"], help="Tool list to use for the simulation, only use the tools that have been evaluated or full tool list")
    parser.add_argument("--shuffle_func", action="store_true", help="Whether to shuffle assistant functions")
    parser.add_argument("--default_constraint_option", type=str, default="full", choices=["full", "required"], help="Default dependency to use for the other unevaluated actions")
    parser.add_argument("--constraint_descr_format", type=str, default="structured", choices=["old", "structured"], help="Constraint dependency description format")
    parser.add_argument("--num_run_per_interaction", type=int, default=1, help="Number of interactions per task")
    parser.add_argument("--verbose", action="store_true", help="Whether to print verbose output")
    # Data settings
    parser.add_argument("--output_dir", type=str, default="./output_v2", help="Output directory")
    parser.add_argument("--domain", type=str, default="bank", choices=["bank", "online_market", "dmv", "healthcare", "library", "hotel", "university", "all"], help="Domain name")
    parser.add_argument("--indent_amount", type=int, default=2, help="controls the indent amount when writing to a file")
    args = parser.parse_args()
    return args

def main():
    """Main function to run the simulation."""
    args = parse_args()
    # Define domains to process
    domains_to_process = [ele for ele in domain_keys if "_strict" not in ele] if args.domain == "all" else [args.domain]
    # Initialize combined results for all domains
    domain_stats = None
    ex_task_eval_res = None
    ex_task_stat_res = None
    combined_results = {}
    goal_distribution = {}
    for current_domain in domains_to_process:
        # Setup output path
        output_dir = f"{args.output_dir}/{current_domain}"
        new_output_dir = f"{args.output_dir}/{current_domain}"
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(new_output_dir, exist_ok=True)
        output_file = os.path.join(
            output_dir,
            (f"usr_{args.user_model.replace('/', '_')}-" if args.user_model else "") + \
            f"ast_{args.assistant_model.replace('/', '_')}-" + \
            f"mode_{args.tool_call_mode}-" + \
            f"dep_{args.default_constraint_option}-" + \
            f"fmt_{args.constraint_descr_format}-" + \
            f"tool_{args.tool_list}-" + \
            f"shuffle_{args.shuffle_func}.json"
        )
        new_output_file = os.path.join(
            new_output_dir,
            (f"usr_{args.user_model.replace('/', '_')}-" if args.user_model else "") + \
            f"ast_{args.assistant_model.replace('/', '_')}-" + \
            f"mode_{args.tool_call_mode}-" + \
            f"dep_{args.default_constraint_option}-" + \
            f"fmt_{args.constraint_descr_format}-" + \
            f"tool_{args.tool_list}-" + \
            f"shuffle_{args.shuffle_func}.json"
        )
        # Goal statistics (evaluation index grouped by user goals)
        usergoal_evalind = {}
        # Group statistics (evaluation index grouped by number of constraints)
        numconstr_evalind = {}
        # Error statistics
        error_statistics = {
            "total_evaluations": 0,
            "total_failures": 0,           
            "error_causes": {
                "tool_call_errors": 0,             # Changed from no_tool_call_error
                "constraint_violations": 0,        # Changed from constraint_not_violated
                "database_mismatches": 0,          # Changed from database_match
                "dirgraph_violations": 0,          # Changed from dirgraph_satisfied
                "incorrect_action_calls": 0        # Changed from action_called_correctly
            }
        }
        # Create a new list to store updated simulations
        updated_task_simulations = []
        # Load existing results
        task_simulations = load_existing_results(output_file)
        if not task_simulations: continue
        all_stats = []
        for idx, task_simulation in tqdm(enumerate(task_simulations), desc="Evaluating task simulations"):
            user_goal = task_simulation["task"]["user_goal"]
            evaluations = []
            # Limit interactions to top num_run_per_interaction
            limited_interactions = task_simulation["interactions"][:args.num_run_per_interaction]
            # run and record evaluations
            for interaction_log in limited_interactions:
                results = {"final_database": interaction_log["database"]}
                interaction = interaction_log["interaction"]
                # collect the function call and response
                func_calls = []
                for i in range(len(interaction)-1):
                    if interaction[i].get("tool_calls", []):
                        # Clean N/A function call
                        for tool_call in interaction[i]["tool_calls"]:
                            if tool_call["function"]["name"].lower() in ["n/a", "na", "none", "null"]:
                                interaction[i]["tool_calls"].remove(tool_call)
                        if len(interaction[i]["tool_calls"]) > 0:
                            func_calls.append({
                                "tool_name": interaction[i+1]["tool_name"],
                                "arguments": try_eval(interaction[i]["tool_calls"][0]["function"]["arguments"]),
                                "content": try_eval(interaction[i+1]["content"])
                            })
                # Use directed graph evaluator instead of gorilla
                evaluation_result = evaluator_function_directed_graph(
                    domain_str=task_simulation["domain"],
                    task=task_simulation["task"],
                    log_msg_fcall=interaction,
                    func_calls=func_calls,
                    results=results,
                    default_constraint_option=args.default_constraint_option)
                evaluations.append(evaluation_result)
                if args.verbose: print(json.dumps(evaluation_result, indent=4))
                if not ex_task_eval_res or len(ex_task_eval_res) < len(evaluation_result): ex_task_eval_res = evaluation_result
            # Calculate the simulation statistics
            stats = interaction_statistics(evaluations, AVG_PARAMS, args.num_run_per_interaction)
            all_stats.append(stats)
            # Group by user goal
            if user_goal not in usergoal_evalind: usergoal_evalind[user_goal] = []
            usergoal_evalind[user_goal].append(idx)
            # Group by number of constraints
            constraint_count = evaluation_result["num_constraints"]
            if constraint_count >= 6: constraint_count = "6+" # Group all counts >= 6 into "6+"
            elif constraint_count <= 1: constraint_count = 1 # Group 0 and 1 together as "1"
            if constraint_count not in numconstr_evalind: numconstr_evalind[constraint_count] = []
            numconstr_evalind[constraint_count].append(idx)
            # Update the error statistics
            for evaluation_result in evaluations:
                error_statistics["total_evaluations"] += 1
                if evaluation_result.get("success", False): continue # Only track errors for failed cases
                error_statistics["total_failures"] += 1
                # Check all status indicators for each failed evaluation
                error_statistics["error_causes"]["tool_call_errors"] += 1-int(evaluation_result["no_tool_call_error"])
                error_statistics["error_causes"]["constraint_violations"] += 1-int(evaluation_result["constraint_not_violated"])
                error_statistics["error_causes"]["database_mismatches"] += 1-int(evaluation_result["database_match"])
                error_statistics["error_causes"]["dirgraph_violations"] += 1-int(evaluation_result["dirgraph_satisfied"])
                error_statistics["error_causes"]["incorrect_action_calls"] += 1-int(evaluation_result["action_called_correctly"])
            # Create a new task simulation dict with the evaluations
            updated_simulation = copy.deepcopy(task_simulation)
            updated_simulation["evaluations"] = evaluations
            updated_simulation["statistics"] = stats
            # Trim interactions to only include the top num_run_per_interaction
            updated_simulation["interactions"] = limited_interactions
            updated_task_simulations.append(updated_simulation)
        for stat in all_stats:
            if not ex_task_stat_res or len(ex_task_stat_res) < len(stat): ex_task_stat_res = stat
        # Goal statistics
        goal_statistics = {key: domain_statistics([all_stats[ind] for ind in usergoal_evalind[key]], ex_task_eval_res, ex_task_stat_res)
            for key in usergoal_evalind}
        # Group statistics
        group_statistics = {key: domain_statistics([all_stats[ind] for ind in numconstr_evalind[key]], ex_task_eval_res, ex_task_stat_res)
            for key in numconstr_evalind}
        # Run domain statistics
        domain_stats = domain_statistics(all_stats, ex_task_eval_res, ex_task_stat_res)
        # innate information
        domain_stats["user_model"] = args.user_model,
        domain_stats["assistant_model"] = args.assistant_model,
        domain_stats["domain"] = current_domain
        # collected statistics
        # domain_stats["goal_statistics"] = goal_statistics
        domain_stats["group_statistics"] = group_statistics
        domain_stats["error_statistics"] = error_statistics
        goal_distribution[current_domain] = goal_statistics
        # Save the updated task simulations
        save_results(new_output_file, updated_task_simulations, verbose=True)
        if args.domain == "all": combined_results[current_domain] = domain_stats
        
    # Aggregate results if needed
    if args.domain != "all": 
        # Use the same separate_out_keys as for "all" domains to ensure per_run_pass_rates is shown
        separate_out_keys = ["distr_user_goal", "group_statistics", "error_statistics", "per_run_pass_rates"]
        print(get_domain_results_str(args.domain, domain_stats, args.indent_amount, separate_out_keys))
    else:
        # combine the domain statistics
        combined_domain_stats = domain_statistics([combined_results[key] for key in combined_results], ex_task_eval_res, ex_task_stat_res)
        # combine the group statistics
        combined_group_statistics = cgs = {}
        for key in combined_results:
            for grou in combined_results[key]["group_statistics"]:
                dgs = combined_results[key]["group_statistics"][grou] # domain group statistics
                if grou not in cgs: cgs[grou] = copy.deepcopy(dgs)
                else: cgs[grou] = domain_statistics([cgs[grou], dgs], ex_task_eval_res, ex_task_stat_res)
        combined_domain_stats["group_statistics"] = combined_group_statistics
        # combine the error statistics
        combined_error_statistics = combine_list_numerical_dicts([combined_results[key]["error_statistics"] for key in combined_results])   
        combined_domain_stats["error_statistics"] = combined_error_statistics
        # print the result
        separate_out_keys = ["distr_user_goal", "group_statistics", "error_statistics", "per_run_pass_rates"]
        print(get_domain_results_str(args.domain, combined_domain_stats, args.indent_amount, separate_out_keys))

        
if __name__ == "__main__": main()