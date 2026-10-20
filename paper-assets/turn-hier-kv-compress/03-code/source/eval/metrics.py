"""Metric computation for TurnKV evaluation — KIRR, perplexity, and summary statistics."""

from __future__ import annotations

import re
from collections import defaultdict
from typing import TYPE_CHECKING, Dict, List, Tuple

if TYPE_CHECKING:
    import torch

from .config import MVPThresholds


def check_info_retained(generated_text: str, expected_answer: str) -> bool:
    """Exact substring match, case-insensitive, collapsing whitespace."""

    def _norm(s: str) -> str:
        return re.sub(r"\s+", " ", s.strip().lower())

    return _norm(expected_answer) in _norm(generated_text)


def compute_perplexity(
    model: "torch.nn.Module",
    tokenizer,
    input_ids: "torch.Tensor",
    target_start_idx: int,
) -> float:
    """Compute perplexity on continuation tokens using (possibly compressed) KV cache.

    Two-step approach so KV cache compression actually affects the result:
    1. Forward prefix tokens → build KV cache (press hook compresses it)
    2. Forward target tokens with compressed past_key_values → measure loss
    """
    import torch
    import torch.nn.functional as F

    prefix_ids = input_ids[:, :target_start_idx]
    target_ids = input_ids[:, target_start_idx:]

    if target_ids.shape[1] < 2:
        return 0.0

    with torch.no_grad():
        prefix_out = model(prefix_ids, use_cache=True)
        past_kv = prefix_out.past_key_values

        target_out = model(target_ids, past_key_values=past_kv)
        logits = target_out.logits

    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = target_ids[:, 1:].contiguous()
    loss = F.cross_entropy(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1),
    )
    return loss.exp().item()


def compute_kirr(
    results: List[dict],
) -> Dict[str, Dict[Tuple[str, float], dict]]:
    """Aggregate per-info retention booleans into KIRR, grouped by case_type.

    Each dict in *results* must have keys: case_type, method, compression_ratio,
    retained (bool).

    Returns::

        {case_type: {(method, cr): {"kirr": float, "n": int, "retained": int}}}
    """
    groups: Dict[str, Dict[Tuple[str, float], Dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: {"retained": 0, "total": 0})
    )
    for r in results:
        key = (r["method"], r["compression_ratio"])
        ct = r["case_type"]
        groups[ct][key]["total"] += 1
        if r["retained"]:
            groups[ct][key]["retained"] += 1

    out: Dict[str, Dict[Tuple[str, float], dict]] = {}
    for ct, methods in groups.items():
        out[ct] = {}
        for key, counts in methods.items():
            out[ct][key] = {
                "kirr": counts["retained"] / counts["total"] if counts["total"] else 0.0,
                "n": counts["total"],
                "retained": counts["retained"],
            }
    return out


def _mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def compute_summary(results_df: List[dict], compression_ratios: List[float]) -> dict:
    """Generate full summary with MVP verdict from per-trace result rows.

    *results_df* is the list of row-dicts written to the CSV (one row per
    trace x method x compression_ratio).
    """
    thresholds = MVPThresholds()
    summary: dict = {}

    for cr in compression_ratios:
        cr_key = f"compression_ratio_{cr}"
        summary[cr_key] = {}

        for case_type in ["standard", "adversarial", "overall"]:
            subset = [
                r for r in results_df
                if case_type == "overall" or r["case_type"] == case_type
            ]
            if not subset:
                continue

            group: dict = {}

            # Full baseline (compression_ratio == 0.0)
            full_rows = [r for r in subset if r["method"] == "full"]
            if full_rows:
                group["full"] = {
                    "kirr_mean": round(_mean([r["kirr"] for r in full_rows]), 4),
                    "ppl_mean": round(_mean([r["ppl_full"] for r in full_rows]), 4),
                }

            for method in ["uniform_ea", "turnkv"]:
                m_rows = [
                    r for r in subset
                    if r["method"] == method and r["compression_ratio"] == cr
                ]
                if m_rows:
                    group[method] = {
                        "kirr_mean": round(_mean([r["kirr"] for r in m_rows]), 4),
                        "ppl_mean": round(_mean([r["ppl_compressed"] for r in m_rows]), 4),
                    }

            if "turnkv" in group and "uniform_ea" in group:
                kirr_diff = (
                    group["turnkv"]["kirr_mean"] - group["uniform_ea"]["kirr_mean"]
                ) * 100
                ea_ppl = group["uniform_ea"]["ppl_mean"]
                ppl_ratio = (
                    group["turnkv"]["ppl_mean"] / ea_ppl if ea_ppl > 0 else float("inf")
                )
                group["kirr_diff_pp"] = round(kirr_diff, 1)
                group["ppl_ratio"] = round(ppl_ratio, 4)

            summary[cr_key][case_type] = group

    # ---- MVP verdict ----
    kirr_pass_any = False
    ppl_pass_any = False
    full_pass_any = False
    all_below_kill = True

    for cr in compression_ratios:
        cr_key = f"compression_ratio_{cr}"
        overall = summary.get(cr_key, {}).get("overall", {})
        kirr_diff = overall.get("kirr_diff_pp", 0)
        turnkv_kirr = overall.get("turnkv", {}).get("kirr_mean", 0)
        ppl_r = overall.get("ppl_ratio", float("inf"))

        kirr_ok = (
            kirr_diff >= thresholds.kirr_diff_pass_pp
            and turnkv_kirr >= thresholds.kirr_min_pass
        )
        ppl_ok = ppl_r <= thresholds.ppl_ratio_max

        if kirr_ok:
            kirr_pass_any = True
        if ppl_ok:
            ppl_pass_any = True
        if kirr_ok and ppl_ok:
            full_pass_any = True
        if kirr_diff >= thresholds.kirr_diff_kill_pp:
            all_below_kill = False

    if full_pass_any:
        verdict = "PASS"
    elif all_below_kill:
        verdict = "KILL"
    else:
        verdict = "INCONCLUSIVE"

    summary["mvp_verdict"] = {
        "kirr_pass": kirr_pass_any,
        "ppl_pass": ppl_pass_any,
        "overall": verdict,
    }
    return summary
