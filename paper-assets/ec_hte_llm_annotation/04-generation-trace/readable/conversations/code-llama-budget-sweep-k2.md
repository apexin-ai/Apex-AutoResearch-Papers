# code llama budget sweep k2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_code_llama-budget-sweep-k2_20260521T212758.jsonl`
- **Structured JSON:** [`b94f6907fa5529877b07.json`](../../sessions/b9/b94f6907fa5529877b07.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-21T21:33:45.531508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T21:33:45.532066+00:00_

1	"""
2	Llama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.
3	
4	Uses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.
5	Ground truth CATE is synthetic; confusion matrices are empirical.
6	
7	4 subgroups with real asymmetric CMs:
8	  False_medium: FPR=0.235, FNR=0.319, weight=193/500
9	  False_short:  FPR=0.310, FNR=0.212, weight=109/500
10	  True_medium:  FPR=0.219, FNR=0.258, weight=129/500
11	  True_short:   FPR=0.091, FNR=0.190, weight=69/500
12	
13	P(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65
14	Methods: Naive, Global, Stratified MLE, HB EC-HTE
15	n_expert=200, 20 MC seeds
16	
17	Usage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py
18	"""
19	
20	import time
21	import warnings
22	import numpy as np
23	import pandas as pd
24	from scipy.special import gammaln
25	
26	warnings.filterwarnings('ignore')
27	
28	# === Config ===
29	
30	N = 5000
31	N_EXPERT = 200
32	N_MC = 20
33	SEED_BASE = 0
34	
35	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
36	SUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)
37	SUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()
38	
39	SUBGROUP_CM = {
40	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
41	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
42	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
43	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
44	}
45	
46	P_Z1 = 0.652
47	P_T1 = 0.5
48	TAU_Z0 = 0.35
49	TAU_Z1 = 0.65
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: C[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# === Core Estimators ===
59	
60	def diff_in_means(Y, T, mask):
61	    t1 = mask & (T == 1)
62	    t0 = mask & (T == 0)
63	    n1, n0 = t1.sum(), t0.sum()
64	    if n1 < 2 or n0 < 2:
65	        return np.nan, np.nan
66	    y1, y0 = Y[t1], Y[t0]
67	    tau_hat = y1.mean() - y0.mean()
68	    se = np.sqrt(y1.var(ddof=1) / n
…[truncated 24032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T21:33:45.532379+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k2.py",
  "content": "\"\"\"\nK=2 Budget Sensitivity Sweep: Llama-3.1-8B Semi-Synthetic EC-HTE.\n\nMerged subgroups by has_hashtag:\n  False (no hashtag): FPR=0.252, FNR=0.269, weight=0.604\n  True (has hashtag):  FPR=0.186, FNR=0.233, weight=0.396\n\nΔπ = |0.261 - 0.210| = 0.051\n\nn_expert ∈ {100, 200, 500, 1000, 2000}, 50 MC seeds per budget.\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\n\nUsage: python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False', 'True']\nSUBGROUP_WEIGHTS = np.array([0.604, 0.396])\n\nSUBGROUP_CM = {\n    'False': {'fpr': 0.252, 'fnr': 0.269},\n    'True':  {'fpr': 0.186, 'fnr': 0.233},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler (MAP-EB accelerated) ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=800, n_warmup=400, n_chains=2,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits = [np.array([1.0, 1.0]), np.array([5.0, 5.0])][:n_chains]\n    all_theta = []\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                if np.log(rng.rand()) < log_r:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(np.log(rng.rand()) < log_r)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    theta_arr = np.stack(all_theta)\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n    return C\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(2, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(2):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n                'coverage': cov_or,\n            })\n\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n                'coverage': cov_nv,\n            })\n\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n                'coverage': cov_gc,\n            })\n\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n                'coverage': cov_ml,\n            })\n\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Aggregation (corrected |Bias| = |mean(bias)|) ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['abs_mean_bias'] = abs(valid.mean())\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_summary):\n    lines = []\n    lines.append(\"# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Merged subgroups by `has_hashtag` (K=2).\\n\")\n    lines.append(\"| Subgroup | Weight | FPR | FNR | π_s |\")\n    lines.append(\"|----------|--------|-----|-----|-----|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        pi = (cm['fpr'] + cm['fnr']) / 2\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {pi:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051\")\n    lines.append(f\"\\nN={N}, P(Z=1)={P_Z1}, τ(z=0)={TAU_Z0}, τ(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"n_expert ∈ {N_EXPERT_LIST}, {N_MC} MC seeds per budget\\n\")\n\n    lines.append(\"## Summary by n_expert\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|--------|-------|------|----------|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['abs_mean_bias'].mean():.4f} | \"\n                             f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## RMSE Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_rmse = nv['rmse'].mean()\n            hb_rmse = hb['rmse'].mean()\n            ratio = hb_rmse / nv_rmse\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_rmse:.4f} | {hb_rmse:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and crossover is None:\n                crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## |Bias| Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    bias_crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_b = nv['abs_mean_bias'].mean()\n            hb_b = hb['abs_mean_bias'].mean()\n            ratio = hb_b / nv_b if nv_b > 1e-8 else float('inf')\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_b:.4f} | {hb_b:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and bias_crossover is None:\n                bias_crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Var | MSE |\")\n    lines.append(\"|----------|--------|-------|-----|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                bias_sq = (sub['mean_bias'] ** 2).mean()\n                mse = (sub['rmse'] ** 2).mean()\n                var = mse - bias_sq\n                lines.append(f\"| {ne} | {m} | {bias_sq:.4f} | {var:.4f} | {mse:.4f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## Crossover Analysis\\n\")\n    if crossover:\n        lines.append(f\"**RMSE crossover**: EC-HTE first beats Naive at n_expert={crossover}\")\n    else:\n        lines.append(\"**RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    if bias_crossover:\n        lines.append(f\"**|Bias| crossover**: EC-HTE first beats Naive at n_expert={bias_crossover}\")\n    else:\n        lines.append(\"**|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n\n    lines.append(\"\")\n    lines.append(\"## Conclusion\\n\")\n    lines.append(f\"With K=2 and Δπ=0.051, the CM heterogeneity is small.\")\n    lines.append(\"The bias reduction from stratified correction is limited, \"\n                 \"so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.\")\n    if crossover:\n        lines.append(f\"\\nAt n_expert≥{crossover}, HB EC-HTE achieves lower RMSE than Naive, \"\n                     \"indicating the variance cost is amortized.\")\n    else:\n        lines.append(\"\\nEven at n_expert=2000, the variance cost exceeds the bias reduction. \"\n                     \"K=2 with Δπ=0.051 may be too homogeneous for EC-HTE to help.\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/budget_sweep_k2_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"K=2 Budget Sensitivity Sweep\")\n    print(f\"N={N}, n_expert_list={N_EXPERT_LIST}, n_mc={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"K=2 Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}, π={(cm['fpr']+cm['fnr'])/2:.3f}\")\n    print()\n\n    # Dry run: 1 seed, smallest budget\n    print(\"=== Dry run (1 seed, n_expert=100) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    proceed = input(\"Proceed with full run? [y/N] \").strip().lower()\n    if proceed != 'y':\n        print(\"Aborted.\")\n        exit(0)\n\n    # Full run\n    all_results = []\n    t0_total = time.time()\n\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n=== n_expert={ne} ({N_MC} seeds) ===\")\n        t0 = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, ne)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = ne\n            all_results.extend(mc_rows)\n\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n        elapsed = time.time() - t0\n        print(f\"  n_expert={ne} done in {elapsed:.1f}s\")\n\n    total_time = time.time() - t0_total\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    df_summary = aggregate_results(df_raw)\n\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_true', 'cate_est', 'coverage']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/budget_sweep_k2_results.csv', index=False)\n    print(f\"Saved budget_sweep_k2_results.csv ({len(df_raw)} rows)\")\n\n    write_analysis(df_summary)\n\n    print(\"\\n=== Summary ===\")\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                print(f\"    {m:20s}: |bias|={sub['abs_mean_bias'].mean():.4f}  \"\n                      f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k2.py",
    "content": "\"\"\"\nK=2 Budget Sensitivity Sweep: Llama-3.1-8B Semi-Synthetic EC-HTE.\n\nMerged subgroups by has_hashtag:\n  False (no hashtag): FPR=0.252, FNR=0.269, weight=0.604\n  True (has hashtag):  FPR=0.186, FNR=0.233, weight=0.396\n\nΔπ = |0.261 - 0.210| = 0.051\n\nn_expert ∈ {100, 200, 500, 1000, 2000}, 50 MC seeds per budget.\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\n\nUsage: python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False', 'True']\nSUBGROUP_WEIGHTS = np.array([0.604, 0.396])\n\nSUBGROUP_CM = {\n    'False': {'fpr': 0.252, 'fnr': 0.269},\n    'True':  {'fpr': 0.186, 'fnr': 0.233},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler (MAP-EB accelerated) ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=800, n_warmup=400, n_chains=2,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits = [np.array([1.0, 1.0]), np.array([5.0, 5.0])][:n_chains]\n    all_theta = []\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                if np.log(rng.rand()) < log_r:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(np.log(rng.rand()) < log_r)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    theta_arr = np.stack(all_theta)\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n    return C\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(2, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(2):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n                'coverage': cov_or,\n            })\n\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n                'coverage': cov_nv,\n            })\n\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n                'coverage': cov_gc,\n            })\n\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n                'coverage': cov_ml,\n            })\n\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Aggregation (corrected |Bias| = |mean(bias)|) ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['abs_mean_bias'] = abs(valid.mean())\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_summary):\n    lines = []\n    lines.append(\"# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Merged subgroups by `has_hashtag` (K=2).\\n\")\n    lines.append(\"| Subgroup | Weight | FPR | FNR | π_s |\")\n    lines.append(\"|----------|--------|-----|-----|-----|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        pi = (cm['fpr'] + cm['fnr']) / 2\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {pi:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051\")\n    lines.append(f\"\\nN={N}, P(Z=1)={P_Z1}, τ(z=0)={TAU_Z0}, τ(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"n_expert ∈ {N_EXPERT_LIST}, {N_MC} MC seeds per budget\\n\")\n\n    lines.append(\"## Summary by n_expert\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|--------|-------|------|----------|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['abs_mean_bias'].mean():.4f} | \"\n                             f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## RMSE Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_rmse = nv['rmse'].mean()\n            hb_rmse = hb['rmse'].mean()\n            ratio = hb_rmse / nv_rmse\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_rmse:.4f} | {hb_rmse:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and crossover is None:\n                crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## |Bias| Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    bias_crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_b = nv['abs_mean_bias'].mean()\n            hb_b = hb['abs_mean_bias'].mean()\n            ratio = hb_b / nv_b if nv_b > 1e-8 else float('inf')\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_b:.4f} | {hb_b:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and bias_crossover is None:\n                bias_crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Var | MSE |\")\n    lines.append(\"|----------|--------|-------|-----|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                bias_sq = (sub['mean_bias'] ** 2).mean()\n                mse = (sub['rmse'] ** 2).mean()\n                var = mse - bias_sq\n                lines.append(f\"| {ne} | {m} | {bias_sq:.4f} | {var:.4f} | {mse:.4f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## Crossover Analysis\\n\")\n    if crossover:\n        lines.append(f\"**RMSE crossover**: EC-HTE first beats Naive at n_expert={crossover}\")\n    else:\n        lines.append(\"**RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    if bias_crossover:\n        lines.append(f\"**|Bias| crossover**: EC-HTE first beats Naive at n_expert={bias_crossover}\")\n    else:\n        lines.append(\"**|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n\n    lines.append(\"\")\n    lines.append(\"## Conclusion\\n\")\n    lines.append(f\"With K=2 and Δπ=0.051, the CM heterogeneity is small.\")\n    lines.append(\"The bias reduction from stratified correction is limited, \"\n                 \"so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.\")\n    if crossover:\n        lines.append(f\"\\nAt n_expert≥{crossover}, HB EC-HTE achieves lower RMSE than Naive, \"\n                     \"indicating the variance cost is amortized.\")\n    else:\n        lines.append(\"\\nEven at n_expert=2000, the variance cost exceeds the bias reduction. \"\n                     \"K=2 with Δπ=0.051 may be too homogeneous for EC-HTE to help.\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/budget_sweep_k2_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"K=2 Budget Sensitivity Sweep\")\n    print(f\"N={N}, n_expert_list={N_EXPERT_LIST}, n_mc={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"K=2 Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}, π={(cm['fpr']+cm['fnr'])/2:.3f}\")\n    print()\n\n    # Dry run: 1 seed, smallest budget\n    print(\"=== Dry run (1 seed, n_expert=100) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    proceed = input(\"Proceed with full run? [y/N] \").strip().lower()\n    if proceed != 'y':\n        print(\"Aborted.\")\n        exit(0)\n\n    # Full run\n    all_results = []\n    t0_total = time.time()\n\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n=== n_expert={ne} ({N_MC} seeds) ===\")\n        t0 = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, ne)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = ne\n            all_results.extend(mc_rows)\n\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n        elapsed = time.time() - t0\n        print(f\"  n_expert={ne} done in {elapsed:.1f}s\")\n\n    total_time = time.time() - t0_total\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    df_summary = aggregate_results(df_raw)\n\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_true', 'cate_est', 'coverage']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/budget_sweep_k2_results.csv', index=False)\n    print(f\"Saved budget_sweep_k2_results.csv ({len(df_raw)} rows)\")\n\n    write_analysis(df_summary)\n\n    print(\"\\n=== Summary ===\")\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                print(f\"    {m:20s}: |bias|={sub['abs_mean_bias'].mean():.4f}  \"\n                      f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T21:33:45.532838+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k2.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T21:33:45.533012+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | head -30",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Bash",
  "tool_args": {
    "command": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | head -30",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T21:33:45.533164+00:00_

K=2 Budget Sensitivity Sweep
N=5000, n_expert_list=[100, 200, 500, 1000, 2000], n_mc=50
tau(z=0)=0.35, tau(z=1)=0.65, Δτ=0.3
K=2 Subgroup CMs:
  False: FPR=0.252, FNR=0.269, π=0.261
  True: FPR=0.186, FNR=0.233, π=0.210

=== Dry run (1 seed, n_expert=100) ===
Dry run OK: 20 rows
  oracle              : mean |bias| = 0.0465
  naive               : mean |bias| = 0.0626
  global_corrected    : mean |bias| = 0.2893
  stratified_mle      : mean |bias| = 0.3114
  hb_ec_hte           : mean |bias| = 0.3143

Proceed with full run? [y/N] 
=== n_expert=100 (50 seeds) ===
  [10/50] 4s elapsed, ETA 16s
  [20/50] 8s elapsed, ETA 11s
  [30/50] 12s elapsed, ETA 8s
  [40/50] 15s elapsed, ETA 4s
  [50/50] 19s elapsed, ETA 0s
  n_expert=100 done in 18.8s

=== n_expert=200 (50 seeds) ===
  [10/50] 3s elapsed, ETA 14s
  [20/50] 7s elapsed, ETA 11s
  [30/50] 11s elapsed, ETA 7s
  [40/50] 14s elapsed, ETA 4s
  [50/50] 18s elapsed, ETA 0s

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T21:33:45.533361+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | tail -50",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Bash",
  "tool_args": {
    "command": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | tail -50",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T21:33:45.533575+00:00_

  [10/50] 4s elapsed, ETA 15s
  [20/50] 7s elapsed, ETA 11s
  [30/50] 11s elapsed, ETA 7s
  [40/50] 15s elapsed, ETA 4s
  [50/50] 18s elapsed, ETA 0s
  n_expert=1000 done in 18.2s

=== n_expert=2000 (50 seeds) ===
  [10/50] 4s elapsed, ETA 15s
  [20/50] 8s elapsed, ETA 11s
  [30/50] 11s elapsed, ETA 7s
  [40/50] 15s elapsed, ETA 4s
  [50/50] 18s elapsed, ETA 0s
  n_expert=2000 done in 18.5s

Total time: 92.2s
Saved budget_sweep_k2_results.csv (5000 rows)
Wrote artifacts/c1_multi_llm/budget_sweep_k2_analysis.md

=== Summary ===

  n_expert=100:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0094  rmse=0.1456  cov=0.840
    stratified_mle      : |bias|=0.0128  rmse=0.1905  cov=0.745
    hb_ec_hte           : |bias|=0.0116  rmse=0.1927  cov=0.745

  n_expert=200:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0161  rmse=0.1223  cov=0.860
    stratified_mle      : |bias|=0.0179  rmse=0.1540  cov=0.775
    hb_ec_hte           : |bias|=0.0168  rmse=0.1557  cov=0.780

  n_expert=500:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0132  rmse=0.1070  cov=0.925
    stratified_mle      : |bias|=0.0128  rmse=0.1239  cov=0.900
    hb_ec_hte           : |bias|=0.0125  rmse=0.1242  cov=0.905

  n_expert=1000:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0073  rmse=0.0952  cov=0.960
    stratified_mle      : |bias|=0.0065  rmse=0.0999  cov=0.940
    hb_ec_hte           : |bias|=0.0065  rmse=0.0997  cov=0.940

  n_expert=2000:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0069  rmse=0.0908  cov=0.955
    stratified_mle      : |bias|=0.0137  rmse=0.0921  cov=0.950
    hb_ec_hte           : |bias|=0.0137  rmse=0.0920  cov=0.950

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T21:33:45.533759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k2_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k2_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T21:33:45.534031+00:00_

1	# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs
2	
3	## Design
4	
5	Merged subgroups by `has_hashtag` (K=2).
6	
7	| Subgroup | Weight | FPR | FNR | π_s |
8	|----------|--------|-----|-----|-----|
9	| False | 0.604 | 0.252 | 0.269 | 0.261 |
10	| True | 0.396 | 0.186 | 0.233 | 0.210 |
11	
12	Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051
13	
14	N=5000, P(Z=1)=0.652, τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
15	n_expert ∈ [100, 200, 500, 1000, 2000], 50 MC seeds per budget
16	
17	## Summary by n_expert
18	
19	| n_expert | Method | |Bias| | RMSE | Coverage |
20	|----------|--------|-------|------|----------|
21	| 100 | naive | 0.0819 | 0.1000 | 0.675 |
22	| 100 | global_corrected | 0.0094 | 0.1456 | 0.840 |
23	| 100 | stratified_mle | 0.0128 | 0.1905 | 0.745 |
24	| 100 | hb_ec_hte | 0.0116 | 0.1927 | 0.745 |
25	|---|---|---|---|---|
26	| 200 | naive | 0.0819 | 0.1000 | 0.675 |
27	| 200 | global_corrected | 0.0161 | 0.1223 | 0.860 |
28	| 200 | stratified_mle | 0.0179 | 0.1540 | 0.775 |
29	| 200 | hb_ec_hte | 0.0168 | 0.1557 | 0.780 |
30	|---|---|---|---|---|
31	| 500 | naive | 0.0819 | 0.1000 | 0.675 |
32	| 500 | global_corrected | 0.0132 | 0.1070 | 0.925 |
33	| 500 | stratified_mle | 0.0128 | 0.1239 | 0.900 |
34	| 500 | hb_ec_hte | 0.0125 | 0.1242 | 0.905 |
35	|---|---|---|---|---|
36	| 1000 | naive | 0.0819 | 0.1000 | 0.675 |
37	| 1000 | global_corrected | 0.0073 | 0.0952 | 0.960 |
38	| 1000 | stratified_mle | 0.0065 | 0.0999 | 0.940 |
39	| 1000 | hb_ec_hte | 0.0065 | 0.0997 | 0.940 |
40	|---|---|---|---|---|
41	| 2000 | naive | 0.0819 | 0.1000 | 0.675 |
42	| 2000 | global_corrected | 0.0069 | 0.0908 | 0.955 |
43	| 2000 | stratified_mle | 0.0137 | 0.0921 | 0.950 |
44	| 2000 | hb_ec_hte | 0.0137 | 0.0920 | 0.950 |
45	|---|---|---|---|---|
46	
47	## RMSE Ratio: EC-HTE / Naive
48	
49	| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |
50	|----------|-----------|---------|-------|----------|
51	| 100 | 0.1000 | 0.1927 | 1.928 | no |
52	| 200 | 0.1000 | 0.1557 | 1.557 
…[truncated 2052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T21:33:45.534358+00:00_

Run complete (92s). Both outputs saved.

**Key results:**

| n_expert | Naive RMSE | Global RMSE | HB EC-HTE RMSE | HB/Naive |
|----------|-----------|-------------|----------------|----------|
| 100 | 0.1000 | 0.1456 | 0.1927 | 1.93 |
| 200 | 0.1000 | 0.1223 | 0.1557 | 1.56 |
| 500 | 0.1000 | 0.1070 | 0.1242 | 1.24 |
| **1000** | **0.1000** | **0.0952** | **0.0997** | **1.00** |
| 2000 | 0.1000 | 0.0908 | 0.0920 | 0.92 |

**Findings:**
- **RMSE crossover at n_expert=1000** — HB EC-HTE just barely beats Naive (ratio=0.998)
- **|Bias| is always lower for HB** (5-8x reduction over Naive at all budgets), but variance inflation dominates until n_expert≈1000
- **Global corrected dominates HB EC-HTE at every budget** — with Δπ=0.051, the per-subgroup CM heterogeneity is too small to justify the extra variance from stratified estimation
- Bias-variance decomposition confirms: Naive has Bias²=0.0082 (stable), HB trades this for Var that shrinks from 0.041→0.009 as n_expert grows

**Bottom line:** K=2 merging reduced Δπ from 0.137 (K=4) to 0.051, pushing the crossover from ~200 to ~1000. The global corrected estimator (single CM) is the best choice here since CM heterogeneity is negligible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_llama-budget-sweep-k2_20260521T212758"
}
```

</details>

---
