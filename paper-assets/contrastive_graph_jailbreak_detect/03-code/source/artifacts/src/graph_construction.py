import json
import torch
from torch_geometric.data import Data


def extract_tool_calls(trace: dict) -> list[dict]:
    """Extract tool call nodes from interaction_history."""
    nodes = []
    history = trace.get("interaction_history", [])

    tool_outputs = {}
    pending_tool_calls = []

    for msg in history:
        if msg["role"] == "assistant" and "tool_calls" in msg:
            for tc in msg["tool_calls"]:
                func = tc["function"]
                args_str = func.get("arguments", "{}")
                if isinstance(args_str, str):
                    try:
                        args = json.loads(args_str)
                    except json.JSONDecodeError:
                        args = {}
                else:
                    args = args_str
                node = {
                    "tool_name": func["name"],
                    "arguments": args,
                    "args_str": json.dumps(args) if isinstance(args, dict) else str(args),
                    "tool_call_id": tc.get("id", ""),
                    "output": "",
                    "step": len(nodes),
                }
                pending_tool_calls.append(node)
                nodes.append(node)

        elif msg["role"] == "tool":
            tool_call_id = msg.get("tool_call_id", "")
            content = msg.get("content", "")
            for node in pending_tool_calls:
                if node["tool_call_id"] == tool_call_id:
                    node["output"] = content
                    break
            tool_outputs[tool_call_id] = content
            pending_tool_calls = [n for n in pending_tool_calls if n["tool_call_id"] != tool_call_id]

    return nodes


def build_edges(nodes: list[dict]) -> list[tuple[int, int]]:
    """Build data-flow edges via string matching of outputs in subsequent arguments."""
    edges = set()
    has_dataflow = [False] * len(nodes)

    for i in range(len(nodes)):
        output_i = nodes[i]["output"]
        if not output_i or len(output_i) < 3:
            continue
        output_tokens = _extract_tokens(output_i)
        for j in range(i + 1, len(nodes)):
            args_j = nodes[j]["args_str"]
            if _has_overlap(output_tokens, args_j):
                edges.add((i, j))
                has_dataflow[i] = True
                has_dataflow[j] = True

    # Fallback: sequential edges for nodes without data-flow connections
    for i in range(len(nodes) - 1):
        if not has_dataflow[i] and not has_dataflow[i + 1]:
            edges.add((i, i + 1))
        elif not has_dataflow[i] and i + 1 < len(nodes):
            edges.add((i, i + 1))

    if not edges and len(nodes) > 1:
        for i in range(len(nodes) - 1):
            edges.add((i, i + 1))

    return list(edges)


def _extract_tokens(text: str, min_len: int = 4) -> set[str]:
    """Extract meaningful tokens from text for matching."""
    import re
    words = re.findall(r'[a-zA-Z0-9_@.\-]+', text)
    return {w for w in words if len(w) >= min_len}


def _has_overlap(tokens: set[str], target: str) -> bool:
    """Check if any token from source appears in target."""
    for token in tokens:
        if token in target:
            return True
    return False


def build_graph(trace: dict, label: int, tool_vocab: dict) -> Data:
    """
    Convert a single STAC trace into a PyG Data object.

    Args:
        trace: STAC trace dict
        label: 1=attack, 0=benign
        tool_vocab: mapping tool_name -> index

    Returns:
        PyG Data with x, edge_index, y, and failure_mode
    """
    nodes = extract_tool_calls(trace)

    if not nodes:
        x = torch.zeros((1, len(tool_vocab) + 3), dtype=torch.float)
        edge_index = torch.zeros((2, 0), dtype=torch.long)
        return Data(x=x, edge_index=edge_index, y=torch.tensor([label], dtype=torch.long),
                    failure_mode="unknown")

    vocab_size = len(tool_vocab)
    num_nodes = len(nodes)
    features = []

    for node in nodes:
        tool_idx = tool_vocab.get(node["tool_name"], vocab_size - 1)
        one_hot = [0.0] * vocab_size
        if tool_idx < vocab_size:
            one_hot[tool_idx] = 1.0

        param_count = float(len(node["arguments"]))
        output_len = float(len(node["output"])) / 1000.0
        step_pos = float(node["step"]) / max(num_nodes - 1, 1)

        feat = one_hot + [param_count, output_len, step_pos]
        features.append(feat)

    x = torch.tensor(features, dtype=torch.float)

    edges = build_edges(nodes)
    if edges:
        src = [e[0] for e in edges]
        dst = [e[1] for e in edges]
        edge_index = torch.tensor([src, dst], dtype=torch.long)
    else:
        edge_index = torch.zeros((2, 0), dtype=torch.long)

    failure_mode = trace.get("generation_config", {}).get("failure_mode", "unknown")

    return Data(
        x=x,
        edge_index=edge_index,
        y=torch.tensor([label], dtype=torch.long),
        failure_mode=failure_mode,
    )


def build_tool_vocab(traces: list[dict]) -> dict[str, int]:
    """Build tool vocabulary from a list of traces."""
    tools = set()
    for trace in traces:
        for msg in trace.get("interaction_history", []):
            if msg.get("role") == "assistant" and "tool_calls" in msg:
                for tc in msg["tool_calls"]:
                    tools.add(tc["function"]["name"])
    vocab = {name: i for i, name in enumerate(sorted(tools))}
    return vocab


def build_dataset(traces: list[dict], labels: list[int], tool_vocab: dict = None) -> list[Data]:
    """
    Convert a list of traces into PyG Data objects.

    Args:
        traces: list of STAC trace dicts
        labels: list of labels (1=attack, 0=benign)
        tool_vocab: optional pre-built vocab; if None, built from traces

    Returns:
        list of PyG Data objects
    """
    if tool_vocab is None:
        tool_vocab = build_tool_vocab(traces)

    dataset = []
    for trace, label in zip(traces, labels):
        data = build_graph(trace, label, tool_vocab)
        dataset.append(data)

    return dataset
