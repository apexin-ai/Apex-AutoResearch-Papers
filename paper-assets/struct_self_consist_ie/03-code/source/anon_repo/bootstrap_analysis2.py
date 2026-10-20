import json
import numpy as np
from scipy.stats import binomtest

with open('/root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/selection_f1_full.json') as f:
    data = json.load(f)

methods = data['ner']['methods']
n = data['ner']['n']
print(f"=== NER Selection F1 Bootstrap Analysis ===")
print(f"Instances: {n}")
print(f"Available methods: {list(methods.keys())}")
print()

method_names = ['greedy', 'logprob_best', 'sj_best', 'voting_conf_best']
arrays = {}
for m in method_names:
    if m in methods:
        arr = np.array(methods[m]['per_instance'])
        arrays[m] = arr
        print(f"{m:20s}: mean_f1={methods[m]['mean_f1']:.4f}, computed={arr.mean():.4f}, n={len(arr)}")
    else:
        print(f"WARNING: {m} NOT FOUND")

print()
print("=" * 60)
print("1. BOOTSTRAP 95% CI (B=10000)")
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
    print(f"{m:20s}: {arr.mean():.4f}  [{ci_lo:.4f}, {ci_hi:.4f}]  w={ci_hi-ci_lo:.4f}")

print()
print("--- Diff vs greedy ---")
for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in boot_means:
        continue
    diff_boots = boot_means[m] - boot_means['greedy']
    obs = arrays[m].mean() - arrays['greedy'].mean()
    lo, hi = np.percentile(diff_boots, 2.5), np.percentile(diff_boots, 97.5)
    z = "YES" if lo <= 0 <= hi else "NO"
    print(f"{m:20s}: {obs:+.4f}  [{lo:+.4f}, {hi:+.4f}]  0_in_CI: {z}")

print()
print("=" * 60)
print("2. PAIRED PERMUTATION TEST (10000)")
print("=" * 60)

np.random.seed(42)
for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in arrays:
        continue
    obs = arrays[m].mean() - arrays['greedy'].mean()
    combined = np.stack([arrays[m], arrays['greedy']], axis=1)
    perm_diffs = np.zeros(10000)
    for i in range(10000):
        swaps = np.random.randint(0, 2, n)
        pa = np.where(swaps == 0, combined[:, 0], combined[:, 1])
        pb = np.where(swaps == 0, combined[:, 1], combined[:, 0])
        perm_diffs[i] = pa.mean() - pb.mean()
    p = np.mean(np.abs(perm_diffs) >= np.abs(obs))
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "n.s."
    print(f"{m:20s} vs greedy: diff={obs:+.4f}, p={p:.4f} {sig}")

print()
print("=" * 60)
print("3. SIGN TEST")
print("=" * 60)

for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in arrays:
        continue
    w = int(np.sum(arrays[m] > arrays['greedy']))
    t = int(np.sum(arrays[m] == arrays['greedy']))
    l = int(np.sum(arrays[m] < arrays['greedy']))
    nt = w + l
    if nt > 0:
        res = binomtest(w, nt, 0.5)
        p = res.pvalue
    else:
        p = 1.0
    print(f"{m:20s}: {w}W/{t}T/{l}L  win%={w/max(nt,1)*100:.1f}%  p={p:.4f}")

print()
print("=" * 60)
print("4. PAIRED COHEN'S d")
print("=" * 60)

for m in ['logprob_best', 'sj_best', 'voting_conf_best']:
    if m not in arrays:
        continue
    diff = arrays[m] - arrays['greedy']
    d = diff.mean() / diff.std()
    print(f"{m:20s}: d={d:.4f}")

print()
print("=" * 60)
print("CONCLUSION")
print("=" * 60)
if 'logprob_best' in arrays:
    obs = arrays['logprob_best'].mean() - arrays['greedy'].mean()
    diff_boots = boot_means['logprob_best'] - boot_means['greedy']
    lo, hi = np.percentile(diff_boots, 2.5), np.percentile(diff_boots, 97.5)
    print(f"logprob_best - greedy = {obs:+.4f} ({obs*100:+.2f}pp)")
    print(f"Bootstrap 95% CI: [{lo:+.4f}, {hi:+.4f}]")
    if lo <= 0 <= hi:
        print("CI contains 0 => +0.6pp is NOT statistically significant at alpha=0.05")
    else:
        print("CI does NOT contain 0 => statistically significant at alpha=0.05")
