"""
tab3_mechanism_verification analysis.
Computes empirical metrics from advantage_log.jsonl for paper Table 3.
"""
import json
import numpy as np
from collections import defaultdict
from math import comb, sqrt
from scipy.special import comb as scomb

LOG_PATH = "/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl"

# Load data
records = []
with open(LOG_PATH) as f:
    for line in f:
        if line.strip():
            records.append(json.loads(line))

print(f"Total records: {len(records)}")

# Build episodes
episodes = defaultdict(list)
for r in records:
    episodes[r["episode_id"]].append(r)
for eid in episodes:
    episodes[eid].sort(key=lambda x: x["window_position"])

# Classify episode outcomes
outcomes = {}
for eid, windows in episodes.items():
    max_ret = max(w["step_return"] for w in windows)
    outcomes[eid] = 1 if max_ret > 1.0 else 0

n_episodes = len(episodes)
n_success_ep = sum(outcomes.values())
n_fail_ep = n_episodes - n_success_ep
ep_success_rate = n_success_ep / n_episodes

print(f"Episodes: {n_episodes} (success={n_success_ep}, fail={n_fail_ep}, rate={ep_success_rate:.4f})")
print(f"Unique uids: {sorted(set(r['uid'] for r in records))}")

# Show episode count per uid
uid_episodes = defaultdict(set)
for r in records:
    uid_episodes[r["uid"]].add(r["episode_id"])
print(f"Episodes per uid: {[(uid, len(eids)) for uid, eids in sorted(uid_episodes.items(), key=lambda x: int(x[0]))]}")

# ============================================================
# 1. P(correct sign | per-sample)
# ============================================================
correct = 0
total = 0
for r in records:
    eid = r["episode_id"]
    if eid not in outcomes:
        continue
    total += 1
    is_success = outcomes[eid] == 1
    adv_pos = r["advantage"] > 0
    if (adv_pos and is_success) or (not adv_pos and not is_success):
        correct += 1

p_correct_per_sample = correct / total
print(f"\n=== P(correct sign | per-sample) = {p_correct_per_sample:.4f} ({correct}/{total}) ===")

# ============================================================
# 2. Try to form GRPO groups
# ============================================================
K = 8

uid_ep_lists = {}
for uid, eids in uid_episodes.items():
    uid_ep_lists[uid] = sorted(eids)

groups = []
for uid in sorted(uid_ep_lists.keys(), key=int):
    ep_list = uid_ep_lists[uid]
    for i in range(0, len(ep_list), K):
        batch = ep_list[i:i+K]
        if len(batch) >= 2:
            groups.append({"uid": uid, "episode_ids": batch})

print(f"\nFormed {len(groups)} GRPO groups (K={K} target)")
print(f"Group sizes: {[len(g['episode_ids']) for g in groups]}")

# ============================================================
# 2a. P(correct sign | group majority)
# ============================================================
group_majority_correct = 0
n_valid_groups = 0

for g in groups:
    eids = g["episode_ids"]
    correct_in_group = 0
    total_in_group = 0
    for eid in eids:
        if eid not in outcomes:
            continue
        ep_windows = episodes[eid]
        ep_adv_mean = np.mean([w["advantage"] for w in ep_windows])
        is_success = outcomes[eid] == 1
        adv_pos = ep_adv_mean > 0
        total_in_group += 1
        if (adv_pos and is_success) or (not adv_pos and not is_success):
            correct_in_group += 1

    if total_in_group > 0:
        n_valid_groups += 1
        if correct_in_group > total_in_group / 2:
            group_majority_correct += 1

p_group_majority = group_majority_correct / n_valid_groups if n_valid_groups > 0 else 0
print(f"\n=== P(correct sign | group majority) = {p_group_majority:.4f} ({group_majority_correct}/{n_valid_groups}) ===")

# ============================================================
# 2b. P(correct direction | normalized advantage)
# ============================================================
correct_normalized = 0
total_normalized = 0

for g in groups:
    eids = g["episode_ids"]
    group_windows = []
    for eid in eids:
        if eid not in outcomes:
            continue
        for w in episodes[eid]:
            group_windows.append({**w, "outcome": outcomes[eid]})

    if len(group_windows) < 2:
        continue

    advs = np.array([w["advantage"] for w in group_windows])
    group_mean = np.mean(advs)

    for i, w in enumerate(group_windows):
        normalized_adv = advs[i] - group_mean
        total_normalized += 1
        adv_pos = normalized_adv > 0
        is_success = w["outcome"] == 1
        if (adv_pos and is_success) or (not adv_pos and not is_success):
            correct_normalized += 1

p_correct_normalized = correct_normalized / total_normalized if total_normalized > 0 else 0
print(f"\n=== P(correct direction | normalized) = {p_correct_normalized:.4f} ({correct_normalized}/{total_normalized}) ===")

# ============================================================
# 2c. Normalize by episode-level returns within group
# ============================================================
correct_ep_norm = 0
total_ep_norm = 0

for g in groups:
    eids = g["episode_ids"]
    ep_returns = {}
    for eid in eids:
        if eid not in outcomes:
            continue
        ep_windows = episodes[eid]
        ep_returns[eid] = max(w["step_return"] for w in ep_windows)

    if len(ep_returns) < 2:
        continue

    returns = np.array(list(ep_returns.values()))
    ep_ids_list = list(ep_returns.keys())
    ret_mean = np.mean(returns)

    for i, eid in enumerate(ep_ids_list):
        norm_adv = returns[i] - ret_mean
        is_success = outcomes[eid] == 1
        n_windows = len(episodes[eid])

        for _ in range(n_windows):
            total_ep_norm += 1
            adv_pos = norm_adv > 0
            if (adv_pos and is_success) or (not adv_pos and not is_success):
                correct_ep_norm += 1

p_correct_ep_norm = correct_ep_norm / total_ep_norm if total_ep_norm > 0 else 0
print(f"\n=== P(correct direction | episode-level normalization) = {p_correct_ep_norm:.4f} ({correct_ep_norm}/{total_ep_norm}) ===")

# ============================================================
# 2d. Step-level correctness analysis
# ============================================================
correct_step = 0
total_step = 0
for r in records:
    eid = r["episode_id"]
    if eid not in outcomes:
        continue
    total_step += 1
    step_good = r["step_return"] > 0
    adv_pos = r["advantage"] > 0
    if (adv_pos and step_good) or (not adv_pos and not step_good):
        correct_step += 1

p_correct_step = correct_step / total_step
print(f"\n=== P(correct sign | step-level quality, ret>0) = {p_correct_step:.4f} ({correct_step}/{total_step}) ===")

correct_step2 = 0
for r in records:
    eid = r["episode_id"]
    if eid not in outcomes:
        continue
    step_good = r["step_return"] >= 0
    adv_pos = r["advantage"] > 0
    if (adv_pos and step_good) or (not adv_pos and not step_good):
        correct_step2 += 1

p_correct_step2 = correct_step2 / total
print(f"  (with step_return>=0 threshold: {p_correct_step2:.4f} ({correct_step2}/{total}))")

# ============================================================
# 3. Window position analysis (early vs late)
# ============================================================
by_pos = defaultdict(lambda: {"correct": 0, "total": 0})
for r in records:
    eid = r["episode_id"]
    if eid not in outcomes:
        continue
    pos = r["window_position"]
    by_pos[pos]["total"] += 1
    is_success = outcomes[eid] == 1
    adv_pos = r["advantage"] > 0
    if (adv_pos and is_success) or (not adv_pos and not is_success):
        by_pos[pos]["correct"] += 1

positions = sorted(by_pos.keys())
max_pos = max(positions)

early_threshold = max_pos / 3
late_threshold = max_pos * 2 / 3

early_correct = 0
early_total = 0
late_correct = 0
late_total = 0

for pos in positions:
    if pos <= early_threshold:
        early_correct += by_pos[pos]["correct"]
        early_total += by_pos[pos]["total"]
    elif pos >= late_threshold:
        late_correct += by_pos[pos]["correct"]
        late_total += by_pos[pos]["total"]

sign_early = early_correct / early_total if early_total > 0 else 0
sign_late = late_correct / late_total if late_total > 0 else 0

print(f"\n=== Window position analysis ===")
print(f"Early (pos 0-{int(early_threshold)}): {sign_early:.4f} ({early_correct}/{early_total})")
print(f"Late (pos {int(late_threshold)}-{max_pos}): {sign_late:.4f} ({late_correct}/{late_total})")

print(f"\nPer-position sign-outcome agreement:")
for pos in positions:
    d = by_pos[pos]
    if d["total"] > 0:
        rate = d["correct"] / d["total"]
        print(f"  pos {pos:2d}: {rate:.4f} (n={d['total']})")

# ============================================================
# 4. Step_return distribution analysis
# ============================================================
step_returns = [r["step_return"] for r in records]
print(f"\n=== Step return distribution ===")
print(f"  min={min(step_returns):.4f}, max={max(step_returns):.4f}")
print(f"  mean={np.mean(step_returns):.4f}, median={np.median(step_returns):.4f}")
print(f"  n(>0)={sum(1 for s in step_returns if s > 0)}")
print(f"  n(=0)={sum(1 for s in step_returns if s == 0)}")
print(f"  n(<0)={sum(1 for s in step_returns if s < 0)}")

ep_lengths = {eid: len(wins) for eid, wins in episodes.items()}
print(f"\n=== Episode length distribution ===")
for l in sorted(set(ep_lengths.values())):
    n = sum(1 for v in ep_lengths.values() if v == l)
    print(f"  length {l}: {n} episodes")

# ============================================================
# 5. Theoretical predictions
# ============================================================
print(f"\n=== Theoretical analysis ===")

h = 2
print(f"Episode success rate: {ep_success_rate:.4f}")

p_base = ep_success_rate ** (1.0 / h)
print(f"Inferred base step success rate p = {p_base:.4f} (from p^h = {ep_success_rate:.4f})")

p_ep = ep_success_rate
p_step = p_base

p_step_correct_given_fail = (p_step - p_step**h) / (1 - p_step**h) if p_step**h < 1 else 0
print(f"P(step correct | failed episode) = {p_step_correct_given_fail:.4f}")

# P(misattribution) = P(step correct in failed ep, gets negative advantage)
# = P(episode fails AND step correct) = p - p^h = p*(1 - p^(h-1))
p_wrong = p_step * (1 - p_step**(h-1))
print(f"\nP(misattribution per step) = p*(1-p^(h-1))")
print(f"  = {p_step:.4f} * (1 - {p_step**(h-1):.4f})")
print(f"  = {p_wrong:.4f}")
print(f"P(correct direction per step) = 1 - P(wrong) = {1-p_wrong:.4f}")

# GRPO-adjusted: condition on informative groups (0 < m < K)
p_correct_theory = 0.0
for m in range(1, K):
    p_m = scomb(K, m, exact=True) * (p_ep ** m) * ((1 - p_ep) ** (K - m))
    p_correct_given_m = m / K + (K - m) / K * (1 - p_step_correct_given_fail)
    p_correct_theory += p_m * p_correct_given_m
    print(f"  m={m}: P(m)={p_m:.4f}, P(correct|m)={p_correct_given_m:.4f}")

p_informative = sum(scomb(K, m, exact=True) * (p_ep ** m) * ((1 - p_ep) ** (K - m)) for m in range(1, K))
p_correct_theory_normalized = p_correct_theory / p_informative if p_informative > 0 else 0

print(f"\nP(informative group, 0<m<K) = {p_informative:.4f}")
print(f"P(correct direction | step, theory, normalized) = {p_correct_theory_normalized:.4f}")

p_misattrib_grpo = 0.0
for m in range(1, K):
    p_m = scomb(K, m, exact=True) * (p_ep ** m) * ((1 - p_ep) ** (K - m))
    misattrib_rate = (K - m) / K * p_step_correct_given_fail
    p_misattrib_grpo += p_m * misattrib_rate

p_misattrib_grpo_norm = p_misattrib_grpo / p_informative if p_informative > 0 else 0
print(f"GRPO P(misattribution per step, normalized) = {p_misattrib_grpo_norm:.4f}")

# ============================================================
# 6. Empirical step-level misattribution rate
# ============================================================
misattrib_count = 0
total_fail_good_steps = 0
total_steps_all = 0

for r in records:
    eid = r["episode_id"]
    if eid not in outcomes:
        continue
    total_steps_all += 1
    is_success = outcomes[eid] == 1
    step_good = r["step_return"] >= 0

    if not is_success and step_good:
        total_fail_good_steps += 1
        if r["advantage"] < 0:
            misattrib_count += 1

print(f"\n=== Step-level misattribution (failed episodes, good steps) ===")
print(f"Failed episodes, good steps: {total_fail_good_steps}/{total_steps_all}")
print(f"Of those, negative advantage (misattributed): {misattrib_count}")
p_misattrib_empirical = misattrib_count / total_steps_all if total_steps_all > 0 else 0
print(f"P(misattribution) = misattributed / total_steps = {p_misattrib_empirical:.4f}")

# Also with step_return > 0 strictly
total_fail_good2 = 0
misattrib2 = 0
for r in records:
    eid = r["episode_id"]
    if eid not in outcomes:
        continue
    is_success = outcomes[eid] == 1
    if not is_success and r["step_return"] > 0:
        total_fail_good2 += 1
        if r["advantage"] < 0:
            misattrib2 += 1

print(f"\nWith step_return > 0: {total_fail_good2} good steps in failed episodes, {misattrib2} misattributed")

n_zero_return = sum(1 for r in records if r["step_return"] == 0.0)
n_zero_success = sum(1 for r in records if r["step_return"] == 0.0 and outcomes[r["episode_id"]] == 1)
n_zero_fail = sum(1 for r in records if r["step_return"] == 0.0 and outcomes[r["episode_id"]] == 0)
print(f"\nstep_return=0: total={n_zero_return}, in_success_ep={n_zero_success}, in_fail_ep={n_zero_fail}")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("FINAL SUMMARY FOR TAB3")
print("="*60)
print(f"N samples: {len(records)}")
print(f"N episodes: {n_episodes} (success={n_success_ep}, fail={n_fail_ep})")
print(f"Episode success rate: {ep_success_rate:.4f}")
print(f"Group size K: {K}")
print(f"Horizon h: {h}")
print(f"Inferred step success rate p: {p_base:.4f}")
print(f"")
print(f"P(correct sign | per-sample):        {p_correct_per_sample:.4f}")
print(f"P(correct sign | group majority):    {p_group_majority:.4f}")
print(f"P(correct dir | window-normalized):  {p_correct_normalized:.4f}")
print(f"P(correct dir | episode-normalized): {p_correct_ep_norm:.4f}")
print(f"P(correct sign | step-level):        {p_correct_step:.4f}")
print(f"Sign agreement early windows:        {sign_early:.4f}")
print(f"Sign agreement late windows:         {sign_late:.4f}")
print(f"")
print(f"Theoretical P(misattribution) = p*(1-p^(h-1)) = {p_wrong:.4f}")
print(f"Theoretical P(correct direction) = 1 - above = {1-p_wrong:.4f}")
print(f"GRPO-adjusted P(misattribution): {p_misattrib_grpo_norm:.4f}")
print(f"Empirical P(misattribution, step-level): {p_misattrib_empirical:.4f}")

# Output JSON
output = {
    "empirical": {
        "p_correct_sign_per_sample": round(p_correct_per_sample, 4),
        "p_correct_sign_group_majority": round(p_group_majority, 4),
        "p_correct_direction_window_normalized": round(p_correct_normalized, 4),
        "p_correct_direction_episode_normalized": round(p_correct_ep_norm, 4),
        "p_correct_sign_step_level": round(p_correct_step, 4),
        "p_misattribution_step_level": round(p_misattrib_empirical, 4),
        "sign_agreement_early_windows": round(sign_early, 4),
        "sign_agreement_late_windows": round(sign_late, 4),
        "n_samples": len(records),
        "n_episodes": n_episodes,
        "n_success_episodes": n_success_ep,
        "n_fail_episodes": n_fail_ep,
        "episode_success_rate": round(ep_success_rate, 4),
        "n_groups": n_valid_groups,
        "group_size_K": K,
        "step_return_distribution": {
            "n_positive": sum(1 for s in step_returns if s > 0),
            "n_zero": sum(1 for s in step_returns if s == 0),
            "n_negative": sum(1 for s in step_returns if s < 0)
        }
    },
    "theoretical": {
        "p_correct_sign_formula": "P(correct) = p^h + (1-p) = 1 - p*(1-p^(h-1))",
        "p_misattribution_formula": "P(misattrib) = p*(1-p^(h-1))",
        "p_predicted_misattribution": round(p_wrong, 4),
        "p_predicted_correct": round(1 - p_wrong, 4),
        "p_grpo_adjusted_misattribution": round(p_misattrib_grpo_norm, 4),
        "p_grpo_adjusted_correct": round(p_correct_theory_normalized, 4),
        "parameters": {
            "h": h,
            "p_base_step": round(p_base, 4),
            "p_episode_success": round(ep_success_rate, 4),
            "K": K
        }
    },
    "comparison": {
        "empirical_misattrib_step_level": round(p_misattrib_empirical, 4),
        "theoretical_misattrib": round(p_wrong, 4),
        "delta": round(abs(p_misattrib_empirical - p_wrong), 4),
        "empirical_sign_agreement_vs_episode": round(p_correct_per_sample, 4),
        "verdict": ""
    }
}

delta = abs(p_misattrib_empirical - p_wrong)
if delta < 0.03:
    output["comparison"]["verdict"] = f"Empirical misattribution ({p_misattrib_empirical:.1%}) closely matches theoretical prediction ({p_wrong:.1%}), delta={delta:.1%}"
elif delta < 0.05:
    output["comparison"]["verdict"] = f"Empirical misattribution ({p_misattrib_empirical:.1%}) approximately matches theoretical prediction ({p_wrong:.1%}), delta={delta:.1%}"
else:
    output["comparison"]["verdict"] = f"Empirical misattribution ({p_misattrib_empirical:.1%}) deviates from theoretical prediction ({p_wrong:.1%}), delta={delta:.1%}"

print(f"\n{json.dumps(output, indent=2)}")

with open("/tmp/tab3_result.json", "w") as f:
    json.dump(output, f, indent=2)
print("\nSaved to /tmp/tab3_result.json")
