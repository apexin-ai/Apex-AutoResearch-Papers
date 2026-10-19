#!/usr/bin/env python3
"""DPO pipeline integration test (dry-run, no GPU required).

Validates the full data pipeline:
  synthetic JSONL -> DPODataset -> collate_dpo -> phi weights -> loss shapes

Uses gpt2 tokenizer with a custom chat template for format testing only.
"""
import json
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import torch
from dmpo_loss import compute_phi_weights
from etadn_discount import compute_discount_weights, phi

SYNTH_PATH = ROOT / "tests" / "synthetic_dpo.jsonl"
REPORT_PATH = ROOT / "tests" / "pipeline_test_report.md"

results = []


def record(name: str, passed: bool, detail: str = ""):
    status = "PASS" if passed else "FAIL"
    results.append((name, status, detail))
    tag = f"[{status}]"
    print(f"  {tag} {name}" + (f" -- {detail}" if detail else ""))


# ── Step 1: Validate synthetic JSONL format ──────────────────────────────────

print("=" * 60)
print("Step 1: Validate synthetic JSONL format")
print("=" * 60)

samples = []
try:
    with open(SYNTH_PATH) as f:
        for i, line in enumerate(f):
            obj = json.loads(line)
            samples.append(obj)
    record("jsonl_load", True, f"{len(samples)} samples loaded")
except Exception as e:
    record("jsonl_load", False, str(e))

required_fields = [
    "prompt", "chosen", "rejected", "gamma_e", "error_type",
    "divergence_step", "game_file", "correction_span",
]
for field in required_fields:
    present = all(field in s for s in samples)
    record(f"field_{field}", present, "" if present else "missing in some samples")

msg_list_fields = ["prompt", "chosen", "rejected"]
for field in msg_list_fields:
    ok = all(
        isinstance(s[field], list)
        and all(isinstance(m, dict) and "role" in m and "content" in m for m in s[field])
        for s in samples
    )
    record(f"{field}_is_msg_list", ok)

gamma_values = [s["gamma_e"] for s in samples]
gamma_min, gamma_max = min(gamma_values), max(gamma_values)
covers_range = gamma_min <= 0.86 and gamma_max >= 0.96
record(
    "gamma_e_range",
    covers_range,
    f"min={gamma_min}, max={gamma_max} (target: covers 0.85-0.97)",
)

d_values = [s.get("d", -1) for s in samples]
d_range_ok = min(d_values) >= 0.0 and max(d_values) <= 1.0
record("d_range", d_range_ok, f"min={min(d_values)}, max={max(d_values)}")

error_types = set(s["error_type"] for s in samples)
record("error_type_coverage", error_types == {"action", "verification", "planning"},
       f"found: {error_types}")


# ── Step 2: DPODataset loading ───────────────────────────────────────────────

print()
print("=" * 60)
print("Step 2: DPODataset loading (gpt2 + custom chat template)")
print("=" * 60)

try:
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.chat_template = (
        "{% for message in messages %}"
        "{% if message['role'] == 'user' %}User: {{ message['content'] }}\n"
        "{% elif message['role'] == 'assistant' %}Assistant: {{ message['content'] }}\n"
        "{% endif %}"
        "{% endfor %}"
        "{% if add_generation_prompt %}Assistant: {% endif %}"
    )
    record("tokenizer_load", True, "gpt2 with custom chat_template")
except Exception as e:
    record("tokenizer_load", False, str(e))
    tokenizer = None

if tokenizer is not None:
    from train_dpo import DPODataset, collate_dpo

    # ── etadn mode ──
    try:
        ds_etadn = DPODataset(
            str(SYNTH_PATH), tokenizer, max_length=512, mode="etadn", gamma=0.92
        )
        record("dataset_etadn_load", True, f"{len(ds_etadn)} samples")
    except Exception as e:
        record("dataset_etadn_load", False, traceback.format_exc())
        ds_etadn = None

    if ds_etadn is not None:
        try:
            sample0 = ds_etadn[0]
            keys = set(sample0.keys())
            expected_keys = {"idx", "chosen_ids", "rejected_ids", "prompt_len", "gamma"}
            record("sample_keys", keys == expected_keys, f"got: {keys}")

            gamma_from_jsonl = samples[0]["gamma_e"]
            gamma_from_dataset = sample0["gamma"]
            gamma_match = abs(gamma_from_dataset - gamma_from_jsonl) < 1e-6
            record(
                "etadn_gamma_from_jsonl",
                gamma_match,
                f"dataset={gamma_from_dataset}, jsonl={gamma_from_jsonl}",
            )
        except Exception as e:
            record("sample_access", False, traceback.format_exc())

        # collate
        try:
            batch_items = [ds_etadn[i] for i in range(min(3, len(ds_etadn)))]
            batch = collate_dpo(batch_items, tokenizer.pad_token_id)
            record("collate_dpo", True, f"batch keys: {list(batch.keys())}")

            gammas = batch["gammas"]
            expected_gammas = [samples[i]["gamma_e"] for i in range(len(batch_items))]
            gammas_ok = all(
                abs(g - e) < 1e-6 for g, e in zip(gammas, expected_gammas)
            )
            record(
                "batch_gammas_etadn",
                gammas_ok,
                f"batch={gammas}, expected={expected_gammas}",
            )

            record(
                "batch_tensor_shapes",
                True,
                f"chosen={batch['chosen_ids'].shape}, rejected={batch['rejected_ids'].shape}",
            )
        except Exception as e:
            record("collate_dpo", False, traceback.format_exc())

    # ── single_gamma mode ──
    try:
        ds_sg = DPODataset(
            str(SYNTH_PATH), tokenizer, max_length=512, mode="single_gamma", gamma=0.92
        )
        sample_sg = ds_sg[0]
        gamma_sg = sample_sg["gamma"]
        sg_ok = abs(gamma_sg - 0.92) < 1e-6
        record(
            "single_gamma_mode",
            sg_ok,
            f"gamma={gamma_sg} (should be CLI value 0.92, not jsonl gamma_e={samples[0]['gamma_e']})",
        )
    except Exception as e:
        record("single_gamma_mode", False, traceback.format_exc())

    # ── all 10 samples accessible ──
    try:
        for i in range(len(ds_etadn)):
            _ = ds_etadn[i]
        record("all_samples_accessible", True, f"all {len(ds_etadn)} indexed without error")
    except Exception as e:
        record("all_samples_accessible", False, f"failed at index: {traceback.format_exc()}")


# ── Step 3: phi weights validation ───────────────────────────────────────────

print()
print("=" * 60)
print("Step 3: phi weights validation")
print("=" * 60)

# 3a: basic properties
for gamma in [0.85, 0.92, 0.97]:
    w = compute_phi_weights(10, gamma)
    record(
        f"phi_shape_gamma={gamma}",
        w.shape == (10,),
        f"shape={w.shape}",
    )
    record(
        f"phi_positive_gamma={gamma}",
        (w > 0).all().item(),
        f"min={w.min().item():.6f}",
    )
    # monotonically decreasing
    mono = all(w[i] >= w[i + 1] - 1e-6 for i in range(len(w) - 1))
    record(f"phi_monotone_gamma={gamma}", mono)

# 3b: normalization check (Sigma = 1?)
print()
print("  -- Normalization check (sum=1?) --")
for gamma in [0.85, 0.92, 0.97]:
    w = compute_phi_weights(10, gamma)
    wsum = w.sum().item()
    normalized = abs(wsum - 1.0) < 1e-5
    record(
        f"phi_normalized_gamma={gamma}",
        normalized,
        f"sum={wsum:.6f}",
    )

# 3c: scalar phi() matches vectorized compute_discount_weights()
for gamma in [0.85, 0.97]:
    T = 8
    w = compute_discount_weights(T, gamma)
    match = all(abs(w[t].item() - phi(t, T, gamma)) < 1e-5 for t in range(T))
    record(f"scalar_vec_match_gamma={gamma}", match)

# 3d: edge cases
w_t1 = compute_phi_weights(1, 0.92)
record("phi_T=1", w_t1.shape == (1,) and abs(w_t1[0].item() - 1.0) < 1e-5,
       f"T=1 weight={w_t1[0].item():.6f}")

w_g1 = compute_phi_weights(5, 1.0)
uniform_ok = abs(w_g1.sum().item() - 1.0) < 1e-5 and abs(w_g1[0].item() - 0.2) < 1e-5
record("phi_gamma=1_uniform", uniform_ok, f"weights={w_g1.tolist()}")

w_empty = compute_phi_weights(0, 0.92)
record("phi_T=0", len(w_empty) == 0, f"shape={w_empty.shape}")


# ── Step 4: dmpo_loss integration ────────────────────────────────────────────

print()
print("=" * 60)
print("Step 4: dmpo_loss integration (no model, synthetic tensors)")
print("=" * 60)

from dmpo_loss import dmpo_loss, dmpo_loss_batch, phi_weighted_logps

try:
    T_c, T_r = 8, 6
    gamma_test = 0.92
    w_c = compute_phi_weights(T_c, gamma_test)
    w_r = compute_phi_weights(T_r, gamma_test)

    torch.manual_seed(42)
    pc = torch.randn(T_c)
    pr = torch.randn(T_r)
    rc = torch.randn(T_c)
    rr = torch.randn(T_r)

    loss = dmpo_loss(pc, pr, rc, rr, w_c, w_r, beta=0.1)
    record("dmpo_loss_scalar", torch.isfinite(loss).item(), f"loss={loss.item():.6f}")
except Exception as e:
    record("dmpo_loss_scalar", False, traceback.format_exc())

try:
    B, max_len = 3, 20
    torch.manual_seed(42)
    pol_c = torch.randn(B, max_len, requires_grad=True)
    pol_r = torch.randn(B, max_len, requires_grad=True)
    ref_c = torch.randn(B, max_len)
    ref_r = torch.randn(B, max_len)
    prompt_lens = [3, 4, 2]
    chosen_resp_lens = [8, 6, 10]
    rejected_resp_lens = [7, 5, 9]
    gammas_list = [0.85, 0.92, 0.97]

    loss_b, metrics = dmpo_loss_batch(
        pol_c, pol_r, ref_c, ref_r,
        chosen_resp_lens, rejected_resp_lens, prompt_lens, gammas_list, beta=0.1,
    )
    record("dmpo_loss_batch", torch.isfinite(loss_b).item(),
           f"loss={loss_b.item():.4f}, metrics_keys={list(metrics.keys())}")

    loss_b.backward()
    grad_ok = pol_c.grad is not None and torch.isfinite(pol_c.grad).all().item()
    record("dmpo_loss_gradient", grad_ok)
except Exception as e:
    record("dmpo_loss_batch", False, traceback.format_exc())


# ── Step 5: etadn_discount module tests ──────────────────────────────────────

print()
print("=" * 60)
print("Step 5: etadn_discount module (ETADNConfig, loss variants)")
print("=" * 60)

from etadn_discount import (
    ETADNConfig, get_gamma_for_error_type,
    uniform_dpo_loss, single_gamma_dpo_loss, etadn_dpo_loss,
)

config = ETADNConfig()
record("gamma_action", get_gamma_for_error_type("action", config) == 0.85)
record("gamma_verification", get_gamma_for_error_type("verification", config) == 0.92)
record("gamma_planning", get_gamma_for_error_type("planning", config) == 0.97)
record("gamma_unknown_fallback", get_gamma_for_error_type("unknown", config) == 0.92)

try:
    B, L = 4, 10
    torch.manual_seed(42)
    c_lp = torch.randn(B, L, requires_grad=True)
    r_lp = torch.randn(B, L, requires_grad=True)
    rc_lp = torch.randn(B, L)
    rr_lp = torch.randn(B, L)
    lengths = torch.tensor([8, 7, 9, 6])
    error_types = ["action", "verification", "planning", "action"]

    l_u = uniform_dpo_loss(c_lp, r_lp, rc_lp, rr_lp, lengths)
    l_s = single_gamma_dpo_loss(c_lp, r_lp, rc_lp, rr_lp, lengths, gamma=0.92)
    l_e = etadn_dpo_loss(c_lp, r_lp, rc_lp, rr_lp, error_types, lengths, config)

    all_finite = all(torch.isfinite(l).item() for l in [l_u, l_s, l_e])
    record("three_loss_variants", all_finite,
           f"uniform={l_u.item():.4f}, single_gamma={l_s.item():.4f}, etadn={l_e.item():.4f}")
except Exception as e:
    record("three_loss_variants", False, traceback.format_exc())


# ── Generate report ──────────────────────────────────────────────────────────

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)

pass_count = sum(1 for _, s, _ in results if s == "PASS")
fail_count = sum(1 for _, s, _ in results if s == "FAIL")
print(f"  Total: {len(results)}  PASS: {pass_count}  FAIL: {fail_count}")

report_lines = [
    "# DPO Pipeline Integration Test Report",
    "",
    f"Date: 2026-05-13",
    f"Total checks: {len(results)} | PASS: {pass_count} | FAIL: {fail_count}",
    "",
    "## Results",
    "",
    "| # | Check | Status | Detail |",
    "|---|-------|--------|--------|",
]
for i, (name, status, detail) in enumerate(results, 1):
    detail_escaped = detail.replace("|", "\\|").replace("\n", " ")
    if len(detail_escaped) > 120:
        detail_escaped = detail_escaped[:117] + "..."
    report_lines.append(f"| {i} | {name} | {status} | {detail_escaped} |")

report_lines += [
    "",
    "## Key Findings",
    "",
]

# Identify specific findings
phi_norm_fails = [
    (n, d) for n, s, d in results if "phi_normalized" in n and s == "FAIL"
]
if phi_norm_fails:
    report_lines.append(
        "### phi weights are NOT normalized to sum=1"
    )
    report_lines.append("")
    report_lines.append(
        "The φ(t,T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T) formula produces weights "
        "where φ(0)=1.0 for all γ, but the total sum > 1 for γ < 1. "
        "This is by design — the formula normalizes such that the first weight is always 1, "
        "not such that the sum is 1. "
        "The dmpo_loss.py docstring claiming 'already normalized (sum=1)' is inaccurate."
    )
    report_lines.append("")
    for name, detail in phi_norm_fails:
        report_lines.append(f"- {name}: {detail}")
    report_lines.append("")
    report_lines.append(
        "**Impact**: In `train_dpo.py:compute_batch_loss`, chosen and rejected use "
        "separate φ weight vectors (potentially different lengths → different sums). "
        "The absolute scale cancels within each log-ratio but NOT across the "
        "chosen-vs-rejected comparison when lengths differ. "
        "This may cause length bias. Consider normalizing weights to sum=1 "
        "or documenting the current behavior as intentional."
    )
    report_lines.append("")
    report_lines.append(
        "**File**: `src/dmpo_loss.py:5` (docstring), `src/etadn_discount.py:56-70` (implementation)"
    )
    report_lines.append("")

all_pass = fail_count == 0
if all_pass:
    report_lines.append("All checks passed. Pipeline is ready for real data.")
else:
    report_lines.append(
        f"{fail_count} check(s) failed. See details above."
    )

report_text = "\n".join(report_lines) + "\n"
REPORT_PATH.write_text(report_text)
print(f"\nReport written to {REPORT_PATH}")
