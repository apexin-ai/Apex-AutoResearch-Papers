import json
import random
import re
from collections import defaultdict


def extract_tool_inventory(stac_data: list[dict]) -> dict:
    """
    Extract tool definitions from STAC data: tool_name -> {params, output_patterns, input_types, output_types}.
    """
    inventory = {}

    for trace in stac_data:
        history = trace.get("interaction_history", [])
        tool_outputs = {}

        for msg in history:
            if msg.get("role") == "assistant" and "tool_calls" in msg:
                for tc in msg["tool_calls"]:
                    func = tc["function"]
                    name = func["name"]
                    args_str = func.get("arguments", "{}")
                    if isinstance(args_str, str):
                        try:
                            args = json.loads(args_str)
                        except json.JSONDecodeError:
                            args = {}
                    else:
                        args = args_str

                    if name not in inventory:
                        inventory[name] = {
                            "params": set(),
                            "param_examples": defaultdict(list),
                            "output_samples": [],
                            "output_types": set(),
                            "input_types": set(),
                        }

                    for k, v in args.items():
                        inventory[name]["params"].add(k)
                        if len(inventory[name]["param_examples"][k]) < 5:
                            inventory[name]["param_examples"][k].append(v)
                        inventory[name]["input_types"].add(_infer_type(v))

                    tool_outputs[tc.get("id", "")] = (name, tc)

            elif msg.get("role") == "tool":
                tool_call_id = msg.get("tool_call_id", "")
                content = msg.get("content", "")
                tool_name = msg.get("name", "")

                if tool_name and tool_name in inventory:
                    if len(inventory[tool_name]["output_samples"]) < 5:
                        inventory[tool_name]["output_samples"].append(content[:500])
                    inventory[tool_name]["output_types"].add(_infer_output_type(content))

    for name in inventory:
        inventory[name]["params"] = list(inventory[name]["params"])
        inventory[name]["param_examples"] = dict(inventory[name]["param_examples"])
        inventory[name]["output_types"] = list(inventory[name]["output_types"])
        inventory[name]["input_types"] = list(inventory[name]["input_types"])

    return inventory


def _infer_type(value) -> str:
    if isinstance(value, str):
        if "@" in value:
            return "email"
        if re.match(r'^\d+$', value):
            return "numeric_string"
        if re.match(r'^https?://', value):
            return "url"
        return "string"
    elif isinstance(value, (int, float)):
        return "number"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, list):
        return "list"
    elif isinstance(value, dict):
        return "object"
    return "string"


def _infer_output_type(content: str) -> str:
    if not content:
        return "empty"
    try:
        parsed = json.loads(content)
        if isinstance(parsed, list):
            return "list"
        elif isinstance(parsed, dict):
            return "object"
        return "primitive"
    except (json.JSONDecodeError, TypeError):
        if re.search(r'[{}\[\]]', content):
            return "structured_text"
        return "text"


def build_compatibility_graph(inventory: dict) -> dict[str, list[str]]:
    """
    Build tool compatibility: tool_A -> list of tools whose input types
    overlap with tool_A's output types.
    """
    compat = defaultdict(list)

    for tool_a, info_a in inventory.items():
        out_types_a = set(info_a["output_types"])
        for tool_b, info_b in inventory.items():
            in_types_b = set(info_b["input_types"])
            if out_types_a & in_types_b:
                compat[tool_a].append(tool_b)
            elif out_types_a and in_types_b:
                if "string" in in_types_b and ("text" in out_types_a or "structured_text" in out_types_a):
                    compat[tool_a].append(tool_b)

    # Ensure every tool has at least some successors (fallback to all tools)
    all_tools = list(inventory.keys())
    for tool in all_tools:
        if not compat[tool]:
            compat[tool] = [t for t in all_tools if t != tool]

    return dict(compat)


def _generate_param_value(param_name: str, examples: list, rng: random.Random) -> str:
    if examples:
        return str(rng.choice(examples))
    if "name" in param_name.lower():
        names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
        return rng.choice(names)
    if "email" in param_name.lower():
        return f"user{rng.randint(1,100)}@example.com"
    if "id" in param_name.lower():
        return str(rng.randint(1000, 9999))
    if "query" in param_name.lower() or "search" in param_name.lower():
        queries = ["meeting notes", "project update", "schedule", "report", "invoice"]
        return rng.choice(queries)
    return f"value_{rng.randint(1, 100)}"


def _generate_tool_output(tool_name: str, inventory: dict, rng: random.Random) -> str:
    info = inventory.get(tool_name, {})
    samples = info.get("output_samples", [])
    if samples:
        return rng.choice(samples)
    return json.dumps({"status": "success", "result": f"{tool_name}_output_{rng.randint(1,100)}"})


DEPTH_WEIGHTS = {2: 0.42, 3: 0.43, 4: 0.08, 5: 0.04, 6: 0.02, 7: 0.005, 8: 0.005}


def _sample_depth(rng: random.Random) -> int:
    """Sample chain depth matching STAC attack chain distribution (~85% 2-3 steps)."""
    depths = list(DEPTH_WEIGHTS.keys())
    weights = list(DEPTH_WEIGHTS.values())
    return rng.choices(depths, weights=weights, k=1)[0]


def generate_single_trace(
    inventory: dict,
    compat_graph: dict,
    rng: random.Random,
    branch_prob: float = 0.15,
) -> dict:
    """Generate a single benign trace with valid data-flow structure."""
    all_tools = list(inventory.keys())
    if not all_tools:
        return {"interaction_history": []}

    depth = min(_sample_depth(rng), len(all_tools))
    current_tool = rng.choice(all_tools)

    interaction_history = []
    # Initial user message
    interaction_history.append({
        "role": "user",
        "content": f"Please help me with a task involving {current_tool.replace('_', ' ')}."
    })

    tool_call_id_counter = 0
    chain = []

    for step in range(depth):
        tool_name = current_tool
        info = inventory.get(tool_name, {"params": [], "param_examples": {}})

        # Generate arguments
        args = {}
        for param in info["params"]:
            examples = info.get("param_examples", {}).get(param, [])
            args[param] = _generate_param_value(param, examples, rng)

        tool_call_id = f"call_{tool_call_id_counter}"
        tool_call_id_counter += 1

        # Assistant message with tool call
        assistant_msg = {
            "role": "assistant",
            "tool_calls": [{
                "id": tool_call_id,
                "function": {
                    "name": tool_name,
                    "arguments": json.dumps(args),
                }
            }]
        }

        # Branching: add a second tool call with some probability
        if rng.random() < branch_prob and step < depth - 1:
            successors = compat_graph.get(tool_name, all_tools)
            if successors:
                branch_tool = rng.choice(successors)
                branch_info = inventory.get(branch_tool, {"params": [], "param_examples": {}})
                branch_args = {}
                for param in branch_info["params"]:
                    examples = branch_info.get("param_examples", {}).get(param, [])
                    branch_args[param] = _generate_param_value(param, examples, rng)

                branch_id = f"call_{tool_call_id_counter}"
                tool_call_id_counter += 1
                assistant_msg["tool_calls"].append({
                    "id": branch_id,
                    "function": {
                        "name": branch_tool,
                        "arguments": json.dumps(branch_args),
                    }
                })

        interaction_history.append(assistant_msg)

        # Tool response(s)
        for tc in assistant_msg["tool_calls"]:
            output = _generate_tool_output(tc["function"]["name"], inventory, rng)
            interaction_history.append({
                "role": "tool",
                "tool_call_id": tc["id"],
                "name": tc["function"]["name"],
                "content": output,
            })

        chain.append(tool_name)

        # Pick next tool from compatibility graph
        successors = compat_graph.get(tool_name, [])
        if successors:
            current_tool = rng.choice(successors)
        else:
            current_tool = rng.choice(all_tools)

    trace = {
        "id": None,
        "generation_config": {"failure_mode": "benign", "environment": "synthetic"},
        "attack_plan": {"verified_tool_chain": []},
        "interaction_history": interaction_history,
    }
    return trace


def generate_benign_traces(
    stac_data: list[dict],
    n_traces: int = 500,
    seed: int = 42,
) -> list[dict]:
    """
    Generate synthetic benign traces based on tool inventory extracted from STAC data.

    Args:
        stac_data: list of STAC attack traces
        n_traces: number of benign traces to generate
        seed: random seed

    Returns:
        list of benign traces in STAC-compatible format
    """
    rng = random.Random(seed)
    inventory = extract_tool_inventory(stac_data)

    if not inventory:
        return []

    compat_graph = build_compatibility_graph(inventory)

    traces = []
    for i in range(n_traces):
        trace = generate_single_trace(inventory, compat_graph, rng)
        trace["id"] = i
        traces.append(trace)

    return traces
