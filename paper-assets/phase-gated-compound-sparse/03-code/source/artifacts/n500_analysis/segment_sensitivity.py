#!/usr/bin/env python3
"""
segment_sensitivity.py — Segmentation robustness analysis for PACS.

Recomputes D = II_lowest - II_highest under tercile/quartile/quintile
for all 16 conditions to verify the phase-dependent effect is not an
artifact of the tercile split.

Usage:
    python segment_sensitivity.py --model deepseek --gpu 0
    python segment_sensitivity.py --model qwen --gpu 2
    python segment_sensitivity.py --merge   # combine partial results
"""

import json, os, sys, logging, time, argparse, math
from pathlib import Path
from collections import defaultdict
from datetime import datetime

import numpy as np
from scipy import stats

BASE = Path("/root/autodl-tmp/pacs")
sys.path.insert(0, str(BASE))

import torch
import torch.nn.functional as F

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("seg_sens")

SEED = 42
B_BOOT = 10000
ALPHA = 0.05

MODELS = {
    "deepseek": str(BASE / "checkpoints/DeepSeek-R1-Distill-Qwen-7B"),
    "qwen": "/root/autodl-tmp/models/Qwen2.5-7B-Instruct",
}
MODEL_SHORT = {"deepseek": "ds", "qwen": "qw"}
MASKING_TYPES = ["imp", "rand"]
SPARSITY_LABELS = ["s015", "s020", "s025", "s030"]
SPARSITY_VALUES = {"s015": 0.15, "s020": 0.20, "s025": 0.25, "s030": 0.30}
SEG_GROUPS = [3, 4, 5]
SEG_NAMES = {3: "tercile", 4: "quartile", 5: "quintile"}

OUT_DIR = BASE / "analysis_output"


# ── Data ──────────────────────────────────────────────────────────────

def load_math500():
    with open(BASE / "data" / "math500.json") as f:
        raw = json.load(f)
    if isinstance(raw, dict) and "data" in raw:
        raw = raw["data"]
    return raw


def load_stored_sparsity(model_short: str) -> list:
    dname = f"profiling_output_n500_bf16_{model_short}_imp_s015"
    fpath = BASE / dname / "profiling_results.json"
    with open(fpath) as f:
        data = json.load(f)
    return data["diagnostics"]["per_problem_sparsity"]


def load_stored_tercile_ii(model_short: str, masking: str, slabel: str) -> list:
    dname = f"profiling_output_n500_bf16_{model_short}_{masking}_{slabel}"
    fpath = BASE / dname / "profiling_results.json"
    with open(fpath) as f:
        data = json.load(f)
    ppi = data.get("per_problem_ii", {})
    slevel = str(SPARSITY_VALUES[slabel])
    return ppi.get(slevel, [])


# ── Model ─────────────────────────────────────────────────────────────

def load_model(model_path: str, device: str):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map=device,
        trust_remote_code=True,
        attn_implementation="eager",
    )
    model.eval()
    return model, tok


# ── Forward passes ────────────────────────────────────────────────────

@torch.no_grad()
def dense_forward_with_importance(model, tokenizer, input_ids, device):
    """Dense forward → (per_token_ce, head_importance, kv_importance)."""
    from pacs.profiling.interaction_index import InteractionIndexCalculator
    ii_calc = InteractionIndexCalculator(model, tokenizer, device=device)
    ce, h_imp, kv_imp = ii_calc.compute_dense_forward_with_importance(input_ids)
    return ce, h_imp, kv_imp, ii_calc


@torch.no_grad()
def sparse_forward_ce(model, input_ids, attn_head_mask=None, kv_mask=None):
    """Forward pass with optional head/KV masks → full per-token CE."""
    from pacs.profiling.interaction_index import _HeadMaskHook

    attention_mask = torch.ones_like(input_ids)
    if kv_mask is not None:
        kv_dev = kv_mask.to(input_ids.device)
        flat = kv_dev.min(dim=0).values if kv_dev.dim() == 2 else kv_dev
        attention_mask = attention_mask * flat.unsqueeze(0)

    hook = None
    if attn_head_mask is not None:
        hook = _HeadMaskHook(model, attn_head_mask)
    try:
        out = model(input_ids=input_ids, attention_mask=attention_mask)
    finally:
        if hook is not None:
            hook.remove()

    logits = out.logits[0]
    labels = input_ids[0]
    return F.cross_entropy(logits[:-1].float(), labels[1:], reduction="none")


# ── Segmentation + II ─────────────────────────────────────────────────

def segment_by_sparsity(sparsity_vals, n_groups, prompt_len):
    """Quantile-based grouping. Returns {group_idx: [full_seq_positions]}."""
    sv = np.array(sparsity_vals)
    if len(sv) < n_groups:
        return {}
    quantiles = np.linspace(0, 1, n_groups + 1)[1:-1]
    boundaries = np.quantile(sv, quantiles)
    assignments = np.digitize(sv, boundaries)
    groups = defaultdict(list)
    for i, g in enumerate(assignments):
        groups[g].append(prompt_len + i)
    return dict(groups)


def ppl_from_ce(ce, token_indices, seq_len):
    idx = torch.tensor(
        [i - 1 for i in token_indices if 0 < i < seq_len],
        device=ce.device,
    )
    if idx.numel() == 0:
        return float("nan")
    sel = ce[idx]
    valid = ~(torch.isnan(sel) | torch.isinf(sel))
    if valid.sum() == 0:
        return float("nan")
    return torch.exp(sel[valid].mean()).item()


def compute_ii(ppl_d, ppl_a, ppl_k, ppl_b):
    if ppl_d <= 0 or any(math.isnan(x) for x in [ppl_d, ppl_a, ppl_k, ppl_b]):
        return None
    return ppl_b / ppl_d - ppl_a / ppl_d - ppl_k / ppl_d + 1


def phase_ii(ce_d, ce_a, ce_k, ce_b, ti, seq_len):
    """II for a specific token group."""
    return compute_ii(
        ppl_from_ce(ce_d, ti, seq_len),
        ppl_from_ce(ce_a, ti, seq_len),
        ppl_from_ce(ce_k, ti, seq_len),
        ppl_from_ce(ce_b, ti, seq_len),
    )


# ── Statistics ────────────────────────────────────────────────────────

def bootstrap_median_ci(arr, B=B_BOOT, alpha=ALPHA, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(arr)
    meds = np.array([
        np.median(rng.choice(arr, size=n, replace=True)) for _ in range(B)
    ])
    return (
        float(np.percentile(meds, 100 * alpha / 2)),
        float(np.percentile(meds, 100 * (1 - alpha / 2))),
    )


def condition_stats(d_list):
    valid = np.array([v for v in d_list if v is not None and not np.isnan(v)])
    n = len(valid)
    if n < 5:
        return dict(n=n, median_D=float("nan"), ci_low=float("nan"),
                    ci_high=float("nan"), wilcoxon_p=float("nan"))
    med = float(np.median(valid))
    ci_lo, ci_hi = bootstrap_median_ci(valid)
    nonzero = valid[valid != 0]
    if len(nonzero) >= 5:
        _, p = stats.wilcoxon(nonzero, alternative="two-sided")
        wp = float(p)
    else:
        wp = float("nan")
    return dict(n=n, median_D=med, ci_low=ci_lo, ci_high=ci_hi, wilcoxon_p=wp)


# ── Main processing ──────────────────────────────────────────────────

def process_model(model_name: str, gpu_id: int):
    device = f"cuda:{gpu_id}"
    mshort = MODEL_SHORT[model_name]

    log.info("Loading model %s on %s", model_name, device)
    model, tok = load_model(MODELS[model_name], device)

    log.info("Loading data")
    data = load_math500()
    stored_sp = load_stored_sparsity(mshort)
    sp_by_id = {e["problem_id"]: e for e in stored_sp}

    from pacs.profiling.interaction_index import InteractionIndexCalculator
    ii_calc = InteractionIndexCalculator(model, tok, device=device)
    num_layers, num_heads = ii_calc._get_model_dims()

    # {(masking, slabel, seg_name): [D per problem]}
    all_diffs = defaultdict(list)
    # {(masking, slabel): [(ii_low_terc, ii_high_terc)]} for validation
    tercile_check = defaultdict(list)

    n_problems = len(data)
    t0 = time.time()

    for pidx, item in enumerate(data):
        problem_text = item.get("problem", item.get("question", ""))
        problem_id = item.get("unique_id", item.get("id", str(pidx)))

        # ── Generate ──
        prompt = (
            f"Solve the following math problem step by step.\n\n"
            f"Problem: {problem_text}\n\nSolution:"
        )
        inputs = tok(prompt, return_tensors="pt").to(device)
        prompt_len = inputs["input_ids"].shape[1]

        with torch.no_grad():
            gen_out = model.generate(
                **inputs, max_new_tokens=2048, do_sample=False,
            )
        full_ids = gen_out if gen_out.dim() == 2 else gen_out.unsqueeze(0)
        seq_len = full_ids.shape[1]
        n_gen = seq_len - prompt_len

        # ── Stored sparsity ──
        sp_entry = sp_by_id.get(problem_id)
        if sp_entry is None and pidx < len(stored_sp):
            sp_entry = stored_sp[pidx]
        if sp_entry is None or len(sp_entry.get("sparsity_values", [])) == 0:
            for mk in MASKING_TYPES:
                for sl in SPARSITY_LABELS:
                    for ng in SEG_GROUPS:
                        all_diffs[(mk, sl, SEG_NAMES[ng])].append(None)
            continue

        sv = sp_entry["sparsity_values"]
        n_use = min(len(sv), n_gen)
        sv = sv[:n_use]

        if n_use < 6:
            for mk in MASKING_TYPES:
                for sl in SPARSITY_LABELS:
                    for ng in SEG_GROUPS:
                        all_diffs[(mk, sl, SEG_NAMES[ng])].append(None)
            continue

        # ── Dense forward (shared) ──
        ce_dense, head_imp, kv_imp = ii_calc.compute_dense_forward_with_importance(
            full_ids
        )

        # ── Segmentations (shared) ──
        segs = {}
        for ng in SEG_GROUPS:
            segs[ng] = segment_by_sparsity(sv, ng, prompt_len)

        # ── Per condition: masks + sparse forwards ──
        for mk in MASKING_TYPES:
            use_imp = mk == "imp"
            for sl_idx, sl in enumerate(SPARSITY_LABELS):
                level = SPARSITY_VALUES[sl]

                # Deterministic seed for random masking
                if not use_imp:
                    torch.manual_seed(SEED + pidx * 100 + sl_idx)

                h_imp = head_imp if use_imp else None
                k_imp = kv_imp if use_imp else None

                attn_mask = InteractionIndexCalculator._select_heads_to_mask(
                    num_layers, num_heads, level, importance=h_imp,
                )
                kv_m = InteractionIndexCalculator._select_kv_to_evict(
                    seq_len, level, importance=k_imp,
                )

                ce_attn = sparse_forward_ce(
                    model, full_ids, attn_head_mask=attn_mask,
                )
                ce_kv = sparse_forward_ce(
                    model, full_ids, kv_mask=kv_m,
                )
                ce_both = sparse_forward_ce(
                    model, full_ids, attn_head_mask=attn_mask, kv_mask=kv_m,
                )

                for ng in SEG_GROUPS:
                    groups = segs[ng]
                    g_low = 0
                    g_high = ng - 1

                    if g_low not in groups or g_high not in groups:
                        all_diffs[(mk, sl, SEG_NAMES[ng])].append(None)
                        continue

                    ii_lo = phase_ii(ce_dense, ce_attn, ce_kv, ce_both,
                                     groups[g_low], seq_len)
                    ii_hi = phase_ii(ce_dense, ce_attn, ce_kv, ce_both,
                                     groups[g_high], seq_len)

                    if ii_lo is not None and ii_hi is not None:
                        d_val = ii_lo - ii_hi
                        all_diffs[(mk, sl, SEG_NAMES[ng])].append(d_val)
                        if ng == 3:
                            tercile_check[(mk, sl)].append(
                                (ii_lo, ii_hi, d_val)
                            )
                    else:
                        all_diffs[(mk, sl, SEG_NAMES[ng])].append(None)

        if (pidx + 1) % 25 == 0:
            elapsed = time.time() - t0
            rate = (pidx + 1) / elapsed
            eta = (n_problems - pidx - 1) / rate
            log.info(
                "[%s] %d/%d  (%.1f prob/min, ETA %.0f min)",
                model_name, pidx + 1, n_problems, rate * 60, eta / 60,
            )

    elapsed = time.time() - t0
    log.info("[%s] Done in %.1f min", model_name, elapsed / 60)

    # ── Validation: compare fresh tercile with stored ──
    if True:
        log.info("── Tercile validation (importance masking) ──")
        for sl in SPARSITY_LABELS:
            stored = load_stored_tercile_ii(mshort, "imp", sl)
            fresh = tercile_check.get(("imp", sl), [])
            if not stored or not fresh:
                continue
            stored_d = [
                p["ii_low"] - p["ii_high"]
                for p in stored
                if p.get("ii_low") is not None and p.get("ii_high") is not None
            ]
            fresh_d = [t[2] for t in fresh if t[2] is not None]
            if stored_d and fresh_d:
                s_med = np.median(stored_d)
                f_med = np.median(fresh_d)
                log.info(
                    "  %s imp_%s: stored median=%.4f, fresh median=%.4f, "
                    "diff=%.6f, n_stored=%d, n_fresh=%d",
                    model_name, sl, s_med, f_med, abs(s_med - f_med),
                    len(stored_d), len(fresh_d),
                )

    # ── Compute stats ──
    results = {}
    for (mk, sl, seg), diffs in all_diffs.items():
        key = f"{model_name}|{mk}|{sl}|{seg}"
        results[key] = condition_stats(diffs)

    return results


# ── Output ────────────────────────────────────────────────────────────

def merge_and_output(all_results: dict, args):
    OUT_DIR.mkdir(exist_ok=True)
    n_tests = len(all_results)

    rows = []
    for key, s in sorted(all_results.items()):
        parts = key.split("|")
        model_name, mk, sl, seg = parts
        bonf_p = min(s["wilcoxon_p"] * n_tests, 1.0) if not math.isnan(s["wilcoxon_p"]) else float("nan")
        sig = "yes" if (not math.isnan(bonf_p) and bonf_p < 0.05) else "no"
        rows.append(dict(
            model=model_name, masking=mk, sparsity=sl, segmentation=seg,
            n=s["n"], median_D=round(s["median_D"], 6),
            ci_low=round(s["ci_low"], 6), ci_high=round(s["ci_high"], 6),
            wilcoxon_p=s["wilcoxon_p"], bonf_p=bonf_p, significant=sig,
        ))

    # JSON
    jpath = OUT_DIR / "segmentation_sensitivity.json"
    with open(jpath, "w") as f:
        json.dump(rows, f, indent=2)
    log.info("Saved %s", jpath)

    # CSV
    cpath = OUT_DIR / "segmentation_sensitivity.csv"
    cols = ["model", "masking", "sparsity", "segmentation", "n",
            "median_D", "ci_low", "ci_high", "wilcoxon_p", "bonf_p", "significant"]
    with open(cpath, "w") as f:
        f.write(",".join(cols) + "\n")
        for r in rows:
            vals = []
            for c in cols:
                v = r[c]
                if isinstance(v, float):
                    if math.isnan(v):
                        vals.append("NaN")
                    else:
                        vals.append(f"{v:.6e}" if c.endswith("_p") else f"{v:.6f}")
                else:
                    vals.append(str(v))
            f.write(",".join(vals) + "\n")
    log.info("Saved %s", cpath)

    # Markdown table
    md_lines = [
        "# Segmentation Sensitivity Analysis",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "D = II(lowest sparsity phase) − II(highest sparsity phase)",
        "",
        "Bonferroni correction over {} tests (α = 0.05).".format(n_tests),
        "",
    ]

    for model_name in ["deepseek", "qwen"]:
        md_lines.append(f"## {model_name.title()}")
        md_lines.append("")
        md_lines.append(
            "| Masking | Sparsity | Seg | n | Median D | 95% CI | p (Wilcoxon) | p (Bonf) | Sig |"
        )
        md_lines.append(
            "|---------|----------|-----|---|----------|--------|--------------|----------|-----|"
        )
        for r in rows:
            if r["model"] != model_name:
                continue
            ci = f"[{r['ci_low']:.4f}, {r['ci_high']:.4f}]"
            wp = f"{r['wilcoxon_p']:.2e}" if not math.isnan(r["wilcoxon_p"]) else "—"
            bp = f"{r['bonf_p']:.2e}" if not math.isnan(r["bonf_p"]) else "—"
            sig = "**✓**" if r["significant"] == "yes" else "✗"
            md_lines.append(
                f"| {r['masking']} | {r['sparsity']} | {r['segmentation']} | "
                f"{r['n']} | {r['median_D']:+.4f} | {ci} | {wp} | {bp} | {sig} |"
            )
        md_lines.append("")

    # Summary
    md_lines.append("## Summary")
    md_lines.append("")
    for seg in ["tercile", "quartile", "quintile"]:
        seg_rows = [r for r in rows if r["segmentation"] == seg]
        n_sig = sum(1 for r in seg_rows if r["significant"] == "yes")
        md_lines.append(f"- **{seg.title()}**: {n_sig}/{len(seg_rows)} conditions significant")
    md_lines.append("")

    md_path = OUT_DIR / "segmentation_sensitivity.md"
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))
    log.info("Saved %s", md_path)

    return md_lines


# ── CLI ───────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", choices=["deepseek", "qwen", "all"], default="all")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--merge", action="store_true",
                   help="Merge partial results from separate model runs")
    return p.parse_args()


def main():
    args = parse_args()
    torch.manual_seed(SEED)

    if args.merge:
        # Merge partial results
        combined = {}
        for mname in ["deepseek", "qwen"]:
            ppath = OUT_DIR / f"seg_sens_partial_{mname}.json"
            if ppath.exists():
                with open(ppath) as f:
                    combined.update(json.load(f))
                log.info("Loaded partial results for %s (%d entries)", mname,
                         sum(1 for k in combined if k.startswith(mname)))
        if combined:
            merge_and_output(combined, args)
        else:
            log.error("No partial results found")
        return

    models_to_run = [args.model] if args.model != "all" else ["deepseek", "qwen"]

    all_results = {}
    for mname in models_to_run:
        results = process_model(mname, args.gpu)
        all_results.update(results)

        # Save partial results
        OUT_DIR.mkdir(exist_ok=True)
        ppath = OUT_DIR / f"seg_sens_partial_{mname}.json"
        with open(ppath, "w") as f:
            json.dump(results, f, indent=2)
        log.info("Saved partial: %s", ppath)

        # Free GPU memory before next model
        import gc
        gc.collect()
        torch.cuda.empty_cache()

    if len(models_to_run) == 2 or args.merge:
        merge_and_output(all_results, args)


if __name__ == "__main__":
    main()
