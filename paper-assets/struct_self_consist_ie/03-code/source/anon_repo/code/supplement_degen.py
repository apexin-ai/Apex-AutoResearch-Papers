import sys
sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from unified_metrics import load_and_filter, compute_sample_f1s, compute_degeneracy
import json

targets = [
    ("rank8_scierc", "/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl"),
    ("n32_scierc", "/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/samples.jsonl"),
    ("n16_scierc_seed42", "/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/samples.jsonl"),
    ("fewnerd_n8_seed42", "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl"),
]

results = {}
for name, path in targets:
    instances = load_and_filter(path, gold_filter=True)
    n_total = len(instances)
    n_degen = 0
    for inst in instances:
        f1s = compute_sample_f1s(inst)
        if compute_degeneracy(f1s):
            n_degen += 1
    degen_pct = round(n_degen / n_total * 100, 2)
    results[name] = {"n_total": n_total, "n_degen": n_degen, "degen_pct": degen_pct}
    print(f"{name}: {n_degen}/{n_total} = {degen_pct}%")

with open("/root/autodl-tmp/struct_self_consist_ie/output/supplement_degen_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nDone. Results saved.")
