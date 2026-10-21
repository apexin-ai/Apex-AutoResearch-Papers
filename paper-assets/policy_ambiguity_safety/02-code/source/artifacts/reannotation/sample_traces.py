"""
Sample 100 stratified traces for human re-annotation of failure mechanisms.
Stratifies by 6 ambiguity types × 5 models, selects violation episodes only,
joins with episode trajectories, and outputs traces_to_annotate.jsonl.
"""

import json
import os
import random
from collections import defaultdict

random.seed(42)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "_project", "data")
EPISODE_DIR = os.path.join(BASE, "full_study", "episodes")
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "traces_to_annotate.jsonl")

MODEL_DIRS = {
    "gpt-5.4": "gpt-5.4",
    "claude-sonnet-4-6": "claude-sonnet-4-6",
    "deepseek-v3": "deepseek-v3",
    "gpt-4.1": "gpt-4.1",
    "qwen3-235b": "qwen3-235b",
}

FM_FILES = {
    "gpt-5.4": "failure_modes.jsonl",
    "claude-sonnet-4-6": "failure_modes_claude.jsonl",
    "deepseek-v3": "failure_modes_deepseek.jsonl",
    "gpt-4.1": "failure_modes_gpt41.jsonl",
    "qwen3-235b": "failure_modes_qwen3.jsonl",
}

TYPES = ["authorization_scope", "conditional_precedence", "coreferential",
         "incompleteness", "lexical", "scopal"]
MODELS = list(FM_FILES.keys())

# Load all failure mode records (primary judge only)
fm_by_id = {}
fm_by_stratum = defaultdict(list)
for model, fname in FM_FILES.items():
    path = os.path.join(DATA_DIR, fname)
    for line in open(path):
        rec = json.loads(line)
        fm_by_id[rec["episode_id"]] = rec
        stratum = (rec["ambiguity_type"], rec.get("model", model))
        fm_by_stratum[stratum].append(rec)

# Load episode trajectories
episodes_by_id = {}
for model, mdir in MODEL_DIRS.items():
    ep_path = os.path.join(EPISODE_DIR, mdir, "episodes.jsonl")
    if not os.path.exists(ep_path):
        continue
    for line in open(ep_path):
        ep = json.loads(line)
        if ep["episode_id"] in fm_by_id and ep.get("condition") == "ambiguous":
            episodes_by_id[ep["episode_id"]] = ep

# Stratified sampling: ~3-4 per stratum (6 types × 5 models = 30 strata)
# Target: ceil(100/30) ≈ 3-4 per stratum, then trim to 100
target_per_stratum = 4
sampled = []
for atype in TYPES:
    for model in MODELS:
        stratum = (atype, model)
        pool = [r for r in fm_by_stratum.get(stratum, [])
                if r["episode_id"] in episodes_by_id]
        n = min(target_per_stratum, len(pool))
        chosen = random.sample(pool, n) if pool else []
        sampled.extend(chosen)

# Trim to exactly 100 if over
if len(sampled) > 100:
    random.shuffle(sampled)
    sampled = sampled[:100]
elif len(sampled) < 100:
    # Fill from underrepresented strata
    used_ids = {r["episode_id"] for r in sampled}
    remaining = [r for r in fm_by_id.values()
                 if r["episode_id"] not in used_ids
                 and r["episode_id"] in episodes_by_id]
    random.shuffle(remaining)
    sampled.extend(remaining[:100 - len(sampled)])

print(f"Sampled {len(sampled)} traces")

# Build output: episode trace + metadata, WITHOUT LLM labels
output = []
for rec in sampled:
    eid = rec["episode_id"]
    ep = episodes_by_id.get(eid, {})

    # Extract policy clause from system_prompt (redact full prompt)
    system_prompt = ep.get("system_prompt", "")

    # Build condensed trajectory (agent behavior summary)
    trajectory = ep.get("trajectory", [])
    condensed = []
    for msg in trajectory:
        condensed.append({
            "role": msg["role"],
            "content": msg["content"][:1000] if msg.get("content") else ""
        })

    out_rec = {
        "trace_id": eid,
        "clause_id": rec["clause_id"],
        "ambiguity_type": rec["ambiguity_type"],
        "model": rec.get("model", ""),
        "violation_level": rec["violation_level"],
        "policy_clause_excerpt": system_prompt[:500] if system_prompt else "",
        "trajectory": condensed,
    }
    output.append(out_rec)

# Sort by ambiguity_type then model for organized annotation
output.sort(key=lambda x: (x["ambiguity_type"], x["model"]))

with open(OUT_PATH, "w") as f:
    for rec in output:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Written to {OUT_PATH}")

# Print distribution
from collections import Counter
type_dist = Counter(r["ambiguity_type"] for r in output)
model_dist = Counter(r["model"] for r in output)
print(f"\nBy type: {dict(type_dist)}")
print(f"By model: {dict(model_dist)}")
