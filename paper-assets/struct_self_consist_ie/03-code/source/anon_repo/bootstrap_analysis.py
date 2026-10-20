import json
import numpy as np

# Load data
with open('/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_full.json') as f:
    data = json.load(f)

methods = data['ner']['methods']
n = data['ner']['n']
print(f"=== NER Selection F1 Bootstrap Analysis ===")
print(f"Instances: {n}")
print()

# Extract per-instance arrays
method_names = ['greedy', 'logprob_best', 'sj_best', 'voting_conf_best']
arrays = {}
for m in method_names:
    if m in methods:
        arr = np.array(methods[m]['per_instance'])
        arrays[m] = arr
        print(f"{m}: mean_f1={methods[m]['mean_f1']}, computed_mean={arr.mean():.4f}, n={len(arr)}")
    else:
        print(f"WARNING: {m} not found in methods. Available: {list(methods.keys())}")

print()

# ============================================================
# 1. Bootstrap CI (B=10000)
# ============================================================
print("=" * 60)
print("1. BOOTSTRAP 95% CONFIDENCE INTERVALS (B=10000)")
print("=" * 60)

B = 10000
np.random.seed(42)

boot_means = {}
for m in method_names:
    if m not in arrays:
        continue
    arr = arrays[m]
    boots = np.array([np.mean(arr[np.random.choice(n, n, replace=True)]) for _ in range(B)])
    boot_means[m] = boots
    ci_lo, ci_hi = np.percentile(boots, 2.5), np.percentile(boots, 97.5)
    print(f"{m:20s}: {arr.mean():.4f}  95% CI [{ci_lo:.4f}, {ci_hi:.4f}]  (width={ci_hi-ci_lo:.4f})")

# Difference CIs
print()
print("--- Differences vs greedy ---")
for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in boot_means:
        continue
    diff_boots = boot_means[m] - boot_means['greedy']
    obs_diff = arrays[m].mean() - arrays['greedy'].mean()
    ci_lo, ci_hi = np.percentile(diff_boots, 2.5), np.percentile(diff_boots, 97.5)
    contains_zero = "YES" if ci_lo <= 0 <= ci_hi else "NO"
    print(f"{m:20s} - greedy: {obs_diff:+.4f}  95% CI [{ci_lo:+.4f}, {ci_hi:+.4f}]  contains 0: {contains_zero}")

# ============================================================
# 2. Paired Permutation Test (10000 permutations)
# ============================================================
print()
print("=" * 60)
print("2. PAIRED PERMUTATION TEST (10000 permutations)")
print("=" * 60)

np.random.seed(42)
for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in arrays:
        continue
    obs_diff = arrays[m].mean() - arrays['greedy'].mean()
    # Under H0, each instance's label (method vs greedy) is exchangeable
    perm_diffs = np.zeros(10000)
    combined = np.stack([arrays[m], arrays['greedy']], axis=1)  # (n, 2)
    for i in range(10000):
        swaps = np.random.randint(0, 2, n)
        perm_a = np.where(swaps == 0, combined[:, 0], combined[:, 1])
        perm_b = np.where(swaps == 0, combined[:, 1], combined[:, 0])
        perm_diffs[i] = perm_a.mean() - perm_b.mean()
    p_value = np.mean(np.abs(perm_diffs) >= np.abs(obs_diff))
    sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else "n.s."
    print(f"H0: {m} F1 = greedy F1")
    print(f"  observed diff: {obs_diff:+.4f},  p = {p_value:.4f}  {sig}")
    print()

# ============================================================
# 3. Sign Test
# ============================================================
print("=" * 60)
print("3. SIGN TEST (per-instance wins/ties/losses vs greedy)")
print("=" * 60)

for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in arrays:
        continue
    wins = int(np.sum(arrays[m] > arrays['greedy']))
    ties = int(np.sum(arrays[m] == arrays['greedy']))
    losses = int(np.sum(arrays[m] < arrays['greedy']))
    total_nontie = wins + losses
    if total_nontie > 0:
        from scipy.stats import binom_test
        try:
            p_sign = binom_test(wins, total_nontie, 0.5)
        except:
            # manual two-sided binomial test
            from math import comb
            k = min(wins, losses)
            p_sign = 2 * sum(comb(total_nontie, i) * 0.5**total_nontie for i in range(k+1))
            p_sign = min(p_sign, 1.0)
    else:
        p_sign = 1.0
    print(f"{m:20s} vs greedy: {wins}W / {ties}T / {losses}L  (win_rate={wins/(wins+losses)*100:.1f}% among non-ties)  sign_test p={p_sign:.4f}")

# ============================================================
# 4. Additional: Effect size (Cohen's d for paired samples)
# ============================================================
print()
print("=" * 60)
print("4. EFFECT SIZE (paired Cohen's d)")
print("=" * 60)

for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in arrays:
        continue
    diff = arrays[m] - arrays['greedy']
    d = diff.mean() / diff.std()
    print(f"{m:20s} vs greedy: d = {d:.4f}")

# ============================================================
# Summary
# ============================================================
print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
obs_diff_lp = arrays['logprob_best'].mean() - arrays['greedy'].mean()
print(f"logprob_best - greedy = {obs_diff_lp:+.4f} ({obs_diff_lp*100:+.2f} pp)")
diff_boots_lp = boot_means['logprob_best'] - boot_means['greedy']
ci_lo, ci_hi = np.percentile(diff_boots_lp, 2.5), np.percentile(diff_boots_lp, 97.5)
print(f"  Bootstrap 95% CI: [{ci_lo:+.4f}, {ci_hi:+.4f}]")
print(f"  CI contains 0: {'YES — NOT significant' if ci_lo <= 0 <= ci_hi else 'NO — significant'}")
