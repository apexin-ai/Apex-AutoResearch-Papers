# code exp 016 semi real better cm

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_code_exp-016-semi-real-better-cm_20260521T132011.jsonl`
- **Structured JSON:** [`6af22db39196e5b66ca6.json`](../../sessions/6a/6af22db39196e5b66ca6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-21T13:28:50.533762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp008_multi_llm_annotations.csv",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp008_multi_llm_annotations.csv",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T13:28:50.534182+00:00_

1	idx,text,true_label,gpt-4.1,has_hashtag,has_mention,text_length_bin,gpt-4o-mini,gpt-3.5-turbo,gpt-4o,gpt-4-turbo
2	10476,"when you jacked into your house without keys. hell yeah, i'm david blaine jr.",2,2,False,False,short,2,2,2,2
3	1824,Cigarettes and Valentines,1,1,False,False,short,1,1,1,1
4	409,@user we'll miss you in Seattle! Especially when you win your NL Cy Young award!,2,2,False,True,medium,2,2,2,2
5	12149,I'm not going to sack Tony romo but I will sack dak,0,0,False,False,short,0,0,0,0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T13:28:50.534361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T13:28:50.534630+00:00_

1	"""
2	exp-015: Semi-Real Confusion Matrix EC-HTE Experiment.
3	
4	Uses real asymmetric confusion matrices from GPT-4.1 TweetEval pilot annotations.
5	Ground truth CATE is synthetic, but CMs come from real LLM pilot data.
6	
7	4 subgroups with real asymmetric CMs (from pilot GPT-4.1 annotations, n>=10 only):
8	  S0 (False_medium): FPR=0.054, FNR=0.526, weight=0.38
9	  S1 (False_short):  FPR=0.101, FNR=0.300, weight=0.22
10	  S2 (True_short):   FPR=0.143, FNR=0.308, weight=0.14
11	  S3 (True_medium):  FPR=0.194, FNR=0.222, weight=0.25
12	
13	Output:
14	  results/exp015_semi_real_raw.csv
15	  results/exp015_semi_real_summary.csv
16	  results/exp015_semi_real_analysis.md
17	
18	Usage: python3 exp015_semi_real_cm.py --n-mc 100
19	"""
20	
21	import argparse
22	import time
23	import warnings
24	import numpy as np
25	import pandas as pd
26	from scipy.special import gammaln
27	
28	warnings.filterwarnings('ignore')
29	
30	# === Config ===
31	
32	N = 5000
33	N_EXPERTS = [100, 250, 500]
34	SEED_BASE = 0
35	
36	SUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']
37	SUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])
38	SUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()
39	
40	# Real asymmetric CMs from GPT-4.1 pilot (FPR, FNR per subgroup)
41	SUBGROUP_CM = {
42	    'S0': {'fpr': 0.054, 'fnr': 0.526},
43	    'S1': {'fpr': 0.101, 'fnr': 0.300},
44	    'S2': {'fpr': 0.143, 'fnr': 0.308},
45	    'S3': {'fpr': 0.194, 'fnr': 0.222},
46	}
47	
48	P_Z1 = 0.18  # P(Z=1) from pilot overall
49	P_T1 = 0.5
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: M[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# True CATE by (z, subgroup)
59	def true_tau(z, s_idx):
60	    if z == 0:
61	        return 0.3 + 0.1 * s_idx
62	    else:
63	        return 0.8 - 0.15 * s_idx
64	
65	
66	# === Core Estimators ===
67	
68	def diff_in_means(Y, T, mask):
69	    t1 = mask & (T == 1)
70	    t0 = mask & (T == 0)
71	    n
…[truncated 21934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T13:28:50.534854+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\ndf = pd.read_csv('results/exp008_multi_llm_annotations.csv')\nprint('Columns:', list(df.columns))\nprint('Shape:', df.shape)\nprint()\n\n# Models\nmodels = ['gpt-3.5-turbo', 'gpt-4-turbo', 'gpt-4.1', 'gpt-4o', 'gpt-4o-mini']\n# Check if gpt-5.4 exists\nif 'gpt-5.4' in df.columns:\n    models.append('gpt-5.4')\n\n# Binarize: Z=1 iff label==2\ndf['true_z'] = (df['true_label'] == 2).astype(int)\n\n# Subgroups\ndf['subgroup'] = df['has_hashtag'].astype(str) + '_' + df['text_length_bin']\nprint('Subgroup counts:')\nprint(df['subgroup'].value_counts().sort_index())\nprint()\n\n# Filter to n>=10 subgroups\nvalid_subgroups = ['False_medium', 'False_short', 'True_medium', 'True_short']\n\nfor model in models:\n    df[f'{model}_z'] = (df[model] == 2).astype(int)\n    print(f'=== {model} ===')\n    worst_fnr = 0\n    for sg in valid_subgroups:\n        mask = df['subgroup'] == sg\n        z_true = df.loc[mask, 'true_z'].values\n        z_hat = df.loc[mask, f'{model}_z'].values\n        n = mask.sum()\n        \n        TP = ((z_true == 1) & (z_hat == 1)).sum()\n        FP = ((z_true == 0) & (z_hat == 1)).sum()\n        FN = ((z_true == 1) & (z_hat == 0)).sum()\n        TN = ((z_true == 0) & (z_hat == 0)).sum()\n        \n        FPR = FP / (FP + TN) if (FP + TN) > 0 else 0\n        FNR = FN / (FN + TP) if (FN + TP) > 0 else 0\n        \n        print(f'  {sg:15s} (n={n:4d}): TP={TP:3d} FP={FP:3d} FN={FN:3d} TN={TN:3d}  FPR={FPR:.3f} FNR={FNR:.3f}')\n        worst_fnr = max(worst_fnr, FNR)\n    print(f'  >>> Worst-subgroup FNR = {worst_fnr:.3f}')\n    print()\n\"\n",
  "description": "Compute per-subgroup FPR/FNR for all models in exp-008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\ndf = pd.read_csv('results/exp008_multi_llm_annotations.csv')\nprint('Columns:', list(df.columns))\nprint('Shape:', df.shape)\nprint()\n\n# Models\nmodels = ['gpt-3.5-turbo', 'gpt-4-turbo', 'gpt-4.1', 'gpt-4o', 'gpt-4o-mini']\n# Check if gpt-5.4 exists\nif 'gpt-5.4' in df.columns:\n    models.append('gpt-5.4')\n\n# Binarize: Z=1 iff label==2\ndf['true_z'] = (df['true_label'] == 2).astype(int)\n\n# Subgroups\ndf['subgroup'] = df['has_hashtag'].astype(str) + '_' + df['text_length_bin']\nprint('Subgroup counts:')\nprint(df['subgroup'].value_counts().sort_index())\nprint()\n\n# Filter to n>=10 subgroups\nvalid_subgroups = ['False_medium', 'False_short', 'True_medium', 'True_short']\n\nfor model in models:\n    df[f'{model}_z'] = (df[model] == 2).astype(int)\n    print(f'=== {model} ===')\n    worst_fnr = 0\n    for sg in valid_subgroups:\n        mask = df['subgroup'] == sg\n        z_true = df.loc[mask, 'true_z'].values\n        z_hat = df.loc[mask, f'{model}_z'].values\n        n = mask.sum()\n        \n        TP = ((z_true == 1) & (z_hat == 1)).sum()\n        FP = ((z_true == 0) & (z_hat == 1)).sum()\n        FN = ((z_true == 1) & (z_hat == 0)).sum()\n        TN = ((z_true == 0) & (z_hat == 0)).sum()\n        \n        FPR = FP / (FP + TN) if (FP + TN) > 0 else 0\n        FNR = FN / (FN + TP) if (FN + TP) > 0 else 0\n        \n        print(f'  {sg:15s} (n={n:4d}): TP={TP:3d} FP={FP:3d} FN={FN:3d} TN={TN:3d}  FPR={FPR:.3f} FNR={FNR:.3f}')\n        worst_fnr = max(worst_fnr, FNR)\n    print(f'  >>> Worst-subgroup FNR = {worst_fnr:.3f}')\n    print()\n\"\n",
    "description": "Compute per-subgroup FPR/FNR for all models in exp-008"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T13:28:50.535053+00:00_

Columns: ['idx', 'text', 'true_label', 'gpt-4.1', 'has_hashtag', 'has_mention', 'text_length_bin', 'gpt-4o-mini', 'gpt-3.5-turbo', 'gpt-4o', 'gpt-4-turbo']
Shape: (500, 11)

Subgroup counts:
subgroup
False_long        6
False_medium    187
False_short     109
True_long         4
True_medium     125
True_short       69
Name: count, dtype: int64

=== gpt-3.5-turbo ===
  False_medium    (n= 187): TP= 15 FP= 24 FN=  4 TN=144  FPR=0.143 FNR=0.211
  False_short     (n= 109): TP= 17 FP= 16 FN=  3 TN= 73  FPR=0.180 FNR=0.150
  True_medium     (n= 125): TP= 23 FP= 37 FN=  4 TN= 61  FPR=0.378 FNR=0.148
  True_short      (n=  69): TP= 11 FP= 22 FN=  2 TN= 34  FPR=0.393 FNR=0.154
  >>> Worst-subgroup FNR = 0.211

=== gpt-4-turbo ===
  False_medium    (n= 187): TP= 12 FP=  7 FN=  7 TN=161  FPR=0.042 FNR=0.368
  False_short     (n= 109): TP=  9 FP=  8 FN= 11 TN= 81  FPR=0.090 FNR=0.550
  True_medium     (n= 125): TP= 19 FP= 20 FN=  8 TN= 78  FPR=0.204 FNR=0.296
  True_short      (n=  69): TP= 11 FP=  6 FN=  2 TN= 50  FPR=0.107 FNR=0.154
  >>> Worst-subgroup FNR = 0.550

=== gpt-4.1 ===
  False_medium    (n= 187): TP=  9 FP=  9 FN= 10 TN=159  FPR=0.054 FNR=0.526
  False_short     (n= 109): TP= 14 FP=  9 FN=  6 TN= 80  FPR=0.101 FNR=0.300
  True_medium     (n= 125): TP= 21 FP= 19 FN=  6 TN= 79  FPR=0.194 FNR=0.222
  True_short      (n=  69): TP=  9 FP=  8 FN=  4 TN= 48  FPR=0.143 FNR=0.308
  >>> Worst-subgroup FNR = 0.526

=== gpt-4o ===
  False_medium    (n= 187): TP=  8 FP=  7 FN= 11 TN=161  FPR=0.042 FNR=0.579
  False_short     (n= 109): TP= 10 FP=  4 FN= 10 TN= 85  FPR=0.045 FNR=0.500
  True_medium     (n= 125): TP= 14 FP=  9 FN= 13 TN= 89  FPR=0.092 FNR=0.481
  True_short      (n=  69): TP=  9 FP=  4 FN=  4 TN= 52  FPR=0.071 FNR=0.308
  >>> Worst-subgroup FNR = 0.579

=== gpt-4o-mini ===
  False_medium    (n= 187): TP= 11 FP=  7 FN=  8 TN=161  FPR=0.042 FNR=0.421
  False_short     (n= 109): TP= 12 FP=  5 FN=  8 TN= 84  FPR=0.056 FNR=0.400
  True_medium     (n= 125): TP= 19 FP=
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T13:28:50.535248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp015_semi_real_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp015_semi_real_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T13:28:50.535427+00:00_

1	# exp-015: Semi-Real Confusion Matrix EC-HTE Experiment
2	
3	## Design
4	
5	Uses **real asymmetric confusion matrices** from GPT-4.1 TweetEval pilot annotations.
6	Ground truth CATE is synthetic; confusion matrices are empirical.
7	
8	| Subgroup | Weight | FPR | FNR |
9	|----------|--------|-----|-----|
10	| S0 | 0.38 | 0.054 | 0.526 |
11	| S1 | 0.22 | 0.101 | 0.300 |
12	| S2 | 0.14 | 0.143 | 0.308 |
13	| S3 | 0.25 | 0.194 | 0.222 |
14	
15	**True CATE**: tau(z=0,s) = 0.3 + 0.1*s_idx; tau(z=1,s) = 0.8 - 0.15*s_idx
16	
17	| Subgroup | tau(z=0) | tau(z=1) |
18	|----------|----------|----------|
19	| S0 | 0.30 | 0.80 |
20	| S1 | 0.40 | 0.65 |
21	| S2 | 0.50 | 0.50 |
22	| S3 | 0.60 | 0.35 |
23	
24	N=5000, P(Z=1)=0.18, P(T=1)=0.5, n_expert in {100, 250, 500}, 100 MC seeds.
25	
26	## Summary Tables
27	
28	### n_expert = 100
29	
30	| Subgroup | Z | Method | Mean Bias | Mean |Bias| | RMSE | Coverage |
31	|----------|---|--------|-----------|-------------|------|----------|
32	| S0 | 0 | global_corrected | +0.0022 | 0.0644 | 0.0823 | 0.920 |
33	| S0 | 0 | hb_ec_hte | +0.0247 | 0.1052 | 0.1864 | 0.790 |
34	| S0 | 0 | naive | +0.0603 | 0.0629 | 0.0751 | 0.780 |
35	| S0 | 0 | oracle | +0.0073 | 0.0394 | 0.0491 | 0.950 |
36	| S0 | 1 | global_corrected | +0.1960 | 0.3665 | 0.5011 | 0.810 |
37	| S0 | 1 | hb_ec_hte | +0.1061 | 0.5946 | 1.1621 | 0.630 |
38	| S0 | 1 | naive | -0.1538 | 0.1713 | 0.2069 | 0.750 |
39	| S0 | 1 | oracle | +0.0101 | 0.0901 | 0.1088 | 0.960 |
40	| S1 | 0 | global_corrected | -0.0096 | 0.0812 | 0.1029 | 0.900 |
41	| S1 | 0 | hb_ec_hte | -0.0059 | 0.1049 | 0.1449 | 0.870 |
42	| S1 | 0 | naive | +0.0129 | 0.0547 | 0.0679 | 0.950 |
43	| S1 | 0 | oracle | -0.0039 | 0.0503 | 0.0649 | 0.960 |
44	| S1 | 1 | global_corrected | +0.0530 | 0.3103 | 0.4022 | 0.830 |
45	| S1 | 1 | hb_ec_hte | +0.3539 | 0.6880 | 1.6854 | 0.710 |
46	| S1 | 1 | naive | -0.1004 | 0.1414 | 0.1667 | 0.900 |
47	| S1 | 1 | oracle | -0.0085 | 0.1203 | 0.1461 | 0.940 |
48	| S2 | 0 | global_correc
…[truncated 7531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T13:28:50.535675+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py",
  "content": "\"\"\"\nexp-016: Semi-Real CM with Better Model (lower worst-subgroup FNR).\n\nSelected model: gpt-3.5-turbo (worst-subgroup FNR=0.211, vs GPT-4.1's 0.526 in exp-015).\ngpt-3.5-turbo trades higher FPR for much lower FNR across all subgroups.\n\n4 subgroups with real asymmetric CMs (from exp-008 pilot annotations, n>=10 only):\n  S0 (False_medium): FPR=0.143, FNR=0.211, weight=0.38\n  S1 (False_short):  FPR=0.180, FNR=0.150, weight=0.22\n  S2 (True_short):   FPR=0.393, FNR=0.154, weight=0.14\n  S3 (True_medium):  FPR=0.378, FNR=0.148, weight=0.25\n\nOutput:\n  results/exp016_semi_real_raw.csv\n  results/exp016_semi_real_analysis.md\n\nUsage: python3 exp016_semi_real_better_cm.py --n-mc 100\n\"\"\"\n\nimport argparse\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERTS = [100, 250, 500]\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']\nSUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\n# Real asymmetric CMs from gpt-3.5-turbo (exp-008 pilot)\nSUBGROUP_CM = {\n    'S0': {'fpr': 0.143, 'fnr': 0.211},  # False_medium\n    'S1': {'fpr': 0.180, 'fnr': 0.150},  # False_short\n    'S2': {'fpr': 0.393, 'fnr': 0.154},  # True_short\n    'S3': {'fpr': 0.378, 'fnr': 0.148},  # True_medium\n}\n\n# exp-015 CMs for comparison (GPT-4.1)\nEXP015_CM = {\n    'S0': {'fpr': 0.054, 'fnr': 0.526},\n    'S1': {'fpr': 0.101, 'fnr': 0.300},\n    'S2': {'fpr': 0.143, 'fnr': 0.308},\n    'S3': {'fpr': 0.194, 'fnr': 0.222},\n}\n\nP_Z1 = 0.18\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\ndef true_tau(z, s_idx):\n    if z == 0:\n        return 0.3 + 0.1 * s_idx\n    else:\n        return 0.8 - 0.15 * s_idx\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                theta_samples[idx] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {}\n\n\n# === DGP ===\n\ndef generate_data(n_expert, seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i in range(4):\n        s_mask = S_idx == i\n        tau_vals[s_mask & (Z == 0)] = true_tau(0, i)\n        tau_vals[s_mask & (Z == 1)] = true_tau(1, i)\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, n_expert, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    S_idx = data['S_idx']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_hb_sub = {}\n    for i, s_val in enumerate(SUBGROUP_LABELS):\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_i, s_val in enumerate(SUBGROUP_LABELS):\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = true_tau(z_level, s_i)\n\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'oracle',\n                'cate': th_or, 'oracle_cate': oracle_cate,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'ci_lo': ci_lo_or, 'ci_hi': ci_hi_or, 'coverage': cov_or,\n            })\n\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'naive',\n                'cate': th_nv, 'oracle_cate': oracle_cate,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'ci_lo': ci_lo_nv, 'ci_hi': ci_hi_nv, 'coverage': cov_nv,\n            })\n\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc = tau_gc[z_level]\n                se_gc_z = se_gc[z_level]\n            else:\n                th_gc, se_gc_z = np.nan, np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'global_corrected',\n                'cate': th_gc, 'oracle_cate': oracle_cate,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'ci_lo': ci_lo_gc, 'ci_hi': ci_hi_gc, 'coverage': cov_gc,\n            })\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb = tau_hb[z_level]\n                se_hb_z = se_hb[z_level]\n            else:\n                th_hb, se_hb_z = np.nan, np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'hb_ec_hte',\n                'cate': th_hb, 'oracle_cate': oracle_cate,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'ci_lo': ci_lo_hb, 'ci_hi': ci_hi_hb, 'coverage': cov_hb,\n            })\n\n    return rows\n\n\ndef aggregate_results(df_raw):\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['mean_rmse'] = np.sqrt((valid ** 2).mean())\n        row['mean_coverage'] = grp['coverage'].mean()\n        row['se_bias'] = valid.std() / np.sqrt(len(valid))\n        row['se_rmse'] = row['mean_rmse'] / np.sqrt(2 * len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef write_analysis(df_summary):\n    lines = []\n    lines.append(\"# exp-016: Semi-Real CM with Better Model\\n\")\n    lines.append(\"## Model Selection\\n\")\n    lines.append(\"Selected **gpt-3.5-turbo** from exp-008 pilot data (lowest worst-subgroup FNR).\\n\")\n    lines.append(\"| Model | Worst-subgroup FNR | Meets threshold (<0.4) |\")\n    lines.append(\"|-------|-------------------|------------------------|\")\n    lines.append(\"| gpt-3.5-turbo | 0.211 | Yes |\")\n    lines.append(\"| gpt-4o-mini | 0.421 | No |\")\n    lines.append(\"| gpt-4.1 (exp-015) | 0.526 | No |\")\n    lines.append(\"| gpt-4-turbo | 0.550 | No |\")\n    lines.append(\"| gpt-4o | 0.579 | No |\")\n    lines.append(\"\")\n    lines.append(\"gpt-3.5-turbo trades higher FPR for much lower FNR (more aggressive positive predictions).\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"| Subgroup | Name | Weight | FPR | FNR | exp-015 FPR | exp-015 FNR |\")\n    lines.append(\"|----------|------|--------|-----|-----|-------------|-------------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        cm15 = EXP015_CM[s]\n        names = ['False_medium', 'False_short', 'True_short', 'True_medium']\n        lines.append(f\"| {s} | {names[i]} | {SUBGROUP_WEIGHTS[i]:.2f} | \"\n                     f\"{cm['fpr']:.3f} | {cm['fnr']:.3f} | \"\n                     f\"{cm15['fpr']:.3f} | {cm15['fnr']:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"**True CATE**: tau(z=0,s) = 0.3 + 0.1*s_idx; tau(z=1,s) = 0.8 - 0.15*s_idx\\n\")\n    lines.append(\"| Subgroup | tau(z=0) | tau(z=1) |\")\n    lines.append(\"|----------|----------|----------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        lines.append(f\"| {s} | {true_tau(0,i):.2f} | {true_tau(1,i):.2f} |\")\n    lines.append(\"\")\n    lines.append(\"N=5000, P(Z=1)=0.18, P(T=1)=0.5, n_expert in {100, 250, 500}, 100 MC seeds.\\n\")\n\n    lines.append(\"## Summary Tables\\n\")\n    for ne in N_EXPERTS:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        sub = df_summary[df_summary['n_expert'] == ne].copy()\n        sub = sub.sort_values(['subgroup', 'z_level', 'method'])\n        lines.append(\"| Subgroup | Z | Method | Mean Bias | Mean |Bias| | RMSE | Coverage |\")\n        lines.append(\"|----------|---|--------|-----------|-------------|------|----------|\")\n        for _, r in sub.iterrows():\n            lines.append(f\"| {r['subgroup']} | {int(r['z_level'])} | {r['method']} | \"\n                         f\"{r['mean_bias']:+.4f} | {r['mean_abs_bias']:.4f} | \"\n                         f\"{r['mean_rmse']:.4f} | {r['mean_coverage']:.3f} |\")\n        lines.append(\"\")\n\n    lines.append(\"## Key Comparisons\\n\")\n    lines.append(\"### HB EC-HTE vs Global Corrected: Bias Reduction\\n\")\n    lines.append(\"| n_expert | Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|----------|---|------------|----------------|-----------|\")\n    for ne in N_EXPERTS:\n        for s in SUBGROUP_LABELS:\n            for z in [0, 1]:\n                hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &\n                                (df_summary['z_level'] == z) & (df_summary['method'] == 'hb_ec_hte')]\n                gc = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &\n                                (df_summary['z_level'] == z) & (df_summary['method'] == 'global_corrected')]\n                if len(hb) > 0 and len(gc) > 0:\n                    hb_b = hb.iloc[0]['mean_abs_bias']\n                    gc_b = gc.iloc[0]['mean_abs_bias']\n                    red = (gc_b - hb_b) / gc_b * 100 if gc_b > 0 else 0\n                    lines.append(f\"| {ne} | {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n    lines.append(\"\")\n\n    lines.append(\"### Coverage (95% CI)\\n\")\n    lines.append(\"| n_expert | Method | Mean Coverage |\")\n    lines.append(\"|----------|--------|---------------|\")\n    for ne in N_EXPERTS:\n        for m in ['oracle', 'naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['mean_coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    lines.append(\"## Comparison with exp-015 (GPT-4.1 CM)\\n\")\n    lines.append(\"### Overall RMSE by method and n_expert\\n\")\n    lines.append(\"| n_expert | Method | exp-016 (gpt-3.5-turbo) | exp-015 (GPT-4.1) |\")\n    lines.append(\"|----------|--------|-------------------------|---------------------|\")\n\n    exp015_rmse = {\n        100: {'naive': 0.1230, 'global_corrected': 0.2631, 'hb_ec_hte': 0.7842},\n        250: {'naive': 0.1230, 'global_corrected': 0.2318, 'hb_ec_hte': 0.4113},\n        500: {'naive': 0.1230, 'global_corrected': 0.1963, 'hb_ec_hte': 0.2599},\n    }\n    exp015_cov = {\n        100: {'naive': 0.879, 'global_corrected': 0.885, 'hb_ec_hte': 0.744},\n        250: {'naive': 0.879, 'global_corrected': 0.909, 'hb_ec_hte': 0.834},\n        500: {'naive': 0.879, 'global_corrected': 0.922, 'hb_ec_hte': 0.890},\n    }\n\n    for ne in N_EXPERTS:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                rmse_016 = sub['mean_rmse'].mean()\n                rmse_015 = exp015_rmse[ne][m]\n                lines.append(f\"| {ne} | {m} | {rmse_016:.4f} | {rmse_015:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Overall Coverage by method and n_expert\\n\")\n    lines.append(\"| n_expert | Method | exp-016 (gpt-3.5-turbo) | exp-015 (GPT-4.1) |\")\n    lines.append(\"|----------|--------|-------------------------|---------------------|\")\n    for ne in N_EXPERTS:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                cov_016 = sub['mean_coverage'].mean()\n                cov_015 = exp015_cov[ne][m]\n                lines.append(f\"| {ne} | {m} | {cov_016:.3f} | {cov_015:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(\"## Conclusion\\n\")\n    for ne in N_EXPERTS:\n        hb_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        gc_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'global_corrected')]\n        nv_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        if len(hb_all) > 0 and len(gc_all) > 0:\n            hb_rmse = hb_all['mean_rmse'].mean()\n            gc_rmse = gc_all['mean_rmse'].mean()\n            nv_rmse = nv_all['mean_rmse'].mean()\n            hb_cov = hb_all['mean_coverage'].mean()\n            gc_cov = gc_all['mean_coverage'].mean()\n            nv_cov = nv_all['mean_coverage'].mean()\n            lines.append(f\"- n_expert={ne}: HB RMSE={hb_rmse:.4f} (cov={hb_cov:.3f}), \"\n                         f\"Global RMSE={gc_rmse:.4f} (cov={gc_cov:.3f}), \"\n                         f\"Naive RMSE={nv_rmse:.4f} (cov={nv_cov:.3f})\")\n\n    report = \"\\n\".join(lines)\n    with open('results/exp016_semi_real_analysis.md', 'w') as f:\n        f.write(report)\n    print(\"Wrote results/exp016_semi_real_analysis.md\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    args = parser.parse_args()\n    n_mc = args.n_mc\n\n    print(f\"exp-016: Semi-Real CM with Better Model (gpt-3.5-turbo)\")\n    print(f\"N={N}, n_mc={n_mc}, n_experts={N_EXPERTS}\")\n    print(f\"Subgroup CMs (real asymmetric from gpt-3.5-turbo pilot):\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print(f\"Methods: oracle, naive, global_corrected, hb_ec_hte\")\n    print()\n\n    results = []\n    configs = [(ne, mc) for ne in N_EXPERTS for mc in range(n_mc)]\n    total = len(configs)\n    t0 = time.time()\n\n    for count, (ne, mc) in enumerate(configs, 1):\n        seed = SEED_BASE + mc\n        data = generate_data(ne, seed)\n        mc_rows = run_one_mc(data, ne, seed)\n        results.extend(mc_rows)\n        if count % max(1, total // 20) == 0:\n            elapsed = time.time() - t0\n            eta = elapsed / count * (total - count)\n            print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | ne={ne} seed={seed}\")\n\n    elapsed = time.time() - t0\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_raw['abs_bias'] = df_raw['bias'].abs()\n    df_raw['squared_error'] = df_raw['bias'] ** 2\n\n    df_summary = aggregate_results(df_raw)\n\n    df_raw.to_csv('results/exp016_semi_real_raw.csv', index=False)\n    print(f\"Saved results/exp016_semi_real_raw.csv ({len(df_raw)} rows)\")\n\n    write_analysis(df_summary)\n\n    print(\"\\n=== Key Metrics Summary ===\\n\")\n    pd.set_option('display.float_format', '{:.4f}'.format)\n    pd.set_option('display.width', 200)\n    for ne in N_EXPERTS:\n        print(f\"--- n_expert = {ne} ---\")\n        sub = df_summary[df_summary['n_expert'] == ne]\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            ms = sub[sub['method'] == m]\n            print(f\"  {m:20s}: mean_abs_bias={ms['mean_abs_bias'].mean():.4f}, \"\n                  f\"rmse={ms['mean_rmse'].mean():.4f}, coverage={ms['mean_coverage'].mean():.3f}\")\n        print()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py",
    "content": "\"\"\"\nexp-016: Semi-Real CM with Better Model (lower worst-subgroup FNR).\n\nSelected model: gpt-3.5-turbo (worst-subgroup FNR=0.211, vs GPT-4.1's 0.526 in exp-015).\ngpt-3.5-turbo trades higher FPR for much lower FNR across all subgroups.\n\n4 subgroups with real asymmetric CMs (from exp-008 pilot annotations, n>=10 only):\n  S0 (False_medium): FPR=0.143, FNR=0.211, weight=0.38\n  S1 (False_short):  FPR=0.180, FNR=0.150, weight=0.22\n  S2 (True_short):   FPR=0.393, FNR=0.154, weight=0.14\n  S3 (True_medium):  FPR=0.378, FNR=0.148, weight=0.25\n\nOutput:\n  results/exp016_semi_real_raw.csv\n  results/exp016_semi_real_analysis.md\n\nUsage: python3 exp016_semi_real_better_cm.py --n-mc 100\n\"\"\"\n\nimport argparse\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERTS = [100, 250, 500]\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']\nSUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\n# Real asymmetric CMs from gpt-3.5-turbo (exp-008 pilot)\nSUBGROUP_CM = {\n    'S0': {'fpr': 0.143, 'fnr': 0.211},  # False_medium\n    'S1': {'fpr': 0.180, 'fnr': 0.150},  # False_short\n    'S2': {'fpr': 0.393, 'fnr': 0.154},  # True_short\n    'S3': {'fpr': 0.378, 'fnr': 0.148},  # True_medium\n}\n\n# exp-015 CMs for comparison (GPT-4.1)\nEXP015_CM = {\n    'S0': {'fpr': 0.054, 'fnr': 0.526},\n    'S1': {'fpr': 0.101, 'fnr': 0.300},\n    'S2': {'fpr': 0.143, 'fnr': 0.308},\n    'S3': {'fpr': 0.194, 'fnr': 0.222},\n}\n\nP_Z1 = 0.18\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\ndef true_tau(z, s_idx):\n    if z == 0:\n        return 0.3 + 0.1 * s_idx\n    else:\n        return 0.8 - 0.15 * s_idx\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                theta_samples[idx] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {}\n\n\n# === DGP ===\n\ndef generate_data(n_expert, seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i in range(4):\n        s_mask = S_idx == i\n        tau_vals[s_mask & (Z == 0)] = true_tau(0, i)\n        tau_vals[s_mask & (Z == 1)] = true_tau(1, i)\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, n_expert, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    S_idx = data['S_idx']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_hb_sub = {}\n    for i, s_val in enumerate(SUBGROUP_LABELS):\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_i, s_val in enumerate(SUBGROUP_LABELS):\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = true_tau(z_level, s_i)\n\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'oracle',\n                'cate': th_or, 'oracle_cate': oracle_cate,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'ci_lo': ci_lo_or, 'ci_hi': ci_hi_or, 'coverage': cov_or,\n            })\n\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'naive',\n                'cate': th_nv, 'oracle_cate': oracle_cate,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'ci_lo': ci_lo_nv, 'ci_hi': ci_hi_nv, 'coverage': cov_nv,\n            })\n\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc = tau_gc[z_level]\n                se_gc_z = se_gc[z_level]\n            else:\n                th_gc, se_gc_z = np.nan, np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'global_corrected',\n                'cate': th_gc, 'oracle_cate': oracle_cate,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'ci_lo': ci_lo_gc, 'ci_hi': ci_hi_gc, 'coverage': cov_gc,\n            })\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb = tau_hb[z_level]\n                se_hb_z = se_hb[z_level]\n            else:\n                th_hb, se_hb_z = np.nan, np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'hb_ec_hte',\n                'cate': th_hb, 'oracle_cate': oracle_cate,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'ci_lo': ci_lo_hb, 'ci_hi': ci_hi_hb, 'coverage': cov_hb,\n            })\n\n    return rows\n\n\ndef aggregate_results(df_raw):\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['mean_rmse'] = np.sqrt((valid ** 2).mean())\n        row['mean_coverage'] = grp['coverage'].mean()\n        row['se_bias'] = valid.std() / np.sqrt(len(valid))\n        row['se_rmse'] = row['mean_rmse'] / np.sqrt(2 * len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef write_analysis(df_summary):\n    lines = []\n    lines.append(\"# exp-016: Semi-Real CM with Better Model\\n\")\n    lines.append(\"## Model Selection\\n\")\n    lines.append(\"Selected **gpt-3.5-turbo** from exp-008 pilot data (lowest worst-subgroup FNR).\\n\")\n    lines.append(\"| Model | Worst-subgroup FNR | Meets threshold (<0.4) |\")\n    lines.append(\"|-------|-------------------|------------------------|\")\n    lines.append(\"| gpt-3.5-turbo | 0.211 | Yes |\")\n    lines.append(\"| gpt-4o-mini | 0.421 | No |\")\n    lines.append(\"| gpt-4.1 (exp-015) | 0.526 | No |\")\n    lines.append(\"| gpt-4-turbo | 0.550 | No |\")\n    lines.append(\"| gpt-4o | 0.579 | No |\")\n    lines.append(\"\")\n    lines.append(\"gpt-3.5-turbo trades higher FPR for much lower FNR (more aggressive positive predictions).\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"| Subgroup | Name | Weight | FPR | FNR | exp-015 FPR | exp-015 FNR |\")\n    lines.append(\"|----------|------|--------|-----|-----|-------------|-------------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        cm15 = EXP015_CM[s]\n        names = ['False_medium', 'False_short', 'True_short', 'True_medium']\n        lines.append(f\"| {s} | {names[i]} | {SUBGROUP_WEIGHTS[i]:.2f} | \"\n                     f\"{cm['fpr']:.3f} | {cm['fnr']:.3f} | \"\n                     f\"{cm15['fpr']:.3f} | {cm15['fnr']:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"**True CATE**: tau(z=0,s) = 0.3 + 0.1*s_idx; tau(z=1,s) = 0.8 - 0.15*s_idx\\n\")\n    lines.append(\"| Subgroup | tau(z=0) | tau(z=1) |\")\n    lines.append(\"|----------|----------|----------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        lines.append(f\"| {s} | {true_tau(0,i):.2f} | {true_tau(1,i):.2f} |\")\n    lines.append(\"\")\n    lines.append(\"N=5000, P(Z=1)=0.18, P(T=1)=0.5, n_expert in {100, 250, 500}, 100 MC seeds.\\n\")\n\n    lines.append(\"## Summary Tables\\n\")\n    for ne in N_EXPERTS:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        sub = df_summary[df_summary['n_expert'] == ne].copy()\n        sub = sub.sort_values(['subgroup', 'z_level', 'method'])\n        lines.append(\"| Subgroup | Z | Method | Mean Bias | Mean |Bias| | RMSE | Coverage |\")\n        lines.append(\"|----------|---|--------|-----------|-------------|------|----------|\")\n        for _, r in sub.iterrows():\n            lines.append(f\"| {r['subgroup']} | {int(r['z_level'])} | {r['method']} | \"\n                         f\"{r['mean_bias']:+.4f} | {r['mean_abs_bias']:.4f} | \"\n                         f\"{r['mean_rmse']:.4f} | {r['mean_coverage']:.3f} |\")\n        lines.append(\"\")\n\n    lines.append(\"## Key Comparisons\\n\")\n    lines.append(\"### HB EC-HTE vs Global Corrected: Bias Reduction\\n\")\n    lines.append(\"| n_expert | Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|----------|---|------------|----------------|-----------|\")\n    for ne in N_EXPERTS:\n        for s in SUBGROUP_LABELS:\n            for z in [0, 1]:\n                hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &\n                                (df_summary['z_level'] == z) & (df_summary['method'] == 'hb_ec_hte')]\n                gc = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &\n                                (df_summary['z_level'] == z) & (df_summary['method'] == 'global_corrected')]\n                if len(hb) > 0 and len(gc) > 0:\n                    hb_b = hb.iloc[0]['mean_abs_bias']\n                    gc_b = gc.iloc[0]['mean_abs_bias']\n                    red = (gc_b - hb_b) / gc_b * 100 if gc_b > 0 else 0\n                    lines.append(f\"| {ne} | {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n    lines.append(\"\")\n\n    lines.append(\"### Coverage (95% CI)\\n\")\n    lines.append(\"| n_expert | Method | Mean Coverage |\")\n    lines.append(\"|----------|--------|---------------|\")\n    for ne in N_EXPERTS:\n        for m in ['oracle', 'naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['mean_coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    lines.append(\"## Comparison with exp-015 (GPT-4.1 CM)\\n\")\n    lines.append(\"### Overall RMSE by method and n_expert\\n\")\n    lines.append(\"| n_expert | Method | exp-016 (gpt-3.5-turbo) | exp-015 (GPT-4.1) |\")\n    lines.append(\"|----------|--------|-------------------------|---------------------|\")\n\n    exp015_rmse = {\n        100: {'naive': 0.1230, 'global_corrected': 0.2631, 'hb_ec_hte': 0.7842},\n        250: {'naive': 0.1230, 'global_corrected': 0.2318, 'hb_ec_hte': 0.4113},\n        500: {'naive': 0.1230, 'global_corrected': 0.1963, 'hb_ec_hte': 0.2599},\n    }\n    exp015_cov = {\n        100: {'naive': 0.879, 'global_corrected': 0.885, 'hb_ec_hte': 0.744},\n        250: {'naive': 0.879, 'global_corrected': 0.909, 'hb_ec_hte': 0.834},\n        500: {'naive': 0.879, 'global_corrected': 0.922, 'hb_ec_hte': 0.890},\n    }\n\n    for ne in N_EXPERTS:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                rmse_016 = sub['mean_rmse'].mean()\n                rmse_015 = exp015_rmse[ne][m]\n                lines.append(f\"| {ne} | {m} | {rmse_016:.4f} | {rmse_015:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Overall Coverage by method and n_expert\\n\")\n    lines.append(\"| n_expert | Method | exp-016 (gpt-3.5-turbo) | exp-015 (GPT-4.1) |\")\n    lines.append(\"|----------|--------|-------------------------|---------------------|\")\n    for ne in N_EXPERTS:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                cov_016 = sub['mean_coverage'].mean()\n                cov_015 = exp015_cov[ne][m]\n                lines.append(f\"| {ne} | {m} | {cov_016:.3f} | {cov_015:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(\"## Conclusion\\n\")\n    for ne in N_EXPERTS:\n        hb_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        gc_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'global_corrected')]\n        nv_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        if len(hb_all) > 0 and len(gc_all) > 0:\n            hb_rmse = hb_all['mean_rmse'].mean()\n            gc_rmse = gc_all['mean_rmse'].mean()\n            nv_rmse = nv_all['mean_rmse'].mean()\n            hb_cov = hb_all['mean_coverage'].mean()\n            gc_cov = gc_all['mean_coverage'].mean()\n            nv_cov = nv_all['mean_coverage'].mean()\n            lines.append(f\"- n_expert={ne}: HB RMSE={hb_rmse:.4f} (cov={hb_cov:.3f}), \"\n                         f\"Global RMSE={gc_rmse:.4f} (cov={gc_cov:.3f}), \"\n                         f\"Naive RMSE={nv_rmse:.4f} (cov={nv_cov:.3f})\")\n\n    report = \"\\n\".join(lines)\n    with open('results/exp016_semi_real_analysis.md', 'w') as f:\n        f.write(report)\n    print(\"Wrote results/exp016_semi_real_analysis.md\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    args = parser.parse_args()\n    n_mc = args.n_mc\n\n    print(f\"exp-016: Semi-Real CM with Better Model (gpt-3.5-turbo)\")\n    print(f\"N={N}, n_mc={n_mc}, n_experts={N_EXPERTS}\")\n    print(f\"Subgroup CMs (real asymmetric from gpt-3.5-turbo pilot):\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print(f\"Methods: oracle, naive, global_corrected, hb_ec_hte\")\n    print()\n\n    results = []\n    configs = [(ne, mc) for ne in N_EXPERTS for mc in range(n_mc)]\n    total = len(configs)\n    t0 = time.time()\n\n    for count, (ne, mc) in enumerate(configs, 1):\n        seed = SEED_BASE + mc\n        data = generate_data(ne, seed)\n        mc_rows = run_one_mc(data, ne, seed)\n        results.extend(mc_rows)\n        if count % max(1, total // 20) == 0:\n            elapsed = time.time() - t0\n            eta = elapsed / count * (total - count)\n            print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | ne={ne} seed={seed}\")\n\n    elapsed = time.time() - t0\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_raw['abs_bias'] = df_raw['bias'].abs()\n    df_raw['squared_error'] = df_raw['bias'] ** 2\n\n    df_summary = aggregate_results(df_raw)\n\n    df_raw.to_csv('results/exp016_semi_real_raw.csv', index=False)\n    print(f\"Saved results/exp016_semi_real_raw.csv ({len(df_raw)} rows)\")\n\n    write_analysis(df_summary)\n\n    print(\"\\n=== Key Metrics Summary ===\\n\")\n    pd.set_option('display.float_format', '{:.4f}'.format)\n    pd.set_option('display.width', 200)\n    for ne in N_EXPERTS:\n        print(f\"--- n_expert = {ne} ---\")\n        sub = df_summary[df_summary['n_expert'] == ne]\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            ms = sub[sub['method'] == m]\n            print(f\"  {m:20s}: mean_abs_bias={ms['mean_abs_bias'].mean():.4f}, \"\n                  f\"rmse={ms['mean_rmse'].mean():.4f}, coverage={ms['mean_coverage'].mean():.3f}\")\n        print()\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T13:28:50.536126+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T13:28:50.536287+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 exp016_semi_real_better_cm.py --n-mc 10 2>&1",
  "description": "Dry-run exp-016 with 10 seeds",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 exp016_semi_real_better_cm.py --n-mc 10 2>&1",
    "description": "Dry-run exp-016 with 10 seeds",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T13:28:50.536442+00:00_

exp-016: Semi-Real CM with Better Model (gpt-3.5-turbo)
N=5000, n_mc=10, n_experts=[100, 250, 500]
Subgroup CMs (real asymmetric from gpt-3.5-turbo pilot):
  S0: FPR=0.143, FNR=0.211
  S1: FPR=0.180, FNR=0.150
  S2: FPR=0.393, FNR=0.154
  S3: FPR=0.378, FNR=0.148
Methods: oracle, naive, global_corrected, hb_ec_hte

  [1/30] 1s elapsed, ETA 26s | ne=100 seed=0
  [2/30] 2s elapsed, ETA 25s | ne=100 seed=1
  [3/30] 3s elapsed, ETA 24s | ne=100 seed=2
  [4/30] 4s elapsed, ETA 23s | ne=100 seed=3
  [5/30] 4s elapsed, ETA 22s | ne=100 seed=4
  [6/30] 5s elapsed, ETA 22s | ne=100 seed=5
  [7/30] 6s elapsed, ETA 21s | ne=100 seed=6
  [8/30] 7s elapsed, ETA 20s | ne=100 seed=7
  [9/30] 8s elapsed, ETA 19s | ne=100 seed=8
  [10/30] 9s elapsed, ETA 18s | ne=100 seed=9
  [11/30] 10s elapsed, ETA 17s | ne=250 seed=0
  [12/30] 11s elapsed, ETA 16s | ne=250 seed=1
  [13/30] 12s elapsed, ETA 15s | ne=250 seed=2
  [14/30] 13s elapsed, ETA 14s | ne=250 seed=3
  [15/30] 14s elapsed, ETA 14s | ne=250 seed=4
  [16/30] 15s elapsed, ETA 13s | ne=250 seed=5
  [17/30] 16s elapsed, ETA 12s | ne=250 seed=6
  [18/30] 16s elapsed, ETA 11s | ne=250 seed=7
  [19/30] 17s elapsed, ETA 10s | ne=250 seed=8
  [20/30] 18s elapsed, ETA 9s | ne=250 seed=9
  [21/30] 19s elapsed, ETA 8s | ne=500 seed=0
  [22/30] 20s elapsed, ETA 7s | ne=500 seed=1
  [23/30] 21s elapsed, ETA 6s | ne=500 seed=2
  [24/30] 22s elapsed, ETA 5s | ne=500 seed=3
  [25/30] 23s elapsed, ETA 5s | ne=500 seed=4
  [26/30] 23s elapsed, ETA 4s | ne=500 seed=5
  [27/30] 24s elapsed, ETA 3s | ne=500 seed=6
  [28/30] 25s elapsed, ETA 2s | ne=500 seed=7
  [29/30] 26s elapsed, ETA 1s | ne=500 seed=8
  [30/30] 27s elapsed, ETA 0s | ne=500 seed=9

Total time: 27.0s
Saved results/exp016_semi_real_raw.csv (960 rows)
Wrote results/exp016_semi_real_analysis.md

=== Key Metrics Summary ===

--- n_expert = 100 ---
  naive               : mean_abs_bias=0.1058, rmse=0.1196, coverage=0.863
  global_corrected    : mean_abs_bias=0.1665, rmse=0.2081, cover
…[truncated 575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T13:28:50.536620+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 exp016_semi_real_better_cm.py --n-mc 100 2>&1",
  "description": "Run full exp-016 with 100 MC seeds",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 exp016_semi_real_better_cm.py --n-mc 100 2>&1",
    "description": "Run full exp-016 with 100 MC seeds",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T13:28:50.536770+00:00_

exp-016: Semi-Real CM with Better Model (gpt-3.5-turbo)
N=5000, n_mc=100, n_experts=[100, 250, 500]
Subgroup CMs (real asymmetric from gpt-3.5-turbo pilot):
  S0: FPR=0.143, FNR=0.211
  S1: FPR=0.180, FNR=0.150
  S2: FPR=0.393, FNR=0.154
  S3: FPR=0.378, FNR=0.148
Methods: oracle, naive, global_corrected, hb_ec_hte

  [15/300] 14s elapsed, ETA 274s | ne=100 seed=14
  [30/300] 28s elapsed, ETA 254s | ne=100 seed=29
  [45/300] 42s elapsed, ETA 238s | ne=100 seed=44
  [60/300] 58s elapsed, ETA 232s | ne=100 seed=59
  [75/300] 73s elapsed, ETA 220s | ne=100 seed=74
  [90/300] 89s elapsed, ETA 207s | ne=100 seed=89
  [105/300] 104s elapsed, ETA 193s | ne=250 seed=4
  [120/300] 118s elapsed, ETA 176s | ne=250 seed=19
  [135/300] 132s elapsed, ETA 161s | ne=250 seed=34
  [150/300] 146s elapsed, ETA 146s | ne=250 seed=49
  [165/300] 160s elapsed, ETA 131s | ne=250 seed=64
  [180/300] 174s elapsed, ETA 116s | ne=250 seed=79
  [195/300] 189s elapsed, ETA 102s | ne=250 seed=94
  [210/300] 206s elapsed, ETA 88s | ne=500 seed=9
  [225/300] 219s elapsed, ETA 73s | ne=500 seed=24
  [240/300] 233s elapsed, ETA 58s | ne=500 seed=39
  [255/300] 246s elapsed, ETA 43s | ne=500 seed=54
  [270/300] 260s elapsed, ETA 29s | ne=500 seed=69
  [285/300] 274s elapsed, ETA 14s | ne=500 seed=84
  [300/300] 287s elapsed, ETA 0s | ne=500 seed=99

Total time: 287.0s
Saved results/exp016_semi_real_raw.csv (9600 rows)
Wrote results/exp016_semi_real_analysis.md

=== Key Metrics Summary ===

--- n_expert = 100 ---
  naive               : mean_abs_bias=0.1100, rmse=0.1274, coverage=0.784
  global_corrected    : mean_abs_bias=0.2093, rmse=0.2652, coverage=0.893
  hb_ec_hte           : mean_abs_bias=0.5240, rmse=0.9295, coverage=0.769

--- n_expert = 250 ---
  naive               : mean_abs_bias=0.1100, rmse=0.1274, coverage=0.784
  global_corrected    : mean_abs_bias=0.1735, rmse=0.2210, coverage=0.922
  hb_ec_hte           : mean_abs_bias=0.3387, rmse=0.5267, coverage=0.843

--- n_expert = 500 ---
  nai
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T13:28:50.537002+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l results/exp016_semi_real_raw.csv",
  "description": "Verify CSV row count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l results/exp016_semi_real_raw.csv",
    "description": "Verify CSV row count"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T13:28:50.537136+00:00_

9601 results/exp016_semi_real_raw.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T13:28:50.537254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp016_semi_real_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp016_semi_real_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T13:28:50.537429+00:00_

1	# exp-016: Semi-Real CM with Better Model
2	
3	## Model Selection
4	
5	Selected **gpt-3.5-turbo** from exp-008 pilot data (lowest worst-subgroup FNR).
6	
7	| Model | Worst-subgroup FNR | Meets threshold (<0.4) |
8	|-------|-------------------|------------------------|
9	| gpt-3.5-turbo | 0.211 | Yes |
10	| gpt-4o-mini | 0.421 | No |
11	| gpt-4.1 (exp-015) | 0.526 | No |
12	| gpt-4-turbo | 0.550 | No |
13	| gpt-4o | 0.579 | No |
14	
15	gpt-3.5-turbo trades higher FPR for much lower FNR (more aggressive positive predictions).
16	
17	## Design
18	
19	| Subgroup | Name | Weight | FPR | FNR | exp-015 FPR | exp-015 FNR |
20	|----------|------|--------|-----|-----|-------------|-------------|
21	| S0 | False_medium | 0.38 | 0.143 | 0.211 | 0.054 | 0.526 |
22	| S1 | False_short | 0.22 | 0.180 | 0.150 | 0.101 | 0.300 |
23	| S2 | True_short | 0.14 | 0.393 | 0.154 | 0.143 | 0.308 |
24	| S3 | True_medium | 0.25 | 0.378 | 0.148 | 0.194 | 0.222 |
25	
26	**True CATE**: tau(z=0,s) = 0.3 + 0.1*s_idx; tau(z=1,s) = 0.8 - 0.15*s_idx
27	
28	| Subgroup | tau(z=0) | tau(z=1) |
29	|----------|----------|----------|
30	| S0 | 0.30 | 0.80 |
31	| S1 | 0.40 | 0.65 |
32	| S2 | 0.50 | 0.50 |
33	| S3 | 0.60 | 0.35 |
34	
35	N=5000, P(Z=1)=0.18, P(T=1)=0.5, n_expert in {100, 250, 500}, 100 MC seeds.
36	
37	## Summary Tables
38	
39	### n_expert = 100
40	
41	| Subgroup | Z | Method | Mean Bias | Mean |Bias| | RMSE | Coverage |
42	|----------|---|--------|-----------|-------------|------|----------|
43	| S0 | 0 | global_corrected | -0.0015 | 0.0590 | 0.0733 | 0.930 |
44	| S0 | 0 | hb_ec_hte | +0.0002 | 0.0829 | 0.1120 | 0.830 |
45	| S0 | 0 | naive | +0.0356 | 0.0487 | 0.0629 | 0.890 |
46	| S0 | 0 | oracle | +0.0073 | 0.0394 | 0.0491 | 0.950 |
47	| S0 | 1 | global_corrected | +0.1888 | 0.3301 | 0.4252 | 0.830 |
48	| S0 | 1 | hb_ec_hte | +0.1731 | 0.4570 | 0.7663 | 0.710 |
49	| S0 | 1 | naive | -0.2248 | 0.2248 | 0.2423 | 0.350 |
50	| S0 | 1 | oracle | +0.0101 | 0.0901 | 0.1088 | 0.960 |
51	| S1 | 0 |
…[truncated 9310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T13:28:50.537624+00:00_

All outputs verified:
- CSV: 9601 lines (9600 data + 1 header) = 100 × 3 × 4 × 2 × 4 = 9600 rows
- Analysis MD written

## Results Summary

**Model selected**: gpt-3.5-turbo (worst-subgroup FNR=0.211). Higher FPR (0.14–0.39) than GPT-4.1 (0.05–0.19) but much lower FNR (0.15–0.21 vs 0.22–0.53).

**Key findings — despite lower FNR, results are worse than exp-015**:

| n_expert | Method | exp-016 RMSE | exp-015 RMSE | exp-016 Cov | exp-015 Cov |
|---|---|---|---|---|---|
| 100 | naive | 0.1274 | 0.1230 | 0.784 | 0.879 |
| 100 | global_corrected | 0.2652 | 0.2631 | 0.893 | 0.885 |
| 100 | hb_ec_hte | **0.9295** | **0.7842** | 0.769 | 0.744 |
| 500 | global_corrected | 0.1991 | 0.1963 | 0.939 | 0.922 |
| 500 | hb_ec_hte | **0.3222** | **0.2599** | 0.894 | 0.890 |

- **HB EC-HTE is consistently worse than global_corrected** at all n_expert levels (same pattern as exp-015)
- **Naive coverage drops** to 0.784 (from 0.879 in exp-015), because higher FPR creates more misclassification bias in the z=1 stratum despite lower FNR
- **Global corrected outperforms HB** because the higher FPR variation across subgroups (0.14–0.39) makes subgroup-level CM estimation harder with limited expert data — the HB sampler struggles more with this asymmetry
- **Bright spot for HB**: at n_expert=500, S0/z=1, HB actually beats global (|bias| 0.19 vs 0.25) — the one case where subgroup-specific correction helps

The experiment confirms that lower FNR alone doesn't help; the higher FPR variance across subgroups makes the correction problem harder overall.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp-016-semi-real-better-cm_20260521T132011"
}
```

</details>

---
