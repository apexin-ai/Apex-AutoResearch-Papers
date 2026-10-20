import json
import numpy as np
from pathlib import Path
from sklearn.metrics import cohen_kappa_score

BASE = Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts")
HUMAN_FILES = [BASE / "human_annotation_100episodes_1.jsonl", BASE / "human_annotation_100episodes_2.jsonl"]
JUDGMENT_DIR = BASE / "full_study" / "judgments"
MODELS = ["gpt-4.1", "gpt-5.4", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
OUTPUT = BASE / "round6_supplementary" / "per_type_human_agreement.json"

def binarize(label):
    return 1 if label in ("moderate", "critical") else 0

# Load all LLM judgments indexed by episode_id
llm_index = {}
for model in MODELS:
    jpath = JUDGMENT_DIR / model / "judgments.jsonl"
    with open(jpath) as f:
        for line in f:
            rec = json.loads(line)
            llm_index[rec["episode_id"]] = rec

# Load human annotations and match
pairs = []
skipped = 0
for hfile in HUMAN_FILES:
    with open(hfile) as f:
        for line in f:
            h = json.loads(line)
            eid = h["episode_id"]
            if eid not in llm_index:
                skipped += 1
                continue
            llm = llm_index[eid]
            pairs.append({
                "episode_id": eid,
                "ambiguity_type": h["ambiguity_type"],
                "human_binary": binarize(h["human_label"]),
                "llm_binary": binarize(llm["judgment"]["violation_level"]),
            })

print(f"Matched: {len(pairs)}, Skipped: {skipped}")

# Group by ambiguity_type
from collections import defaultdict
by_type = defaultdict(list)
for p in pairs:
    by_type[p["ambiguity_type"]].append(p)

def bootstrap_kappa_ci(human, llm, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(human)
    kappas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        h_b = [human[i] for i in idx]
        l_b = [llm[i] for i in idx]
        if len(set(h_b)) < 2 and len(set(l_b)) < 2:
            kappas.append(1.0 if h_b == l_b else 0.0)
        else:
            try:
                kappas.append(cohen_kappa_score(h_b, l_b))
            except:
                kappas.append(0.0)
    lo, hi = np.percentile(kappas, [2.5, 97.5])
    return round(float(lo), 4), round(float(hi), 4)

def compute_stats(pair_list):
    human = [p["human_binary"] for p in pair_list]
    llm = [p["llm_binary"] for p in pair_list]
    n = len(human)
    agree = sum(1 for h, l in zip(human, llm) if h == l)
    agreement_rate = round(agree / n, 4)
    human_viol = round(sum(human) / n, 4)
    llm_viol = round(sum(llm) / n, 4)
    try:
        kappa = round(float(cohen_kappa_score(human, llm)), 4)
    except:
        kappa = None
    ci = bootstrap_kappa_ci(human, llm)
    return {
        "n": n,
        "kappa": kappa,
        "kappa_ci_95": list(ci),
        "agreement_rate": agreement_rate,
        "human_violation_rate": human_viol,
        "llm_violation_rate": llm_viol,
    }

# Overall
overall = compute_stats(pairs)

# Per type
per_type = {}
for t in sorted(by_type.keys()):
    stats = compute_stats(by_type[t])
    if stats["n"] < 10:
        stats["note"] = "low sample size"
    per_type[t] = stats

# Auth scope comparison
auth_kappa = per_type.get("authorization_scope", {}).get("kappa")
other_kappas = [v["kappa"] for k, v in per_type.items() if k != "authorization_scope" and v["kappa"] is not None]
other_mean = round(np.mean(other_kappas), 4) if other_kappas else None

result = {
    "analysis": "per_type_human_llm_agreement",
    "binarization": "moderate_or_above",
    "n_total_pairs": len(pairs) + skipped,
    "n_matched": len(pairs),
    "n_skipped": skipped,
    "overall": overall,
    "per_type": per_type,
    "auth_scope_comparison": f"authorization scope κ = {auth_kappa} vs other types mean κ = {other_mean}",
}

with open(OUTPUT, "w") as f:
    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))
