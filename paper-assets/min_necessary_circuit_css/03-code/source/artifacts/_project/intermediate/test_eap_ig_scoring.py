"""Smoke tests for eap_ig_scoring.py — AST checks + optional runtime integration."""

import ast
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(SCRIPT_DIR, "eap_ig_scoring.py")


# ---------------------------------------------------------------------------
# 1. AST-based checks (no dependencies)
# ---------------------------------------------------------------------------

def _parse_source():
    with open(SOURCE) as f:
        return ast.parse(f.read(), filename=SOURCE)


def test_file_loads():
    tree = _parse_source()
    assert isinstance(tree, ast.Module)
    print("  [PASS] file parses as valid Python")


def test_compute_eap_ig_edges_signature():
    tree = _parse_source()
    func = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "compute_eap_ig_edges":
            func = node
            break
    assert func is not None, "compute_eap_ig_edges not found"

    args = func.args
    pos_names = [a.arg for a in args.args]
    assert pos_names[:5] == [
        "model", "clean_inputs", "corrupt_inputs", "metric_fn", "target_ids"
    ], f"Unexpected positional args: {pos_names}"

    kw_names = {a.arg for a in args.args}
    assert "ig_steps" in kw_names, "missing ig_steps param"
    assert "device" in kw_names, "missing device param"

    ret = ast.dump(func.returns) if func.returns else ""
    assert "Dict" in ret or "dict" in ret.lower() or func.returns is None, \
        f"Unexpected return annotation: {ret}"

    print("  [PASS] compute_eap_ig_edges signature (AST)")


def test_required_functions_exist():
    tree = _parse_source()
    names = {
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }
    expected = {
        "compute_eap_ig_edges",
        "_get_model_info",
        "_prepare_inputs",
        "_before_attn",
        "_before_mlp",
        "_src_label",
        "_decompose_per_head",
        "_capture_source_activations",
        "_get_proj_weights",
        "_get_pre_mlp_ln",
    }
    missing = expected - names
    assert not missing, f"Missing functions: {missing}"
    print(f"  [PASS] all {len(expected)} required functions found")


def test_edge_name_format_in_source():
    with open(SOURCE) as f:
        src = f.read()
    assert "->a" in src, "Missing attention edge format"
    assert "->m" in src, "Missing MLP edge format"
    assert ".q" in src and ".k" in src and ".v" in src, "Missing Q/K/V suffixes"
    assert '"input"' in src, "Missing 'input' node name"
    print("  [PASS] canonical edge naming in source")


def test_docstring():
    tree = _parse_source()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "compute_eap_ig_edges":
            docstring = ast.get_docstring(node)
            assert docstring is not None, "compute_eap_ig_edges has no docstring"
            assert "edge" in docstring.lower(), "Docstring should mention edges"
            assert "IG" in docstring.upper() or "integrated" in docstring.lower(), \
                "Docstring should mention IG/Integrated Gradients"
            print("  [PASS] compute_eap_ig_edges has docstring")
            return
    assert False, "compute_eap_ig_edges not found"


def test_gqa_handling_in_source():
    with open(SOURCE) as f:
        src = f.read()
    assert "n_kv_heads" in src, "Missing GQA support (n_kv_heads)"
    assert "heads_per_group" in src, "Missing GQA head grouping logic"
    print("  [PASS] GQA handling present in source")


# ---------------------------------------------------------------------------
# 2. Runtime tests (only if torch + transformers available)
# ---------------------------------------------------------------------------

def test_runtime_helpers():
    try:
        import torch
    except ImportError:
        print("  [SKIP] runtime tests (torch not installed)")
        return

    sys.path.insert(0, SCRIPT_DIR)
    from eap_ig_scoring import (
        _before_attn, _before_mlp, _src_label, _prepare_inputs,
    )

    assert _before_attn("input", -1, 0)
    assert _before_attn("attn", 0, 1)
    assert not _before_attn("attn", 1, 1)
    assert not _before_attn("mlp", 2, 1)

    assert _before_mlp("input", -1, 0)
    assert _before_mlp("attn", 0, 0)
    assert not _before_mlp("mlp", 0, 0)
    assert _before_mlp("mlp", 0, 1)

    assert _src_label("input", -1, -1) == "input"
    assert _src_label("attn", 2, 5) == "a2.h5"
    assert _src_label("mlp", 3, -1) == "m3"

    t = _prepare_inputs(torch.tensor([1, 2, 3]), "cpu")
    assert t.shape == (1, 3)
    t = _prepare_inputs({"input_ids": [[1, 2]]}, "cpu")
    assert t.shape == (1, 2)
    t = _prepare_inputs([[1, 2], [3, 4]], "cpu")
    assert t.shape == (2, 2)

    print("  [PASS] runtime helpers")


def test_gpt2_integration():
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoConfig
    except ImportError:
        print("  [SKIP] GPT-2 integration (missing deps)")
        return

    sys.path.insert(0, SCRIPT_DIR)
    from eap_ig_scoring import compute_eap_ig_edges

    config = AutoConfig.from_pretrained("gpt2")
    config.n_layer = 2
    config.n_head = 2
    config.n_embd = 64
    config.vocab_size = 100
    model = AutoModelForCausalLM.from_config(config)
    model.eval()

    B, S, V = 2, 8, 100
    clean = torch.randint(0, V, (B, S))
    corrupt = torch.randint(0, V, (B, S))
    target = torch.tensor([1])

    def metric_fn(logits, tgt):
        return logits[:, -1, tgt[0]].mean()

    scores = compute_eap_ig_edges(
        model, clean, corrupt, metric_fn, target,
        ig_steps=2, device="cpu",
    )

    assert isinstance(scores, dict)
    assert len(scores) > 0
    for name, val in scores.items():
        assert isinstance(name, str) and "->" in name, f"Bad edge name: {name}"
        assert isinstance(val, float) and val >= 0, f"Bad score: {name}={val}"

    attn_q = sum(1 for e in scores if ".q" in e.split("->")[1])
    attn_k = sum(1 for e in scores if ".k" in e.split("->")[1])
    attn_v = sum(1 for e in scores if ".v" in e.split("->")[1])
    mlp_edges = sum(1 for e in scores if e.split("->")[1].startswith("m"))
    assert attn_q > 0, "No .q edges"
    assert attn_k > 0, "No .k edges"
    assert attn_v > 0, "No .v edges"
    assert mlp_edges > 0, "No MLP edges"

    has_nonzero = any(v > 0 for v in scores.values())
    assert has_nonzero, "All scores are zero — gradient flow may be broken"

    print(f"  [PASS] GPT-2 integration ({len(scores)} edges: "
          f"{attn_q} .q, {attn_k} .k, {attn_v} .v, {mlp_edges} mlp)")
    sample = list(scores.items())[:3]
    print(f"         sample: {sample}")


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("eap_ig_scoring smoke tests")
    print("--- AST-based (no deps) ---")
    test_file_loads()
    test_compute_eap_ig_edges_signature()
    test_required_functions_exist()
    test_edge_name_format_in_source()
    test_docstring()
    test_gqa_handling_in_source()
    print("--- Runtime ---")
    test_runtime_helpers()
    test_gpt2_integration()
    print("\nDone.")
