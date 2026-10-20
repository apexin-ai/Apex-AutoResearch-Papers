import json, csv, os

BASE = "/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed"
conditions = ["Vanilla_s0", "Full_OCC_s0", "Detach_BN_s2", "Random_s2"]

data = {}
for c in conditions:
    path = os.path.join(BASE, f"{c}_gradient_stats.json")
    if os.path.exists(path):
        with open(path) as f:
            data[c] = json.load(f)
    else:
        print(f"MISSING: {path}")

def get_group(layer_name):
    prefix, idx = layer_name.rsplit("_", 1)
    idx = int(idx)
    if prefix == "dino":
        if idx <= 7: return "early"
        elif idx <= 15: return "mid"
        else: return "late"
    else:
        if idx <= 8: return "early"
        elif idx <= 17: return "mid"
        else: return "late"

rows = []
for cond in conditions:
    if cond not in data:
        continue
    layers = data[cond]["layers"]
    for ln, stats in layers.items():
        agn = stats["action_grad_norm"]["mean"]
        aug = stats.get("aux_grad_norm", {}).get("mean", None)
        if agn == 0 and (aug is None or aug == 0):
            continue
        prefix, idx_s = ln.rsplit("_", 1)
        cr = stats.get("conflict_rate", {}).get("mean", None)
        cs = stats.get("cosine_similarity", {}).get("mean", None)
        rows.append({
            "condition": cond,
            "encoder": prefix,
            "layer_idx": int(idx_s),
            "layer_name": ln,
            "group": get_group(ln),
            "conflict_rate": round(cr, 6) if cr is not None else "",
            "cosine_sim": round(cs, 6) if cs is not None else "",
            "action_grad_norm": round(agn, 6),
            "aux_grad_norm": round(aug, 6) if aug is not None else "",
        })

csv_path = os.path.join(BASE, "per_layer_conflict_rate_full.csv")
with open(csv_path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["condition","encoder","layer_idx","layer_name","group",
                                       "conflict_rate","cosine_sim","action_grad_norm","aux_grad_norm"])
    w.writeheader()
    w.writerows(rows)

for cond in conditions:
    if cond not in data:
        print(f"{cond}: NO DATA FILE")
        continue
    layers = data[cond]["layers"]
    sample_key = list(layers.keys())[0]
    fields = list(layers[sample_key].keys())
    has_cr = "conflict_rate" in fields
    n_layers = sum(1 for s in layers.values() if s["action_grad_norm"]["mean"] != 0 or s.get("aux_grad_norm", {}).get("mean", 0) != 0)
    print(f"{cond}: {n_layers} layers, fields={fields}, has_conflict_rate={has_cr}")

cond_counts = {}
for r in rows:
    c = r["condition"]
    cond_counts[c] = cond_counts.get(c, 0) + 1
print(f"\nTotal rows: {len(rows)}")
for c, n in cond_counts.items():
    print(f"  {c}: {n} rows")
print(f"Saved: {csv_path}")
