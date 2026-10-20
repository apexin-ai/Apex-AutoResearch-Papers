#!/usr/bin/env python3
"""Fix AUROC + SJ selection in analyze_fewnerd_s789.py, then rerun analysis."""
import re

SCRIPT = "/root/autodl-tmp/struct_self_consist_ie/code/analyze_fewnerd_s789.py"

with open(SCRIPT) as f:
    code = f.read()

# --- Fix 1: Add _ner_soft_jaccard_pair import ---
old_import = "from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface"
new_import = "from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface, _ner_soft_jaccard_pair, _extract_surface_keys"
code = code.replace(old_import, new_import)

# --- Fix 2: Remove unused sklearn import ---
code = code.replace("from sklearn.metrics import roc_auc_score\n", "from scipy.stats import rankdata\n")

# --- Fix 3: Replace SJ selection (hard Jaccard -> soft Jaccard) ---
old_sj = '''# SJ selection
sj_sel_f1 = np.zeros(n_filtered)
for i, inst in enumerate(gold_filtered):
    samples = inst["samples"]
    n = len(samples)
    sample_sets = []
    for s in samples:
        eset = set((e.get("text",""), e.get("type","")) for e in s.get("entities", []))
        sample_sets.append(eset)
    per_sample_sj = []
    for k in range(n):
        jaccards = []
        for j in range(n):
            if j == k:
                continue
            inter = len(sample_sets[k] & sample_sets[j])
            union = len(sample_sets[k] | sample_sets[j])
            jaccards.append(inter/union if union > 0 else 1.0)
        per_sample_sj.append(float(np.mean(jaccards)))
    best_idx = int(np.argmax(per_sample_sj))
    sj_sel_f1[i] = all_sample_f1s[i, best_idx]
    if (i+1) % 10000 == 0:
        print(f"  SJ {i+1}/{n_filtered}")
print("  SJ done")'''

new_sj = '''# SJ selection (soft Jaccard with Hungarian span matching)
sj_sel_f1 = np.zeros(n_filtered)
for i, inst in enumerate(gold_filtered):
    samples = inst["samples"]
    n = len(samples)
    sj_matrix = np.zeros((n, n))
    for ii in range(n):
        for jj in range(ii + 1, n):
            s = _ner_soft_jaccard_pair(samples[ii].get("entities", []), samples[jj].get("entities", []))
            sj_matrix[ii][jj] = s
            sj_matrix[jj][ii] = s
    np.fill_diagonal(sj_matrix, 1.0)
    per_sample_sj = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]
    best_idx = int(np.argmax(per_sample_sj))
    sj_sel_f1[i] = all_sample_f1s[i, best_idx]
    if (i+1) % 10000 == 0:
        print(f"  SJ {i+1}/{n_filtered}")
print("  SJ done")'''

code = code.replace(old_sj, new_sj)

# --- Fix 4: Replace AUROC computation (broken median -> oracle-based sample-level) ---
old_auroc = '''    # AUROC: binary label = greedy_f1 > median
    median_f1 = float(np.median(greedy_f1s[valid]))
    labels = (greedy_f1s[valid] > median_f1).astype(int)
    try:
        auroc = float(roc_auc_score(labels, sig_arr[valid]))
    except:
        auroc = 0.5'''

new_auroc = '''    # AUROC: oracle-based sample-level (matches other seeds)
    # Collect per-sample signal scores + oracle labels for this signal
    all_scores_sig = []
    all_labels_sig = []
    for idx in range(n_filtered):
        inst = gold_filtered[idx]
        samples = inst["samples"]
        n_s = len(samples)
        oracle_idx = int(np.argmax(all_sample_f1s[idx]))
        if sig_name == "LP":
            per_s = [s.get("mean_logprob", float("-inf")) for s in samples]
        elif sig_name == "SJ":
            sj_mat = np.zeros((n_s, n_s))
            for ii in range(n_s):
                for jj in range(ii+1, n_s):
                    sv = _ner_soft_jaccard_pair(samples[ii].get("entities",[]), samples[jj].get("entities",[]))
                    sj_mat[ii][jj] = sv
                    sj_mat[jj][ii] = sv
            np.fill_diagonal(sj_mat, 1.0)
            per_s = [float(np.mean([sj_mat[k][j] for j in range(n_s) if j!=k])) for k in range(n_s)]
        elif sig_name == "FK":
            ks = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
            fk_mat = np.zeros((n_s, n_s))
            for ii in range(n_s):
                for jj in range(ii+1, n_s):
                    union = len(ks[ii] | ks[jj])
                    inter = len(ks[ii] & ks[jj])
                    fk_mat[ii][jj] = inter/union if union > 0 else 1.0
                    fk_mat[jj][ii] = fk_mat[ii][jj]
            np.fill_diagonal(fk_mat, 1.0)
            per_s = [float(np.mean([fk_mat[k][j] for j in range(n_s) if j!=k])) for k in range(n_s)]
        elif sig_name == "EM":
            ks = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
            per_s = [float(sum(1 for j in range(n_s) if j!=k and ks[k]==ks[j])) for k in range(n_s)]
        elif sig_name == "VC":
            ks = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
            counter_tmp = {}
            for k_s in ks:
                for key in k_s:
                    counter_tmp[key] = counter_tmp.get(key, 0) + 1
            per_s = []
            for k_s in ks:
                if not k_s:
                    per_s.append(0.0)
                else:
                    per_s.append(float(np.mean([counter_tmp[key]/n_s for key in k_s])))
        else:
            per_s = [0.0] * n_s
        all_scores_sig.extend(per_s)
        all_labels_sig.extend([1 if k == oracle_idx else 0 for k in range(n_s)])
    all_scores_sig = np.array(all_scores_sig)
    all_labels_sig = np.array(all_labels_sig, dtype=int)
    if len(np.unique(all_labels_sig)) < 2 or len(np.unique(all_scores_sig)) < 2:
        auroc = float("nan")
    else:
        n_pos = (all_labels_sig == 1).sum()
        n_neg = (all_labels_sig == 0).sum()
        ranks = rankdata(all_scores_sig)
        u = ranks[all_labels_sig == 1].sum() - n_pos * (n_pos + 1) / 2
        auroc = float(u / (n_pos * n_neg))'''

code = code.replace(old_auroc, new_auroc)

# --- Fix 5: Handle NaN AUROC in JSON output ---
old_auroc_round = '''        "auroc": round(auroc, 4),'''
new_auroc_round = '''        "auroc": round(auroc, 4) if not np.isnan(auroc) else None,'''
code = code.replace(old_auroc_round, new_auroc_round)

# --- Fix 6: Handle NaN in summary print ---
old_print = '''    print(f"{sig:<6} {q['auroc']:>7.4f} {q['spearman_global']:>8.4f} {q['spearman_conditional']:>8.4f} {s['f1']:>8.4f} {s['delta_pp']:>+8.2f}")'''
new_print = '''    auroc_str = f"{q['auroc']:>7.4f}" if q['auroc'] is not None else "   None"
    print(f"{sig:<6} {auroc_str} {q['spearman_global']:>8.4f} {q['spearman_conditional']:>8.4f} {s['f1']:>8.4f} {s['delta_pp']:>+8.2f}")'''
code = code.replace(old_print, new_print)

with open(SCRIPT, "w") as f:
    f.write(code)

print("Patch applied successfully")

# Verify changes
with open(SCRIPT) as f:
    content = f.read()
assert "roc_auc_score" not in content, "sklearn roc_auc_score should be removed"
assert "_ner_soft_jaccard_pair" in content, "soft Jaccard import missing"
assert "oracle-based sample-level" in content, "new AUROC comment missing"
assert "rankdata" in content, "rankdata import missing"
print("All verification checks passed")
