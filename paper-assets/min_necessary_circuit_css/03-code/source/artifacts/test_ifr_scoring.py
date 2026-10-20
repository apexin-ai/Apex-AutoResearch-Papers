"""Smoke tests for ifr_scoring.py — AST-based signature checks + optional integration."""

import ast
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(SCRIPT_DIR, "ifr_scoring.py")


# ---------------------------------------------------------------------------
# 1. Parse source with AST (no torch/transformers dependency)
# ---------------------------------------------------------------------------

def _parse_source():
    with open(SOURCE) as f:
        return ast.parse(f.read(), filename=SOURCE)


def test_file_loads():
    tree = _parse_source()
    assert isinstance(tree, ast.Module)
    print("  [PASS] file parses as valid Python")


def test_compute_ifr_edges_signature():
    tree = _parse_source()
    func = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "compute_ifr_edges":
            func = node
            break
    assert func is not None, "compute_ifr_edges not found"

    args = func.args
    # Positional args: model, dataset, metric_fn
    pos_names = [a.arg for a in args.args]
    assert pos_names[:3] == ["self"] or pos_names[:3] == ["model", "dataset", "metric_fn"], \
        f"Unexpected positional args: {pos_names}"

    # keyword defaults: threshold, device
    default_names = {a.arg for a in args.args if a.arg in ("threshold", "device")}
    assert "threshold" in default_names, "missing threshold param"
    assert "device" in default_names, "missing device param"

    # Check return annotation mentions Dict
    ret = ast.dump(func.returns) if func.returns else ""
    assert "Dict" in ret or "dict" in ret.lower() or func.returns is None, \
        f"Unexpected return annotation: {ret}"

    print("  [PASS] compute_ifr_edges signature (AST)")


def test_required_functions_exist():
    tree = _parse_source()
    names = {
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }
    expected = {
        "compute_ifr_edges",
        "_proximity",
        "_get_model_info",
        "_before_attn",
        "_before_mlp",
        "_prepare_tokens",
        "_decompose_per_head",
        "_src_label",
    }
    missing = expected - names
    assert not missing, f"Missing functions: {missing}"
    print(f"  [PASS] all {len(expected)} required functions found")


def test_edge_name_format_in_source():
    """Verify canonical edge naming appears in the source code."""
    with open(SOURCE) as f:
        src = f.read()
    # Should contain the edge format pattern
    assert "->a" in src, "Missing attention edge format"
    assert "->m" in src, "Missing MLP edge format"
    assert ".q" in src and ".k" in src and ".v" in src, "Missing Q/K/V suffixes"
    assert '"input"' in src, "Missing 'input' node name"
    print("  [PASS] canonical edge naming in source")


def test_docstring():
    tree = _parse_source()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "compute_ifr_edges":
            docstring = ast.get_docstring(node)
            assert docstring is not None, "compute_ifr_edges has no docstring"
            assert "edge" in docstring.lower(), "Docstring should mention edges"
            print("  [PASS] compute_ifr_edges has docstring")
            return
    assert False, "compute_ifr_edges not found"


# ---------------------------------------------------------------------------
# 2. Runtime tests (only if torch + transformers available)
# ---------------------------------------------------------------------------

def test_runtime():
    try:
        import torch
    except ImportError:
        print("  [SKIP] runtime tests (torch not installed)")
        return

    sys.path.insert(0, SCRIPT_DIR)
    from ifr_scoring import (
        _proximity, _before_attn, _before_mlp, _prepare_tokens, _src_label,
    )

    # Proximity
    x = torch.tensor([[[1.0, 2.0, 3.0]]])
    assert _proximity(x, x) > 0
    assert _proximity(torch.zeros_like(x), x) >= 0
    print("  [PASS] _proximity (runtime)")

    # Topology
    assert _before_attn("input", -1, 0)
    assert not _before_attn("attn", 1, 1)
    assert _before_mlp("attn", 0, 0)
    assert not _before_mlp("mlp", 0, 0)
    print("  [PASS] topology helpers (runtime)")

    # Token prep
    t = _prepare_tokens(torch.tensor([1, 2, 3]), "cpu")
    assert t.shape == (1, 3)
    t = _prepare_tokens({"input_ids": [[1, 2, 3]]}, "cpu")
    assert t.shape == (1, 3)
    t = _prepare_tokens([{"input_ids": [1, 2]}, {"input_ids": [3, 4]}], "cpu")
    assert t.shape == (2, 2)
    print("  [PASS] _prepare_tokens (runtime)")

    # Labels
    assert _src_label("input", -1, -1) == "input"
    assert _src_label("attn", 0, 3) == "a0.h3"
    assert _src_label("mlp", 5, -1) == "m5"
    print("  [PASS] _src_label (runtime)")


def test_gpt2_integration():
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoConfig
    except ImportError:
        print("  [SKIP] GPT-2 integration (missing deps)")
        return

    sys.path.insert(0, SCRIPT_DIR)
    from ifr_scoring import compute_ifr_edges

    config = AutoConfig.from_pretrained("gpt2")
    config.n_layer = 2
    config.n_head = 2
    config.n_embd = 64
    config.vocab_size = 100
    model = AutoModelForCausalLM.from_config(config)
    model.eval()

    tokens = torch.randint(0, 100, (2, 8))
    scores = compute_ifr_edges(model, tokens, metric_fn=lambda x: x, threshold=0.0, device="cpu")

    assert isinstance(scores, dict)
    assert len(scores) > 0
    for name, val in scores.items():
        assert isinstance(name, str) and "->" in name
        assert isinstance(val, float) and val >= 0

    attn_edges = sum(1 for e in scores if e.split("->")[1].startswith("a"))
    mlp_edges = sum(1 for e in scores if e.split("->")[1].startswith("m"))
    assert attn_edges > 0 and mlp_edges > 0

    print(f"  [PASS] GPT-2 integration ({len(scores)} edges: {attn_edges} attn, {mlp_edges} mlp)")
    sample = list(scores.keys())[:3]
    print(f"         sample: {sample}")


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("ifr_scoring smoke tests")
    print("--- AST-based (no deps) ---")
    test_file_loads()
    test_compute_ifr_edges_signature()
    test_required_functions_exist()
    test_edge_name_format_in_source()
    test_docstring()
    print("--- Runtime ---")
    test_runtime()
    test_gpt2_integration()
    print("\nDone.")
