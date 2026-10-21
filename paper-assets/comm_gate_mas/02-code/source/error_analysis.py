import json
import os
import numpy as np
from collections import defaultdict

def load_heuristic_files(directory, prefix="seed_"):
    """Load all seed JSON files from a heuristic pruning directory."""
    results = {}
    for f in sorted(os.listdir(directory)):
        if f.startswith(prefix) and f.endswith(".json"):
            seed = f.replace(prefix, "").replace(".json", "")
            with open(os.path.join(directory, f)) as fh:
                results[seed] = json.load(fh)
    return results

def analyze_discordant(per_task, baseline_key="baseline_correct", pruned_key="pruned_correct", suppressed_key="suppressed"):
    """Analyze discordant pairs in a single seed's per_task data."""
    concordant_correct = 0
    concordant_wrong = 0
    regressed = []  # baseline correct -> pruned wrong
    improved = []   # baseline wrong -> pruned correct
    
    for t in per_task:
        bl = t[baseline_key]
        pr = t[pruned_key]
        if bl and pr:
            concordant_correct += 1
        elif not bl and not pr:
            concordant_wrong += 1
        elif bl and not pr:
            regressed.append(t)
        else:
            improved.append(t)
    
    total = len(per_task)
    n_discordant = len(regressed) + len(improved)
    
    return {
        "total": total,
        "concordant_correct": concordant_correct,
        "concordant_wrong": concordant_wrong,
        "n_regressed": len(regressed),
        "n_improved": len(improved),
        "n_discordant": n_discordant,
        "discordant_rate": n_discordant / total if total > 0 else 0,
        "regressed_tasks": regressed,
        "improved_tasks": improved,
    }

def suppression_stats(tasks, suppressed_key="suppressed"):
    """Compute suppression statistics for a list of tasks."""
    if not tasks:
        return {"mean": 0, "median": 0, "min": 0, "max": 0, "std": 0}
    vals = [t[suppressed_key] for t in tasks]
    return {
        "mean": float(np.mean(vals)),
        "median": float(np.median(vals)),
        "min": int(np.min(vals)),
        "max": int(np.max(vals)),
        "std": float(np.std(vals, ddof=1)) if len(vals) > 1 else 0,
    }

# ============================================================
# 1. Qwen heuristic 10-seed
# ============================================================
print("=" * 60)
print("QWEN HEURISTIC 10-SEED ANALYSIS")
print("=" * 60)

qwen_seeds = {}
for d in ["/root/autodl-tmp/comm_gate_mas/outputs/heuristic_sync/replication_5run",
          "/root/autodl-tmp/comm_gate_mas/outputs/heuristic_sync/replication_10run"]:
    qwen_seeds.update(load_heuristic_files(d))

# Remove baseline files (prefix "baseline_")
qwen_seeds = {k: v for k, v in qwen_seeds.items() if not k.startswith("baseline")}

print(f"Loaded {len(qwen_seeds)} seeds: {sorted(qwen_seeds.keys())}")

qwen_results = {}
all_regressed = []
all_improved = []
all_concordant_tasks = []

for seed, data in sorted(qwen_seeds.items()):
    res = analyze_discordant(data["per_task"])
    qwen_results[seed] = res
    all_regressed.extend(res["regressed_tasks"])
    all_improved.extend(res["improved_tasks"])
    
    bl_acc = data["baseline"]["accuracy"]
    pr_acc = data["online_pruned"]["accuracy"]
    supp_pct = data["online_pruned"]["suppress_pct"]
    
    print(f"\nSeed {seed}: baseline={bl_acc:.1%}, pruned={pr_acc:.1%}, suppress={supp_pct:.1f}%")
    print(f"  Concordant: {res['concordant_correct']} correct, {res['concordant_wrong']} wrong")
    print(f"  Discordant: {res['n_regressed']} regressed, {res['n_improved']} improved ({res['n_discordant']}/{res['total']}={res['discordant_rate']:.1%})")

# Aggregate
total_tasks = sum(r["total"] for r in qwen_results.values())
total_disc = sum(r["n_discordant"] for r in qwen_results.values())
total_reg = sum(r["n_regressed"] for r in qwen_results.values())
total_imp = sum(r["n_improved"] for r in qwen_results.values())

print(f"\n--- QWEN AGGREGATE ---")
print(f"Total tasks: {total_tasks} ({len(qwen_results)} seeds x 200)")
print(f"Total discordant: {total_disc}/{total_tasks} = {total_disc/total_tasks:.2%}")
print(f"  Regressed: {total_reg} ({total_reg/total_tasks:.2%})")
print(f"  Improved:  {total_imp} ({total_imp/total_tasks:.2%})")
if total_reg + total_imp > 0:
    print(f"  Ratio improved/regressed: {total_imp}/{total_reg} = {total_imp/total_reg:.2f}" if total_reg > 0 else f"  No regressions!")

# Suppression analysis for discordant vs concordant
all_tasks_flat = []
for seed, data in qwen_seeds.items():
    for t in data["per_task"]:
        t["_seed"] = seed
        all_tasks_flat.append(t)

concordant = [t for t in all_tasks_flat if t["baseline_correct"] == t["pruned_correct"]]
discordant = [t for t in all_tasks_flat if t["baseline_correct"] != t["pruned_correct"]]

print(f"\n--- SUPPRESSION STATS ---")
print(f"Concordant tasks ({len(concordant)}):")
cs = suppression_stats(concordant)
print(f"  suppressed msgs: mean={cs['mean']:.2f}, median={cs['median']:.1f}, std={cs['std']:.2f}")
print(f"Discordant tasks ({len(discordant)}):")
ds = suppression_stats(discordant)
print(f"  suppressed msgs: mean={ds['mean']:.2f}, median={ds['median']:.1f}, std={ds['std']:.2f}")
print(f"Regressed tasks ({len(all_regressed)}):")
rs = suppression_stats(all_regressed)
print(f"  suppressed msgs: mean={rs['mean']:.2f}, median={rs['median']:.1f}, std={rs['std']:.2f}")
print(f"Improved tasks ({len(all_improved)}):")
ims = suppression_stats(all_improved)
print(f"  suppressed msgs: mean={ims['mean']:.2f}, median={ims['median']:.1f}, std={ims['std']:.2f}")

# Breakdown by suppression count
print(f"\n--- DISCORDANT BY SUPPRESSION COUNT ---")
supp_bins = defaultdict(lambda: {"regressed": 0, "improved": 0, "concordant": 0})
for t in all_tasks_flat:
    s = t["suppressed"]
    if t["baseline_correct"] and not t["pruned_correct"]:
        supp_bins[s]["regressed"] += 1
    elif not t["baseline_correct"] and t["pruned_correct"]:
        supp_bins[s]["improved"] += 1
    else:
        supp_bins[s]["concordant"] += 1

for s in sorted(supp_bins.keys()):
    b = supp_bins[s]
    total_at_s = b["regressed"] + b["improved"] + b["concordant"]
    disc_at_s = b["regressed"] + b["improved"]
    print(f"  suppressed={s}: total={total_at_s}, discordant={disc_at_s} ({disc_at_s/total_at_s:.1%}) [reg={b['regressed']}, imp={b['improved']}]")

# Baseline correctness of discordant tasks
print(f"\n--- BASELINE DIFFICULTY OF DISCORDANT TASKS ---")
baseline_correct_rate_all = sum(1 for t in all_tasks_flat if t["baseline_correct"]) / len(all_tasks_flat)
print(f"Overall baseline accuracy: {baseline_correct_rate_all:.1%}")

# ============================================================
# 2. Llama heuristic (1 seed, N=300)
# ============================================================
print("\n" + "=" * 60)
print("LLAMA HEURISTIC 1-SEED (N=300)")
print("=" * 60)

llama_heur = json.load(open("/root/autodl-tmp/comm_gate_mas/outputs/e2e_llama_n300_clean/seed42_heuristic.json"))
lr = analyze_discordant(llama_heur["per_task"])
print(f"Baseline={llama_heur['baseline']['accuracy']:.1%}, Pruned={llama_heur['online_pruned']['accuracy']:.1%}")
print(f"Concordant: {lr['concordant_correct']} correct, {lr['concordant_wrong']} wrong")
print(f"Discordant: {lr['n_regressed']} regressed, {lr['n_improved']} improved ({lr['n_discordant']}/{lr['total']}={lr['discordant_rate']:.1%})")
if lr["n_regressed"] > 0:
    lr_supp = suppression_stats(lr["regressed_tasks"])
    print(f"Regressed suppression: mean={lr_supp['mean']:.2f}")
if lr["n_improved"] > 0:
    li_supp = suppression_stats(lr["improved_tasks"])
    print(f"Improved suppression: mean={li_supp['mean']:.2f}")

# ============================================================
# 3. Llama oracle 10-seed (cross-reference)
# ============================================================
print("\n" + "=" * 60)
print("LLAMA ORACLE 10-SEED (cross-reference)")
print("=" * 60)

llama_oracle_dir = "/root/autodl-tmp/comm_gate_mas/outputs/oracle_llama_10run"
llama_oracle_seeds = load_heuristic_files(llama_oracle_dir)
print(f"Loaded {len(llama_oracle_seeds)} seeds")

lo_total_reg = 0
lo_total_imp = 0
lo_total = 0

for seed, data in sorted(llama_oracle_seeds.items()):
    res = analyze_discordant(data["per_task"], 
                              baseline_key="baseline_correct",
                              pruned_key="oracle_pruned_correct",
                              suppressed_key="messages_suppressed")
    lo_total += res["total"]
    lo_total_reg += res["n_regressed"]
    lo_total_imp += res["n_improved"]
    print(f"  Seed {seed}: {res['n_discordant']}/{res['total']} discordant (reg={res['n_regressed']}, imp={res['n_improved']})")

lo_total_disc = lo_total_reg + lo_total_imp
print(f"Aggregate: {lo_total_disc}/{lo_total} = {lo_total_disc/lo_total:.2%} discordant")
print(f"  Regressed: {lo_total_reg}, Improved: {lo_total_imp}")

# ============================================================
# 4. Qwen oracle 10-seed (cross-reference)  
# ============================================================
print("\n" + "=" * 60)
print("QWEN ORACLE 10-SEED (cross-reference)")
print("=" * 60)

qwen_oracle_dir = "/root/autodl-tmp/comm_gate_mas/outputs/oracle_qwen_10run"
qwen_oracle_seeds = load_heuristic_files(qwen_oracle_dir)
print(f"Loaded {len(qwen_oracle_seeds)} seeds")

qo_total_reg = 0
qo_total_imp = 0
qo_total = 0

for seed, data in sorted(qwen_oracle_seeds.items()):
    res = analyze_discordant(data["per_task"],
                              baseline_key="baseline_correct",
                              pruned_key="oracle_pruned_correct",
                              suppressed_key="messages_suppressed")
    qo_total += res["total"]
    qo_total_reg += res["n_regressed"]
    qo_total_imp += res["n_improved"]
    print(f"  Seed {seed}: {res['n_discordant']}/{res['total']} discordant (reg={res['n_regressed']}, imp={res['n_improved']})")

qo_total_disc = qo_total_reg + qo_total_imp
print(f"Aggregate: {qo_total_disc}/{qo_total} = {qo_total_disc/qo_total:.2%} discordant")
print(f"  Regressed: {qo_total_reg}, Improved: {qo_total_imp}")

# ============================================================
# 5. Export data
# ============================================================
export = {
    "qwen_heuristic_10seed": {
        "seeds": {},
        "aggregate": {
            "total_tasks": total_tasks,
            "total_discordant": total_disc,
            "total_regressed": total_reg,
            "total_improved": total_imp,
            "discordant_rate": total_disc / total_tasks,
            "suppression_stats": {
                "concordant": cs,
                "discordant": ds,
                "regressed": rs,
                "improved": ims,
            },
            "suppression_breakdown": {str(k): v for k, v in sorted(supp_bins.items())},
        }
    },
    "llama_heuristic_1seed": {
        "total": lr["total"],
        "n_regressed": lr["n_regressed"],
        "n_improved": lr["n_improved"],
        "discordant_rate": lr["discordant_rate"],
    },
    "llama_oracle_10seed": {
        "total": lo_total,
        "total_regressed": lo_total_reg,
        "total_improved": lo_total_imp,
        "discordant_rate": lo_total_disc / lo_total,
    },
    "qwen_oracle_10seed": {
        "total": qo_total,
        "total_regressed": qo_total_reg,
        "total_improved": qo_total_imp,
        "discordant_rate": qo_total_disc / qo_total,
    },
}

for seed, data in sorted(qwen_seeds.items()):
    r = qwen_results[seed]
    export["qwen_heuristic_10seed"]["seeds"][seed] = {
        "baseline_acc": data["baseline"]["accuracy"],
        "pruned_acc": data["online_pruned"]["accuracy"],
        "suppress_pct": data["online_pruned"]["suppress_pct"],
        "n_regressed": r["n_regressed"],
        "n_improved": r["n_improved"],
        "discordant_rate": r["discordant_rate"],
        "regressed_task_ids": [t["task_id"] for t in r["regressed_tasks"]],
        "improved_task_ids": [t["task_id"] for t in r["improved_tasks"]],
        "regressed_suppression": [t["suppressed"] for t in r["regressed_tasks"]],
        "improved_suppression": [t["suppressed"] for t in r["improved_tasks"]],
    }

with open("/root/autodl-tmp/comm_gate_mas/outputs/error_analysis_data.json", "w") as f:
    json.dump(export, f, indent=2)
print("\nExported to outputs/error_analysis_data.json")
