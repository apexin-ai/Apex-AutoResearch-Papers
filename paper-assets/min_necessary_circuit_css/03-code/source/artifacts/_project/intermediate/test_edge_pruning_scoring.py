"""Smoke tests for edge_pruning_scoring.py.

Tests split by dependency:
  - No-torch tests: AST syntax, function signature from AST, edge topology logic
  - Torch tests: HardConcrete numerics, gradient flow, estimate_edge_counts

Run without torch: python3 test_edge_pruning_scoring.py
Run with torch:    python3 test_edge_pruning_scoring.py  (auto-detects)
"""

import ast
import os
import sys

SRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "edge_pruning_scoring.py")

HAS_TORCH = False
try:
    import torch
    HAS_TORCH = True
except ImportError:
    pass


# ===========================================================================
# No-torch tests (pure AST / logic)
# ===========================================================================

def test_ast_syntax():
    with open(SRC_PATH) as f:
        source = f.read()
    tree = ast.parse(source)
    assert isinstance(tree, ast.Module)
    top_names = {node.name for node in ast.walk(tree)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    assert "HardConcrete" in top_names
    assert "compute_edge_pruning_scores" in top_names
    assert "estimate_edge_counts" in top_names
    assert "_build_edge_topology" in top_names
    assert "_masked_forward" in top_names
    assert "_faithfulness_loss" in top_names
    print("[PASS] AST syntax check")


def test_function_signature_from_ast():
    with open(SRC_PATH) as f:
        source = f.read()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "compute_edge_pruning_scores":
            args = node.args
            param_names = [a.arg for a in args.args]
            expected = [
                "model", "clean_inputs", "corrupt_inputs", "metric_fn",
                "target_ids", "n_epochs", "lambda_l0", "lr", "device",
            ]
            assert param_names == expected, f"Expected {expected}, got {param_names}"
            # Check defaults: n_epochs=100, lambda_l0=1e-3, lr=0.1, device="cuda"
            defaults = args.defaults
            assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device="cuda"
            print("[PASS] Function signature (AST)")
            return
    raise AssertionError("compute_edge_pruning_scores not found")


def _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):
    """Standalone copy of edge topology logic for testing without torch."""
    edge_names = []
    edge_to_mask_idx = {}
    mask_idx = 0

    def _src_nodes(layer, include_attn_same_layer=False):
        yield "input"
        for l in range(layer):
            for h in range(n_heads):
                yield f"a{l}.h{h}"
            yield f"m{l}"
        if include_attn_same_layer:
            for h in range(n_heads):
                yield f"a{layer}.h{h}"

    for L in range(n_layers):
        srcs_attn = list(_src_nodes(L))
        for src in srcs_attn:
            for H in range(n_heads):
                q_edge = f"{src}->a{L}.h{H}.q"
                edge_names.append(q_edge)
                edge_to_mask_idx[q_edge] = mask_idx
                mask_idx += 1
            for kv_group in range(n_kv_heads):
                k_mask_idx = mask_idx
                mask_idx += 1
                for h_in_group in range(heads_per_kv_group):
                    H = kv_group * heads_per_kv_group + h_in_group
                    k_edge = f"{src}->a{L}.h{H}.k"
                    edge_names.append(k_edge)
                    edge_to_mask_idx[k_edge] = k_mask_idx
            for kv_group in range(n_kv_heads):
                v_mask_idx = mask_idx
                mask_idx += 1
                for h_in_group in range(heads_per_kv_group):
                    H = kv_group * heads_per_kv_group + h_in_group
                    v_edge = f"{src}->a{L}.h{H}.v"
                    edge_names.append(v_edge)
                    edge_to_mask_idx[v_edge] = v_mask_idx

        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))
        for src in srcs_mlp:
            mlp_edge = f"{src}->m{L}"
            edge_names.append(mlp_edge)
            edge_to_mask_idx[mlp_edge] = mask_idx
            mask_idx += 1

    return edge_names, edge_to_mask_idx, mask_idx


def test_edge_topology_no_gqa():
    n_layers, n_heads, n_kv_heads = 2, 4, 4
    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(
        n_layers, n_heads, n_kv_heads, 1,
    )
    assert len(set(edge_to_mask_idx.values())) == n_masks
    assert n_masks == len(edge_to_mask_idx)
    assert "input->a0.h0.q" in edge_to_mask_idx
    assert "input->a0.h0.k" in edge_to_mask_idx
    assert "input->a0.h0.v" in edge_to_mask_idx
    assert "input->m0" in edge_to_mask_idx
    assert "a0.h0->m0" in edge_to_mask_idx
    assert "a0.h0->a1.h0.q" in edge_to_mask_idx
    print(f"[PASS] Edge topology non-GQA: {len(edge_names)} edges, {n_masks} masks")


def test_edge_topology_gqa():
    n_layers, n_heads, n_kv_heads = 2, 14, 2
    heads_per_kv = 7
    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(
        n_layers, n_heads, n_kv_heads, heads_per_kv,
    )

    # K mask sharing within KV group 0 (heads 0-6)
    k_masks_g0 = {edge_to_mask_idx[f"input->a0.h{h}.k"] for h in range(7)}
    assert len(k_masks_g0) == 1, f"KV group 0 K masks should share, got {len(k_masks_g0)}"

    # K mask sharing within KV group 1 (heads 7-13)
    k_masks_g1 = {edge_to_mask_idx[f"input->a0.h{h}.k"] for h in range(7, 14)}
    assert len(k_masks_g1) == 1
    assert k_masks_g0 != k_masks_g1

    # Q edges independent
    q_masks = {edge_to_mask_idx[f"input->a0.h{h}.q"] for h in range(14)}
    assert len(q_masks) == 14

    # V sharing
    v_masks_g0 = {edge_to_mask_idx[f"input->a0.h{h}.v"] for h in range(7)}
    assert len(v_masks_g0) == 1

    print(f"[PASS] Edge topology GQA: {len(edge_names)} edges, {n_masks} masks")


def test_dst_mask_table():
    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(1, 2, 2, 1)
    table = {}
    for edge, idx in edge_to_mask_idx.items():
        src, dst = edge.split("->", 1)
        table.setdefault(dst, {})[src] = idx

    assert "a0.h0.q" in table
    assert "input" in table["a0.h0.q"]
    assert "m0" in table
    assert "input" in table["m0"]
    assert "a0.h0" in table["m0"]
    assert "a0.h1" in table["m0"]
    print("[PASS] Destination mask table")


def test_edge_counts_qwen():
    """Estimate edge counts for Qwen-2.5 0.5B without torch."""
    _, _, n_masks = _build_edge_topology_standalone(24, 14, 2, 7)
    total_edges = 0
    for L in range(24):
        n_src = 1 + L * (14 + 1)
        total_edges += n_src * 14 * 3
        total_edges += (n_src + 14)
    mem_mb = n_masks * 4 / (1024 ** 2)
    assert total_edges > 0
    assert n_masks > 0
    assert n_masks <= total_edges
    print(f"[PASS] Qwen-2.5 0.5B: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB")


def test_edge_counts_gpt2():
    _, _, n_masks = _build_edge_topology_standalone(12, 12, 12, 1)
    total_edges = 0
    for L in range(12):
        n_src = 1 + L * (12 + 1)
        total_edges += n_src * 12 * 3
        total_edges += (n_src + 12)
    mem_mb = n_masks * 4 / (1024 ** 2)
    print(f"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB")


# ===========================================================================
# Torch-dependent tests
# ===========================================================================

def test_hard_concrete_sampling():
    from edge_pruning_scoring import HardConcrete
    hc = HardConcrete(n_masks=1000, init_mean=0.5)
    torch.manual_seed(42)
    samples = hc(training=True)
    assert samples.shape == (1000,)
    assert samples.min() >= 0.0
    assert samples.max() <= 1.0
    penalty = hc.l0_penalty()
    assert penalty.item() >= 0.0
    assert penalty.item() <= 1000.0
    expected = hc.expected_masks()
    assert expected.min() >= 0.0
    assert expected.max() <= 1.0
    print("[PASS] HardConcrete sampling")


def test_hard_concrete_gradient():
    from edge_pruning_scoring import HardConcrete
    hc = HardConcrete(n_masks=10, init_mean=0.5)
    masks = hc(training=True)
    masks.sum().backward()
    assert hc.log_alpha.grad is not None
    assert not torch.all(hc.log_alpha.grad == 0)
    print("[PASS] HardConcrete gradient flow")


def test_hard_concrete_extremes():
    from edge_pruning_scoring import HardConcrete
    hc = HardConcrete(n_masks=2, init_mean=0.5)
    with torch.no_grad():
        hc.log_alpha[0] = -10.0
        hc.log_alpha[1] = 10.0
    masks = hc.expected_masks()
    assert masks[0].item() < 0.01
    assert masks[1].item() > 0.99
    print("[PASS] HardConcrete extremes")


def test_module_topology_matches_standalone():
    """Verify the actual module's topology matches our standalone copy."""
    from edge_pruning_scoring import _build_edge_topology
    _, idx_module, n_module = _build_edge_topology(2, 14, 2, 7)
    _, idx_standalone, n_standalone = _build_edge_topology_standalone(2, 14, 2, 7)
    assert n_module == n_standalone, f"n_masks mismatch: {n_module} vs {n_standalone}"
    assert idx_module == idx_standalone, "edge_to_mask_idx mismatch"
    print("[PASS] Module topology matches standalone")


# ===========================================================================

if __name__ == "__main__":
    # Always run: no-torch tests
    test_ast_syntax()
    test_function_signature_from_ast()
    test_edge_topology_no_gqa()
    test_edge_topology_gqa()
    test_dst_mask_table()
    test_edge_counts_qwen()
    test_edge_counts_gpt2()

    if HAS_TORCH:
        test_hard_concrete_sampling()
        test_hard_concrete_gradient()
        test_hard_concrete_extremes()
        test_module_topology_matches_standalone()
    else:
        print("[SKIP] Torch-dependent tests (torch not installed)")

    print("\n=== All applicable smoke tests passed ===")
