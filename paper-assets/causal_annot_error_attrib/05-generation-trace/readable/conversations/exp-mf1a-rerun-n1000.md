# exp mf1a rerun n1000

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_exp_mf1a_rerun_n1000_20260523T175940.jsonl`
- **Structured JSON:** [`20e8e22ea99b5e5c3d37.json`](../../sessions/20/20e8e22ea99b5e5c3d37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-23T18:02:45.102230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T18:02:45.102573+00:00_

1	#!/usr/bin/env python3
2	"""
3	MF-1a: Adversarial Monotonicity Test for Conjecture 1.
4	
5	Verifies ε-approximate envelope monotonicity of |B(C(δ))| along
6	C(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.
7	
8	Grid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀
9	"""
10	
11	import json
12	import os
13	import sys
14	import time
15	import numpy as np
16	
17	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
18	from exp_d_conjecture_verify_v2 import (
19	    ALL_TOPOS, NON_DECREASING, NON_INCREASING,
20	    _COMPUTE_SS, make_all_params, get_tau_true,
21	    compute_bias_curve,
22	)
23	
24	K_VALUES = [3, 5, 7]
25	N_DELTA = 101
26	DELTA_STEP = 0.01
27	N_C0 = 100
28	SEED = 2024
29	EPS_THRESHOLD = 0.001
30	
31	BETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']
32	ADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']
33	ADV_PARAMS = {
34	    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],
35	    'block_diag': [{}],
36	    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],
37	    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],
38	}
39	
40	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
41	
42	
43	def make_beta_vec(name, K):
44	    pools = {
45	        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],
46	        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],
47	        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],
48	    }
49	    return np.array(pools[name][:K])
50	
51	
52	def make_params_with_beta(K, beta_name):
53	    params = make_all_params(K)
54	    bv = make_beta_vec(beta_name, K)
55	    params['exposure']['beta'] = bv.copy()
56	    params['iv']['beta'] = bv.copy()
57	    params['mediation']['beta'] = bv.copy()
58	    params['frontdoor']['beta'] = bv.copy()
59	    params['confounding']['beta_A'] = bv[1:].copy()
60	    params['collider']['dY'] = bv.copy()
61	    params['mbias']['a1'] = bv.copy()
62	    r
…[truncated 10895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T18:02:45.102744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T18:02:45.102971+00:00_

1	{
2	  "description": "Adversarial envelope monotonicity test for Conjecture 1",
3	  "config": {
4	    "K_values": [
5	      3,
6	      5,
7	      7
8	    ],
9	    "adversarial_types": [
10	      "near_perm",
11	      "block_diag",
12	      "sparse",
13	      "near_uniform"
14	    ],
15	    "adversarial_params": {
16	      "near_perm": [
17	        {
18	          "eps": 0.05
19	        },
20	        {
21	          "eps": 0.1
22	        },
23	        {
24	          "eps": 0.2
25	        }
26	      ],
27	      "block_diag": [
28	        {}
29	      ],
30	      "sparse": [
31	        {
32	          "p_diag": 0.3
33	        },
34	        {
35	          "p_diag": 0.5
36	        },
37	        {
38	          "p_diag": 0.7
39	        }
40	      ],
41	      "near_uniform": [
42	        {
43	          "eps": 0.01
44	        },
45	        {
46	          "eps": 0.05
47	        }
48	      ]
49	    },
50	    "topologies": [
51	      "confounding",
52	      "mediation",
53	      "collider",
54	      "exposure",
55	      "mbias",
56	      "iv",
57	      "frontdoor"
58	    ],
59	    "beta_configs": [
60	      "alternating_large",
61	      "same_sign",
62	      "alternating_small"
63	    ],
64	    "n_C0_per_cell": 100,
65	    "n_delta_steps": 101,
66	    "delta_step": 0.01,
67	    "eps_threshold": 0.001,
68	    "seed": 2024
69	  },
70	  "summary": {
71	    "total_curves": 54611,
72	    "non_monotone_fraction": 0.11933493252275183,
73	    "max_eps_abs": 0.01636529529573094,
74	    "median_eps_abs": 0.0,
75	    "mean_eps_abs": 0.00047372456391479953,
76	    "p95_eps_abs": 0.002532176988620627,
77	    "p99_eps_abs": 0.008253228263722434,
78	    "safe_topo_max_eps": 0.01636529529573094,
79	    "fragile_topo_max_eps": 0.013176775652375183,
80	    "total_weak_iv_filtered": 2089,
81	    "total_skipped_zero_tau": 0
82	  },
83	  "by_adversarial_type": {
84	    "near_perm": {
85	      "total_curves": 17279,
86	      "non_monotone_count": 6096,
87	      "non_monotone_fraction": 0.3527981943399
…[truncated 9113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T18:02:45.103144+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
  "old_string": "N_C0 = 100",
  "new_string": "N_C0 = 1000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
    "old_string": "N_C0 = 100",
    "new_string": "N_C0 = 1000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T18:02:45.103326+00:00_

The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T18:02:45.103442+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py",
  "description": "Run adversarial monotonicity test with N_C0=1000",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py",
    "description": "Run adversarial monotonicity test with N_C0=1000",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T18:02:45.103582+00:00_

==============================================================================
MF-1a: Adversarial Monotonicity Test
  K=[3, 5, 7]  β=['alternating_large', 'same_sign', 'alternating_small']
  Adversarial: ['near_perm', 'block_diag', 'sparse', 'near_uniform']
  N_C0=1000  δ steps=101  ε threshold=0.001
==============================================================================
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py:682: RuntimeWarning: divide by zero encountered in divide
  taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
  [  63/567] K=3 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/1000  (14.3s)
  [ 126/567] K=3 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/1000  (27.0s)
  [ 189/567] K=3 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/1000  (40.0s)
  [ 252/567] K=5 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/1000  (55.0s)
  [ 315/567] K=5 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/1000  (69.2s)
  [ 378/567] K=5 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/1000  (83.1s)
  [ 441/567] K=7 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/1000  (100.4s)
  [ 504/567] K=7 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/1000  (118.4s)
  [ 567/567] K=7 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/1000  (135.7s)

JSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json

============================================================
Total curves: 545,945  Non-monotone: 65182 (11.939%)
Max ε_abs: 0.016365  Median: 0.000000
Safe max ε: 0.016365  Fragile max ε: 0.013177
Weak-IV filtered: 21055

By topology:
  confounding    [non-dec]  n= 81000  nm=17407  (21.49%)  max_ε=0.016365
  mediation      [non-dec]  n= 81
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T18:02:45.103733+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T18:02:45.103845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T18:02:45.103952+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "adversarial_monotonicity_results_N1000",
  "type": "data",
  "description": "MF-1a Adversarial Monotonicity Test results with N_C0=1000 (10x previous). 545,945 curves tested, max ε=0.0164, non-monotone fraction 11.94%.",
  "project": "causal_annot_error_attrib",
  "source_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json",
  "tags": "['MF-1a', 'monotonicity', 'conjecture1', 'adversarial']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "adversarial_monotonicity_results_N1000",
    "type": "data",
    "description": "MF-1a Adversarial Monotonicity Test results with N_C0=1000 (10x previous). 545,945 curves tested, max ε=0.0164, non-monotone fraction 11.94%.",
    "project": "causal_annot_error_attrib",
    "source_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json",
    "tags": "['MF-1a', 'monotonicity', 'conjecture1', 'adversarial']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T18:02:45.104084+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_b60bb1\", \"name\": \"adversarial_monotonicity_results_N1000\", \"type\": \"data\", \"description\": \"MF-1a Adversarial Monotonicity Test results with N_C0=1000 (10x previous). 545,945 curves tested, max ε=0.0164, non-monotone fraction 11.94%.\", \"path\": \"projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results_b60bb1.json\", \"url\": null, \"project\": \"causal_annot_error_attrib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T18:02:35.685975+00:00\", \"tags\": [\"MF-1a\", \"monotonicity\", \"conjecture1\", \"adversarial\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T18:02:45.104245+00:00_

N=1000 重跑完成（135.8s）。核心数字对比：

| 指标 | N=100 | N=1000 | 变化 |
|------|-------|--------|------|
| total_curves | 54,611 | 545,945 | ×10 |
| non_monotone_fraction | 11.93% | 11.94% | 稳定 |
| max_eps_abs | 0.01637 | 0.01637 | 不变 |
| median_eps_abs | 0.0 | 0.0 | 不变 |
| mean_eps_abs | 0.000474 | — | — |
| p95_eps_abs | 0.00253 | — | — |
| p99_eps_abs | 0.00825 | — | — |
| safe_topo_max_eps | 0.01637 | 0.01637 | 不变 |
| fragile_topo_max_eps | 0.01318 | 0.01318 | 不变 |
| weak_iv_filtered | 2,089 | 21,055 | ×10 |

结论：10 倍采样量下所有关键指标高度稳定，max ε bound 未被突破，non-monotone fraction 收敛于 ~11.9%，bound 可信度得到增强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_exp_mf1a_rerun_n1000_20260523T175940"
}
```

</details>

---
