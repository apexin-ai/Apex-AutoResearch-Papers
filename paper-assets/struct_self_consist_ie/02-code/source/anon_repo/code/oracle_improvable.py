import json
import sys
import os

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from evaluation import per_instance_f1

CONFIGS = {
    "qwen_scierc_ner": {
        "path": "exp_012_rerun_1024/samples.jsonl",
        "subtask": "ner",
    },
    "qwen_scierc_re": {
        "path": "exp_012_rerun_1024/samples.jsonl",
        "subtask": "re",
    },
    "llama_scierc_ner": {
        "path": "exp007_llama_inference/samples.jsonl",
        "subtask": "ner",
    },
    "qwen_conll_ner": {
        "path": "exp002_conll2003/samples.jsonl",
        "subtask": "ner",
    },
    "llama_conll_ner": {
        "path": "exp_017_llama_conll_infer/samples.jsonl",
        "subtask": "ner",
    },
}

OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output"

def gold_nonempty(gold, subtask):
    if subtask == "ner":
        return len(gold.get("entities", [])) > 0
    elif subtask == "re":
        return len(gold.get("relations", [])) > 0
    elif subtask == "eae":
        return len(gold.get("events", [])) > 0
    return False

results = {}

for config_name, cfg in CONFIGS.items():
    fpath = os.path.join(OUTPUT_DIR, cfg["path"])
    subtask = cfg["subtask"]

    instances = []
    with open(fpath) as f:
        for line in f:
            instances.append(json.loads(line))

    n_total = 0
    n_improvable = 0
    n_degradable = 0
    n_tied = 0
    headrooms = []
    degradations = []

    for inst in instances:
        gold = inst["gold"]
        if not gold_nonempty(gold, subtask):
            continue

        n_total += 1
        greedy = inst.get("greedy")
        greedy_f1 = per_instance_f1(greedy, gold, subtask) if greedy else 0.0

        samples = inst.get("samples", [])
        sample_f1s = [per_instance_f1(s, gold, subtask) for s in samples]
        oracle_f1 = max(sample_f1s) if sample_f1s else 0.0

        if oracle_f1 > greedy_f1 + 1e-9:
            n_improvable += 1
            headrooms.append(oracle_f1 - greedy_f1)
        elif oracle_f1 < greedy_f1 - 1e-9:
            n_degradable += 1
            degradations.append(greedy_f1 - oracle_f1)
        else:
            n_tied += 1

    results[config_name] = {
        "n_total": n_total,
        "n_improvable": n_improvable,
        "n_degradable": n_degradable,
        "n_tied": n_tied,
        "improvable_fraction": round(n_improvable / n_total, 4) if n_total else 0,
        "mean_headroom_improvable": round(sum(headrooms) / len(headrooms), 4) if headrooms else 0,
        "mean_degradation_degradable": round(sum(degradations) / len(degradations), 4) if degradations else 0,
    }

os.makedirs(os.path.join(OUTPUT_DIR, "review_round2"), exist_ok=True)
out_path = os.path.join(OUTPUT_DIR, "review_round2/oracle_improvable_fraction.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)

# Print table
print(f"{'Config':<22} {'Total':>6} {'Improv':>7} {'Degrad':>7} {'Tied':>6} {'Imp%':>8} {'Headroom':>10} {'Degrad':>10}")
print("-" * 90)
for name, r in results.items():
    print(f"{name:<22} {r['n_total']:>6} {r['n_improvable']:>7} {r['n_degradable']:>7} {r['n_tied']:>6} {r['improvable_fraction']:>8.4f} {r['mean_headroom_improvable']:>10.4f} {r['mean_degradation_degradable']:>10.4f}")

print(f"\nSaved to {out_path}")
