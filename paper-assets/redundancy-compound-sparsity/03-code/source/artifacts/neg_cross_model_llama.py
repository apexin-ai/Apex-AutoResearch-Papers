#!/usr/bin/env python3
"""
neg-cross-model-001: Cross-model negative evidence for CARC.
Repeats MVP validation (vector EMA anchor + perturbation) on Llama-3.1-8B-Instruct
to confirm cross-axis negative is not DeepSeek-specific.
Reference: mvp_carc_validation_v2.py (DeepSeek-R1-Distill-Qwen-7B).
"""
import argparse, json, os, sys, time, traceback
import numpy as np
import torch, torch.nn.functional as F
from scipy import stats
from transformers import AutoModelForCausalLM, AutoTokenizer

os.environ.setdefault('HF_HOME', '/root/autodl-tmp/.hf_cache')
os.environ['HF_HUB_DISABLE_XET'] = '1'
os.environ.setdefault('REQUESTS_CA_BUNDLE', '/etc/ssl/certs/ca-certificates.crt')
os.environ.setdefault('SSL_CERT_FILE', '/etc/ssl/certs/ca-certificates.crt')

MODEL_PATH = "/root/autodl-tmp/.ms_cache/LLM-Research/Meta-Llama-3.1-8B-Instruct"
OUTPUT_DIR = "/home/sonny/redundancy-compound-sparsity/results/neg_cross_model"
EMA_GAMMA = 0.99
SPARSITY_LEVELS = [0.40, 0.55]
MAX_NEW_TOKENS = 4096
DEVICE = "cuda:0"
DTYPE = torch.bfloat16

FALLBACK_PROBLEMS = [
    {"problem": "Find all values of x such that x^2 - 7x + 12 = 0."},
    {"problem": "A right triangle has legs of length 5 and 12. What is the length of the hypotenuse?"},
    {"problem": "How many integers between 1 and 1000 are divisible by 3 but not by 5?"},
    {"problem": "If log_2(x) + log_2(x-1) = 3, find x."},
    {"problem": "Find the sum of all positive divisors of 360."},
    {"problem": "A fair coin is flipped 6 times. What is the probability of getting exactly 3 heads?"},
    {"problem": "Find the remainder when 2^100 is divided by 7."},
    {"problem": "If the roots of x^3 - 6x^2 + 11x - 6 = 0 are a, b, c, find a^2 + b^2 + c^2."},
    {"problem": "In how many ways can 8 people be seated around a circular table?"},
    {"problem": "Find the area enclosed by y = x^2 and y = 2x + 3."},
    {"problem": "A geometric series has first term 3 and common ratio 2/3. Find the sum to infinity."},
    {"problem": "How many distinct permutations of the letters in MISSISSIPPI are there?"},
    {"problem": "Find the value of cos(arctan(3/4))."},
    {"problem": "A rectangle has perimeter 20 and diagonal of length sqrt(52). Find its area."},
    {"problem": "Find the number of positive divisors of 720."},
    {"problem": "If 3^x = 12, find the value of 9^(x-1)."},
    {"problem": "Find the coefficient of x^3 in the expansion of (2x+1)^5."},
    {"problem": "A bag has 5 red and 3 blue balls. Two drawn without replacement. P(both red)?"},
    {"problem": "Find the shortest distance from the point (3,4) to the line 3x+4y=25."},
    {"problem": "If f(x) = x^3 - 3x + 2, find all x where f has a local maximum."},
]


def load_math_problems(n=20):
    try:
        from datasets import load_dataset
        ds = load_dataset("HuggingFaceH4/MATH-500", split="test")
        filtered = [ex for ex in ds if ex.get("level") in ["Level 3", "Level 4", "Level 5"]]
        if len(filtered) < n:
            filtered = list(ds)
        import random; random.seed(42); random.shuffle(filtered)
        print(f"Loaded MATH-500: {len(filtered)} filtered problems")
        return filtered[:n]
    except Exception as e1:
        print(f"MATH-500 failed: {e1}")
        try:
            from datasets import load_dataset
            ds = load_dataset("hendrycks/competition_math", split="test")
            filtered = [ex for ex in ds if ex.get("level") in ["Level 3", "Level 4", "Level 5"]]
            import random; random.seed(42); random.shuffle(filtered)
            print(f"Loaded competition_math: {len(filtered)} problems")
            return filtered[:n]
        except Exception as e2:
            print(f"competition_math failed: {e2}")
            print("Using fallback problems")
            return FALLBACK_PROBLEMS[:n]


def compute_anchor_signal(x, num_kv_heads, gamma=EMA_GAMMA):
    """Vector EMA anchor cosine similarity signal.
    x: [seq, num_kv_heads * head_dim] -> [seq] per-token scores.
    Reshape to [seq, num_kv_heads, head_dim], maintain per-head anchor,
    compute cosine sim with anchor, mean over heads, then update anchor.
    """
    seq_len = x.shape[0]
    if seq_len == 0:
        return torch.zeros(0, device=x.device, dtype=torch.float32)
    head_dim = x.shape[1] // num_kv_heads
    x_float = x.float().view(seq_len, num_kv_heads, head_dim)

    scores = torch.zeros(seq_len, device=x.device, dtype=torch.float32)
    anchor = x_float[0].clone()  # [num_kv_heads, head_dim]

    for t in range(1, seq_len):
        token = x_float[t]  # [num_kv_heads, head_dim]
        sim = F.cosine_similarity(token, anchor, dim=-1)  # [num_kv_heads]
        scores[t] = sim.mean()
        anchor = gamma * anchor + (1 - gamma) * token

    return scores


class MetricsCollector:
    def __init__(self, num_layers, num_kv_heads):
        self.num_layers = num_layers
        self.num_kv_heads = num_kv_heads
        self.key_scores = {}
        self.val_scores = {}
        self.mlp_l1 = {}
        self.perturbations = {}

    def reset(self):
        self.key_scores.clear(); self.val_scores.clear()
        self.mlp_l1.clear(); self.perturbations.clear()

    def register_hooks(self, model):
        hooks = []
        for li, layer in enumerate(model.model.layers):
            def make_kv_hook(idx, store, nkv):
                def fn(mod, inp, out):
                    x = out[0] if isinstance(out, tuple) else out
                    store[idx] = compute_anchor_signal(x.squeeze(0), nkv).cpu()
                return fn
            hooks.append(layer.self_attn.k_proj.register_forward_hook(
                make_kv_hook(li, self.key_scores, self.num_kv_heads)))
            hooks.append(layer.self_attn.v_proj.register_forward_hook(
                make_kv_hook(li, self.val_scores, self.num_kv_heads)))

            def make_mlp_hook(idx):
                def fn(mod, inp, out):
                    x = inp[0].squeeze(0)
                    dense = (out[0] if isinstance(out, tuple) else out).squeeze(0)
                    self.mlp_l1[idx] = x.float().abs().sum(-1).cpu()
                    for sp in SPARSITY_LEVELS:
                        k = int(sp * x.shape[-1])
                        thresh = x.abs().kthvalue(k, dim=-1).values.unsqueeze(-1)
                        sparse_x = x * (x.abs() >= thresh)
                        sparse_out = F.linear(sparse_x, mod.weight, mod.bias)
                        diff = (dense.float() - sparse_out.float()).norm(dim=-1)
                        denom = dense.float().norm(dim=-1).clamp(min=1e-10)
                        self.perturbations[(idx, sp)] = (diff / denom).cpu()
                return fn
            hooks.append(layer.mlp.down_proj.register_forward_hook(make_mlp_hook(li)))
        return hooks


def process_problem(model, tokenizer, text, collector, max_new_tokens):
    try:
        msgs = [{"role": "user", "content": f"Solve this math problem step by step.\n\n{text}"}]
        prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    except Exception:
        prompt = f"Solve this math problem step by step.\n\n{text}\n\nSolution:"

    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    prompt_len = inputs.input_ids.shape[1]

    with torch.no_grad():
        gen_ids = model.generate(
            inputs.input_ids, attention_mask=inputs.attention_mask,
            max_new_tokens=max_new_tokens, do_sample=False,
            pad_token_id=tokenizer.eos_token_id)
    total_len = gen_ids.shape[1]
    gen_len = total_len - prompt_len
    print(f"    prompt={prompt_len} gen={gen_len} total={total_len}")

    collector.reset()
    with torch.no_grad():
        outputs = model(gen_ids, attention_mask=torch.ones(1, gen_ids.shape[1], device=DEVICE, dtype=torch.long))

    logits = outputs.logits[0]
    token_ids = gen_ids[0]
    del inputs
    surprisal = np.full(total_len, np.nan, dtype=np.float32)
    if total_len > 1:
        tgt = logits[:-1].gather(1, token_ids[1:].unsqueeze(1)).squeeze(1).float()
        lse = torch.logsumexp(logits[:-1].float(), dim=-1)
        surprisal[1:] = -(tgt - lse).cpu().numpy()
    del logits, outputs
    torch.cuda.empty_cache()

    ema_per_layer = {}
    for li in range(collector.num_layers):
        ks = collector.key_scores.get(li)
        vs = collector.val_scores.get(li)
        if ks is not None and vs is not None:
            ema_per_layer[li] = (0.5 * ks + 0.5 * vs).numpy()

    global_ema = (np.nanmean(np.stack(list(ema_per_layer.values())), axis=0)
                  if ema_per_layer else np.full(total_len, np.nan))

    return {
        'total_len': total_len, 'prompt_len': prompt_len,
        'surprisal': surprisal, 'global_ema': global_ema,
        'ema_per_layer': ema_per_layer,
        'mlp_l1': {li: collector.mlp_l1[li].numpy() for li in collector.mlp_l1},
        'perturbations': {k: v.numpy() for k, v in collector.perturbations.items()},
    }


def aggregate(results, num_layers):
    all_surp, all_ema = [], []
    all_l1 = {li: [] for li in range(num_layers)}
    all_pert = {}

    for r in results:
        mask = ~np.isnan(r['surprisal']) & ~np.isnan(r['global_ema'])
        all_surp.append(r['surprisal'][mask])
        all_ema.append(r['global_ema'][mask])
        for li in range(num_layers):
            if li in r['mlp_l1']:
                all_l1[li].append(r['mlp_l1'][li][mask])
            for sp in SPARSITY_LEVELS:
                k = (li, sp)
                if k in r['perturbations']:
                    all_pert.setdefault(k, []).append(r['perturbations'][k][mask])

    surp = np.concatenate(all_surp)
    ema = np.concatenate(all_ema)
    neg_surp = -surp

    r_global, p_global = stats.pearsonr(ema, neg_surp)

    r_layer = {}
    for li in range(num_layers):
        ls, le = [], []
        for r in results:
            if li in r['ema_per_layer']:
                m = ~np.isnan(r['surprisal']) & ~np.isnan(r['ema_per_layer'][li])
                ls.append(r['surprisal'][m])
                le.append(r['ema_per_layer'][li][m])
        if ls:
            lsc, lec = np.concatenate(ls), np.concatenate(le)
            if len(lsc) > 10:
                rl, pl = stats.pearsonr(lec, -lsc)
                r_layer[li] = {'r': float(rl), 'p': float(pl)}

    median_ema = float(np.median(ema))
    red = ema >= median_ema
    nov = ~red

    ks_out = {}
    for li in range(num_layers):
        if all_l1[li]:
            l1 = np.concatenate(all_l1[li])
            if len(l1) == len(red):
                ks_s, ks_p = stats.ks_2samp(l1[red], l1[nov])
                ks_out[li] = {
                    'ks_stat': float(ks_s), 'p_value': float(ks_p),
                    'redundant_mean': float(l1[red].mean()),
                    'novel_mean': float(l1[nov].mean()),
                }

    pert_out = {}
    for sp in SPARSITY_LEVELS:
        reds, novs, per_layer = [], [], {}
        for li in range(num_layers):
            k = (li, sp)
            if k in all_pert:
                p = np.concatenate(all_pert[k])
                if len(p) == len(red):
                    rp, np_ = float(p[red].mean()), float(p[nov].mean())
                    per_layer[li] = {'redundant_mean': rp, 'novel_mean': np_}
                    reds.append(rp)
                    novs.append(np_)
        mr = float(np.mean(reds)) if reds else float('nan')
        mn = float(np.mean(novs)) if novs else float('nan')
        dp = (mn - mr) / (mn + 1e-10) * 100
        pert_out[sp] = {
            'mean_pert_redundant': mr, 'mean_pert_novel': mn,
            'delta_pert_pct': float(dp),
            'per_layer': {str(k): v for k, v in per_layer.items()},
        }

    abs_r = abs(r_global)
    d55 = pert_out.get(0.55, {}).get('delta_pert_pct', 0)
    if abs_r > 0.5 and d55 >= 20:
        verdict = "STRONG_PASS"
    elif (abs_r >= 0.4 and d55 >= 10) or (d55 >= 15 and abs_r >= 0.35):
        verdict = "SUGGESTIVE"
    else:
        verdict = "FAIL"

    return {
        'metric_1_pearson': {
            'global_r': float(r_global), 'global_p': float(p_global),
            'per_layer': {str(k): v for k, v in r_layer.items()},
        },
        'metric_2_ks_test': {str(k): v for k, v in ks_out.items()},
        'metric_3_perturbation': {str(k): v for k, v in pert_out.items()},
        'metric_4_delta_pert_55': float(d55),
        'ema_median': median_ema,
        'total_tokens': int(len(surp)),
        'verdict': verdict,
    }


def main():
    ap = argparse.ArgumentParser(description="neg-cross-model-001: CARC on Llama-3.1-8B-Instruct")
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--num-problems', type=int, default=20)
    args = ap.parse_args()

    t0 = time.time()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading model...")
    tok = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, dtype=DTYPE, device_map=DEVICE, trust_remote_code=True)
    model.eval()
    nl = model.config.num_hidden_layers
    nkv = model.config.num_key_value_heads
    print(f"Model: {nl} layers, {nkv} KV heads, "
          f"{model.config.intermediate_size} intermediate_size")

    if args.dry_run:
        problems = [{'problem': 'What is 2+3?'}]
        max_tok = 64
    else:
        problems = load_math_problems(args.num_problems)
        max_tok = MAX_NEW_TOKENS
    print(f"{len(problems)} problems loaded")

    coll = MetricsCollector(nl, nkv)
    hooks = coll.register_hooks(model)

    results = []
    per_problem = []
    for i, p in enumerate(problems):
        text = p.get('problem', p.get('question', ''))
        print(f"\n[{i+1}/{len(problems)}] {text[:80]}...")
        try:
            r = process_problem(model, tok, text, coll, max_tok)
            results.append(r)
            mask = ~np.isnan(r['surprisal']) & ~np.isnan(r['global_ema'])
            n_valid = int(mask.sum())
            ps = {'idx': i, 'total_len': r['total_len'],
                  'prompt_len': r['prompt_len'], 'valid_tokens': n_valid}
            if n_valid > 10:
                rr, _ = stats.pearsonr(r['global_ema'][mask], -r['surprisal'][mask])
                ps['pearson_r'] = float(rr)
            per_problem.append(ps)
            print(f"    valid={n_valid}" +
                  (f" r={ps['pearson_r']:.3f}" if 'pearson_r' in ps else ""))
        except torch.cuda.OutOfMemoryError:
            print("    OOM, skipping")
            torch.cuda.empty_cache()
        except Exception as e:
            print(f"    Error: {e}")
            traceback.print_exc()

    for h in hooks:
        h.remove()

    if not results:
        print("No results!")
        sys.exit(1)

    final = aggregate(results, nl)
    final['metadata'] = {
        'experiment': 'neg-cross-model-001',
        'model': MODEL_PATH,
        'model_name': 'Llama-3.1-8B-Instruct',
        'reference_model': 'DeepSeek-R1-Distill-Qwen-7B',
        'num_problems_attempted': len(problems),
        'num_problems_completed': len(results),
        'ema_gamma': EMA_GAMMA,
        'signal_type': 'vector_ema_anchor',
        'sparsity_levels': SPARSITY_LEVELS,
        'max_new_tokens': max_tok,
        'elapsed_seconds': time.time() - t0,
        'dry_run': args.dry_run,
    }
    final['per_problem'] = per_problem

    out = os.path.join(OUTPUT_DIR, "neg_cross_model_results.json")
    with open(out, 'w') as f:
        json.dump(final, f, indent=2)

    print(f"\n{'='*60}")
    print(f"neg-cross-model-001 (Llama-3.1-8B) -- {final['total_tokens']} tokens from {len(results)} problems")
    print(f"{'='*60}")
    m1 = final['metric_1_pearson']
    print(f"Pearson r(anchor_sim, -surprisal): {m1['global_r']:.4f} (p={m1['global_p']:.2e})")
    print(f"\nK-S test (first 5 layers):")
    for li in range(min(5, nl)):
        k = str(li)
        if k in final['metric_2_ks_test']:
            ks = final['metric_2_ks_test'][k]
            print(f"  L{li}: stat={ks['ks_stat']:.4f} p={ks['p_value']:.2e} "
                  f"red={ks['redundant_mean']:.1f} nov={ks['novel_mean']:.1f}")
    for sp_s, d in final['metric_3_perturbation'].items():
        print(f"\nSparsity {sp_s}: red={d['mean_pert_redundant']:.4f} "
              f"nov={d['mean_pert_novel']:.4f} dpert={d['delta_pert_pct']:.1f}%")
    print(f"\ndpert@55%: {final['metric_4_delta_pert_55']:.1f}%")
    print(f"\n>>> VERDICT: {final['verdict']} <<<")
    print(f"Elapsed: {time.time()-t0:.0f}s | Saved: {out}")


if __name__ == "__main__":
    main()
