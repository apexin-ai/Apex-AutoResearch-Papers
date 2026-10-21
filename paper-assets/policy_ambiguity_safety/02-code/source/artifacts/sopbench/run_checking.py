import json
import pprint
from colorama import init, Fore, Back, Style
import os
import argparse
from env.helpers import bfsconvert_ifg_to_tree
from env.generation import dfsgather_dep_tree_vis

# Initialize colorama
init()

def clear_screen():
    # Clear screen command based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def display_dependency_graph(dirgraph, option=2):
    print(f"\n{Back.RED}{Fore.WHITE}=== Directed Action Graph ==={Style.RESET_ALL}")
    # print(json.dumps(dirgraph, indent=4))
    
    # The first option to display the dependency graph is to convert it to a tree and display it
    if option == 1:
        tree = bfsconvert_ifg_to_tree(dirgraph)
        print(dfsgather_dep_tree_vis(tree))
        return 

    def format_node(node):
        """Format a node for display with appropriate colors"""
        if isinstance(node, str):
            return f"{node.upper()}"
        return f"{node[0]} (args: {node[1]})"
    
    def get_dependencies(node_idx):
        """Get dependencies for a node"""
        if isinstance(dirgraph['connections'], list):
            return [dep_idx for from_idx, dep_idx in dirgraph['connections'] if from_idx == node_idx]
        else:
            return dirgraph['connections'].get(str(node_idx), [])
    
    def print_tree(node_idx, visited=None, level=0):
        """Print the dependency tree in a visual format similar to dfsget_depverb_tree"""
        if visited is None:
            visited = set()
            
        if node_idx in visited:
            return
            
        visited.add(node_idx)
        node = dirgraph['nodes'][node_idx]
        
        # Create the branch visualization
        prefix = "│  " * (level - 1) + "└─ " if level > 0 else ""
        
        # Format and print the current node
        node_str = format_node(node)
        print(f"{Fore.CYAN}{prefix}{node_str}{Style.RESET_ALL}")
        
        # Process dependencies
        dependencies = get_dependencies(node_idx)
        for dep_idx in dependencies:
            print_tree(dep_idx, visited, level + 1)
    
    # Find root nodes (nodes that have no dependents)
    all_dependencies = set()
    if isinstance(dirgraph['connections'], list):
        all_dependencies = {dep_idx for _, dep_idx in dirgraph['connections']}
        root_nodes = {from_idx for from_idx, _ in dirgraph['connections']} - all_dependencies
    else:
        for deps in dirgraph['connections'].values():
            all_dependencies.update(deps)
        root_nodes = {int(k) for k in dirgraph['connections'].keys()} - all_dependencies
    
    # If no root nodes found (might be an empty or cyclic graph), print all nodes
    if not root_nodes:
        root_nodes = {0} if dirgraph['nodes'] else set()
    
    # Print tree starting from each root node
    for root_idx in sorted(root_nodes):
        print_tree(root_idx)

def display_evaluation(evaluation):
    print(f"\n{Back.YELLOW}{Fore.BLACK}=== EVALUATION RESULTS ==={Style.RESET_ALL}")
    
    # Display each evaluation metric with color coding
    metrics = [
        ("User Goal", evaluation['user_goal']),
        ("Should Succeed", evaluation['action_should_succeed']),
        ("Number of Messages", evaluation['num_messages']),
        ("Number of Function Calls", evaluation['num_function_calls']),
        ("No Tool Call Error", evaluation['no_tool_call_error']),
        ("Constraint Not Violated", evaluation['constraint_not_violated']),
        ("Database Match", evaluation['database_match']),
        ("Action Called Successfully", evaluation['action_successfully_called']),
        ("Action Called Correctly", evaluation['action_called_correctly']),
        ("Dirgraph Satisfied", evaluation['dirgraph_satisfied']),
        ("Overall Success", evaluation['success'])
    ]
    
    for label, value in metrics:
        if isinstance(value, bool):
            color = Fore.GREEN if value else Fore.RED
            print(f"{Fore.CYAN}{label}:{Style.RESET_ALL} {color}{value}{Style.RESET_ALL}")
        elif isinstance(value, (int, float)):
            print(f"{Fore.CYAN}{label}:{Style.RESET_ALL} {Fore.YELLOW}{value}{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}{label}:{Style.RESET_ALL} {value}")

def display_task_info(task):
    print(f"\n{Back.BLUE}{Fore.WHITE}=== TASK INFORMATION ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}User Goal (target action):{Style.RESET_ALL} {task['user_goal']}")
    
    # Display user known information
    print(f"\n{Fore.CYAN}User Provided Information:{Style.RESET_ALL}")
    for key, value in task['user_known'].items():
        print(f"  {Fore.YELLOW}{key}:{Style.RESET_ALL} {value}")
    
    print(f"\n{Fore.CYAN}Should Succeed:{Style.RESET_ALL} {Fore.GREEN if bool(task['action_should_succeed']) else Fore.RED}{bool(task['action_should_succeed'])}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}User Instruction:{Style.RESET_ALL} {task['user_instruction']}")
    print(f"\n{Fore.YELLOW}User Prompt:{Style.RESET_ALL}")
    print(task['user_prompt'])
    print(f"\n{Fore.YELLOW}Assistant Prompt:{Style.RESET_ALL}")
    print(task['assistant_prompt'])
    
    # Display dependency graph
    # print(json.dumps(task['dependency'], indent=4))
    display_dependency_graph(task['directed_action_graph'])




def display_interaction(interaction):
    print(f"\n{Back.GREEN}{Fore.WHITE}=== INTERACTION TURNS ==={Style.RESET_ALL}")
    
    i = 0
    turn_idx = 0
    while i < len(interaction):
        turn = interaction[i]
        print(f"\n{Back.WHITE}{Fore.BLACK}--- Turn {turn_idx+1} ---{Style.RESET_ALL}")
        
        # Display sender if present
        if 'sender' in turn:
            sender_color = Fore.BLUE if turn['sender'] == 'bank assistant' else Fore.GREEN
            print(f"\n{sender_color}Sender:{Style.RESET_ALL} {turn['sender']}")
        
        # Display assistant's message
        if 'content' in turn and turn['content']:
            print(f"\n{Fore.YELLOW}Message:{Style.RESET_ALL} {turn['content']}")
        
        # display thinking if present
        if 'thinking' in turn:
            print(f"\n{Fore.YELLOW}Thinking:{Style.RESET_ALL} {turn['thinking']}")
        
        # Display tool calls and their immediate responses
        if 'tool_calls' in turn:
            if not turn['tool_calls']:
                print(f"\n{Fore.MAGENTA}Tool Call:{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Function:{Style.RESET_ALL} None")
                print(f"{Fore.CYAN}Arguments:{Style.RESET_ALL} None")
            else:
                for tool_call in turn['tool_calls']:
                    print(f"\n{Fore.MAGENTA}Tool Call:{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}Function:{Style.RESET_ALL} {tool_call['function']['name']}")
                    print(f"{Fore.CYAN}Arguments:{Style.RESET_ALL} {tool_call['function']['arguments']}")
                
                # Look ahead for the response
                response = None
                if i + 1 < len(interaction):
                    next_turn = interaction[i + 1]
                    if 'tool_call_id' in next_turn and next_turn['tool_call_id'] == tool_call['id']:
                        response = next_turn['content']
                        i += 1  # Skip the response turn since we've handled it here
                
                # Always display response field, even if None
                if response is not None:
                    result_color = Fore.GREEN if response == "True" else Fore.RED
                    print(f"{Fore.CYAN}Response:{Style.RESET_ALL} {result_color}{response}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.CYAN}Response:{Style.RESET_ALL} {Fore.YELLOW}None{Style.RESET_ALL}")
        
        i += 1
        turn_idx += 1
        
def main():
    parser = argparse.ArgumentParser(description='Run checking tool for evaluating interactions')
    
    # Required arguments for output file construction
    parser.add_argument("--output_dir", type=str, default="./output",
                       help="Output directory")
    parser.add_argument("--domain", type=str, required=True,
                       choices=["bank", "online_market", "dmv", "healthcare", "library", "hotel", "university"], 
                       help="Domain name")
    parser.add_argument("--user_model", type=str, default=None,
                       help="Model to use for the user agent")
    parser.add_argument("--assistant_model", type=str, required=True,
                       help="Model to use for the assistant agent")
    parser.add_argument("--tool_call_mode", type=str, default="fc",
                       choices=["fc", "react", "act-only", "react-v"],
                       help="Tool call mode for the assistant model")
    parser.add_argument("--default_constraint_option", type=str, default="full",
                       choices=["full", "required"], 
                       help="Default dependency to use")
    parser.add_argument("--constraint_descr_format", type=str, default="structured",
                       choices=["old", "structured"], 
                       help="Constraint dependency description format")
    parser.add_argument("--tool_list", type=str, default="full",
                       choices=["full", "oracle"],
                       help="Tool list to use for the simulation")
    parser.add_argument("--shuffle_func", action="store_true",
                       help="Whether to shuffle assistant functions")

    args = parser.parse_args()
    output_dir = f"{args.output_dir}/{args.domain}"
    os.makedirs(output_dir, exist_ok=True)
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
    
    data = load_json_file(output_file)
    for i, scenario in enumerate(data, 1):
        clear_screen()
        print("Loading data from", output_file + '\n\n')
        print(f"\n{Back.MAGENTA}{Fore.WHITE}{'='*20} SCENARIO {i}/{len(data)} {'='*20}{Style.RESET_ALL}")
        
        # Display database
        print(f"\n{Back.YELLOW}{Fore.BLACK}=== DATABASE ==={Style.RESET_ALL}")
        print(json.dumps(scenario['task']['initial_database'], indent=4))
        
        # Display task information
        scenario['task']['assistant_prompt'] = scenario['interactions'][0]['prompt']
        display_task_info(scenario['task'])
        
        # Display each interaction
        for interaction_group in scenario['interactions']:
            display_interaction(interaction_group['interaction'])
            
        # Display evaluation results
        if "evaluations" in scenario:
            for evaluation in scenario['evaluations']:
                display_evaluation(evaluation)
        
        print(f"\n{Fore.YELLOW}Press Enter to continue to next scenario...{Style.RESET_ALL}")
        input()

        
if __name__ == "__main__":
    main() 