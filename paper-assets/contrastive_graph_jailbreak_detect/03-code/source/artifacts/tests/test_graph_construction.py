import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import torch
from src.graph_construction import build_graph, build_dataset, build_tool_vocab
from src.data.benign_generator import generate_benign_traces


MOCK_TRACE = {
    "id": 0,
    "generation_config": {"failure_mode": "data_exfiltration", "environment": "office"},
    "attack_plan": {
        "verified_tool_chain": [
            {"step": 1, "tool_name": "search_contacts_by_name", "parameters": {"name": "Alice"}, "purpose": "find target"}
        ]
    },
    "interaction_history": [
        {"role": "user", "content": "Find Alice's email and send her a message"},
        {
            "role": "assistant",
            "tool_calls": [{
                "id": "call_1",
                "function": {
                    "name": "search_contacts_by_name",
                    "arguments": '{"name": "Alice"}'
                }
            }]
        },
        {
            "role": "tool",
            "tool_call_id": "call_1",
            "name": "search_contacts_by_name",
            "content": '{"email": "alice@company.com", "phone": "555-1234"}'
        },
        {
            "role": "assistant",
            "tool_calls": [{
                "id": "call_2",
                "function": {
                    "name": "send_email",
                    "arguments": '{"to": "alice@company.com", "subject": "Hello", "body": "Hi Alice"}'
                }
            }]
        },
        {
            "role": "tool",
            "tool_call_id": "call_2",
            "name": "send_email",
            "content": '{"status": "sent", "message_id": "msg_001"}'
        },
        {
            "role": "assistant",
            "tool_calls": [{
                "id": "call_3",
                "function": {
                    "name": "get_calendar",
                    "arguments": '{"user": "alice@company.com", "date": "2024-01-15"}'
                }
            }]
        },
        {
            "role": "tool",
            "tool_call_id": "call_3",
            "name": "get_calendar",
            "content": '{"events": [{"title": "Team meeting", "time": "10:00"}]}'
        }
    ]
}


def test_build_graph_basic():
    tool_vocab = {"search_contacts_by_name": 0, "send_email": 1, "get_calendar": 2}
    data = build_graph(MOCK_TRACE, label=1, tool_vocab=tool_vocab)

    assert data.x is not None
    assert data.edge_index is not None
    assert data.y is not None
    assert data.x.shape[0] == 3  # 3 tool calls
    assert data.x.shape[1] == len(tool_vocab) + 3  # one-hot + 3 features
    assert data.y.item() == 1
    assert data.failure_mode == "data_exfiltration"
    assert data.edge_index.shape[0] == 2
    assert data.edge_index.shape[1] > 0  # should have edges (alice@company.com flows)
    print("  [PASS] test_build_graph_basic")


def test_build_graph_dataflow():
    """Verify data-flow edge from search_contacts -> send_email via alice@company.com."""
    tool_vocab = {"search_contacts_by_name": 0, "send_email": 1, "get_calendar": 2}
    data = build_graph(MOCK_TRACE, label=1, tool_vocab=tool_vocab)

    edges = set()
    for i in range(data.edge_index.shape[1]):
        src = data.edge_index[0, i].item()
        dst = data.edge_index[1, i].item()
        edges.add((src, dst))

    # search_contacts (0) output contains alice@company.com, used by send_email (1) and get_calendar (2)
    assert (0, 1) in edges, f"Expected edge (0,1) in {edges}"
    assert (0, 2) in edges, f"Expected edge (0,2) in {edges}"
    print("  [PASS] test_build_graph_dataflow")


def test_build_dataset():
    traces = [MOCK_TRACE, MOCK_TRACE]
    labels = [1, 0]
    dataset = build_dataset(traces, labels)

    assert len(dataset) == 2
    assert dataset[0].y.item() == 1
    assert dataset[1].y.item() == 0
    print("  [PASS] test_build_dataset")


def test_build_tool_vocab():
    vocab = build_tool_vocab([MOCK_TRACE])
    assert "search_contacts_by_name" in vocab
    assert "send_email" in vocab
    assert "get_calendar" in vocab
    assert len(vocab) == 3
    print("  [PASS] test_build_tool_vocab")


def test_benign_generator():
    traces = generate_benign_traces([MOCK_TRACE], n_traces=10, seed=42)

    assert len(traces) == 10
    for t in traces:
        assert "interaction_history" in t
        assert "generation_config" in t
        assert t["generation_config"]["failure_mode"] == "benign"
        # Should have at least user msg + assistant msg + tool msg
        assert len(t["interaction_history"]) >= 3

        # Verify structure: has assistant with tool_calls and corresponding tool responses
        has_tool_call = False
        for msg in t["interaction_history"]:
            if msg.get("role") == "assistant" and "tool_calls" in msg:
                has_tool_call = True
                for tc in msg["tool_calls"]:
                    assert "function" in tc
                    assert "name" in tc["function"]
                    assert "arguments" in tc["function"]
        assert has_tool_call
    print("  [PASS] test_benign_generator")


def test_benign_traces_as_graphs():
    """Verify benign traces can be converted to graphs."""
    benign = generate_benign_traces([MOCK_TRACE], n_traces=5, seed=123)
    all_traces = [MOCK_TRACE] + benign
    labels = [1] + [0] * len(benign)

    dataset = build_dataset(all_traces, labels)
    assert len(dataset) == 6
    assert dataset[0].y.item() == 1
    for d in dataset[1:]:
        assert d.y.item() == 0
        assert d.x.shape[0] >= 1
    print("  [PASS] test_benign_traces_as_graphs")


if __name__ == "__main__":
    print("Running tests...")
    test_build_graph_basic()
    test_build_graph_dataflow()
    test_build_dataset()
    test_build_tool_vocab()
    test_benign_generator()
    test_benign_traces_as_graphs()
    print("\nAll tests passed!")
