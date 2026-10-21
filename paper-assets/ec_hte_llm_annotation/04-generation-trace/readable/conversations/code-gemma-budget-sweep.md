# code gemma budget sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_code_gemma-budget-sweep_20260521T221030.jsonl`
- **Structured JSON:** [`734d825291497b895f24.json`](../../sessions/73/734d825291497b895f24.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-21T22:13:38.199924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T22:13:38.200577+00:00_

1	#!/usr/bin/env python3
2	"""
3	Budget sensitivity sweep for Llama K=4 real confusion matrices.
4	
5	Sweeps n_expert in {100, 200, 500, 1000, 2000} with 50 MC seeds each.
6	Uses MAP-EB instead of Gibbs for speed (250 total runs).
7	
8	|Bias| metric: |mean(estimate - truth) across seeds| averaged across cells.
9	"""
10	
11	import time
12	import warnings
13	import numpy as np
14	import pandas as pd
15	from scipy.optimize import minimize_scalar
16	from scipy.special import gammaln
17	
18	warnings.filterwarnings('ignore')
19	
20	# === Config ===
21	
22	N = 5000
23	N_EXPERT_LIST = [100, 200, 500, 1000, 2000]
24	N_MC = 50
25	SEED_BASE = 0
26	
27	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
28	SUBGROUP_WEIGHTS = np.array([0.386, 0.218, 0.258, 0.138])
29	
30	SUBGROUP_CM = {
31	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
32	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
33	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
34	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
35	}
36	
37	P_Z1 = 0.652
38	P_T1 = 0.5
39	TAU_Z0 = 0.35
40	TAU_Z1 = 0.65
41	
42	
43	def get_cm_matrix(fpr, fnr):
44	    return np.array([[1 - fpr, fpr],
45	                     [fnr, 1 - fnr]])
46	
47	
48	# === Estimators ===
49	
50	def diff_in_means(Y, T, mask):
51	    t1 = mask & (T == 1)
52	    t0 = mask & (T == 0)
53	    n1, n0 = t1.sum(), t0.sum()
54	    if n1 < 2 or n0 < 2:
55	        return np.nan, np.nan
56	    y1, y0 = Y[t1], Y[t0]
57	    tau_hat = y1.mean() - y0.mean()
58	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
59	    return tau_hat, se
60	
61	
62	def estimate_confusion_matrix(z_true, z_hat):
63	    C = np.zeros((2, 2))
64	    for zt in [0, 1]:
65	        mask = z_true == zt
66	        n = mask.sum()
67	        for zh in [0, 1]:
68	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
69	    return C
70	
71	
72	def estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):
73	    C = {}
74	    for s in
…[truncated 19036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T22:13:38.200903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma2_9b_balanced.csv",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma2_9b_balanced.csv",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T22:13:38.201189+00:00_

1	idx,text,true_label,llm_label,z,has_hashtag,has_mention,text_length_bin
2	10476,"when you jacked into your house without keys. hell yeah, i'm david blaine jr.",2,2,1,False,False,short
3	1824,Cigarettes and Valentines,1,1,1,False,False,short
4	409,@user we'll miss you in Seattle! Especially when you win your NL Cy Young award!,2,2,1,False,True,medium
5	12149,I'm not going to sack Tony romo but I will sack dak,0,0,0,False,False,short
6	4506,@user Article reminds us Obama's new policy towards #Cuba follows path #Canada has taken all along #cdnpoli,1,1,1,True,True,medium
7	4012,@user @user Link to review for #ThisIsUs isn't launching.,1,0,1,True,True,short
8	3657,@user The same media that hides from the truth about the Clinton Foundation...,0,0,0,False,True,short
9	2286,Oh. my. God. Bernie is a white supremacist Nazi. The warning signs have been there for years and we never noticed!!…,0,0,0,False,False,medium
10	12066,"@user such as telling us exactly what we have to do as my points already made with gun control, health care, business, speech, ect.",1,0,1,False,True,medium
11	1679,The latest one hundred people you should know! Thanks to @user @user @user #chile #isis,1,2,1,True,True,medium
12	11087,@user @user twenty bags of rusted dicks.,0,0,0,False,True,short
13	12135,Finally watching Scream Queens episode 5 after what feels like forever!! #ScreamQueens,2,2,1,True,False,medium
14	8935,@user she'd claimed Thomistic view of ensoulment showed church's oppositon to abortion is recent develpmnt & Benedict wasn't having it,1,1,1,False,True,medium
15	1424,Preparations Continue For #Tesla's #Model3 Launch #ElectricVehicles #GoGreen #GoElectric #GreenerDriving,1,2,1,True,False,medium
16	9674,"Manasseh, Amon, Josiah. Pray Kim Jong Un follows Josiah's example-find the book of the Law discarded by ancestors.…",1,1,1,False,False,medium
17	6912,"Donald, take it easy my friend, but I can't wait to see u start building that thick high wall on the Mexican border to seal ur legacy",1
…[truncated 1657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T22:13:38.201521+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_sweep.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nGemma-2-9B full pipeline: CM profile + budget sweep (K=4 and K=2).\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\nOUT_DIR = 'artifacts/c1_multi_llm'\n\n# === Step 1: Compute per-subgroup CM from CSV ===\n\ndef compute_cm_profile(csv_path):\n    df = pd.read_csv(csv_path)\n\n    # Balanced binary Z\n    df['Z'] = (df['true_label'] >= 1).astype(int)\n    df['Z_hat'] = (df['llm_label'] >= 1).astype(int)\n\n    # Global stats\n    acc = (df['Z'] == df['Z_hat']).mean()\n    p_z1 = df['Z'].mean()\n\n    # Global FPR, FNR\n    neg = df[df['Z'] == 0]\n    pos = df[df['Z'] == 1]\n    fpr_global = (neg['Z_hat'] == 1).mean()\n    fnr_global = (pos['Z_hat'] == 0).mean()\n\n    print(f\"=== Gemma CM Profile ===\")\n    print(f\"N = {len(df)}, Accuracy = {acc:.3f}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"Global FPR = {fpr_global:.3f}, FNR = {fnr_global:.3f}\")\n    print(f\"Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    print()\n\n    # K=4: has_hashtag x text_length_bin (exclude \"long\")\n    df_k4 = df[df['text_length_bin'] != 'long'].copy()\n    df_k4['subgroup'] = df_k4['has_hashtag'].astype(str) + '_' + df_k4['text_length_bin']\n    k4_labels = sorted(df_k4['subgroup'].unique())\n\n    print(f\"K=4 subgroups (excluding 'long'): {k4_labels}\")\n    print(f\"K=4 sample size: {len(df_k4)}\")\n\n    k4_cm = {}\n    k4_weights = {}\n    k4_pi = {}\n    k4_kappa = {}\n\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df_k4)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k4_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k4_weights[s] = round(w_s, 3)\n        k4_pi[s] = round(pi_s, 3)\n        k4_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # K=2: has_hashtag only\n    df['subgroup_k2'] = df['has_hashtag'].astype(str)\n    k2_labels = sorted(df['subgroup_k2'].unique())\n\n    print(f\"K=2 subgroups: {k2_labels}\")\n\n    k2_cm = {}\n    k2_weights = {}\n    k2_pi = {}\n    k2_kappa = {}\n\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k2_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k2_weights[s] = round(w_s, 3)\n        k2_pi[s] = round(pi_s, 3)\n        k2_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # Write CM profile markdown\n    lines = []\n    lines.append(\"# Gemma-2-9B Confusion Matrix Profile\\n\")\n    lines.append(\"## Global Statistics\\n\")\n    lines.append(f\"- N = {len(df)}\")\n    lines.append(f\"- Accuracy = {acc:.3f}\")\n    lines.append(f\"- P(Z=1) = {p_z1:.3f}\")\n    lines.append(f\"- Global FPR = {fpr_global:.3f}\")\n    lines.append(f\"- Global FNR = {fnr_global:.3f}\")\n    lines.append(f\"- Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    lines.append(f\"- FNR > FPR asymmetry: {'YES' if fnr_global > fpr_global else 'NO'}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)\\n\")\n    lines.append(f\"- Sample size (excl. long): {len(df_k4)}\")\n    lines.append(\"\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k4_weights[s]:.3f} | {k4_pi[s]:.3f} | {k4_cm[s]['fpr']:.3f} | {k4_cm[s]['fnr']:.3f} | {k4_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k4 = max(k4_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k4:.2f}\")\n    prop2_count = sum(1 for s in k4_labels if k4_kappa[s] > 2.0)\n    lines.append(f\"- Prop2 triggered (kappa > 2): {prop2_count}/{len(k4_labels)}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=2 Subgroups (has_hashtag only)\\n\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k2_weights[s]:.3f} | {k2_pi[s]:.3f} | {k2_cm[s]['fpr']:.3f} | {k2_cm[s]['fnr']:.3f} | {k2_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k2 = max(k2_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k2:.2f}\")\n    lines.append(\"\")\n\n    profile_path = f'{OUT_DIR}/gemma_cm_profile.md'\n    with open(profile_path, 'w') as f:\n        f.write(\"\\n\".join(lines))\n    print(f\"Wrote {profile_path}\")\n\n    return {\n        'p_z1': p_z1,\n        'k4': {'labels': k4_labels, 'weights': k4_weights, 'cm': k4_cm},\n        'k2': {'labels': k2_labels, 'weights': k2_weights, 'cm': k2_cm},\n    }\n\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\n# === Estimators ===\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert, subgroup_labels, subgroup_weights, subgroup_cm, p_z1):\n    rng = np.random.RandomState(seed)\n    k = len(subgroup_labels)\n\n    S_idx = rng.choice(k, size=N, p=subgroup_weights)\n    S = np.array([subgroup_labels[i] for i in S_idx])\n\n    Z = rng.binomial(1, p_z1, N)\n    T = rng.binomial(1, 0.5, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(k):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(subgroup_cm[subgroup_labels[i]]['fpr'],\n                           subgroup_cm[subgroup_labels[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed, subgroup_labels):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, subgroup_labels)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, subgroup_labels)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, subgroup_labels)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in subgroup_labels:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in subgroup_labels:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            ci_w_nv = (ci_hi_nv - ci_lo_nv) if not np.isnan(ci_lo_nv) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            ci_w_gc = (ci_hi_gc - ci_lo_gc) if not np.isnan(ci_lo_gc) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            ci_w_ml = (ci_hi_ml - ci_lo_ml) if not np.isnan(ci_lo_ml) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            ci_w_hb = (ci_hi_hb - ci_lo_hb) if not np.isnan(ci_lo_hb) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    cell_w = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['ci_width']\n              .mean().reset_index(name='ci_width'))\n    return (cell_w.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Run sweep for one K config ===\n\ndef run_sweep(k_label, subgroup_labels, subgroup_weights_dict, subgroup_cm, p_z1, dry_run=False):\n    labels = subgroup_labels\n    weights_arr = np.array([subgroup_weights_dict[s] for s in labels])\n    weights_arr = weights_arr / weights_arr.sum()  # normalize\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Budget Sweep: Gemma {k_label}\")\n    print(f\"Subgroups: {labels}\")\n    print(f\"Weights: {dict(zip(labels, [round(w, 3) for w in weights_arr]))}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"tau(z=0) = {TAU_Z0}, tau(z=1) = {TAU_Z1}\")\n    print(f\"{'='*60}\")\n\n    if dry_run:\n        print(\"\\n--- Dry run (n_expert=100, 1 seed) ---\")\n        data = generate_data(SEED_BASE, 100, labels, weights_arr, subgroup_cm, p_z1)\n        rows = run_one_mc(data, SEED_BASE, labels)\n        df_dry = pd.DataFrame(rows)\n        df_dry['n_expert'] = 100\n        print(f\"Dry run OK: {len(df_dry)} rows\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_dry[df_dry['method'] == m]\n            bias = sub['bias'].abs().mean()\n            print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n        return None\n\n    # Full run\n    print(f\"\\nFull run: {len(N_EXPERT_LIST)} budgets x {N_MC} seeds\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert, labels, weights_arr, subgroup_cm, p_z1)\n            mc_rows = run_one_mc(data, seed, labels)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    return df_raw\n\n\ndef save_sweep_csv(df_raw, csv_path):\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level',\n                 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(csv_path, index=False)\n    print(f\"Saved {csv_path} ({len(df_raw)} rows)\")\n\n\ndef build_summary(df_raw):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n    return abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n\ndef write_analysis(summary_k4, summary_k2, df_k4, df_k2, outpath, profile):\n    lines = []\n    lines.append(\"# Gemma-2-9B Budget Sweep Analysis\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={profile['p_z1']:.3f}\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)\")\n    lines.append(f\"- Coverage = avg across cells of fraction(95% CI contains true CATE)\")\n    lines.append(f\"- CI Width = avg across cells of mean(CI_width)\")\n    lines.append(\"\")\n\n    for k_label, summary, df_raw in [(\"K=4\", summary_k4, df_k4), (\"K=2\", summary_k2, df_k2)]:\n        lines.append(f\"## {k_label} Summary Table\\n\")\n        lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |\")\n        lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|\")\n\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            vals = {}\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = sub[sub['method'] == m]\n                if len(row) > 0:\n                    vals[m] = {\n                        'abs_bias': row.iloc[0]['abs_bias'],\n                        'rmse': row.iloc[0]['rmse'],\n                        'coverage': row.iloc[0]['coverage'],\n                        'ci_width': row.iloc[0]['ci_width'],\n                    }\n                else:\n                    vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan, 'ci_width': np.nan}\n\n            hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n            hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n            lines.append(\n                f\"| {ne} \"\n                f\"| {vals['naive']['abs_bias']:.4f} \"\n                f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n                f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n                f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n                f\"| {vals['naive']['rmse']:.4f} \"\n                f\"| {vals['global_corrected']['rmse']:.4f} \"\n                f\"| {vals['stratified_mle']['rmse']:.4f} \"\n                f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n                f\"| {vals['naive']['coverage']:.3f} \"\n                f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n                f\"| {vals['naive']['ci_width']:.4f} \"\n                f\"| {vals['hb_ec_hte']['ci_width']:.4f} \"\n                f\"| {hb_wins_bias} \"\n                f\"| {hb_wins_rmse} |\"\n            )\n        lines.append(\"\")\n\n        # Crossover analysis\n        lines.append(f\"### {k_label} Crossover Analysis\\n\")\n        crossover_bias = None\n        crossover_rmse = None\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            hb = sub[sub['method'] == 'hb_ec_hte']\n            nv = sub[sub['method'] == 'naive']\n            if len(hb) > 0 and len(nv) > 0:\n                if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                    crossover_bias = ne\n                if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                    crossover_rmse = ne\n\n        if crossover_bias is not None:\n            lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n        else:\n            lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n        if crossover_rmse is not None:\n            lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n        else:\n            lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n        lines.append(\"\")\n\n        # Bias-variance decomposition\n        lines.append(f\"### {k_label} Bias-Variance Decomposition\\n\")\n        lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n        lines.append(\"|----------|--------|--------|----------|-----|\")\n        for ne in N_EXPERT_LIST:\n            for m in ['naive', 'hb_ec_hte']:\n                sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n                cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                              .agg(['mean', 'var', 'count']).reset_index())\n                mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n                variance = cell_stats['var'].mean()\n                mse = mean_bias_sq + variance\n                lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n        lines.append(\"\")\n\n    # K=4 vs K=2 comparison\n    lines.append(\"## K=4 vs K=2 Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_echte_K4 | |Bias|_echte_K2 | RMSE_echte_K4 | RMSE_echte_K2 | Cov_echte_K4 | Cov_echte_K2 |\")\n    lines.append(\"|----------|----------------|----------------|---------------|---------------|--------------|--------------|\")\n    for ne in N_EXPERT_LIST:\n        hb4 = summary_k4[(summary_k4['n_expert'] == ne) & (summary_k4['method'] == 'hb_ec_hte')]\n        hb2 = summary_k2[(summary_k2['n_expert'] == ne) & (summary_k2['method'] == 'hb_ec_hte')]\n        if len(hb4) > 0 and len(hb2) > 0:\n            lines.append(\n                f\"| {ne} \"\n                f\"| {hb4.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb2.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb4.iloc[0]['rmse']:.4f} \"\n                f\"| {hb2.iloc[0]['rmse']:.4f} \"\n                f\"| {hb4.iloc[0]['coverage']:.3f} \"\n                f\"| {hb2.iloc[0]['coverage']:.3f} |\"\n            )\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    csv_path = 'artifacts/c1_multi_llm/gemma2_9b_balanced.csv'\n    profile = compute_cm_profile(csv_path)\n\n    # Prepare K=4 config\n    k4_labels = profile['k4']['labels']\n    k4_weights = profile['k4']['weights']\n    k4_cm = profile['k4']['cm']\n\n    # Prepare K=2 config\n    k2_labels = profile['k2']['labels']\n    k2_weights = profile['k2']['weights']\n    k2_cm = profile['k2']['cm']\n\n    p_z1 = profile['p_z1']\n\n    # Dry run K=4\n    print(\"\\n\\n=== DRY RUN K=4 ===\")\n    run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=True)\n\n    # Dry run K=2\n    print(\"\\n\\n=== DRY RUN K=2 ===\")\n    run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=True)\n\n    # Full K=4\n    print(\"\\n\\n=== FULL RUN K=4 ===\")\n    df_k4 = run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k4, f'{OUT_DIR}/gemma_budget_sweep_k4.csv')\n\n    # Full K=2\n    print(\"\\n\\n=== FULL RUN K=2 ===\")\n    df_k2 = run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k2, f'{OUT_DIR}/gemma_budget_sweep_k2.csv')\n\n    # Build summaries and write analysis\n    summary_k4 = build_summary(df_k4)\n    summary_k2 = build_summary(df_k2)\n\n    write_analysis(summary_k4, summary_k2, df_k4, df_k2,\n                   f'{OUT_DIR}/gemma_sweep_analysis.md', profile)\n\n    # Print final summary\n    print(\"\\n\\n=== FINAL SUMMARY ===\")\n    for k_label, summary in [(\"K=4\", summary_k4), (\"K=2\", summary_k2)]:\n        print(f\"\\n{k_label}:\")\n        for ne in N_EXPERT_LIST:\n            print(f\"  n_expert={ne}:\")\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n                if len(row) > 0:\n                    print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}  Cov={row.iloc[0]['coverage']:.3f}  CIW={row.iloc[0]['ci_width']:.4f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_sweep.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nGemma-2-9B full pipeline: CM profile + budget sweep (K=4 and K=2).\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\nOUT_DIR = 'artifacts/c1_multi_llm'\n\n# === Step 1: Compute per-subgroup CM from CSV ===\n\ndef compute_cm_profile(csv_path):\n    df = pd.read_csv(csv_path)\n\n    # Balanced binary Z\n    df['Z'] = (df['true_label'] >= 1).astype(int)\n    df['Z_hat'] = (df['llm_label'] >= 1).astype(int)\n\n    # Global stats\n    acc = (df['Z'] == df['Z_hat']).mean()\n    p_z1 = df['Z'].mean()\n\n    # Global FPR, FNR\n    neg = df[df['Z'] == 0]\n    pos = df[df['Z'] == 1]\n    fpr_global = (neg['Z_hat'] == 1).mean()\n    fnr_global = (pos['Z_hat'] == 0).mean()\n\n    print(f\"=== Gemma CM Profile ===\")\n    print(f\"N = {len(df)}, Accuracy = {acc:.3f}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"Global FPR = {fpr_global:.3f}, FNR = {fnr_global:.3f}\")\n    print(f\"Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    print()\n\n    # K=4: has_hashtag x text_length_bin (exclude \"long\")\n    df_k4 = df[df['text_length_bin'] != 'long'].copy()\n    df_k4['subgroup'] = df_k4['has_hashtag'].astype(str) + '_' + df_k4['text_length_bin']\n    k4_labels = sorted(df_k4['subgroup'].unique())\n\n    print(f\"K=4 subgroups (excluding 'long'): {k4_labels}\")\n    print(f\"K=4 sample size: {len(df_k4)}\")\n\n    k4_cm = {}\n    k4_weights = {}\n    k4_pi = {}\n    k4_kappa = {}\n\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df_k4)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k4_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k4_weights[s] = round(w_s, 3)\n        k4_pi[s] = round(pi_s, 3)\n        k4_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # K=2: has_hashtag only\n    df['subgroup_k2'] = df['has_hashtag'].astype(str)\n    k2_labels = sorted(df['subgroup_k2'].unique())\n\n    print(f\"K=2 subgroups: {k2_labels}\")\n\n    k2_cm = {}\n    k2_weights = {}\n    k2_pi = {}\n    k2_kappa = {}\n\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k2_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k2_weights[s] = round(w_s, 3)\n        k2_pi[s] = round(pi_s, 3)\n        k2_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # Write CM profile markdown\n    lines = []\n    lines.append(\"# Gemma-2-9B Confusion Matrix Profile\\n\")\n    lines.append(\"## Global Statistics\\n\")\n    lines.append(f\"- N = {len(df)}\")\n    lines.append(f\"- Accuracy = {acc:.3f}\")\n    lines.append(f\"- P(Z=1) = {p_z1:.3f}\")\n    lines.append(f\"- Global FPR = {fpr_global:.3f}\")\n    lines.append(f\"- Global FNR = {fnr_global:.3f}\")\n    lines.append(f\"- Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    lines.append(f\"- FNR > FPR asymmetry: {'YES' if fnr_global > fpr_global else 'NO'}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)\\n\")\n    lines.append(f\"- Sample size (excl. long): {len(df_k4)}\")\n    lines.append(\"\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k4_weights[s]:.3f} | {k4_pi[s]:.3f} | {k4_cm[s]['fpr']:.3f} | {k4_cm[s]['fnr']:.3f} | {k4_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k4 = max(k4_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k4:.2f}\")\n    prop2_count = sum(1 for s in k4_labels if k4_kappa[s] > 2.0)\n    lines.append(f\"- Prop2 triggered (kappa > 2): {prop2_count}/{len(k4_labels)}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=2 Subgroups (has_hashtag only)\\n\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k2_weights[s]:.3f} | {k2_pi[s]:.3f} | {k2_cm[s]['fpr']:.3f} | {k2_cm[s]['fnr']:.3f} | {k2_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k2 = max(k2_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k2:.2f}\")\n    lines.append(\"\")\n\n    profile_path = f'{OUT_DIR}/gemma_cm_profile.md'\n    with open(profile_path, 'w') as f:\n        f.write(\"\\n\".join(lines))\n    print(f\"Wrote {profile_path}\")\n\n    return {\n        'p_z1': p_z1,\n        'k4': {'labels': k4_labels, 'weights': k4_weights, 'cm': k4_cm},\n        'k2': {'labels': k2_labels, 'weights': k2_weights, 'cm': k2_cm},\n    }\n\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\n# === Estimators ===\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert, subgroup_labels, subgroup_weights, subgroup_cm, p_z1):\n    rng = np.random.RandomState(seed)\n    k = len(subgroup_labels)\n\n    S_idx = rng.choice(k, size=N, p=subgroup_weights)\n    S = np.array([subgroup_labels[i] for i in S_idx])\n\n    Z = rng.binomial(1, p_z1, N)\n    T = rng.binomial(1, 0.5, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(k):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(subgroup_cm[subgroup_labels[i]]['fpr'],\n                           subgroup_cm[subgroup_labels[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed, subgroup_labels):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, subgroup_labels)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, subgroup_labels)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, subgroup_labels)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in subgroup_labels:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in subgroup_labels:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            ci_w_nv = (ci_hi_nv - ci_lo_nv) if not np.isnan(ci_lo_nv) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            ci_w_gc = (ci_hi_gc - ci_lo_gc) if not np.isnan(ci_lo_gc) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            ci_w_ml = (ci_hi_ml - ci_lo_ml) if not np.isnan(ci_lo_ml) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            ci_w_hb = (ci_hi_hb - ci_lo_hb) if not np.isnan(ci_lo_hb) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    cell_w = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['ci_width']\n              .mean().reset_index(name='ci_width'))\n    return (cell_w.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Run sweep for one K config ===\n\ndef run_sweep(k_label, subgroup_labels, subgroup_weights_dict, subgroup_cm, p_z1, dry_run=False):\n    labels = subgroup_labels\n    weights_arr = np.array([subgroup_weights_dict[s] for s in labels])\n    weights_arr = weights_arr / weights_arr.sum()  # normalize\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Budget Sweep: Gemma {k_label}\")\n    print(f\"Subgroups: {labels}\")\n    print(f\"Weights: {dict(zip(labels, [round(w, 3) for w in weights_arr]))}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"tau(z=0) = {TAU_Z0}, tau(z=1) = {TAU_Z1}\")\n    print(f\"{'='*60}\")\n\n    if dry_run:\n        print(\"\\n--- Dry run (n_expert=100, 1 seed) ---\")\n        data = generate_data(SEED_BASE, 100, labels, weights_arr, subgroup_cm, p_z1)\n        rows = run_one_mc(data, SEED_BASE, labels)\n        df_dry = pd.DataFrame(rows)\n        df_dry['n_expert'] = 100\n        print(f\"Dry run OK: {len(df_dry)} rows\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_dry[df_dry['method'] == m]\n            bias = sub['bias'].abs().mean()\n            print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n        return None\n\n    # Full run\n    print(f\"\\nFull run: {len(N_EXPERT_LIST)} budgets x {N_MC} seeds\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert, labels, weights_arr, subgroup_cm, p_z1)\n            mc_rows = run_one_mc(data, seed, labels)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    return df_raw\n\n\ndef save_sweep_csv(df_raw, csv_path):\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level',\n                 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(csv_path, index=False)\n    print(f\"Saved {csv_path} ({len(df_raw)} rows)\")\n\n\ndef build_summary(df_raw):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n    return abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n\ndef write_analysis(summary_k4, summary_k2, df_k4, df_k2, outpath, profile):\n    lines = []\n    lines.append(\"# Gemma-2-9B Budget Sweep Analysis\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={profile['p_z1']:.3f}\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)\")\n    lines.append(f\"- Coverage = avg across cells of fraction(95% CI contains true CATE)\")\n    lines.append(f\"- CI Width = avg across cells of mean(CI_width)\")\n    lines.append(\"\")\n\n    for k_label, summary, df_raw in [(\"K=4\", summary_k4, df_k4), (\"K=2\", summary_k2, df_k2)]:\n        lines.append(f\"## {k_label} Summary Table\\n\")\n        lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |\")\n        lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|\")\n\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            vals = {}\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = sub[sub['method'] == m]\n                if len(row) > 0:\n                    vals[m] = {\n                        'abs_bias': row.iloc[0]['abs_bias'],\n                        'rmse': row.iloc[0]['rmse'],\n                        'coverage': row.iloc[0]['coverage'],\n                        'ci_width': row.iloc[0]['ci_width'],\n                    }\n                else:\n                    vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan, 'ci_width': np.nan}\n\n            hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n            hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n            lines.append(\n                f\"| {ne} \"\n                f\"| {vals['naive']['abs_bias']:.4f} \"\n                f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n                f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n                f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n                f\"| {vals['naive']['rmse']:.4f} \"\n                f\"| {vals['global_corrected']['rmse']:.4f} \"\n                f\"| {vals['stratified_mle']['rmse']:.4f} \"\n                f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n                f\"| {vals['naive']['coverage']:.3f} \"\n                f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n                f\"| {vals['naive']['ci_width']:.4f} \"\n                f\"| {vals['hb_ec_hte']['ci_width']:.4f} \"\n                f\"| {hb_wins_bias} \"\n                f\"| {hb_wins_rmse} |\"\n            )\n        lines.append(\"\")\n\n        # Crossover analysis\n        lines.append(f\"### {k_label} Crossover Analysis\\n\")\n        crossover_bias = None\n        crossover_rmse = None\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            hb = sub[sub['method'] == 'hb_ec_hte']\n            nv = sub[sub['method'] == 'naive']\n            if len(hb) > 0 and len(nv) > 0:\n                if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                    crossover_bias = ne\n                if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                    crossover_rmse = ne\n\n        if crossover_bias is not None:\n            lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n        else:\n            lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n        if crossover_rmse is not None:\n            lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n        else:\n            lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n        lines.append(\"\")\n\n        # Bias-variance decomposition\n        lines.append(f\"### {k_label} Bias-Variance Decomposition\\n\")\n        lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n        lines.append(\"|----------|--------|--------|----------|-----|\")\n        for ne in N_EXPERT_LIST:\n            for m in ['naive', 'hb_ec_hte']:\n                sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n                cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                              .agg(['mean', 'var', 'count']).reset_index())\n                mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n                variance = cell_stats['var'].mean()\n                mse = mean_bias_sq + variance\n                lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n        lines.append(\"\")\n\n    # K=4 vs K=2 comparison\n    lines.append(\"## K=4 vs K=2 Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_echte_K4 | |Bias|_echte_K2 | RMSE_echte_K4 | RMSE_echte_K2 | Cov_echte_K4 | Cov_echte_K2 |\")\n    lines.append(\"|----------|----------------|----------------|---------------|---------------|--------------|--------------|\")\n    for ne in N_EXPERT_LIST:\n        hb4 = summary_k4[(summary_k4['n_expert'] == ne) & (summary_k4['method'] == 'hb_ec_hte')]\n        hb2 = summary_k2[(summary_k2['n_expert'] == ne) & (summary_k2['method'] == 'hb_ec_hte')]\n        if len(hb4) > 0 and len(hb2) > 0:\n            lines.append(\n                f\"| {ne} \"\n                f\"| {hb4.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb2.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb4.iloc[0]['rmse']:.4f} \"\n                f\"| {hb2.iloc[0]['rmse']:.4f} \"\n                f\"| {hb4.iloc[0]['coverage']:.3f} \"\n                f\"| {hb2.iloc[0]['coverage']:.3f} |\"\n            )\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    csv_path = 'artifacts/c1_multi_llm/gemma2_9b_balanced.csv'\n    profile = compute_cm_profile(csv_path)\n\n    # Prepare K=4 config\n    k4_labels = profile['k4']['labels']\n    k4_weights = profile['k4']['weights']\n    k4_cm = profile['k4']['cm']\n\n    # Prepare K=2 config\n    k2_labels = profile['k2']['labels']\n    k2_weights = profile['k2']['weights']\n    k2_cm = profile['k2']['cm']\n\n    p_z1 = profile['p_z1']\n\n    # Dry run K=4\n    print(\"\\n\\n=== DRY RUN K=4 ===\")\n    run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=True)\n\n    # Dry run K=2\n    print(\"\\n\\n=== DRY RUN K=2 ===\")\n    run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=True)\n\n    # Full K=4\n    print(\"\\n\\n=== FULL RUN K=4 ===\")\n    df_k4 = run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k4, f'{OUT_DIR}/gemma_budget_sweep_k4.csv')\n\n    # Full K=2\n    print(\"\\n\\n=== FULL RUN K=2 ===\")\n    df_k2 = run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k2, f'{OUT_DIR}/gemma_budget_sweep_k2.csv')\n\n    # Build summaries and write analysis\n    summary_k4 = build_summary(df_k4)\n    summary_k2 = build_summary(df_k2)\n\n    write_analysis(summary_k4, summary_k2, df_k4, df_k2,\n                   f'{OUT_DIR}/gemma_sweep_analysis.md', profile)\n\n    # Print final summary\n    print(\"\\n\\n=== FINAL SUMMARY ===\")\n    for k_label, summary in [(\"K=4\", summary_k4), (\"K=2\", summary_k2)]:\n        print(f\"\\n{k_label}:\")\n        for ne in N_EXPERT_LIST:\n            print(f\"  n_expert={ne}:\")\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n                if len(row) > 0:\n                    print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}  Cov={row.iloc[0]['coverage']:.3f}  CIW={row.iloc[0]['ci_width']:.4f}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T22:13:38.202014+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_sweep.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T22:13:38.202173+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Bash",
  "tool_args": {
    "command": "python artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T22:13:38.202299+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T22:13:38.202417+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which python3 && python3 artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Bash",
  "tool_args": {
    "command": "which python3 && python3 artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T22:13:38.202587+00:00_

/usr/bin/python3
=== Gemma CM Profile ===
N = 500, Accuracy = 0.764
P(Z=1) = 0.652
Global FPR = 0.098, FNR = 0.310
Delta_pi = |FPR - FNR| = 0.212

K=4 subgroups (excluding 'long'): ['False_medium', 'False_short', 'True_medium', 'True_short']
K=4 sample size: 490
  False_medium        : n= 187, w=0.382, pi=0.465, FPR=0.110, FNR=0.437, kappa=2.21
  False_short         : n= 109, w=0.222, pi=0.734, FPR=0.138, FNR=0.300, kappa=1.78
  True_medium         : n= 125, w=0.255, pi=0.760, FPR=0.033, FNR=0.263, kappa=1.42
  True_short          : n=  69, w=0.141, pi=0.841, FPR=0.091, FNR=0.207, kappa=1.42

K=2 subgroups: ['False', 'True']
  False               : n= 302, w=0.604, pi=0.566, FPR=0.115, FNR=0.368, kappa=1.93
  True                : n= 198, w=0.396, pi=0.783, FPR=0.047, FNR=0.245, kappa=1.41

Wrote artifacts/c1_multi_llm/gemma_cm_profile.md


=== DRY RUN K=4 ===

============================================================
Budget Sweep: Gemma K=4
Subgroups: ['False_medium', 'False_short', 'True_medium', 'True_short']
Weights: {'False_medium': np.float64(0.382), 'False_short': np.float64(0.222), 'True_medium': np.float64(0.255), 'True_short': np.float64(0.141)}
P(Z=1) = 0.652
tau(z=0) = 0.35, tau(z=1) = 0.65
============================================================

--- Dry run (n_expert=100, 1 seed) ---
Dry run OK: 32 rows
  naive               : mean |bias| = 0.0663
  global_corrected    : mean |bias| = 0.0653
  stratified_mle      : mean |bias| = 0.0892
  hb_ec_hte           : mean |bias| = 0.0988


=== DRY RUN K=2 ===

============================================================
Budget Sweep: Gemma K=2
Subgroups: ['False', 'True']
Weights: {'False': np.float64(0.604), 'True': np.float64(0.396)}
P(Z=1) = 0.652
tau(z=0) = 0.35, tau(z=1) = 0.65
============================================================

--- Dry run (n_expert=100, 1 seed) ---
Dry run OK: 16 rows
  naive               : mean |bias| = 0.0517
  global_corrected    : mean |bias| = 0.1555
  stratified_
…[truncated 6329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T22:13:38.202759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_cm_profile.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_cm_profile.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T22:13:38.202946+00:00_

1	# Gemma-2-9B Confusion Matrix Profile
2	
3	## Global Statistics
4	
5	- N = 500
6	- Accuracy = 0.764
7	- P(Z=1) = 0.652
8	- Global FPR = 0.098
9	- Global FNR = 0.310
10	- Delta_pi = |FPR - FNR| = 0.212
11	- FNR > FPR asymmetry: YES
12	
13	## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)
14	
15	- Sample size (excl. long): 490
16	
17	| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |
18	|----------|---|--------|------|-----|-----|-------|
19	| False_medium | 187 | 0.382 | 0.465 | 0.110 | 0.437 | 2.21 |
20	| False_short | 109 | 0.222 | 0.734 | 0.138 | 0.300 | 1.78 |
21	| True_medium | 125 | 0.255 | 0.760 | 0.033 | 0.263 | 1.42 |
22	| True_short | 69 | 0.141 | 0.841 | 0.091 | 0.207 | 1.42 |
23	
24	- Max kappa = 2.21
25	- Prop2 triggered (kappa > 2): 1/4
26	
27	## K=2 Subgroups (has_hashtag only)
28	
29	| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |
30	|----------|---|--------|------|-----|-----|-------|
31	| False | 302 | 0.604 | 0.566 | 0.115 | 0.368 | 1.93 |
32	| True | 198 | 0.396 | 0.783 | 0.047 | 0.245 | 1.41 |
33	
34	- Max kappa = 1.93
35	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T22:13:38.203083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_sweep_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_sweep_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T22:13:38.203228+00:00_

1	# Gemma-2-9B Budget Sweep Analysis
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652
6	- tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
7	- n_expert sweep: [100, 200, 500, 1000, 2000]
8	- 50 MC seeds per budget
9	- HB method: MAP-EB (Gamma(3,1) prior)
10	- |Bias| = avg across cells of |mean(bias) across seeds|
11	- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)
12	- Coverage = avg across cells of fraction(95% CI contains true CATE)
13	- CI Width = avg across cells of mean(CI_width)
14	
15	## K=4 Summary Table
16	
17	| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |
18	|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|
19	| 100 | 0.0711 | 0.0202 | 0.1066 | 0.2106 | 0.1192 | 0.1950 | 0.6609 | 1.2291 | 0.775 | 0.690 | 0.3312 | 0.8005 | no | no |
20	| 200 | 0.0711 | 0.0223 | 0.0646 | 0.0676 | 0.1192 | 0.1682 | 0.3844 | 0.4212 | 0.775 | 0.790 | 0.3312 | 0.5810 | YES | no |
21	| 500 | 0.0711 | 0.0172 | 0.0244 | 0.0233 | 0.1192 | 0.1480 | 0.1844 | 0.1824 | 0.775 | 0.873 | 0.3312 | 0.5160 | YES | no |
22	| 1000 | 0.0711 | 0.0157 | 0.0180 | 0.0175 | 0.1192 | 0.1428 | 0.1549 | 0.1541 | 0.775 | 0.907 | 0.3312 | 0.5025 | YES | no |
23	| 2000 | 0.0711 | 0.0160 | 0.0161 | 0.0156 | 0.1192 | 0.1377 | 0.1394 | 0.1390 | 0.775 | 0.917 | 0.3312 | 0.4940 | YES | no |
24	
25	### K=4 Crossover Analysis
26	
27	- **|Bias| crossover**: EC-HTE beats Naive at n_expert=200
28	- **RMSE crossover**: EC-HTE never beats Naive in tested range
29	
30	### K=4 Bias-Variance Decomposition
31	
32	| n_expert | Method | Bias^2 | Variance | MSE |
33	|----------|--------|--------|----------|-----|
34	| 100 | naive | 0.0076 | 0.0079 | 0.0155 |
35	| 100 | hb_ec_hte | 0.1217 | 5.2627 | 5.3844 |
36	| 200 
…[truncated 2847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_gemma-budget-sweep_20260521T221030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-21T22:13:38.203419+00:00_

All 4 outputs generated successfully:

| File | Status |
|------|--------|
| `gemma_cm_profile.md` | Gemma Accuracy=0.764, FPR=0.098, FNR=0.310, Δπ=0.212, strong FNR>FPR asymmetry confirmed |
| `gemma_budget_sweep_k4.csv` | 8000 rows (5 budgets × 50 seeds × 4 subgroups × 2 z-levels × 4 methods) |
| `gemma_budget_sweep_k2.csv` | 4000 rows (5 budgets × 50 seeds × 2 subgroups × 2 z-levels × 4 methods) |
| `gemma_sweep_analysis.md` | Full analysis with summary tables, crossover, bias-variance decomposition, K4 vs K2 comparison |

Key findings:

**CM Profile:** Max κ=2.21 (K=4), only 1/4 subgroups with κ>2 (vs. task's claimed 4/4 — the "known" Gemma stats appear to be from a different binarization or dataset version). The `False_medium` subgroup has the worst FNR (0.437).

**K=4:** |Bias| crossover at n_expert=200, RMSE crossover never reached (variance cost of 4-way stratification is high at small budgets — K=4 with only 490 eligible observations means thin cells).

**K=2:** |Bias| crossover at n_expert=100, RMSE crossover at n_expert=1000. K=2 dominates K=4 across all budgets — fewer subgroups = less variance, and Gemma's CM heterogeneity between hashtag groups is substantial enough that K=2 still captures the important variation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_gemma-budget-sweep_20260521T221030"
}
```

</details>

---
