"""K/V Separation Experiment (plan_014).
Independent bit-width allocation for K and V heads via MCKP.
"""
import json
import math
import time
import os
import importlib
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
from eval_ppl import evaluate_perplexity, restore_attention, _get_rotary_fn
from utils import quantize_per_channel, quantize_per_token, repeat_kv
from solver import solve_mckp_constrained, enforce_monotonicity

MODEL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
DEVICE = "cuda:1"
BUDGET = 0.25
MAX_2BIT_JOINT = 8
MAX_2BIT_SEP = 16
CALIBRATION = "calibration_hires.json"
HIRES_PROFILES = "ppl_profiles_hires.json"
OUTPUT = "kv_separation_results.json"
KV_PROFILES_FILE = "kv_separation_profiles.json"
BATCH_SIZE = 16
SEQ_LEN = 2048
NUM_SAMPLES = 64


def patch_attention_kv_sep(model, k_allocs, v_allocs):
    config = model.config
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_q_heads
    n_groups = num_q_heads // num_kv_heads
    rotary_fn = _get_rotary_fn(model)
    original_forwards = {}

    for layer_idx, layer in enumerate(model.model.layers):
        attn = layer.self_attn
        k_ha = {}
        v_ha = {}
        for h in range(num_kv_heads):
            key = f"{layer_idx},{h}"
            k_ha[h] = k_allocs.get(key, ["full", 16])
            v_ha[h] = v_allocs.get(key, ["full", 16])

        all_full = (
            all(a[1] >= 16 for a in k_ha.values()) and
            all(a[1] >= 16 for a in v_ha.values())
        )
        if all_full:
            continue

        original_forwards[layer_idx] = attn.forward

        def make_forward(orig_attn, k_h, v_h,
                         n_kv=num_kv_heads, ng=n_groups, hd=head_dim,
                         rope_fn=rotary_fn):
            def fwd(hidden_states, position_embeddings, attention_mask=None, **kwargs):
                bsz, seq_len = hidden_states.shape[:2]
                q = orig_attn.q_proj(hidden_states).view(bsz, seq_len, -1, hd).transpose(1, 2)
                k = orig_attn.k_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)
                v = orig_attn.v_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)
                cos, sin = position_embeddings
                q, k = rope_fn(q, k, cos, sin)

                for h in range(n_kv):
                    kb = int(k_h[h][1])
                    if kb < 16:
                        k[:, h] = quantize_per_channel(k[:, h:h+1], kb).squeeze(1)
                    vb = int(v_h[h][1])
                    if vb < 16:
                        v[:, h] = quantize_per_token(v[:, h:h+1], vb).squeeze(1)

                k_exp = repeat_kv(k, ng)
                v_exp = repeat_kv(v, ng)
                attn_scores = torch.matmul(q, k_exp.transpose(2, 3)) * orig_attn.scaling
                if attention_mask is not None:
                    cm = attention_mask[:, :, :, :k_exp.shape[-2]]
                    attn_scores = attn_scores + cm
                else:
                    causal = torch.triu(
                        torch.full((seq_len, seq_len), float("-inf"),
                                   device=attn_scores.device, dtype=attn_scores.dtype),
                        diagonal=1
                    )
                    attn_scores = attn_scores + causal

                attn_w = F.softmax(attn_scores, dim=-1, dtype=torch.float32).to(q.dtype)
                out = torch.matmul(attn_w, v_exp)
                out = out.transpose(1, 2).contiguous().reshape(bsz, seq_len, -1)
                out = orig_attn.o_proj(out)
                return out, attn_w
            return fwd

        attn.forward = make_forward(attn, k_ha, v_ha)

    return original_forwards


class KVSepProfiler:
    def __init__(self, model, tokenizer, device, calibration_path,
                 num_samples=64, seq_len=2048, batch_size=16):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        self.seq_len = seq_len
        self.batch_size = batch_size
        self.num_layers = model.config.num_hidden_layers
        self.num_kv_heads = model.config.num_key_value_heads
        self.input_ids = self._load_calibration(calibration_path, num_samples)
        print(f"Calibration: {self.input_ids.shape[0]} seqs x {self.input_ids.shape[1]} tokens")
        self._baseline_ppl = None

    def _load_calibration(self, path, num_samples):
        with open(path) as f:
            samples = json.load(f)
        all_ids = []
        for s in samples:
            tokens = self.tokenizer.encode(s["text"], add_special_tokens=False)
            if len(tokens) >= self.seq_len:
                all_ids.append(tokens[:self.seq_len])
            if len(all_ids) >= num_samples:
                break
        return torch.tensor(all_ids, dtype=torch.long, device=self.device)

    def _compute_ppl(self):
        total_loss = 0.0
        total_tokens = 0
        n = self.input_ids.shape[0]
        with torch.no_grad():
            for start in range(0, n, self.batch_size):
                end = min(start + self.batch_size, n)
                batch = self.input_ids[start:end]
                outputs = self.model(
                    batch, use_cache=False,
                    cache_position=torch.arange(self.seq_len, device=self.device)
                )
                shift_logits = outputs.logits[:, :-1].contiguous()
                shift_labels = batch[:, 1:].contiguous()
                loss = F.cross_entropy(
                    shift_logits.float().view(-1, shift_logits.shape[-1]),
                    shift_labels.view(-1), reduction="sum"
                )
                total_loss += loss.item()
                total_tokens += shift_labels.numel()
                del outputs, shift_logits, loss
                torch.cuda.empty_cache()
        return math.exp(total_loss / total_tokens)

    def compute_baseline(self):
        if self._baseline_ppl is None:
            print("Computing baseline calibration PPL...")
            self._baseline_ppl = self._compute_ppl()
            print(f"Baseline calibration PPL: {self._baseline_ppl:.4f}")
        return self._baseline_ppl

    def _profile_one(self, layer, head, bits, target):
        key = f"{layer},{head}"
        if target == "K":
            k_allocs = {key: ["quant", bits]}
            v_allocs = {}
        else:
            k_allocs = {}
            v_allocs = {key: ["quant", bits]}

        orig_fwds = patch_attention_kv_sep(self.model, k_allocs, v_allocs)
        ppl = self._compute_ppl()
        restore_attention(self.model, orig_fwds)
        return ppl - self._baseline_ppl

    def profile_all(self, bit_widths=(2, 4, 8), checkpoint_path=None):
        self.compute_baseline()
        total = self.num_layers * self.num_kv_heads
        total_evals = total * len(bit_widths) * 2

        k_profiles = {}
        v_profiles = {}

        if checkpoint_path and os.path.exists(checkpoint_path):
            with open(checkpoint_path) as f:
                ckpt = json.load(f)
            k_profiles = ckpt.get("k_profiles", {})
            v_profiles = ckpt.get("v_profiles", {})
            print(f"Resumed from checkpoint: {sum(len(v) for v in k_profiles.values())} K heads, "
                  f"{sum(len(v) for v in v_profiles.values())} V heads done")

        done = 0
        t_start = time.time()

        for l in range(self.num_layers):
            l_str = str(l)
            if l_str not in k_profiles:
                k_profiles[l_str] = {}
            if l_str not in v_profiles:
                v_profiles[l_str] = {}

            for h in range(self.num_kv_heads):
                h_str = str(h)

                # K profiling
                if h_str not in k_profiles[l_str]:
                    kp = {"quantization": {}}
                    for bits in bit_widths:
                        delta = self._profile_one(l, h, bits, "K")
                        kp["quantization"][str(bits)] = delta
                    k_profiles[l_str][h_str] = kp
                    done += len(bit_widths)
                    elapsed = time.time() - t_start
                    rate = done / elapsed if elapsed > 0 else 0
                    remaining = (total_evals - done) / rate if rate > 0 else 0
                    print(f"[K] L{l}H{h}: {kp['quantization']}  "
                          f"({done}/{total_evals}, ETA {remaining/60:.0f}min)")
                else:
                    done += len(bit_widths)

                # V profiling
                if h_str not in v_profiles[l_str]:
                    vp = {"quantization": {}}
                    for bits in bit_widths:
                        delta = self._profile_one(l, h, bits, "V")
                        vp["quantization"][str(bits)] = delta
                    v_profiles[l_str][h_str] = vp
                    done += len(bit_widths)
                    elapsed = time.time() - t_start
                    rate = done / elapsed if elapsed > 0 else 0
                    remaining = (total_evals - done) / rate if rate > 0 else 0
                    print(f"[V] L{l}H{h}: {vp['quantization']}  "
                          f"({done}/{total_evals}, ETA {remaining/60:.0f}min)")
                else:
                    done += len(bit_widths)

                # Checkpoint every 4 heads
                if checkpoint_path and (done % (len(bit_widths) * 8)) < (len(bit_widths) * 2):
                    with open(checkpoint_path, "w") as f:
                        json.dump({
                            "k_profiles": k_profiles,
                            "v_profiles": v_profiles,
                            "baseline_ppl": self._baseline_ppl,
                        }, f, indent=2)

        # Final save
        if checkpoint_path:
            with open(checkpoint_path, "w") as f:
                json.dump({
                    "k_profiles": k_profiles,
                    "v_profiles": v_profiles,
                    "baseline_ppl": self._baseline_ppl,
                }, f, indent=2)

        return k_profiles, v_profiles


def solve_kv_sep_mckp(k_profiles, v_profiles, budget, max_2bit=16,
                       l0_exclude_2bit=True):
    bit_options = sorted([2, 4, 8, 16])
    items = []

    for l_str in sorted(k_profiles.keys(), key=lambda x: int(x)):
        for h_str in sorted(k_profiles[l_str].keys(), key=lambda x: int(x)):
            l, h = int(l_str), int(h_str)
            qdata = k_profiles[l_str][h_str].get("quantization", {})
            exclude = {2} if (l0_exclude_2bit and l == 0) else set()
            actions = [(1.0, 0.0, "full", 16)]
            for b_str, mse in qdata.items():
                b = int(float(b_str))
                if b in exclude:
                    continue
                actions.append((b / 16.0, mse, "quant", b))
            by_mem = {}
            for a in actions:
                mem = round(a[0], 6)
                if mem not in by_mem or a[1] < by_mem[mem][1]:
                    by_mem[mem] = a
            actions = sorted(by_mem.values(), key=lambda x: -x[0])
            items.append((l, h, "K", actions))

    for l_str in sorted(v_profiles.keys(), key=lambda x: int(x)):
        for h_str in sorted(v_profiles[l_str].keys(), key=lambda x: int(x)):
            l, h = int(l_str), int(h_str)
            qdata = v_profiles[l_str][h_str].get("quantization", {})
            exclude = {2} if (l0_exclude_2bit and l == 0) else set()
            actions = [(1.0, 0.0, "full", 16)]
            for b_str, mse in qdata.items():
                b = int(float(b_str))
                if b in exclude:
                    continue
                actions.append((b / 16.0, mse, "quant", b))
            by_mem = {}
            for a in actions:
                mem = round(a[0], 6)
                if mem not in by_mem or a[1] < by_mem[mem][1]:
                    by_mem[mem] = a
            actions = sorted(by_mem.values(), key=lambda x: -x[0])
            items.append((l, h, "V", actions))

    n_items = len(items)
    target = budget * n_items
    current = [0] * n_items
    total_memory = sum(items[i][3][0][0] for i in range(n_items))
    n_2bit = 0

    while total_memory > target + 1e-9:
        best_eff = float("inf")
        best_saved = 0.0
        best_i = None
        best_ni = None

        for i in range(n_items):
            ci = current[i]
            actions = items[i][3]
            if ci + 1 >= len(actions):
                continue
            curr = actions[ci]
            for ni in range(ci + 1, len(actions)):
                nxt = actions[ni]
                mem_saved = curr[0] - nxt[0]
                if mem_saved < 1e-12:
                    continue
                is_2bit = (nxt[2] == "quant" and nxt[3] == 2)
                if is_2bit and n_2bit >= max_2bit:
                    continue
                eff = (nxt[1] - curr[1]) / mem_saved
                if eff < best_eff - 1e-12 or (abs(eff - best_eff) < 1e-12 and mem_saved > best_saved):
                    best_eff = eff
                    best_saved = mem_saved
                    best_i = i
                    best_ni = ni

        if best_i is None:
            break

        actions = items[best_i][3]
        old = actions[current[best_i]]
        new = actions[best_ni]
        total_memory -= (old[0] - new[0])
        was_2bit = (old[2] == "quant" and old[3] == 2)
        is_now_2bit = (new[2] == "quant" and new[3] == 2)
        if is_now_2bit and not was_2bit:
            n_2bit += 1
        elif was_2bit and not is_now_2bit:
            n_2bit -= 1
        current[best_i] = best_ni

    k_alloc = {}
    v_alloc = {}
    total_dist = 0.0
    k_bit_dist = {}
    v_bit_dist = {}

    for i, (l, h, kv_type, actions) in enumerate(items):
        a = actions[current[i]]
        key = f"{l},{h}"
        entry = [a[2], a[3]]
        total_dist += a[1]

        if kv_type == "K":
            k_alloc[key] = entry
            k_bit_dist[a[3]] = k_bit_dist.get(a[3], 0) + 1
        else:
            v_alloc[key] = entry
            v_bit_dist[a[3]] = v_bit_dist.get(a[3], 0) + 1

    actual_ratio = total_memory / n_items

    return {
        "k_allocation": k_alloc,
        "v_allocation": v_alloc,
        "total_distortion": total_dist,
        "actual_memory_ratio": actual_ratio,
        "k_bit_distribution": k_bit_dist,
        "v_bit_distribution": v_bit_dist,
        "n_2bit": n_2bit,
        "n_items": n_items,
    }


def count_asymmetric(k_alloc, v_alloc):
    asym = 0
    details = []
    for key in k_alloc:
        kb = k_alloc[key][1]
        vb = v_alloc[key][1]
        if kb != vb:
            asym += 1
            details.append(f"  {key}: K={kb}bit V={vb}bit")
    return asym, details


def main():
    t_start = time.time()
    os.chdir("/root/ratekv")

    print(f"Device: {DEVICE}")
    print(f"Loading model {MODEL}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(DEVICE)
    model.eval()
    print(f"Model loaded. Layers={model.config.num_hidden_layers}, KV_heads={model.config.num_key_value_heads}")

    # === Phase 1: K/V separated profiling ===
    print(f"\n{'='*60}")
    print("Phase 1: K/V Separated Profiling")
    print(f"{'='*60}")

    profiler = KVSepProfiler(
        model, tokenizer, DEVICE, CALIBRATION,
        num_samples=NUM_SAMPLES, seq_len=SEQ_LEN, batch_size=BATCH_SIZE
    )

    t_prof_start = time.time()
    k_profiles, v_profiles = profiler.profile_all(
        bit_widths=(2, 4, 8),
        checkpoint_path=KV_PROFILES_FILE
    )
    t_profile = time.time() - t_prof_start
    print(f"Profiling done in {t_profile:.1f}s ({t_profile/60:.1f}min)")

    # Enforce monotonicity
    k_profiles = enforce_monotonicity(k_profiles)
    v_profiles = enforce_monotonicity(v_profiles)

    # === Phase 2: Solve MCKP ===
    print(f"\n{'='*60}")
    print("Phase 2: MCKP Solving")
    print(f"{'='*60}")

    # K/V separated
    sep_result = solve_kv_sep_mckp(
        k_profiles, v_profiles, BUDGET,
        max_2bit=MAX_2BIT_SEP, l0_exclude_2bit=True
    )
    print(f"\n[K/V Separated] budget={BUDGET}")
    print(f"  K bit dist: {sep_result['k_bit_distribution']}")
    print(f"  V bit dist: {sep_result['v_bit_distribution']}")
    print(f"  Memory ratio: {sep_result['actual_memory_ratio']:.4f}")
    print(f"  2-bit count: {sep_result['n_2bit']}")

    asym_count, asym_details = count_asymmetric(
        sep_result["k_allocation"], sep_result["v_allocation"]
    )
    print(f"  Asymmetric heads (K≠V): {asym_count}/112")
    for d in asym_details[:20]:
        print(d)
    if len(asym_details) > 20:
        print(f"  ... and {len(asym_details)-20} more")

    # Joint K=V baseline using existing hires profiles
    with open(HIRES_PROFILES) as f:
        hires_data = json.load(f)
    joint_profiles = hires_data["profiles"]
    joint_profiles = enforce_monotonicity(joint_profiles)

    joint_result = solve_mckp_constrained(
        joint_profiles, BUDGET, mode="quant_only",
        max_2bit=MAX_2BIT_JOINT, l0_exclude_2bit=True
    )
    print(f"\n[Joint K=V] budget={BUDGET}")
    print(f"  Bit dist: {joint_result['bit_distribution']}")
    print(f"  Memory ratio: {joint_result['actual_memory_ratio']:.4f}")

    # === Phase 3: WikiText-2 PPL Evaluation ===
    print(f"\n{'='*60}")
    print("Phase 3: WikiText-2 PPL Evaluation (bf16)")
    print(f"{'='*60}")

    # Baseline
    print("\nEval: baseline (no quant)...")
    baseline_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    print(f">>> Baseline PPL: {baseline_ppl:.4f}")

    # K/V separated MCKP
    print("\nEval: K/V separated MCKP...")
    orig = patch_attention_kv_sep(model, sep_result["k_allocation"], sep_result["v_allocation"])
    sep_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f">>> K/V Separated PPL: {sep_ppl:.4f}")

    # Joint K=V MCKP
    print("\nEval: Joint K=V MCKP (hires)...")
    from eval_ppl import patch_attention
    orig = patch_attention(model, joint_result["allocation"])
    joint_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f">>> Joint K=V PPL: {joint_ppl:.4f}")

    # Uniform 4-bit
    print("\nEval: Uniform 4-bit...")
    uniform_alloc = {}
    for l in range(model.config.num_hidden_layers):
        for h in range(model.config.num_key_value_heads):
            uniform_alloc[f"{l},{h}"] = ["quant", 4]
    orig = patch_attention(model, uniform_alloc)
    uniform_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f">>> Uniform 4-bit PPL: {uniform_ppl:.4f}")

    t_total = time.time() - t_start

    # === Results ===
    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}")
    print(f"{'Method':<35} {'PPL':>10} {'Memory':>10} {'Delta':>10}")
    print("-" * 67)
    print(f"{'Baseline (bf16)':<35} {baseline_ppl:>10.4f} {'1.0000':>10} {'---':>10}")
    print(f"{'Uniform 4-bit':<35} {uniform_ppl:>10.4f} {'0.2500':>10} {uniform_ppl-baseline_ppl:>+10.4f}")
    print(f"{'Joint K=V MCKP (hires)':<35} {joint_ppl:>10.4f} {joint_result['actual_memory_ratio']:>10.4f} {joint_ppl-baseline_ppl:>+10.4f}")
    print(f"{'K/V Separated MCKP':<35} {sep_ppl:>10.4f} {sep_result['actual_memory_ratio']:>10.4f} {sep_ppl-baseline_ppl:>+10.4f}")
    print(f"\nK/V Sep vs Joint K=V: {sep_ppl - joint_ppl:+.4f}")
    print(f"K/V Sep vs Uniform 4-bit: {sep_ppl - uniform_ppl:+.4f}")
    print(f"Asymmetric heads: {asym_count}/112")
    print(f"Total time: {t_total:.1f}s ({t_total/60:.1f}min)")

    results = {
        "kv_separated_ppl": sep_ppl,
        "joint_kv_ppl": joint_ppl,
        "uniform_4bit_ppl": uniform_ppl,
        "baseline_ppl": baseline_ppl,
        "delta_sep_vs_joint": sep_ppl - joint_ppl,
        "delta_sep_vs_uniform": sep_ppl - uniform_ppl,
        "kv_separated": {
            "k_allocation": sep_result["k_allocation"],
            "v_allocation": sep_result["v_allocation"],
            "k_bit_distribution": sep_result["k_bit_distribution"],
            "v_bit_distribution": sep_result["v_bit_distribution"],
            "actual_memory_ratio": sep_result["actual_memory_ratio"],
            "total_distortion": sep_result["total_distortion"],
            "n_2bit": sep_result["n_2bit"],
        },
        "joint_kv": {
            "allocation": joint_result["allocation"],
            "bit_distribution": joint_result["bit_distribution"],
            "actual_memory_ratio": joint_result["actual_memory_ratio"],
        },
        "asymmetric_heads": asym_count,
        "asymmetric_details": asym_details,
        "calibration_baseline_ppl": profiler._baseline_ppl,
        "profile_time_seconds": t_profile,
        "total_time_seconds": t_total,
        "config": {
            "model": MODEL,
            "device": DEVICE,
            "budget": BUDGET,
            "max_2bit_sep": MAX_2BIT_SEP,
            "max_2bit_joint": MAX_2BIT_JOINT,
            "l0_exclude_2bit": True,
            "calibration": CALIBRATION,
            "num_samples": NUM_SAMPLES,
            "seq_len": SEQ_LEN,
        },
    }

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {OUTPUT}")


if __name__ == "__main__":
    main()
