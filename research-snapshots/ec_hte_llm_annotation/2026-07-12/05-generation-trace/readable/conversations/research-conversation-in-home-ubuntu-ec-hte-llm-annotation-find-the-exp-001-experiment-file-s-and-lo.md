# Research conversation: In /home/ubuntu/ec_hte_llm_annotation, find the exp-001 experiment file(s) and locate these helper functions: 1. `build_

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2eeebeae4ff9ddd4.jsonl`
- **Structured JSON:** [`1946a222bda7263e8898.json`](../../sessions/19/1946a222bda7263e8898.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-21T01:32:25.836Z_

In /home/ubuntu/ec_hte_llm_annotation, find the exp-001 experiment file(s) and locate these helper functions:
1. `build_mixing_matrix`
2. `invert_mixing_safe`
3. `compute_confusion_matrix` (or similar)
4. Any DGP / `generate_data` function

For each, return the full function source code and file path with line numbers. Also check if there's a `results/` directory already.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "20575606-c86a-423d-a817-151a8d892c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T01:32:27.464Z_

I'll help you find these helper functions and check for the results directory. Let me start by exploring the directory structure and searching for the exp-001 experiment file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20575606-c86a-423d-a817-151a8d892c56",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMAnfhECQkLXQfWjSU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05d31021-dbef-4a7c-b6ca-a0e704ecdbc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01299pdzGPtAP3UY5R8NsQ4r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35701,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35701,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T01:32:28.435Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VD8WPHYCj8gu58XF8XZcR8`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*exp*001*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05d31021-dbef-4a7c-b6ca-a0e704ecdbc4",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMAnfhECQkLXQfWjSU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d9639a7-0ed8-4f6d-aa9c-4bff91c1a563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01299pdzGPtAP3UY5R8NsQ4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35701,
      "cache_read_input_tokens": 0,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35701
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 122,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35701,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T01:32:29.217Z_

<details><summary>↩ Tool result · `toolu_01VD8WPHYCj8gu58XF8XZcR8`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/__pycache__/exp001_hb_synthetic.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/results/exp001_reg_run.log
/home/ubuntu/ec_hte_llm_annotation/results/exp001_hb_results.csv
/home/ubuntu/ec_hte_llm_annotation/results/exp001_full_run.log
/home/ubuntu/ec_hte_llm_annotation/results/exp001_hb_results_v2.csv
/home/ubuntu/ec_hte_llm_annotation/results/exp001_hyperprior_run.log
/home/ubuntu/ec_hte_llm_annotation/results/exp001_hyperprior_sensitivity.csv
/home/ubuntu/ec_hte_llm_annotation/results/exp001_reg_v2_run.log
/home/ubuntu/ec_hte_llm_annotation/results/exp001_hb_diagnostics.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d9639a7-0ed8-4f6d-aa9c-4bff91c1a563",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "2985ec84-b356-4125-9e2d-06a243d30412",
  "sourceToolAssistantUUID": "0d9639a7-0ed8-4f6d-aa9c-4bff91c1a563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T01:32:31.424Z_

Great! I found several exp001 files and a results directory. Now let me search for the specific helper functions in these experiment files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2985ec84-b356-4125-9e2d-06a243d30412",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMQcNJdRQe4YyXhMz9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d7e85d0-61ab-4194-80e3-3efbf1d52658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ABZYtiMsUC7gW1Cqt5z1C6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1299,
      "cache_read_input_tokens": 35701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1299,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T01:32:32.270Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XQmt6ivPLwC9XV9urpCm4y`</summary>

```json
{
  "pattern": "def (build_mixing_matrix|invert_mixing_safe|compute_confusion_matrix|generate_data|DGP)",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d7e85d0-61ab-4194-80e3-3efbf1d52658",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMQcNJdRQe4YyXhMz9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17b3e2f0-5cbc-4f1f-b53b-900de5cef21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ABZYtiMsUC7gW1Cqt5z1C6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1299,
      "cache_read_input_tokens": 35701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1299,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T01:32:32.452Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WfYTikvJRKJTK16dLv5J8e`</summary>

```json
{
  "command": "ls -ld /home/ubuntu/ec_hte_llm_annotation/results 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b3e2f0-5cbc-4f1f-b53b-900de5cef21d",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMQcNJdRQe4YyXhMz9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d55b783-2fc2-4ebf-b29e-1bc90064331f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ABZYtiMsUC7gW1Cqt5z1C6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1299,
      "cache_read_input_tokens": 35701,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 221,
          "cache_read_input_tokens": 35701,
          "cache_creation_input_tokens": 1299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1299,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T01:32:32.777Z_

<details><summary>↩ Tool result · `toolu_01WfYTikvJRKJTK16dLv5J8e`</summary>

```text
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 00:53 /home/ubuntu/ec_hte_llm_annotation/results
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d55b783-2fc2-4ebf-b29e-1bc90064331f",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "bf1c7ef4-10c3-40c9-b9a9-768bfbc1f3eb",
  "sourceToolAssistantUUID": "0d55b783-2fc2-4ebf-b29e-1bc90064331f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T01:32:33.154Z_

<details><summary>↩ Tool result · `toolu_01XQmt6ivPLwC9XV9urpCm4y`</summary>

```text
Found 7 files
exp006_budget_sensitivity.py
exp003_tweeteval.py
exp001_hb_synthetic.py
exp007_ppci_dsl.py
mvp_simulation.py
.venv/lib/python3.14/site-packages/sklearn/tests/test_discriminant_analysis.py
.venv/lib/python3.14/site-packages/sklearn/mixture/tests/test_gaussian_mixture.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17b3e2f0-5cbc-4f1f-b53b-900de5cef21d",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "de50d21a-3e9e-43f3-97b4-33d0e3c18985",
  "sourceToolAssistantUUID": "17b3e2f0-5cbc-4f1f-b53b-900de5cef21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T01:32:34.399Z_

Good! The results directory exists. Now let me read the main exp001 file to find all those helper functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de50d21a-3e9e-43f3-97b4-33d0e3c18985",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMhQAeakvmK1J6qQio",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "195434d5-b1dc-4cbc-9f4a-b37cb822f70f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018QUpNEULJcbag7H5kpNv6A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 72,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 37000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 365,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T01:32:34.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FZjt2U73QfngLhMaG83Qjn`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "195434d5-b1dc-4cbc-9f4a-b37cb822f70f",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMhQAeakvmK1J6qQio",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "083afed6-494a-49d8-a8f2-c99bbdac9880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018QUpNEULJcbag7H5kpNv6A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 72,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 37000,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 72,
          "output_tokens": 101,
          "cache_read_input_tokens": 37000,
          "cache_creation_input_tokens": 365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 365,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T01:32:34.987Z_

<details><summary>↩ Tool result · `toolu_01FZjt2U73QfngLhMaG83Qjn`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	
211	
212	def _split_rhat(chains):
213	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
214	    parts = []
215	    for c in range(chains.shape[0]):
216	        half = chains.shape[1] // 2
217	        parts.append(chains[c, :half])
218	        parts.append(chains[c, half:2 * half])
219	    parts = np.array(parts)
220	    m = parts.shape[0]
221	    n = parts.shape[1]
222	    chain_means = parts.mean(axis=1)
223	    W = np.mean(np.var(parts, axis=1, ddof=1))
224	    B = n * np.var(chain_means, ddof=1)
225	    if W < 1e-20:
226	        return 1.0
227	    var_hat = (1 - 1.0 / n) * W + B / n
228	    return float(np.sqrt(var_hat / W))
229	
230	
231	def _bulk_ess(chains):
232	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
233	    x = chains.ravel()
234	    n = len(x)
235	    mu = x.mean()
236	    xc = x - mu
237	    max_lag = min(n // 2, 300)
238	    c0 = np.dot(xc, xc)
239	    if c0 < 1e-20:
240	        return float(n)
241	    tau = 1.0
242	    for lag in range(1, max_lag - 1, 2):
243	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
244	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
245	        pair = r1 + r2
246	        if pair < 0:
247	            break
248	        tau += 2 * pair
249	    return float(n / tau)
250	
251	
252	def _fast_diagnostics(alpha_arr, theta_arr, labels):
253	    """Compute R-hat and ESS over all parameters without arviz."""
254	    rhats, esss = [], []
255	    for d in range(alpha_arr.shape[2]):
256	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
257	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
258	    k = len(labels)
259	    for i in range(k):
260	        for z in [0, 1]:
261	            for zh in range(theta_arr.shape[4]):
262	                ch = theta_arr[:, :, i, z, zh]
263	                rhats.append(_split_rhat(ch))
264	                esss.append(_bulk_ess(ch))
265	    return max(rhats), min(esss)
266	
267	
268	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
269	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
270	    if alpha < 1e-10:
271	        return -1e10
272	    a = alpha / 2.0
273	    k = theta_z.shape[0]
274	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
275	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
276	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
277	    return lp
278	
279	
280	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
281	                         hp_a0=3.0, hp_b0=1.0):
282	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).
283	
284	    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).
285	    """
286	    k = len(labels)
287	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
288	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
289	    chain_inits = chain_inits_pool[:n_chains]
290	    all_alpha, all_theta = [], []
291	    t0 = time.time()
292	
293	    for chain in range(n_chains):
294	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
295	        alpha = chain_inits[chain].copy()
296	        theta = np.ones((k, 2, 2)) * 0.5
297	        mh_scale = np.array([0.3, 0.3])
298	        accept_ct = np.array([0, 0])
299	        attempt_ct = np.array([0, 0])
300	
301	        alpha_samples = np.zeros((n_iter, 2))
302	        theta_samples = np.zeros((n_iter, k, 2, 2))
303	
304	        for it in range(n_warmup + n_iter):
305	            for z in [0, 1]:
306	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
307	                post_a = np.maximum(post_a, 1e-6)
308	                g = rng.gamma(post_a)
309	                g_sum = g.sum(axis=1, keepdims=True)
310	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
311	
312	            for z in [0, 1]:
313	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
314	                a_prop = np.exp(x_prop)
315	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
316	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
317	                accepted = np.log(rng.rand()) < log_r
318	                if accepted:
319	                    alpha[z] = a_prop
320	                if it < n_warmup:
321	                    accept_ct[z] += int(accepted)
322	                    attempt_ct[z] += 1
323	
324	            if it < n_warmup and it > 0 and it % 100 == 0:
325	                for z in [0, 1]:
326	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
327	                    if rate < 0.2:
328	                        mh_scale[z] *= 0.7
329	                    elif rate > 0.5:
330	                        mh_scale[z] *= 1.3
331	                    accept_ct[z] = 0
332	                    attempt_ct[z] = 0
333	
334	            if it >= n_warmup:
335	                idx = it - n_warmup
336	                alpha_samples[idx] = alpha.copy()
337	                theta_samples[idx] = theta.copy()
338	
339	        all_alpha.append(alpha_samples)
340	        all_theta.append(theta_samples)
341	
342	    runtime = time.time() - t0
343	    alpha_arr = np.stack(all_alpha)
344	    theta_arr = np.stack(all_theta)
345	
346	    C = {}
347	    for i, s in enumerate(labels):
348	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
349	
350	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
351	
352	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
353	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
354	    return C, diag
355	
356	
357	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
358	    """Full Bayesian HB with PyMC MCMC."""
359	    k = len(labels)
360	    n_per_sz = counts.sum(axis=2)
361	
362	    with pm.Model():
363	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
364	        for z in [0, 1]:
365	            for i, s in enumerate(labels):
366	                nsz = int(n_per_sz[i, z])
367	                if nsz == 0:
368	                    continue
369	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
370	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
371	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
372	                               observed=counts[i, z, :].astype('int32'))
373	        t0 = time.time()
374	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
375	                          random_seed=seed, progressbar=False)
376	        runtime = time.time() - t0
377	
378	    C = {}
379	    for i, s in enumerate(labels):
380	        C_s = np.zeros((2, 2))
381	        for z in [0, 1]:
382	            vn = f'theta_{s}_z{z}'
383	            if vn in trace.posterior:
384	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
385	            else:
386	                C_s[z, :] = 0.5
387	        C[s] = C_s
388	
389	    all_vars = list(trace.posterior.data_vars)
390	    try:
391	        summ = az.summary(trace, var_names=all_vars)
392	        rhat_max = float(summ['r_hat'].max())
393	        ess_min = float(summ['ess_bulk'].min())
394	    except Exception:
395	        rhat_max = ess_min = np.nan
396	    try:
397	        divergent = int(trace.sample_stats['diverging'].values.sum())
398	    except Exception:
399	        divergent = -1
400	
401	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
402	            'divergent_count': divergent, 'runtime_seconds': runtime,
403	            'hb_method': 'mcmc'}
404	    return C, diag
405	
406	
407	# ── Single MC Run ─────────────────────────────────────────────────────────────
408	
409	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
410	    data = generate_data(regime_params, n_expert, k, seed)
411	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
412	    em = data['expert_mask']
413	    labels = SUBGROUP_LABELS[k]
414	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
415	
416	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
417	
418	    C_mle = estimate_cm_mle(counts, labels)
419	
420	    if hb_method == 'gibbs':
421	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
422	    elif hb_method == 'mcmc' and HAS_PYMC:
423	        try:
424	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
425	        except Exception:
426	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
427	            hb_diag['hb_method'] = 'eb_fallback'
428	    else:
429	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
430	
431	    # Global CM (pool all expert labels, Laplace)
432	    cg = counts.sum(axis=0)
433	    C_gl = np.zeros((2, 2))
434	    for z in [0, 1]:
435	        n = cg[z, :].sum()
436	        for zh in [0, 1]:
437	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
438	
439	    M_gl = build_mixing_matrix(C_gl)
440	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
441	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
442	
443	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
444	    rows = []
445	
446	    for s in labels:
447	        sm = S == s
448	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
449	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
450	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
451	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
452	
453	        tau_obs = np.array([th0_n, th1_n])
454	        se_obs = np.array([se0_n, se1_n])
455	        if np.any(np.isnan(tau_obs)):
456	            continue
457	
458	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
459	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
460	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
461	
462	        def mr(method, th0, th1, se0, se1):
463	            return {**base, 'subgroup': s, 'method': method,
464	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
465	                    'se_z0': se0, 'se_z1': se1,
466	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
467	
468	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
469	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
470	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
471	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
472	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
473	
474	    return rows, {**base, **hb_diag}
475	
476	
477	# ── Aggregation ───────────────────────────────────────────────────────────────
478	
479	def aggregate_results(df):
480	    rows = []
481	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
482	    for keys, grp in df.groupby(grp_cols):
483	        regime, n_expert, k, subgroup, method = keys
484	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
485	               'subgroup': subgroup, 'method': method}
486	        n_mc = len(grp)
487	        for z in ['z0', 'z1']:
488	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
489	            bias = err.mean()
490	            mse = (err ** 2).mean()
491	            rmse = np.sqrt(mse)
492	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
493	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
494	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
495	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
496	            row[f'bias_{z}'] = bias
497	            row[f'rmse_{z}'] = rmse
498	            row[f'coverage_{z}'] = cov
499	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
500	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
501	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
502	        rows.append(row)
503	    return pd.DataFrame(rows)
504	
505	
506	# ── Output ────────────────────────────────────────────────────────────────────
507	
508	def print_summary(df_agg, df_diag):
509	    pd.set_option('display.float_format', '{:.4f}'.format)
510	
511	    # MCMC / Gibbs diagnostics
512	    if 'hb_method' in df_diag.columns:
513	        for method_label in ['gibbs', 'mcmc']:
514	            mrows = df_diag[df_diag['hb_method'] == method_label]
515	            if mrows.empty:
516	                continue
517	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
518	            print(f"  Runs:           {len(mrows)}")
519	            rh = mrows['rhat_max'].dropna()
520	            es = mrows['ess_min'].dropna()
521	            if not rh.empty:
522	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
523	            if not es.empty:
524	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
525	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
526	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
527	
528	    # Per-config HB vs MLE comparison
529	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530	    for k in sorted(df_agg['k_subgroups'].unique()):
531	        print(f"\n  K = {int(k)} subgroups")
532	        for regime in ['extreme', 'moderate', 'homogeneous']:
533	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534	            if sub.empty:
535	                continue
536	            print(f"    {regime}:")
537	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
538	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
539	            for ne in sorted(sub['n_expert'].unique()):
540	                vals = {}
541	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
542	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
543	                    if ms.empty:
544	                        vals[m] = np.nan
545	                    else:
546	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
547	                                           ms['rmse_z1'].values ** 2).mean())
548	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
549	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
550	                tag = f"{pct:+.1f}%"
551	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
552	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
553	
554	
555	# ── Sweep ─────────────────────────────────────────────────────────────────────
556	
557	def run_sweep(regime_names, n_experts, k_list, n_mc,
558	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559	    all_rows, all_diag = [], []
560	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
561	    count = 0
562	    t0 = time.time()
563	
564	    for k in k_list:
565	        for rn in regime_names:
566	            if rn not in REGIMES[k]:
567	                continue
568	            rp = REGIMES[k][rn]
569	            for ne in n_experts:
570	                for mc in range(n_mc):
571	                    use = hb_method
572	                    if hb_method == 'auto':
573	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
574	                    try:
575	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
576	                        all_rows.extend(rows)
577	                        all_diag.append(diag)
578	                    except Exception as e:
579	                        if verbose:
580	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
581	                        all_diag.append({
582	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
583	                            'mc_run': mc, 'hb_method': 'error',
584	                            'rhat_max': np.nan, 'ess_min': np.nan,
585	                            'divergent_count': -1, 'runtime_seconds': 0.0})
586	                    count += 1
587	                    if verbose and count % max(1, total // 20) == 0:
588	                        el = time.time() - t0
589	                        eta = el / count * (total - count)
590	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
591	                              f"k={k} {rn} ne={ne} mc={mc}")
592	
593	    if verbose:
594	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
595	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
596	
597	
598	# ── Main ──────────────────────────────────────────────────────────────────────
599	
600	if __name__ == '__main__':
601	    parser = argparse.ArgumentParser()
602	    parser.add_argument('--n-mc', type=int, default=100)
603	    parser.add_argument('--dry-run', action='store_true')
604	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
605	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
606	    args = parser.parse_args()
607	
608	    n_mc = 5 if args.dry_run else args.n_mc
609	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
610	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
611	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
612	
613	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
614	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
615	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
616	
617	    # Timing test
618	    effective_method = args.hb_method
619	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
620	    em = d['expert_mask']
621	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
622	
623	    if args.hb_method == 'auto':
624	        print("Timing Gibbs sampler...")
625	        t0 = time.time()
626	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
627	        gt = time.time() - t0
628	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
629	              f"ess={dg['ess_min']:.0f}")
630	        if gt < 5:
631	            effective_method = 'gibbs'
632	            print(f"  Fast enough → using Gibbs for all runs")
633	        else:
634	            effective_method = 'eb'
635	            print(f"  Slow → using EB")
636	    elif args.hb_method == 'mcmc' and HAS_PYMC:
637	        print("Timing PyMC MCMC...")
638	        t0 = time.time()
639	        try:
640	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
641	            mt = time.time() - t0
642	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
643	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
644	        except Exception as e:
645	            print(f"  MCMC failed: {e} → falling back to Gibbs")
646	            effective_method = 'gibbs'
647	
648	    print(f"\nEffective method: {effective_method}\n")
649	
650	    df_raw, df_diag = run_sweep(
651	        regime_names, n_experts, k_list, n_mc,
652	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
653	
654	    df_agg = aggregate_results(df_raw)
655	
656	    os.makedirs('results', exist_ok=True)
657	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
658	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
659	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
660	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
661	
662	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
663	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
664	    save_cols = [c for c in diag_cols if c in df_diag.columns]
665	    if 'hb_method' in df_diag.columns:
666	        save_cols.insert(4, 'hb_method')
667	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
668	
669	    print_summary(df_agg, df_diag)
670	
671	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
672	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "083afed6-494a-49d8-a8f2-c99bbdac9880",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "c92c591b-84ed-4cf8-892f-f1d080fa3558",
  "sourceToolAssistantUUID": "083afed6-494a-49d8-a8f2-c99bbdac9880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T01:32:36.740Z_

Perfect! I found all the functions you're looking for. Let me also check the other exp001 files to see if there are any additional variations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c92c591b-84ed-4cf8-892f-f1d080fa3558",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMqsQL1PSmrJfCYbco",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "965f050f-d313-47fb-95bf-6314c7aafcdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018SNjzqK4HNUw6ZBqhvnHxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11752,
      "cache_read_input_tokens": 37365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11752,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T01:32:37.348Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JvowPrCzmiuRC2KSGXLWdx`</summary>

```json
{
  "command": "head -100 /home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "965f050f-d313-47fb-95bf-6314c7aafcdf",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErMqsQL1PSmrJfCYbco",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67e3258d-e95d-44d3-ad6b-29fd8f552b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018SNjzqK4HNUw6ZBqhvnHxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11752,
      "cache_read_input_tokens": 37365,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 165,
          "cache_read_input_tokens": 37365,
          "cache_creation_input_tokens": 11752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11752,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T01:32:37.611Z_

<details><summary>↩ Tool result · `toolu_01JvowPrCzmiuRC2KSGXLWdx`</summary>

```text
#!/usr/bin/env python3
"""
exp-001 hyperprior sensitivity analysis.
Tests robustness of HB Dirichlet confusion matrix estimator
to hyperprior specification.

Sweeps over hyperprior scale factors on two configurations:
  - K=2/moderate/n=250 (safe baseline)
  - K=4/moderate/n=100 (harder: more subgroups, fewer experts)
Each config × 3 scales × 100 MC = 600 runs total.

Output: results/exp001_hyperprior_sensitivity.csv
"""

import argparse
import os
import time
import numpy as np
import pandas as pd

from exp001_hb_synthetic import (
    REGIMES, SUBGROUP_LABELS, generate_data, get_counts,
    estimate_cm_mle, estimate_cm_hb_gibbs,
    build_mixing_matrix, invert_mixing, invert_mixing_safe, diff_in_means,
)

# Default Gamma hyperprior on alpha_0: Gamma(a0=3, b0=1), mean=3, var=3.
# Scaling: Gamma(a0/s, b0/s) keeps mean fixed, scales variance by s.
#   s=0.5 → Gamma(6, 2), var=1.5  (tighter, more shrinkage)
#   s=1.0 → Gamma(3, 1), var=3    (baseline)
#   s=2.0 → Gamma(1.5, 0.5), var=6 (wider, closer to MLE)
DEFAULT_HP_A0 = 3.0
DEFAULT_HP_B0 = 1.0
HYPERPRIOR_SCALES = [0.5, 1.0, 2.0]

CONFIGS = [
    {'k': 2, 'regime': 'moderate', 'n_expert': 250, 'label': 'K2_moderate_n250'},
    {'k': 4, 'regime': 'moderate', 'n_expert': 100, 'label': 'K4_moderate_n100'},
]


def run_one_sensitivity(regime_params, n_expert, k, seed, hp_a0, hp_b0,
                        use_safe_invert=False):
    data = generate_data(regime_params, n_expert, k, seed)
    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
    em = data['expert_mask']
    labels = SUBGROUP_LABELS[k]
    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']

    counts = get_counts(Z[em], Z_hat[em], S[em], labels)

    C_mle = estimate_cm_mle(counts, labels)
    C_hb, _ = estimate_cm_hb_gibbs(counts, labels, seed=seed, hp_a0=hp_a0, hp_b0=hp_b0)

    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}

    rows = []
    for s in labels:
        sm = S == s
        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
        tau_obs = np.array([th0_n, th1_n])
        se_obs = np.array([se0_n, se1_n])
        if np.any(np.isnan(tau_obs)):
            continue

        _invert = invert_mixing_safe if use_safe_invert else invert_mixing
        tml, sml = _invert(M_mle[s], tau_obs, se_obs)
        thb, shb = _invert(M_hb[s], tau_obs, se_obs)

        base = {'subgroup': s, 'mc_run': seed, 'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
        rows.append({**base, 'method': 'mle_laplace',
                     'tau_hat_z0': tml[0], 'tau_hat_z1': tml[1],
                     'se_z0': sml[0], 'se_z1': sml[1]})
        rows.append({**base, 'method': 'hb_dirichlet',
                     'tau_hat_z0': thb[0], 'tau_hat_z1': thb[1],
                     'se_z0': shb[0], 'se_z1': shb[1]})
    return rows


def aggregate(df):
    rows = []
    for (config, scale, method, subgroup), grp in df.groupby(
            ['config', 'hyperprior_scale', 'method', 'subgroup']):
        row = {'config': config, 'hyperprior_scale': scale,
               'method': method, 'subgroup': subgroup}
        for z in ['z0', 'z1']:
            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
            bias = err.mean()
            rmse = np.sqrt((err ** 2).mean())
            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
            row[f'bias_{z}'] = bias
            row[f'rmse_{z}'] = rmse
            row[f'coverage_{z}'] = cov
        rows.append(row)
    return pd.DataFrame(rows)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67e3258d-e95d-44d3-ad6b-29fd8f552b0b",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "bf0f7abd-9ab0-4b19-b240-c3f5c9597ab3",
  "sourceToolAssistantUUID": "67e3258d-e95d-44d3-ad6b-29fd8f552b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T01:32:39.717Z_

Now let me check the regularization file as well to see if there are any variations:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0f7abd-9ab0-4b19-b240-c3f5c9597ab3",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErN2ZbPLY9S11vxGZce",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92bbfcd1-0e29-4a47-bfb6-05be722e69a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DWBMFk9Q2bBBjH87cMpUVZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 49117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T01:32:40.506Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017KZmSXsve3DR3y11NE211W`</summary>

```json
{
  "command": "grep -n \"def (build_mixing_matrix|invert_mixing|compute_confusion|generate_data)\" /home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92bbfcd1-0e29-4a47-bfb6-05be722e69a8",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErN2ZbPLY9S11vxGZce",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "667a81d2-9eee-47e3-bbea-47c8ce4fac2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DWBMFk9Q2bBBjH87cMpUVZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 49117,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 117,
          "cache_read_input_tokens": 49117,
          "cache_creation_input_tokens": 1711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1711,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T01:32:40.678Z_

<details><summary>↩ Tool result · `toolu_017KZmSXsve3DR3y11NE211W`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "667a81d2-9eee-47e3-bbea-47c8ce4fac2a",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "fcbc20c5-206e-4932-98d3-1239c7c6aa50",
  "sourceToolAssistantUUID": "667a81d2-9eee-47e3-bbea-47c8ce4fac2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T01:32:42.529Z_

Let me check the regularize file more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcbc20c5-206e-4932-98d3-1239c7c6aa50",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErNFicRTwvkjer1ihn6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce524c2f-c188-44c0-a77e-9f62e70d8c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJxCDpRntDiJBkwNJ86hq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 50828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 240,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T01:32:42.794Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JmQ86C745ZP8zL3c96FQJQ`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce524c2f-c188-44c0-a77e-9f62e70d8c44",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErNFicRTwvkjer1ihn6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e01b4ee5-a89b-4925-8fc2-476be3b84ca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJxCDpRntDiJBkwNJ86hq3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 50828,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 240
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 50828,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 240,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T01:32:42.861Z_

<details><summary>↩ Tool result · `toolu_01JmQ86C745ZP8zL3c96FQJQ`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp001_regularize.py - Rerun affected cells with condition-number-guarded inversion."""
3	
4	import argparse
5	import time
6	import numpy as np
7	import pandas as pd
8	
9	from exp001_hb_synthetic import (
10	    REGIMES, SUBGROUP_LABELS,
11	    generate_data, get_counts, build_mixing_matrix, diff_in_means,
12	    estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs,
13	    invert_mixing_safe, aggregate_results,
14	)
15	
16	AFFECTED_CELLS = [
17	    (4, 'extreme', 50),
18	    (4, 'extreme', 100),
19	    (4, 'moderate', 50),
20	    (4, 'moderate', 100),
21	    (4, 'homogeneous', 50),
22	    (4, 'homogeneous', 100),
23	]
24	
25	
26	def run_one_mc_reg(regime_name, regime_params, n_expert, k, seed,
27	                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
28	    data = generate_data(regime_params, n_expert, k, seed)
29	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
30	    em = data['expert_mask']
31	    labels = SUBGROUP_LABELS[k]
32	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
33	
34	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
35	    C_mle = estimate_cm_mle(counts, labels)
36	    C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed,
37	                                          n_chains=n_chains, n_iter=n_iter,
38	                                          n_warmup=n_warmup)
39	
40	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
41	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
42	
43	    base = {'regime': regime_name, 'n_expert': n_expert,
44	            'k_subgroups': k, 'mc_run': seed}
45	    rows = []
46	    guard_hb = 0
47	    guard_mle = 0
48	
49	    for s in labels:
50	        sm = S == s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e01b4ee5-a89b-4925-8fc2-476be3b84ca4",
  "isSidechain": true,
  "promptId": "31284733-a771-44d4-85f0-10655729d3a4",
  "agentId": "a2eeebeae4ff9ddd4",
  "type": "user",
  "uuid": "16aea61e-279d-4029-bdd5-90b59989f876",
  "sourceToolAssistantUUID": "e01b4ee5-a89b-4925-8fc2-476be3b84ca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T01:32:54.208Z_

Perfect! Now I have all the information. Let me compile my findings:

## Summary

I found all the helper functions you requested in the exp-001 experiment file. Here are the results:

### File Location
**Primary file:** `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`

**Related files also importing these functions:**
- `/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py`
- `/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py`

### Results Directory
**Yes, exists:** `/home/ubuntu/ec_hte_llm_annotation/results` (contains output CSV files and logs)

---

### Function 1: `build_mixing_matrix`
**File:** `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`
**Lines:** 98-112

```python
def build_mixing_matrix(C):
    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).

    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
    """
    M = np.zeros((2, 2))
    for zh in [0, 1]:
        cs = C[0, zh] + C[1, zh]
        if cs > 0:
            M[zh, 0] = C[0, zh] / cs
            M[zh, 1] = C[1, zh] / cs
        else:
            M[zh, :] = 0.5
    return M
```

---

### Function 2: `invert_mixing_safe`
**File:** `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`
**Lines:** 137-148

```python
def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
    """Like invert_mixing but with condition number guard."""
    cond = np.linalg.cond(M)
    if cond > cond_threshold:
        return tau_obs.copy(), se_obs.copy()
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    Mi = np.linalg.inv(M)
    tau_c = Mi @ tau_obs
    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
    return tau_c, se_c
```

---

### Function 3: Confusion Matrix Computation
**File:** `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`
**Function name:** `get_counts` (computes confusion matrix counts per subgroup)
**Lines:** 85-95

```python
def get_counts(z_true, z_hat, subgroups, labels):
    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
    k = len(labels)
    counts = np.zeros((k, 2, 2), dtype=int)
    for i, s in enumerate(labels):
        ms = subgroups == s
        for z in [0, 1]:
            mz = ms & (z_true == z)
            counts[i, z, 0] = (z_hat[mz] == 0).sum()
            counts[i, z, 1] = (z_hat[mz] == 1).sum()
    return counts
```

---

### Function 4: Data Generation (DGP)
**File:** `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`
**Function name:** `generate_data`
**Lines:** 55-71

```python
def generate_data(regime_params, n_expert, k, seed):
    rng = np.random.RandomState(seed)
    labels = SUBGROUP_LABELS[k]
    T = rng.binomial(1, 0.5, N)
    Z = rng.binomial(1, 0.5, N)
    S = rng.choice(labels, N, p=[1.0 / k] * k)
    X = rng.randn(N, 5)
    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
    mc_rates = np.zeros(N)
    for i, s in enumerate(labels):
        mc_rates[S == s] = regime_params['misclass'][i]
    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
    idx = rng.choice(N, min(n_expert, N), replace=False)
    expert_mask = np.zeros(N, dtype=bool)
    expert_mask[idx] = True
    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
```

---

### Additional Related Function
**File:** `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`
**Function name:** `invert_mixing` (non-safe version)
**Lines:** 115-122

```python
def invert_mixing(M, tau_obs, se_obs):
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    Mi = np.linalg.inv(M)
    tau_c = Mi @ tau_obs
    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
    return tau_c, se_c
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16aea61e-279d-4029-bdd5-90b59989f876",
  "isSidechain": true,
  "agentId": "a2eeebeae4ff9ddd4",
  "requestId": "req_011CbErNRMYbRKVHiQRHiuz7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b70fdcf8-e17b-47c8-9a03-f3186da7719c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "b9f8dff7-6096-42b9-b3ae-ecb9b5730df0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SfoYrUESb582LLy3aZrzGJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 51068,
      "output_tokens": 1598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 855
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1598,
          "cache_read_input_tokens": 51068,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 855,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
