"""W2: unconstrained greedy & MCKP baselines for Yi-1.5 / Llama / Mistral / Gemma-2.

Reads each model's hires bf16 2bit-only profile, runs unconstrained allocation
(no cardinality limit on 2-bit heads), patches per-head quantization, and
evaluates PPL on calibration_hires.json (64 seq x 2048 tok).

Since the hires profiles only contain 2-bit deltas, the per-head Pareto
action set is {full=16, quant=2}; budget=0.25 implies ~85.7% heads at 2-bit.
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import gc
import json
import math
import time
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

from solver import solve_mckp, enforce_monotonicity
from eval_ppl import patch_attention, restore_attention
from run_gemma2_full_pipeline import patch_attention_gemma2


MODELS = [
    {
        "name": "Yi-1.5-9B",
        "path": "/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B",
        "profiles": "/root/ratekv/yi15_hires_bf16_2bitonly_profiles.json",
        "patch": "standard",
        "prepend_bos": False,
    },
    {
        "name": "Llama-3.1-8B",
        "path": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B",
        "profiles": "/root/ratekv/llama_hires_bf16_2bitonly_profiles.json",
        "patch": "standard",
        "prepend_bos": False,
    },
    {
        "name": "Mistral-7B-v0.3",
        "path": "/root/autodl-tmp/models/Mistral-7B-v0.3",
        "profiles": "/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json",
        "patch": "standard",
        "prepend_bos": False,
    },
    {
        "name": "Gemma-2-9B",
        "path": "/root/autodl-tmp/.hf_cache/google/gemma-2-9b",
        "profiles": "/root/ratekv/gemma2_hires_bf16_2bitonly_profiles.json",
        "patch": "gemma2",
        "prepend_bos": True,
    },
]


CALIB_PATH = "/root/ratekv/calibration_hires.json"
DEVICE = "cuda:0"
BUDGET = 0.25
NUM_SAMPLES = 64
SEQ_LEN = 2048
BATCH_SIZE = 2
BIT_OPTIONS = [2, 4, 8, 16]


def load_calibration(tokenizer, path, num_samples, seq_len, device, prepend_bos):
    with open(path) as f:
        samples = json.load(f)
    bos_id = tokenizer.bos_token_id if prepend_bos else None
    if prepend_bos and bos_id is None:
        raise RuntimeError("BOS requested but tokenizer has no BOS token id")
    target_len = seq_len - 1 if prepend_bos else seq_len
    all_ids = []
    for s in samples:
        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
        if len(tokens) >= target_len:
            if prepend_bos:
                all_ids.append([bos_id] + tokens[:target_len])
            else:
                all_ids.append(tokens[:target_len])
        if len(all_ids) >= num_samples:
            break
    if not all_ids:
        raise RuntimeError(f"No calibration seqs with >= {target_len} tokens")
    return torch.tensor(all_ids, dtype=torch.long, device=device)


def compute_ppl(model, input_ids, seq_len, batch_size, device):
    total_loss = 0.0
    total_tokens = 0
    n = input_ids.shape[0]
    with torch.no_grad():
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            batch = input_ids[start:end]
            outputs = model(
                batch, use_cache=False,
                cache_position=torch.arange(seq_len, device=device),
            )
            shift_logits = outputs.logits[:, :-1].contiguous()
            shift_labels = batch[:, 1:].contiguous()
            loss = F.cross_entropy(
                shift_logits.float().view(-1, shift_logits.shape[-1]),
                shift_labels.view(-1),
                reduction="sum",
            )
            total_loss += loss.item()
            total_tokens += shift_labels.numel()
            del outputs, shift_logits, loss
            torch.cuda.empty_cache()
    return math.exp(total_loss / total_tokens)


def available_bits_per_head(profile_entry, bit_options):
    """Return sorted list of bits available in this head's quantization profile (always includes 16)."""
    qdata = profile_entry.get("quantization", {})
    avail = {16}
    for b in bit_options:
        if b == 16:
            continue
        for key in (str(b), str(float(b))):
            if key in qdata:
                avail.add(b)
                break
    return sorted(avail)


def unconstrained_greedy(profiles, budget, bit_options=BIT_OPTIONS):
    """Greedy downgrade with no cardinality constraint, robust to missing bits.

    For each head, only the bits actually present in the profile (plus 16) are
    candidates. Marginal cost = (delta_lower - delta_current) / (bits_current - bits_lower).
    Tie-break: smallest delta_lower.
    """
    heads = []
    for l_str in sorted(profiles.keys(), key=lambda x: int(x)):
        for h_str in sorted(profiles[l_str].keys(), key=lambda x: int(x)):
            l, h = int(l_str), int(h_str)
            entry = profiles[l_str][h_str]
            dmap = {16: 0.0}
            qdata = entry.get("quantization", {})
            for b in bit_options:
                if b == 16:
                    continue
                for key in (str(b), str(float(b))):
                    if key in qdata:
                        dmap[b] = float(qdata[key])
                        break
            avail = sorted(dmap.keys())  # ascending
            heads.append((l, h, dmap, avail))

    n_heads = len(heads)
    max_bits = max(bit_options)
    allocation = [max_bits] * n_heads
    target_mem = budget * n_heads * max_bits

    while sum(allocation) > target_mem + 1e-9:
        best_head = None
        best_next = None
        best_eff = float("inf")
        for i, (l, h, dmap, avail) in enumerate(heads):
            cur = allocation[i]
            # candidate next bits = all available bits < cur
            cand = [b for b in avail if b < cur]
            if not cand:
                continue
            cur_d = dmap.get(cur, 0.0)
            for nb in cand:
                nb_d = dmap[nb]
                bits_saved = cur - nb
                eff = (nb_d - cur_d) / bits_saved
                if eff < best_eff - 1e-15:
                    best_eff = eff
                    best_head = i
                    best_next = nb
        if best_head is None:
            break
        allocation[best_head] = best_next

    alloc_dict = {}
    total_dist = 0.0
    bit_dist = {}
    for i, (l, h, dmap, _avail) in enumerate(heads):
        b = allocation[i]
        alloc_dict[f"{l},{h}"] = ["quant" if b < 16 else "full", b]
        total_dist += dmap.get(b, 0.0)
        bit_dist[b] = bit_dist.get(b, 0) + 1
    actual_ratio = sum(allocation) / (n_heads * max_bits)
    return {
        "allocation": alloc_dict,
        "total_distortion": total_dist,
        "actual_memory_ratio": actual_ratio,
        "bit_distribution": bit_dist,
        "n_2bit": bit_dist.get(2, 0),
    }


def run_one(model_cfg):
    print("\n" + "=" * 70)
    print(f"MODEL: {model_cfg['name']}")
    print("=" * 70)
    t0 = time.time()

    with open(model_cfg["profiles"]) as f:
        raw = json.load(f)
    profiles_raw = raw["profiles"] if "profiles" in raw else raw
    n_layers = len(profiles_raw)
    n_heads_per = len(next(iter(profiles_raw.values())))
    print(f"Profiles: {n_layers} layers x {n_heads_per} kv-heads = {n_layers*n_heads_per} heads")

    profiles = enforce_monotonicity(profiles_raw)

    print(f"\nGreedy unconstrained ({BIT_OPTIONS}, budget={BUDGET})...")
    greedy = unconstrained_greedy(profiles, BUDGET, BIT_OPTIONS)
    print(f"  bit_distribution={greedy['bit_distribution']}  mem_ratio={greedy['actual_memory_ratio']:.4f}  n_2bit={greedy['n_2bit']}")

    print(f"\nMCKP unconstrained (quant_only, budget={BUDGET})...")
    mckp = solve_mckp(profiles, BUDGET, mode="quant_only")
    bit_dist_mckp = {}
    for _, (atype, param) in mckp["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_dist_mckp[b] = bit_dist_mckp.get(b, 0) + 1
    n_2bit_mckp = bit_dist_mckp.get(2, 0)
    print(f"  bit_distribution={bit_dist_mckp}  mem_ratio={mckp['actual_memory_ratio']:.4f}  n_2bit={n_2bit_mckp}")

    print(f"\nLoading model {model_cfg['name']} to {DEVICE}...")
    tokenizer = AutoTokenizer.from_pretrained(model_cfg["path"])
    model = AutoModelForCausalLM.from_pretrained(
        model_cfg["path"], torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(DEVICE)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(DEVICE) / 1e9
    print(f"  GPU mem after load: {mem_gb:.1f}GB")

    input_ids = load_calibration(
        tokenizer, CALIB_PATH, NUM_SAMPLES, SEQ_LEN, DEVICE, model_cfg["prepend_bos"]
    )
    print(f"Calibration: {input_ids.shape[0]} seq x {input_ids.shape[1]} tok")

    patcher = patch_attention_gemma2 if model_cfg["patch"] == "gemma2" else patch_attention

    print("Baseline PPL (no compression)...")
    baseline_ppl = compute_ppl(model, input_ids, input_ids.shape[1], BATCH_SIZE, DEVICE)
    print(f"  baseline_ppl={baseline_ppl:.4f}")

    print("Greedy unconstrained PPL...")
    orig = patcher(model, greedy["allocation"])
    greedy_ppl = compute_ppl(model, input_ids, input_ids.shape[1], BATCH_SIZE, DEVICE)
    restore_attention(model, orig)
    print(f"  greedy_ppl={greedy_ppl:.4f}")

    print("MCKP unconstrained PPL...")
    orig = patcher(model, mckp["allocation"])
    mckp_ppl = compute_ppl(model, input_ids, input_ids.shape[1], BATCH_SIZE, DEVICE)
    restore_attention(model, orig)
    print(f"  mckp_ppl={mckp_ppl:.4f}")

    elapsed = time.time() - t0
    result = {
        "model_name": model_cfg["name"],
        "model_path": model_cfg["path"],
        "profile_source": model_cfg["profiles"],
        "budget": BUDGET,
        "bit_options": BIT_OPTIONS,
        "calibration": {"num_samples": NUM_SAMPLES, "seq_len": SEQ_LEN, "batch_size": BATCH_SIZE},
        "baseline_calibration_ppl": round(baseline_ppl, 4),
        "unconstrained_greedy_ppl": round(greedy_ppl, 4),
        "unconstrained_mckp_ppl": round(mckp_ppl, 4),
        "greedy": {
            "bit_distribution": {int(k): int(v) for k, v in greedy["bit_distribution"].items()},
            "n_2bit_heads": int(greedy["n_2bit"]),
            "actual_memory_ratio": round(greedy["actual_memory_ratio"], 4),
            "total_distortion": float(greedy["total_distortion"]),
        },
        "mckp": {
            "bit_distribution": {int(k): int(v) for k, v in bit_dist_mckp.items()},
            "n_2bit_heads": int(n_2bit_mckp),
            "actual_memory_ratio": round(mckp["actual_memory_ratio"], 4),
            "total_distortion": float(mckp["total_distortion"]),
        },
        "elapsed_seconds": round(elapsed, 1),
    }
    print(f"\nMODEL {model_cfg['name']} done in {elapsed/60:.1f}min")
    print(f"  unconstrained_greedy_ppl={greedy_ppl:.4f}  unconstrained_mckp_ppl={mckp_ppl:.4f}")

    del model, tokenizer, input_ids
    gc.collect()
    torch.cuda.empty_cache()
    return result


def main():
    t_total = time.time()
    out_path = "/root/ratekv/w2_unconstrained_baselines_results.json"
    results = {"exp_id": "w2_unconstrained_baselines", "models": {}}
    for cfg in MODELS:
        try:
            results["models"][cfg["name"]] = run_one(cfg)
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            print(f"\nERROR on {cfg['name']}: {e}\n{tb}")
            results["models"][cfg["name"]] = {"error": str(e), "traceback": tb}
        with open(out_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Intermediate save -> {out_path}")
    results["total_elapsed_seconds"] = round(time.time() - t_total, 1)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nALL DONE. Total {(time.time()-t_total)/60:.1f}min. Saved {out_path}")


if __name__ == "__main__":
    main()
