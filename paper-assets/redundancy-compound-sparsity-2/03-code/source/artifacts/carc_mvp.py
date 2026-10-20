"""
CARC MVP validation: five measurements for EMA-guided sparsity routing on
reasoning traces.

Measurements:
  (a) MLP activation magnitude: redundant vs novel near-zero fraction
  (b) Perturbation@55%: redundant vs novel mean perturbation + r(EMA, pert)
  (c) EMA <-> surprisal correlation (Contribution A bridge)
  (d) Perplexity: two-tier (55%/40% by EMA) vs uniform 40%
  (e) Position-residualized correlations for (b) and (c)

Input:  DeepSeek-R1-Distill-Qwen-14B + calibrated thresholds JSON
Output: JSON results + verdict

Per chain, runs 4 forward passes:
  1) Baseline  — MLP outputs, KV->EMA, logits->surprisal, gate magnitudes
  2) Sparse@55 — MLP outputs
  3) Sparse@40 — MLP outputs + logits for PPL
  4) Two-tier  — logits for PPL (redundant@55%, novel@40% by EMA score)

Usage:
    python carc_mvp.py --thresholds thresholds.json --output results.json
    python carc_mvp.py --thresholds thresholds.json --dataset c4 --seq-len 2048
    python carc_mvp.py --thresholds thresholds.json --dry-run
"""

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import torch
import torch.nn.functional as F
from scipy import stats
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

from carc_utils import (
    EMAAnchorManager,
    compute_perturbation,
    load_eval_data,
    load_math_data,
    residualize,
    sparsify,
)

MODEL_ID = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"


def parse_args():
    p = argparse.ArgumentParser(
        description="CARC MVP: validate EMA-guided sparsity routing with 5 measurements."
    )
    p.add_argument("--model", default=MODEL_ID, help="HF model name or local path")
    p.add_argument("--thresholds", required=True, help="Calibrated thresholds JSON from carc_calibrate.py")
    p.add_argument("--output", default="carc_results.json", help="Output JSON path")
    p.add_argument("--num-samples", type=int, default=60, help="Number of chains/samples")
    p.add_argument("--max-new-tokens", type=int, default=2048, help="Max new tokens for reasoning generation")
    p.add_argument("--seq-len", type=int, default=2048, help="Sequence length (for non-math datasets)")
    p.add_argument("--dataset", default="math", choices=["math", "c4", "wikitext", "alpaca"])
    p.add_argument("--tau", type=float, default=0.7, help="EMA score threshold for redundant/novel split")
    p.add_argument("--per-head", dest="per_head", action="store_true", default=True,
                   help="Per-head EMA cosine (default)")
    p.add_argument("--no-per-head", dest="per_head", action="store_false",
                   help="Disable per-head EMA, use concatenated")
    p.add_argument("--dry-run", action="store_true", help="2 samples, 2 layers only")
    p.add_argument("--dtype", default="bf16", choices=["fp16", "bf16"])
    return p.parse_args()


# ---------------------------------------------------------------------------
# Hook managers
# ---------------------------------------------------------------------------

class MLPCapture:
    """
    Captures MLP outputs and optionally sparsifies MLP projection inputs.

    Modes:
        "baseline"       — record outputs + gate_proj near-zero fractions
        "sparse_55"      — sparsify at 55% threshold
        "sparse_40"      — sparsify at 40% threshold
        "sparse_twotier" — per-token routing: redundant@55%, novel@40%
    """

    def __init__(self, model, thresholds: dict, max_layers: int, tau: float = 0.7):
        self.thresholds = thresholds
        self.max_layers = max_layers
        self.tau = tau
        self._hooks: list = []
        self.mode = "baseline"
        self.outputs: Dict[int, torch.Tensor] = {}
        self.gate_near_zero: Dict[int, torch.Tensor] = {}
        self.token_ema_scores: Optional[torch.Tensor] = None

        for i in range(max_layers):
            mlp = model.model.layers[i].mlp
            self._hooks.append(mlp.register_forward_hook(self._out_hook(i)))
            for name in ("gate_proj", "up_proj", "down_proj"):
                mod = getattr(mlp, name)
                self._hooks.append(
                    mod.register_forward_pre_hook(self._sparse_hook(i, name))
                )

    def _out_hook(self, layer_idx: int):
        def fn(_module, _inp, out):
            self.outputs[layer_idx] = out.detach()
        return fn

    def _sparse_hook(self, layer_idx: int, component: str):
        def fn(_module, args):
            if self.mode == "baseline":
                if component == "gate_proj":
                    x = args[0].detach()
                    t40 = (
                        self.thresholds
                        .get(str(layer_idx), {})
                        .get(component, {})
                        .get("40")
                    )
                    if t40 is not None:
                        near_zero = (x.abs() < t40).float().mean(dim=-1)
                        self.gate_near_zero[layer_idx] = near_zero.cpu()
                return None

            if self.mode == "sparse_twotier":
                t55 = self.thresholds.get(str(layer_idx), {}).get(component, {}).get("55")
                t40 = self.thresholds.get(str(layer_idx), {}).get(component, {}).get("40")
                if t55 is None or t40 is None or self.token_ema_scores is None:
                    return None
                x = args[0]
                scores = self.token_ema_scores.to(x.device)
                redundant = (scores > self.tau).unsqueeze(-1)  # (batch, seq, 1)
                sparse_hi = x * (x.abs() > t55)
                sparse_lo = x * (x.abs() > t40)
                return (torch.where(redundant, sparse_hi, sparse_lo),)

            level = "55" if self.mode == "sparse_55" else "40"
            t = (
                self.thresholds
                .get(str(layer_idx), {})
                .get(component, {})
                .get(level)
            )
            if t is None:
                return None
            return (sparsify(args[0], t),)
        return fn

    def set_mode(self, mode: str, token_ema_scores: Optional[torch.Tensor] = None):
        self.mode = mode
        self.outputs.clear()
        self.gate_near_zero.clear()
        if token_ema_scores is not None:
            self.token_ema_scores = token_ema_scores
        elif mode != "sparse_twotier":
            self.token_ema_scores = None

    def remove(self):
        for h in self._hooks:
            h.remove()
        self._hooks.clear()


class KVCapture:
    """Captures raw K/V projection outputs (pre-RoPE) for EMA scoring."""

    def __init__(self, model, max_layers: int):
        self._hooks: list = []
        self.kv: Dict[int, list] = {}
        self.active = True

        for i in range(max_layers):
            attn = model.model.layers[i].self_attn
            self._hooks.append(attn.k_proj.register_forward_hook(self._hook(i, 0)))
            self._hooks.append(attn.v_proj.register_forward_hook(self._hook(i, 1)))

    def _hook(self, layer_idx: int, slot: int):
        def fn(_module, _inp, out):
            if not self.active:
                return
            self.kv.setdefault(layer_idx, [None, None])[slot] = out.detach()
        return fn

    def clear(self):
        self.kv.clear()

    def remove(self):
        for h in self._hooks:
            h.remove()
        self._hooks.clear()


# ---------------------------------------------------------------------------
# Judgment
# ---------------------------------------------------------------------------

def judge(r: float, diff: float) -> str:
    """
    Refined 2x2 decision matrix:
        |r| >= 0.4 AND diff >= 10%:
            PASS-Strong    if |r| > 0.5 AND diff >= 20%
            PASS-Suggestive otherwise
        |r| >= 0.4 AND diff <  10%  ->  DISCORDANT-B
        |r| <  0.4 AND diff >= 10%  ->  DISCORDANT-A
        both fail                   ->  FAIL
    """
    has_r = abs(r) >= 0.4
    has_d = diff >= 0.10
    if has_r and has_d:
        if abs(r) > 0.5 and diff >= 0.20:
            return "PASS-Strong"
        return "PASS-Suggestive"
    if has_r:
        return "DISCORDANT-B"
    if has_d:
        return "DISCORDANT-A"
    return "FAIL"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    dtype = torch.float16 if args.dtype == "fp16" else torch.bfloat16

    if args.dry_run:
        args.num_samples = 2
        print("[DRY RUN] 2 samples, 2 layers")

    thresholds = json.loads(Path(args.thresholds).read_text())
    print(f"Loaded thresholds for {len(thresholds)} layers")

    print(f"Loading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True
    )
    model.eval()

    num_layers = len(model.model.layers)
    max_layers = min(2 if args.dry_run else num_layers, len(thresholds))
    assert hasattr(model.model.layers[0].mlp, "gate_proj"), (
        f"Expected Qwen2-style MLP; got {type(model.model.layers[0].mlp)}"
    )

    num_kv_heads = getattr(model.config, "num_key_value_heads", None)
    per_head = args.per_head and num_kv_heads is not None
    print(f"EMA mode: {'per-head' if per_head else 'concatenated'}"
          f"{f' ({num_kv_heads} KV heads)' if per_head else ''}")

    # -----------------------------------------------------------------
    # Data loading / generation (no hooks installed yet)
    # -----------------------------------------------------------------
    if args.dataset == "math":
        print(f"Loading {args.num_samples} MATH problems for reasoning trace generation...")
        prompts = load_math_data(num_problems=args.num_samples, seed=42)

        print(f"Generating reasoning chains (max_new_tokens={args.max_new_tokens})...")
        chains: List[torch.Tensor] = []
        for prompt in tqdm(prompts, desc="Generating"):
            input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
            with torch.no_grad():
                output = model.generate(
                    input_ids,
                    max_new_tokens=args.max_new_tokens,
                    do_sample=True,
                    temperature=0.6,
                    top_p=0.95,
                )
            chains.append(output[0].cpu())
        samples = chains
        print(f"Generated {len(samples)} chains, lengths: "
              f"min={min(len(c) for c in samples)}, "
              f"max={max(len(c) for c in samples)}, "
              f"median={int(np.median([len(c) for c in samples]))}")
    else:
        split = "train" if args.dataset == "alpaca" else "validation"
        samples = load_eval_data(
            dataset_name=args.dataset,
            num_samples=args.num_samples,
            seq_len=args.seq_len,
            tokenizer=tokenizer,
            split=split,
        )

    print(f"Analyzing {len(samples)} samples, evaluating {max_layers} layers")

    # -----------------------------------------------------------------
    # Install hooks for analysis phase
    # -----------------------------------------------------------------
    mlp_cap = MLPCapture(model, thresholds, max_layers, tau=args.tau)
    kv_cap = KVCapture(model, max_layers)
    ema = EMAAnchorManager(
        gamma=0.9,
        num_kv_heads=num_kv_heads if per_head else None,
        per_head=per_head,
    )

    # -----------------------------------------------------------------
    # Accumulators
    # -----------------------------------------------------------------
    # Per-token records: (ema_score, p55, p40, layer_idx, token_position)
    records: List[tuple] = []
    # (c) EMA <-> surprisal: layer-averaged EMA per token
    all_token_avg_ema: List[float] = []
    all_token_surprisal: List[float] = []
    all_token_positions: List[int] = []
    # Chain-level stats
    chain_mean_ema: List[float] = []
    chain_mean_perturb: List[float] = []
    chain_mean_surprisal: List[float] = []
    chain_lag1_ema: List[float] = []
    chain_lag1_surprisal: List[float] = []
    # (a) Per-layer near-zero fractions
    layer_redun_nz: Dict[int, list] = {i: [] for i in range(max_layers)}
    layer_novel_nz: Dict[int, list] = {i: [] for i in range(max_layers)}
    # (b) Per-layer perturbation
    layer_redun_55: Dict[int, list] = {i: [] for i in range(max_layers)}
    layer_novel_55: Dict[int, list] = {i: [] for i in range(max_layers)}
    # (d) CE losses for PPL
    all_ce_uniform40: List[float] = []
    all_ce_twotier: List[float] = []

    for _sample_idx, token_ids in enumerate(tqdm(samples, desc="Analyzing")):
        input_ids = token_ids.unsqueeze(0).to(model.device)
        seq_len = input_ids.shape[1]
        ema.reset()

        # ---- Pass 1: baseline + KV capture + logits -> surprisal ----
        kv_cap.active = True
        kv_cap.clear()
        mlp_cap.set_mode("baseline")
        with torch.no_grad():
            outputs = model(input_ids, use_cache=False)
            logits = outputs.logits  # (1, seq_len, vocab_size)
        kv_cap.active = False

        # Surprisal: positions 1..seq_len-1
        log_probs = F.log_softmax(logits[:, :-1, :].float(), dim=-1)
        token_targets = input_ids[:, 1:]
        surprisal = -log_probs.gather(dim=-1, index=token_targets.unsqueeze(-1)).squeeze(-1)
        surprisal_np = surprisal[0].cpu().numpy()  # (seq_len-1,)
        del logits, log_probs, surprisal
        torch.cuda.empty_cache()

        base_out = {i: mlp_cap.outputs[i].cpu() for i in mlp_cap.outputs}
        gate_nz = {i: mlp_cap.gate_near_zero[i] for i in mlp_cap.gate_near_zero}

        kv_cpu = {}
        for i, pair in kv_cap.kv.items():
            if pair[0] is not None and pair[1] is not None:
                kv_cpu[i] = (pair[0].cpu(), pair[1].cpu())

        # EMA scores per layer
        layer_scores: Dict[int, torch.Tensor] = {}
        for li in range(max_layers):
            if li not in kv_cpu:
                continue
            k, v = kv_cpu[li]
            layer_scores[li] = ema.compute_scores(li, k, v)
        del kv_cpu
        torch.cuda.empty_cache()

        # Average EMA across layers per token
        valid_layers = [li for li in range(max_layers) if li in layer_scores]
        if valid_layers:
            stacked = torch.stack([layer_scores[li][0] for li in valid_layers])
            avg_ema_np = stacked.mean(dim=0).numpy()  # (seq_len,)
        else:
            avg_ema_np = np.zeros(seq_len)

        avg_ema_tensor = torch.from_numpy(avg_ema_np).unsqueeze(0).float()

        # ---- Pass 2: 55% sparsity ----
        mlp_cap.set_mode("sparse_55")
        with torch.no_grad():
            model(input_ids, use_cache=False)
        s55_out = {i: mlp_cap.outputs[i].cpu() for i in mlp_cap.outputs}

        # ---- Pass 3: 40% sparsity + logits for PPL ----
        mlp_cap.set_mode("sparse_40")
        with torch.no_grad():
            outputs_40 = model(input_ids, use_cache=False)
            logits_40 = outputs_40.logits.float()
        s40_out = {i: mlp_cap.outputs[i].cpu() for i in mlp_cap.outputs}

        lp_40 = F.log_softmax(logits_40[:, :-1, :], dim=-1)
        ce_40 = -lp_40.gather(dim=-1, index=token_targets.unsqueeze(-1)).squeeze(-1)
        all_ce_uniform40.append(ce_40.mean().item())
        del logits_40, lp_40, ce_40
        torch.cuda.empty_cache()

        # ---- Pass 4: two-tier sparsity + logits for PPL ----
        mlp_cap.set_mode("sparse_twotier", token_ema_scores=avg_ema_tensor)
        with torch.no_grad():
            outputs_tt = model(input_ids, use_cache=False)
            logits_tt = outputs_tt.logits.float()

        lp_tt = F.log_softmax(logits_tt[:, :-1, :], dim=-1)
        ce_tt = -lp_tt.gather(dim=-1, index=token_targets.unsqueeze(-1)).squeeze(-1)
        all_ce_twotier.append(ce_tt.mean().item())
        del logits_tt, lp_tt, ce_tt, avg_ema_tensor
        torch.cuda.empty_cache()

        # ---- Collect per-layer, per-token records ----
        chain_perturb_accum: List[float] = []

        for li in range(max_layers):
            if li not in base_out or li not in s55_out or li not in s40_out:
                continue
            if li not in layer_scores:
                continue

            p55 = compute_perturbation(s55_out[li], base_out[li])[0].numpy()
            p40 = compute_perturbation(s40_out[li], base_out[li])[0].numpy()
            s_arr = layer_scores[li][0].numpy()

            for t in range(len(s_arr)):
                records.append((float(s_arr[t]), float(p55[t]), float(p40[t]), li, t))

            chain_perturb_accum.extend(p55.tolist())

            mask_r = s_arr > args.tau
            mask_n = ~mask_r
            if mask_r.any():
                layer_redun_55[li].extend(p55[mask_r].tolist())
            if mask_n.any():
                layer_novel_55[li].extend(p55[mask_n].tolist())

            # (a) Near-zero fractions by redundancy
            if li in gate_nz:
                nz = gate_nz[li][0].numpy()
                if mask_r.any():
                    layer_redun_nz[li].extend(nz[mask_r].tolist())
                if mask_n.any():
                    layer_novel_nz[li].extend(nz[mask_n].tolist())

        # ---- Token-level EMA<->surprisal accumulation ----
        # avg_ema_np[1:] aligns with surprisal_np (both cover positions 1..seq_len-1)
        for t in range(len(surprisal_np)):
            all_token_avg_ema.append(float(avg_ema_np[t + 1]))
            all_token_surprisal.append(float(surprisal_np[t]))
            all_token_positions.append(t + 1)

        # ---- Chain-level stats ----
        chain_mean_ema.append(float(np.mean(avg_ema_np)))
        chain_mean_surprisal.append(float(np.mean(surprisal_np)))
        if chain_perturb_accum:
            chain_mean_perturb.append(float(np.mean(chain_perturb_accum)))
        else:
            chain_mean_perturb.append(0.0)

        # Lag-1 autocorrelation
        ema_aligned = avg_ema_np[1:]  # align with surprisal range
        if len(ema_aligned) > 2:
            chain_lag1_ema.append(float(np.corrcoef(ema_aligned[:-1], ema_aligned[1:])[0, 1]))
        if len(surprisal_np) > 2:
            chain_lag1_surprisal.append(float(np.corrcoef(surprisal_np[:-1], surprisal_np[1:])[0, 1]))

        del base_out, s55_out, s40_out, gate_nz, token_targets
        torch.cuda.empty_cache()

    mlp_cap.remove()
    kv_cap.remove()

    # ------------------------------------------------------------------
    # Aggregate statistics
    # ------------------------------------------------------------------
    if len(records) < 3:
        print("ERROR: too few records to compute statistics")
        return

    all_s = np.array([r[0] for r in records])
    all_p55 = np.array([r[1] for r in records])
    all_rec_pos = np.array([r[4] for r in records], dtype=np.float64)

    # (b) r(EMA, perturbation)
    pearson_r, pearson_p = stats.pearsonr(all_s, all_p55)
    spearman_r, spearman_p = stats.spearmanr(all_s, all_p55)

    redun_vals = [r[1] for r in records if r[0] > args.tau]
    novel_vals = [r[1] for r in records if r[0] <= args.tau]
    mean_r55 = float(np.mean(redun_vals)) if redun_vals else 0.0
    mean_n55 = float(np.mean(novel_vals)) if novel_vals else 0.0
    diff = mean_n55 - mean_r55

    # (c) r(EMA, -surprisal)
    arr_ema = np.array(all_token_avg_ema)
    arr_surp = np.array(all_token_surprisal)
    arr_pos = np.array(all_token_positions, dtype=np.float64)
    if len(arr_ema) > 2:
        r_ema_surp, p_ema_surp = stats.pearsonr(arr_ema, -arr_surp)
    else:
        r_ema_surp, p_ema_surp = 0.0, 1.0

    # (d) PPL
    ppl_uniform40 = math.exp(np.mean(all_ce_uniform40)) if all_ce_uniform40 else float("inf")
    ppl_twotier = math.exp(np.mean(all_ce_twotier)) if all_ce_twotier else float("inf")

    # (e) Position-residualized correlations
    if len(all_rec_pos) > 10:
        ema_resid = residualize(all_s, all_rec_pos)
        p55_resid = residualize(all_p55, all_rec_pos)
        resid_r_ema_pert, _ = stats.pearsonr(ema_resid, p55_resid)
    else:
        resid_r_ema_pert = 0.0

    if len(arr_pos) > 10:
        ema_avg_resid = residualize(arr_ema, arr_pos)
        surp_neg_resid = residualize(-arr_surp, arr_pos)
        resid_r_ema_surp, _ = stats.pearsonr(ema_avg_resid, surp_neg_resid)
    else:
        resid_r_ema_surp = 0.0

    # (a) Global near-zero fractions
    all_redun_nz = []
    all_novel_nz = []
    for li in range(max_layers):
        all_redun_nz.extend(layer_redun_nz[li])
        all_novel_nz.extend(layer_novel_nz[li])
    avg_redun_nz = float(np.mean(all_redun_nz)) if all_redun_nz else 0.0
    avg_novel_nz = float(np.mean(all_novel_nz)) if all_novel_nz else 0.0

    # Multi-chain: chain-level correlations
    chain_ema_arr = np.array(chain_mean_ema)
    chain_pert_arr = np.array(chain_mean_perturb)
    chain_surp_arr = np.array(chain_mean_surprisal)

    if len(chain_ema_arr) > 2:
        chain_r_ema_pert, _ = stats.pearsonr(chain_ema_arr, chain_pert_arr)
        chain_r_ema_surp, _ = stats.pearsonr(chain_ema_arr, -chain_surp_arr)
    else:
        chain_r_ema_pert, chain_r_ema_surp = 0.0, 0.0

    median_lag1_ema = float(np.median(chain_lag1_ema)) if chain_lag1_ema else 0.0
    median_lag1_surp = float(np.median(chain_lag1_surprisal)) if chain_lag1_surprisal else 0.0

    # ------------------------------------------------------------------
    # Per-layer breakdown
    # ------------------------------------------------------------------
    per_layer: Dict[str, dict] = {}
    for li in range(max_layers):
        rv = layer_redun_55[li]
        nv = layer_novel_55[li]
        if not rv or not nv:
            continue
        lrec = [(r[0], r[1]) for r in records if r[3] == li]
        if len(lrec) < 10:
            continue
        ls, lp = zip(*lrec)
        lr, _ = stats.pearsonr(ls, lp)

        entry = {
            "pearson_r": round(float(lr), 4),
            "mean_redundant_55": round(float(np.mean(rv)), 6),
            "mean_novel_55": round(float(np.mean(nv)), 6),
            "diff": round(float(np.mean(nv) - np.mean(rv)), 6),
            "n_redundant": len(rv),
            "n_novel": len(nv),
        }

        # (a) near-zero fractions
        rnz = layer_redun_nz[li]
        nnz = layer_novel_nz[li]
        if rnz and nnz:
            entry["redundant_near_zero_frac"] = round(float(np.mean(rnz)), 4)
            entry["novel_near_zero_frac"] = round(float(np.mean(nnz)), 4)

        per_layer[str(li)] = entry

    # ------------------------------------------------------------------
    # Verdict
    # ------------------------------------------------------------------
    verdict = judge(pearson_r, diff)

    # ------------------------------------------------------------------
    # Results
    # ------------------------------------------------------------------
    results = {
        "config": {
            "model": args.model,
            "dataset": args.dataset,
            "num_chains": len(samples),
            "max_new_tokens": args.max_new_tokens if args.dataset == "math" else None,
            "seq_len": args.seq_len if args.dataset != "math" else None,
            "tau": args.tau,
            "layers_evaluated": max_layers,
            "per_head": per_head,
        },
        "global": {
            "pearson_r_ema_perturbation": round(float(pearson_r), 4),
            "pearson_p_ema_perturbation": float(pearson_p),
            "spearman_r_ema_perturbation": round(float(spearman_r), 4),
            "spearman_p_ema_perturbation": float(spearman_p),
            "pearson_r_ema_surprisal": round(float(r_ema_surp), 4),
            "pearson_p_ema_surprisal": float(p_ema_surp),
            "position_residualized_r_ema_perturbation": round(float(resid_r_ema_pert), 4),
            "position_residualized_r_ema_surprisal": round(float(resid_r_ema_surp), 4),
            "chain_level_r_ema_perturbation": round(float(chain_r_ema_pert), 4),
            "chain_level_r_ema_surprisal": round(float(chain_r_ema_surp), 4),
            "mean_perturbation_redundant_55": round(mean_r55, 6),
            "mean_perturbation_novel_55": round(mean_n55, 6),
            "perturbation_diff": round(diff, 6),
            "perturbation_diff_pct": round(diff * 100, 2),
            "ppl_twotier": round(ppl_twotier, 2),
            "ppl_uniform40": round(ppl_uniform40, 2),
            "avg_redundant_near_zero_frac": round(avg_redun_nz, 4),
            "avg_novel_near_zero_frac": round(avg_novel_nz, 4),
            "median_lag1_autocorr_ema": round(median_lag1_ema, 4),
            "median_lag1_autocorr_surprisal": round(median_lag1_surp, 4),
            "n_redundant": len(redun_vals),
            "n_novel": len(novel_vals),
            "total_records": len(records),
        },
        "per_layer": per_layer,
        "verdict": verdict,
    }

    Path(args.output).write_text(json.dumps(results, indent=2))

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    W = 62
    print(f"\n{'=' * W}")
    print("CARC MVP Results — 5 Measurements")
    print(f"{'=' * W}")

    print(f"\n(a) MLP Activation Magnitudes (near-zero fraction)")
    print(f"    Redundant near-zero: {avg_redun_nz:.4f}")
    print(f"    Novel near-zero:     {avg_novel_nz:.4f}")
    if avg_novel_nz > 0:
        ratio = avg_redun_nz / max(avg_novel_nz, 1e-8)
        print(f"    Ratio (redundant/novel): {ratio:.2f}x")

    print(f"\n(b) Perturbation@55% (redundant vs novel)")
    print(f"    Pearson  r(EMA, perturbation) = {pearson_r:+.4f}  (p={pearson_p:.2e})")
    print(f"    Spearman r(EMA, perturbation) = {spearman_r:+.4f}  (p={spearman_p:.2e})")
    print(f"    Mean perturbation: redundant@55% = {mean_r55:.6f}")
    print(f"                       novel@55%     = {mean_n55:.6f}")
    print(f"    Perturbation diff = {diff:.4f} ({diff * 100:.1f}%)")
    print(f"    Tokens: {len(redun_vals)} redundant, {len(novel_vals)} novel  (tau={args.tau})")

    print(f"\n(c) EMA <-> Surprisal Correlation")
    print(f"    Pearson r(EMA, -surprisal) = {r_ema_surp:+.4f}  (p={p_ema_surp:.2e})")

    print(f"\n(d) Perplexity: Two-tier vs Uniform")
    print(f"    PPL two-tier (55%/40%): {ppl_twotier:.2f}")
    print(f"    PPL uniform 40%:        {ppl_uniform40:.2f}")
    ppl_delta = ppl_twotier - ppl_uniform40
    print(f"    Delta PPL: {ppl_delta:+.2f} ({'two-tier better' if ppl_delta < 0 else 'uniform better'})")

    print(f"\n(e) Position-residualized Correlations")
    print(f"    Partial r(EMA, perturbation | pos) = {resid_r_ema_pert:+.4f}")
    print(f"    Partial r(EMA, -surprisal | pos)   = {resid_r_ema_surp:+.4f}")

    print(f"\nMulti-chain Statistics ({len(samples)} chains)")
    print(f"    Chain-level r(EMA, perturbation): {chain_r_ema_pert:+.4f}")
    print(f"    Chain-level r(EMA, -surprisal):   {chain_r_ema_surp:+.4f}")
    print(f"    Median lag-1 autocorr (EMA):       {median_lag1_ema:.4f}")
    print(f"    Median lag-1 autocorr (surprisal): {median_lag1_surp:.4f}")

    print(f"\n{'—' * W}")
    print(f"Verdict: {verdict}")
    print(f"  |r| >= 0.4 ? {'YES' if abs(pearson_r) >= 0.4 else 'NO'} ({abs(pearson_r):.4f})")
    print(f"  diff >= 10%? {'YES' if diff >= 0.10 else 'NO'} ({diff * 100:.1f}%)")
    if verdict.startswith("PASS"):
        print(f"  (Strong requires |r|>0.5 AND diff>=20%)")
    print(f"{'=' * W}")
    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
