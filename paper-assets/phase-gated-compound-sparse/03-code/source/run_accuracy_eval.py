"""
R9-C2: Compound Sparsity Accuracy Evaluation on MATH-500.

Evaluates accuracy under compound sparsity (head pruning + KV eviction)
across multiple sparsity levels and strategies (importance vs random).
Computes correlation between accuracy degradation and PPL severity gradient.

Usage:
  # Spike (10 problems, single condition):
  python run_accuracy_eval.py --num-problems 10 --conditions dense,importance_s025 --gpu cuda:0

  # Full run (all conditions, single GPU):
  python run_accuracy_eval.py --conditions all --gpu cuda:0

  # Parallel subset per GPU:
  python run_accuracy_eval.py --conditions dense,importance_s015,importance_s020 --gpu cuda:0
  python run_accuracy_eval.py --conditions importance_s025,importance_s030 --gpu cuda:1
"""
import json, re, time, os, sys, argparse
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

CONDITION_SPECS = {
    "dense": {"sparsity": 0.0, "strategy": None},
    "importance_s015": {"sparsity": 0.15, "strategy": "importance"},
    "importance_s020": {"sparsity": 0.20, "strategy": "importance"},
    "importance_s025": {"sparsity": 0.25, "strategy": "importance"},
    "importance_s030": {"sparsity": 0.30, "strategy": "importance"},
    "random_s015": {"sparsity": 0.15, "strategy": "random"},
    "random_s020": {"sparsity": 0.20, "strategy": "random"},
    "random_s025": {"sparsity": 0.25, "strategy": "random"},
    "random_s030": {"sparsity": 0.30, "strategy": "random"},
}
ALL_CONDITIONS = list(CONDITION_SPECS.keys())


def extract_boxed(text):
    results = []
    i = 0
    while i < len(text):
        idx = text.find("\\boxed{", i)
        if idx == -1:
            break
        depth = 0
        start = idx + len("\\boxed{")
        for j in range(start, len(text)):
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                if depth == 0:
                    results.append(text[start:j])
                    i = j + 1
                    break
                depth -= 1
        else:
            i = len(text)
    return results[-1].strip() if results else None


def normalize_answer(ans):
    if ans is None:
        return ""
    ans = ans.strip()
    ans = re.sub(r'\\(text|mathrm|mathbf|mathit|textbf)\{([^}]*)\}', r'\2', ans)
    ans = ans.replace("\\left", "").replace("\\right", "")
    ans = re.sub(r'\\[,;:!]', '', ans)
    ans = ans.replace(" ", "")
    ans = ans.replace("\\dfrac", "\\frac").replace("\\tfrac", "\\frac")
    ans = ans.rstrip(".")
    return ans


def answers_match(pred, ref):
    np_ = normalize_answer(pred)
    nr_ = normalize_answer(ref)
    if not np_ or not nr_:
        return False
    if np_ == nr_:
        return True
    def to_frac(s):
        m = re.match(r'^\\frac\{(-?\d+)\}\{(-?\d+)\}$', s)
        if m:
            return (int(m.group(1)), int(m.group(2)))
        try:
            v = int(s)
            return (v, 1)
        except Exception:
            pass
        try:
            v = float(s)
            return (v, 1.0)
        except Exception:
            return None
    fp, fr = to_frac(np_), to_frac(nr_)
    if fp and fr:
        return abs(fp[0] * fr[1] - fp[1] * fr[0]) < 1e-9
    return False


class HeadMaskHook:
    def __init__(self, model, head_mask):
        self.handles = []
        attn_layers = self._find_attention_layers(model)
        for layer_idx, attn_module in enumerate(attn_layers):
            if layer_idx >= head_mask.size(0):
                break
            mask = head_mask[layer_idx]
            handle = attn_module.register_forward_hook(self._make_hook(mask))
            self.handles.append(handle)

    @staticmethod
    def _find_attention_layers(model):
        layers = []
        for name, module in model.named_modules():
            if type(module).__name__.endswith("Attention") and "self" not in name.split(".")[-1].lower():
                children_attn = [m for m in module.children() if type(m).__name__.endswith("Attention")]
                if not children_attn:
                    layers.append(module)
        if not layers:
            for name, module in model.named_modules():
                if name.endswith(".self_attn") or name.endswith(".attention"):
                    layers.append(module)
        return layers

    @staticmethod
    def _make_hook(mask):
        def hook_fn(module, input, output):
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output
            num_heads = mask.size(0)
            bsz, seq_len, hidden_dim = hidden.shape
            head_dim = hidden_dim // num_heads
            reshaped = hidden.view(bsz, seq_len, num_heads, head_dim)
            head_mask_expanded = mask.to(hidden.device).view(1, 1, num_heads, 1)
            reshaped = torch.where(head_mask_expanded.bool(), reshaped, torch.zeros_like(reshaped))
            masked_hidden = reshaped.view(bsz, seq_len, hidden_dim)
            if isinstance(output, tuple):
                return (masked_hidden,) + output[1:]
            return masked_hidden
        return hook_fn

    def remove(self):
        for h in self.handles:
            h.remove()
        self.handles.clear()


@torch.no_grad()
def collect_importance(model, input_ids, device):
    config = model.config
    num_layers = config.num_hidden_layers
    num_heads = config.num_attention_heads
    seq_len = input_ids.size(-1)

    head_importance = torch.zeros(num_layers, num_heads)
    kv_importance = torch.zeros(seq_len)
    nan_count = 0

    attn_layers = HeadMaskHook._find_attention_layers(model)
    handles = []

    for layer_idx, attn_module in enumerate(attn_layers):
        def _make_pre_hook():
            def _pre(module, args, kwargs):
                kwargs = dict(kwargs)
                kwargs["output_attentions"] = True
                return args, kwargs
            return _pre

        def _make_post_hook(l_idx):
            nonlocal nan_count
            def _post(module, input, output):
                nonlocal nan_count
                if isinstance(output, tuple) and len(output) > 1 and output[1] is not None:
                    attn_f = output[1][0].float()
                    if torch.isnan(attn_f).any():
                        nan_count += 1
                    else:
                        head_importance[l_idx] = attn_f.norm(dim=(-2, -1)).cpu()
                        kv_importance.add_(attn_f.sum(dim=(0, 1)).cpu())
                    del attn_f
                    return (output[0],) + (None,) + output[2:]
            return _post

        h_pre = attn_module.register_forward_pre_hook(_make_pre_hook(), with_kwargs=True)
        h_post = attn_module.register_forward_hook(_make_post_hook(layer_idx))
        handles.extend([h_pre, h_post])

    try:
        model(input_ids=input_ids.to(device))
    finally:
        for h in handles:
            h.remove()

    if nan_count:
        print(f"  [warn] {nan_count} layers had NaN attention weights", flush=True)

    return head_importance, kv_importance


def build_head_mask(num_layers, num_heads, ratio, importance=None):
    mask = torch.ones(num_layers, num_heads)
    num_to_mask = max(1, int(num_heads * ratio))
    for layer in range(num_layers):
        if importance is not None:
            _, indices = importance[layer].topk(num_to_mask, largest=False)
        else:
            indices = torch.randperm(num_heads)[:num_to_mask]
        mask[layer, indices] = 0.0
    return mask


def build_kv_mask(seq_len, ratio, importance=None):
    mask = torch.ones(seq_len)
    num_to_evict = max(1, int(seq_len * ratio))
    num_to_evict = min(num_to_evict, seq_len - 1)
    if importance is not None:
        if importance.dim() == 2:
            importance = importance.mean(dim=0)
        position_counts = torch.arange(importance.shape[0], 0, -1, dtype=importance.dtype)
        importance = importance / position_counts
        candidates = importance[1:]
        _, indices = candidates.topk(min(num_to_evict, len(candidates)), largest=False)
        indices = indices + 1
    else:
        indices = torch.randperm(seq_len - 1)[:num_to_evict] + 1
    mask[indices] = 0.0
    return mask


def run_evaluation(model, tokenizer, problems, device, conditions):
    num_layers = model.config.num_hidden_layers
    num_heads = model.config.num_attention_heads

    need_importance = any(
        CONDITION_SPECS[c]["strategy"] == "importance" for c in conditions
    )

    cond_results = {c: {"correct": 0, "total": 0, "details": []} for c in conditions}

    for i, prob in enumerate(problems):
        messages = [{"role": "user", "content": f"Please solve the following math problem step by step. Put your final answer in \\boxed{{}}.\n\n{prob['problem']}"}]
        try:
            prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        except Exception:
            prompt = f"User: {messages[0]['content']}\n\nAssistant:"

        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        prompt_len = input_ids.size(1)
        ref_answer = prob["answer"]

        print(f"\n[Problem {i+1}/{len(problems)}] prompt_len={prompt_len}", flush=True)

        head_imp, kv_imp = None, None
        if need_importance:
            t_imp = time.time()
            head_imp, kv_imp = collect_importance(model, input_ids, device)
            print(f"  Importance collected ({time.time()-t_imp:.1f}s)", flush=True)

        for cond_name in conditions:
            spec = CONDITION_SPECS[cond_name]
            t0 = time.time()

            hook_ctx = None
            gen_kwargs = dict(max_new_tokens=2048, do_sample=False)

            if spec["strategy"] is not None and spec["sparsity"] > 0:
                s = spec["sparsity"]
                imp_h = head_imp if spec["strategy"] == "importance" else None
                imp_k = kv_imp if spec["strategy"] == "importance" else None

                head_mask = build_head_mask(num_layers, num_heads, s, imp_h)
                kv_mask = build_kv_mask(prompt_len, s, imp_k)

                attention_mask = torch.ones(1, prompt_len, dtype=torch.long)
                evicted = (kv_mask == 0).nonzero(as_tuple=True)[0]
                attention_mask[0, evicted] = 0
                gen_kwargs["attention_mask"] = attention_mask.to(device)

                hook_ctx = HeadMaskHook(model, head_mask)

                heads_pruned = int((head_mask == 0).sum().item())
                kv_evicted = int((kv_mask == 0).sum().item())
                print(f"  [{cond_name}] heads_pruned={heads_pruned}, kv_evicted={kv_evicted}/{prompt_len}", flush=True)

            try:
                output_ids = model.generate(input_ids.to(device), **gen_kwargs)
            except torch.cuda.OutOfMemoryError:
                print(f"  [{cond_name}] OOM", flush=True)
                torch.cuda.empty_cache()
                cond_results[cond_name]["details"].append({"id": prob.get("id", str(i)), "error": "OOM"})
                cond_results[cond_name]["total"] += 1
                continue
            finally:
                if hook_ctx is not None:
                    hook_ctx.remove()

            gen_ids = output_ids[0, prompt_len:]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)

            pred_answer = extract_boxed(gen_text)
            match = answers_match(pred_answer, ref_answer)
            if match:
                cond_results[cond_name]["correct"] += 1
            cond_results[cond_name]["total"] += 1

            elapsed = time.time() - t0
            cond_results[cond_name]["details"].append({
                "id": prob.get("id", str(i)),
                "pred_answer": pred_answer,
                "ref_answer": ref_answer,
                "match": match,
                "gen_length": len(gen_ids),
                "time_seconds": round(elapsed, 1),
            })

            c = cond_results[cond_name]["correct"]
            t = cond_results[cond_name]["total"]
            status = "✓" if match else "✗"
            print(f"  [{cond_name}] {status} pred={pred_answer} ref={ref_answer} ({elapsed:.1f}s) running={c}/{t}", flush=True)

            torch.cuda.empty_cache()

    return cond_results


def load_ppl_severity(ppl_base_dir, strategy, sparsity_levels):
    severity = {}
    for s in sparsity_levels:
        s_str = f"s{int(s*100):03d}"
        strat_str = "imp" if strategy == "importance" else "rand"
        ppl_path = os.path.join(
            ppl_base_dir,
            f"profiling_output_n500_bf16_ds_{strat_str}_{s_str}",
            "profiling_results.json",
        )
        if not os.path.exists(ppl_path):
            print(f"  [warn] PPL not found: {ppl_path}", flush=True)
            continue
        with open(ppl_path) as f:
            data = json.load(f)
        ppl = data.get("perplexity", {})
        ratios = []
        for phase_name, phase_data in ppl.items():
            s_key = str(s)
            if s_key in phase_data:
                dense_ppl = phase_data[s_key].get("dense", 1.0)
                compound_ppl = phase_data[s_key].get("both", dense_ppl)
                if dense_ppl > 0:
                    ratios.append(compound_ppl / dense_ppl)
        if ratios:
            severity[s] = sum(ratios) / len(ratios)
    return severity


def compute_correlation(cond_results, dense_accuracy, ppl_base_dir):
    try:
        from scipy.stats import spearmanr
    except ImportError:
        print("  [warn] scipy not available, skipping correlation", flush=True)
        return {}

    sparsity_levels = [0.15, 0.20, 0.25, 0.30]
    correlations = {}

    for strategy in ["importance", "random"]:
        ppl_severity = load_ppl_severity(ppl_base_dir, strategy, sparsity_levels)

        acc_deltas = []
        ppl_vals = []
        matched_levels = []
        for s in sparsity_levels:
            cond_name = f"{strategy}_s{int(s*100):03d}"
            if cond_name in cond_results and s in ppl_severity:
                cr = cond_results[cond_name]
                acc = cr["correct"] / cr["total"] if cr["total"] > 0 else 0
                delta = acc - dense_accuracy
                acc_deltas.append(delta)
                ppl_vals.append(ppl_severity[s])
                matched_levels.append(s)

        if len(acc_deltas) >= 3:
            rho, p_value = spearmanr(ppl_vals, acc_deltas)
            correlations[strategy] = {
                "spearman_rho": round(float(rho), 4),
                "p_value": round(float(p_value), 4),
                "n_points": len(acc_deltas),
                "ppl_severity": {
                    f"s{int(s*100):03d}": round(ppl_severity[s], 4)
                    for s in matched_levels
                },
                "accuracy_deltas": {
                    f"s{int(s*100):03d}": round(d, 4)
                    for s, d in zip(matched_levels, acc_deltas)
                },
            }

    return correlations


def main():
    parser = argparse.ArgumentParser(description="R9-C2 Compound Sparsity Accuracy Eval")
    parser.add_argument("--model", default="/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B")
    parser.add_argument("--data", default="/root/autodl-tmp/pacs/data/math500.json")
    parser.add_argument("--output-dir", default="/root/autodl-tmp/pacs/analysis_output")
    parser.add_argument("--num-problems", type=int, default=500)
    parser.add_argument("--gpu", default="cuda:0")
    parser.add_argument("--conditions", default="dense,importance_s025",
                        help="Comma-separated condition names, or 'all'")
    parser.add_argument("--output-name", default="accuracy_eval_r9c2.json")
    parser.add_argument("--ppl-base-dir", default="/root/autodl-tmp/pacs")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)

    if args.conditions == "all":
        conditions = list(ALL_CONDITIONS)
    else:
        conditions = [c.strip() for c in args.conditions.split(",")]
        for c in conditions:
            if c not in CONDITION_SPECS:
                print(f"Unknown condition: {c}. Valid: {ALL_CONDITIONS}")
                sys.exit(1)

    t_start = time.time()

    print(f"Loading model: {args.model}", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16, device_map=args.gpu,
        trust_remote_code=True, attn_implementation='eager',
    )
    model.eval()
    print(f"Layers={model.config.num_hidden_layers}, Heads={model.config.num_attention_heads}, "
          f"KV_heads={getattr(model.config, 'num_key_value_heads', 'N/A')}", flush=True)

    with open(args.data) as f:
        data = json.load(f)
    problems = data[:args.num_problems]
    print(f"Loaded {len(problems)} problems, conditions: {conditions}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)

    cond_results = run_evaluation(model, tokenizer, problems, args.gpu, conditions)

    dense_accuracy = None
    output = {
        "config": {
            "model": args.model,
            "num_problems": len(problems),
            "max_new_tokens": 2048,
            "device": args.gpu,
            "conditions": conditions,
            "seed": args.seed,
        },
        "conditions": {},
    }

    for cond_name in conditions:
        cr = cond_results[cond_name]
        acc = cr["correct"] / cr["total"] if cr["total"] > 0 else 0
        output["conditions"][cond_name] = {
            "accuracy": round(acc, 4),
            "correct": cr["correct"],
            "n_problems": cr["total"],
            "details": cr["details"],
        }
        if cond_name == "dense":
            dense_accuracy = acc
            output["dense_accuracy"] = round(acc, 4)

    if dense_accuracy is not None:
        for cond_name in conditions:
            if cond_name != "dense":
                cr = cond_results[cond_name]
                acc = cr["correct"] / cr["total"] if cr["total"] > 0 else 0
                output["conditions"][cond_name]["delta"] = round(acc - dense_accuracy, 4)

    try:
        correlations = compute_correlation(cond_results, dense_accuracy or 0, args.ppl_base_dir)
        if correlations:
            output["correlation_with_ppl_gradient"] = correlations
    except Exception as e:
        print(f"  [warn] Correlation failed: {e}", flush=True)

    output["total_time_seconds"] = round(time.time() - t_start, 1)

    output_path = os.path.join(args.output_dir, args.output_name)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}", flush=True)
    print(f"RESULTS SAVED: {output_path}", flush=True)
    for cond_name in conditions:
        c = output["conditions"][cond_name]
        delta_str = f" (delta={c['delta']:+.1%})" if 'delta' in c else ""
        print(f"  {cond_name}: {c['accuracy']:.1%} ({c['correct']}/{c['n_problems']}){delta_str}", flush=True)
    if "correlation_with_ppl_gradient" in output:
        for strat, corr in output["correlation_with_ppl_gradient"].items():
            print(f"  Corr({strat}): rho={corr['spearman_rho']:.4f}, p={corr['p_value']:.4f}", flush=True)
    print(f"  Total time: {output['total_time_seconds']:.0f}s", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()
