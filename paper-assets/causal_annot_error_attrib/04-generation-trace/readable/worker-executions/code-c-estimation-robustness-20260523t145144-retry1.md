# code c estimation robustness 20260523T145144 retry1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_code_c_estimation_robustness_20260523T145144_retry1.log`
- **Structured JSON:** [`468fd113d1c7fdc1b422.json`](../../sessions/46/468fd113d1c7fdc1b422.json)

## Before a recorded user message

63 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-7[1m]",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "713f89c9-a02d-41cc-83a0-fad6fa4ec663",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779562800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b83cc370-75bf-468a-84be-bd0c4c7e82c5",
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "eba17322-79d0-4ce4-b0e0-d505280db500",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P3GWJndMecu4mFgb1sg2CG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17184,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17184
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Bash · `toolu_01T9UQh5QCdmtBpnwTMD3fNj`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/ 2>/dev/null | head -20",
  "description": "Check dream_reports directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "81981924-b777-4e78-b630-38c4c5ea8623",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P3GWJndMecu4mFgb1sg2CG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17184,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17184
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T14:52:06.195Z_

<details><summary>↩ Tool result · `toolu_01T9UQh5QCdmtBpnwTMD3fNj`</summary>

```text
dream_20260520T072911
dream_20260520T074549
dream_20260521T052211
dream_20260521T052307
dream_20260521T052449
dream_20260521T052547
dream_20260521T052836
dream_20260521T054240
dream_20260521T054441
dream_20260521T054528
dream_20260521T083151
latest
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "2781c4c8-941a-408a-9b97-aabe81008cd3",
  "tool_use_result": {
    "stdout": "dream_20260520T072911\ndream_20260520T074549\ndream_20260521T052211\ndream_20260521T052307\ndream_20260521T052449\ndream_20260521T052547\ndream_20260521T052836\ndream_20260521T054240\ndream_20260521T054441\ndream_20260521T054528\ndream_20260521T083151\nlatest",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01QoLuL19BtKgGasstknJ8T2`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ | grep -iE \"ranking|asv|confusion|empirical\" | head -20",
  "description": "List relevant artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "c23d14e4-961a-41da-9c94-1ecef97b6862",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P3GWJndMecu4mFgb1sg2CG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17184,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17184
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T14:52:07.183Z_

<details><summary>↩ Tool result · `toolu_01QoLuL19BtKgGasstknJ8T2`</summary>

```text
compute_ppi_empirical.py
compute_theory_empirical_mape.py
compute_updated_empirical.py
exp_c_bootstrap_asv.py
exp_e_asv_stability.py
exp_e_asv_stability_results.json
exp_e_asv_stability_table.tex
plan004_asv_framework
plan006_asv_empirical
plan006_empirical_data.txt
plan_004_asv_v3_fixed
plan_005_asv_extended_fixed.py
ppi_empirical_validation.json
ppi_empirical_validation_appendix.tex
ppi_empirical_validation_table.tex
ranking_stability.py
ranking_stability_results.json
theory_empirical_mape.json
theory_empirical_mape_table.tex
updated_empirical_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "a5b1ab70-0ef8-4a61-b596-cc9294c7b81c",
  "tool_use_result": {
    "stdout": "compute_ppi_empirical.py\ncompute_theory_empirical_mape.py\ncompute_updated_empirical.py\nexp_c_bootstrap_asv.py\nexp_e_asv_stability.py\nexp_e_asv_stability_results.json\nexp_e_asv_stability_table.tex\nplan004_asv_framework\nplan006_asv_empirical\nplan006_empirical_data.txt\nplan_004_asv_v3_fixed\nplan_005_asv_extended_fixed.py\nppi_empirical_validation.json\nppi_empirical_validation_appendix.tex\nppi_empirical_validation_table.tex\nranking_stability.py\nranking_stability_results.json\ntheory_empirical_mape.json\ntheory_empirical_mape_table.tex\nupdated_empirical_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01ChzgYWvtyEKxUffQTc7atd`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ -name \"*.json\" | xargs grep -l \"confusion\" 2>/dev/null | head -10",
  "description": "Find confusion matrix JSON files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "135539ad-7c51-4806-aa08-dfc71810863d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TEwuspfUSZxmWmbEjaqUg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 33425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T14:52:10.391Z_

<details><summary>↩ Tool result · `toolu_01ChzgYWvtyEKxUffQTc7atd`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/plan011_frontier_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/updated_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/nondiff_stress_test_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/delta_max_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_topic_stratified_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "66215a59-e239-4551-be99-06d971271555",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/plan011_frontier_cms.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/updated_empirical_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/nondiff_stress_test_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/delta_max_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_topic_stratified_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01TW1N35R8AjJSJFX8SsgvDH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "024e8f2a-7626-4925-b23a-e9bef1a104ad",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TEwuspfUSZxmWmbEjaqUg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 33425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 790
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T14:52:11.362Z_

<details><summary>↩ Tool result · `toolu_01TW1N35R8AjJSJFX8SsgvDH`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	ASV topology ranking stability analysis.
4	
5	Computes three things:
6	  1. ASV topology ranking stability: For N random Dirichlet(1,1,1) confusion
7	     matrices C0, compute magnitude ASV delta* for 6 topologies and measure
8	     Kendall tau correlation between empirical and theoretical ranking.
9	     Collider/M-bias are assigned ASV=inf (immune) since annotation error
10	     is protective (|B| non-increasing). IV is included but may produce NaN
11	     due to first-stage singularities.
12	  2. Epsilon-perturbation ranking robustness: At each delta*, check if
13	     perturbing by +/-0.013 would change the relative ranking between any
14	     pair of topologies.
15	  3. Large-scale Conjecture verification: Verify epsilon-approximate
16	     monotonicity of |B(C(delta))| along delta in [0,1] for non-IV topologies.
17	     Report worst-case step deviation across all matrices.
18	
19	Uses analytic plim computation (Gauss-Hermite quadrature for nonlinear
20	topologies) -- zero sampling noise. Fully vectorized over matrices in chunks.
21	
22	Input: Random K=3 Dirichlet(1,1,1) confusion matrices.
23	Output: artifacts/ranking_stability_results.json + console summary.
24	"""
25	
26	import numpy as np
27	import json
28	import time
29	import sys
30	import os
31	from scipy.special import roots_hermite
32	from scipy.stats import kendalltau, rankdata
33	
34	# ====================================================================
35	# Gauss-Hermite quadrature setup
36	# ====================================================================
37	N_GH = 100
38	_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)
39	GH_X = _gh_x_raw * np.sqrt(2)
40	GH_W = _gh_w_raw / np.sqrt(np.pi)
41	
42	GH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')
43	GH_W2 = np.outer(GH_W, GH_W)
44	GH_X2_a_flat = GH_X2_a.ravel()
45	GH_X2_b_flat = GH_X2_b.ravel()
46	GH_W2_flat = GH_W2.ravel()
47	
48	# ====================================================================
49	# Configuration
50	# ====================================================================
51	K = 3
52	N_MATRICES = 1_000_000
53	CHUNK_SIZE = 10_000          # process this many matrices at once
54	SEED = 42
55	DELTA_STEP = 0.005           # step size for bias curve
56	ASV_EPSILON = 0.05           # magnitude ASV threshold (10% of tau=0.5)
57	PERTURB_EPSILON = 0.013      # perturbation for ranking robustness check
58	MONO_TOL = 1e-12             # tolerance for monotonicity violation detection
59	
60	# Theoretical ranking (most fragile to most robust)
61	THEORETICAL_RANKING_ORDER = [
62	    'iv', 'frontdoor', 'mediation', 'confounding', 'collider', 'mbias'
63	]
64	
65	RANKING_TOPOS = ['iv', 'frontdoor', 'mediation', 'confounding',
66	                 'collider', 'mbias']
67	CONJECTURE_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
68	                    'mbias', 'frontdoor']
69	ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
70	             'mbias', 'iv', 'frontdoor']
71	
72	NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
73	NON_INCREASING = {'collider', 'mbias'}
74	PROTECTIVE = {'collider', 'mbias'}
75	
76	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
77	
78	# Fixed delta grid (delta_max capped at 1.0 for all Dirichlet matrices)
79	DELTAS = np.arange(0, 1.0 + DELTA_STEP / 2, DELTA_STEP)
80	N_DELTA = len(DELTAS)
81	
82	# ====================================================================
83	# DGP parameters (paper defaults, K=3)
84	# ====================================================================
85	DGP_PARAMS = {
86	    'confounding': dict(
87	        p_A=np.array([0.40, 0.35, 0.25]),
88	        alpha=np.array([1.5, -1.0]),
89	        beta_A=np.array([1.0, -0.5]),
90	        beta_T=2.0, sigma_T=1.0),
91	    'mediation': dict(
92	        tau=0.5,
93	        gamma=np.array([0.0, 0.5, -0.3]),
94	        delta=np.array([0.0, 0.8, -0.6]),
95	        beta=np.array([0.0, 1.0, -0.5])),
96	    'collider': dict(
97	        tau=1.0,
98	        g=np.array([0.0, 0.0, 0.0]),
99	        dT=np.array([0.0, 0.5, -0.3]),
100	        dY=np.array([0.0, 0.8, 0.6])),
101	    'exposure': dict(
102	        beta=np.array([0.0, 1.0, -0.5]),
103	        p_A=np.array([0.40, 0.35, 0.25])),
104	    'mbias': dict(
105	        tau=1.0, delta_coef=1.0, lam=1.0,
106	        g=np.array([0.0, 0.0, 0.0]),
107	        a1=np.array([0.0, 0.8, -0.5]),
108	        a2=np.array([0.0, 0.6, 0.9])),
109	    'iv': dict(
110	        lam=1.0,
111	        g=np.array([0.0, 0.0, 0.0]),
112	        dZ=np.array([0.0, 1.0, -0.5]),
113	        dU=np.array([0.0, 0.8, 0.6]),
114	        beta=np.array([0.0, 1.0, -0.5])),
115	    'frontdoor': dict(
116	        alpha_U=1.0, lam_U=1.0,
117	        gamma=np.array([0.0, 0.5, -0.3]),
118	        delta=np.array([0.0, 1.0, -0.8]),
119	        beta=np.array([0.0, 1.0, -0.5])),
120	}
121	
122	
123	# ====================================================================
124	# Stable softmax
125	# ====================================================================
126	def _softmax(logits):
127	    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
128	    return e / np.sum(e, axis=-1, keepdims=True)
129	
130	
131	# ====================================================================
132	# Analytic Sufficient Statistics
133	# ====================================================================
134	class SuffStats:
135	    def __init__(self, K, has_T=True):
136	        self.K = K
137	        self.has_T = has_T
138	
139	
140	class IVSuffStats:
141	    def __init__(self, K):
142	        self.K = K
143	
144	
145	def compute_confounding_ss(p):
146	    ss = SuffStats(K, has_T=True)
147	    p_A = p['p_A']
148	    alpha = p['alpha']
149	    beta_A = p['beta_A']
150	    beta_T = p['beta_T']
151	    sigma_T = p['sigma_T']
152	    ss.p_A = p_A.copy()
153	    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))
154	    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2
155	    ss.E_TD = np.zeros(K)
156	    for k in range(1, K):
157	        ss.E_TD[k] = alpha[k - 1] * p_A[k]
158	    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))
159	    ss.E_YD = np.zeros(K)
160	    for k in range(1, K):
161	        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]
162	    ss.E_TY = beta_T * ss.E_T2 + sum(
163	        beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))
164	    return ss
165	
166	
167	def compute_exposure_ss(p):
168	    ss = SuffStats(K, has_T=False)
169	    p_A = p['p_A']
170	    beta = p['beta']
171	    ss.p_A = p_A.copy()
172	    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))
173	    ss.E_YD = np.zeros(K)
174	    ss.E_YD[0] = beta[0] * p_A[0]
175	    for k in range(1, K):
176	        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]
177	    return ss
178	
179	
180	def compute_mediation_ss(p):
181	    ss = SuffStats(K, has_T=True)
182	    tau = p['tau']
183	    gamma = p['gamma']
184	    delta_coef = p['delta']
185	    beta = p['beta']
186	    probs_T0 = _softmax(gamma)
187	    probs_T1 = _softmax(gamma + delta_coef)
188	    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1
189	    ss.E_T = 0.5
190	    ss.E_T2 = 0.5
191	    ss.E_TD = 0.5 * probs_T1
192	    ss.E_Y = (beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K))
193	              + tau * 0.5)
194	    ss.E_YD = np.zeros(K)
195	    for k in range(K):
196	        beta_k = beta[k] if k >= 1 else 0.0
197	        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]
198	    ss.E_TY = (beta[0] * 0.5
199	               + sum(beta[k] * ss.E_TD[k] for k in range(1, K))
200	               + tau * 0.5)
201	    return ss
202	
203	
204	def compute_collider_ss(p):
205	    ss = SuffStats(K, has_T=True)
206	    tau = p['tau']
207	    g, dT, dY = p['g'], p['dT'], p['dY']
208	    coeff1 = dT + tau * dY
209	    coeff2 = dY
210	    logits = (g[None, :]
211	              + coeff1[None, :] * GH_X2_a_flat[:, None]
212	              + coeff2[None, :] * GH_X2_b_flat[:, None])
213	    probs = _softmax(logits)
214	    T_vals = GH_X2_a_flat
215	    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat
216	    w = GH_W2_flat
217	    ss.p_A = (w[:, None] * probs).sum(axis=0)
218	    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
219	    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)
220	    ss.E_T = 0.0
221	    ss.E_T2 = 1.0
222	    ss.E_Y = 0.0
223	    ss.E_TY = tau
224	    return ss
225	
226	
227	def compute_mbias_ss(p):
228	    ss = SuffStats(K, has_T=True)
229	    tau = p['tau']
230	    delta_coef = p['delta_coef']
231	    lam = p['lam']
232	    g, a1, a2 = p['g'], p['a1'], p['a2']
233	    logits = (g[None, :]
234	              + a1[None, :] * GH_X2_a_flat[:, None]
235	              + a2[None, :] * GH_X2_b_flat[:, None])
236	    probs = _softmax(logits)
237	    w = GH_W2_flat
238	    ss.p_A = (w[:, None] * probs).sum(axis=0)
239	    E_U1_Dk = (w[:, None] * GH_X2_a_flat[:, None] * probs).sum(axis=0)
240	    E_U2_Dk = (w[:, None] * GH_X2_b_flat[:, None] * probs).sum(axis=0)
241	    ss.E_TD = delta_coef * E_U1_Dk
242	    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk
243	    ss.E_T = 0.0
244	    ss.E_T2 = delta_coef**2 + 1.0
245	    ss.E_Y = 0.0
246	    ss.E_TY = tau * ss.E_T2
247	    return ss
248	
249	
250	def compute_frontdoor_ss(p):
251	    ss = SuffStats(K, has_T=True)
252	    alpha_U = p['alpha_U']
253	    lam_U = p['lam_U']
254	    gamma = p['gamma']
255	    delta_coef = p['delta']
256	    beta = p['beta']
257	    sigma_T2 = alpha_U**2 + 1.0
258	    sigma_T = np.sqrt(sigma_T2)
259	    T_nodes = GH_X * sigma_T
260	    T_weights = GH_W
261	    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
262	    probs = _softmax(logits)
263	    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)
264	    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)
265	    E_U_given_T = alpha_U / sigma_T2 * T_nodes
266	    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)
267	    ss.E_YD = np.zeros(K)
268	    for k in range(K):
269	        beta_k = beta[k] if k >= 1 else 0.0
270	        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]
271	    ss.E_T = 0.0
272	    ss.E_T2 = sigma_T2
273	    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))
274	    ss.E_TY = (sum(beta[k] * ss.E_TD[k] for k in range(1, K))
275	               + lam_U * alpha_U)
276	    return ss
277	
278	
279	def compute_iv_ss(p):
280	    ivss = IVSuffStats(K)
281	    g, dZ, dU = p['g'], p['dZ'], p['dU']
282	    beta = p['beta']
283	    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]
284	    probs_z0 = _softmax(logits_z0)
285	    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)
286	    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]
287	    probs_z1 = _softmax(logits_z1)
288	    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)
289	    ivss.FS = P_A_z1 - P_A_z0
290	    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))
291	    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))
292	    ivss.RF = E_Y_z1 - E_Y_z0
293	    return ivss
294	
295	
296	COMPUTE_SS = {
297	    'confounding': compute_confounding_ss,
298	    'mediation': compute_mediation_ss,
299	    'collider': compute_collider_ss,
300	    'exposure': compute_exposure_ss,
301	    'mbias': compute_mbias_ss,
302	    'iv': compute_iv_ss,
303	    'frontdoor': compute_frontdoor_ss,
304	}
305	
306	
307	def get_tau_true(topo, ss):
308	    """True causal parameter."""
309	    p = DGP_PARAMS[topo]
310	    if topo in PROTECTIVE:
311	        return p['tau']
312	    if topo == 'iv':
313	        if abs(ss.FS[1]) < 1e-15:
314	            return np.nan
315	        return ss.RF / ss.FS[1]
316	    elif topo == 'exposure':
317	        q = ss.p_A
318	        EZZ = np.zeros((K, K))
319	        EZZ[0, 0] = 1.0
320	        EZZ[0, 1:] = q[1:]
321	        EZZ[1:, 0] = q[1:]
322	        for j in range(K - 1):
323	            EZZ[j + 1, j + 1] = q[j + 1]
324	        EZY = np.zeros(K)
325	        EZY[0] = ss.E_Y
326	        EZY[1:] = ss.E_YD[1:]
327	        return np.linalg.solve(EZZ, EZY)[1]
328	    else:
329	        q = ss.p_A
330	        ct = ss.E_TD
331	        cy = ss.E_YD
332	        dim = K + 1
333	        EZZ = np.zeros((dim, dim))
334	        EZZ[0, 0] = 1.0
335	        EZZ[0, 1] = ss.E_T
336	        EZZ[1, 0] = ss.E_T
337	        EZZ[1, 1] = ss.E_T2
338	        EZZ[0, 2:] = q[1:]
339	        EZZ[2:, 0] = q[1:]
340	        EZZ[1, 2:] = ct[1:]
341	        EZZ[2:, 1] = ct[1:]
342	        for j in range(K - 1):
343	            EZZ[j + 2, j + 2] = q[j + 1]
344	        EZY = np.zeros(dim)
345	        EZY[0] = ss.E_Y
346	        EZY[1] = ss.E_TY
347	        EZY[2:] = cy[1:]
348	        return np.linalg.solve(EZZ, EZY)[1]
349	
350	
351	# ====================================================================
352	# Batch bias curve + ASV + monotonicity (fully vectorized)
353	# ====================================================================
354	def process_batch_iv(C0_batch, ss, tau_true):
355	    """Process a batch of C0 matrices for IV topology.
356	
357	    Args:
358	        C0_batch: (M, K, K) confusion matrices
359	        ss: IVSuffStats
360	        tau_true: scalar
361	
362	    Returns:
363	        asv_vals: (M,) ASV values (inf if threshold never crossed)
364	    """
365	    M = C0_batch.shape[0]
366	    # FS0[m, k] = sum_j C0[m, k, j] * ss.FS[j]
367	    FS0 = np.einsum('mkj,j->mk', C0_batch, ss.FS)  # (M, K)
368	
369	    # For each delta, FS*(delta) = (1-d)*ss.FS + d*FS0
370	    # Shape: (N_DELTA, M, K)
371	    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)
372	    fs_star = (1 - d) * ss.FS[None, None, :] + d * FS0[None, :, :]
373	    denom = fs_star[:, :, 1]  # (N_DELTA, M)
374	
375	    # tau(delta) = RF / denom
376	    with np.errstate(divide='ignore', invalid='ignore'):
377	        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
378	
379	    bias_abs = np.abs(taus - tau_true)  # (N_DELTA, M)
380	
381	    # ASV: find first delta where running-max envelope > ASV_EPSILON
382	    # Compute running max along delta axis
383	    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
384	    # Find first crossing
385	    crossed = envelope > ASV_EPSILON  # (N_DELTA, M)
386	    # For each matrix, find first delta index where crossed
387	    # Use argmax on the crossed array (first True)
388	    any_crossed = crossed.any(axis=0)  # (M,)
389	    first_idx = crossed.argmax(axis=0)  # (M,) — 0 if never crossed
390	    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
391	
392	    return asv_vals
393	
394	
395	def process_batch_exposure(C0_batch, ss, tau_true):
396	    """Process batch for exposure topology.
397	
398	    Returns:
399	        asv_vals: (M,) ASV values
400	        worst_devs: (M,) worst monotonicity violation per matrix
401	    """
402	    M = C0_batch.shape[0]
403	    # Precompute C0 @ ss.p_A and C0 @ ss.E_YD for all matrices
404	    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)  # (M, K)
405	    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)  # (M, K)
406	
407	    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)
408	    # q[delta, m, k] = (1-delta)*ss.p_A[k] + delta*pA0[m, k]
409	    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]
410	    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]
411	
412	    # Build EZZ: (N_DELTA, M, K, K) — but K=3, so (N_D, M, 3, 3)
413	    dim = K
414	    EZZ = np.zeros((N_DELTA, M, dim, dim))
415	    EZZ[:, :, 0, 0] = 1.0
416	    EZZ[:, :, 0, 1:] = q[:, :, 1:]
417	    EZZ[:, :, 1:, 0] = q[:, :, 1:]
418	    for j in range(K - 1):
419	        EZZ[:, :, j + 1, j + 1] = q[:, :, j + 1]
420	
421	    EZY = np.zeros((N_DELTA, M, dim))
422	    EZY[:, :, 0] = ss.E_Y
423	    EZY[:, :, 1:] = cy[:, :, 1:]
424	
425	    # Solve for all at once: (N_DELTA * M, dim, dim) solve
426	    EZZ_flat = EZZ.reshape(-1, dim, dim)
427	    EZY_flat = EZY.reshape(-1, dim, 1)
428	    try:
429	        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]
430	    except np.linalg.LinAlgError:
431	        coefs_flat = np.full((N_DELTA * M, dim), np.nan)
432	    taus = coefs_flat[:, 1].reshape(N_DELTA, M)
433	
434	    bias_abs = np.abs(taus - tau_true)
435	
436	    # ASV
437	    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
438	    crossed = envelope > ASV_EPSILON
439	    any_crossed = crossed.any(axis=0)
440	    first_idx = crossed.argmax(axis=0)
441	    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
442	
443	    # Monotonicity: non-decreasing
444	    valid_bias = np.nan_to_num(bias_abs, nan=0.0)
445	    diffs = np.diff(valid_bias, axis=0)  # (N_DELTA-1, M)
446	    violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)
447	    worst_devs = violations.max(axis=0)  # (M,)
448	
449	    return asv_vals, worst_devs
450	
451	
452	def process_batch_with_T(C0_batch, ss, tau_true, topo):
453	    """Process batch for topologies with treatment T.
454	
455	    Returns:
456	        asv_vals: (M,) ASV values (None if protective)
457	        worst_devs: (M,) worst monotonicity violation per matrix
458	    """
459	    M = C0_batch.shape[0]
460	    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)
461	    TD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_TD)
462	    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)
463	
464	    d = DELTAS[:, None, None]
465	    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]
466	    ct = (1 - d) * ss.E_TD[None, None, :] + d * TD0[None, :, :]
467	    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]
468	
469	    dim = K + 1
470	    EZZ = np.zeros((N_DELTA, M, dim, dim))
471	    EZZ[:, :, 0, 0] = 1.0
472	    EZZ[:, :, 0, 1] = ss.E_T
473	    EZZ[:, :, 1, 0] = ss.E_T
474	    EZZ[:, :, 1, 1] = ss.E_T2
475	    EZZ[:, :, 0, 2:] = q[:, :, 1:]
476	    EZZ[:, :, 2:, 0] = q[:, :, 1:]
477	    EZZ[:, :, 1, 2:] = ct[:, :, 1:]
478	    EZZ[:, :, 2:, 1] = ct[:, :, 1:]
479	    for j in range(K - 1):
480	        EZZ[:, :, j + 2, j + 2] = q[:, :, j + 1]
481	
482	    EZY = np.zeros((N_DELTA, M, dim))
483	    EZY[:, :, 0] = ss.E_Y
484	    EZY[:, :, 1] = ss.E_TY
485	    EZY[:, :, 2:] = cy[:, :, 1:]
486	
487	    EZZ_flat = EZZ.reshape(-1, dim, dim)
488	    EZY_flat = EZY.reshape(-1, dim, 1)
489	    try:
490	        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]
491	    except np.linalg.LinAlgError:
492	        coefs_flat = np.full((N_DELTA * M, dim), np.nan)
493	    taus = coefs_flat[:, 1].reshape(N_DELTA, M)
494	
495	    bias_abs = np.abs(taus - tau_true)
496	
497	    # ASV (only for non-protective topologies)
498	    asv_vals = None
499	    if topo not in PROTECTIVE:
500	        envelope = np.fmax.accumulate(
501	            np.nan_to_num(bias_abs, nan=0.0), axis=0)
502	        crossed = envelope > ASV_EPSILON
503	        any_crossed = crossed.any(axis=0)
504	        first_idx = crossed.argmax(axis=0)
505	        asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
506	
507	    # Monotonicity
508	    valid_bias = np.nan_to_num(bias_abs, nan=0.0)
509	    diffs = np.diff(valid_bias, axis=0)
510	    if topo in NON_DECREASING:
511	        violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)
512	    else:
513	        violations = np.where(diffs > MONO_TOL, diffs, 0.0)
514	    worst_devs = violations.max(axis=0)
515	
516	    return asv_vals, worst_devs
517	
518	
519	# ====================================================================
520	# Main
521	# ====================================================================
522	def main():
523	    t_total = time.time()
524	
525	    print("ASV Topology Ranking Stability Analysis")
526	    print(f"  N_matrices = {N_MATRICES:,}")
527	    print(f"  K = {K}, ASV_threshold = {ASV_EPSILON}")
528	    print(f"  Perturbation epsilon = {PERTURB_EPSILON}")
529	    print(f"  delta_step = {DELTA_STEP}, n_delta = {N_DELTA}")
530	    print(f"  GH quadrature: {N_GH} pts/dim")
531	    print(f"  Chunk size: {CHUNK_SIZE:,}")
532	    print(f"  Seed = {SEED}")
533	    print("=" * 70)
534	    sys.stdout.flush()
535	
536	    # ── Precompute sufficient statistics ──────────────────────────────
537	    print("\nPrecomputing analytic sufficient statistics...")
538	    all_ss = {}
539	    all_tau_true = {}
540	    for topo in ALL_TOPOS:
541	        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])
542	        all_ss[topo] = ss
543	        all_tau_true[topo] = get_tau_true(topo, ss)
544	        print(f"  {topo:<14} tau_true = {all_tau_true[topo]:.10f}")
545	    sys.stdout.flush()
546	
547	    # ── Generate random confusion matrices ────────────────────────────
548	    print(f"\nGenerating {N_MATRICES:,} Dirichlet(1,1,1) C0 matrices...")
549	    sys.stdout.flush()
550	    rng = np.random.default_rng(SEED)
551	    all_C0 = np.zeros((N_MATRICES, K, K))
552	    for j in range(K):
553	        all_C0[:, :, j] = rng.dirichlet(np.ones(K), size=N_MATRICES)
554	
555	    # ── Storage ───────────────────────────────────────────────────────
556	    ranking_topo_idx = {t: i for i, t in enumerate(RANKING_TOPOS)}
557	    n_rank = len(RANKING_TOPOS)
558	    asv_matrix = np.full((N_MATRICES, n_rank), np.nan)
559	
560	    # Collider and M-bias: ASV = inf (protective)
561	    asv_matrix[:, ranking_topo_idx['collider']] = np.inf
562	    asv_matrix[:, ranking_topo_idx['mbias']] = np.inf
563	
564	    worst_step_dev = {t: 0.0 for t in CONJECTURE_TOPOS}
565	    violation_count = {t: 0 for t in CONJECTURE_TOPOS}
566	
567	    # ── Process topologies in chunks ──────────────────────────────────
568	    print(f"\nProcessing topologies (chunk_size={CHUNK_SIZE:,})...")
569	    sys.stdout.flush()
570	
571	    n_chunks = (N_MATRICES + CHUNK_SIZE - 1) // CHUNK_SIZE
572	
573	    for topo in ALL_TOPOS:
574	        t0 = time.time()
575	        ss = all_ss[topo]
576	        tau_true = all_tau_true[topo]
577	
578	        need_asv = (topo in ranking_topo_idx and topo not in PROTECTIVE)
579	        need_conj = topo in CONJECTURE_TOPOS
580	
581	        if not need_asv and not need_conj:
582	            continue
583	
584	        topo_worst = 0.0
585	        topo_viol = 0
586	
587	        for c in range(n_chunks):
588	            start = c * CHUNK_SIZE
589	            end = min(start + CHUNK_SIZE, N_MATRICES)
590	            C0_chunk = all_C0[start:end]
591	
592	            if topo == 'iv':
593	                asv_vals = process_batch_iv(C0_chunk, ss, tau_true)
594	                if need_asv:
595	                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
596	                # No conjecture for IV
597	            elif topo == 'exposure':
598	                asv_vals, w_devs = process_batch_exposure(
599	                    C0_chunk, ss, tau_true)
600	                if need_asv:
601	                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
602	                if need_conj:
603	                    chunk_worst = float(w_devs.max())
604	                    topo_worst = max(topo_worst, chunk_worst)
605	                    topo_viol += int((w_devs > 0).sum())
606	            else:
607	                asv_vals, w_devs = process_batch_with_T(
608	                    C0_chunk, ss, tau_true, topo)
609	                if need_asv and asv_vals is not None:
610	                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
611	                if need_conj:
612	                    chunk_worst = float(w_devs.max())
613	                    topo_worst = max(topo_worst, chunk_worst)
614	                    topo_viol += int((w_devs > 0).sum())
615	
616	            if (c + 1) % max(1, n_chunks // 5) == 0:
617	                elapsed = time.time() - t0
618	                frac = (c + 1) / n_chunks
619	                eta = elapsed / frac * (1 - frac)
620	                print(f"    {topo}: chunk {c+1}/{n_chunks} "
621	                      f"({elapsed:.0f}s, ~{eta:.0f}s left)")
622	                sys.stdout.flush()
623	
624	        if need_conj:
625	            worst_step_dev[topo] = topo_worst
626	            violation_count[topo] = topo_viol
627	
628	        elapsed = time.time() - t0
629	        extras = []
630	        if need_conj:
631	            extras.append(f"worst_dev={topo_worst:.2e}")
632	            extras.append(f"viol={topo_viol}")
633	        if need_asv and topo in ranking_topo_idx:
634	            col = asv_matrix[:, ranking_topo_idx[topo]]
635	            finite = col[np.isfinite(col)]
636	            if len(finite) > 0:
637	                extras.append(f"med_ASV={np.median(finite):.4f}")
638	        print(f"  {topo:<14} {elapsed:.1f}s  {', '.join(extras)}")
639	        sys.stdout.flush()
640	
641	    # ── Part 1: Kendall tau ranking analysis ──────────────────────────
642	    print("\n" + "=" * 70)
643	    print("PART 1: ASV Topology Ranking Stability")
644	    print("=" * 70)
645	
646	    theoretical_ranks = np.array([
647	        THEORETICAL_RANKING_ORDER.index(t) + 1 for t in RANKING_TOPOS
648	    ], dtype=float)
649	
650	    # Vectorized Kendall tau for all valid matrices
651	    valid_mask = ~np.any(np.isnan(asv_matrix), axis=1)
652	    n_valid = int(valid_mask.sum())
653	
654	    kendall_taus = np.full(N_MATRICES, np.nan)
655	    exact_match_count = 0
656	
657	    if n_valid > 0:
658	        valid_asv = asv_matrix[valid_mask]
659	        emp_ranks = np.apply_along_axis(
660	            lambda x: rankdata(x, method='average'), 1, valid_asv)
661	
662	        theo_order = np.argsort(theoretical_ranks)
663	
664	        for idx in range(n_valid):
665	            tau_corr, _ = kendalltau(theoretical_ranks, emp_ranks[idx])
666	            orig_idx = np.where(valid_mask)[0][idx]
667	            kendall_taus[orig_idx] = tau_corr
668	
669	            emp_order = np.argsort(emp_ranks[idx])
670	            if np.array_equal(theo_order, emp_order):
671	                exact_match_count += 1
672	
673	    valid_taus = kendall_taus[~np.isnan(kendall_taus)]
674	    mean_tau = float(np.mean(valid_taus)) if len(valid_taus) > 0 else float('nan')
675	    min_tau = float(np.min(valid_taus)) if len(valid_taus) > 0 else float('nan')
676	    median_tau = float(np.median(valid_taus)) if len(valid_taus) > 0 else float('nan')
677	    exact_frac = exact_match_count / n_valid if n_valid > 0 else 0.0
678	
679	    print(f"  Valid rankings: {n_valid:,} / {N_MATRICES:,}")
680	    print(f"  Kendall tau:")
681	    print(f"    Mean:   {mean_tau:.4f}")
682	    print(f"    Median: {median_tau:.4f}")
683	    print(f"    Min:    {min_tau:.4f}")
684	    print(f"  Exact match: {exact_match_count:,}/{n_valid:,} ({exact_frac:.6f})")
685	
686	    tau_dist = {}
687	    for t in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
688	        frac = float(np.mean(valid_taus >= t)) if len(valid_taus) > 0 else 0.0
689	        tau_dist[f"ge_{t:.1f}"] = frac
690	        print(f"    tau >= {t:.1f}: {frac:.4f}")
691	    sys.stdout.flush()
692	
693	    # ── Part 2: epsilon-perturbation ranking robustness ───────────────
694	    print("\n" + "=" * 70)
695	    print(f"PART 2: Perturbation Robustness (eps={PERTURB_EPSILON})")
696	    print("=" * 70)
697	
698	    # Vectorized: for each valid matrix, check all pairs
699	    n_reversals = 0
700	    n_pair_reversals = 0
701	    n_checked = n_valid
702	    n_pairs_per = n_rank * (n_rank - 1) // 2
703	    n_pairs_total = n_checked * n_pairs_per
704	
705	    if n_valid > 0:
706	        valid_asv = asv_matrix[valid_mask]
707	        for a in range(n_rank):
708	            for b in range(a + 1, n_rank):
709	                va = valid_asv[:, a]
710	                vb = valid_asv[:, b]
711	                # Both inf => no reversal
712	                both_inf = np.isinf(va) & np.isinf(vb)
713	                gap = np.abs(va - vb)
714	                pair_rev = (~both_inf) & (gap < 2 * PERTURB_EPSILON)
715	                n_pair_reversals += int(pair_rev.sum())
716	
717	        # Count matrices with any reversal
718	        has_reversal = np.zeros(n_valid, dtype=bool)
719	        for a in range(n_rank):
720	            for b in range(a + 1, n_rank):
721	                va = valid_asv[:, a]
722	                vb = valid_asv[:, b]
723	                both_inf = np.isinf(va) & np.isinf(vb)
724	                gap = np.abs(va - vb)
725	                has_reversal |= (~both_inf) & (gap < 2 * PERTURB_EPSILON)
726	        n_reversals = int(has_reversal.sum())
727	
728	    rev_frac = n_reversals / n_checked if n_checked > 0 else 0.0
729	    pair_rev_frac = (n_pair_reversals / n_pairs_total
730	                     if n_pairs_total > 0 else 0.0)
731	
732	    print(f"  Matrices checked: {n_checked:,}")
733	    print(f"  Any pairwise reversal: {n_reversals:,}/{n_checked:,} "
734	          f"({rev_frac:.4f})")
735	    print(f"  Pairwise reversals: {n_pair_reversals:,}/{n_pairs_total:,} "
736	          f"({pair_rev_frac:.4f})")
737	    sys.stdout.flush()
738	
739	    # ── Part 3: Conjecture verification ───────────────────────────────
740	    print("\n" + "=" * 70)
741	    print("PART 3: Conjecture Verification (non-IV topologies)")
742	    print("=" * 70)
743	
744	    global_worst = 0.0
745	    global_worst_topo = None
746	    total_viol = 0
747	
748	    for topo in CONJECTURE_TOPOS:
749	        dev = worst_step_dev[topo]
750	        viol = violation_count[topo]
751	        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
752	        total_viol += viol
753	        print(f"  {topo:<14} [{direction}]  worst_dev={dev:.6e}  "
754	              f"violations={viol:,}/{N_MATRICES:,}")
755	        if dev > global_worst:
756	            global_worst = dev
757	            global_worst_topo = topo
758	
759	    print(f"\n  Global worst step deviation: {global_worst:.6e} "
760	          f"({global_worst_topo})")
761	    conj_holds = global_worst < 0.06
762	    print(f"  Conjecture holds (worst_dev < 0.06)? {conj_holds}")
763	    sys.stdout.flush()
764	
765	    # ── ASV summary ───────────────────────────────────────────────────
766	    print("\n" + "=" * 70)
767	    print("ASV Summary (per topology)")
768	    print("=" * 70)
769	    asv_summary = {}
770	    for topo in RANKING_TOPOS:
771	        col = asv_matrix[:, ranking_topo_idx[topo]]
772	        finite = col[np.isfinite(col) & ~np.isnan(col)]
773	        pct_inf = float(np.mean(np.isinf(col) & (col > 0)) * 100)
774	        pct_nan = float(np.mean(np.isnan(col)) * 100)
775	        if len(finite) > 0:
776	            med = float(np.median(finite))
777	            mn = float(np.mean(finite))
778	            print(f"  {topo:<14} median={med:.4f}  mean={mn:.4f}  "
779	                  f"immune={pct_inf:.1f}%  NaN={pct_nan:.1f}%")
780	            asv_summary[topo] = {
781	                "median": med, "mean": mn,
782	                "pct_immune": pct_inf, "pct_nan": pct_nan
783	            }
784	        else:
785	            print(f"  {topo:<14} all inf/NaN  immune={pct_inf:.1f}%  "
786	                  f"NaN={pct_nan:.1f}%")
787	            asv_summary[topo] = {
788	                "median": None, "mean": None,
789	                "pct_immune": pct_inf, "pct_nan": pct_nan
790	            }
791	    sys.stdout.flush()
792	
793	    # ── Save results ──────────────────────────────────────────────────
794	    total_time = time.time() - t_total
795	
796	    results = {
797	        "description": "ASV topology ranking stability analysis",
798	        "config": {
799	            "n_matrices": N_MATRICES,
800	            "K": K,
801	            "asv_threshold": ASV_EPSILON,
802	            "perturbation_epsilon": PERTURB_EPSILON,
803	            "delta_step": DELTA_STEP,
804	            "n_delta": N_DELTA,
805	            "gh_quadrature_points": N_GH,
806	            "mono_tol": MONO_TOL,
807	            "seed": SEED,
808	            "theoretical_ranking": THEORETICAL_RANKING_ORDER,
809	        },
810	        "part1_ranking_stability": {
811	            "n_valid_rankings": n_valid,
812	            "kendall_tau_mean": mean_tau,
813	            "kendall_tau_median": median_tau,
814	            "kendall_tau_min": min_tau,
815	            "exact_match_count": exact_match_count,
816	            "exact_match_fraction": exact_frac,
817	            "tau_distribution": tau_dist,
818	        },
819	        "part2_perturbation_robustness": {
820	            "n_checked": n_checked,
821	            "n_reversals": n_reversals,
822	            "reversal_fraction": rev_frac,
823	            "n_pair_reversals": n_pair_reversals,
824	            "n_pairs_total": n_pairs_total,
825	            "pair_reversal_fraction": pair_rev_frac,
826	        },
827	        "part3_conjecture_verification": {
828	            "global_worst_step_deviation": global_worst,
829	            "global_worst_topology": global_worst_topo,
830	            "conjecture_holds_0_06": conj_holds,
831	            "per_topology": {
832	                topo: {
833	                    "worst_step_deviation": worst_step_dev[topo],
834	                    "violation_count": violation_count[topo],
835	                    "direction": ("non-dec" if topo in NON_DECREASING
836	                                  else "non-inc"),
837	                }
838	                for topo in CONJECTURE_TOPOS
839	            },
840	        },
841	        "asv_summary": asv_summary,
842	        "total_time_seconds": total_time,
843	    }
844	
845	    out_path = os.path.join(OUT_DIR, 'ranking_stability_results.json')
846	    with open(out_path, 'w') as f:
847	        json.dump(results, f, indent=2)
848	    print(f"\nJSON saved: {out_path}")
849	
850	    print(f"\n{'=' * 70}")
851	    print("SUMMARY")
852	    print(f"{'=' * 70}")
853	    print(f"  Kendall tau: mean={mean_tau:.4f}, median={median_tau:.4f}, "
854	          f"min={min_tau:.4f}")
855	    print(f"  Exact ranking match: {exact_frac:.6f}")
856	    print(f"  Reversal rate (eps={PERTURB_EPSILON}): {rev_frac:.4f}")
857	    print(f"  Worst |B| step deviation: {global_worst:.6e} "
858	          f"({global_worst_topo})")
859	    print(f"  Conjecture holds: {conj_holds}")
860	    print(f"  Total time: {total_time:.1f}s ({total_time/60:.1f}min)")
861	    print(f"{'=' * 70}")
862	
863	
864	if __name__ == "__main__":
865	    main()
866	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "592bd787-7a9c-487d-95dd-425fd93fea2d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nASV topology ranking stability analysis.\n\nComputes three things:\n  1. ASV topology ranking stability: For N random Dirichlet(1,1,1) confusion\n     matrices C0, compute magnitude ASV delta* for 6 topologies and measure\n     Kendall tau correlation between empirical and theoretical ranking.\n     Collider/M-bias are assigned ASV=inf (immune) since annotation error\n     is protective (|B| non-increasing). IV is included but may produce NaN\n     due to first-stage singularities.\n  2. Epsilon-perturbation ranking robustness: At each delta*, check if\n     perturbing by +/-0.013 would change the relative ranking between any\n     pair of topologies.\n  3. Large-scale Conjecture verification: Verify epsilon-approximate\n     monotonicity of |B(C(delta))| along delta in [0,1] for non-IV topologies.\n     Report worst-case step deviation across all matrices.\n\nUses analytic plim computation (Gauss-Hermite quadrature for nonlinear\ntopologies) -- zero sampling noise. Fully vectorized over matrices in chunks.\n\nInput: Random K=3 Dirichlet(1,1,1) confusion matrices.\nOutput: artifacts/ranking_stability_results.json + console summary.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\nimport sys\nimport os\nfrom scipy.special import roots_hermite\nfrom scipy.stats import kendalltau, rankdata\n\n# ====================================================================\n# Gauss-Hermite quadrature setup\n# ====================================================================\nN_GH = 100\n_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)\nGH_X = _gh_x_raw * np.sqrt(2)\nGH_W = _gh_w_raw / np.sqrt(np.pi)\n\nGH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')\nGH_W2 = np.outer(GH_W, GH_W)\nGH_X2_a_flat = GH_X2_a.ravel()\nGH_X2_b_flat = GH_X2_b.ravel()\nGH_W2_flat = GH_W2.ravel()\n\n# ====================================================================\n# Configuration\n# ====================================================================\nK = 3\nN_MATRICES = 1_000_000\nCHUNK_SIZE = 10_000          # process this many matrices at once\nSEED = 42\nDELTA_STEP = 0.005           # step size for bias curve\nASV_EPSILON = 0.05           # magnitude ASV threshold (10% of tau=0.5)\nPERTURB_EPSILON = 0.013      # perturbation for ranking robustness check\nMONO_TOL = 1e-12             # tolerance for monotonicity violation detection\n\n# Theoretical ranking (most fragile to most robust)\nTHEORETICAL_RANKING_ORDER = [\n    'iv', 'frontdoor', 'mediation', 'confounding', 'collider', 'mbias'\n]\n\nRANKING_TOPOS = ['iv', 'frontdoor', 'mediation', 'confounding',\n                 'collider', 'mbias']\nCONJECTURE_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n                    'mbias', 'frontdoor']\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\n\nNON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}\nNON_INCREASING = {'collider', 'mbias'}\nPROTECTIVE = {'collider', 'mbias'}\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n# Fixed delta grid (delta_max capped at 1.0 for all Dirichlet matrices)\nDELTAS = np.arange(0, 1.0 + DELTA_STEP / 2, DELTA_STEP)\nN_DELTA = len(DELTAS)\n\n# ====================================================================\n# DGP parameters (paper defaults, K=3)\n# ====================================================================\nDGP_PARAMS = {\n    'confounding': dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    'mediation': dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    'collider': dict(\n        tau=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    'exposure': dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    'mbias': dict(\n        tau=1.0, delta_coef=1.0, lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    'iv': dict(\n        lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    'frontdoor': dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n}\n\n\n# ====================================================================\n# Stable softmax\n# ====================================================================\ndef _softmax(logits):\n    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))\n    return e / np.sum(e, axis=-1, keepdims=True)\n\n\n# ====================================================================\n# Analytic Sufficient Statistics\n# ====================================================================\nclass SuffStats:\n    def __init__(self, K, has_T=True):\n        self.K = K\n        self.has_T = has_T\n\n\nclass IVSuffStats:\n    def __init__(self, K):\n        self.K = K\n\n\ndef compute_confounding_ss(p):\n    ss = SuffStats(K, has_T=True)\n    p_A = p['p_A']\n    alpha = p['alpha']\n    beta_A = p['beta_A']\n    beta_T = p['beta_T']\n    sigma_T = p['sigma_T']\n    ss.p_A = p_A.copy()\n    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))\n    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2\n    ss.E_TD = np.zeros(K)\n    for k in range(1, K):\n        ss.E_TD[k] = alpha[k - 1] * p_A[k]\n    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))\n    ss.E_YD = np.zeros(K)\n    for k in range(1, K):\n        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]\n    ss.E_TY = beta_T * ss.E_T2 + sum(\n        beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))\n    return ss\n\n\ndef compute_exposure_ss(p):\n    ss = SuffStats(K, has_T=False)\n    p_A = p['p_A']\n    beta = p['beta']\n    ss.p_A = p_A.copy()\n    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))\n    ss.E_YD = np.zeros(K)\n    ss.E_YD[0] = beta[0] * p_A[0]\n    for k in range(1, K):\n        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]\n    return ss\n\n\ndef compute_mediation_ss(p):\n    ss = SuffStats(K, has_T=True)\n    tau = p['tau']\n    gamma = p['gamma']\n    delta_coef = p['delta']\n    beta = p['beta']\n    probs_T0 = _softmax(gamma)\n    probs_T1 = _softmax(gamma + delta_coef)\n    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1\n    ss.E_T = 0.5\n    ss.E_T2 = 0.5\n    ss.E_TD = 0.5 * probs_T1\n    ss.E_Y = (beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K))\n              + tau * 0.5)\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]\n    ss.E_TY = (beta[0] * 0.5\n               + sum(beta[k] * ss.E_TD[k] for k in range(1, K))\n               + tau * 0.5)\n    return ss\n\n\ndef compute_collider_ss(p):\n    ss = SuffStats(K, has_T=True)\n    tau = p['tau']\n    g, dT, dY = p['g'], p['dT'], p['dY']\n    coeff1 = dT + tau * dY\n    coeff2 = dY\n    logits = (g[None, :]\n              + coeff1[None, :] * GH_X2_a_flat[:, None]\n              + coeff2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)\n    T_vals = GH_X2_a_flat\n    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat\n    w = GH_W2_flat\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)\n    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)\n    ss.E_T = 0.0\n    ss.E_T2 = 1.0\n    ss.E_Y = 0.0\n    ss.E_TY = tau\n    return ss\n\n\ndef compute_mbias_ss(p):\n    ss = SuffStats(K, has_T=True)\n    tau = p['tau']\n    delta_coef = p['delta_coef']\n    lam = p['lam']\n    g, a1, a2 = p['g'], p['a1'], p['a2']\n    logits = (g[None, :]\n              + a1[None, :] * GH_X2_a_flat[:, None]\n              + a2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)\n    w = GH_W2_flat\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    E_U1_Dk = (w[:, None] * GH_X2_a_flat[:, None] * probs).sum(axis=0)\n    E_U2_Dk = (w[:, None] * GH_X2_b_flat[:, None] * probs).sum(axis=0)\n    ss.E_TD = delta_coef * E_U1_Dk\n    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk\n    ss.E_T = 0.0\n    ss.E_T2 = delta_coef**2 + 1.0\n    ss.E_Y = 0.0\n    ss.E_TY = tau * ss.E_T2\n    return ss\n\n\ndef compute_frontdoor_ss(p):\n    ss = SuffStats(K, has_T=True)\n    alpha_U = p['alpha_U']\n    lam_U = p['lam_U']\n    gamma = p['gamma']\n    delta_coef = p['delta']\n    beta = p['beta']\n    sigma_T2 = alpha_U**2 + 1.0\n    sigma_T = np.sqrt(sigma_T2)\n    T_nodes = GH_X * sigma_T\n    T_weights = GH_W\n    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]\n    probs = _softmax(logits)\n    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)\n    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)\n    E_U_given_T = alpha_U / sigma_T2 * T_nodes\n    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]\n    ss.E_T = 0.0\n    ss.E_T2 = sigma_T2\n    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))\n    ss.E_TY = (sum(beta[k] * ss.E_TD[k] for k in range(1, K))\n               + lam_U * alpha_U)\n    return ss\n\n\ndef compute_iv_ss(p):\n    ivss = IVSuffStats(K)\n    g, dZ, dU = p['g'], p['dZ'], p['dU']\n    beta = p['beta']\n    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]\n    probs_z0 = _softmax(logits_z0)\n    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)\n    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]\n    probs_z1 = _softmax(logits_z1)\n    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)\n    ivss.FS = P_A_z1 - P_A_z0\n    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))\n    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))\n    ivss.RF = E_Y_z1 - E_Y_z0\n    return ivss\n\n\nCOMPUTE_SS = {\n    'confounding': compute_confounding_ss,\n    'mediation': compute_mediation_ss,\n    'collider': compute_collider_ss,\n    'exposure': compute_exposure_ss,\n    'mbias': compute_mbias_ss,\n    'iv': compute_iv_ss,\n    'frontdoor': compute_frontdoor_ss,\n}\n\n\ndef get_tau_true(topo, ss):\n    \"\"\"True causal parameter.\"\"\"\n    p = DGP_PARAMS[topo]\n    if topo in PROTECTIVE:\n        return p['tau']\n    if topo == 'iv':\n        if abs(ss.FS[1]) < 1e-15:\n            return np.nan\n        return ss.RF / ss.FS[1]\n    elif topo == 'exposure':\n        q = ss.p_A\n        EZZ = np.zeros((K, K))\n        EZZ[0, 0] = 1.0\n        EZZ[0, 1:] = q[1:]\n        EZZ[1:, 0] = q[1:]\n        for j in range(K - 1):\n            EZZ[j + 1, j + 1] = q[j + 1]\n        EZY = np.zeros(K)\n        EZY[0] = ss.E_Y\n        EZY[1:] = ss.E_YD[1:]\n        return np.linalg.solve(EZZ, EZY)[1]\n    else:\n        q = ss.p_A\n        ct = ss.E_TD\n        cy = ss.E_YD\n        dim = K + 1\n        EZZ = np.zeros((dim, dim))\n        EZZ[0, 0] = 1.0\n        EZZ[0, 1] = ss.E_T\n        EZZ[1, 0] = ss.E_T\n        EZZ[1, 1] = ss.E_T2\n        EZZ[0, 2:] = q[1:]\n        EZZ[2:, 0] = q[1:]\n        EZZ[1, 2:] = ct[1:]\n        EZZ[2:, 1] = ct[1:]\n        for j in range(K - 1):\n            EZZ[j + 2, j + 2] = q[j + 1]\n        EZY = np.zeros(dim)\n        EZY[0] = ss.E_Y\n        EZY[1] = ss.E_TY\n        EZY[2:] = cy[1:]\n        return np.linalg.solve(EZZ, EZY)[1]\n\n\n# ====================================================================\n# Batch bias curve + ASV + monotonicity (fully vectorized)\n# ====================================================================\ndef process_batch_iv(C0_batch, ss, tau_true):\n    \"\"\"Process a batch of C0 matrices for IV topology.\n\n    Args:\n        C0_batch: (M, K, K) confusion matrices\n        ss: IVSuffStats\n        tau_true: scalar\n\n    Returns:\n        asv_vals: (M,) ASV values (inf if threshold never crossed)\n    \"\"\"\n    M = C0_batch.shape[0]\n    # FS0[m, k] = sum_j C0[m, k, j] * ss.FS[j]\n    FS0 = np.einsum('mkj,j->mk', C0_batch, ss.FS)  # (M, K)\n\n    # For each delta, FS*(delta) = (1-d)*ss.FS + d*FS0\n    # Shape: (N_DELTA, M, K)\n    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)\n    fs_star = (1 - d) * ss.FS[None, None, :] + d * FS0[None, :, :]\n    denom = fs_star[:, :, 1]  # (N_DELTA, M)\n\n    # tau(delta) = RF / denom\n    with np.errstate(divide='ignore', invalid='ignore'):\n        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)\n\n    bias_abs = np.abs(taus - tau_true)  # (N_DELTA, M)\n\n    # ASV: find first delta where running-max envelope > ASV_EPSILON\n    # Compute running max along delta axis\n    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)\n    # Find first crossing\n    crossed = envelope > ASV_EPSILON  # (N_DELTA, M)\n    # For each matrix, find first delta index where crossed\n    # Use argmax on the crossed array (first True)\n    any_crossed = crossed.any(axis=0)  # (M,)\n    first_idx = crossed.argmax(axis=0)  # (M,) — 0 if never crossed\n    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)\n\n    return asv_vals\n\n\ndef process_batch_exposure(C0_batch, ss, tau_true):\n    \"\"\"Process batch for exposure topology.\n\n    Returns:\n        asv_vals: (M,) ASV values\n        worst_devs: (M,) worst monotonicity violation per matrix\n    \"\"\"\n    M = C0_batch.shape[0]\n    # Precompute C0 @ ss.p_A and C0 @ ss.E_YD for all matrices\n    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)  # (M, K)\n    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)  # (M, K)\n\n    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)\n    # q[delta, m, k] = (1-delta)*ss.p_A[k] + delta*pA0[m, k]\n    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]\n    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]\n\n    # Build EZZ: (N_DELTA, M, K, K) — but K=3, so (N_D, M, 3, 3)\n    dim = K\n    EZZ = np.zeros((N_DELTA, M, dim, dim))\n    EZZ[:, :, 0, 0] = 1.0\n    EZZ[:, :, 0, 1:] = q[:, :, 1:]\n    EZZ[:, :, 1:, 0] = q[:, :, 1:]\n    for j in range(K - 1):\n        EZZ[:, :, j + 1, j + 1] = q[:, :, j + 1]\n\n    EZY = np.zeros((N_DELTA, M, dim))\n    EZY[:, :, 0] = ss.E_Y\n    EZY[:, :, 1:] = cy[:, :, 1:]\n\n    # Solve for all at once: (N_DELTA * M, dim, dim) solve\n    EZZ_flat = EZZ.reshape(-1, dim, dim)\n    EZY_flat = EZY.reshape(-1, dim, 1)\n    try:\n        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]\n    except np.linalg.LinAlgError:\n        coefs_flat = np.full((N_DELTA * M, dim), np.nan)\n    taus = coefs_flat[:, 1].reshape(N_DELTA, M)\n\n    bias_abs = np.abs(taus - tau_true)\n\n    # ASV\n    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)\n    crossed = envelope > ASV_EPSILON\n    any_crossed = crossed.any(axis=0)\n    first_idx = crossed.argmax(axis=0)\n    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)\n\n    # Monotonicity: non-decreasing\n    valid_bias = np.nan_to_num(bias_abs, nan=0.0)\n    diffs = np.diff(valid_bias, axis=0)  # (N_DELTA-1, M)\n    violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)\n    worst_devs = violations.max(axis=0)  # (M,)\n\n    return asv_vals, worst_devs\n\n\ndef process_batch_with_T(C0_batch, ss, tau_true, topo):\n    \"\"\"Process batch for topologies with treatment T.\n\n    Returns:\n        asv_vals: (M,) ASV values (None if protective)\n        worst_devs: (M,) worst monotonicity violation per matrix\n    \"\"\"\n    M = C0_batch.shape[0]\n    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)\n    TD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_TD)\n    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)\n\n    d = DELTAS[:, None, None]\n    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]\n    ct = (1 - d) * ss.E_TD[None, None, :] + d * TD0[None, :, :]\n    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]\n\n    dim = K + 1\n    EZZ = np.zeros((N_DELTA, M, dim, dim))\n    EZZ[:, :, 0, 0] = 1.0\n    EZZ[:, :, 0, 1] = ss.E_T\n    EZZ[:, :, 1, 0] = ss.E_T\n    EZZ[:, :, 1, 1] = ss.E_T2\n    EZZ[:, :, 0, 2:] = q[:, :, 1:]\n    EZZ[:, :, 2:, 0] = q[:, :, 1:]\n    EZZ[:, :, 1, 2:] = ct[:, :, 1:]\n    EZZ[:, :, 2:, 1] = ct[:, :, 1:]\n    for j in range(K - 1):\n        EZZ[:, :, j + 2, j + 2] = q[:, :, j + 1]\n\n    EZY = np.zeros((N_DELTA, M, dim))\n    EZY[:, :, 0] = ss.E_Y\n    EZY[:, :, 1] = ss.E_TY\n    EZY[:, :, 2:] = cy[:, :, 1:]\n\n    EZZ_flat = EZZ.reshape(-1, dim, dim)\n    EZY_flat = EZY.reshape(-1, dim, 1)\n    try:\n        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]\n    except np.linalg.LinAlgError:\n        coefs_flat = np.full((N_DELTA * M, dim), np.nan)\n    taus = coefs_flat[:, 1].reshape(N_DELTA, M)\n\n    bias_abs = np.abs(taus - tau_true)\n\n    # ASV (only for non-protective topologies)\n    asv_vals = None\n    if topo not in PROTECTIVE:\n        envelope = np.fmax.accumulate(\n            np.nan_to_num(bias_abs, nan=0.0), axis=0)\n        crossed = envelope > ASV_EPSILON\n        any_crossed = crossed.any(axis=0)\n        first_idx = crossed.argmax(axis=0)\n        asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)\n\n    # Monotonicity\n    valid_bias = np.nan_to_num(bias_abs, nan=0.0)\n    diffs = np.diff(valid_bias, axis=0)\n    if topo in NON_DECREASING:\n        violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)\n    else:\n        violations = np.where(diffs > MONO_TOL, diffs, 0.0)\n    worst_devs = violations.max(axis=0)\n\n    return asv_vals, worst_devs\n\n\n# ====================================================================\n# Main\n# ====================================================================\ndef main():\n    t_total = time.time()\n\n    print(\"ASV Topology Ranking Stability Analysis\")\n    print(f\"  N_matrices = {N_MATRICES:,}\")\n    print(f\"  K = {K}, ASV_threshold = {ASV_EPSILON}\")\n    print(f\"  Perturbation epsilon = {PERTURB_EPSILON}\")\n    print(f\"  delta_step = {DELTA_STEP}, n_delta = {N_DELTA}\")\n    print(f\"  GH quadrature: {N_GH} pts/dim\")\n    print(f\"  Chunk size: {CHUNK_SIZE:,}\")\n    print(f\"  Seed = {SEED}\")\n    print(\"=\" * 70)\n    sys.stdout.flush()\n\n    # ── Precompute sufficient statistics ──────────────────────────────\n    print(\"\\nPrecomputing analytic sufficient statistics...\")\n    all_ss = {}\n    all_tau_true = {}\n    for topo in ALL_TOPOS:\n        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])\n        all_ss[topo] = ss\n        all_tau_true[topo] = get_tau_true(topo, ss)\n        print(f\"  {topo:<14} tau_true = {all_tau_true[topo]:.10f}\")\n    sys.stdout.flush()\n\n    # ── Generate random confusion matrices ────────────────────────────\n    print(f\"\\nGenerating {N_MATRICES:,} Dirichlet(1,1,1) C0 matrices...\")\n    sys.stdout.flush()\n    rng = np.random.default_rng(SEED)\n    all_C0 = np.zeros((N_MATRICES, K, K))\n    for j in range(K):\n        all_C0[:, :, j] = rng.dirichlet(np.ones(K), size=N_MATRICES)\n\n    # ── Storage ───────────────────────────────────────────────────────\n    ranking_topo_idx = {t: i for i, t in enumerate(RANKING_TOPOS)}\n    n_rank = len(RANKING_TOPOS)\n    asv_matrix = np.full((N_MATRICES, n_rank), np.nan)\n\n    # Collider and M-bias: ASV = inf (protective)\n    asv_matrix[:, ranking_topo_idx['collider']] = np.inf\n    asv_matrix[:, ranking_topo_idx['mbias']] = np.inf\n\n    worst_step_dev = {t: 0.0 for t in CONJECTURE_TOPOS}\n    violation_count = {t: 0 for t in CONJECTURE_TOPOS}\n\n    # ── Process topologies in chunks ──────────────────────────────────\n    print(f\"\\nProcessing topologies (chunk_size={CHUNK_SIZE:,})...\")\n    sys.stdout.flush()\n\n    n_chunks = (N_MATRICES + CHUNK_SIZE - 1) // CHUNK_SIZE\n\n    for topo in ALL_TOPOS:\n        t0 = time.time()\n        ss = all_ss[topo]\n        tau_true = all_tau_true[topo]\n\n        need_asv = (topo in ranking_topo_idx and topo not in PROTECTIVE)\n        need_conj = topo in CONJECTURE_TOPOS\n\n        if not need_asv and not need_conj:\n            continue\n\n        topo_worst = 0.0\n        topo_viol = 0\n\n        for c in range(n_chunks):\n            start = c * CHUNK_SIZE\n            end = min(start + CHUNK_SIZE, N_MATRICES)\n            C0_chunk = all_C0[start:end]\n\n            if topo == 'iv':\n                asv_vals = process_batch_iv(C0_chunk, ss, tau_true)\n                if need_asv:\n                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals\n                # No conjecture for IV\n            elif topo == 'exposure':\n                asv_vals, w_devs = process_batch_exposure(\n                    C0_chunk, ss, tau_true)\n                if need_asv:\n                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals\n                if need_conj:\n                    chunk_worst = float(w_devs.max())\n                    topo_worst = max(topo_worst, chunk_worst)\n                    topo_viol += int((w_devs > 0).sum())\n            else:\n                asv_vals, w_devs = process_batch_with_T(\n                    C0_chunk, ss, tau_true, topo)\n                if need_asv and asv_vals is not None:\n                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals\n                if need_conj:\n                    chunk_worst = float(w_devs.max())\n                    topo_worst = max(topo_worst, chunk_worst)\n                    topo_viol += int((w_devs > 0).sum())\n\n            if (c + 1) % max(1, n_chunks // 5) == 0:\n                elapsed = time.time() - t0\n                frac = (c + 1) / n_chunks\n                eta = elapsed / frac * (1 - frac)\n                print(f\"    {topo}: chunk {c+1}/{n_chunks} \"\n                      f\"({elapsed:.0f}s, ~{eta:.0f}s left)\")\n                sys.stdout.flush()\n\n        if need_conj:\n            worst_step_dev[topo] = topo_worst\n            violation_count[topo] = topo_viol\n\n        elapsed = time.time() - t0\n        extras = []\n        if need_conj:\n            extras.append(f\"worst_dev={topo_worst:.2e}\")\n            extras.append(f\"viol={topo_viol}\")\n        if need_asv and topo in ranking_topo_idx:\n            col = asv_matrix[:, ranking_topo_idx[topo]]\n            finite = col[np.isfinite(col)]\n            if len(finite) > 0:\n                extras.append(f\"med_ASV={np.median(finite):.4f}\")\n        print(f\"  {topo:<14} {elapsed:.1f}s  {', '.join(extras)}\")\n        sys.stdout.flush()\n\n    # ── Part 1: Kendall tau ranking analysis ──────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 1: ASV Topology Ranking Stability\")\n    print(\"=\" * 70)\n\n    theoretical_ranks = np.array([\n        THEORETICAL_RANKING_ORDER.index(t) + 1 for t in RANKING_TOPOS\n    ], dtype=float)\n\n    # Vectorized Kendall tau for all valid matrices\n    valid_mask = ~np.any(np.isnan(asv_matrix), axis=1)\n    n_valid = int(valid_mask.sum())\n\n    kendall_taus = np.full(N_MATRICES, np.nan)\n    exact_match_count = 0\n\n    if n_valid > 0:\n        valid_asv = asv_matrix[valid_mask]\n        emp_ranks = np.apply_along_axis(\n            lambda x: rankdata(x, method='average'), 1, valid_asv)\n\n        theo_order = np.argsort(theoretical_ranks)\n\n        for idx in range(n_valid):\n            tau_corr, _ = kendalltau(theoretical_ranks, emp_ranks[idx])\n            orig_idx = np.where(valid_mask)[0][idx]\n            kendall_taus[orig_idx] = tau_corr\n\n            emp_order = np.argsort(emp_ranks[idx])\n            if np.array_equal(theo_order, emp_order):\n                exact_match_count += 1\n\n    valid_taus = kendall_taus[~np.isnan(kendall_taus)]\n    mean_tau = float(np.mean(valid_taus)) if len(valid_taus) > 0 else float('nan')\n    min_tau = float(np.min(valid_taus)) if len(valid_taus) > 0 else float('nan')\n    median_tau = float(np.median(valid_taus)) if len(valid_taus) > 0 else float('nan')\n    exact_frac = exact_match_count / n_valid if n_valid > 0 else 0.0\n\n    print(f\"  Valid rankings: {n_valid:,} / {N_MATRICES:,}\")\n    print(f\"  Kendall tau:\")\n    print(f\"    Mean:   {mean_tau:.4f}\")\n    print(f\"    Median: {median_tau:.4f}\")\n    print(f\"    Min:    {min_tau:.4f}\")\n    print(f\"  Exact match: {exact_match_count:,}/{n_valid:,} ({exact_frac:.6f})\")\n\n    tau_dist = {}\n    for t in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:\n        frac = float(np.mean(valid_taus >= t)) if len(valid_taus) > 0 else 0.0\n        tau_dist[f\"ge_{t:.1f}\"] = frac\n        print(f\"    tau >= {t:.1f}: {frac:.4f}\")\n    sys.stdout.flush()\n\n    # ── Part 2: epsilon-perturbation ranking robustness ───────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 2: Perturbation Robustness (eps={PERTURB_EPSILON})\")\n    print(\"=\" * 70)\n\n    # Vectorized: for each valid matrix, check all pairs\n    n_reversals = 0\n    n_pair_reversals = 0\n    n_checked = n_valid\n    n_pairs_per = n_rank * (n_rank - 1) // 2\n    n_pairs_total = n_checked * n_pairs_per\n\n    if n_valid > 0:\n        valid_asv = asv_matrix[valid_mask]\n        for a in range(n_rank):\n            for b in range(a + 1, n_rank):\n                va = valid_asv[:, a]\n                vb = valid_asv[:, b]\n                # Both inf => no reversal\n                both_inf = np.isinf(va) & np.isinf(vb)\n                gap = np.abs(va - vb)\n                pair_rev = (~both_inf) & (gap < 2 * PERTURB_EPSILON)\n                n_pair_reversals += int(pair_rev.sum())\n\n        # Count matrices with any reversal\n        has_reversal = np.zeros(n_valid, dtype=bool)\n        for a in range(n_rank):\n            for b in range(a + 1, n_rank):\n                va = valid_asv[:, a]\n                vb = valid_asv[:, b]\n                both_inf = np.isinf(va) & np.isinf(vb)\n                gap = np.abs(va - vb)\n                has_reversal |= (~both_inf) & (gap < 2 * PERTURB_EPSILON)\n        n_reversals = int(has_reversal.sum())\n\n    rev_frac = n_reversals / n_checked if n_checked > 0 else 0.0\n    pair_rev_frac = (n_pair_reversals / n_pairs_total\n                     if n_pairs_total > 0 else 0.0)\n\n    print(f\"  Matrices checked: {n_checked:,}\")\n    print(f\"  Any pairwise reversal: {n_reversals:,}/{n_checked:,} \"\n          f\"({rev_frac:.4f})\")\n    print(f\"  Pairwise reversals: {n_pair_reversals:,}/{n_pairs_total:,} \"\n          f\"({pair_rev_frac:.4f})\")\n    sys.stdout.flush()\n\n    # ── Part 3: Conjecture verification ───────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 3: Conjecture Verification (non-IV topologies)\")\n    print(\"=\" * 70)\n\n    global_worst = 0.0\n    global_worst_topo = None\n    total_viol = 0\n\n    for topo in CONJECTURE_TOPOS:\n        dev = worst_step_dev[topo]\n        viol = violation_count[topo]\n        direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n        total_viol += viol\n        print(f\"  {topo:<14} [{direction}]  worst_dev={dev:.6e}  \"\n              f\"violations={viol:,}/{N_MATRICES:,}\")\n        if dev > global_worst:\n            global_worst = dev\n            global_worst_topo = topo\n\n    print(f\"\\n  Global worst step deviation: {global_worst:.6e} \"\n          f\"({global_worst_topo})\")\n    conj_holds = global_worst < 0.06\n    print(f\"  Conjecture holds (worst_dev < 0.06)? {conj_holds}\")\n    sys.stdout.flush()\n\n    # ── ASV summary ───────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"ASV Summary (per topology)\")\n    print(\"=\" * 70)\n    asv_summary = {}\n    for topo in RANKING_TOPOS:\n        col = asv_matrix[:, ranking_topo_idx[topo]]\n        finite = col[np.isfinite(col) & ~np.isnan(col)]\n        pct_inf = float(np.mean(np.isinf(col) & (col > 0)) * 100)\n        pct_nan = float(np.mean(np.isnan(col)) * 100)\n        if len(finite) > 0:\n            med = float(np.median(finite))\n            mn = float(np.mean(finite))\n            print(f\"  {topo:<14} median={med:.4f}  mean={mn:.4f}  \"\n                  f\"immune={pct_inf:.1f}%  NaN={pct_nan:.1f}%\")\n            asv_summary[topo] = {\n                \"median\": med, \"mean\": mn,\n                \"pct_immune\": pct_inf, \"pct_nan\": pct_nan\n            }\n        else:\n            print(f\"  {topo:<14} all inf/NaN  immune={pct_inf:.1f}%  \"\n                  f\"NaN={pct_nan:.1f}%\")\n            asv_summary[topo] = {\n                \"median\": None, \"mean\": None,\n                \"pct_immune\": pct_inf, \"pct_nan\": pct_nan\n            }\n    sys.stdout.flush()\n\n    # ── Save results ──────────────────────────────────────────────────\n    total_time = time.time() - t_total\n\n    results = {\n        \"description\": \"ASV topology ranking stability analysis\",\n        \"config\": {\n            \"n_matrices\": N_MATRICES,\n            \"K\": K,\n            \"asv_threshold\": ASV_EPSILON,\n            \"perturbation_epsilon\": PERTURB_EPSILON,\n            \"delta_step\": DELTA_STEP,\n            \"n_delta\": N_DELTA,\n            \"gh_quadrature_points\": N_GH,\n            \"mono_tol\": MONO_TOL,\n            \"seed\": SEED,\n            \"theoretical_ranking\": THEORETICAL_RANKING_ORDER,\n        },\n        \"part1_ranking_stability\": {\n            \"n_valid_rankings\": n_valid,\n            \"kendall_tau_mean\": mean_tau,\n            \"kendall_tau_median\": median_tau,\n            \"kendall_tau_min\": min_tau,\n            \"exact_match_count\": exact_match_count,\n            \"exact_match_fraction\": exact_frac,\n            \"tau_distribution\": tau_dist,\n        },\n        \"part2_perturbation_robustness\": {\n            \"n_checked\": n_checked,\n            \"n_reversals\": n_reversals,\n            \"reversal_fraction\": rev_frac,\n            \"n_pair_reversals\": n_pair_reversals,\n            \"n_pairs_total\": n_pairs_total,\n            \"pair_reversal_fraction\": pair_rev_frac,\n        },\n        \"part3_conjecture_verification\": {\n            \"global_worst_step_deviation\": global_worst,\n            \"global_worst_topology\": global_worst_topo,\n            \"conjecture_holds_0_06\": conj_holds,\n            \"per_topology\": {\n                topo: {\n                    \"worst_step_deviation\": worst_step_dev[topo],\n                    \"violation_count\": violation_count[topo],\n                    \"direction\": (\"non-dec\" if topo in NON_DECREASING\n                                  else \"non-inc\"),\n                }\n                for topo in CONJECTURE_TOPOS\n            },\n        },\n        \"asv_summary\": asv_summary,\n        \"total_time_seconds\": total_time,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'ranking_stability_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nJSON saved: {out_path}\")\n\n    print(f\"\\n{'=' * 70}\")\n    print(\"SUMMARY\")\n    print(f\"{'=' * 70}\")\n    print(f\"  Kendall tau: mean={mean_tau:.4f}, median={median_tau:.4f}, \"\n          f\"min={min_tau:.4f}\")\n    print(f\"  Exact ranking match: {exact_frac:.6f}\")\n    print(f\"  Reversal rate (eps={PERTURB_EPSILON}): {rev_frac:.4f}\")\n    print(f\"  Worst |B| step deviation: {global_worst:.6e} \"\n          f\"({global_worst_topo})\")\n    print(f\"  Conjecture holds: {conj_holds}\")\n    print(f\"  Total time: {total_time:.1f}s ({total_time/60:.1f}min)\")\n    print(f\"{'=' * 70}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 866,
      "startLine": 1,
      "totalLines": 866
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "b5d51906-c583-4740-853e-c1c380b1b103",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VxZ73frqbbTggReEj3iw7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18023,
      "cache_read_input_tokens": 34215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18023
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01GUxzqGuTG95SARrGBZprNM`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ -name \"empirical*\" 2>/dev/null | head -20",
  "description": "Find empirical files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "e1583361-3f82-4136-982a-ddc68c7408ce",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VxZ73frqbbTggReEj3iw7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18023,
      "cache_read_input_tokens": 34215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18023
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T14:52:16.888Z_

<details><summary>↩ Tool result · `toolu_01GUxzqGuTG95SARrGBZprNM`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "45eb90de-afca-473b-8f6a-6d0c32c23f28",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_012DHGXdpiEzEkC6qFeNFHfM`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/ | head -30",
  "description": "List project data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "3b7e02ba-ed04-46f3-add7-f8de846f2aa4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VxZ73frqbbTggReEj3iw7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18023,
      "cache_read_input_tokens": 34215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18023
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T14:52:17.486Z_

<details><summary>↩ Tool result · `toolu_012DHGXdpiEzEkC6qFeNFHfM`</summary>

```text
bootstrap_ci_convergence_results.json
case_study_results.json
e2e_demo_results.json
exp_d_epsilon_tau_sensitivity.json
exp_fwl_logistic_breakdown.py
mvp_confounding_dag.py
mvp_exposure_dag.py
nondiff_stress_test_results.json
nondiff_structured_stress_results.json
plan006_empirical_data.txt
plan006_empirical_data_505323.txt
plan006_full_meta.txt
plan011_frontier_cms.json
ppi_empirical_validation.json
updated_empirical_results.json
verify_lambda_bound_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "08bc7a54-506e-40d4-8aa9-61f37daf6e47",
  "tool_use_result": {
    "stdout": "bootstrap_ci_convergence_results.json\ncase_study_results.json\ne2e_demo_results.json\nexp_d_epsilon_tau_sensitivity.json\nexp_fwl_logistic_breakdown.py\nmvp_confounding_dag.py\nmvp_exposure_dag.py\nnondiff_stress_test_results.json\nnondiff_structured_stress_results.json\nplan006_empirical_data.txt\nplan006_empirical_data_505323.txt\nplan006_full_meta.txt\nplan011_frontier_cms.json\nppi_empirical_validation.json\nupdated_empirical_results.json\nverify_lambda_bound_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01GC4cRdNqXvXSJYHnwsiu6K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "8c2a94fa-c6af-4993-9623-711951038e79",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015QT3ygx1inAAKUrfdHrK7d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 630,
      "cache_read_input_tokens": 52238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 630
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T14:52:20.252Z_

<details><summary>↩ Tool result · `toolu_01GC4cRdNqXvXSJYHnwsiu6K`</summary>

```text
1	{
2	  "civil_comments/deepseek_few-shot-5": {
3	    "source": "npz",
4	    "confusion_matrix_normalized": [
5	      [
6	        0.7341211225997046,
7	        0.19863013698630136
8	      ],
9	      [
10	        0.2658788774002954,
11	        0.8013698630136986
12	      ]
13	    ],
14	    "shape": [
15	      2,
16	      2
17	    ],
18	    "labels": [
19	      "non_toxic",
20	      "toxic"
21	    ],
22	    "confusion_matrix_counts": [
23	      [
24	        994,
25	        29
26	      ],
27	      [
28	        360,
29	        117
30	      ]
31	    ],
32	    "n_samples": 1500,
33	    "accuracy": 0.7406666666666667,
34	    "n_total": 1500,
35	    "n_valid": 1500
36	  },
37	  "civil_comments/qwen2.5-7b_few-shot-3": {
38	    "source": "npz",
39	    "confusion_matrix_normalized": [
40	      [
41	        0.6787296898079763,
42	        0.2191780821917808
43	      ],
44	      [
45	        0.3212703101920236,
46	        0.7808219178082192
47	      ]
48	    ],
49	    "shape": [
50	      2,
51	      2
52	    ],
53	    "labels": [
54	      "non_toxic",
55	      "toxic"
56	    ],
57	    "confusion_matrix_counts": [
58	      [
59	        919,
60	        32
61	      ],
62	      [
63	        435,
64	        114
65	      ]
66	    ],
67	    "n_samples": 1500,
68	    "accuracy": 0.6886666666666666,
69	    "n_total": 1500,
70	    "n_valid": 1500
71	  },
72	  "civil_comments/qwen2.5-7b_few-shot-5": {
73	    "source": "npz",
74	    "confusion_matrix_normalized": [
75	      [
76	        0.7370753323485968,
77	        0.23972602739726026
78	      ],
79	      [
80	        0.26292466765140327,
81	        0.7602739726027398
82	      ]
83	    ],
84	    "shape": [
85	      2,
86	      2
87	    ],
88	    "labels": [
89	      "non_toxic",
90	      "toxic"
91	    ],
92	    "confusion_matrix_counts": [
93	      [
94	        998,
95	        35
96	      ],
97	      [
98	        356,
99	        111
100	      ]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "e27a20f7-e72c-4fa4-a434-460216689e82",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json",
      "content": "{\n  \"civil_comments/deepseek_few-shot-5\": {\n    \"source\": \"npz\",\n    \"confusion_matrix_normalized\": [\n      [\n        0.7341211225997046,\n        0.19863013698630136\n      ],\n      [\n        0.2658788774002954,\n        0.8013698630136986\n      ]\n    ],\n    \"shape\": [\n      2,\n      2\n    ],\n    \"labels\": [\n      \"non_toxic\",\n      \"toxic\"\n    ],\n    \"confusion_matrix_counts\": [\n      [\n        994,\n        29\n      ],\n      [\n        360,\n        117\n      ]\n    ],\n    \"n_samples\": 1500,\n    \"accuracy\": 0.7406666666666667,\n    \"n_total\": 1500,\n    \"n_valid\": 1500\n  },\n  \"civil_comments/qwen2.5-7b_few-shot-3\": {\n    \"source\": \"npz\",\n    \"confusion_matrix_normalized\": [\n      [\n        0.6787296898079763,\n        0.2191780821917808\n      ],\n      [\n        0.3212703101920236,\n        0.7808219178082192\n      ]\n    ],\n    \"shape\": [\n      2,\n      2\n    ],\n    \"labels\": [\n      \"non_toxic\",\n      \"toxic\"\n    ],\n    \"confusion_matrix_counts\": [\n      [\n        919,\n        32\n      ],\n      [\n        435,\n        114\n      ]\n    ],\n    \"n_samples\": 1500,\n    \"accuracy\": 0.6886666666666666,\n    \"n_total\": 1500,\n    \"n_valid\": 1500\n  },\n  \"civil_comments/qwen2.5-7b_few-shot-5\": {\n    \"source\": \"npz\",\n    \"confusion_matrix_normalized\": [\n      [\n        0.7370753323485968,\n        0.23972602739726026\n      ],\n      [\n        0.26292466765140327,\n        0.7602739726027398\n      ]\n    ],\n    \"shape\": [\n      2,\n      2\n    ],\n    \"labels\": [\n      \"non_toxic\",\n      \"toxic\"\n    ],\n    \"confusion_matrix_counts\": [\n      [\n        998,\n        35\n      ],\n      [\n        356,\n        111\n      ]",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 2807
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "5156582a-4162-4418-8d30-460df97e5f84",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014cEVvPG9npm8MBNppaMJVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 52868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1067
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_018cvJ5GcZTM14q5EZX4P2iA`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ -name \"*.json\" -newer /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py 2>/dev/null | head -20",
  "description": "Find recent JSON files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "d434ed63-3140-496c-9870-df7c09a7ca84",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014cEVvPG9npm8MBNppaMJVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 52868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1067
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T14:52:25.023Z_

<details><summary>↩ Tool result · `toolu_018cvJ5GcZTM14q5EZX4P2iA`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/e2e_demo_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/structured_nondiff_violation_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "56046abf-2ae1-4f92-957d-50cd21c1198f",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/e2e_demo_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/structured_nondiff_violation_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01JGrhgMtpkbTT1bT1qcjczp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/latest -type f 2>/dev/null | head -30",
  "description": "List dream_reports/latest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "61978de3-aa92-48d5-a9a6-a36d10e33e05",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014cEVvPG9npm8MBNppaMJVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 52868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1067
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T14:52:25.896Z_

<details><summary>↩ Tool result · `toolu_01JGrhgMtpkbTT1bT1qcjczp`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "e98d5e56-0d46-4559-81bc-28c64b1e954b",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mb3Yyv43SYwfrUDwL7CyeH`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/latest 2>&1; readlink /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/latest 2>&1",
  "description": "Check latest symlink"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "1bd73035-94e3-42f2-82ad-4e1f709f870a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019ypm1bcxnwqvwg2tCvmAjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 53935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T14:52:29.999Z_

<details><summary>↩ Tool result · `toolu_01Mb3Yyv43SYwfrUDwL7CyeH`</summary>

```text
logs
meta.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T083151
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "0f875cef-bf75-45e8-af95-69255689c3aa",
  "tool_use_result": {
    "stdout": "logs\nmeta.yaml\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T083151",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01SmSM7epp2suxM7NVXCamqe`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/ -name \"*.json\" 2>/dev/null | head -10",
  "description": "Find JSON in dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "db5db638-3643-45ad-8532-e2c49176f114",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019ypm1bcxnwqvwg2tCvmAjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 53935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 771
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T14:52:30.914Z_

<details><summary>↩ Tool result · `toolu_01SmSM7epp2suxM7NVXCamqe`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "c7bb135c-7c6b-4a21-81b9-860750ba82be",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011FrG1WQTyvMRq3Uy5QBB7A`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "62690af4-5702-4362-a8af-12e9ee7747f5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G6MdqxxV8T3McfpMuEKd9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 54706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 921
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T14:52:35.224Z_

<details><summary>↩ Tool result · `toolu_011FrG1WQTyvMRq3Uy5QBB7A`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "ca0979d7-868a-4431-9d52-2453a45d1db4",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01ToqMrZ6snQbyQ2hb4oSnvf`</summary>

```json
{
  "todos": [
    {
      "content": "Locate empirical LLM confusion matrices",
      "activeForm": "Locating empirical LLM confusion matrices",
      "status": "in_progress"
    },
    {
      "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
      "activeForm": "Designing c_estimation_robustness.py",
      "status": "pending"
    },
    {
      "content": "Run script and validate JSON output",
      "activeForm": "Running script and validating JSON output",
      "status": "pending"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "b4e2cb6c-ff25-4422-82ee-2124e52d0c53",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013mL3rEx4AvQEJPFzvXb9Dv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 42898,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42898
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 45897
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T14:52:39.305Z_

<details><summary>↩ Tool result · `toolu_01ToqMrZ6snQbyQ2hb4oSnvf`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "9dab9248-4e65-4693-a60c-070bb70cb2e5",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Locate empirical LLM confusion matrices",
        "status": "in_progress",
        "activeForm": "Locating empirical LLM confusion matrices"
      },
      {
        "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
        "status": "pending",
        "activeForm": "Designing c_estimation_robustness.py"
      },
      {
        "content": "Run script and validate JSON output",
        "status": "pending",
        "activeForm": "Running script and validating JSON output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01AdznbyWYx7Y35CTFYLt9XJ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ -name \"empirical*\" -o -name \"*confusion*\" 2>/dev/null | head -30",
  "description": "Find empirical confusion matrices files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "d7b2f725-1ec5-4a56-a7b5-be5070c3b32a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019E2xMv1zsRLDjP9sgeEnA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 59232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 290
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T14:52:43.518Z_

<details><summary>↩ Tool result · `toolu_01AdznbyWYx7Y35CTFYLt9XJ`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/cron_hook_plan003_empirical_confusion_matrices.jsonl
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/cron_hook_plan003_empirical_confusion_matrices.lock
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/archive/cron_hook_plan003_empirical_confusion_matrices_20260521T175518_250563.jsonl
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/__pycache__/confusion_matrix.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/tests/test_confusion_matrix_display.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/tests/__pycache__/test_confusion_matrix_display.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/confusion_matrix.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_PENDING_20260520T101329.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T230145.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T112306.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_DONE_20260520T230146.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T140314.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_ALLOCATED_20260520T101510.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_QUEUED_20260520T101434.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_PREPARING_20260520T101312.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T104934.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__pycache__/confusion.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "d9bc8723-904c-4c25-a3b1-94f3707e2312",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/cron_hook_plan003_empirical_confusion_matrices.jsonl\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/cron_hook_plan003_empirical_confusion_matrices.lock\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/archive/cron_hook_plan003_empirical_confusion_matrices_20260521T175518_250563.jsonl\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/__pycache__/confusion_matrix.cpython-314.pyc\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/tests/test_confusion_matrix_display.py\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/tests/__pycache__/test_confusion_matrix_display.cpython-314.pyc\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/sklearn/metrics/_plot/confusion_matrix.py\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_PENDING_20260520T101329.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T230145.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T112306.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_DONE_20260520T230146.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T140314.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_ALLOCATED_20260520T101510.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_QUEUED_20260520T101434.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_PREPARING_20260520T101312.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_RUNNING_20260520T104934.json\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__pycache__/confusion.cpython-314.pyc\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01Sf6L6CtTwSfiaPVqQwWoPw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_DONE_20260520T230146.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "69fec546-4c7f-4d24-98e1-1618701f2a4b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TPWg3VXQWKeAUjdEnBUoGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 59522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1567
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T14:52:46.391Z_

<details><summary>↩ Tool result · `toolu_01Sf6L6CtTwSfiaPVqQwWoPw`</summary>

```text
1	{
2	  "exp_id": "plan003_empirical_confusion_matrices",
3	  "project": "causal_annot_error_attrib",
4	  "state": "DONE",
5	  "previous_state": "RUNNING",
6	  "experiment_data": {
7	    "status": "DONE",
8	    "retry_count": 0,
9	    "created_at": "2026-05-20T10:13:12.825Z",
10	    "updated_at": "2026-05-20T23:01:45.976Z",
11	    "hypothesis": "Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.",
12	    "spec": {
13	      "command": "3x parallel nohup: annotate.py --model {llama4,qwen3,deepseek}",
14	      "server": "home-1x5090",
15	      "data_path": "/home/sonny/causal_annot_error_attrib/data/ (humaid.jsonl, vast.jsonl, civil_comments.jsonl)",
16	      "data_count": "HumAID 1500, VAST+CivilComments default, 9 combinations per model",
17	      "model_name": "Llama 4 Maverick, Qwen 3 235B, DeepSeek Chat V3",
18	      "seed": "N/A",
19	      "log_path": "/home/sonny/causal_annot_error_attrib/plan003_{llama4,qwen3,deepseek}.log",
20	      "api_base": "http://47.94.22.126/v1",
21	      "combinations": "3 datasets x 3 models x 3 prompts = 27 runs (3-way parallel by model)",
22	      "pids": {
23	        "llama4": 438497,
24	        "qwen3": 438843,
25	        "deepseek": 439116
26	      },
27	      "launch_method": "3x nohup parallel (streaming write + resume)",
28	      "fix_applied": "streaming write per sample + --model filter + resume from existing JSONL",
29	      "previous_attempt": "PID 401208 died, 1000 samples lost (no streaming write)"
30	    },
31	    "metrics": {
32	      "status_detail": "PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)",
33	      "api_endpoint": "http://47.94.22.126/v1/chat/completions",
34	      "data_dir": "results/ (not data/)",
35	      "tasks_complete": 6,
36	      "tasks_partial": 5,
37	      "tasks_failed": 16,
38	      "tasks_total": 27,
39	      "complete_tasks": [
40	        "humaid/llama4_zero-shot (1500)",
41	        "humaid/llama4_few-shot-3 (1498)",
42	        "humaid/qwen3_zero-shot (1500)",
43	        "humaid/deepseek_zero-shot (1500)",
44	        "vast/llama4_zero-shot (1496)",
45	        "vast/llama4_few-shot-3 (1500)"
46	      ],
47	      "partial_tasks": [
48	        "humaid/llama4_few-shot-5 (1471/1500)",
49	        "humaid/qwen3_few-shot-3 (1423/1500)",
50	        "humaid/deepseek_few-shot-3 (1345/1500)",
51	        "humaid/deepseek_few-shot-5 (1237/1500)",
52	        "vast/deepseek_zero-shot (1000/1500)"
53	      ],
54	      "failed_tasks_count": "humaid: 1, vast: 6, civil_comments: 9",
55	      "civil_comments_status": "zero valid data across all 9 combinations",
56	      "data_fields": {
57	        "true_label": "gold_label",
58	        "pred_label": "pred_label"
59	      },
60	      "pids_killed": "438843 (qwen3), 439116 (deepseek) at 22:55 UTC",
61	      "pid_438497_llama4": "exited naturally"
62	    },
63	    "reproduce": {
64	      "finished_at": "2026-05-20T23:01:45.649Z"
65	    },
66	    "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
67	    "conclusion": "failed",
68	    "completed_at": "2026-05-20T23:01:45.976Z"
69	  },
70	  "timestamp": "2026-05-20T23:01:46.024507+00:00",
71	  "trigger": "update_registry"
72	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "da61e801-1196-4cb8-a054-ab8b41fa7ca1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/checkpoints/plan003_empirical_confusion_matrices_DONE_20260520T230146.json",
      "content": "{\n  \"exp_id\": \"plan003_empirical_confusion_matrices\",\n  \"project\": \"causal_annot_error_attrib\",\n  \"state\": \"DONE\",\n  \"previous_state\": \"RUNNING\",\n  \"experiment_data\": {\n    \"status\": \"DONE\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-20T10:13:12.825Z\",\n    \"updated_at\": \"2026-05-20T23:01:45.976Z\",\n    \"hypothesis\": \"Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\",\n    \"spec\": {\n      \"command\": \"3x parallel nohup: annotate.py --model {llama4,qwen3,deepseek}\",\n      \"server\": \"home-1x5090\",\n      \"data_path\": \"/home/sonny/causal_annot_error_attrib/data/ (humaid.jsonl, vast.jsonl, civil_comments.jsonl)\",\n      \"data_count\": \"HumAID 1500, VAST+CivilComments default, 9 combinations per model\",\n      \"model_name\": \"Llama 4 Maverick, Qwen 3 235B, DeepSeek Chat V3\",\n      \"seed\": \"N/A\",\n      \"log_path\": \"/home/sonny/causal_annot_error_attrib/plan003_{llama4,qwen3,deepseek}.log\",\n      \"api_base\": \"http://47.94.22.126/v1\",\n      \"combinations\": \"3 datasets x 3 models x 3 prompts = 27 runs (3-way parallel by model)\",\n      \"pids\": {\n        \"llama4\": 438497,\n        \"qwen3\": 438843,\n        \"deepseek\": 439116\n      },\n      \"launch_method\": \"3x nohup parallel (streaming write + resume)\",\n      \"fix_applied\": \"streaming write per sample + --model filter + resume from existing JSONL\",\n      \"previous_attempt\": \"PID 401208 died, 1000 samples lost (no streaming write)\"\n    },\n    \"metrics\": {\n      \"status_detail\": \"PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\",\n      \"api_endpoint\": \"http://47.94.22.126/v1/chat/completions\",\n      \"data_dir\": \"results/ (not data/)\",\n      \"tasks_complete\": 6,\n      \"tasks_partial\": 5,\n      \"tasks_failed\": 16,\n      \"tasks_total\": 27,\n      \"complete_tasks\": [\n        \"humaid/llama4_zero-shot (1500)\",\n        \"humaid/llama4_few-shot-3 (1498)\",\n        \"humaid/qwen3_zero-shot (1500)\",\n        \"humaid/deepseek_zero-shot (1500)\",\n        \"vast/llama4_zero-shot (1496)\",\n        \"vast/llama4_few-shot-3 (1500)\"\n      ],\n      \"partial_tasks\": [\n        \"humaid/llama4_few-shot-5 (1471/1500)\",\n        \"humaid/qwen3_few-shot-3 (1423/1500)\",\n        \"humaid/deepseek_few-shot-3 (1345/1500)\",\n        \"humaid/deepseek_few-shot-5 (1237/1500)\",\n        \"vast/deepseek_zero-shot (1000/1500)\"\n      ],\n      \"failed_tasks_count\": \"humaid: 1, vast: 6, civil_comments: 9\",\n      \"civil_comments_status\": \"zero valid data across all 9 combinations\",\n      \"data_fields\": {\n        \"true_label\": \"gold_label\",\n        \"pred_label\": \"pred_label\"\n      },\n      \"pids_killed\": \"438843 (qwen3), 439116 (deepseek) at 22:55 UTC\",\n      \"pid_438497_llama4\": \"exited naturally\"\n    },\n    \"reproduce\": {\n      \"finished_at\": \"2026-05-20T23:01:45.649Z\"\n    },\n    \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\",\n    \"conclusion\": \"failed\",\n    \"completed_at\": \"2026-05-20T23:01:45.976Z\"\n  },\n  \"timestamp\": \"2026-05-20T23:01:46.024507+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 72,
      "startLine": 1,
      "totalLines": 72
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01CvZGxHJmT3XkwmXz7kEx3i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "f4813433-bb6c-4a20-94e9-6aeb6587c66d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01G9L3xEFaLpWrNNumHSAqnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1789,
      "cache_read_input_tokens": 61089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1789
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T14:52:49.295Z_

<details><summary>↩ Tool result · `toolu_01CvZGxHJmT3XkwmXz7kEx3i`</summary>

```text
1	{
2	  "confusion_matrices": {
3	    "civil_comments_deepseek_few-shot-5": [
4	      [
5	        0.7341211225997046,
6	        0.19863013698630136
7	      ],
8	      [
9	        0.2658788774002954,
10	        0.8013698630136986
11	      ]
12	    ],
13	    "civil_comments_qwen2.5-7b_few-shot-3": [
14	      [
15	        0.6787296898079763,
16	        0.2191780821917808
17	      ],
18	      [
19	        0.3212703101920236,
20	        0.7808219178082192
21	      ]
22	    ],
23	    "civil_comments_qwen2.5-7b_few-shot-5": [
24	      [
25	        0.7370753323485968,
26	        0.23972602739726026
27	      ],
28	      [
29	        0.26292466765140327,
30	        0.7602739726027398
31	      ]
32	    ],
33	    "civil_comments_qwen2.5-7b_zero-shot": [
34	      [
35	        0.7481536189069424,
36	        0.3150684931506849
37	      ],
38	      [
39	        0.2518463810930576,
40	        0.684931506849315
41	      ]
42	    ],
43	    "civil_comments_qwen3_few-shot-3": [
44	      [
45	        0.8179126572908957,
46	        0.25517241379310346
47	      ],
48	      [
49	        0.18208734270910437,
50	        0.7448275862068966
51	      ]
52	    ],
53	    "civil_comments_qwen3_few-shot-5": [
54	      [
55	        0.8240534521158129,
56	        0.20689655172413793
57	      ],
58	      [
59	        0.1759465478841871,
60	        0.7931034482758621
61	      ]
62	    ],
63	    "civil_comments_qwen3_zero-shot": [
64	      [
65	        0.778118609406953,
66	        0.25742574257425743
67	      ],
68	      [
69	        0.22188139059304704,
70	        0.7425742574257426
71	      ]
72	    ],
73	    "humaid_deepseek_few-shot-3": [
74	      [
75	        0.5795454545454546,
76	        0.15,
77	        0.050955414012738856,
78	        0.0,
79	        0.0,
80	        0.011363636363636364,
81	        0.1297071129707113,
82	        0.0,
83	        0.008287292817679558,
84	        0.043478260869565216
85	      ],
86	      [
87	        0.0,
88	        0.7,
89	        0.03184713375796178,
90	        0.024,
91	        0.0,
92	        0.056818181818181816,
93	        0.03347280334728033,
94	        0.018867924528301886,
95	        0.008287292817679558,
96	        0.006211180124223602
97	      ],
98	      [
99	        0.07954545454545454,
100	        0.0,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "c732078d-4dd4-4d5b-a58d-4adb77a15dd7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json",
      "content": "{\n  \"confusion_matrices\": {\n    \"civil_comments_deepseek_few-shot-5\": [\n      [\n        0.7341211225997046,\n        0.19863013698630136\n      ],\n      [\n        0.2658788774002954,\n        0.8013698630136986\n      ]\n    ],\n    \"civil_comments_qwen2.5-7b_few-shot-3\": [\n      [\n        0.6787296898079763,\n        0.2191780821917808\n      ],\n      [\n        0.3212703101920236,\n        0.7808219178082192\n      ]\n    ],\n    \"civil_comments_qwen2.5-7b_few-shot-5\": [\n      [\n        0.7370753323485968,\n        0.23972602739726026\n      ],\n      [\n        0.26292466765140327,\n        0.7602739726027398\n      ]\n    ],\n    \"civil_comments_qwen2.5-7b_zero-shot\": [\n      [\n        0.7481536189069424,\n        0.3150684931506849\n      ],\n      [\n        0.2518463810930576,\n        0.684931506849315\n      ]\n    ],\n    \"civil_comments_qwen3_few-shot-3\": [\n      [\n        0.8179126572908957,\n        0.25517241379310346\n      ],\n      [\n        0.18208734270910437,\n        0.7448275862068966\n      ]\n    ],\n    \"civil_comments_qwen3_few-shot-5\": [\n      [\n        0.8240534521158129,\n        0.20689655172413793\n      ],\n      [\n        0.1759465478841871,\n        0.7931034482758621\n      ]\n    ],\n    \"civil_comments_qwen3_zero-shot\": [\n      [\n        0.778118609406953,\n        0.25742574257425743\n      ],\n      [\n        0.22188139059304704,\n        0.7425742574257426\n      ]\n    ],\n    \"humaid_deepseek_few-shot-3\": [\n      [\n        0.5795454545454546,\n        0.15,\n        0.050955414012738856,\n        0.0,\n        0.0,\n        0.011363636363636364,\n        0.1297071129707113,\n        0.0,\n        0.008287292817679558,\n        0.043478260869565216\n      ],\n      [\n        0.0,\n        0.7,\n        0.03184713375796178,\n        0.024,\n        0.0,\n        0.056818181818181816,\n        0.03347280334728033,\n        0.018867924528301886,\n        0.008287292817679558,\n        0.006211180124223602\n      ],\n      [\n        0.07954545454545454,\n        0.0,",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 4212
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_0158g5w2h7fPfBvVn2rj93uD`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json') as f:\n    d = json.load(f)\nprint('Top keys:', list(d.keys()))\ncms = d.get('confusion_matrices', {})\nprint('N matrices:', len(cms))\nfor k in list(cms.keys())[:5]:\n    import numpy as np\n    arr = np.array(cms[k])\n    print(f'  {k}: shape={arr.shape}')\nprint('Other top-level keys:')\nfor k in d.keys():\n    if k != 'confusion_matrices':\n        v = d[k]\n        if isinstance(v, dict):\n            print(f'  {k}: dict with {len(v)} keys')\n        else:\n            print(f'  {k}: {type(v).__name__}')\n\"\n",
  "description": "Inspect updated_empirical_results structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "35f930ca-e0c2-4821-926a-e9c815886b72",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019K7pV9ewpR7cCpWA81Ywpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1181,
      "cache_read_input_tokens": 62878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1181
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T14:52:54.821Z_

<details><summary>↩ Tool result · `toolu_0158g5w2h7fPfBvVn2rj93uD`</summary>

```text
Top keys: ['confusion_matrices', 'config_meta', 'biases', 'summary']
N matrices: 23
  civil_comments_deepseek_few-shot-5: shape=(2, 2)
  civil_comments_qwen2.5-7b_few-shot-3: shape=(2, 2)
  civil_comments_qwen2.5-7b_few-shot-5: shape=(2, 2)
  civil_comments_qwen2.5-7b_zero-shot: shape=(2, 2)
  civil_comments_qwen3_few-shot-3: shape=(2, 2)
Other top-level keys:
  config_meta: dict with 23 keys
  biases: list
  summary: dict with 9 keys
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "6c250225-ba07-475d-99f1-f6188c03acb0",
  "tool_use_result": {
    "stdout": "Top keys: ['confusion_matrices', 'config_meta', 'biases', 'summary']\nN matrices: 23\n  civil_comments_deepseek_few-shot-5: shape=(2, 2)\n  civil_comments_qwen2.5-7b_few-shot-3: shape=(2, 2)\n  civil_comments_qwen2.5-7b_few-shot-5: shape=(2, 2)\n  civil_comments_qwen2.5-7b_zero-shot: shape=(2, 2)\n  civil_comments_qwen3_few-shot-3: shape=(2, 2)\nOther top-level keys:\n  config_meta: dict with 23 keys\n  biases: list\n  summary: dict with 9 keys",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01JvPYAeCnH13ktDKr4tVMLy`</summary>

```json
{
  "command": "python3 -c \"\nimport json, numpy as np\nwith open('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json') as f:\n    d = json.load(f)\ncms = d['confusion_matrices']\nprint('All matrix shapes:')\nshapes = {}\nfor k, v in cms.items():\n    arr = np.array(v)\n    s = arr.shape\n    shapes.setdefault(s, []).append(k)\nfor s, ks in shapes.items():\n    print(f'  shape={s}: {len(ks)} matrices')\n    for k in ks[:3]:\n        print(f'    {k}')\n\nprint()\nprint('config_meta sample:')\nprint(json.dumps(d['config_meta'][list(d['config_meta'].keys())[0]], indent=2)[:500])\n\"\n",
  "description": "Inspect matrix shapes and config_meta"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "6f74245d-f7e2-49b1-856e-fc28e3233488",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SMtTMEZU17TwhcZAou1FKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 64059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 648
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T14:53:00.605Z_

<details><summary>↩ Tool result · `toolu_01JvPYAeCnH13ktDKr4tVMLy`</summary>

```text
All matrix shapes:
  shape=(2, 2): 7 matrices
    civil_comments_deepseek_few-shot-5
    civil_comments_qwen2.5-7b_few-shot-3
    civil_comments_qwen2.5-7b_few-shot-5
  shape=(10, 10): 8 matrices
    humaid_deepseek_few-shot-3
    humaid_deepseek_few-shot-5
    humaid_deepseek_zero-shot
  shape=(3, 3): 8 matrices
    vast_deepseek_few-shot-3
    vast_deepseek_few-shot-5
    vast_llama4_few-shot-3

config_meta sample:
{
  "dataset": "humaid",
  "model_prompt": "llama4_zero-shot",
  "K": 10,
  "source": "plan006"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "db0df79b-6aa9-476b-9217-cf958ee90174",
  "tool_use_result": {
    "stdout": "All matrix shapes:\n  shape=(2, 2): 7 matrices\n    civil_comments_deepseek_few-shot-5\n    civil_comments_qwen2.5-7b_few-shot-3\n    civil_comments_qwen2.5-7b_few-shot-5\n  shape=(10, 10): 8 matrices\n    humaid_deepseek_few-shot-3\n    humaid_deepseek_few-shot-5\n    humaid_deepseek_zero-shot\n  shape=(3, 3): 8 matrices\n    vast_deepseek_few-shot-3\n    vast_deepseek_few-shot-5\n    vast_llama4_few-shot-3\n\nconfig_meta sample:\n{\n  \"dataset\": \"humaid\",\n  \"model_prompt\": \"llama4_zero-shot\",\n  \"K\": 10,\n  \"source\": \"plan006\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "55d2c2fb-4ce6-4bb1-8d40-9e5294bc1fc5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KAiiPzpWmVQjPp3QkuSw5x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 64707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 684
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01MPhAhKnMa24CQv6VUBTtK5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "5d623bdd-57c8-486d-926c-4ed18db23deb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KAiiPzpWmVQjPp3QkuSw5x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 64707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 684
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T14:53:14.250Z_

<details><summary>↩ Tool result · `toolu_01MPhAhKnMa24CQv6VUBTtK5`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Exp-E: ASV Stability Across DGPs
4	
5	Demonstrates that ASV ranking (relative topology vulnerability ordering)
6	is stable across different DGP parameter configurations.
7	
8	3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.
9	Each of 9 cells reports the median δ* over the 5 C₀s.
10	"""
11	
12	import numpy as np
13	import json
14	import time
15	
16	K = 3
17	STEP = 0.001
18	
19	# ─── C(δ) parameterization ──────────────────────────────────────────────────
20	
21	def make_C_delta(C0, delta):
22	    C = (1 - delta) * np.eye(K) + delta * C0
23	    C = np.maximum(C, 0.0)
24	    cs = C.sum(axis=0)
25	    cs = np.where(cs < 1e-10, 1.0, cs)
26	    return C / cs
27	
28	
29	def get_delta_max(C0):
30	    d = np.diag(C0).min()
31	    if d >= 1.0:
32	        return 10.0
33	    return min(1.0 / (1.0 - d), 10.0)
34	
35	
36	def make_fixed_C0(diag_val):
37	    off = (1 - diag_val) / (K - 1)
38	    C0 = np.full((K, K), off)
39	    np.fill_diagonal(C0, diag_val)
40	    return C0
41	
42	
43	# ─── Topology 1: Confounding ────────────────────────────────────────────────
44	# DAG: A → T, A → Y, T → Y, A → A*
45	# OLS: Y ~ 1 + T + D*₁ + D*₂
46	# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A
47	
48	def plim_confounding(C, dgp):
49	    p = dgp['p']
50	    g = dgp['gamma']
51	    tau = dgp['tau']
52	    bA = dgp['beta'][1:]
53	    sT = dgp.get('sigma_T', 1.0)
54	
55	    b = np.array([0.0, tau, bA[0], bA[1]])
56	    ET = g[0] * p[1] + g[1] * p[2]
57	    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2
58	    q = C @ p
59	    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]
60	                     for j in range(K)])
61	
62	    EZZ = np.array([
63	        [1,    ET,      q[1],     q[2]    ],
64	        [ET,   ET2,     ETDs[1],  ETDs[2] ],
65	        [q[1], ETDs[1], q[1],     0       ],
66	        [q[2], ETDs[2], 0,        q[2]    ]])
67	    EZX = np.array([
68	        [1,    ET,      p[1],         p[2]        ],
69	        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],
70	        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],
71	        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])
72	    return np.linalg.solve(EZZ, EZX @ b)[1]
73	
74	
75	# ─── Topology 2: Exposure ───────────────────────────────────────────────────
76	# DAG: A → Y, A → A*
77	# OLS: Y ~ 1 + D*₁ + D*₂
78	
79	def plim_exposure(C, dgp):
80	    p, beta = dgp['p'], dgp['beta']
81	    q = C @ p
82	    EZZ = np.array([
83	        [1,    q[1], q[2]],
84	        [q[1], q[1], 0   ],
85	        [q[2], 0,    q[2]]])
86	    EZX = np.array([
87	        [1,    p[1],           p[2]          ],
88	        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],
89	        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])
90	    return np.linalg.solve(EZZ, EZX @ beta)
91	
92	
93	# ─── Topology 3: IV ─────────────────────────────────────────────────────────
94	# DAG: Z → A, U → {A,Y}, A → Y, A → A*
95	# Wald estimator: RF / FS*₁
96	
97	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
98	
99	
100	def _softmax_sample(logits, rng):
101	    e = np.exp(logits - logits.max(1, keepdims=True))
102	    p = e / e.sum(1, keepdims=True)
103	    c = np.cumsum(p, axis=1)
104	    u = rng.uniform(size=logits.shape[0])
105	    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)
106	
107	
108	def precomp_iv(beta, params, N=2_000_000, seed=999):
109	    rng = np.random.default_rng(seed)
110	    Z = rng.binomial(1, 0.5, N).astype(float)
111	    U = rng.normal(0, 1, N)
112	    logits = np.column_stack([
113	        np.zeros(N),
114	        params['g1'] + params['dZ'] * Z + params['dU'] * U,
115	        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])
116	    A = _softmax_sample(logits, rng)
117	    Y = (beta[1] * (A == 1).astype(float)
118	         + beta[2] * (A == 2).astype(float)
119	         + params['lam'] * U + rng.normal(0, 1, N))
120	    z1, z0 = Z == 1, Z == 0
121	    RF = Y[z1].mean() - Y[z0].mean()
122	    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()
123	                   for k in range(K)])
124	    return dict(RF=RF, FS=FS)
125	
126	
127	def plim_iv(C, st):
128	    fs = (C @ st['FS'])[1]
129	    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs
130	
131	
132	# ─── ASV computation ────────────────────────────────────────────────────────
133	
134	def _make_grid(C0):
135	    dmax = get_delta_max(C0)
136	    n = int(round(dmax / STEP)) + 1
137	    return np.linspace(0, dmax, n)
138	
139	
140	def _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):
141	    if tau_abs < 1e-12:
142	        return 0.0
143	    thresh = threshold * tau_abs
144	    rmax = 0.0
145	    for i in range(len(deltas)):
146	        b = bias_abs[i]
147	        if not np.isnan(b):
148	            rmax = max(rmax, b)
149	        if rmax > thresh:
150	            return float(deltas[i])
151	    return None
152	
153	
154	def compute_cell_confounding(dgp, C0):
155	    deltas = _make_grid(C0)
156	    tau0 = plim_confounding(np.eye(K), dgp)
157	    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)
158	                      for d in deltas])
159	    ba = np.abs(curve - tau0)
160	    return {
161	        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),
162	        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),
163	    }
164	
165	
166	def compute_cell_exposure(dgp, C0):
167	    deltas = _make_grid(C0)
168	    beta0 = plim_exposure(np.eye(K), dgp)
169	    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)
170	                       for d in deltas])
171	
172	    mr = np.zeros(len(deltas))
173	    for i in range(len(deltas)):
174	        for k in [1, 2]:
175	            if abs(beta0[k]) > 1e-10:
176	                mr[i] = max(mr[i],
177	                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))
178	
179	    def _mag(threshold):
180	        rmax = 0.0
181	        for i in range(len(deltas)):
182	            rmax = max(rmax, mr[i])
183	            if rmax > threshold:
184	                return float(deltas[i])
185	        return None
186	
187	    sf = None
188	    for i, d in enumerate(deltas):
189	        for k in [1, 2]:
190	            if (abs(beta0[k]) > 1e-10
191	                    and abs(curves[i, k]) > 1e-10
192	                    and curves[i, k] * beta0[k] < 0):
193	                sf = float(d)
194	                break
195	        if sf is not None:
196	            break
197	
198	    return {
199	        'mag_asv_10pct': _mag(0.1),
200	        'mag_asv_50pct': _mag(0.5),
201	        'sign_flip_asv': sf,
202	    }
203	
204	
205	def compute_cell_iv(st, C0):
206	    deltas = _make_grid(C0)
207	    tau0 = plim_iv(np.eye(K), st)
208	    if np.isnan(tau0) or abs(tau0) < 1e-10:
209	        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}
210	    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])
211	    ba = np.abs(curve - tau0)
212	    return {
213	        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),
214	        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),
215	    }
216	
217	
218	def median_results(cells):
219	    keys = cells[0].keys()
220	    out = {}
221	    for k in keys:
222	        vals = [c[k] for c in cells if c[k] is not None]
223	        out[k] = round(float(np.median(vals)), 4) if vals else None
224	    return out
225	
226	
227	# ─── Main ────────────────────────────────────────────────────────────────────
228	
229	if __name__ == '__main__':
230	    t0 = time.time()
231	
232	    DGPS = [
233	        {'name': 'alternating_large',
234	         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,
235	         'p': np.array([0.5, 0.33, 0.17]),
236	         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
237	        {'name': 'same_sign_medium',
238	         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,
239	         'p': np.array([0.5, 0.33, 0.17]),
240	         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
241	        {'name': 'alternating_small',
242	         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,
243	         'p': np.array([0.5, 0.33, 0.17]),
244	         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
245	    ]
246	
247	    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]
248	    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]
249	    TOPOS = ['confounding', 'exposure', 'iv']
250	
251	    print("Exp-E: ASV Stability Across DGPs")
252	    print("=" * 70)
253	
254	    print("Precomputing IV sufficient statistics...")
255	    iv_st = {}
256	    for dgp in DGPS:
257	        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)
258	        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])
259	        print(f"  {dgp['name']}: Wald(I) = {t_iv:.6f}")
260	
261	    results = {t: {} for t in TOPOS}
262	    per_c0 = {t: {} for t in TOPOS}
263	
264	    for dgp in DGPS:
265	        nm = dgp['name']
266	        print(f"\nDGP: {nm}  beta={dgp['beta'].tolist()}")
267	
268	        for topo in TOPOS:
269	            cells = []
270	            for dv, C0 in C0S:
271	                if topo == 'confounding':
272	                    c = compute_cell_confounding(dgp, C0)
273	                elif topo == 'exposure':
274	                    c = compute_cell_exposure(dgp, C0)
275	                else:
276	                    c = compute_cell_iv(iv_st[nm], C0)
277	                cells.append(c)
278	
279	            med = median_results(cells)
280	            results[topo][nm] = med
281	            per_c0[topo][nm] = [
282	                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]
283	
284	            parts = [f"10%={med['mag_asv_10pct']}",
285	                     f"50%={med['mag_asv_50pct']}"]
286	            if 'sign_flip_asv' in med:
287	                parts.append(f"sf={med['sign_flip_asv']}")
288	            print(f"  {topo:>12}: {', '.join(parts)}")
289	
290	    # ── Ranking analysis ─────────────────────────────────────────────────────
291	    print("\n" + "=" * 70)
292	    print("Ranking (by delta*_10%, lower = more fragile)")
293	    print("=" * 70)
294	    rankings = {}
295	    for dgp in DGPS:
296	        nm = dgp['name']
297	        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))
298	                for t in TOPOS]
299	        vals.sort(key=lambda x: x[1])
300	        rankings[nm] = [t for t, _ in vals]
301	        vstr = ' < '.join(f"{t}({v:.4f})" for t, v in vals)
302	        print(f"  {nm}: {vstr}")
303	
304	    stable = len(set(tuple(r) for r in rankings.values())) == 1
305	    stability_msg = ("Rankings preserved across all 3 DGPs" if stable
306	                     else "Rankings vary across DGPs")
307	    print(f"\nStable: {stable} -- {stability_msg}")
308	
309	    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')
310	    print(f"Same-sign sign-flip: "
311	          f"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}")
312	
313	    # ── Save JSON ────────────────────────────────────────────────────────────
314	    output = {
315	        'dgp_configs': [
316	            {'name': d['name'], 'beta': d['beta'].tolist(),
317	             'tau': d['tau'], 'p': d['p'].tolist()}
318	            for d in DGPS],
319	        'C0_diag_values': DIAG_VALS,
320	        'results': results,
321	        'per_C0_results': per_c0,
322	        'rankings': rankings,
323	        'ranking_stable': stable,
324	        'ranking_stability': stability_msg,
325	    }
326	    json_path = 'artifacts/exp_e_asv_stability_results.json'
327	    with open(json_path, 'w') as f:
328	        json.dump(output, f, indent=2)
329	    print(f"\nSaved: {json_path}")
330	
331	    # ── Save LaTeX table ─────────────────────────────────────────────────────
332	    labels = {
333	        'alternating_large': r'Alt.\ large: $\bm{\beta}=[0,\,1.0,\,-0.5]$',
334	        'same_sign_medium':  r'Same-sign: $\bm{\beta}=[0,\,0.5,\,0.3]$',
335	        'alternating_small': r'Alt.\ small: $\bm{\beta}=[0,\,0.2,\,-0.1]$',
336	    }
337	    tex = [
338	        r'\begin{table}[t]',
339	        r'\centering',
340	        r'\caption{ASV stability across DGP configurations. '
341	        r'Each cell shows $\delta^*$ at the 10\% relative bias threshold '
342	        r'(median over 5 confusion matrices with diagonal '
343	        r'$\in\{0.5,0.6,0.7,0.8,0.9\}$). '
344	        r'Lower $\delta^*$ indicates greater fragility. '
345	        r'Confounding is consistently most robust; '
346	        r'for alternating-sign $\bm{\beta}$, '
347	        r'the ranking Exposure $<$ IV $<$ Confounding holds. '
348	        r"``$\infty$\!\!'' = threshold never reached within $\delta$ range.}",
349	        r'\label{tab:asv_stability}',
350	        r'\small',
351	        r'\begin{tabular}{l ccc}',
352	        r'\toprule',
353	        r' & \multicolumn{3}{c}{Magnitude ASV $\delta^*_{10\%}$} \\',
354	        r'\cmidrule(lr){2-4}',
355	        r'DGP Configuration & Confounding & Exposure & IV \\',
356	        r'\midrule',
357	    ]
358	    for dgp in DGPS:
359	        nm = dgp['name']
360	        vals = []
361	        for t in TOPOS:
362	            v = results[t][nm]['mag_asv_10pct']
363	            vals.append(f'{v:.3f}' if v is not None else r'$\infty$')
364	        tex.append(
365	            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\')
366	    tex += [r'\bottomrule', r'\end{tabular}', r'\end{table}']
367	
368	    tex_path = 'artifacts/exp_e_asv_stability_table.tex'
369	    with open(tex_path, 'w') as f:
370	        f.write('\n'.join(tex))
371	    print(f"Saved: {tex_path}")
372	
373	    print(f"\nTotal: {time.time() - t0:.1f}s")
374	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "cd7b20fc-a082-4f35-9652-5622ab949801",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and abs(curves[i, k]) > 1e-10\n                    and curves[i, k] * beta0[k] < 0):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower $\\delta^*$ indicates greater fragility. '\n        r'Confounding is consistently most robust; '\n        r'for alternating-sign $\\bm{\\beta}$, '\n        r'the ranking Exposure $<$ IV $<$ Confounding holds. '\n        r\"``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}\",\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\',\n        r'\\cmidrule(lr){2-4}',\n        r'DGP Configuration & Confounding & Exposure & IV \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else r'$\\infty$')\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
      "numLines": 374,
      "startLine": 1,
      "totalLines": 374
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "a690d1e4-4ea1-4488-a910-47c023a1273e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LswCEbhrN1bowiukXvcBW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7771,
      "cache_read_input_tokens": 65391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7771
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01YA8vZ6z8mrnjDTmeArcaBj`</summary>

```json
{
  "command": "python3 -c \"\nimport json, numpy as np\nwith open('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json') as f:\n    d = json.load(f)\ncms = d['confusion_matrices']\nprint('K=3 matrices (vast):')\nfor k, v in cms.items():\n    arr = np.array(v)\n    if arr.shape == (3, 3):\n        # Check column sums\n        col_sums = arr.sum(axis=0)\n        print(f'  {k}: col_sums={col_sums}')\n        print(f'    diag={np.diag(arr)}')\n\"\n",
  "description": "Inspect K=3 matrices"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "f7a69793-2bd4-4b02-b7e9-9836991a0c66",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LswCEbhrN1bowiukXvcBW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7771,
      "cache_read_input_tokens": 65391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7771
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T14:53:36.938Z_

<details><summary>↩ Tool result · `toolu_01YA8vZ6z8mrnjDTmeArcaBj`</summary>

```text
K=3 matrices (vast):
  vast_deepseek_few-shot-3: col_sums=[1. 1. 1.]
    diag=[0.5139 0.7985 0.1614]
  vast_deepseek_few-shot-5: col_sums=[1. 1. 1.]
    diag=[0.5268 0.7853 0.1534]
  vast_llama4_few-shot-3: col_sums=[1. 1. 1.]
    diag=[0.65952891 0.80037665 0.03585657]
  vast_llama4_zero-shot: col_sums=[1. 1. 1.]
    diag=[0.67811159 0.84090909 0.04581673]
  vast_qwen2.5-7b_few-shot-3: col_sums=[1. 1. 1.]
    diag=[0.41327623 0.82109228 0.12549801]
  vast_qwen2.5-7b_few-shot-5: col_sums=[1. 1. 1.]
    diag=[0.47537473 0.77589454 0.12549801]
  vast_qwen2.5-7b_zero-shot: col_sums=[1. 1. 1.]
    diag=[0.46137339 0.84745763 0.10956175]
  vast_qwen3_zero-shot: col_sums=[1. 1. 1.]
    diag=[0.68589744 0.77462121 0.07355865]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "7f90e722-072b-4fc0-ad25-f8436f5af227",
  "tool_use_result": {
    "stdout": "K=3 matrices (vast):\n  vast_deepseek_few-shot-3: col_sums=[1. 1. 1.]\n    diag=[0.5139 0.7985 0.1614]\n  vast_deepseek_few-shot-5: col_sums=[1. 1. 1.]\n    diag=[0.5268 0.7853 0.1534]\n  vast_llama4_few-shot-3: col_sums=[1. 1. 1.]\n    diag=[0.65952891 0.80037665 0.03585657]\n  vast_llama4_zero-shot: col_sums=[1. 1. 1.]\n    diag=[0.67811159 0.84090909 0.04581673]\n  vast_qwen2.5-7b_few-shot-3: col_sums=[1. 1. 1.]\n    diag=[0.41327623 0.82109228 0.12549801]\n  vast_qwen2.5-7b_few-shot-5: col_sums=[1. 1. 1.]\n    diag=[0.47537473 0.77589454 0.12549801]\n  vast_qwen2.5-7b_zero-shot: col_sums=[1. 1. 1.]\n    diag=[0.46137339 0.84745763 0.10956175]\n  vast_qwen3_zero-shot: col_sums=[1. 1. 1.]\n    diag=[0.68589744 0.77462121 0.07355865]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "861ae4c5-ded5-48dd-8e93-e2a714a60d91",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011XcGwQgTvCVNz1DUSdkxF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1942,
      "cache_read_input_tokens": 73162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1942
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01VdRjab1VsqubAExpdJQjdT`</summary>

```json
{
  "todos": [
    {
      "content": "Locate empirical LLM confusion matrices",
      "activeForm": "Locating empirical LLM confusion matrices",
      "status": "completed"
    },
    {
      "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
      "activeForm": "Designing c_estimation_robustness.py",
      "status": "in_progress"
    },
    {
      "content": "Run script and validate JSON output",
      "activeForm": "Running script and validating JSON output",
      "status": "pending"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "084b3b31-6f7d-4a8e-82d0-f1b4ca016898",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011XcGwQgTvCVNz1DUSdkxF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1942,
      "cache_read_input_tokens": 73162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1942
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T14:53:54.770Z_

<details><summary>↩ Tool result · `toolu_01VdRjab1VsqubAExpdJQjdT`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "c8f69aa6-d20b-4cde-8256-4528b664beb8",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Locate empirical LLM confusion matrices",
        "status": "in_progress",
        "activeForm": "Locating empirical LLM confusion matrices"
      },
      {
        "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
        "status": "pending",
        "activeForm": "Designing c_estimation_robustness.py"
      },
      {
        "content": "Run script and validate JSON output",
        "status": "pending",
        "activeForm": "Running script and validating JSON output"
      }
    ],
    "newTodos": [
      {
        "content": "Locate empirical LLM confusion matrices",
        "status": "completed",
        "activeForm": "Locating empirical LLM confusion matrices"
      },
      {
        "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
        "status": "in_progress",
        "activeForm": "Designing c_estimation_robustness.py"
      },
      {
        "content": "Run script and validate JSON output",
        "status": "pending",
        "activeForm": "Running script and validating JSON output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Write · `toolu_0154bqUogNKJ5YjUrpXgNNHZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nĈ Estimation Robustness Experiment.\n\nQuestion: With a finite K-class gold-labelled set used to estimate C, does\nthe safe/fragile topology partition (5 vs 2) hold under multinomial bootstrap\nof Ĉ?\n\nFor each empirical column-stochastic K=3 confusion matrix C (LLM truth),\ndraw B bootstrap replicates Ĉ ~ multinomial(C[:,k] · n_gold) / n_gold for\neach class k. For each Ĉ, recompute the magnitude ASV δ* for the 7\ntopologies (confounding, mediation, collider, exposure, mbias, IV,\nfrontdoor) and report:\n\n  • Partition stability rate vs n_gold: fraction of bootstraps where the\n    two lowest-ASV topologies equal {exposure, IV}.\n  • Spearman ρ vs n_gold: rank correlation between ASV ranking from Ĉ and\n    from true C (averaged over bootstraps and source matrices).\n\nEmpirical Cs come from artifacts/updated_empirical_results.json (23 LLM\nmatrices; 8 are K=3 vast/stance — the K=3 framework subset).\n\nOutput: c_estimation_robustness_results.json next to this script.\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nfrom collections import defaultdict\n\nimport numpy as np\nfrom scipy.stats import rankdata, spearmanr\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n\nfrom ranking_stability import (  # noqa: E402\n    ALL_TOPOS, COMPUTE_SS, DGP_PARAMS, K, N_DELTA, DELTAS, ASV_EPSILON,\n    PROTECTIVE, get_tau_true, process_batch_iv, process_batch_exposure,\n    process_batch_with_T,\n)\n\n# ──────────────────────────────────────────────────────────────────────────\nEMP_PATH = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json'\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_PATH = os.path.join(OUT_DIR, 'c_estimation_robustness_results.json')\n\nN_GOLD_GRID = [50, 100, 200, 500]\nB_BOOT = 200\nSEED = 20260523\nSAFE = {'confounding', 'mediation', 'collider', 'frontdoor', 'mbias'}\nFRAGILE = {'exposure', 'iv'}\nRANK_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\nTOPO_IDX = {t: i for i, t in enumerate(RANK_TOPOS)}\n\n\ndef load_k3_matrices():\n    with open(EMP_PATH) as f:\n        d = json.load(f)\n    out = {}\n    for name, cm in d['confusion_matrices'].items():\n        arr = np.asarray(cm, dtype=float)\n        if arr.shape == (K, K):\n            # Re-normalise columns just in case\n            cs = arr.sum(axis=0, keepdims=True)\n            cs = np.where(cs < 1e-12, 1.0, cs)\n            out[name] = arr / cs\n    return out\n\n\ndef bootstrap_chats(C_true, n_gold, B, rng):\n    \"\"\"Multinomial bootstrap of Ĉ.\n\n    For each class k, draw n_gold predictions from C_true[:, k] then\n    normalise. Returns (B, K, K) array of column-stochastic matrices.\n    \"\"\"\n    out = np.empty((B, K, K))\n    for k in range(K):\n        # rng.multinomial returns (B, K) with each row summing to n_gold\n        counts = rng.multinomial(n_gold, C_true[:, k], size=B)\n        out[:, :, k] = counts / float(n_gold)\n    return out\n\n\ndef compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):\n    \"\"\"Compute magnitude ASV per topology for a batch of C0 matrices.\n\n    Returns asv: (M, n_topo) ndarray. Collider/M-bias get +inf (protective).\n    \"\"\"\n    M = C0_batch.shape[0]\n    n_topo = len(RANK_TOPOS)\n    asv = np.full((M, n_topo), np.nan)\n    # Protective topologies: always inf\n    asv[:, TOPO_IDX['collider']] = np.inf\n    asv[:, TOPO_IDX['mbias']] = np.inf\n\n    for topo in RANK_TOPOS:\n        if topo in PROTECTIVE:\n            continue\n        ss = all_ss[topo]\n        tau_true = all_tau_true[topo]\n        if topo == 'iv':\n            vals = process_batch_iv(C0_batch, ss, tau_true)\n        elif topo == 'exposure':\n            vals, _ = process_batch_exposure(C0_batch, ss, tau_true)\n        else:\n            vals, _ = process_batch_with_T(C0_batch, ss, tau_true, topo)\n        asv[:, TOPO_IDX[topo]] = vals\n    return asv\n\n\ndef partition_from_asv(asv_row):\n    \"\"\"Bottom-2 topologies (smallest ASV) form the fragile set.\"\"\"\n    order = np.argsort(asv_row, kind='stable')\n    return frozenset(RANK_TOPOS[i] for i in order[:2])\n\n\ndef spearman_versus_truth(asv_boot, asv_true):\n    \"\"\"Spearman rho between bootstrap ASV ranking and truth ranking.\"\"\"\n    # Handle infinities: replace +inf with large finite via rank ordering.\n    # scipy.spearmanr is OK with finite inputs; rankdata handles infinities.\n    r_true = rankdata(asv_true)\n    r_boot = rankdata(asv_boot)\n    # If all values are identical (or all inf), correlation undefined → NaN\n    if np.all(r_true == r_true[0]) or np.all(r_boot == r_boot[0]):\n        return np.nan\n    rho, _ = spearmanr(r_true, r_boot)\n    return rho\n\n\ndef main():\n    t_total = time.time()\n    print('Ĉ Estimation Robustness Experiment')\n    print(f'  K={K}, B={B_BOOT}, n_gold ∈ {N_GOLD_GRID}')\n    print(f'  Topologies: {RANK_TOPOS}')\n    print(f'  ASV threshold (magnitude): {ASV_EPSILON}')\n    print(f'  n_delta = {N_DELTA}')\n    print('=' * 70)\n    sys.stdout.flush()\n\n    # Precompute analytic sufficient statistics + tau_true\n    print('\\nPrecomputing sufficient statistics & tau_true...')\n    all_ss = {}\n    all_tau_true = {}\n    for topo in ALL_TOPOS:\n        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])\n        all_ss[topo] = ss\n        all_tau_true[topo] = get_tau_true(topo, ss)\n        print(f'  {topo:<12} tau_true = {all_tau_true[topo]:.6f}')\n    sys.stdout.flush()\n\n    # Load empirical K=3 matrices\n    print('\\nLoading empirical K=3 confusion matrices...')\n    Cs = load_k3_matrices()\n    print(f'  Loaded {len(Cs)} K=3 matrices')\n    for name in Cs:\n        print(f'    {name}  diag={np.diag(Cs[name]).round(3).tolist()}')\n    sys.stdout.flush()\n\n    # Truth ASV per source C\n    print('\\nComputing ASV for the truth Cs...')\n    truth_C_batch = np.stack(list(Cs.values()))\n    truth_asv = compute_asv_for_matrices(truth_C_batch, all_ss, all_tau_true)\n    truth_partition = {}\n    truth_asv_dict = {}\n    for i, name in enumerate(Cs):\n        truth_partition[name] = partition_from_asv(truth_asv[i])\n        truth_asv_dict[name] = {\n            RANK_TOPOS[j]: (None if np.isinf(truth_asv[i, j])\n                            else float(truth_asv[i, j]))\n            for j in range(len(RANK_TOPOS))\n        }\n        eq = 'YES' if truth_partition[name] == FRAGILE else 'NO'\n        print(f'  {name}  fragile-set={sorted(truth_partition[name])}  '\n              f'matches canonical: {eq}')\n    sys.stdout.flush()\n\n    # Bootstrap loop\n    print(f'\\nBootstrapping (B={B_BOOT})...')\n    rng = np.random.default_rng(SEED)\n\n    results_per_n = {}\n    for n_gold in N_GOLD_GRID:\n        t0 = time.time()\n        partition_match_total = 0   # vs canonical {exposure,iv}\n        partition_match_truth = 0   # vs source-C truth partition\n        n_bootstraps_total = 0\n        rho_values_vs_truth = []\n        rho_values_vs_theoretical_safe = []\n\n        # Per-source-C aggregates\n        per_C = {}\n\n        for name, C_true in Cs.items():\n            boot = bootstrap_chats(C_true, n_gold, B_BOOT, rng)\n            asv_boot = compute_asv_for_matrices(\n                boot, all_ss, all_tau_true)  # (B, n_topo)\n\n            truth_row = truth_asv[list(Cs).index(name)]\n\n            n_match_canon = 0\n            n_match_truth = 0\n            rho_vs_truth = []\n            for b in range(B_BOOT):\n                part = partition_from_asv(asv_boot[b])\n                if part == FRAGILE:\n                    n_match_canon += 1\n                if part == truth_partition[name]:\n                    n_match_truth += 1\n                rho_vs_truth.append(\n                    spearman_versus_truth(asv_boot[b], truth_row))\n\n            rho_vs_truth = np.array(rho_vs_truth, dtype=float)\n            rho_clean = rho_vs_truth[~np.isnan(rho_vs_truth)]\n\n            per_C[name] = {\n                'partition_match_canonical': n_match_canon / B_BOOT,\n                'partition_match_truth_C': n_match_truth / B_BOOT,\n                'spearman_rho_mean_vs_truth':\n                    float(rho_clean.mean()) if rho_clean.size else float('nan'),\n                'spearman_rho_median_vs_truth':\n                    float(np.median(rho_clean)) if rho_clean.size else float('nan'),\n                'spearman_rho_q25_vs_truth':\n                    float(np.quantile(rho_clean, 0.25)) if rho_clean.size else float('nan'),\n                'truth_partition_matches_canonical':\n                    truth_partition[name] == FRAGILE,\n            }\n\n            partition_match_total += n_match_canon\n            partition_match_truth += n_match_truth\n            n_bootstraps_total += B_BOOT\n            rho_values_vs_truth.extend(rho_clean.tolist())\n\n        results_per_n[n_gold] = {\n            'n_bootstraps_total': n_bootstraps_total,\n            'partition_stability_rate_vs_canonical':\n                partition_match_total / n_bootstraps_total,\n            'partition_stability_rate_vs_truth_C':\n                partition_match_truth / n_bootstraps_total,\n            'spearman_rho_mean':\n                float(np.mean(rho_values_vs_truth)) if rho_values_vs_truth\n                else float('nan'),\n            'spearman_rho_median':\n                float(np.median(rho_values_vs_truth)) if rho_values_vs_truth\n                else float('nan'),\n            'spearman_rho_q25':\n                float(np.quantile(rho_values_vs_truth, 0.25))\n                if rho_values_vs_truth else float('nan'),\n            'spearman_rho_q75':\n                float(np.quantile(rho_values_vs_truth, 0.75))\n                if rho_values_vs_truth else float('nan'),\n            'per_source_C': per_C,\n        }\n        elapsed = time.time() - t0\n        r = results_per_n[n_gold]\n        print(f'  n_gold={n_gold:<4}  '\n              f'partition_rate_canonical={r[\"partition_stability_rate_vs_canonical\"]:.4f}  '\n              f'partition_rate_truth={r[\"partition_stability_rate_vs_truth_C\"]:.4f}  '\n              f'rho_mean={r[\"spearman_rho_mean\"]:.4f}  '\n              f'({elapsed:.1f}s)')\n        sys.stdout.flush()\n\n    # Summary\n    print('\\n' + '=' * 70)\n    print('Summary')\n    print('=' * 70)\n    print(f'{\"n_gold\":<8}{\"part_canon\":<14}{\"part_truth\":<14}'\n          f'{\"rho_mean\":<12}{\"rho_median\":<12}')\n    for n_gold in N_GOLD_GRID:\n        r = results_per_n[n_gold]\n        print(f'{n_gold:<8}'\n              f'{r[\"partition_stability_rate_vs_canonical\"]:<14.4f}'\n              f'{r[\"partition_stability_rate_vs_truth_C\"]:<14.4f}'\n              f'{r[\"spearman_rho_mean\"]:<12.4f}'\n              f'{r[\"spearman_rho_median\"]:<12.4f}')\n\n    # Save\n    total_time = time.time() - t_total\n    out = {\n        'description': ('Ĉ estimation robustness under multinomial bootstrap'\n                        ' from finite gold set'),\n        'config': {\n            'K': K,\n            'n_gold_grid': N_GOLD_GRID,\n            'B_bootstrap': B_BOOT,\n            'seed': SEED,\n            'asv_threshold': ASV_EPSILON,\n            'n_delta': N_DELTA,\n            'topologies': RANK_TOPOS,\n            'canonical_safe': sorted(SAFE),\n            'canonical_fragile': sorted(FRAGILE),\n            'empirical_path': EMP_PATH,\n        },\n        'source_matrices': {\n            name: {\n                'C': Cs[name].tolist(),\n                'diag': np.diag(Cs[name]).tolist(),\n                'truth_asv': truth_asv_dict[name],\n                'truth_fragile_set': sorted(truth_partition[name]),\n                'truth_matches_canonical':\n                    truth_partition[name] == FRAGILE,\n            }\n            for name in Cs\n        },\n        'results_per_n_gold': {\n            str(n): results_per_n[n] for n in N_GOLD_GRID\n        },\n        'total_time_seconds': total_time,\n    }\n    with open(OUT_PATH, 'w') as f:\n        json.dump(out, f, indent=2)\n    print(f'\\nJSON saved: {OUT_PATH}')\n    print(f'Total: {total_time:.1f}s')\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "f4f85847-07c9-4ae8-8fe2-3da2b28b569b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Fas7qaCV5phETnAaRfrGXo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 75104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1394
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-23T14:54:52.790Z_

<details><summary>↩ Tool result · `toolu_0154bqUogNKJ5YjUrpXgNNHZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "c73dc458-375e-4cd9-bec7-0fcab5bfbb67",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nĈ Estimation Robustness Experiment.\n\nQuestion: With a finite K-class gold-labelled set used to estimate C, does\nthe safe/fragile topology partition (5 vs 2) hold under multinomial bootstrap\nof Ĉ?\n\nFor each empirical column-stochastic K=3 confusion matrix C (LLM truth),\ndraw B bootstrap replicates Ĉ ~ multinomial(C[:,k] · n_gold) / n_gold for\neach class k. For each Ĉ, recompute the magnitude ASV δ* for the 7\ntopologies (confounding, mediation, collider, exposure, mbias, IV,\nfrontdoor) and report:\n\n  • Partition stability rate vs n_gold: fraction of bootstraps where the\n    two lowest-ASV topologies equal {exposure, IV}.\n  • Spearman ρ vs n_gold: rank correlation between ASV ranking from Ĉ and\n    from true C (averaged over bootstraps and source matrices).\n\nEmpirical Cs come from artifacts/updated_empirical_results.json (23 LLM\nmatrices; 8 are K=3 vast/stance — the K=3 framework subset).\n\nOutput: c_estimation_robustness_results.json next to this script.\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nfrom collections import defaultdict\n\nimport numpy as np\nfrom scipy.stats import rankdata, spearmanr\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n\nfrom ranking_stability import (  # noqa: E402\n    ALL_TOPOS, COMPUTE_SS, DGP_PARAMS, K, N_DELTA, DELTAS, ASV_EPSILON,\n    PROTECTIVE, get_tau_true, process_batch_iv, process_batch_exposure,\n    process_batch_with_T,\n)\n\n# ──────────────────────────────────────────────────────────────────────────\nEMP_PATH = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json'\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_PATH = os.path.join(OUT_DIR, 'c_estimation_robustness_results.json')\n\nN_GOLD_GRID = [50, 100, 200, 500]\nB_BOOT = 200\nSEED = 20260523\nSAFE = {'confounding', 'mediation', 'collider', 'frontdoor', 'mbias'}\nFRAGILE = {'exposure', 'iv'}\nRANK_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\nTOPO_IDX = {t: i for i, t in enumerate(RANK_TOPOS)}\n\n\ndef load_k3_matrices():\n    with open(EMP_PATH) as f:\n        d = json.load(f)\n    out = {}\n    for name, cm in d['confusion_matrices'].items():\n        arr = np.asarray(cm, dtype=float)\n        if arr.shape == (K, K):\n            # Re-normalise columns just in case\n            cs = arr.sum(axis=0, keepdims=True)\n            cs = np.where(cs < 1e-12, 1.0, cs)\n            out[name] = arr / cs\n    return out\n\n\ndef bootstrap_chats(C_true, n_gold, B, rng):\n    \"\"\"Multinomial bootstrap of Ĉ.\n\n    For each class k, draw n_gold predictions from C_true[:, k] then\n    normalise. Returns (B, K, K) array of column-stochastic matrices.\n    \"\"\"\n    out = np.empty((B, K, K))\n    for k in range(K):\n        # rng.multinomial returns (B, K) with each row summing to n_gold\n        counts = rng.multinomial(n_gold, C_true[:, k], size=B)\n        out[:, :, k] = counts / float(n_gold)\n    return out\n\n\ndef compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):\n    \"\"\"Compute magnitude ASV per topology for a batch of C0 matrices.\n\n    Returns asv: (M, n_topo) ndarray. Collider/M-bias get +inf (protective).\n    \"\"\"\n    M = C0_batch.shape[0]\n    n_topo = len(RANK_TOPOS)\n    asv = np.full((M, n_topo), np.nan)\n    # Protective topologies: always inf\n    asv[:, TOPO_IDX['collider']] = np.inf\n    asv[:, TOPO_IDX['mbias']] = np.inf\n\n    for topo in RANK_TOPOS:\n        if topo in PROTECTIVE:\n            continue\n        ss = all_ss[topo]\n        tau_true = all_tau_true[topo]\n        if topo == 'iv':\n            vals = process_batch_iv(C0_batch, ss, tau_true)\n        elif topo == 'exposure':\n            vals, _ = process_batch_exposure(C0_batch, ss, tau_true)\n        else:\n            vals, _ = process_batch_with_T(C0_batch, ss, tau_true, topo)\n        asv[:, TOPO_IDX[topo]] = vals\n    return asv\n\n\ndef partition_from_asv(asv_row):\n    \"\"\"Bottom-2 topologies (smallest ASV) form the fragile set.\"\"\"\n    order = np.argsort(asv_row, kind='stable')\n    return frozenset(RANK_TOPOS[i] for i in order[:2])\n\n\ndef spearman_versus_truth(asv_boot, asv_true):\n    \"\"\"Spearman rho between bootstrap ASV ranking and truth ranking.\"\"\"\n    # Handle infinities: replace +inf with large finite via rank ordering.\n    # scipy.spearmanr is OK with finite inputs; rankdata handles infinities.\n    r_true = rankdata(asv_true)\n    r_boot = rankdata(asv_boot)\n    # If all values are identical (or all inf), correlation undefined → NaN\n    if np.all(r_true == r_true[0]) or np.all(r_boot == r_boot[0]):\n        return np.nan\n    rho, _ = spearmanr(r_true, r_boot)\n    return rho\n\n\ndef main():\n    t_total = time.time()\n    print('Ĉ Estimation Robustness Experiment')\n    print(f'  K={K}, B={B_BOOT}, n_gold ∈ {N_GOLD_GRID}')\n    print(f'  Topologies: {RANK_TOPOS}')\n    print(f'  ASV threshold (magnitude): {ASV_EPSILON}')\n    print(f'  n_delta = {N_DELTA}')\n    print('=' * 70)\n    sys.stdout.flush()\n\n    # Precompute analytic sufficient statistics + tau_true\n    print('\\nPrecomputing sufficient statistics & tau_true...')\n    all_ss = {}\n    all_tau_true = {}\n    for topo in ALL_TOPOS:\n        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])\n        all_ss[topo] = ss\n        all_tau_true[topo] = get_tau_true(topo, ss)\n        print(f'  {topo:<12} tau_true = {all_tau_true[topo]:.6f}')\n    sys.stdout.flush()\n\n    # Load empirical K=3 matrices\n    print('\\nLoading empirical K=3 confusion matrices...')\n    Cs = load_k3_matrices()\n    print(f'  Loaded {len(Cs)} K=3 matrices')\n    for name in Cs:\n        print(f'    {name}  diag={np.diag(Cs[name]).round(3).tolist()}')\n    sys.stdout.flush()\n\n    # Truth ASV per source C\n    print('\\nComputing ASV for the truth Cs...')\n    truth_C_batch = np.stack(list(Cs.values()))\n    truth_asv = compute_asv_for_matrices(truth_C_batch, all_ss, all_tau_true)\n    truth_partition = {}\n    truth_asv_dict = {}\n    for i, name in enumerate(Cs):\n        truth_partition[name] = partition_from_asv(truth_asv[i])\n        truth_asv_dict[name] = {\n            RANK_TOPOS[j]: (None if np.isinf(truth_asv[i, j])\n                            else float(truth_asv[i, j]))\n            for j in range(len(RANK_TOPOS))\n        }\n        eq = 'YES' if truth_partition[name] == FRAGILE else 'NO'\n        print(f'  {name}  fragile-set={sorted(truth_partition[name])}  '\n              f'matches canonical: {eq}')\n    sys.stdout.flush()\n\n    # Bootstrap loop\n    print(f'\\nBootstrapping (B={B_BOOT})...')\n    rng = np.random.default_rng(SEED)\n\n    results_per_n = {}\n    for n_gold in N_GOLD_GRID:\n        t0 = time.time()\n        partition_match_total = 0   # vs canonical {exposure,iv}\n        partition_match_truth = 0   # vs source-C truth partition\n        n_bootstraps_total = 0\n        rho_values_vs_truth = []\n        rho_values_vs_theoretical_safe = []\n\n        # Per-source-C aggregates\n        per_C = {}\n\n        for name, C_true in Cs.items():\n            boot = bootstrap_chats(C_true, n_gold, B_BOOT, rng)\n            asv_boot = compute_asv_for_matrices(\n                boot, all_ss, all_tau_true)  # (B, n_topo)\n\n            truth_row = truth_asv[list(Cs).index(name)]\n\n            n_match_canon = 0\n            n_match_truth = 0\n            rho_vs_truth = []\n            for b in range(B_BOOT):\n                part = partition_from_asv(asv_boot[b])\n                if part == FRAGILE:\n                    n_match_canon += 1\n                if part == truth_partition[name]:\n                    n_match_truth += 1\n                rho_vs_truth.append(\n                    spearman_versus_truth(asv_boot[b], truth_row))\n\n            rho_vs_truth = np.array(rho_vs_truth, dtype=float)\n            rho_clean = rho_vs_truth[~np.isnan(rho_vs_truth)]\n\n            per_C[name] = {\n                'partition_match_canonical': n_match_canon / B_BOOT,\n                'partition_match_truth_C': n_match_truth / B_BOOT,\n                'spearman_rho_mean_vs_truth':\n                    float(rho_clean.mean()) if rho_clean.size else float('nan'),\n                'spearman_rho_median_vs_truth':\n                    float(np.median(rho_clean)) if rho_clean.size else float('nan'),\n                'spearman_rho_q25_vs_truth':\n                    float(np.quantile(rho_clean, 0.25)) if rho_clean.size else float('nan'),\n                'truth_partition_matches_canonical':\n                    truth_partition[name] == FRAGILE,\n            }\n\n            partition_match_total += n_match_canon\n            partition_match_truth += n_match_truth\n            n_bootstraps_total += B_BOOT\n            rho_values_vs_truth.extend(rho_clean.tolist())\n\n        results_per_n[n_gold] = {\n            'n_bootstraps_total': n_bootstraps_total,\n            'partition_stability_rate_vs_canonical':\n                partition_match_total / n_bootstraps_total,\n            'partition_stability_rate_vs_truth_C':\n                partition_match_truth / n_bootstraps_total,\n            'spearman_rho_mean':\n                float(np.mean(rho_values_vs_truth)) if rho_values_vs_truth\n                else float('nan'),\n            'spearman_rho_median':\n                float(np.median(rho_values_vs_truth)) if rho_values_vs_truth\n                else float('nan'),\n            'spearman_rho_q25':\n                float(np.quantile(rho_values_vs_truth, 0.25))\n                if rho_values_vs_truth else float('nan'),\n            'spearman_rho_q75':\n                float(np.quantile(rho_values_vs_truth, 0.75))\n                if rho_values_vs_truth else float('nan'),\n            'per_source_C': per_C,\n        }\n        elapsed = time.time() - t0\n        r = results_per_n[n_gold]\n        print(f'  n_gold={n_gold:<4}  '\n              f'partition_rate_canonical={r[\"partition_stability_rate_vs_canonical\"]:.4f}  '\n              f'partition_rate_truth={r[\"partition_stability_rate_vs_truth_C\"]:.4f}  '\n              f'rho_mean={r[\"spearman_rho_mean\"]:.4f}  '\n              f'({elapsed:.1f}s)')\n        sys.stdout.flush()\n\n    # Summary\n    print('\\n' + '=' * 70)\n    print('Summary')\n    print('=' * 70)\n    print(f'{\"n_gold\":<8}{\"part_canon\":<14}{\"part_truth\":<14}'\n          f'{\"rho_mean\":<12}{\"rho_median\":<12}')\n    for n_gold in N_GOLD_GRID:\n        r = results_per_n[n_gold]\n        print(f'{n_gold:<8}'\n              f'{r[\"partition_stability_rate_vs_canonical\"]:<14.4f}'\n              f'{r[\"partition_stability_rate_vs_truth_C\"]:<14.4f}'\n              f'{r[\"spearman_rho_mean\"]:<12.4f}'\n              f'{r[\"spearman_rho_median\"]:<12.4f}')\n\n    # Save\n    total_time = time.time() - t_total\n    out = {\n        'description': ('Ĉ estimation robustness under multinomial bootstrap'\n                        ' from finite gold set'),\n        'config': {\n            'K': K,\n            'n_gold_grid': N_GOLD_GRID,\n            'B_bootstrap': B_BOOT,\n            'seed': SEED,\n            'asv_threshold': ASV_EPSILON,\n            'n_delta': N_DELTA,\n            'topologies': RANK_TOPOS,\n            'canonical_safe': sorted(SAFE),\n            'canonical_fragile': sorted(FRAGILE),\n            'empirical_path': EMP_PATH,\n        },\n        'source_matrices': {\n            name: {\n                'C': Cs[name].tolist(),\n                'diag': np.diag(Cs[name]).tolist(),\n                'truth_asv': truth_asv_dict[name],\n                'truth_fragile_set': sorted(truth_partition[name]),\n                'truth_matches_canonical':\n                    truth_partition[name] == FRAGILE,\n            }\n            for name in Cs\n        },\n        'results_per_n_gold': {\n            str(n): results_per_n[n] for n in N_GOLD_GRID\n        },\n        'total_time_seconds': total_time,\n    }\n    with open(OUT_PATH, 'w') as f:\n        json.dump(out, f, indent=2)\n    print(f'\\nJSON saved: {OUT_PATH}')\n    print(f'Total: {total_time:.1f}s')\n\n\nif __name__ == '__main__':\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01CpvdaXmxcicJLkpSniZHF1`</summary>

```json
{
  "command": "timeout 600 python3 artifacts/c_estimation_robustness.py 2>&1 | tail -80",
  "description": "Run c_estimation_robustness.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "3d12dc80-25b3-49a0-99ef-d3c17d5a1654",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WffRkg95mWQJvSk2ZQYVJ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5446,
      "cache_read_input_tokens": 76498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5446
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bymriiocr",
  "tool_use_id": "toolu_01CpvdaXmxcicJLkpSniZHF1",
  "description": "Run c_estimation_robustness.py",
  "task_type": "local_bash",
  "uuid": "59d17ca0-bec4-45d6-bcb6-eb2e3b49a4fe",
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd"
}
```

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bymriiocr",
  "tool_use_id": "toolu_01CpvdaXmxcicJLkpSniZHF1",
  "status": "completed",
  "output_file": "",
  "summary": "Run c_estimation_robustness.py",
  "uuid": "e51961d1-3045-4cba-9130-0ac931078aa5",
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd"
}
```

---

### Tool result

_source line 57 · 2026-05-23T14:55:13.376Z_

<details><summary>↩ Tool result · `toolu_01CpvdaXmxcicJLkpSniZHF1`</summary>

```text
Ĉ Estimation Robustness Experiment
  K=3, B=200, n_gold ∈ [50, 100, 200, 500]
  Topologies: ['confounding', 'mediation', 'collider', 'exposure', 'mbias', 'iv', 'frontdoor']
  ASV threshold (magnitude): 0.05
  n_delta = 201
======================================================================

Precomputing sufficient statistics & tau_true...
  confounding  tau_true = 2.000000
  mediation    tau_true = 0.500000
  collider     tau_true = 1.000000
  exposure     tau_true = 1.000000
  mbias        tau_true = 1.000000
  iv           tau_true = 1.333121
  frontdoor    tau_true = 0.500000

Loading empirical K=3 confusion matrices...
  Loaded 8 K=3 matrices
    vast_deepseek_few-shot-3  diag=[0.514, 0.798, 0.161]
    vast_deepseek_few-shot-5  diag=[0.527, 0.785, 0.153]
    vast_llama4_few-shot-3  diag=[0.66, 0.8, 0.036]
    vast_llama4_zero-shot  diag=[0.678, 0.841, 0.046]
    vast_qwen2.5-7b_few-shot-3  diag=[0.413, 0.821, 0.125]
    vast_qwen2.5-7b_few-shot-5  diag=[0.475, 0.776, 0.125]
    vast_qwen2.5-7b_zero-shot  diag=[0.461, 0.847, 0.11]
    vast_qwen3_zero-shot  diag=[0.686, 0.775, 0.074]

Computing ASV for the truth Cs...
  vast_deepseek_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_deepseek_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_llama4_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_llama4_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen2.5-7b_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen2.5-7b_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen2.5-7b_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen3_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES

Bootstrapping (B=200)...
  n_gold=50    partition_rate_canonical=0.5044  partition_rate_truth=0.5044  rho_mean=0.8573  (4.0s)
  n_gold=100   partition_rate_canonical=0.8200  partition_rate_truth=0.8200  rho_mean=0.9932  (4.1s)
  n_gold=200   partition_rate_canonical=0.8556  partition_rate_truth=0.8556  rho_mean=0.9950  (4.0s)
  n_gold=500   partition_rate_canonical=0.8850  partition_rate_truth=0.8850  rho_mean=0.9962  (3.8s)

======================================================================
Summary
======================================================================
n_gold  part_canon    part_truth    rho_mean    rho_median  
50      0.5044        0.5044        0.8573      0.9909      
100     0.8200        0.8200        0.9932      1.0000      
200     0.8556        0.8556        0.9950      1.0000      
500     0.8850        0.8850        0.9962      1.0000      

JSON saved: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json
Total: 15.9s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "74fc6c5e-3e8b-47f6-ad57-9e736279d25e",
  "tool_use_result": {
    "stdout": "Ĉ Estimation Robustness Experiment\n  K=3, B=200, n_gold ∈ [50, 100, 200, 500]\n  Topologies: ['confounding', 'mediation', 'collider', 'exposure', 'mbias', 'iv', 'frontdoor']\n  ASV threshold (magnitude): 0.05\n  n_delta = 201\n======================================================================\n\nPrecomputing sufficient statistics & tau_true...\n  confounding  tau_true = 2.000000\n  mediation    tau_true = 0.500000\n  collider     tau_true = 1.000000\n  exposure     tau_true = 1.000000\n  mbias        tau_true = 1.000000\n  iv           tau_true = 1.333121\n  frontdoor    tau_true = 0.500000\n\nLoading empirical K=3 confusion matrices...\n  Loaded 8 K=3 matrices\n    vast_deepseek_few-shot-3  diag=[0.514, 0.798, 0.161]\n    vast_deepseek_few-shot-5  diag=[0.527, 0.785, 0.153]\n    vast_llama4_few-shot-3  diag=[0.66, 0.8, 0.036]\n    vast_llama4_zero-shot  diag=[0.678, 0.841, 0.046]\n    vast_qwen2.5-7b_few-shot-3  diag=[0.413, 0.821, 0.125]\n    vast_qwen2.5-7b_few-shot-5  diag=[0.475, 0.776, 0.125]\n    vast_qwen2.5-7b_zero-shot  diag=[0.461, 0.847, 0.11]\n    vast_qwen3_zero-shot  diag=[0.686, 0.775, 0.074]\n\nComputing ASV for the truth Cs...\n  vast_deepseek_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_deepseek_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_llama4_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_llama4_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen2.5-7b_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen2.5-7b_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen2.5-7b_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen3_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES\n\nBootstrapping (B=200)...\n  n_gold=50    partition_rate_canonical=0.5044  partition_rate_truth=0.5044  rho_mean=0.8573  (4.0s)\n  n_gold=100   partition_rate_canonical=0.8200  partition_rate_truth=0.8200  rho_mean=0.9932  (4.1s)\n  n_gold=200   partition_rate_canonical=0.8556  partition_rate_truth=0.8556  rho_mean=0.9950  (4.0s)\n  n_gold=500   partition_rate_canonical=0.8850  partition_rate_truth=0.8850  rho_mean=0.9962  (3.8s)\n\n======================================================================\nSummary\n======================================================================\nn_gold  part_canon    part_truth    rho_mean    rho_median  \n50      0.5044        0.5044        0.8573      0.9909      \n100     0.8200        0.8200        0.9932      1.0000      \n200     0.8556        0.8556        0.9950      1.0000      \n500     0.8850        0.8850        0.9962      1.0000      \n\nJSON saved: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json\nTotal: 15.9s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01F5JDSP1VngtUWrSvQFF7Ku`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json') as f:\n    d = json.load(f)\nprint('Top keys:', list(d.keys()))\nprint('Source matrices:', len(d['source_matrices']))\nprint('n_gold keys:', list(d['results_per_n_gold'].keys()))\nprint()\nprint('Sample per_n_gold[50]:')\nr = d['results_per_n_gold']['50']\nfor k, v in r.items():\n    if k != 'per_source_C':\n        print(f'  {k}: {v}')\nprint(f'  per_source_C: {len(r[\\\"per_source_C\\\"])} entries')\n\"\n",
  "description": "Validate JSON contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "c16d5250-305e-4ba6-a329-d7afeffeae15",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WFSWMwnW8tR8ocjrAZsC1i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1530,
      "cache_read_input_tokens": 81944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1530
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-23T14:55:18.291Z_

<details><summary>↩ Tool result · `toolu_01F5JDSP1VngtUWrSvQFF7Ku`</summary>

```text
Top keys: ['description', 'config', 'source_matrices', 'results_per_n_gold', 'total_time_seconds']
Source matrices: 8
n_gold keys: ['50', '100', '200', '500']

Sample per_n_gold[50]:
  n_bootstraps_total: 1600
  partition_stability_rate_vs_canonical: 0.504375
  partition_stability_rate_vs_truth_C: 0.504375
  spearman_rho_mean: 0.8572827199901789
  spearman_rho_median: 0.9908673886137246
  spearman_rho_q25: 0.7888259403211363
  spearman_rho_q75: 1.0
  per_source_C: 8 entries
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "a3be051e-e87d-46f2-be5a-7ea7eb9715c7",
  "tool_use_result": {
    "stdout": "Top keys: ['description', 'config', 'source_matrices', 'results_per_n_gold', 'total_time_seconds']\nSource matrices: 8\nn_gold keys: ['50', '100', '200', '500']\n\nSample per_n_gold[50]:\n  n_bootstraps_total: 1600\n  partition_stability_rate_vs_canonical: 0.504375\n  partition_stability_rate_vs_truth_C: 0.504375\n  spearman_rho_mean: 0.8572827199901789\n  spearman_rho_median: 0.9908673886137246\n  spearman_rho_q25: 0.7888259403211363\n  spearman_rho_q75: 1.0\n  per_source_C: 8 entries",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01LtrDcxLr75geTZGA4sUKmH`</summary>

```json
{
  "todos": [
    {
      "content": "Locate empirical LLM confusion matrices",
      "activeForm": "Locating empirical LLM confusion matrices",
      "status": "completed"
    },
    {
      "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
      "activeForm": "Designing c_estimation_robustness.py",
      "status": "completed"
    },
    {
      "content": "Run script and validate JSON output",
      "activeForm": "Running script and validating JSON output",
      "status": "completed"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "5164c034-52b7-4e68-949c-89cd9665f894",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012uiQHVLnzUicS3UDvWHXb3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 83474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 601
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-23T14:55:29.341Z_

<details><summary>↩ Tool result · `toolu_01LtrDcxLr75geTZGA4sUKmH`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "2bf838fd-f649-49d1-a24d-0716521b5ec9",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Locate empirical LLM confusion matrices",
        "status": "completed",
        "activeForm": "Locating empirical LLM confusion matrices"
      },
      {
        "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
        "status": "in_progress",
        "activeForm": "Designing c_estimation_robustness.py"
      },
      {
        "content": "Run script and validate JSON output",
        "status": "pending",
        "activeForm": "Running script and validating JSON output"
      }
    ],
    "newTodos": [
      {
        "content": "Locate empirical LLM confusion matrices",
        "status": "completed",
        "activeForm": "Locating empirical LLM confusion matrices"
      },
      {
        "content": "Design c_estimation_robustness.py with bootstrap of Ĉ",
        "status": "completed",
        "activeForm": "Designing c_estimation_robustness.py"
      },
      {
        "content": "Run script and validate JSON output",
        "status": "completed",
        "activeForm": "Running script and validating JSON output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 62_

完成。

**产出**：
- 脚本：`artifacts/c_estimation_robustness.py`
- 结果：`artifacts/c_estimation_robustness_results.json`

**数据范围**：23 个 LLM 矩阵中只有 8 个是 K=3（vast 数据集），与论文的 K=3 DGP 框架直接兼容。K=2 (7) 和 K=10 (8) 跳过。

**关键结果**（每个 source C × 200 bootstrap = 1600 ASV）：

| n_gold | partition stability rate | Spearman ρ mean | ρ median |
|--------|------|------|------|
| 50  | 0.504 | 0.857 | 0.991 |
| 100 | 0.820 | 0.993 | 1.000 |
| 200 | 0.856 | 0.995 | 1.000 |
| 500 | 0.885 | 0.996 | 1.000 |

**解读**：
- 全部 8 个 truth C 都满足 fragile = {exposure, IV} 的 canonical partition
- n_gold≥100 时 partition 稳定率 >82%，ρ_median = 1.0
- n_gold=50 时 ρ_mean 显著低于 1（0.857），表明小样本下 ASV 排名抖动较大，但 median 仍≈1（少数 bootstrap 严重偏离把均值拉低）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "uuid": "ee3bcf7f-df17-4652-886b-d93ad4efa02e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FHbWphcstsJhk3JZRXRKSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 84075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 63_

完成。

**产出**：
- 脚本：`artifacts/c_estimation_robustness.py`
- 结果：`artifacts/c_estimation_robustness_results.json`

**数据范围**：23 个 LLM 矩阵中只有 8 个是 K=3（vast 数据集），与论文的 K=3 DGP 框架直接兼容。K=2 (7) 和 K=10 (8) 跳过。

**关键结果**（每个 source C × 200 bootstrap = 1600 ASV）：

| n_gold | partition stability rate | Spearman ρ mean | ρ median |
|--------|------|------|------|
| 50  | 0.504 | 0.857 | 0.991 |
| 100 | 0.820 | 0.993 | 1.000 |
| 200 | 0.856 | 0.995 | 1.000 |
| 500 | 0.885 | 0.996 | 1.000 |

**解读**：
- 全部 8 个 truth C 都满足 fragile = {exposure, IV} 的 canonical partition
- n_gold≥100 时 partition 稳定率 >82%，ρ_median = 1.0
- n_gold=50 时 ρ_mean 显著低于 1（0.857），表明小样本下 ASV 排名抖动较大，但 median 仍≈1（少数 bootstrap 严重偏离把均值拉低）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 216468,
  "duration_api_ms": 198804,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "8f806b72-4882-41d0-a7bc-d34a5c3148dd",
  "total_cost_usd": 1.6286157499999998,
  "usage": {
    "input_tokens": 31,
    "cache_creation_input_tokens": 107409,
    "cache_read_input_tokens": 1225097,
    "output_tokens": 13729,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 107409,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 472,
        "cache_read_input_tokens": 84075,
        "cache_creation_input_tokens": 282,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 282
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1276,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001381,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 31,
      "outputTokens": 13729,
      "cacheReadInputTokens": 1225097,
      "cacheCreationInputTokens": 107409,
      "webSearchRequests": 0,
      "costUSD": 1.6272347499999997,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a0278aee-5268-4cb3-b157-39478db057d6"
}
```

</details>

---
