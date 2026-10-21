# exp mf1a adversarial monotonicity

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_exp_mf1a_adversarial_monotonicity_20260523T173639.log`
- **Structured JSON:** [`d96ca865f0588170fee8.json`](../../sessions/d9/d96ca865f0588170fee8.json)

## Before a recorded user message

32 recorded events

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
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
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
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
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
  "uuid": "542edff8-2e2f-438c-80cb-16cbc592177c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "resetsAt": 1779570000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b65b4ad9-d60b-472e-aae2-413cf32139c5",
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant source files to understand the API and existing implementations before writing the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "b4edc0ca-16c7-4f99-ac1f-73ed2efdebd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFoRszrSp3GrL9usiTMzdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14739,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14739
      },
      "output_tokens": 25,
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

### Assistant

_source line 5_

I'll read the bias computation API and reference scripts to understand the implementation patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "0db33acf-6713-4ba5-b91d-7c65498f2425",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFoRszrSp3GrL9usiTMzdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14739,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14739
      },
      "output_tokens": 25,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01BWm4kz1mfKy2b3YTyVxrko`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "8451da06-cab0-4396-a708-eff4ad15bf36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFoRszrSp3GrL9usiTMzdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14739,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14739
      },
      "output_tokens": 25,
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

_source line 7 · 2026-05-23T17:36:52.051Z_

<details><summary>↩ Tool result · `toolu_01BWm4kz1mfKy2b3YTyVxrko`</summary>

```text
1	"""Compute annotation-error bias via probability limit calculations.
2	
3	Uses precomputed sufficient statistics from large-sample DGP simulations
4	to compute OLS plim as a function of confusion matrix C, avoiding MC.
5	"""
6	
7	import warnings
8	import numpy as np
9	from .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
10	from .confusion import validate_confusion_matrix
11	
12	_N_PRECOMP = 2_000_000
13	_precomp_cache = {}
14	
15	
16	def _params_key(params):
17	    items = []
18	    for k, v in sorted(params.items()):
19	        if isinstance(v, np.ndarray):
20	            items.append((k, tuple(v.flat)))
21	        else:
22	            items.append((k, v))
23	    return tuple(items)
24	
25	
26	def _precompute(topology, params, K, seed=999):
27	    """Precompute sufficient statistics for plim calculation."""
28	    cache_key = (topology, _params_key(params), K)
29	    if cache_key in _precomp_cache:
30	        return _precomp_cache[cache_key]
31	
32	    rng = np.random.default_rng(seed)
33	    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)
34	    Y = data["Y"]
35	    A = data["A"]
36	
37	    DA = np.zeros((_N_PRECOMP, K))
38	    for k in range(K):
39	        DA[:, k] = (A == k).astype(float)
40	
41	    stats = {
42	        "E_Y": Y.mean(),
43	        "E_DA": DA.mean(0),
44	        "E_DA_Y": (DA * Y[:, None]).mean(0),
45	    }
46	
47	    if topology in HAS_TREATMENT:
48	        T = data["T"]
49	        stats.update({
50	            "E_T": T.mean(),
51	            "E_T2": (T ** 2).mean(),
52	            "E_TY": (T * Y).mean(),
53	            "E_DA_T": (DA * T[:, None]).mean(0),
54	        })
55	
56	    if topology == "iv":
57	        Z = data["Z"]
58	        Zc = Z - Z.mean()
59	        var_Z = (Zc ** 2).mean()
60	        stats["RF"] = (Zc * (Y - Y.mean())).mean() / var_Z
61	        FS = np.zeros(K)
62	        for k in range(K):
63	            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z
64	        stats["FS"] = FS
65	
66	    _precomp_cache[cache_key] = stats
67	    return stats
68	
69	
70	def _plim_with_T(C, stats, K):
71	    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
72	    ds = C @ stats["E_DA"]
73	    dst = C @ stats["E_DA_T"]
74	    dsy = C @ stats["E_DA_Y"]
75	    ET, ET2 = stats["E_T"], stats["E_T2"]
76	    EY, ETY = stats["E_Y"], stats["E_TY"]
77	
78	    dim = 1 + K  # intercept + T + (K-1) dummies
79	    EZZ = np.zeros((dim, dim))
80	    EZZ[0, 0] = 1.0
81	    EZZ[0, 1] = EZZ[1, 0] = ET
82	    EZZ[1, 1] = ET2
83	    for j in range(1, K):
84	        idx = j + 1
85	        EZZ[0, idx] = EZZ[idx, 0] = ds[j]
86	        EZZ[1, idx] = EZZ[idx, 1] = dst[j]
87	        EZZ[idx, idx] = ds[j]
88	
89	    EZY = np.zeros(dim)
90	    EZY[0] = EY
91	    EZY[1] = ETY
92	    for j in range(1, K):
93	        EZY[j + 1] = dsy[j]
94	
95	    cond = np.linalg.cond(EZZ)
96	    if cond > 1e12:
97	        warnings.warn(
98	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
99	        )
100	
101	    return np.linalg.solve(EZZ, EZY)
102	
103	
104	def _plim_no_T(C, stats, K):
105	    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""
106	    ds = C @ stats["E_DA"]
107	    dsy = C @ stats["E_DA_Y"]
108	    EY = stats["E_Y"]
109	
110	    dim = K  # intercept + (K-1) dummies
111	    EZZ = np.zeros((dim, dim))
112	    EZZ[0, 0] = 1.0
113	    for j in range(1, K):
114	        EZZ[0, j] = EZZ[j, 0] = ds[j]
115	        EZZ[j, j] = ds[j]
116	
117	    EZY = np.zeros(dim)
118	    EZY[0] = EY
119	    for j in range(1, K):
120	        EZY[j] = dsy[j]
121	
122	    cond = np.linalg.cond(EZZ)
123	    if cond > 1e12:
124	        warnings.warn(
125	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
126	        )
127	
128	    return np.linalg.solve(EZZ, EZY)
129	
130	
131	def _plim_iv(C, stats, K):
132	    """Wald estimator plim: RF / (C @ FS)[1]."""
133	    FS_star = C @ stats["FS"]
134	    denom = FS_star[1]
135	    if abs(denom) < 1e-15:
136	        return np.nan
137	    return stats["RF"] / denom
138	
139	
140	def _get_tau(topology, C, stats, K):
141	    """Extract target coefficient from plim vector.
142	
143	    For IV: Wald estimator RF / (C @ FS)[1].
144	    For topologies with T: OLS coefficient index 1 (treatment effect).
145	    For topologies without T: OLS coefficient index 1 (first dummy).
146	    """
147	    if topology == "iv":
148	        return _plim_iv(C, stats, K)
149	    if topology in HAS_TREATMENT:
150	        coefs = _plim_with_T(C, stats, K)
151	    else:
152	        coefs = _plim_no_T(C, stats, K)
153	    return coefs[1]
154	
155	
156	def compute_bias(topology, C, params=None):
157	    """Compute annotation-error bias for a given topology and confusion matrix.
158	
159	    Args:
160	        topology: one of "confounding", "mediation", "collider", "exposure",
161	                  "mbias", "iv", "frontdoor"
162	        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
163	        params: optional DGP parameters dict, None uses defaults
164	
165	    Returns:
166	        dict with tau_true, tau_biased, bias, bias_pct, topology
167	    """
168	    if topology not in TOPOLOGIES:
169	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
170	    if not validate_confusion_matrix(C):
171	        raise ValueError("C must be a square, non-negative, column-stochastic matrix")
172	
173	    K = C.shape[0]
174	    merged = dict(DEFAULT_PARAMS[topology])
175	    if params is not None:
176	        merged.update(params)
177	
178	    stats = _precompute(topology, merged, K)
179	    tau_true = _get_tau(topology, np.eye(K), stats, K)
180	    tau_biased = _get_tau(topology, C, stats, K)
181	    bias = tau_biased - tau_true
182	    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float("nan")
183	
184	    return {
185	        "tau_true": float(tau_true),
186	        "tau_biased": float(tau_biased),
187	        "bias": float(bias),
188	        "bias_pct": float(bias_pct),
189	        "topology": topology,
190	    }
191	
192	
193	def clear_cache():
194	    """Clear the precomputed statistics cache."""
195	    _precomp_cache.clear()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "1cb6e052-0515-41dc-a5d6-389a42a163fe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
      "content": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    if topology == \"iv\":\n        Z = data[\"Z\"]\n        Zc = Z - Z.mean()\n        var_Z = (Zc ** 2).mean()\n        stats[\"RF\"] = (Zc * (Y - Y.mean())).mean() / var_Z\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z\n        stats[\"FS\"] = FS\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_iv(C, stats, K):\n    \"\"\"Wald estimator plim: RF / (C @ FS)[1].\"\"\"\n    FS_star = C @ stats[\"FS\"]\n    denom = FS_star[1]\n    if abs(denom) < 1e-15:\n        return np.nan\n    return stats[\"RF\"] / denom\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For IV: Wald estimator RF / (C @ FS)[1].\n    For topologies with T: OLS coefficient index 1 (treatment effect).\n    For topologies without T: OLS coefficient index 1 (first dummy).\n    \"\"\"\n    if topology == \"iv\":\n        return _plim_iv(C, stats, K)\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01SdcNPorEaCM69JJSQbkXQJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "8ed7d634-0581-46b7-9532-9817b9b01678",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFoRszrSp3GrL9usiTMzdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14739,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14739
      },
      "output_tokens": 25,
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

_source line 9 · 2026-05-23T17:36:53.016Z_

<details><summary>↩ Tool result · `toolu_01SdcNPorEaCM69JJSQbkXQJ`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Conjecture 1 robustness to DGP parameters (β, σ²).
4	
5	Reviewer concern: "Only default DGP tested" in Conjecture 1 verification.
6	This sweeps a (β, σ²) × topology grid and reports per-cell ε-approximate
7	monotonicity statistics.
8	
9	Grid:
10	  - β (coefficient magnitude scale) ∈ {0.1, 0.5, 1.0, 2.0, 5.0}
11	  - σ² (T-equation noise variance, where applicable) ∈ {0.5, 1.0, 2.0}
12	  - topology ∈ {confounding, mediation, collider, exposure, mbias, frontdoor, iv}
13	  - K = 3, N_C0 = 10,000 Dirichlet(1,1,1) per cell, δ step = 0.01
14	
15	For each (β, σ², topology, C₀), build C(δ) = (1-δ)·I + δ·C₀ for δ ∈ [0, δ_max]
16	and compute the analytic plim curve |B(δ)| = |τ̂(C(δ)) - τ_true|.
17	The wrong-direction step is the largest single-δ violation against the
18	expected direction (non-decreasing for confounding/mediation/exposure/
19	frontdoor/iv; non-increasing for collider/mbias).
20	
21	Outputs:
22	  artifacts/conjecture_dgp_sensitivity_results.json
23	  artifacts/conjecture_dgp_sensitivity_table.tex
24	"""
25	
26	import json
27	import os
28	import sys
29	import time
30	
31	import numpy as np
32	
33	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
34	from exp_d_conjecture_verify_v2 import (
35	    ALL_TOPOS, NON_DECREASING,
36	    GH_X, GH_W, GH_X2_a_flat, GH_X2_b_flat, GH_W2_flat,
37	    _softmax,
38	    AnalyticSuffStats, AnalyticIVSuffStats,
39	    compute_confounding_ss as _ss_conf_v2,
40	    compute_mediation_ss as _ss_med_v2,
41	    compute_exposure_ss as _ss_exp_v2,
42	    compute_iv_ss as _ss_iv_v2,
43	    compute_bias_curve, check_monotonicity,
44	    get_tau_at_C, make_p_A,
45	    _ALPHA_POOL, _BETA_A_POOL, _BETA_POOL,
46	    _GAMMA_POOL, _DELTA_POOL, _DT_POOL, _DY_POOL,
47	    _MBIAS_A1_POOL, _MBIAS_A2_POOL,
48	    _IV_DZ_POOL, _IV_DU_POOL,
49	    _FD_GAMMA_POOL, _FD_DELTA_POOL,
50	)
51	
52	# ====================================================================
53	# Configuration
54	# ====================================================================
55	K = 3
56	N_C0 = 10_000
57	DELTA_STEP = 0.01
58	SEED = 42
59	MONO_TOL = 1e-12
60	
61	BETA_GRID = [0.1, 0.5, 1.0, 2.0, 5.0]
62	SIGMA_SQ_GRID = [0.5, 1.0, 2.0]
63	EPS_DISPLAY_THRESHOLD = 0.06  # paper-claimed bound
64	
65	DRY_RUN_N = int(os.environ.get('DRY_RUN_N', '0'))  # >0 overrides N_C0
66	
67	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
68	
69	# σ² affects the T-equation noise variance for: confounding (sigma_T²),
70	# collider (T variance), mbias (eta_T variance), frontdoor (eta_T variance).
71	# For mediation (binary T), exposure (no T), iv (Wald, no T regression),
72	# σ² does not enter the plim — those cells will be identical across σ².
73	SIGMA_DEPENDENT = {'confounding', 'collider', 'mbias', 'frontdoor'}
74	
75	# Weak-IV filter: for IV, the Wald denominator (1-δ)·FS[1] + δ·(C₀·FS)[1]
76	# is linear in δ. If FS[1] and (C₀·FS)[1] have opposite signs, the
77	# denominator crosses zero, the Wald plim has a pole, and |bias(δ)| diverges
78	# there — a weak-instrument pathology rather than a Conjecture-1 violation.
79	# We drop these C₀ from the violation count and report them separately.
80	
81	# ====================================================================
82	# Parameter grid: scale coefficients by β, noise variance by σ²
83	# ====================================================================
84	def make_params(beta, sigma_sq):
85	    """DGP parameters scaled by β (coefficient magnitude) and σ² (T-noise variance).
86	
87	    β scales all "effect" coefficients (those that enter the structural
88	    equations besides the target τ and U-confounder coefficients).
89	    σ² sets the variance of the T-equation noise (where T is a continuous
90	    variable: confounding/collider/mbias/frontdoor).
91	    """
92	    p_A = make_p_A(K)
93	    sigma = float(np.sqrt(sigma_sq))
94	    b = float(beta)
95	    return dict(
96	        confounding=dict(
97	            p_A=p_A,
98	            alpha=b * np.array(_ALPHA_POOL[:K - 1]),
99	            beta_A=b * np.array(_BETA_A_POOL[:K - 1]),
100	            beta_T=2.0,        # target τ kept fixed
101	            sigma_T=sigma,
102	        ),
103	        mediation=dict(
104	            tau=0.5,           # target τ kept fixed
105	            gamma=b * np.array(_GAMMA_POOL[:K]),
106	            delta=b * np.array(_DELTA_POOL[:K]),
107	            beta=b * np.array(_BETA_POOL[:K]),
108	        ),
109	        collider=dict(
110	            tau=1.0,
111	            g=np.zeros(K),
112	            dT=b * np.array(_DT_POOL[:K]),
113	            dY=b * np.array(_DY_POOL[:K]),
114	            sigma_T=sigma,
115	        ),
116	        exposure=dict(
117	            p_A=p_A,
118	            beta=b * np.array(_BETA_POOL[:K]),
119	        ),
120	        mbias=dict(
121	            tau=1.0,
122	            delta_coef=b,
123	            lam=b,
124	            g=np.zeros(K),
125	            a1=b * np.array(_MBIAS_A1_POOL[:K]),
126	            a2=b * np.array(_MBIAS_A2_POOL[:K]),
127	            sigma_eta=sigma,
128	        ),
129	        iv=dict(
130	            lam=b,
131	            g=np.zeros(K),
132	            dZ=b * np.array(_IV_DZ_POOL[:K]),
133	            dU=b * np.array(_IV_DU_POOL[:K]),
134	            beta=b * np.array(_BETA_POOL[:K]),
135	        ),
136	        frontdoor=dict(
137	            alpha_U=1.0,
138	            lam_U=b,
139	            gamma=b * np.array(_FD_GAMMA_POOL[:K]),
140	            delta=b * np.array(_FD_DELTA_POOL[:K]),
141	            beta=b * np.array(_BETA_POOL[:K]),
142	            sigma_eta=sigma,
143	        ),
144	    )
145	
146	
147	# ====================================================================
148	# Sufficient stats: confounding, mediation, exposure, iv reuse v2.
149	# Collider/mbias/frontdoor need σ²-aware variants.
150	# ====================================================================
151	def compute_collider_ss_scaled(p):
152	    """Collider with T ~ N(0, sigma_T²) instead of N(0,1).
153	
154	    DGP: T ~ N(0, σ²), eps_Y ~ N(0,1) independent
155	         Y = τ·T + eps_Y
156	         A | T, Y ~ Cat(softmax(g + dT·T + dY·Y))
157	    Reparametrize Z1 = T/σ ~ N(0,1) so T = σ·Z1, Y = τσ·Z1 + Z2.
158	    """
159	    ss = AnalyticSuffStats(K, has_T=True)
160	    tau = p['tau']
161	    g = p['g']
162	    dT = p['dT']
163	    dY = p['dY']
164	    sigma_T = p['sigma_T']
165	    sigma_T2 = sigma_T ** 2
166	
167	    # T = σ_T · Z1, eps_Y = Z2; Y = τ·σ_T·Z1 + Z2
168	    coeff1 = (dT + tau * dY) * sigma_T   # of Z1 in logits
169	    coeff2 = dY                           # of Z2 in logits
170	
171	    logits = (g[None, :]
172	              + coeff1[None, :] * GH_X2_a_flat[:, None]
173	              + coeff2[None, :] * GH_X2_b_flat[:, None])
174	    probs = _softmax(logits)
175	    w = GH_W2_flat
176	
177	    T_vals = sigma_T * GH_X2_a_flat
178	    Y_vals = tau * sigma_T * GH_X2_a_flat + GH_X2_b_flat
179	
180	    ss.p_A = (w[:, None] * probs).sum(axis=0)
181	    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
182	    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)
183	
184	    ss.E_T = 0.0
185	    ss.E_T2 = sigma_T2
186	    ss.E_Y = 0.0
187	    ss.E_TY = tau * sigma_T2
188	    return ss
189	
190	
191	def compute_mbias_ss_scaled(p):
192	    """M-bias with eta_T ~ N(0, sigma_eta²) instead of N(0,1).
193	
194	    DGP: U1, U2 ~ N(0,1) iid (latent confounders kept unit variance)
195	         T = δ·U1 + η,  η ~ N(0, σ_η²)
196	         Y = τ·T + λ·U2 + eps_Y
197	         A | U1, U2 ~ Cat(softmax(g + a1·U1 + a2·U2))
198	    """
199	    ss = AnalyticSuffStats(K, has_T=True)
200	    tau = p['tau']
201	    delta_coef = p['delta_coef']
202	    lam = p['lam']
203	    g = p['g']
204	    a1 = p['a1']
205	    a2 = p['a2']
206	    sigma_eta = p['sigma_eta']
207	
208	    logits = (g[None, :]
209	              + a1[None, :] * GH_X2_a_flat[:, None]
210	              + a2[None, :] * GH_X2_b_flat[:, None])
211	    probs = _softmax(logits)
212	    w = GH_W2_flat
213	    U1_vals = GH_X2_a_flat
214	    U2_vals = GH_X2_b_flat
215	
216	    ss.p_A = (w[:, None] * probs).sum(axis=0)
217	    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)
218	    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)
219	    # eta indep of A => E[eta·1(A=k)] = 0
220	    ss.E_TD = delta_coef * E_U1_Dk
221	    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk
222	
223	    ss.E_T = 0.0
224	    ss.E_T2 = delta_coef ** 2 + sigma_eta ** 2
225	    ss.E_Y = 0.0
226	    ss.E_TY = tau * ss.E_T2
227	    return ss
228	
229	
230	def compute_frontdoor_ss_scaled(p):
231	    """Front-door with eta_T ~ N(0, sigma_eta²) instead of N(0,1).
232	
233	    DGP: U ~ N(0,1), T = α_U·U + η, η ~ N(0, σ_η²)
234	         M | T ~ Cat(softmax(γ + δ·T))
235	         Y = D_M·β[1:] + λ_U·U + eps_Y
236	    """
237	    ss = AnalyticSuffStats(K, has_T=True)
238	    alpha_U = p['alpha_U']
239	    lam_U = p['lam_U']
240	    gamma = p['gamma']
241	    delta_coef = p['delta']
242	    beta = p['beta']
243	    sigma_eta = p['sigma_eta']
244	
245	    sigma_T2 = alpha_U ** 2 + sigma_eta ** 2
246	    sigma_T = float(np.sqrt(sigma_T2))
247	
248	    T_nodes = GH_X * sigma_T
249	    T_weights = GH_W
250	
251	    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
252	    probs = _softmax(logits)
253	
254	    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)
255	    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)
256	
257	    # E[U|T] = Cov(U,T)/Var(T)·T = α_U/σ_T² · T
258	    E_U_given_T = alpha_U / sigma_T2 * T_nodes
259	    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)
260	
261	    ss.E_YD = np.zeros(K)
262	    for k in range(K):
263	        beta_k = beta[k] if k >= 1 else 0.0
264	        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]
265	
266	    ss.E_T = 0.0
267	    ss.E_T2 = sigma_T2
268	    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))
269	    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U
270	    return ss
271	
272	
273	_COMPUTE_SS = {
274	    'confounding': lambda p: _ss_conf_v2(K, p),
275	    'mediation':   lambda p: _ss_med_v2(K, p),
276	    'exposure':    lambda p: _ss_exp_v2(K, p),
277	    'iv':          lambda p: _ss_iv_v2(K, p),
278	    'collider':    lambda p: compute_collider_ss_scaled(p),
279	    'mbias':       lambda p: compute_mbias_ss_scaled(p),
280	    'frontdoor':   lambda p: compute_frontdoor_ss_scaled(p),
281	}
282	
283	
284	def get_tau_true(topo, params, ss):
285	    p = params[topo]
286	    if topo in ('collider', 'mbias'):
287	        return p['tau']
288	    return get_tau_at_C(topo, np.eye(K), ss)
289	
290	
291	def compute_iv_bias_curve_analytic(C0, ss, delta_step=DELTA_STEP):
292	    """Cancellation-free IV bias curve.
293	
294	    Wald: τ̂(δ) = RF / fs_star_1(δ),  fs_star_1(δ) = (1-δ)·FS[1] + δ·(C₀·FS)[1].
295	    τ_true = RF / FS[1].  Then
296	       |B(δ)| = |RF| · δ · |Δ| / (|fs_star_1(δ)| · |FS[1]|),   Δ = (C₀·FS)[1] - FS[1].
297	    This avoids the catastrophic cancellation in `RF/fs - RF/FS[1]` that
298	    triggers spurious "violations" when |bias| is large.
299	    """
300	    Kloc = C0.shape[0]
301	    min_diag = np.diag(C0).min()
302	    if min_diag >= 1.0:
303	        delta_max = 10.0
304	    else:
305	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
306	    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)
307	
308	    FS = ss.FS
309	    FS0_1 = float((C0 @ FS)[1])
310	    a = float(FS[1])
311	    b = FS0_1
312	    fs_star_1 = (1.0 - deltas) * a + deltas * b
313	    Delta = b - a
314	
315	    # Sign-flip ⇒ denominator crosses zero in the δ range
316	    if np.any(np.diff(np.sign(fs_star_1)) != 0):
317	        return deltas, np.full(len(deltas), np.nan), True
318	
319	    abs_RF = abs(float(ss.RF))
320	    abs_a = abs(a)
321	    if abs_a < 1e-15:
322	        return deltas, np.full(len(deltas), np.nan), True
323	    bias_abs = abs_RF * deltas * abs(Delta) / (np.abs(fs_star_1) * abs_a)
324	    return deltas, bias_abs, False
325	
326	
327	# ====================================================================
328	# Per-cell evaluation
329	# ====================================================================
330	def evaluate_cell(topo, beta, sigma_sq, n_c0):
331	    params = make_params(beta, sigma_sq)
332	    ss = _COMPUTE_SS[topo](params[topo])
333	    tau_true = get_tau_true(topo, params, ss)
334	
335	    if np.isnan(tau_true) or abs(tau_true) < 1e-12:
336	        return {
337	            'beta': beta, 'sigma_sq': sigma_sq, 'topology': topo,
338	            'n_matrices': n_c0, 'violation_count': 0, 'violation_rate': 0.0,
339	            'worst_epsilon_abs': 0.0, 'worst_epsilon_rel': 0.0,
340	            'tau_true': float(tau_true) if not np.isnan(tau_true) else None,
341	            'direction': 'non-dec' if topo in NON_DECREASING else 'non-inc',
342	            'skipped': True,
343	            'reason': 'tau_true is NaN or near zero',
344	        }
345	
346	    rng = np.random.default_rng(
347	        SEED * 17 + ALL_TOPOS.index(topo) * 100003
348	        + int(round(beta * 1000)) * 13 + int(round(sigma_sq * 1000))
349	    )
350	
351	    violations = 0
352	    nan_curves = 0
353	    weak_iv_filtered = 0
354	    worst_abs = 0.0
355	
356	    for _ in range(n_c0):
357	        C0 = np.empty((K, K))
358	        for j in range(K):
359	            C0[:, j] = rng.dirichlet(np.ones(K))
360	
361	        if topo == 'iv':
362	            _, bias_abs, weak = compute_iv_bias_curve_analytic(C0, ss,
363	                                                                delta_step=DELTA_STEP)
364	            if weak:
365	                weak_iv_filtered += 1
366	                continue
367	        else:
368	            _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true,
369	                                             delta_step=DELTA_STEP)
370	
371	        n_nan = int(np.isnan(bias_abs).sum())
372	        if n_nan > len(bias_abs) * 0.5:
373	            nan_curves += 1
374	            continue
375	
376	        n_viol = check_monotonicity(bias_abs, topo, tol=MONO_TOL)
377	        if n_viol > 0:
378	            violations += 1
379	            valid = ~np.isnan(bias_abs)
380	            diffs = np.diff(bias_abs[valid])
381	            if topo in NON_DECREASING:
382	                step = float(-diffs.min())  # most negative => largest violation
383	            else:
384	                step = float(diffs.max())   # most positive => largest violation
385	            if step > worst_abs:
386	                worst_abs = step
387	
388	    effective_denom = max(n_c0 - nan_curves - weak_iv_filtered, 1)
389	    return {
390	        'beta': beta,
391	        'sigma_sq': sigma_sq,
392	        'topology': topo,
393	        'n_matrices': n_c0,
394	        'nan_curves': nan_curves,
395	        'weak_iv_filtered': weak_iv_filtered,
396	        'violation_count': int(violations),
397	        'violation_rate': 100.0 * violations / effective_denom,
398	        'worst_epsilon_abs': float(worst_abs),
399	        'worst_epsilon_rel': float(worst_abs / abs(tau_true)),
400	        'tau_true': float(tau_true),
401	        'direction': 'non-dec' if topo in NON_DECREASING else 'non-inc',
402	        'sigma_affects_plim': topo in SIGMA_DEPENDENT,
403	    }
404	
405	
406	# ====================================================================
407	# Main
408	# ====================================================================
409	def main():
410	    t_total = time.time()
411	    n_c0 = DRY_RUN_N if DRY_RUN_N > 0 else N_C0
412	    if DRY_RUN_N > 0:
413	        print(f"DRY RUN: N_C0 = {n_c0} (env DRY_RUN_N override)")
414	    print("=" * 78)
415	    print(f"Conjecture 1 robustness across (β, σ²) × topology, K={K}")
416	    print(f"  β grid: {BETA_GRID}")
417	    print(f"  σ² grid: {SIGMA_SQ_GRID}")
418	    print(f"  topologies: {ALL_TOPOS}")
419	    print(f"  N_C0 per cell: {n_c0:,}, δ step: {DELTA_STEP}, seed: {SEED}")
420	    print(f"  σ²-dependent topologies: {sorted(SIGMA_DEPENDENT)}")
421	    print("=" * 78)
422	    sys.stdout.flush()
423	
424	    grid_results = []
425	    n_cells = len(BETA_GRID) * len(SIGMA_SQ_GRID) * len(ALL_TOPOS)
426	    cell_i = 0
427	
428	    print(f"\n  {'topo':<14} {'β':>6} {'σ²':>5} {'τ_true':>11} "
429	          f"{'viol':>7} {'rate%':>7} {'ε_abs':>10} {'ε_rel':>10} "
430	          f"{'wkIV':>5} {'time':>7}")
431	    print("  " + "-" * 86)
432	    sys.stdout.flush()
433	
434	    for topo in ALL_TOPOS:
435	        for beta in BETA_GRID:
436	            for sigma_sq in SIGMA_SQ_GRID:
437	                cell_i += 1
438	                t0 = time.time()
439	                rec = evaluate_cell(topo, beta, sigma_sq, n_c0)
440	                elapsed = time.time() - t0
441	                tau_str = (f"{rec['tau_true']:>11.5f}"
442	                           if rec.get('tau_true') is not None
443	                           and not np.isnan(rec['tau_true'])
444	                           else f"{'NaN':>11}")
445	                wkiv = rec.get('weak_iv_filtered', 0)
446	                print(f"  {topo:<14} {beta:>6.2f} {sigma_sq:>5.2f} "
447	                      f"{tau_str} "
448	                      f"{rec['violation_count']:>7} "
449	                      f"{rec['violation_rate']:>7.3f} "
450	                      f"{rec['worst_epsilon_abs']:>10.2e} "
451	                      f"{rec['worst_epsilon_rel']:>10.2e} "
452	                      f"{wkiv:>5} "
453	                      f"{elapsed:>6.1f}s  [{cell_i}/{n_cells}]")
454	                sys.stdout.flush()
455	                grid_results.append(rec)
456	
457	    # ----- Aggregate summary -----
458	    max_eps_overall = max(r['worst_epsilon_rel'] for r in grid_results)
459	    max_eps_abs_overall = max(r['worst_epsilon_abs'] for r in grid_results)
460	    by_topo_rel = {}
461	    by_topo_abs = {}
462	    for t in ALL_TOPOS:
463	        vals_rel = [r['worst_epsilon_rel'] for r in grid_results
464	                    if r['topology'] == t]
465	        vals_abs = [r['worst_epsilon_abs'] for r in grid_results
466	                    if r['topology'] == t]
467	        by_topo_rel[t] = max(vals_rel) if vals_rel else 0.0
468	        by_topo_abs[t] = max(vals_abs) if vals_abs else 0.0
469	
470	    summary = {
471	        'max_epsilon_rel_overall': float(max_eps_overall),
472	        'max_epsilon_abs_overall': float(max_eps_abs_overall),
473	        'max_epsilon_rel_by_topology': {k: float(v)
474	                                         for k, v in by_topo_rel.items()},
475	        'max_epsilon_abs_by_topology': {k: float(v)
476	                                         for k, v in by_topo_abs.items()},
477	        'all_below_006': bool(max_eps_overall <= EPS_DISPLAY_THRESHOLD),
478	        'eps_display_threshold': EPS_DISPLAY_THRESHOLD,
479	        'total_cells': n_cells,
480	        'total_C0_samples': n_cells * n_c0,
481	    }
482	
483	    elapsed_total = time.time() - t_total
484	    output = {
485	        'config': {
486	            'K': K,
487	            'n_C0_per_cell': n_c0,
488	            'beta_grid': BETA_GRID,
489	            'sigma_sq_grid': SIGMA_SQ_GRID,
490	            'topologies': ALL_TOPOS,
491	            'delta_step': DELTA_STEP,
492	            'seed': SEED,
493	            'mono_tol': MONO_TOL,
494	            'method': 'analytic_plim_via_GH_quadrature',
495	            'sigma_dependent_topologies': sorted(SIGMA_DEPENDENT),
496	            'tau_treatment': {
497	                'confounding': 'beta_T = 2.0 (fixed); β scales α (confounder→T) and β_A (confounder→Y)',
498	                'mediation': 'tau = 0.5 (fixed); β scales γ (mediator|T), δ (mediator|T,A), β (mediator→Y)',
499	                'collider': 'tau = 1.0 (fixed); β scales dT, dY; σ² is Var(T)',
500	                'exposure': 'no T; β scales β (A→Y) only',
501	                'mbias': 'tau = 1.0 (fixed); β scales δ, λ, a1, a2; σ² is Var(η_T)',
502	                'iv': 'β scales β (A→Y), dZ, dU, λ',
503	                'frontdoor': 'α_U = 1.0 (fixed); β scales γ, δ, β, λ_U; σ² is Var(η_T)',
504	            },
505	            'dry_run': DRY_RUN_N > 0,
506	        },
507	        'grid_results': grid_results,
508	        'summary': summary,
509	        'elapsed_seconds': elapsed_total,
510	    }
511	
512	    out_path = os.path.join(OUT_DIR, 'conjecture_dgp_sensitivity_results.json')
513	    with open(out_path, 'w') as f:
514	        json.dump(output, f, indent=2, default=str)
515	    print(f"\nJSON -> {out_path}")
516	
517	    # ----- LaTeX table -----
518	    tex = []
519	    tex.append("% Auto-generated by conjecture_dgp_sensitivity.py")
520	    tex.append("% Worst-case ε_rel = max wrong-direction step / |τ_true| over "
521	               f"{n_c0:,} random C₀ per cell.")
522	    tex.append("\\begin{table}[t]")
523	    tex.append("\\centering")
524	    tex.append("\\small")
525	    tex.append("\\setlength{\\tabcolsep}{4pt}")
526	    tex.append("\\begin{tabular}{cc" + "c" * len(ALL_TOPOS) + "}")
527	    tex.append("\\toprule")
528	    tex.append("$\\beta$ & $\\sigma^2$ & "
529	               + " & ".join("\\textsc{" + t[:5] + "}" for t in ALL_TOPOS)
530	               + " \\\\")
531	    tex.append("\\midrule")
532	
533	    rec_by = {(r['topology'], r['beta'], r['sigma_sq']): r for r in grid_results}
534	    for beta in BETA_GRID:
535	        for sigma_sq in SIGMA_SQ_GRID:
536	            row = [f"{beta:g}", f"{sigma_sq:g}"]
537	            for topo in ALL_TOPOS:
538	                r = rec_by[(topo, beta, sigma_sq)]
539	                eps = r['worst_epsilon_rel']
540	                if eps <= 1e-10:
541	                    cell = "$0$"
542	                elif eps < 1e-4:
543	                    cell = f"${eps:.1e}$".replace("e-0", "e-").replace("e+0", "e")
544	                else:
545	                    cell = f"${eps:.4f}$"
546	                row.append(cell)
547	            tex.append(" & ".join(row) + " \\\\")
548	        if beta != BETA_GRID[-1]:
549	            tex.append("\\midrule")
550	    tex.append("\\bottomrule")
551	    tex.append("\\end{tabular}")
552	    cap = (f"Conjecture~1 robustness: worst-case $\\varepsilon_{{\\text{{rel}}}}"
553	           f" = \\max_{{C_0}} (\\text{{wrong-direction step}})/|\\tau_{{\\text{{true}}}}|$"
554	           f" across {len(BETA_GRID)} effect-magnitude scales $\\beta$, "
555	           f"{len(SIGMA_SQ_GRID)} noise variances $\\sigma^2$, and "
556	           f"{len(ALL_TOPOS)} topologies ($K{{=}}{K}$, "
557	           f"${n_c0:,}$ Dirichlet$(1,...,1)$ matrices per cell). "
558	           f"Overall maximum $\\varepsilon_{{\\text{{rel}}}}"
559	           f"={max_eps_overall:.4f}$; "
560	           f"all cells {'$\\le 0.06$' if summary['all_below_006'] else '> 0.06 at some cell'}.")
561	    tex.append("\\caption{" + cap + "}")
562	    tex.append("\\label{tab:conj1-dgp-sensitivity}")
563	    tex.append("\\end{table}")
564	
565	    tex_path = os.path.join(OUT_DIR, 'conjecture_dgp_sensitivity_table.tex')
566	    with open(tex_path, 'w') as f:
567	        f.write("\n".join(tex) + "\n")
568	    print(f"LaTeX -> {tex_path}")
569	
570	    # ----- Console summary -----
571	    print("\n" + "=" * 78)
572	    print(f"Overall max ε_rel = {max_eps_overall:.5f}"
573	          f" (abs = {max_eps_abs_overall:.5e})")
574	    print(f"All cells ≤ 0.06: {summary['all_below_006']}")
575	    print("Per-topology max ε_rel:")
576	    for t in ALL_TOPOS:
577	        print(f"  {t:<14} {by_topo_rel[t]:.5f}  (abs {by_topo_abs[t]:.3e})")
578	    print(f"Total cells: {n_cells}, total C₀ samples: {n_cells * n_c0:,}")
579	    print(f"Elapsed: {elapsed_total:.1f}s ({elapsed_total / 60:.2f} min)")
580	    print("=" * 78)
581	
582	
583	if __name__ == "__main__":
584	    main()
585	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "66c860a4-5634-4fac-b556-ec206ef32cfa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nConjecture 1 robustness to DGP parameters (β, σ²).\n\nReviewer concern: \"Only default DGP tested\" in Conjecture 1 verification.\nThis sweeps a (β, σ²) × topology grid and reports per-cell ε-approximate\nmonotonicity statistics.\n\nGrid:\n  - β (coefficient magnitude scale) ∈ {0.1, 0.5, 1.0, 2.0, 5.0}\n  - σ² (T-equation noise variance, where applicable) ∈ {0.5, 1.0, 2.0}\n  - topology ∈ {confounding, mediation, collider, exposure, mbias, frontdoor, iv}\n  - K = 3, N_C0 = 10,000 Dirichlet(1,1,1) per cell, δ step = 0.01\n\nFor each (β, σ², topology, C₀), build C(δ) = (1-δ)·I + δ·C₀ for δ ∈ [0, δ_max]\nand compute the analytic plim curve |B(δ)| = |τ̂(C(δ)) - τ_true|.\nThe wrong-direction step is the largest single-δ violation against the\nexpected direction (non-decreasing for confounding/mediation/exposure/\nfrontdoor/iv; non-increasing for collider/mbias).\n\nOutputs:\n  artifacts/conjecture_dgp_sensitivity_results.json\n  artifacts/conjecture_dgp_sensitivity_table.tex\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\n\nimport numpy as np\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom exp_d_conjecture_verify_v2 import (\n    ALL_TOPOS, NON_DECREASING,\n    GH_X, GH_W, GH_X2_a_flat, GH_X2_b_flat, GH_W2_flat,\n    _softmax,\n    AnalyticSuffStats, AnalyticIVSuffStats,\n    compute_confounding_ss as _ss_conf_v2,\n    compute_mediation_ss as _ss_med_v2,\n    compute_exposure_ss as _ss_exp_v2,\n    compute_iv_ss as _ss_iv_v2,\n    compute_bias_curve, check_monotonicity,\n    get_tau_at_C, make_p_A,\n    _ALPHA_POOL, _BETA_A_POOL, _BETA_POOL,\n    _GAMMA_POOL, _DELTA_POOL, _DT_POOL, _DY_POOL,\n    _MBIAS_A1_POOL, _MBIAS_A2_POOL,\n    _IV_DZ_POOL, _IV_DU_POOL,\n    _FD_GAMMA_POOL, _FD_DELTA_POOL,\n)\n\n# ====================================================================\n# Configuration\n# ====================================================================\nK = 3\nN_C0 = 10_000\nDELTA_STEP = 0.01\nSEED = 42\nMONO_TOL = 1e-12\n\nBETA_GRID = [0.1, 0.5, 1.0, 2.0, 5.0]\nSIGMA_SQ_GRID = [0.5, 1.0, 2.0]\nEPS_DISPLAY_THRESHOLD = 0.06  # paper-claimed bound\n\nDRY_RUN_N = int(os.environ.get('DRY_RUN_N', '0'))  # >0 overrides N_C0\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n# σ² affects the T-equation noise variance for: confounding (sigma_T²),\n# collider (T variance), mbias (eta_T variance), frontdoor (eta_T variance).\n# For mediation (binary T), exposure (no T), iv (Wald, no T regression),\n# σ² does not enter the plim — those cells will be identical across σ².\nSIGMA_DEPENDENT = {'confounding', 'collider', 'mbias', 'frontdoor'}\n\n# Weak-IV filter: for IV, the Wald denominator (1-δ)·FS[1] + δ·(C₀·FS)[1]\n# is linear in δ. If FS[1] and (C₀·FS)[1] have opposite signs, the\n# denominator crosses zero, the Wald plim has a pole, and |bias(δ)| diverges\n# there — a weak-instrument pathology rather than a Conjecture-1 violation.\n# We drop these C₀ from the violation count and report them separately.\n\n# ====================================================================\n# Parameter grid: scale coefficients by β, noise variance by σ²\n# ====================================================================\ndef make_params(beta, sigma_sq):\n    \"\"\"DGP parameters scaled by β (coefficient magnitude) and σ² (T-noise variance).\n\n    β scales all \"effect\" coefficients (those that enter the structural\n    equations besides the target τ and U-confounder coefficients).\n    σ² sets the variance of the T-equation noise (where T is a continuous\n    variable: confounding/collider/mbias/frontdoor).\n    \"\"\"\n    p_A = make_p_A(K)\n    sigma = float(np.sqrt(sigma_sq))\n    b = float(beta)\n    return dict(\n        confounding=dict(\n            p_A=p_A,\n            alpha=b * np.array(_ALPHA_POOL[:K - 1]),\n            beta_A=b * np.array(_BETA_A_POOL[:K - 1]),\n            beta_T=2.0,        # target τ kept fixed\n            sigma_T=sigma,\n        ),\n        mediation=dict(\n            tau=0.5,           # target τ kept fixed\n            gamma=b * np.array(_GAMMA_POOL[:K]),\n            delta=b * np.array(_DELTA_POOL[:K]),\n            beta=b * np.array(_BETA_POOL[:K]),\n        ),\n        collider=dict(\n            tau=1.0,\n            g=np.zeros(K),\n            dT=b * np.array(_DT_POOL[:K]),\n            dY=b * np.array(_DY_POOL[:K]),\n            sigma_T=sigma,\n        ),\n        exposure=dict(\n            p_A=p_A,\n            beta=b * np.array(_BETA_POOL[:K]),\n        ),\n        mbias=dict(\n            tau=1.0,\n            delta_coef=b,\n            lam=b,\n            g=np.zeros(K),\n            a1=b * np.array(_MBIAS_A1_POOL[:K]),\n            a2=b * np.array(_MBIAS_A2_POOL[:K]),\n            sigma_eta=sigma,\n        ),\n        iv=dict(\n            lam=b,\n            g=np.zeros(K),\n            dZ=b * np.array(_IV_DZ_POOL[:K]),\n            dU=b * np.array(_IV_DU_POOL[:K]),\n            beta=b * np.array(_BETA_POOL[:K]),\n        ),\n        frontdoor=dict(\n            alpha_U=1.0,\n            lam_U=b,\n            gamma=b * np.array(_FD_GAMMA_POOL[:K]),\n            delta=b * np.array(_FD_DELTA_POOL[:K]),\n            beta=b * np.array(_BETA_POOL[:K]),\n            sigma_eta=sigma,\n        ),\n    )\n\n\n# ====================================================================\n# Sufficient stats: confounding, mediation, exposure, iv reuse v2.\n# Collider/mbias/frontdoor need σ²-aware variants.\n# ====================================================================\ndef compute_collider_ss_scaled(p):\n    \"\"\"Collider with T ~ N(0, sigma_T²) instead of N(0,1).\n\n    DGP: T ~ N(0, σ²), eps_Y ~ N(0,1) independent\n         Y = τ·T + eps_Y\n         A | T, Y ~ Cat(softmax(g + dT·T + dY·Y))\n    Reparametrize Z1 = T/σ ~ N(0,1) so T = σ·Z1, Y = τσ·Z1 + Z2.\n    \"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    g = p['g']\n    dT = p['dT']\n    dY = p['dY']\n    sigma_T = p['sigma_T']\n    sigma_T2 = sigma_T ** 2\n\n    # T = σ_T · Z1, eps_Y = Z2; Y = τ·σ_T·Z1 + Z2\n    coeff1 = (dT + tau * dY) * sigma_T   # of Z1 in logits\n    coeff2 = dY                           # of Z2 in logits\n\n    logits = (g[None, :]\n              + coeff1[None, :] * GH_X2_a_flat[:, None]\n              + coeff2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)\n    w = GH_W2_flat\n\n    T_vals = sigma_T * GH_X2_a_flat\n    Y_vals = tau * sigma_T * GH_X2_a_flat + GH_X2_b_flat\n\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)\n    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)\n\n    ss.E_T = 0.0\n    ss.E_T2 = sigma_T2\n    ss.E_Y = 0.0\n    ss.E_TY = tau * sigma_T2\n    return ss\n\n\ndef compute_mbias_ss_scaled(p):\n    \"\"\"M-bias with eta_T ~ N(0, sigma_eta²) instead of N(0,1).\n\n    DGP: U1, U2 ~ N(0,1) iid (latent confounders kept unit variance)\n         T = δ·U1 + η,  η ~ N(0, σ_η²)\n         Y = τ·T + λ·U2 + eps_Y\n         A | U1, U2 ~ Cat(softmax(g + a1·U1 + a2·U2))\n    \"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    delta_coef = p['delta_coef']\n    lam = p['lam']\n    g = p['g']\n    a1 = p['a1']\n    a2 = p['a2']\n    sigma_eta = p['sigma_eta']\n\n    logits = (g[None, :]\n              + a1[None, :] * GH_X2_a_flat[:, None]\n              + a2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)\n    w = GH_W2_flat\n    U1_vals = GH_X2_a_flat\n    U2_vals = GH_X2_b_flat\n\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)\n    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)\n    # eta indep of A => E[eta·1(A=k)] = 0\n    ss.E_TD = delta_coef * E_U1_Dk\n    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk\n\n    ss.E_T = 0.0\n    ss.E_T2 = delta_coef ** 2 + sigma_eta ** 2\n    ss.E_Y = 0.0\n    ss.E_TY = tau * ss.E_T2\n    return ss\n\n\ndef compute_frontdoor_ss_scaled(p):\n    \"\"\"Front-door with eta_T ~ N(0, sigma_eta²) instead of N(0,1).\n\n    DGP: U ~ N(0,1), T = α_U·U + η, η ~ N(0, σ_η²)\n         M | T ~ Cat(softmax(γ + δ·T))\n         Y = D_M·β[1:] + λ_U·U + eps_Y\n    \"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    alpha_U = p['alpha_U']\n    lam_U = p['lam_U']\n    gamma = p['gamma']\n    delta_coef = p['delta']\n    beta = p['beta']\n    sigma_eta = p['sigma_eta']\n\n    sigma_T2 = alpha_U ** 2 + sigma_eta ** 2\n    sigma_T = float(np.sqrt(sigma_T2))\n\n    T_nodes = GH_X * sigma_T\n    T_weights = GH_W\n\n    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]\n    probs = _softmax(logits)\n\n    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)\n    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)\n\n    # E[U|T] = Cov(U,T)/Var(T)·T = α_U/σ_T² · T\n    E_U_given_T = alpha_U / sigma_T2 * T_nodes\n    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)\n\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]\n\n    ss.E_T = 0.0\n    ss.E_T2 = sigma_T2\n    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))\n    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U\n    return ss\n\n\n_COMPUTE_SS = {\n    'confounding': lambda p: _ss_conf_v2(K, p),\n    'mediation':   lambda p: _ss_med_v2(K, p),\n    'exposure':    lambda p: _ss_exp_v2(K, p),\n    'iv':          lambda p: _ss_iv_v2(K, p),\n    'collider':    lambda p: compute_collider_ss_scaled(p),\n    'mbias':       lambda p: compute_mbias_ss_scaled(p),\n    'frontdoor':   lambda p: compute_frontdoor_ss_scaled(p),\n}\n\n\ndef get_tau_true(topo, params, ss):\n    p = params[topo]\n    if topo in ('collider', 'mbias'):\n        return p['tau']\n    return get_tau_at_C(topo, np.eye(K), ss)\n\n\ndef compute_iv_bias_curve_analytic(C0, ss, delta_step=DELTA_STEP):\n    \"\"\"Cancellation-free IV bias curve.\n\n    Wald: τ̂(δ) = RF / fs_star_1(δ),  fs_star_1(δ) = (1-δ)·FS[1] + δ·(C₀·FS)[1].\n    τ_true = RF / FS[1].  Then\n       |B(δ)| = |RF| · δ · |Δ| / (|fs_star_1(δ)| · |FS[1]|),   Δ = (C₀·FS)[1] - FS[1].\n    This avoids the catastrophic cancellation in `RF/fs - RF/FS[1]` that\n    triggers spurious \"violations\" when |bias| is large.\n    \"\"\"\n    Kloc = C0.shape[0]\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        delta_max = 10.0\n    else:\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)\n\n    FS = ss.FS\n    FS0_1 = float((C0 @ FS)[1])\n    a = float(FS[1])\n    b = FS0_1\n    fs_star_1 = (1.0 - deltas) * a + deltas * b\n    Delta = b - a\n\n    # Sign-flip ⇒ denominator crosses zero in the δ range\n    if np.any(np.diff(np.sign(fs_star_1)) != 0):\n        return deltas, np.full(len(deltas), np.nan), True\n\n    abs_RF = abs(float(ss.RF))\n    abs_a = abs(a)\n    if abs_a < 1e-15:\n        return deltas, np.full(len(deltas), np.nan), True\n    bias_abs = abs_RF * deltas * abs(Delta) / (np.abs(fs_star_1) * abs_a)\n    return deltas, bias_abs, False\n\n\n# ====================================================================\n# Per-cell evaluation\n# ====================================================================\ndef evaluate_cell(topo, beta, sigma_sq, n_c0):\n    params = make_params(beta, sigma_sq)\n    ss = _COMPUTE_SS[topo](params[topo])\n    tau_true = get_tau_true(topo, params, ss)\n\n    if np.isnan(tau_true) or abs(tau_true) < 1e-12:\n        return {\n            'beta': beta, 'sigma_sq': sigma_sq, 'topology': topo,\n            'n_matrices': n_c0, 'violation_count': 0, 'violation_rate': 0.0,\n            'worst_epsilon_abs': 0.0, 'worst_epsilon_rel': 0.0,\n            'tau_true': float(tau_true) if not np.isnan(tau_true) else None,\n            'direction': 'non-dec' if topo in NON_DECREASING else 'non-inc',\n            'skipped': True,\n            'reason': 'tau_true is NaN or near zero',\n        }\n\n    rng = np.random.default_rng(\n        SEED * 17 + ALL_TOPOS.index(topo) * 100003\n        + int(round(beta * 1000)) * 13 + int(round(sigma_sq * 1000))\n    )\n\n    violations = 0\n    nan_curves = 0\n    weak_iv_filtered = 0\n    worst_abs = 0.0\n\n    for _ in range(n_c0):\n        C0 = np.empty((K, K))\n        for j in range(K):\n            C0[:, j] = rng.dirichlet(np.ones(K))\n\n        if topo == 'iv':\n            _, bias_abs, weak = compute_iv_bias_curve_analytic(C0, ss,\n                                                                delta_step=DELTA_STEP)\n            if weak:\n                weak_iv_filtered += 1\n                continue\n        else:\n            _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true,\n                                             delta_step=DELTA_STEP)\n\n        n_nan = int(np.isnan(bias_abs).sum())\n        if n_nan > len(bias_abs) * 0.5:\n            nan_curves += 1\n            continue\n\n        n_viol = check_monotonicity(bias_abs, topo, tol=MONO_TOL)\n        if n_viol > 0:\n            violations += 1\n            valid = ~np.isnan(bias_abs)\n            diffs = np.diff(bias_abs[valid])\n            if topo in NON_DECREASING:\n                step = float(-diffs.min())  # most negative => largest violation\n            else:\n                step = float(diffs.max())   # most positive => largest violation\n            if step > worst_abs:\n                worst_abs = step\n\n    effective_denom = max(n_c0 - nan_curves - weak_iv_filtered, 1)\n    return {\n        'beta': beta,\n        'sigma_sq': sigma_sq,\n        'topology': topo,\n        'n_matrices': n_c0,\n        'nan_curves': nan_curves,\n        'weak_iv_filtered': weak_iv_filtered,\n        'violation_count': int(violations),\n        'violation_rate': 100.0 * violations / effective_denom,\n        'worst_epsilon_abs': float(worst_abs),\n        'worst_epsilon_rel': float(worst_abs / abs(tau_true)),\n        'tau_true': float(tau_true),\n        'direction': 'non-dec' if topo in NON_DECREASING else 'non-inc',\n        'sigma_affects_plim': topo in SIGMA_DEPENDENT,\n    }\n\n\n# ====================================================================\n# Main\n# ====================================================================\ndef main():\n    t_total = time.time()\n    n_c0 = DRY_RUN_N if DRY_RUN_N > 0 else N_C0\n    if DRY_RUN_N > 0:\n        print(f\"DRY RUN: N_C0 = {n_c0} (env DRY_RUN_N override)\")\n    print(\"=\" * 78)\n    print(f\"Conjecture 1 robustness across (β, σ²) × topology, K={K}\")\n    print(f\"  β grid: {BETA_GRID}\")\n    print(f\"  σ² grid: {SIGMA_SQ_GRID}\")\n    print(f\"  topologies: {ALL_TOPOS}\")\n    print(f\"  N_C0 per cell: {n_c0:,}, δ step: {DELTA_STEP}, seed: {SEED}\")\n    print(f\"  σ²-dependent topologies: {sorted(SIGMA_DEPENDENT)}\")\n    print(\"=\" * 78)\n    sys.stdout.flush()\n\n    grid_results = []\n    n_cells = len(BETA_GRID) * len(SIGMA_SQ_GRID) * len(ALL_TOPOS)\n    cell_i = 0\n\n    print(f\"\\n  {'topo':<14} {'β':>6} {'σ²':>5} {'τ_true':>11} \"\n          f\"{'viol':>7} {'rate%':>7} {'ε_abs':>10} {'ε_rel':>10} \"\n          f\"{'wkIV':>5} {'time':>7}\")\n    print(\"  \" + \"-\" * 86)\n    sys.stdout.flush()\n\n    for topo in ALL_TOPOS:\n        for beta in BETA_GRID:\n            for sigma_sq in SIGMA_SQ_GRID:\n                cell_i += 1\n                t0 = time.time()\n                rec = evaluate_cell(topo, beta, sigma_sq, n_c0)\n                elapsed = time.time() - t0\n                tau_str = (f\"{rec['tau_true']:>11.5f}\"\n                           if rec.get('tau_true') is not None\n                           and not np.isnan(rec['tau_true'])\n                           else f\"{'NaN':>11}\")\n                wkiv = rec.get('weak_iv_filtered', 0)\n                print(f\"  {topo:<14} {beta:>6.2f} {sigma_sq:>5.2f} \"\n                      f\"{tau_str} \"\n                      f\"{rec['violation_count']:>7} \"\n                      f\"{rec['violation_rate']:>7.3f} \"\n                      f\"{rec['worst_epsilon_abs']:>10.2e} \"\n                      f\"{rec['worst_epsilon_rel']:>10.2e} \"\n                      f\"{wkiv:>5} \"\n                      f\"{elapsed:>6.1f}s  [{cell_i}/{n_cells}]\")\n                sys.stdout.flush()\n                grid_results.append(rec)\n\n    # ----- Aggregate summary -----\n    max_eps_overall = max(r['worst_epsilon_rel'] for r in grid_results)\n    max_eps_abs_overall = max(r['worst_epsilon_abs'] for r in grid_results)\n    by_topo_rel = {}\n    by_topo_abs = {}\n    for t in ALL_TOPOS:\n        vals_rel = [r['worst_epsilon_rel'] for r in grid_results\n                    if r['topology'] == t]\n        vals_abs = [r['worst_epsilon_abs'] for r in grid_results\n                    if r['topology'] == t]\n        by_topo_rel[t] = max(vals_rel) if vals_rel else 0.0\n        by_topo_abs[t] = max(vals_abs) if vals_abs else 0.0\n\n    summary = {\n        'max_epsilon_rel_overall': float(max_eps_overall),\n        'max_epsilon_abs_overall': float(max_eps_abs_overall),\n        'max_epsilon_rel_by_topology': {k: float(v)\n                                         for k, v in by_topo_rel.items()},\n        'max_epsilon_abs_by_topology': {k: float(v)\n                                         for k, v in by_topo_abs.items()},\n        'all_below_006': bool(max_eps_overall <= EPS_DISPLAY_THRESHOLD),\n        'eps_display_threshold': EPS_DISPLAY_THRESHOLD,\n        'total_cells': n_cells,\n        'total_C0_samples': n_cells * n_c0,\n    }\n\n    elapsed_total = time.time() - t_total\n    output = {\n        'config': {\n            'K': K,\n            'n_C0_per_cell': n_c0,\n            'beta_grid': BETA_GRID,\n            'sigma_sq_grid': SIGMA_SQ_GRID,\n            'topologies': ALL_TOPOS,\n            'delta_step': DELTA_STEP,\n            'seed': SEED,\n            'mono_tol': MONO_TOL,\n            'method': 'analytic_plim_via_GH_quadrature',\n            'sigma_dependent_topologies': sorted(SIGMA_DEPENDENT),\n            'tau_treatment': {\n                'confounding': 'beta_T = 2.0 (fixed); β scales α (confounder→T) and β_A (confounder→Y)',\n                'mediation': 'tau = 0.5 (fixed); β scales γ (mediator|T), δ (mediator|T,A), β (mediator→Y)',\n                'collider': 'tau = 1.0 (fixed); β scales dT, dY; σ² is Var(T)',\n                'exposure': 'no T; β scales β (A→Y) only',\n                'mbias': 'tau = 1.0 (fixed); β scales δ, λ, a1, a2; σ² is Var(η_T)',\n                'iv': 'β scales β (A→Y), dZ, dU, λ',\n                'frontdoor': 'α_U = 1.0 (fixed); β scales γ, δ, β, λ_U; σ² is Var(η_T)',\n            },\n            'dry_run': DRY_RUN_N > 0,\n        },\n        'grid_results': grid_results,\n        'summary': summary,\n        'elapsed_seconds': elapsed_total,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'conjecture_dgp_sensitivity_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nJSON -> {out_path}\")\n\n    # ----- LaTeX table -----\n    tex = []\n    tex.append(\"% Auto-generated by conjecture_dgp_sensitivity.py\")\n    tex.append(\"% Worst-case ε_rel = max wrong-direction step / |τ_true| over \"\n               f\"{n_c0:,} random C₀ per cell.\")\n    tex.append(\"\\\\begin{table}[t]\")\n    tex.append(\"\\\\centering\")\n    tex.append(\"\\\\small\")\n    tex.append(\"\\\\setlength{\\\\tabcolsep}{4pt}\")\n    tex.append(\"\\\\begin{tabular}{cc\" + \"c\" * len(ALL_TOPOS) + \"}\")\n    tex.append(\"\\\\toprule\")\n    tex.append(\"$\\\\beta$ & $\\\\sigma^2$ & \"\n               + \" & \".join(\"\\\\textsc{\" + t[:5] + \"}\" for t in ALL_TOPOS)\n               + \" \\\\\\\\\")\n    tex.append(\"\\\\midrule\")\n\n    rec_by = {(r['topology'], r['beta'], r['sigma_sq']): r for r in grid_results}\n    for beta in BETA_GRID:\n        for sigma_sq in SIGMA_SQ_GRID:\n            row = [f\"{beta:g}\", f\"{sigma_sq:g}\"]\n            for topo in ALL_TOPOS:\n                r = rec_by[(topo, beta, sigma_sq)]\n                eps = r['worst_epsilon_rel']\n                if eps <= 1e-10:\n                    cell = \"$0$\"\n                elif eps < 1e-4:\n                    cell = f\"${eps:.1e}$\".replace(\"e-0\", \"e-\").replace(\"e+0\", \"e\")\n                else:\n                    cell = f\"${eps:.4f}$\"\n                row.append(cell)\n            tex.append(\" & \".join(row) + \" \\\\\\\\\")\n        if beta != BETA_GRID[-1]:\n            tex.append(\"\\\\midrule\")\n    tex.append(\"\\\\bottomrule\")\n    tex.append(\"\\\\end{tabular}\")\n    cap = (f\"Conjecture~1 robustness: worst-case $\\\\varepsilon_{{\\\\text{{rel}}}}\"\n           f\" = \\\\max_{{C_0}} (\\\\text{{wrong-direction step}})/|\\\\tau_{{\\\\text{{true}}}}|$\"\n           f\" across {len(BETA_GRID)} effect-magnitude scales $\\\\beta$, \"\n           f\"{len(SIGMA_SQ_GRID)} noise variances $\\\\sigma^2$, and \"\n           f\"{len(ALL_TOPOS)} topologies ($K{{=}}{K}$, \"\n           f\"${n_c0:,}$ Dirichlet$(1,...,1)$ matrices per cell). \"\n           f\"Overall maximum $\\\\varepsilon_{{\\\\text{{rel}}}}\"\n           f\"={max_eps_overall:.4f}$; \"\n           f\"all cells {'$\\\\le 0.06$' if summary['all_below_006'] else '> 0.06 at some cell'}.\")\n    tex.append(\"\\\\caption{\" + cap + \"}\")\n    tex.append(\"\\\\label{tab:conj1-dgp-sensitivity}\")\n    tex.append(\"\\\\end{table}\")\n\n    tex_path = os.path.join(OUT_DIR, 'conjecture_dgp_sensitivity_table.tex')\n    with open(tex_path, 'w') as f:\n        f.write(\"\\n\".join(tex) + \"\\n\")\n    print(f\"LaTeX -> {tex_path}\")\n\n    # ----- Console summary -----\n    print(\"\\n\" + \"=\" * 78)\n    print(f\"Overall max ε_rel = {max_eps_overall:.5f}\"\n          f\" (abs = {max_eps_abs_overall:.5e})\")\n    print(f\"All cells ≤ 0.06: {summary['all_below_006']}\")\n    print(\"Per-topology max ε_rel:\")\n    for t in ALL_TOPOS:\n        print(f\"  {t:<14} {by_topo_rel[t]:.5f}  (abs {by_topo_abs[t]:.3e})\")\n    print(f\"Total cells: {n_cells}, total C₀ samples: {n_cells * n_c0:,}\")\n    print(f\"Elapsed: {elapsed_total:.1f}s ({elapsed_total / 60:.2f} min)\")\n    print(\"=\" * 78)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 585,
      "startLine": 1,
      "totalLines": 585
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01HP5cewK4D84kWZTDpUsoXK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "c17b4a2a-dcfe-482e-9f68-0373f0d10a54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFoRszrSp3GrL9usiTMzdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14739,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14739
      },
      "output_tokens": 25,
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

_source line 11 · 2026-05-23T17:36:53.229Z_

<details><summary>↩ Tool result · `toolu_01HP5cewK4D84kWZTDpUsoXK`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Exp-A: Non-differential Misclassification Stress Test Expansion
4	
5	Tests sign flip rate and bias ratio under increasing differential
6	misclassification departure ε.
7	
8	4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs
9	N=10,000 × 100 MC reps per config
10	"""
11	import numpy as np
12	import json
13	import time
14	import os
15	
16	TOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']
17	K_VALUES = [3, 10]
18	EPSILONS = [0.0, 0.01, 0.05, 0.10]
19	CM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}
20	N_SAMPLES = 10_000
21	N_REPS = 100
22	N_LARGE = 2_000_000
23	SEED = 42
24	
25	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
26	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
27	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
28	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
29	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
30	
31	
32	def softmax_rows(x):
33	    e = np.exp(x - x.max(axis=1, keepdims=True))
34	    return e / e.sum(axis=1, keepdims=True)
35	
36	
37	def sample_cat(probs, rng):
38	    cum = np.cumsum(probs, axis=1)
39	    u = rng.uniform(size=probs.shape[0])[:, None]
40	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
41	
42	
43	def make_p_A(K):
44	    if K == 3:
45	        return np.array([0.40, 0.35, 0.25])
46	    raw = np.array([1.0 / (i + 1) for i in range(K)])
47	    return raw / raw.sum()
48	
49	
50	def make_dgp_params(K):
51	    p_A = make_p_A(K)
52	    params = {
53	        'confounding': {
54	            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),
55	            'beta_A': np.array(_BETA_A_POOL[:K-1]),
56	            'beta_T': 2.0, 'sigma_T': 1.0,
57	        },
58	        'mediation': {
59	            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),
60	            'delta': np.array(_DELTA_POOL[:K]),
61	            'beta': np.array(_BETA_POOL[:K]),
62	        },
63	        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},
64	    }
65	    if K == 3:
66	        params['iv'] = {
67	            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
68	            'g': np.zeros(3), 'dZ': np.array([0.0, 1.0, -0.5]),
69	            'dU': np.array([0.0, 0.8, 0.6]),
70	        }
71	    else:
72	        iv_b = np.array(_BETA_POOL[:K]) * 0.5
73	        iv_b[0] = 0.0
74	        params['iv'] = {
75	            'lam': 1.0, 'beta': iv_b, 'g': np.zeros(K),
76	            'dZ': np.array([0.0] + [_ALPHA_POOL[i]*0.7 for i in range(K-1)]),
77	            'dU': np.array([0.0] + [_BETA_A_POOL[i]*0.6 for i in range(K-1)]),
78	        }
79	    return params
80	
81	
82	# ── DGP generators ──────────────────────────────────────────
83	
84	def gen_confounding(K, N, p, rng):
85	    A = rng.choice(K, size=N, p=p['p_A'])
86	    D = np.zeros((N, K-1))
87	    for j in range(K-1):
88	        D[:, j] = (A == j+1).astype(float)
89	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
90	    Y = p['beta_T']*T + D @ p['beta_A'] + rng.normal(0, 1, N)
91	    return T, Y, A
92	
93	
94	def gen_mediation(K, N, p, rng):
95	    T = rng.binomial(1, 0.5, N).astype(float)
96	    logits = p['gamma'][None, :] + p['delta'][None, :]*T[:, None]
97	    A = sample_cat(softmax_rows(logits), rng)
98	    D = np.zeros((N, K-1))
99	    for j in range(K-1):
100	        D[:, j] = (A == j+1).astype(float)
101	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau']*T + rng.normal(0, 1, N)
102	    return T, Y, A
103	
104	
105	def gen_exposure(K, N, p, rng):
106	    A = rng.choice(K, size=N, p=p['p_A'])
107	    D = np.zeros((N, K-1))
108	    for j in range(K-1):
109	        D[:, j] = (A == j+1).astype(float)
110	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
111	    return None, Y, A
112	
113	
114	def gen_iv(K, N, p, rng):
115	    Z = rng.binomial(1, 0.5, N).astype(float)
116	    U = rng.normal(0, 1, N)
117	    logits = (p['g'][None, :] + p['dZ'][None, :]*Z[:, None]
118	              + p['dU'][None, :]*U[:, None])
119	    A = sample_cat(softmax_rows(logits), rng)
120	    D = np.zeros((N, K-1))
121	    for j in range(K-1):
122	        D[:, j] = (A == j+1).astype(float)
123	    Y = D @ p['beta'][1:] + p['lam']*U + rng.normal(0, 1, N)
124	    return Z, Y, A
125	
126	
127	GEN = {'confounding': gen_confounding, 'mediation': gen_mediation,
128	       'exposure': gen_exposure, 'iv': gen_iv}
129	
130	
131	# ── Estimators ──────────────────────────────────────────────
132	
133	def est_tau(topo, fv, Y, Ak, K):
134	    N = len(Y)
135	    D = np.zeros((N, K-1))
136	    for k in range(1, K):
137	        D[:, k-1] = (Ak == k).astype(float)
138	    if topo == 'iv':
139	        z1, z0 = fv == 1, fv == 0
140	        if z1.sum() < 2 or z0.sum() < 2:
141	            return np.nan
142	        RF = Y[z1].mean() - Y[z0].mean()
143	        FS = D[z1, 0].mean() - D[z0, 0].mean()
144	        return RF / FS if abs(FS) > 1e-8 else np.nan
145	    elif topo == 'exposure':
146	        X = np.column_stack([np.ones(N), D])
147	    else:
148	        X = np.column_stack([np.ones(N), fv, D])
149	    try:
150	        return np.linalg.lstsq(X, Y, rcond=None)[0][1]
151	    except np.linalg.LinAlgError:
152	        return np.nan
153	
154	
155	# ── Confusion matrix construction & perturbation ────────────
156	
157	def make_cm(K, diag):
158	    C = np.full((K, K), (1.0 - diag) / (K - 1))
159	    np.fill_diagonal(C, diag)
160	    return C
161	
162	
163	def perturb(C, eps):
164	    K = C.shape[0]
165	    Cp = C.copy()
166	    Cp[~np.eye(K, dtype=bool)] += eps
167	    for j in range(K):
168	        Cp[:, j] /= Cp[:, j].sum()
169	    return Cp
170	
171	
172	def gen_Astar(A, Y, Cb, eps, rng):
173	    if eps <= 0:
174	        probs = Cb[:, A]
175	    else:
176	        Cp = perturb(Cb, eps)
177	        high = Y > np.median(Y)
178	        probs = np.where(high[None, :], Cp[:, A], Cb[:, A])
179	    cum = np.cumsum(probs, axis=0)
180	    u = rng.uniform(size=len(A))
181	    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)
182	
183	
184	# ── Main ────────────────────────────────────────────────────
185	
186	def main():
187	    t0 = time.time()
188	    out_dir = os.path.dirname(os.path.abspath(__file__))
189	    n_total = len(TOPOLOGIES) * len(K_VALUES) * len(EPSILONS) * len(CM_QUALS)
190	    print(f"Exp-A: {n_total} configs x {N_REPS} MC reps, N={N_SAMPLES}")
191	
192	    # Validate CMs
193	    for K in K_VALUES:
194	        for dv in CM_QUALS.values():
195	            C = make_cm(K, dv)
196	            assert np.allclose(C.sum(axis=0), 1.0), f"K={K} diag={dv}: bad CM"
197	            for eps in EPSILONS:
198	                if eps > 0:
199	                    Cp = perturb(C, eps)
200	                    assert np.allclose(Cp.sum(axis=0), 1.0)
201	                    assert (Cp >= -1e-12).all()
202	
203	    all_params = {K: make_dgp_params(K) for K in K_VALUES}
204	
205	    # True parameters (oracle with N=2M)
206	    tau_trues = {}
207	    print("\nTrue parameters (N=2M oracle):")
208	    for K in K_VALUES:
209	        for topo in TOPOLOGIES:
210	            rng = np.random.default_rng(K*1000 + abs(hash(topo)) % 1000)
211	            fv, Y, A = GEN[topo](K, N_LARGE, all_params[K][topo], rng)
212	            tau_trues[(K, topo)] = est_tau(topo, fv, Y, A, K)
213	            print(f"  K={K:>2} {topo:<13} tau_true={tau_trues[(K,topo)]:>10.6f}")
214	
215	    # MC simulation
216	    results = []
217	    idx = 0
218	    print(f"\nMC simulation ({n_total} configs):")
219	    for topo in TOPOLOGIES:
220	        for K in K_VALUES:
221	            p = all_params[K][topo]
222	            tt = tau_trues[(K, topo)]
223	            for qn, dv in CM_QUALS.items():
224	                Cb = make_cm(K, dv)
225	                for eps in EPSILONS:
226	                    idx += 1
227	                    rng = np.random.default_rng(SEED + idx*1000)
228	                    hats = np.empty(N_REPS)
229	                    for m in range(N_REPS):
230	                        fv, Y, A = GEN[topo](K, N_SAMPLES, p, rng)
231	                        As = gen_Astar(A, Y, Cb, eps, rng)
232	                        hats[m] = est_tau(topo, fv, Y, As, K)
233	
234	                    ok = np.isfinite(hats)
235	                    nv = int(ok.sum())
236	                    if nv > 0 and abs(tt) > 1e-12:
237	                        vh = hats[ok]
238	                        sfr = float((np.sign(vh) != np.sign(tt)).mean())
239	                        ratios = np.abs(vh / tt)
240	                        br = float(ratios.mean())
241	                        br_std = float(ratios.std())
242	                        br_med = float(np.median(ratios))
243	                        mt = float(vh.mean())
244	                    else:
245	                        sfr = br = br_std = br_med = mt = None
246	
247	                    results.append({
248	                        'topology': topo, 'K': K, 'epsilon': eps,
249	                        'cm_quality': qn, 'cm_diag': dv,
250	                        'sign_flip_rate': sfr,
251	                        'mean_bias_ratio': br,
252	                        'std_bias_ratio': br_std,
253	                        'median_bias_ratio': br_med,
254	                        'tau_true': float(tt),
255	                        'mean_tau_hat': mt,
256	                        'n_reps': nv,
257	                    })
258	
259	                    if idx % 12 == 0 or idx == n_total:
260	                        el = time.time() - t0
261	                        eta = el / idx * (n_total - idx)
262	                        s = f"SF={sfr:.3f} BR={br:.3f}" if sfr is not None else "N/A"
263	                        print(f"  [{idx:>3}/{n_total}] {topo:<13} K={K:>2} "
264	                              f"eps={eps:.2f} {qn:<6} {s}  "
265	                              f"({el:.0f}s, ETA {eta:.0f}s)")
266	
267	    # Summaries
268	    def sm(vals):
269	        v = [x for x in vals if x is not None]
270	        return float(np.mean(v)) if v else None
271	
272	    by_eps = {}
273	    for eps in EPSILONS:
274	        sub = [r for r in results if r['epsilon'] == eps]
275	        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]
276	        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]
277	        by_eps[str(eps)] = {
278	            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,
279	            'mean_bias_ratio': float(np.mean(brs)) if brs else None,
280	            'max_sign_flip_rate': float(max(sfs)) if sfs else None,
281	        }
282	
283	    by_topo = {}
284	    for topo in TOPOLOGIES:
285	        sub = [r for r in results if r['topology'] == topo]
286	        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]
287	        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]
288	        by_topo[topo] = {
289	            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,
290	            'mean_bias_ratio': float(np.mean(brs)) if brs else None,
291	        }
292	
293	    by_K = {}
294	    for K in K_VALUES:
295	        sub = [r for r in results if r['K'] == K]
296	        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]
297	        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]
298	        by_K[str(K)] = {
299	            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,
300	            'mean_bias_ratio': float(np.mean(brs)) if brs else None,
301	        }
302	
303	    output = {
304	        'results': results,
305	        'summary': {'by_epsilon': by_eps, 'by_topology': by_topo, 'by_K': by_K},
306	    }
307	
308	    def clean(o):
309	        if isinstance(o, (float, np.floating)):
310	            v = float(o)
311	            return None if (np.isnan(v) or np.isinf(v)) else v
312	        if isinstance(o, np.integer):
313	            return int(o)
314	        if isinstance(o, dict):
315	            return {k: clean(v) for k, v in o.items()}
316	        if isinstance(o, list):
317	            return [clean(v) for v in o]
318	        return o
319	
320	    output = clean(output)
321	    jpath = os.path.join(out_dir, 'exp_a_stress_test_results.json')
322	    with open(jpath, 'w') as f:
323	        json.dump(output, f, indent=2)
324	    print(f"\nJSON -> {jpath}")
325	
326	    tpath = os.path.join(out_dir, 'exp_a_stress_test_table.tex')
327	    write_tex(results, tpath)
328	    print(f"TeX  -> {tpath}")
329	
330	    total = time.time() - t0
331	    print(f"\nDone in {total:.0f}s ({total/60:.1f}min)")
332	    print("\nBy epsilon:")
333	    for eps, s in by_eps.items():
334	        sf = s['mean_sign_flip_rate']
335	        br = s['mean_bias_ratio']
336	        mx = s['max_sign_flip_rate']
337	        print(f"  eps={eps}: meanSF={sf:.4f} meanBR={br:.4f} maxSF={mx:.4f}")
338	    print("\nBy topology:")
339	    for topo, s in by_topo.items():
340	        print(f"  {topo:<13}: SF={s['mean_sign_flip_rate']:.4f} "
341	              f"BR={s['mean_bias_ratio']:.4f}")
342	    print("\nBy K:")
343	    for k, s in by_K.items():
344	        print(f"  K={k}: SF={s['mean_sign_flip_rate']:.4f} "
345	              f"BR={s['mean_bias_ratio']:.4f}")
346	
347	
348	def write_tex(results, path):
349	    ncols = 3 + 2 * len(EPSILONS)
350	    lines = [
351	        r'\begin{table*}[t]',
352	        r'\centering',
353	        r'\caption{Non-differential misclassification stress test: sign flip rate (SF) '
354	        r'and mean bias ratio (BR\,$=\overline{|\hat\tau/\tau|}$) under increasing '
355	        r'differential departure $\varepsilon$.}',
356	        r'\label{tab:stress-test}',
357	        r'\small\setlength{\tabcolsep}{3.5pt}',
358	        r'\begin{tabular}{llc' + 'rr' * len(EPSILONS) + '}',
359	        r'\toprule',
360	    ]
361	
362	    h1 = r'Topology & $K$ & Q'
363	    for e in EPSILONS:
364	        h1 += rf' & \multicolumn{{2}}{{c}}{{$\varepsilon\!=\!{e}$}}'
365	    lines.append(h1 + r' \\')
366	
367	    clines = ' '.join(
368	        rf'\cmidrule(lr){{{4+2*i}-{5+2*i}}}' for i in range(len(EPSILONS)))
369	    lines.append(clines)
370	
371	    h2 = r' & &'
372	    for _ in EPSILONS:
373	        h2 += r' & {\scriptsize SF} & {\scriptsize BR}'
374	    lines.append(h2 + r' \\')
375	    lines.append(r'\midrule')
376	
377	    for ti, topo in enumerate(TOPOLOGIES):
378	        if ti > 0:
379	            lines.append(r'\midrule')
380	        first_t = True
381	        for ki, K in enumerate(K_VALUES):
382	            if ki > 0:
383	                lines.append(rf'\cmidrule{{2-{ncols}}}')
384	            first_k = True
385	            for qn in CM_QUALS:
386	                TOPO_LABELS = {'confounding': 'Confounding', 'mediation': 'Mediation',
387	                               'exposure': 'Exposure', 'iv': 'IV'}
388	                tl = TOPO_LABELS.get(topo, topo.capitalize()) if first_t else ''
389	                kl = str(K) if first_k else ''
390	                row = f'{tl} & {kl} & {qn[0].upper()}'
391	                for eps in EPSILONS:
392	                    r = next(x for x in results
393	                             if x['topology'] == topo and x['K'] == K
394	                             and x['epsilon'] == eps and x['cm_quality'] == qn)
395	                    sf = r['sign_flip_rate']
396	                    br = r['mean_bias_ratio']
397	                    sfs = f'{sf:.2f}' if sf is not None else '--'
398	                    brs = f'{br:.2f}' if br is not None else '--'
399	                    row += f' & {sfs} & {brs}'
400	                lines.append(row + r' \\')
401	                first_t = False
402	                first_k = False
403	
404	    lines += [
405	        r'\bottomrule',
406	        r'\end{tabular}',
407	        r'\vspace{1mm}',
408	        r'\parbox{\textwidth}{\footnotesize '
409	        r'SF\,=\,sign flip rate; BR\,=\,mean $|\hat\tau/\tau|$ '
410	        r'(1.00 = unbiased). '
411	        r'$\varepsilon\!=\!0$: non-differential; $\varepsilon\!>\!0$: '
412	        r'outcome-dependent misclassification. '
413	        r'Q: H/M/L\,=\,CM diagonal 0.8/0.6/0.4 with uniform off-diagonal. '
414	        r'Each cell: $N\!=\!10{,}000\!\times\!100$ MC replications.}',
415	        r'\end{table*}',
416	    ]
417	    with open(path, 'w') as f:
418	        f.write('\n'.join(lines) + '\n')
419	
420	
421	if __name__ == '__main__':
422	    main()
423	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "d4d44164-83fe-42c5-9386-f058e0167c9d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nExp-A: Non-differential Misclassification Stress Test Expansion\n\nTests sign flip rate and bias ratio under increasing differential\nmisclassification departure ε.\n\n4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs\nN=10,000 × 100 MC reps per config\n\"\"\"\nimport numpy as np\nimport json\nimport time\nimport os\n\nTOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']\nK_VALUES = [3, 10]\nEPSILONS = [0.0, 0.01, 0.05, 0.10]\nCM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}\nN_SAMPLES = 10_000\nN_REPS = 100\nN_LARGE = 2_000_000\nSEED = 42\n\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n\n\ndef softmax_rows(x):\n    e = np.exp(x - x.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / (i + 1) for i in range(K)])\n    return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),\n            'beta_A': np.array(_BETA_A_POOL[:K-1]),\n            'beta_T': 2.0, 'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},\n    }\n    if K == 3:\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3), 'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n    else:\n        iv_b = np.array(_BETA_POOL[:K]) * 0.5\n        iv_b[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_b, 'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i]*0.7 for i in range(K-1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i]*0.6 for i in range(K-1)]),\n        }\n    return params\n\n\n# ── DGP generators ──────────────────────────────────────────\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T']*T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :]*T[:, None]\n    A = sample_cat(softmax_rows(logits), rng)\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau']*T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :]*Z[:, None]\n              + p['dU'][None, :]*U[:, None])\n    A = sample_cat(softmax_rows(logits), rng)\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam']*U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\nGEN = {'confounding': gen_confounding, 'mediation': gen_mediation,\n       'exposure': gen_exposure, 'iv': gen_iv}\n\n\n# ── Estimators ──────────────────────────────────────────────\n\ndef est_tau(topo, fv, Y, Ak, K):\n    N = len(Y)\n    D = np.zeros((N, K-1))\n    for k in range(1, K):\n        D[:, k-1] = (Ak == k).astype(float)\n    if topo == 'iv':\n        z1, z0 = fv == 1, fv == 0\n        if z1.sum() < 2 or z0.sum() < 2:\n            return np.nan\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = D[z1, 0].mean() - D[z0, 0].mean()\n        return RF / FS if abs(FS) > 1e-8 else np.nan\n    elif topo == 'exposure':\n        X = np.column_stack([np.ones(N), D])\n    else:\n        X = np.column_stack([np.ones(N), fv, D])\n    try:\n        return np.linalg.lstsq(X, Y, rcond=None)[0][1]\n    except np.linalg.LinAlgError:\n        return np.nan\n\n\n# ── Confusion matrix construction & perturbation ────────────\n\ndef make_cm(K, diag):\n    C = np.full((K, K), (1.0 - diag) / (K - 1))\n    np.fill_diagonal(C, diag)\n    return C\n\n\ndef perturb(C, eps):\n    K = C.shape[0]\n    Cp = C.copy()\n    Cp[~np.eye(K, dtype=bool)] += eps\n    for j in range(K):\n        Cp[:, j] /= Cp[:, j].sum()\n    return Cp\n\n\ndef gen_Astar(A, Y, Cb, eps, rng):\n    if eps <= 0:\n        probs = Cb[:, A]\n    else:\n        Cp = perturb(Cb, eps)\n        high = Y > np.median(Y)\n        probs = np.where(high[None, :], Cp[:, A], Cb[:, A])\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\n# ── Main ────────────────────────────────────────────────────\n\ndef main():\n    t0 = time.time()\n    out_dir = os.path.dirname(os.path.abspath(__file__))\n    n_total = len(TOPOLOGIES) * len(K_VALUES) * len(EPSILONS) * len(CM_QUALS)\n    print(f\"Exp-A: {n_total} configs x {N_REPS} MC reps, N={N_SAMPLES}\")\n\n    # Validate CMs\n    for K in K_VALUES:\n        for dv in CM_QUALS.values():\n            C = make_cm(K, dv)\n            assert np.allclose(C.sum(axis=0), 1.0), f\"K={K} diag={dv}: bad CM\"\n            for eps in EPSILONS:\n                if eps > 0:\n                    Cp = perturb(C, eps)\n                    assert np.allclose(Cp.sum(axis=0), 1.0)\n                    assert (Cp >= -1e-12).all()\n\n    all_params = {K: make_dgp_params(K) for K in K_VALUES}\n\n    # True parameters (oracle with N=2M)\n    tau_trues = {}\n    print(\"\\nTrue parameters (N=2M oracle):\")\n    for K in K_VALUES:\n        for topo in TOPOLOGIES:\n            rng = np.random.default_rng(K*1000 + abs(hash(topo)) % 1000)\n            fv, Y, A = GEN[topo](K, N_LARGE, all_params[K][topo], rng)\n            tau_trues[(K, topo)] = est_tau(topo, fv, Y, A, K)\n            print(f\"  K={K:>2} {topo:<13} tau_true={tau_trues[(K,topo)]:>10.6f}\")\n\n    # MC simulation\n    results = []\n    idx = 0\n    print(f\"\\nMC simulation ({n_total} configs):\")\n    for topo in TOPOLOGIES:\n        for K in K_VALUES:\n            p = all_params[K][topo]\n            tt = tau_trues[(K, topo)]\n            for qn, dv in CM_QUALS.items():\n                Cb = make_cm(K, dv)\n                for eps in EPSILONS:\n                    idx += 1\n                    rng = np.random.default_rng(SEED + idx*1000)\n                    hats = np.empty(N_REPS)\n                    for m in range(N_REPS):\n                        fv, Y, A = GEN[topo](K, N_SAMPLES, p, rng)\n                        As = gen_Astar(A, Y, Cb, eps, rng)\n                        hats[m] = est_tau(topo, fv, Y, As, K)\n\n                    ok = np.isfinite(hats)\n                    nv = int(ok.sum())\n                    if nv > 0 and abs(tt) > 1e-12:\n                        vh = hats[ok]\n                        sfr = float((np.sign(vh) != np.sign(tt)).mean())\n                        ratios = np.abs(vh / tt)\n                        br = float(ratios.mean())\n                        br_std = float(ratios.std())\n                        br_med = float(np.median(ratios))\n                        mt = float(vh.mean())\n                    else:\n                        sfr = br = br_std = br_med = mt = None\n\n                    results.append({\n                        'topology': topo, 'K': K, 'epsilon': eps,\n                        'cm_quality': qn, 'cm_diag': dv,\n                        'sign_flip_rate': sfr,\n                        'mean_bias_ratio': br,\n                        'std_bias_ratio': br_std,\n                        'median_bias_ratio': br_med,\n                        'tau_true': float(tt),\n                        'mean_tau_hat': mt,\n                        'n_reps': nv,\n                    })\n\n                    if idx % 12 == 0 or idx == n_total:\n                        el = time.time() - t0\n                        eta = el / idx * (n_total - idx)\n                        s = f\"SF={sfr:.3f} BR={br:.3f}\" if sfr is not None else \"N/A\"\n                        print(f\"  [{idx:>3}/{n_total}] {topo:<13} K={K:>2} \"\n                              f\"eps={eps:.2f} {qn:<6} {s}  \"\n                              f\"({el:.0f}s, ETA {eta:.0f}s)\")\n\n    # Summaries\n    def sm(vals):\n        v = [x for x in vals if x is not None]\n        return float(np.mean(v)) if v else None\n\n    by_eps = {}\n    for eps in EPSILONS:\n        sub = [r for r in results if r['epsilon'] == eps]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_eps[str(eps)] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n            'max_sign_flip_rate': float(max(sfs)) if sfs else None,\n        }\n\n    by_topo = {}\n    for topo in TOPOLOGIES:\n        sub = [r for r in results if r['topology'] == topo]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_topo[topo] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n        }\n\n    by_K = {}\n    for K in K_VALUES:\n        sub = [r for r in results if r['K'] == K]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_K[str(K)] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n        }\n\n    output = {\n        'results': results,\n        'summary': {'by_epsilon': by_eps, 'by_topology': by_topo, 'by_K': by_K},\n    }\n\n    def clean(o):\n        if isinstance(o, (float, np.floating)):\n            v = float(o)\n            return None if (np.isnan(v) or np.isinf(v)) else v\n        if isinstance(o, np.integer):\n            return int(o)\n        if isinstance(o, dict):\n            return {k: clean(v) for k, v in o.items()}\n        if isinstance(o, list):\n            return [clean(v) for v in o]\n        return o\n\n    output = clean(output)\n    jpath = os.path.join(out_dir, 'exp_a_stress_test_results.json')\n    with open(jpath, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nJSON -> {jpath}\")\n\n    tpath = os.path.join(out_dir, 'exp_a_stress_test_table.tex')\n    write_tex(results, tpath)\n    print(f\"TeX  -> {tpath}\")\n\n    total = time.time() - t0\n    print(f\"\\nDone in {total:.0f}s ({total/60:.1f}min)\")\n    print(\"\\nBy epsilon:\")\n    for eps, s in by_eps.items():\n        sf = s['mean_sign_flip_rate']\n        br = s['mean_bias_ratio']\n        mx = s['max_sign_flip_rate']\n        print(f\"  eps={eps}: meanSF={sf:.4f} meanBR={br:.4f} maxSF={mx:.4f}\")\n    print(\"\\nBy topology:\")\n    for topo, s in by_topo.items():\n        print(f\"  {topo:<13}: SF={s['mean_sign_flip_rate']:.4f} \"\n              f\"BR={s['mean_bias_ratio']:.4f}\")\n    print(\"\\nBy K:\")\n    for k, s in by_K.items():\n        print(f\"  K={k}: SF={s['mean_sign_flip_rate']:.4f} \"\n              f\"BR={s['mean_bias_ratio']:.4f}\")\n\n\ndef write_tex(results, path):\n    ncols = 3 + 2 * len(EPSILONS)\n    lines = [\n        r'\\begin{table*}[t]',\n        r'\\centering',\n        r'\\caption{Non-differential misclassification stress test: sign flip rate (SF) '\n        r'and mean bias ratio (BR\\,$=\\overline{|\\hat\\tau/\\tau|}$) under increasing '\n        r'differential departure $\\varepsilon$.}',\n        r'\\label{tab:stress-test}',\n        r'\\small\\setlength{\\tabcolsep}{3.5pt}',\n        r'\\begin{tabular}{llc' + 'rr' * len(EPSILONS) + '}',\n        r'\\toprule',\n    ]\n\n    h1 = r'Topology & $K$ & Q'\n    for e in EPSILONS:\n        h1 += rf' & \\multicolumn{{2}}{{c}}{{$\\varepsilon\\!=\\!{e}$}}'\n    lines.append(h1 + r' \\\\')\n\n    clines = ' '.join(\n        rf'\\cmidrule(lr){{{4+2*i}-{5+2*i}}}' for i in range(len(EPSILONS)))\n    lines.append(clines)\n\n    h2 = r' & &'\n    for _ in EPSILONS:\n        h2 += r' & {\\scriptsize SF} & {\\scriptsize BR}'\n    lines.append(h2 + r' \\\\')\n    lines.append(r'\\midrule')\n\n    for ti, topo in enumerate(TOPOLOGIES):\n        if ti > 0:\n            lines.append(r'\\midrule')\n        first_t = True\n        for ki, K in enumerate(K_VALUES):\n            if ki > 0:\n                lines.append(rf'\\cmidrule{{2-{ncols}}}')\n            first_k = True\n            for qn in CM_QUALS:\n                TOPO_LABELS = {'confounding': 'Confounding', 'mediation': 'Mediation',\n                               'exposure': 'Exposure', 'iv': 'IV'}\n                tl = TOPO_LABELS.get(topo, topo.capitalize()) if first_t else ''\n                kl = str(K) if first_k else ''\n                row = f'{tl} & {kl} & {qn[0].upper()}'\n                for eps in EPSILONS:\n                    r = next(x for x in results\n                             if x['topology'] == topo and x['K'] == K\n                             and x['epsilon'] == eps and x['cm_quality'] == qn)\n                    sf = r['sign_flip_rate']\n                    br = r['mean_bias_ratio']\n                    sfs = f'{sf:.2f}' if sf is not None else '--'\n                    brs = f'{br:.2f}' if br is not None else '--'\n                    row += f' & {sfs} & {brs}'\n                lines.append(row + r' \\\\')\n                first_t = False\n                first_k = False\n\n    lines += [\n        r'\\bottomrule',\n        r'\\end{tabular}',\n        r'\\vspace{1mm}',\n        r'\\parbox{\\textwidth}{\\footnotesize '\n        r'SF\\,=\\,sign flip rate; BR\\,=\\,mean $|\\hat\\tau/\\tau|$ '\n        r'(1.00 = unbiased). '\n        r'$\\varepsilon\\!=\\!0$: non-differential; $\\varepsilon\\!>\\!0$: '\n        r'outcome-dependent misclassification. '\n        r'Q: H/M/L\\,=\\,CM diagonal 0.8/0.6/0.4 with uniform off-diagonal. '\n        r'Each cell: $N\\!=\\!10{,}000\\!\\times\\!100$ MC replications.}',\n        r'\\end{table*}',\n    ]\n    with open(path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 423,
      "startLine": 1,
      "totalLines": 423
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

Now let me read the key helper module `exp_d_conjecture_verify_v2.py` to understand the analytic bias computation functions I need to reuse.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "0a50b641-eb49-4139-8160-fb5a7d764dd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVtJS1x1uR9LxvQnbWDa4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19671,
      "cache_read_input_tokens": 26580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19671
      },
      "output_tokens": 4,
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01AGADwmWZyzgyZwphrVwLNN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "28432d83-d971-4a7e-975d-ccbed29c3be4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVtJS1x1uR9LxvQnbWDa4G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19671,
      "cache_read_input_tokens": 26580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19671
      },
      "output_tokens": 4,
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

_source line 14 · 2026-05-23T17:36:59.390Z_

<details><summary>↩ Tool result · `toolu_01AGADwmWZyzgyZwphrVwLNN`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Exp-D v2: Conjecture 1 verification with ANALYTIC plim (zero sampling noise).
4	
5	The original exp_d_conjecture_verify.py computed plim via sufficient statistics
6	estimated from N=5M Monte Carlo simulation, introducing O(1/sqrt(N)) ~ 0.0004
7	sampling noise. At MONO_TOL=1e-8, this generated ~141k false monotonicity
8	violations.
9	
10	This v2 computes ALL sufficient statistics analytically (closed-form for
11	confounding/mediation/exposure, Gauss-Hermite quadrature for collider/mbias/
12	frontdoor/iv), eliminating sampling noise entirely.
13	
14	Topology-specific analytics:
15	  - confounding: fully analytic (categorical A, linear T and Y)
16	  - exposure:    fully analytic (categorical A, linear Y)
17	  - mediation:   fully analytic (binary T, softmax A|T, linear Y)
18	  - collider:    2D Gauss-Hermite over (T, eps_Y), both N(0,1)
19	  - mbias:       2D Gauss-Hermite over (U1, U2), both N(0,1)
20	  - frontdoor:   1D Gauss-Hermite over T ~ N(0, alpha_U^2 + 1)
21	  - iv:          1D Gauss-Hermite over U ~ N(0,1), with binary Z
22	
23	Output: exp_d_conjecture_results_v2.json (same structure as v1)
24	"""
25	
26	import numpy as np
27	import json
28	import time
29	import sys
30	import os
31	from scipy.special import roots_hermite, softmax as scipy_softmax
32	from scipy.optimize import minimize as scipy_minimize
33	
34	# ====================================================================
35	# Gauss-Hermite quadrature setup
36	# ====================================================================
37	N_GH = 100  # points per dimension -- machine precision for smooth integrands
38	
39	# roots_hermite: physicist's convention, weight = exp(-x^2)
40	# integral f(x) exp(-x^2) dx ~ sum w_i f(x_i)
41	# For N(0,1) expectation: E[f(X)] = (1/sqrt(pi)) sum w_i f(x_i * sqrt(2))
42	_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)
43	GH_X = _gh_x_raw * np.sqrt(2)   # rescaled nodes for N(0,1)
44	GH_W = _gh_w_raw / np.sqrt(np.pi)  # rescaled weights: sum w_i f(x_i) = E_{N(0,1)}[f]
45	
46	# Verify: E[1] should be 1.0, E[X^2] should be 1.0
47	assert abs(GH_W.sum() - 1.0) < 1e-12, f"GH weights sum to {GH_W.sum()}, expected 1.0"
48	assert abs((GH_W * GH_X**2).sum() - 1.0) < 1e-10, "GH E[X^2] != 1.0"
49	
50	# 2D quadrature: outer product of 1D grids
51	GH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')  # (N_GH, N_GH)
52	GH_W2 = np.outer(GH_W, GH_W)  # (N_GH, N_GH)
53	GH_X2_a_flat = GH_X2_a.ravel()
54	GH_X2_b_flat = GH_X2_b.ravel()
55	GH_W2_flat = GH_W2.ravel()
56	
57	# ====================================================================
58	# Configuration
59	# ====================================================================
60	K_VALUES = [3, 5, 7]
61	K_ADVERSARIAL = [3, 5]
62	N_RANDOM = 10_000
63	DELTA_STEP = 0.01
64	SEED = 12345
65	MONO_TOL = 1e-12  # much tighter than v1's 1e-8 since we have zero sampling noise
66	
67	ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
68	             'mbias', 'iv', 'frontdoor']
69	TOPO_IDX = {t: i for i, t in enumerate(ALL_TOPOS)}
70	NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
71	NON_INCREASING = {'collider', 'mbias'}
72	
73	ADV_DELTA_PAIRS = [(0.0, 0.2), (0.0, 0.5), (0.1, 0.3), (0.2, 0.5), (0.3, 0.7)]
74	ADV_N_STARTS = 100
75	
76	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
77	
78	# ====================================================================
79	# DGP Parameter Pools (identical to v1)
80	# ====================================================================
81	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
82	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
83	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
84	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
85	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
86	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
87	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
88	_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]
89	_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]
90	_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]
91	_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]
92	_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
93	_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]
94	
95	
96	def make_p_A(K):
97	    if K == 3:
98	        return np.array([0.40, 0.35, 0.25])
99	    raw = np.array([1.0 / i for i in range(1, K + 1)])
100	    return raw / raw.sum()
101	
102	
103	def make_all_params(K):
104	    p_A = make_p_A(K)
105	    return dict(
106	        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),
107	                         beta_A=np.array(_BETA_A_POOL[:K - 1]), beta_T=2.0, sigma_T=1.0),
108	        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),
109	                       delta=np.array(_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
110	        collider=dict(tau=1.0, g=np.zeros(K), dT=np.array(_DT_POOL[:K]),
111	                      dY=np.array(_DY_POOL[:K])),
112	        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),
113	        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
114	                   a1=np.array(_MBIAS_A1_POOL[:K]), a2=np.array(_MBIAS_A2_POOL[:K])),
115	        iv=dict(lam=1.0, g=np.zeros(K), dZ=np.array(_IV_DZ_POOL[:K]),
116	                dU=np.array(_IV_DU_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
117	        frontdoor=dict(alpha_U=1.0, lam_U=1.0, gamma=np.array(_FD_GAMMA_POOL[:K]),
118	                       delta=np.array(_FD_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
119	    )
120	
121	
122	# ====================================================================
123	# Stable softmax utility
124	# ====================================================================
125	def _softmax(logits):
126	    """Softmax along last axis, numerically stable."""
127	    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
128	    return e / np.sum(e, axis=-1, keepdims=True)
129	
130	
131	# ====================================================================
132	# Analytic Sufficient Statistics classes
133	# ====================================================================
134	class AnalyticSuffStats:
135	    """Population moments for OLS topologies (with or without T)."""
136	    def __init__(self, K, has_T=True):
137	        self.K = K
138	        self.has_T = has_T
139	        self.p_A = None   # K-vector: P(A=k)
140	        self.E_Y = None   # scalar
141	        self.E_YD = None  # K-vector: E[Y * 1(A=k)]
142	        if has_T:
143	            self.E_T = None   # scalar
144	            self.E_T2 = None  # scalar: E[T^2]
145	            self.E_TY = None  # scalar: E[T*Y]
146	            self.E_TD = None  # K-vector: E[T * 1(A=k)]
147	
148	
149	class AnalyticIVSuffStats:
150	    """Population moments for IV topology (Wald estimator)."""
151	    def __init__(self, K):
152	        self.K = K
153	        self.RF = None   # E[Y|Z=1] - E[Y|Z=0]
154	        self.FS = None   # K-vector: P(A=k|Z=1) - P(A=k|Z=0)
155	
156	
157	# ====================================================================
158	# Topology 1: Confounding -- FULLY ANALYTIC
159	# ====================================================================
160	# DGP: A ~ Cat(p_A), T = sum_{j=1}^{K-1} alpha_j D_j + eps_T,
161	#       Y = beta_T * T + sum_{j=1}^{K-1} beta_A_j D_j + eps_Y
162	# D_j = 1(A=j+1) for j=0,...,K-2 (ref category A=0)
163	# Wait -- looking at original code more carefully:
164	#   D[:, j] = (A == j + 1) for j in range(K-1)
165	# So D_j = 1(A = j+1), j=0,...,K-2
166	# T = D @ alpha + eps_T = sum_{j=0}^{K-2} alpha_j * 1(A=j+1) + eps_T
167	# Y = beta_T * T + D @ beta_A + eps_Y = beta_T * T + sum_{j=0}^{K-2} beta_A_j * 1(A=j+1) + eps_Y
168	#
169	# For the plim regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}:
170	# D*_j = 1(A* = j) for j=1,...,K-1 (ref category A*=0)
171	# The sufficient stats use A (not A*), and the C matrix maps A->A*.
172	# Actually looking at the SuffStats class: DA[:, k] = (A == k) for k=0,...,K-1
173	# So p_A[k] = P(A=k), E_TD[k] = E[T * 1(A=k)], E_YD[k] = E[Y * 1(A=k)]
174	
175	def compute_confounding_ss(K, p):
176	    """Analytic sufficient stats for confounding topology."""
177	    ss = AnalyticSuffStats(K, has_T=True)
178	    p_A = p['p_A']       # K-vector
179	    alpha = p['alpha']    # (K-1)-vector: alpha_0,...,alpha_{K-2}
180	    beta_A = p['beta_A']  # (K-1)-vector
181	    beta_T = p['beta_T']
182	    sigma_T = p['sigma_T']
183	
184	    ss.p_A = p_A.copy()
185	
186	    # E[T] = sum_{j=0}^{K-2} alpha_j * P(A=j+1)
187	    # (since eps_T has mean 0)
188	    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))
189	
190	    # E[T^2] = E[(sum alpha_j D_j)^2] + sigma_T^2
191	    # = sum_j alpha_j^2 P(A=j+1) + sigma_T^2
192	    # (since D_j D_k = 0 for j!=k, D_j^2 = D_j)
193	    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2
194	
195	    # E[T * 1(A=k)]:
196	    # For k=0: E[(sum alpha_j D_j + eps_T) * 1(A=0)]
197	    #        = sum_j alpha_j E[D_j * 1(A=0)] + E[eps_T * 1(A=0)]
198	    #        = 0 + 0 = 0  (since D_j=1(A=j+1) and A=0 => D_j=0, and eps_T indep of A)
199	    # Actually eps_T is independent of A, so E[eps_T * 1(A=k)] = 0 * P(A=k) = 0
200	    # For k>=1: E[(sum_j alpha_j D_j + eps_T) * 1(A=k)]
201	    #         = alpha_{k-1} * P(A=k) + 0
202	    ss.E_TD = np.zeros(K)
203	    for k in range(1, K):
204	        ss.E_TD[k] = alpha[k - 1] * p_A[k]
205	
206	    # E[Y] = beta_T * E[T] + sum_{j=0}^{K-2} beta_A_j * P(A=j+1)
207	    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))
208	
209	    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + sum_j beta_A_j * E[D_j * 1(A=k)] + E[eps_Y * 1(A=k)]
210	    # E[D_j * 1(A=k)] = P(A=j+1, A=k) = P(A=k) if j+1=k else 0
211	    # E[eps_Y * 1(A=k)] = 0
212	    # So for k=0: E[Y * 1(A=0)] = beta_T * 0 + 0 + 0 = 0 ... wait that's wrong
213	    # Actually: Y = beta_T * T + sum beta_A_j D_j + eps_Y
214	    # E[Y * 1(A=0)] = beta_T * E[T * 1(A=0)] + sum_j beta_A_j * E[D_j * 1(A=0)] + E[eps_Y * 1(A=0)]
215	    #               = beta_T * 0 + 0 + 0 = 0
216	    # Hmm, that gives E_Y = sum_k E[Y * 1(A=k)] = 0 + sum_{k>=1} stuff, but we need E_Y correctly.
217	    # Let me reconsider: the intercept in the Y equation.
218	    # gen_confounding: Y = beta_T * T + D @ beta_A + eps_Y
219	    # There's no explicit intercept in Y. So E[Y | A=0] = beta_T * E[T | A=0] + 0
220	    # E[T | A=0] = 0 (since all alpha terms vanish) + E[eps_T] = 0
221	    # So E[Y * 1(A=0)] = E[Y | A=0] * P(A=0) = 0 * p_A[0] = 0
222	    # That seems correct.
223	
224	    # For k >= 1:
225	    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + beta_A[k-1] * P(A=k)
226	    ss.E_YD = np.zeros(K)
227	    for k in range(1, K):
228	        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]
229	    # k=0: already 0
230	
231	    # E[TY] = E[T * (beta_T * T + sum beta_A_j D_j + eps_Y)]
232	    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * D_j] + E[T * eps_Y]
233	    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * 1(A=j+1)] + 0
234	    ss.E_TY = beta_T * ss.E_T2 + sum(beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))
235	
236	    return ss
237	
238	
239	# ====================================================================
240	# Topology 2: Exposure -- FULLY ANALYTIC
241	# ====================================================================
242	# DGP: A ~ Cat(p_A), Y = beta[0] + D @ beta[1:] + eps_Y
243	# No T variable.
244	
245	def compute_exposure_ss(K, p):
246	    """Analytic sufficient stats for exposure topology."""
247	    ss = AnalyticSuffStats(K, has_T=False)
248	    p_A = p['p_A']
249	    beta = p['beta']  # K-vector: beta[0] is intercept
250	
251	    ss.p_A = p_A.copy()
252	
253	    # E[Y] = beta[0] + sum_{j=1}^{K-1} beta[j] * P(A=j)
254	    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))
255	
256	    # E[Y * 1(A=k)] = E[(beta[0] + sum_j beta[j] D_j + eps_Y) * 1(A=k)]
257	    # = beta[0] * P(A=k) + beta[k] * P(A=k) (if k>=1) + 0
258	    # For k=0: = beta[0] * P(A=0) + 0 = beta[0] * p_A[0]
259	    ss.E_YD = np.zeros(K)
260	    ss.E_YD[0] = beta[0] * p_A[0]
261	    for k in range(1, K):
262	        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]
263	
264	    return ss
265	
266	
267	# ====================================================================
268	# Topology 3: Mediation -- FULLY ANALYTIC (T is binary)
269	# ====================================================================
270	# DGP: T ~ Bern(0.5), A | T ~ Cat(softmax(gamma + delta * T))
271	#       Y = beta[0] + D @ beta[1:] + tau * T + eps_Y
272	# D_j = 1(A = j+1) for j=0,...,K-2
273	
274	def compute_mediation_ss(K, p):
275	    """Analytic sufficient stats for mediation topology."""
276	    ss = AnalyticSuffStats(K, has_T=True)
277	    tau = p['tau']
278	    gamma = p['gamma']  # K-vector
279	    delta_coef = p['delta']   # K-vector
280	    beta = p['beta']    # K-vector
281	
282	    # P(A=k | T=t) = softmax(gamma + delta * t)[k]
283	    probs_T0 = _softmax(gamma)          # K-vector
284	    probs_T1 = _softmax(gamma + delta_coef)  # K-vector
285	
286	    # P(A=k) = 0.5 * P(A=k|T=0) + 0.5 * P(A=k|T=1)
287	    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1
288	
289	    # E[T] = 0.5, E[T^2] = 0.5 (since T is Bernoulli(0.5))
290	    ss.E_T = 0.5
291	    ss.E_T2 = 0.5
292	
293	    # E[T * 1(A=k)] = E[T * 1(A=k)]
294	    # = 0.5 * 0 * P(A=k|T=0) + 0.5 * 1 * P(A=k|T=1)
295	    # = 0.5 * probs_T1[k]
296	    ss.E_TD = 0.5 * probs_T1
297	
298	    # E[Y] = beta[0] + sum_{k=1}^{K-1} beta[k] * P(A=k) + tau * E[T]
299	    # Wait, gen_mediation:
300	    #   Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + eps_Y
301	    # D_j = 1(A=j+1), so D @ beta[1:] = sum_{j=0}^{K-2} beta[j+1] * 1(A=j+1)
302	    # = sum_{k=1}^{K-1} beta[k] * 1(A=k)
303	    ss.E_Y = beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K)) + tau * 0.5
304	
305	    # E[Y * 1(A=k)] for each k:
306	    # Y = beta[0] + sum_j beta[j+1]*D_j + tau*T + eps_Y
307	    # E[Y * 1(A=k)] = E[(beta[0] + beta[k]*1(k>=1) + tau*T + eps_Y) * 1(A=k)]
308	    # = (beta[0] + beta[k]*(k>=1)) * P(A=k) + tau * E[T * 1(A=k)]
309	
310	    ss.E_YD = np.zeros(K)
311	    for k in range(K):
312	        beta_k = beta[k] if k >= 1 else 0.0
313	        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]
314	
315	    # E[TY] = E[T * (beta[0] + sum beta[k]*1(A=k) + tau*T + eps_Y)]
316	    # = beta[0] * E[T] + sum_{k=1}^{K-1} beta[k] * E[T * 1(A=k)] + tau * E[T^2] + 0
317	    ss.E_TY = beta[0] * 0.5 + sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + tau * 0.5
318	
319	    return ss
320	
321	
322	# ====================================================================
323	# Topology 4: Collider -- 2D GAUSS-HERMITE
324	# ====================================================================
325	# DGP: T ~ N(0,1), eps_Y ~ N(0,1) independent
326	#       Y = tau * T + eps_Y
327	#       A | T, Y ~ Cat(softmax(g + dT * T + dY * Y))
328	#
329	# Reparametrize: let Z1=T, Z2=eps_Y, both N(0,1) independent
330	# Y = tau * Z1 + Z2
331	# A | Z1, Z2 ~ Cat(softmax(g + dT * Z1 + dY * (tau * Z1 + Z2)))
332	#            = Cat(softmax(g + (dT + tau * dY) * Z1 + dY * Z2))
333	
334	def compute_collider_ss(K, p):
335	    """Analytic sufficient stats for collider via 2D GH quadrature."""
336	    ss = AnalyticSuffStats(K, has_T=True)
337	    tau = p['tau']
338	    g = p['g']      # K-vector
339	    dT = p['dT']    # K-vector
340	    dY = p['dY']    # K-vector
341	
342	    # Quadrature over (Z1, Z2) = (T, eps_Y), both N(0,1)
343	    # Logits for each quadrature point: g + (dT + tau*dY) * Z1 + dY * Z2
344	    coeff1 = dT + tau * dY   # K-vector: coefficient of Z1
345	    coeff2 = dY               # K-vector: coefficient of Z2
346	
347	    # Compute softmax probabilities at each quadrature point
348	    # logits shape: (N_GH^2, K)
349	    logits = (g[None, :]
350	              + coeff1[None, :] * GH_X2_a_flat[:, None]
351	              + coeff2[None, :] * GH_X2_b_flat[:, None])
352	    probs = _softmax(logits)  # (N_GH^2, K)
353	
354	    # T = Z1, Y = tau * Z1 + Z2
355	    T_vals = GH_X2_a_flat
356	    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat
357	
358	    # Weighted expectations
359	    w = GH_W2_flat  # (N_GH^2,)
360	
361	    ss.p_A = (w[:, None] * probs).sum(axis=0)
362	    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
363	    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)
364	
365	    # Moments of T and Y (independent of A, can compute analytically):
366	    ss.E_T = 0.0
367	    ss.E_T2 = 1.0
368	    ss.E_Y = 0.0  # E[tau*T + eps] = 0
369	    ss.E_TY = tau  # E[T(tau*T + eps)] = tau * E[T^2] = tau
370	
371	    return ss
372	
373	
374	# ====================================================================
375	# Topology 5: M-bias -- 2D GAUSS-HERMITE
376	# ====================================================================
377	# DGP: U1, U2 ~ N(0,1) independent
378	#       T = delta_coef * U1 + eta, eta ~ N(0,1)
379	#       Y = tau * T + lam * U2 + eps_Y, eps_Y ~ N(0,1)
380	#       A | U1, U2 ~ Cat(softmax(g + a1 * U1 + a2 * U2))
381	#
382	# Note: T and Y depend on (U1, U2, eta, eps_Y) but A only depends on (U1, U2).
383	# Since eta, eps_Y are independent of (U1, U2, A):
384	#   E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)] + E[eta * 1(A=k)]
385	#                  = delta_coef * E[U1 * 1(A=k)]  (eta indep of A)
386	#
387	#   E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)] + 0
388	#
389	# So we need 2D GH over (U1, U2) to compute:
390	#   P(A=k), E[U1 * 1(A=k)], E[U2 * 1(A=k)]
391	
392	def compute_mbias_ss(K, p):
393	    """Analytic sufficient stats for M-bias via 2D GH quadrature."""
394	    ss = AnalyticSuffStats(K, has_T=True)
395	    tau = p['tau']
396	    delta_coef = p['delta_coef']
397	    lam = p['lam']
398	    g = p['g']
399	    a1 = p['a1']
400	    a2 = p['a2']
401	
402	    # Logits: g + a1 * U1 + a2 * U2
403	    logits = (g[None, :]
404	              + a1[None, :] * GH_X2_a_flat[:, None]
405	              + a2[None, :] * GH_X2_b_flat[:, None])
406	    probs = _softmax(logits)  # (N_GH^2, K)
407	
408	    w = GH_W2_flat
409	    U1_vals = GH_X2_a_flat
410	    U2_vals = GH_X2_b_flat
411	
412	    ss.p_A = (w[:, None] * probs).sum(axis=0)
413	    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)  # E[U1 * 1(A=k)]
414	    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)  # E[U2 * 1(A=k)]
415	
416	    # E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)]
417	    ss.E_TD = delta_coef * E_U1_Dk
418	
419	    # E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)]
420	    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk
421	
422	    # Marginal moments:
423	    # E[T] = 0 (since E[U1]=0, E[eta]=0)
424	    # E[T^2] = delta_coef^2 * E[U1^2] + E[eta^2] = delta_coef^2 + 1
425	    # E[Y] = 0
426	    # E[TY] = tau * E[T^2] + lam * E[T*U2]
427	    # E[T*U2] = E[(delta_coef * U1 + eta) * U2] = 0 (all independent)
428	    ss.E_T = 0.0
429	    ss.E_T2 = delta_coef**2 + 1.0
430	    ss.E_Y = 0.0
431	    ss.E_TY = tau * ss.E_T2
432	
433	    return ss
434	
435	
436	# ====================================================================
437	# Topology 6: Front-door -- 1D GAUSS-HERMITE
438	# ====================================================================
439	# DGP: U ~ N(0,1), T = alpha_U * U + eta (eta ~ N(0,1))
440	#       M | T ~ Cat(softmax(gamma + delta * T))  -- M is the "annotator" variable
441	#       Y = D_M @ beta[1:] + lam_U * U + eps_Y
442	# where D_M[j] = 1(M=j+1), j=0,...,K-2
443	#
444	# The regression is Y ~ 1 + T + D*_1 + ... + D*_{K-1}
445	# (M plays the role of A in the plim computation)
446	#
447	# T ~ N(0, sigma_T^2) where sigma_T^2 = alpha_U^2 + 1
448	# We do 1D GH over T (after rescaling for its variance).
449	#
450	# For the moments involving U:
451	# E[U | T] = Cov(U,T)/Var(T) * T = alpha_U / (alpha_U^2 + 1) * T
452	# (since Cov(U,T) = alpha_U, Var(T) = alpha_U^2 + 1)
453	#
454	# P(M=k) = E_T[softmax(gamma + delta * T)[k]]
455	# E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]
456	# E[Y * 1(M=k)] = E[E[Y | T, M] * 1(M=k)]
457	#               = E_T[ E[Y|T,M=k] * softmax(gamma+delta*T)[k] ]
458	# E[Y|T,M=k] = beta[k] (if k>=1, else 0 for the intercept part from D_M)
459	#              + lam_U * E[U|T] + 0
460	# Wait, let me reconsider:
461	# Y = sum_{j=0}^{K-2} beta[j+1] * 1(M=j+1) + lam_U * U + eps_Y
462	# (from gen_frontdoor: Y = D @ beta[1:] + lam_U * U + eps_Y,
463	#  where beta = p['beta'] and D[j] = 1(M=j+1))
464	# There's no intercept beta[0] in the Y equation in gen_frontdoor!
465	# Let me re-check: gen_frontdoor has Y = D @ p['beta'][1:] + p['lam_U'] * U + eps_Y
466	# So Y = sum_{k=1}^{K-1} beta[k] * 1(M=k) + lam_U * U + eps_Y
467	#
468	# E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)] + 0
469	# For k=0: E[Y * 1(M=0)] = 0 + lam_U * E[U * 1(M=0)] + 0
470	
471	def compute_frontdoor_ss(K, p):
472	    """Analytic sufficient stats for front-door via 1D GH quadrature."""
473	    ss = AnalyticSuffStats(K, has_T=True)
474	    alpha_U = p['alpha_U']
475	    lam_U = p['lam_U']
476	    gamma = p['gamma']
477	    delta_coef = p['delta']
478	    beta = p['beta']
479	
480	    sigma_T2 = alpha_U**2 + 1.0
481	    sigma_T = np.sqrt(sigma_T2)
482	
483	    # 1D GH over T ~ N(0, sigma_T^2): rescale nodes
484	    T_nodes = GH_X * sigma_T  # (N_GH,)
485	    T_weights = GH_W          # (N_GH,) -- already normalized for E_{N(0,1)}
486	
487	    # softmax(gamma + delta * T) at each T node
488	    # logits shape: (N_GH, K)
489	    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
490	    probs = _softmax(logits)  # (N_GH, K)
491	
492	    # P(M=k) = E_T[softmax(gamma + delta * T)[k]]
493	    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)
494	
495	    # E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]
496	    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)
497	
498	    # E[U * 1(M=k)] via the law of iterated expectations:
499	    # E[U * 1(M=k)] = E_T[ E[U|T] * P(M=k|T) ]
500	    # E[U|T] = alpha_U / sigma_T^2 * T
501	    E_U_given_T = alpha_U / sigma_T2 * T_nodes  # (N_GH,)
502	    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)
503	
504	    # E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)]
505	    ss.E_YD = np.zeros(K)
506	    for k in range(K):
507	        beta_k = beta[k] if k >= 1 else 0.0
508	        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]
509	
510	    # Marginal moments:
511	    # E[T] = 0
512	    # E[T^2] = sigma_T^2
513	    # E[Y] = sum_{k=1}^{K-1} beta[k] * P(M=k) + lam_U * E[U] + 0
514	    #       = sum_{k=1}^{K-1} beta[k] * P(M=k)
515	    ss.E_T = 0.0
516	    ss.E_T2 = sigma_T2
517	    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))
518	
519	    # E[TY] = sum_{k=1}^{K-1} beta[k] * E[T * 1(M=k)] + lam_U * E[T*U] + E[T*eps_Y]
520	    # E[T*U] = Cov(T,U) = alpha_U (since both mean 0)
521	    # E[T*eps_Y] = 0
522	    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U
523	
524	    return ss
525	
526	
527	# ====================================================================
528	# Topology 7: IV -- 1D GAUSS-HERMITE over U, binary Z
529	# ====================================================================
530	# DGP: Z ~ Bern(0.5), U ~ N(0,1), eps_Y ~ N(0,1)
531	#       A | Z, U ~ Cat(softmax(g + dZ * Z + dU * U))
532	#       Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps_Y
533	#
534	# Wald estimator: tau_hat = RF / FS*[1]
535	# RF = E[Y|Z=1] - E[Y|Z=0]
536	# FS[k] = P(A=k|Z=1) - P(A=k|Z=0)
537	#
538	# P(A=k|Z=z) = E_U[softmax(g + dZ * z + dU * U)[k]]
539	# E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z) + lam * E[U] + E[eps]
540	#           = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)
541	
542	def compute_iv_ss(K, p):
543	    """Analytic sufficient stats for IV via 1D GH quadrature."""
544	    ivss = AnalyticIVSuffStats(K)
545	    g = p['g']
546	    dZ = p['dZ']
547	    dU = p['dU']
548	    beta = p['beta']
549	    lam = p['lam']
550	
551	    # P(A=k|Z=z) for z=0 and z=1
552	    # logits for Z=0: g + dU * U
553	    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]  # (N_GH, K)
554	    probs_z0 = _softmax(logits_z0)
555	    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)  # K-vector
556	
557	    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]
558	    probs_z1 = _softmax(logits_z1)
559	    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)  # K-vector
560	
561	    # First stage
562	    ivss.FS = P_A_z1 - P_A_z0  # K-vector
563	
564	    # Reduced form
565	    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)
566	    # (lam * E[U] = 0, E[eps] = 0, beta[0] cancels out since it's not in gen_iv)
567	    # Actually gen_iv: Y = D @ p['beta'][1:] + p['lam'] * U + eps
568	    # So Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps
569	    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)
570	    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))
571	    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))
572	
573	    ivss.RF = E_Y_z1 - E_Y_z0
574	
575	    return ivss
576	
577	
578	# ====================================================================
579	# Plim computation (from original, unchanged)
580	# ====================================================================
581	def plim_ols_with_T(C, ss):
582	    """Plim of OLS regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
583	    K = ss.K
584	    q = C @ ss.p_A        # misclassified P(A*=k)
585	    ct = C @ ss.E_TD       # E[T * 1(A*=k)]
586	    cy = C @ ss.E_YD       # E[Y * 1(A*=k)]
587	    dim = K + 1
588	    EZZ = np.zeros((dim, dim))
589	    EZZ[0, 0] = 1.0
590	    EZZ[0, 1] = ss.E_T
591	    EZZ[1, 0] = ss.E_T
592	    EZZ[1, 1] = ss.E_T2
593	    EZZ[0, 2:] = q[1:]
594	    EZZ[2:, 0] = q[1:]
595	    EZZ[1, 2:] = ct[1:]
596	    EZZ[2:, 1] = ct[1:]
597	    for j in range(K - 1):
598	        EZZ[j + 2, j + 2] = q[j + 1]
599	    EZY = np.zeros(dim)
600	    EZY[0] = ss.E_Y
601	    EZY[1] = ss.E_TY
602	    EZY[2:] = cy[1:]
603	    try:
604	        return np.linalg.solve(EZZ, EZY)
605	    except np.linalg.LinAlgError:
606	        return np.full(dim, np.nan)
607	
608	
609	def plim_ols_exposure(C, ss):
610	    """Plim of OLS regression Y ~ 1 + D*_1 + ... + D*_{K-1}."""
611	    K = ss.K
612	    q = C @ ss.p_A
613	    cy = C @ ss.E_YD
614	    dim = K
615	    EZZ = np.zeros((dim, dim))
616	    EZZ[0, 0] = 1.0
617	    EZZ[0, 1:] = q[1:]
618	    EZZ[1:, 0] = q[1:]
619	    for j in range(K - 1):
620	        EZZ[j + 1, j + 1] = q[j + 1]
621	    EZY = np.zeros(dim)
622	    EZY[0] = ss.E_Y
623	    EZY[1:] = cy[1:]
624	    try:
625	        return np.linalg.solve(EZZ, EZY)
626	    except np.linalg.LinAlgError:
627	        return np.full(dim, np.nan)
628	
629	
630	def plim_iv_single(C, ss):
631	    """Plim of Wald IV estimator with misclassified A."""
632	    FS_star = C @ ss.FS
633	    if abs(FS_star[1]) < 1e-15:
634	        return np.nan
635	    return ss.RF / FS_star[1]
636	
637	
638	def get_tau_at_C(topo, C, ss):
639	    if topo == 'iv':
640	        return plim_iv_single(C, ss)
641	    elif topo == 'exposure':
642	        return plim_ols_exposure(C, ss)[1]
643	    else:
644	        return plim_ols_with_T(C, ss)[1]
645	
646	
647	def get_tau_true(topo, K, params, ss):
648	    """True causal parameter.
649	
650	    For correctly-identified topologies: tau_true = plim(I).
651	    For protective topologies (collider, mbias): tau_true = DGP tau,
652	    so B(0) = plim(I) - tau != 0 (existing bias from Berkson/M-bias).
653	    """
654	    p = params[topo]
655	    if topo == 'collider':
656	        return p['tau']
657	    elif topo == 'mbias':
658	        return p['tau']
659	    else:
660	        return get_tau_at_C(topo, np.eye(K), ss)
661	
662	
663	# ====================================================================
664	# Batched bias curve computation (from original, unchanged)
665	# ====================================================================
666	def compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):
667	    K = C0.shape[0]
668	    min_diag = np.diag(C0).min()
669	    if min_diag >= 1.0:
670	        delta_max = 10.0
671	    else:
672	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
673	
674	    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)
675	    n = len(deltas)
676	    d = deltas[:, None]
677	
678	    if topo == 'iv':
679	        FS0 = C0 @ ss.FS
680	        fs_star = (1 - d) * ss.FS[None, :] + d * FS0[None, :]
681	        denom = fs_star[:, 1]
682	        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
683	    elif topo == 'exposure':
684	        pA0 = C0 @ ss.p_A
685	        YD0 = C0 @ ss.E_YD
686	        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
687	        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
688	        dim = K
689	        EZZ = np.zeros((n, dim, dim))
690	        EZZ[:, 0, 0] = 1.0
691	        EZZ[:, 0, 1:] = q[:, 1:]
692	        EZZ[:, 1:, 0] = q[:, 1:]
693	        for j in range(K - 1):
694	            EZZ[:, j + 1, j + 1] = q[:, j + 1]
695	        EZY = np.zeros((n, dim))
696	        EZY[:, 0] = ss.E_Y
697	        EZY[:, 1:] = cy[:, 1:]
698	        try:
699	            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
700	            taus = coefs[:, 1]
701	        except np.linalg.LinAlgError:
702	            taus = np.full(n, np.nan)
703	    else:
704	        pA0 = C0 @ ss.p_A
705	        TD0 = C0 @ ss.E_TD
706	        YD0 = C0 @ ss.E_YD
707	        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
708	        ct = (1 - d) * ss.E_TD[None, :] + d * TD0[None, :]
709	        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
710	        dim = K + 1
711	        EZZ = np.zeros((n, dim, dim))
712	        EZZ[:, 0, 0] = 1.0
713	        EZZ[:, 0, 1] = ss.E_T
714	        EZZ[:, 1, 0] = ss.E_T
715	        EZZ[:, 1, 1] = ss.E_T2
716	        EZZ[:, 0, 2:] = q[:, 1:]
717	        EZZ[:, 2:, 0] = q[:, 1:]
718	        EZZ[:, 1, 2:] = ct[:, 1:]
719	        EZZ[:, 2:, 1] = ct[:, 1:]
720	        for j in range(K - 1):
721	            EZZ[:, j + 2, j + 2] = q[:, j + 1]
722	        EZY = np.zeros((n, dim))
723	        EZY[:, 0] = ss.E_Y
724	        EZY[:, 1] = ss.E_TY
725	        EZY[:, 2:] = cy[:, 1:]
726	        try:
727	            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
728	            taus = coefs[:, 1]
729	        except np.linalg.LinAlgError:
730	            taus = np.full(n, np.nan)
731	
732	    bias_abs = np.abs(taus - tau_true)
733	    return deltas, bias_abs
734	
735	
736	def check_monotonicity(bias_abs, topo, tol=MONO_TOL):
737	    valid = ~np.isnan(bias_abs)
738	    ba = bias_abs[valid]
739	    if len(ba) < 2:
740	        return 0
741	    diffs = np.diff(ba)
742	    if topo in NON_DECREASING:
743	        return int(np.sum(diffs < -tol))
744	    else:
745	        return int(np.sum(diffs > tol))
746	
747	
748	# ====================================================================
749	# Precompute analytic sufficient statistics
750	# ====================================================================
751	_COMPUTE_SS = {
752	    'confounding': lambda K, p: compute_confounding_ss(K, p),
753	    'mediation':   lambda K, p: compute_mediation_ss(K, p),
754	    'collider':    lambda K, p: compute_collider_ss(K, p),
755	    'exposure':    lambda K, p: compute_exposure_ss(K, p),
756	    'mbias':       lambda K, p: compute_mbias_ss(K, p),
757	    'iv':          lambda K, p: compute_iv_ss(K, p),
758	    'frontdoor':   lambda K, p: compute_frontdoor_ss(K, p),
759	}
760	
761	
762	def precompute_all():
763	    print("\nPrecomputing analytic sufficient statistics...")
764	    sys.stdout.flush()
765	    t0 = time.time()
766	    all_ss = {}
767	    all_tau_true = {}
768	
769	    for K in K_VALUES:
770	        params = make_all_params(K)
771	        for topo in ALL_TOPOS:
772	            ss = _COMPUTE_SS[topo](K, params[topo])
773	            tau_true = get_tau_true(topo, K, params, ss)
774	            all_ss[(topo, K)] = ss
775	            all_tau_true[(topo, K)] = tau_true
776	
777	    print("  Done ({:.3f}s). tau_true values:".format(time.time() - t0))
778	    for topo in ALL_TOPOS:
779	        vals = [all_tau_true[(topo, K)] for K in K_VALUES]
780	        vals_s = ", ".join(
781	            f"K{K}={v:.10f}" if v is not None and not np.isnan(v) else f"K{K}=NaN"
782	            for K, v in zip(K_VALUES, vals))
783	        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
784	        print(f"    {topo:<14} [{direction}] {vals_s}")
785	    sys.stdout.flush()
786	    return all_ss, all_tau_true
787	
788	
789	# ====================================================================
790	# Part 1: Random Verification
791	# ====================================================================
792	def part1_random(all_ss, all_tau_true):
793	    print("\n" + "=" * 70)
794	    print("PART 1: Random Verification ({:,} C0 per topology x K)".format(N_RANDOM))
795	    print("  MONO_TOL = {:.0e} (analytic -- zero sampling noise)".format(MONO_TOL))
796	    print("=" * 70)
797	    sys.stdout.flush()
798	
799	    results = {}
800	    total_tests = 0
801	    total_violations = 0
802	
803	    for K in K_VALUES:
804	        print(f"\n  K = {K}")
805	        print(f"  {'Topology':<14} {'Direction':<10} {'Tested':>8} "
806	              f"{'Violations':>11} {'NaN_curves':>11} {'Worst_mag':>12} {'Time':>7}")
807	        print(f"  {'-' * 75}")
808	        sys.stdout.flush()
809	
810	        for topo in ALL_TOPOS:
811	            t0 = time.time()
812	            ss = all_ss[(topo, K)]
813	            tau_true = all_tau_true[(topo, K)]
814	
815	            rng_C = np.random.default_rng(SEED * 2 + K * 1000 + TOPO_IDX[topo])
816	            violations = 0
817	            nan_curves = 0
818	            worst_mag = 0.0
819	
820	            for i in range(N_RANDOM):
821	                C0 = np.zeros((K, K))
822	                for j in range(K):
823	                    C0[:, j] = rng_C.dirichlet(np.ones(K))
824	
825	                _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)
826	
827	                n_nan = np.isnan(bias_abs).sum()
828	                if n_nan > len(bias_abs) * 0.5:
829	                    nan_curves += 1
830	                    continue
831	
832	                n_viol = check_monotonicity(bias_abs, topo)
833	                if n_viol > 0:
834	                    violations += 1
835	                    valid = ~np.isnan(bias_abs)
836	                    ba = bias_abs[valid]
837	                    diffs = np.diff(ba)
838	                    if topo in NON_DECREASING:
839	                        worst_mag = max(worst_mag, abs(diffs.min()))
840	                    else:
841	                        worst_mag = max(worst_mag, diffs.max())
842	
843	            elapsed = time.time() - t0
844	            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
845	            print(f"  {topo:<14} {direction:<10} {N_RANDOM:>8} "
846	                  f"{violations:>11} {nan_curves:>11} {worst_mag:>12.2e} {elapsed:>6.1f}s")
847	            sys.stdout.flush()
848	
849	            results[f"{topo}_K{K}"] = {
850	                "n_tested": N_RANDOM,
851	                "violations": violations,
852	                "nan_curves": nan_curves,
853	                "direction": direction,
854	                "worst_violation_magnitude": float(worst_mag),
855	                "tau_true": float(tau_true) if not np.isnan(tau_true) else None,
856	            }
857	            total_tests += N_RANDOM
858	            total_violations += violations
859	
860	    print(f"\n  Grand total: {total_tests:,} tests, {total_violations} violations")
861	    return results
862	
863	
864	# ====================================================================
865	# Part 2: Adversarial Search
866	# ====================================================================
867	def part2_adversarial(all_ss, all_tau_true):
868	    print("\n" + "=" * 70)
869	    print(f"PART 2: Adversarial Search ({ADV_N_STARTS} starts x "
870	          f"{len(ADV_DELTA_PAIRS)} delta-pairs)")
871	    print("=" * 70)
872	    sys.stdout.flush()
873	
874	    results = {}
875	
876	    for K in K_ADVERSARIAL:
877	        print(f"\n  K = {K}")
878	        print(f"  {'Topology':<14} {'Direction':<10} {'best_obj':>12} "
879	              f"{'Counterex':>11} {'Time':>7}")
880	        print(f"  {'-' * 57}")
881	        sys.stdout.flush()
882	
883	        for topo in ALL_TOPOS:
884	            t0 = time.time()
885	            ss = all_ss[(topo, K)]
886	            tau_true = all_tau_true[(topo, K)]
887	
888	            best_objective = np.inf
889	            found_counterexample = False
890	            rng_adv = np.random.default_rng(
891	                SEED * 3 + K * 10000 + TOPO_IDX[topo] * 100)
892	
893	            for d1, d2 in ADV_DELTA_PAIRS:
894	                for _ in range(ADV_N_STARTS):
895	                    theta0 = rng_adv.normal(0, 1, K * K)
896	
897	                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,
898	                                  _d1=d1, _d2=d2, _K=K):
899	                        logits = theta.reshape(_K, _K)
900	                        exp_l = np.exp(logits - logits.max(axis=0, keepdims=True))
901	                        C0 = exp_l / exp_l.sum(axis=0, keepdims=True)
902	
903	                        C1 = (1 - _d1) * np.eye(_K) + _d1 * C0
904	                        C2 = (1 - _d2) * np.eye(_K) + _d2 * C0
905	
906	                        tau1 = get_tau_at_C(_topo, C1, _ss)
907	                        tau2 = get_tau_at_C(_topo, C2, _ss)
908	
909	                        if np.isnan(tau1) or np.isnan(tau2):
910	                            return 0.0
911	
912	                        b1_sq = (tau1 - _tt) ** 2
913	                        b2_sq = (tau2 - _tt) ** 2
914	
915	                        if _topo in NON_DECREASING:
916	                            return b2_sq - b1_sq
917	                        else:
918	                            return b1_sq - b2_sq
919	
920	                    res = scipy_minimize(objective, theta0, method='L-BFGS-B',
921	                                         options={'maxiter': 100, 'ftol': 1e-15})
922	
923	                    if res.fun < best_objective:
924	                        best_objective = res.fun
925	
926	                    if res.fun < -1e-8:
927	                        found_counterexample = True
928	
929	            elapsed = time.time() - t0
930	            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
931	            ce_str = "YES!" if found_counterexample else "no"
932	            print(f"  {topo:<14} {direction:<10} {best_objective:>12.2e} "
933	                  f"{ce_str:>11} {elapsed:>6.1f}s")
934	            sys.stdout.flush()
935	
936	            results[f"{topo}_K{K}"] = {
937	                "n_starts": ADV_N_STARTS * len(ADV_DELTA_PAIRS),
938	                "best_objective": float(best_objective),
939	                "found_counterexample": found_counterexample,
940	                "delta_pairs": [[d1, d2] for d1, d2 in ADV_DELTA_PAIRS],
941	            }
942	
943	    return results
944	
945	
946	# ====================================================================
947	# Main
948	# ====================================================================
949	def main():
950	    t_total = time.time()
951	    print("Exp-D v2: Conjecture 1 Verification with ANALYTIC plim")
952	    print(f"  Random: {N_RANDOM:,} C0 x {len(ALL_TOPOS)} topologies x K in {K_VALUES}")
953	    print(f"  Adversarial: {ADV_N_STARTS} starts x {len(ADV_DELTA_PAIRS)} "
954	          f"delta-pairs x K in {K_ADVERSARIAL}")
955	    print(f"  GH quadrature: {N_GH} points/dim, MONO_TOL={MONO_TOL:.0e}")
956	    print(f"  seed={SEED}")
957	    sys.stdout.flush()
958	
959	    all_ss, all_tau_true = precompute_all()
960	
961	    random_results = part1_random(all_ss, all_tau_true)
962	    adversarial_results = part2_adversarial(all_ss, all_tau_true)
963	
964	    # Build output
965	    total_random = sum(r['n_tested'] for r in random_results.values())
966	    total_viol = sum(r['violations'] for r in random_results.values())
967	    total_ce = sum(1 for r in adversarial_results.values()
968	                   if r['found_counterexample'])
969	
970	    if total_viol == 0 and total_ce == 0:
971	        summary = (f"Zero violations across {total_random:,} random tests + "
972	                   f"0 counterexamples found by adversarial search "
973	                   f"(analytic plim, MONO_TOL={MONO_TOL:.0e})")
974	    else:
975	        summary = (f"{total_viol} violations across {total_random:,} random tests + "
976	                   f"{total_ce} counterexamples found by adversarial search "
977	                   f"(analytic plim, MONO_TOL={MONO_TOL:.0e})")
978	
979	    output = {
980	        "method": "analytic_plim",
981	        "gh_quadrature_points": N_GH,
982	        "mono_tol": MONO_TOL,
983	        "random_verification": {},
984	        "adversarial_search": {},
985	        "summary": summary,
986	    }
987	
988	    for topo in ALL_TOPOS:
989	        rv = {}
990	        for K in K_VALUES:
991	            key = f"{topo}_K{K}"
992	            if key in random_results:
993	                rv[f"K{K}"] = random_results[key]
994	        output["random_verification"][topo] = rv
995	
996	    for topo in ALL_TOPOS:
997	        av = {}
998	        for K in K_ADVERSARIAL:
999	            key = f"{topo}_K{K}"
1000	            if key in adversarial_results:
1001	                av[f"K{K}"] = adversarial_results[key]
1002	        output["adversarial_search"][topo] = av
1003	
1004	    out_path = os.path.join(OUT_DIR, 'exp_d_conjecture_results_v2.json')
1005	    with open(out_path, 'w') as f:
1006	        json.dump(output, f, indent=2, default=str)
1007	    print(f"\nJSON -> {out_path}")
1008	
1009	    total_time = time.time() - t_total
1010	    print(f"\n{'=' * 70}")
1011	    print(f"SUMMARY: {summary}")
1012	    print(f"Total time: {total_time:.1f}s ({total_time/60:.1f}min)")
1013	    print(f"{'=' * 70}")
1014	
1015	    # Print comparison note
1016	    print("\nComparison with v1 (Monte Carlo, N=5M, MONO_TOL=1e-8):")
1017	    print("  v1 found 141,514 violations across 210,000 tests")
1018	    print("  v1 found 13 adversarial 'counterexamples'")
1019	    print(f"  v2 found {total_viol} violations across {total_random:,} tests")
1020	    print(f"  v2 found {total_ce} adversarial counterexamples")
1021	
1022	
1023	if __name__ == "__main__":
1024	    main()
1025	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "a5121ffc-af70-479a-b138-7d44b86db83f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nExp-D v2: Conjecture 1 verification with ANALYTIC plim (zero sampling noise).\n\nThe original exp_d_conjecture_verify.py computed plim via sufficient statistics\nestimated from N=5M Monte Carlo simulation, introducing O(1/sqrt(N)) ~ 0.0004\nsampling noise. At MONO_TOL=1e-8, this generated ~141k false monotonicity\nviolations.\n\nThis v2 computes ALL sufficient statistics analytically (closed-form for\nconfounding/mediation/exposure, Gauss-Hermite quadrature for collider/mbias/\nfrontdoor/iv), eliminating sampling noise entirely.\n\nTopology-specific analytics:\n  - confounding: fully analytic (categorical A, linear T and Y)\n  - exposure:    fully analytic (categorical A, linear Y)\n  - mediation:   fully analytic (binary T, softmax A|T, linear Y)\n  - collider:    2D Gauss-Hermite over (T, eps_Y), both N(0,1)\n  - mbias:       2D Gauss-Hermite over (U1, U2), both N(0,1)\n  - frontdoor:   1D Gauss-Hermite over T ~ N(0, alpha_U^2 + 1)\n  - iv:          1D Gauss-Hermite over U ~ N(0,1), with binary Z\n\nOutput: exp_d_conjecture_results_v2.json (same structure as v1)\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\nimport sys\nimport os\nfrom scipy.special import roots_hermite, softmax as scipy_softmax\nfrom scipy.optimize import minimize as scipy_minimize\n\n# ====================================================================\n# Gauss-Hermite quadrature setup\n# ====================================================================\nN_GH = 100  # points per dimension -- machine precision for smooth integrands\n\n# roots_hermite: physicist's convention, weight = exp(-x^2)\n# integral f(x) exp(-x^2) dx ~ sum w_i f(x_i)\n# For N(0,1) expectation: E[f(X)] = (1/sqrt(pi)) sum w_i f(x_i * sqrt(2))\n_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)\nGH_X = _gh_x_raw * np.sqrt(2)   # rescaled nodes for N(0,1)\nGH_W = _gh_w_raw / np.sqrt(np.pi)  # rescaled weights: sum w_i f(x_i) = E_{N(0,1)}[f]\n\n# Verify: E[1] should be 1.0, E[X^2] should be 1.0\nassert abs(GH_W.sum() - 1.0) < 1e-12, f\"GH weights sum to {GH_W.sum()}, expected 1.0\"\nassert abs((GH_W * GH_X**2).sum() - 1.0) < 1e-10, \"GH E[X^2] != 1.0\"\n\n# 2D quadrature: outer product of 1D grids\nGH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')  # (N_GH, N_GH)\nGH_W2 = np.outer(GH_W, GH_W)  # (N_GH, N_GH)\nGH_X2_a_flat = GH_X2_a.ravel()\nGH_X2_b_flat = GH_X2_b.ravel()\nGH_W2_flat = GH_W2.ravel()\n\n# ====================================================================\n# Configuration\n# ====================================================================\nK_VALUES = [3, 5, 7]\nK_ADVERSARIAL = [3, 5]\nN_RANDOM = 10_000\nDELTA_STEP = 0.01\nSEED = 12345\nMONO_TOL = 1e-12  # much tighter than v1's 1e-8 since we have zero sampling noise\n\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\nTOPO_IDX = {t: i for i, t in enumerate(ALL_TOPOS)}\nNON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}\nNON_INCREASING = {'collider', 'mbias'}\n\nADV_DELTA_PAIRS = [(0.0, 0.2), (0.0, 0.5), (0.1, 0.3), (0.2, 0.5), (0.3, 0.7)]\nADV_N_STARTS = 100\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n# ====================================================================\n# DGP Parameter Pools (identical to v1)\n# ====================================================================\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\n_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\n_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\n_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\n_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_all_params(K):\n    p_A = make_p_A(K)\n    return dict(\n        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),\n                         beta_A=np.array(_BETA_A_POOL[:K - 1]), beta_T=2.0, sigma_T=1.0),\n        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),\n                       delta=np.array(_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),\n        collider=dict(tau=1.0, g=np.zeros(K), dT=np.array(_DT_POOL[:K]),\n                      dY=np.array(_DY_POOL[:K])),\n        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),\n        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n                   a1=np.array(_MBIAS_A1_POOL[:K]), a2=np.array(_MBIAS_A2_POOL[:K])),\n        iv=dict(lam=1.0, g=np.zeros(K), dZ=np.array(_IV_DZ_POOL[:K]),\n                dU=np.array(_IV_DU_POOL[:K]), beta=np.array(_BETA_POOL[:K])),\n        frontdoor=dict(alpha_U=1.0, lam_U=1.0, gamma=np.array(_FD_GAMMA_POOL[:K]),\n                       delta=np.array(_FD_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),\n    )\n\n\n# ====================================================================\n# Stable softmax utility\n# ====================================================================\ndef _softmax(logits):\n    \"\"\"Softmax along last axis, numerically stable.\"\"\"\n    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))\n    return e / np.sum(e, axis=-1, keepdims=True)\n\n\n# ====================================================================\n# Analytic Sufficient Statistics classes\n# ====================================================================\nclass AnalyticSuffStats:\n    \"\"\"Population moments for OLS topologies (with or without T).\"\"\"\n    def __init__(self, K, has_T=True):\n        self.K = K\n        self.has_T = has_T\n        self.p_A = None   # K-vector: P(A=k)\n        self.E_Y = None   # scalar\n        self.E_YD = None  # K-vector: E[Y * 1(A=k)]\n        if has_T:\n            self.E_T = None   # scalar\n            self.E_T2 = None  # scalar: E[T^2]\n            self.E_TY = None  # scalar: E[T*Y]\n            self.E_TD = None  # K-vector: E[T * 1(A=k)]\n\n\nclass AnalyticIVSuffStats:\n    \"\"\"Population moments for IV topology (Wald estimator).\"\"\"\n    def __init__(self, K):\n        self.K = K\n        self.RF = None   # E[Y|Z=1] - E[Y|Z=0]\n        self.FS = None   # K-vector: P(A=k|Z=1) - P(A=k|Z=0)\n\n\n# ====================================================================\n# Topology 1: Confounding -- FULLY ANALYTIC\n# ====================================================================\n# DGP: A ~ Cat(p_A), T = sum_{j=1}^{K-1} alpha_j D_j + eps_T,\n#       Y = beta_T * T + sum_{j=1}^{K-1} beta_A_j D_j + eps_Y\n# D_j = 1(A=j+1) for j=0,...,K-2 (ref category A=0)\n# Wait -- looking at original code more carefully:\n#   D[:, j] = (A == j + 1) for j in range(K-1)\n# So D_j = 1(A = j+1), j=0,...,K-2\n# T = D @ alpha + eps_T = sum_{j=0}^{K-2} alpha_j * 1(A=j+1) + eps_T\n# Y = beta_T * T + D @ beta_A + eps_Y = beta_T * T + sum_{j=0}^{K-2} beta_A_j * 1(A=j+1) + eps_Y\n#\n# For the plim regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}:\n# D*_j = 1(A* = j) for j=1,...,K-1 (ref category A*=0)\n# The sufficient stats use A (not A*), and the C matrix maps A->A*.\n# Actually looking at the SuffStats class: DA[:, k] = (A == k) for k=0,...,K-1\n# So p_A[k] = P(A=k), E_TD[k] = E[T * 1(A=k)], E_YD[k] = E[Y * 1(A=k)]\n\ndef compute_confounding_ss(K, p):\n    \"\"\"Analytic sufficient stats for confounding topology.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    p_A = p['p_A']       # K-vector\n    alpha = p['alpha']    # (K-1)-vector: alpha_0,...,alpha_{K-2}\n    beta_A = p['beta_A']  # (K-1)-vector\n    beta_T = p['beta_T']\n    sigma_T = p['sigma_T']\n\n    ss.p_A = p_A.copy()\n\n    # E[T] = sum_{j=0}^{K-2} alpha_j * P(A=j+1)\n    # (since eps_T has mean 0)\n    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))\n\n    # E[T^2] = E[(sum alpha_j D_j)^2] + sigma_T^2\n    # = sum_j alpha_j^2 P(A=j+1) + sigma_T^2\n    # (since D_j D_k = 0 for j!=k, D_j^2 = D_j)\n    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2\n\n    # E[T * 1(A=k)]:\n    # For k=0: E[(sum alpha_j D_j + eps_T) * 1(A=0)]\n    #        = sum_j alpha_j E[D_j * 1(A=0)] + E[eps_T * 1(A=0)]\n    #        = 0 + 0 = 0  (since D_j=1(A=j+1) and A=0 => D_j=0, and eps_T indep of A)\n    # Actually eps_T is independent of A, so E[eps_T * 1(A=k)] = 0 * P(A=k) = 0\n    # For k>=1: E[(sum_j alpha_j D_j + eps_T) * 1(A=k)]\n    #         = alpha_{k-1} * P(A=k) + 0\n    ss.E_TD = np.zeros(K)\n    for k in range(1, K):\n        ss.E_TD[k] = alpha[k - 1] * p_A[k]\n\n    # E[Y] = beta_T * E[T] + sum_{j=0}^{K-2} beta_A_j * P(A=j+1)\n    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))\n\n    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + sum_j beta_A_j * E[D_j * 1(A=k)] + E[eps_Y * 1(A=k)]\n    # E[D_j * 1(A=k)] = P(A=j+1, A=k) = P(A=k) if j+1=k else 0\n    # E[eps_Y * 1(A=k)] = 0\n    # So for k=0: E[Y * 1(A=0)] = beta_T * 0 + 0 + 0 = 0 ... wait that's wrong\n    # Actually: Y = beta_T * T + sum beta_A_j D_j + eps_Y\n    # E[Y * 1(A=0)] = beta_T * E[T * 1(A=0)] + sum_j beta_A_j * E[D_j * 1(A=0)] + E[eps_Y * 1(A=0)]\n    #               = beta_T * 0 + 0 + 0 = 0\n    # Hmm, that gives E_Y = sum_k E[Y * 1(A=k)] = 0 + sum_{k>=1} stuff, but we need E_Y correctly.\n    # Let me reconsider: the intercept in the Y equation.\n    # gen_confounding: Y = beta_T * T + D @ beta_A + eps_Y\n    # There's no explicit intercept in Y. So E[Y | A=0] = beta_T * E[T | A=0] + 0\n    # E[T | A=0] = 0 (since all alpha terms vanish) + E[eps_T] = 0\n    # So E[Y * 1(A=0)] = E[Y | A=0] * P(A=0) = 0 * p_A[0] = 0\n    # That seems correct.\n\n    # For k >= 1:\n    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + beta_A[k-1] * P(A=k)\n    ss.E_YD = np.zeros(K)\n    for k in range(1, K):\n        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]\n    # k=0: already 0\n\n    # E[TY] = E[T * (beta_T * T + sum beta_A_j D_j + eps_Y)]\n    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * D_j] + E[T * eps_Y]\n    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * 1(A=j+1)] + 0\n    ss.E_TY = beta_T * ss.E_T2 + sum(beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))\n\n    return ss\n\n\n# ====================================================================\n# Topology 2: Exposure -- FULLY ANALYTIC\n# ====================================================================\n# DGP: A ~ Cat(p_A), Y = beta[0] + D @ beta[1:] + eps_Y\n# No T variable.\n\ndef compute_exposure_ss(K, p):\n    \"\"\"Analytic sufficient stats for exposure topology.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=False)\n    p_A = p['p_A']\n    beta = p['beta']  # K-vector: beta[0] is intercept\n\n    ss.p_A = p_A.copy()\n\n    # E[Y] = beta[0] + sum_{j=1}^{K-1} beta[j] * P(A=j)\n    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))\n\n    # E[Y * 1(A=k)] = E[(beta[0] + sum_j beta[j] D_j + eps_Y) * 1(A=k)]\n    # = beta[0] * P(A=k) + beta[k] * P(A=k) (if k>=1) + 0\n    # For k=0: = beta[0] * P(A=0) + 0 = beta[0] * p_A[0]\n    ss.E_YD = np.zeros(K)\n    ss.E_YD[0] = beta[0] * p_A[0]\n    for k in range(1, K):\n        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]\n\n    return ss\n\n\n# ====================================================================\n# Topology 3: Mediation -- FULLY ANALYTIC (T is binary)\n# ====================================================================\n# DGP: T ~ Bern(0.5), A | T ~ Cat(softmax(gamma + delta * T))\n#       Y = beta[0] + D @ beta[1:] + tau * T + eps_Y\n# D_j = 1(A = j+1) for j=0,...,K-2\n\ndef compute_mediation_ss(K, p):\n    \"\"\"Analytic sufficient stats for mediation topology.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    gamma = p['gamma']  # K-vector\n    delta_coef = p['delta']   # K-vector\n    beta = p['beta']    # K-vector\n\n    # P(A=k | T=t) = softmax(gamma + delta * t)[k]\n    probs_T0 = _softmax(gamma)          # K-vector\n    probs_T1 = _softmax(gamma + delta_coef)  # K-vector\n\n    # P(A=k) = 0.5 * P(A=k|T=0) + 0.5 * P(A=k|T=1)\n    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1\n\n    # E[T] = 0.5, E[T^2] = 0.5 (since T is Bernoulli(0.5))\n    ss.E_T = 0.5\n    ss.E_T2 = 0.5\n\n    # E[T * 1(A=k)] = E[T * 1(A=k)]\n    # = 0.5 * 0 * P(A=k|T=0) + 0.5 * 1 * P(A=k|T=1)\n    # = 0.5 * probs_T1[k]\n    ss.E_TD = 0.5 * probs_T1\n\n    # E[Y] = beta[0] + sum_{k=1}^{K-1} beta[k] * P(A=k) + tau * E[T]\n    # Wait, gen_mediation:\n    #   Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + eps_Y\n    # D_j = 1(A=j+1), so D @ beta[1:] = sum_{j=0}^{K-2} beta[j+1] * 1(A=j+1)\n    # = sum_{k=1}^{K-1} beta[k] * 1(A=k)\n    ss.E_Y = beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K)) + tau * 0.5\n\n    # E[Y * 1(A=k)] for each k:\n    # Y = beta[0] + sum_j beta[j+1]*D_j + tau*T + eps_Y\n    # E[Y * 1(A=k)] = E[(beta[0] + beta[k]*1(k>=1) + tau*T + eps_Y) * 1(A=k)]\n    # = (beta[0] + beta[k]*(k>=1)) * P(A=k) + tau * E[T * 1(A=k)]\n\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]\n\n    # E[TY] = E[T * (beta[0] + sum beta[k]*1(A=k) + tau*T + eps_Y)]\n    # = beta[0] * E[T] + sum_{k=1}^{K-1} beta[k] * E[T * 1(A=k)] + tau * E[T^2] + 0\n    ss.E_TY = beta[0] * 0.5 + sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + tau * 0.5\n\n    return ss\n\n\n# ====================================================================\n# Topology 4: Collider -- 2D GAUSS-HERMITE\n# ====================================================================\n# DGP: T ~ N(0,1), eps_Y ~ N(0,1) independent\n#       Y = tau * T + eps_Y\n#       A | T, Y ~ Cat(softmax(g + dT * T + dY * Y))\n#\n# Reparametrize: let Z1=T, Z2=eps_Y, both N(0,1) independent\n# Y = tau * Z1 + Z2\n# A | Z1, Z2 ~ Cat(softmax(g + dT * Z1 + dY * (tau * Z1 + Z2)))\n#            = Cat(softmax(g + (dT + tau * dY) * Z1 + dY * Z2))\n\ndef compute_collider_ss(K, p):\n    \"\"\"Analytic sufficient stats for collider via 2D GH quadrature.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    g = p['g']      # K-vector\n    dT = p['dT']    # K-vector\n    dY = p['dY']    # K-vector\n\n    # Quadrature over (Z1, Z2) = (T, eps_Y), both N(0,1)\n    # Logits for each quadrature point: g + (dT + tau*dY) * Z1 + dY * Z2\n    coeff1 = dT + tau * dY   # K-vector: coefficient of Z1\n    coeff2 = dY               # K-vector: coefficient of Z2\n\n    # Compute softmax probabilities at each quadrature point\n    # logits shape: (N_GH^2, K)\n    logits = (g[None, :]\n              + coeff1[None, :] * GH_X2_a_flat[:, None]\n              + coeff2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)  # (N_GH^2, K)\n\n    # T = Z1, Y = tau * Z1 + Z2\n    T_vals = GH_X2_a_flat\n    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat\n\n    # Weighted expectations\n    w = GH_W2_flat  # (N_GH^2,)\n\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)\n    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)\n\n    # Moments of T and Y (independent of A, can compute analytically):\n    ss.E_T = 0.0\n    ss.E_T2 = 1.0\n    ss.E_Y = 0.0  # E[tau*T + eps] = 0\n    ss.E_TY = tau  # E[T(tau*T + eps)] = tau * E[T^2] = tau\n\n    return ss\n\n\n# ====================================================================\n# Topology 5: M-bias -- 2D GAUSS-HERMITE\n# ====================================================================\n# DGP: U1, U2 ~ N(0,1) independent\n#       T = delta_coef * U1 + eta, eta ~ N(0,1)\n#       Y = tau * T + lam * U2 + eps_Y, eps_Y ~ N(0,1)\n#       A | U1, U2 ~ Cat(softmax(g + a1 * U1 + a2 * U2))\n#\n# Note: T and Y depend on (U1, U2, eta, eps_Y) but A only depends on (U1, U2).\n# Since eta, eps_Y are independent of (U1, U2, A):\n#   E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)] + E[eta * 1(A=k)]\n#                  = delta_coef * E[U1 * 1(A=k)]  (eta indep of A)\n#\n#   E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)] + 0\n#\n# So we need 2D GH over (U1, U2) to compute:\n#   P(A=k), E[U1 * 1(A=k)], E[U2 * 1(A=k)]\n\ndef compute_mbias_ss(K, p):\n    \"\"\"Analytic sufficient stats for M-bias via 2D GH quadrature.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    delta_coef = p['delta_coef']\n    lam = p['lam']\n    g = p['g']\n    a1 = p['a1']\n    a2 = p['a2']\n\n    # Logits: g + a1 * U1 + a2 * U2\n    logits = (g[None, :]\n              + a1[None, :] * GH_X2_a_flat[:, None]\n              + a2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)  # (N_GH^2, K)\n\n    w = GH_W2_flat\n    U1_vals = GH_X2_a_flat\n    U2_vals = GH_X2_b_flat\n\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)  # E[U1 * 1(A=k)]\n    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)  # E[U2 * 1(A=k)]\n\n    # E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)]\n    ss.E_TD = delta_coef * E_U1_Dk\n\n    # E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)]\n    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk\n\n    # Marginal moments:\n    # E[T] = 0 (since E[U1]=0, E[eta]=0)\n    # E[T^2] = delta_coef^2 * E[U1^2] + E[eta^2] = delta_coef^2 + 1\n    # E[Y] = 0\n    # E[TY] = tau * E[T^2] + lam * E[T*U2]\n    # E[T*U2] = E[(delta_coef * U1 + eta) * U2] = 0 (all independent)\n    ss.E_T = 0.0\n    ss.E_T2 = delta_coef**2 + 1.0\n    ss.E_Y = 0.0\n    ss.E_TY = tau * ss.E_T2\n\n    return ss\n\n\n# ====================================================================\n# Topology 6: Front-door -- 1D GAUSS-HERMITE\n# ====================================================================\n# DGP: U ~ N(0,1), T = alpha_U * U + eta (eta ~ N(0,1))\n#       M | T ~ Cat(softmax(gamma + delta * T))  -- M is the \"annotator\" variable\n#       Y = D_M @ beta[1:] + lam_U * U + eps_Y\n# where D_M[j] = 1(M=j+1), j=0,...,K-2\n#\n# The regression is Y ~ 1 + T + D*_1 + ... + D*_{K-1}\n# (M plays the role of A in the plim computation)\n#\n# T ~ N(0, sigma_T^2) where sigma_T^2 = alpha_U^2 + 1\n# We do 1D GH over T (after rescaling for its variance).\n#\n# For the moments involving U:\n# E[U | T] = Cov(U,T)/Var(T) * T = alpha_U / (alpha_U^2 + 1) * T\n# (since Cov(U,T) = alpha_U, Var(T) = alpha_U^2 + 1)\n#\n# P(M=k) = E_T[softmax(gamma + delta * T)[k]]\n# E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]\n# E[Y * 1(M=k)] = E[E[Y | T, M] * 1(M=k)]\n#               = E_T[ E[Y|T,M=k] * softmax(gamma+delta*T)[k] ]\n# E[Y|T,M=k] = beta[k] (if k>=1, else 0 for the intercept part from D_M)\n#              + lam_U * E[U|T] + 0\n# Wait, let me reconsider:\n# Y = sum_{j=0}^{K-2} beta[j+1] * 1(M=j+1) + lam_U * U + eps_Y\n# (from gen_frontdoor: Y = D @ beta[1:] + lam_U * U + eps_Y,\n#  where beta = p['beta'] and D[j] = 1(M=j+1))\n# There's no intercept beta[0] in the Y equation in gen_frontdoor!\n# Let me re-check: gen_frontdoor has Y = D @ p['beta'][1:] + p['lam_U'] * U + eps_Y\n# So Y = sum_{k=1}^{K-1} beta[k] * 1(M=k) + lam_U * U + eps_Y\n#\n# E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)] + 0\n# For k=0: E[Y * 1(M=0)] = 0 + lam_U * E[U * 1(M=0)] + 0\n\ndef compute_frontdoor_ss(K, p):\n    \"\"\"Analytic sufficient stats for front-door via 1D GH quadrature.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    alpha_U = p['alpha_U']\n    lam_U = p['lam_U']\n    gamma = p['gamma']\n    delta_coef = p['delta']\n    beta = p['beta']\n\n    sigma_T2 = alpha_U**2 + 1.0\n    sigma_T = np.sqrt(sigma_T2)\n\n    # 1D GH over T ~ N(0, sigma_T^2): rescale nodes\n    T_nodes = GH_X * sigma_T  # (N_GH,)\n    T_weights = GH_W          # (N_GH,) -- already normalized for E_{N(0,1)}\n\n    # softmax(gamma + delta * T) at each T node\n    # logits shape: (N_GH, K)\n    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]\n    probs = _softmax(logits)  # (N_GH, K)\n\n    # P(M=k) = E_T[softmax(gamma + delta * T)[k]]\n    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)\n\n    # E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]\n    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)\n\n    # E[U * 1(M=k)] via the law of iterated expectations:\n    # E[U * 1(M=k)] = E_T[ E[U|T] * P(M=k|T) ]\n    # E[U|T] = alpha_U / sigma_T^2 * T\n    E_U_given_T = alpha_U / sigma_T2 * T_nodes  # (N_GH,)\n    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)\n\n    # E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)]\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]\n\n    # Marginal moments:\n    # E[T] = 0\n    # E[T^2] = sigma_T^2\n    # E[Y] = sum_{k=1}^{K-1} beta[k] * P(M=k) + lam_U * E[U] + 0\n    #       = sum_{k=1}^{K-1} beta[k] * P(M=k)\n    ss.E_T = 0.0\n    ss.E_T2 = sigma_T2\n    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))\n\n    # E[TY] = sum_{k=1}^{K-1} beta[k] * E[T * 1(M=k)] + lam_U * E[T*U] + E[T*eps_Y]\n    # E[T*U] = Cov(T,U) = alpha_U (since both mean 0)\n    # E[T*eps_Y] = 0\n    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U\n\n    return ss\n\n\n# ====================================================================\n# Topology 7: IV -- 1D GAUSS-HERMITE over U, binary Z\n# ====================================================================\n# DGP: Z ~ Bern(0.5), U ~ N(0,1), eps_Y ~ N(0,1)\n#       A | Z, U ~ Cat(softmax(g + dZ * Z + dU * U))\n#       Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps_Y\n#\n# Wald estimator: tau_hat = RF / FS*[1]\n# RF = E[Y|Z=1] - E[Y|Z=0]\n# FS[k] = P(A=k|Z=1) - P(A=k|Z=0)\n#\n# P(A=k|Z=z) = E_U[softmax(g + dZ * z + dU * U)[k]]\n# E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z) + lam * E[U] + E[eps]\n#           = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)\n\ndef compute_iv_ss(K, p):\n    \"\"\"Analytic sufficient stats for IV via 1D GH quadrature.\"\"\"\n    ivss = AnalyticIVSuffStats(K)\n    g = p['g']\n    dZ = p['dZ']\n    dU = p['dU']\n    beta = p['beta']\n    lam = p['lam']\n\n    # P(A=k|Z=z) for z=0 and z=1\n    # logits for Z=0: g + dU * U\n    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]  # (N_GH, K)\n    probs_z0 = _softmax(logits_z0)\n    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)  # K-vector\n\n    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]\n    probs_z1 = _softmax(logits_z1)\n    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)  # K-vector\n\n    # First stage\n    ivss.FS = P_A_z1 - P_A_z0  # K-vector\n\n    # Reduced form\n    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)\n    # (lam * E[U] = 0, E[eps] = 0, beta[0] cancels out since it's not in gen_iv)\n    # Actually gen_iv: Y = D @ p['beta'][1:] + p['lam'] * U + eps\n    # So Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps\n    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)\n    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))\n    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))\n\n    ivss.RF = E_Y_z1 - E_Y_z0\n\n    return ivss\n\n\n# ====================================================================\n# Plim computation (from original, unchanged)\n# ====================================================================\ndef plim_ols_with_T(C, ss):\n    \"\"\"Plim of OLS regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    K = ss.K\n    q = C @ ss.p_A        # misclassified P(A*=k)\n    ct = C @ ss.E_TD       # E[T * 1(A*=k)]\n    cy = C @ ss.E_YD       # E[Y * 1(A*=k)]\n    dim = K + 1\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = ss.E_T\n    EZZ[1, 0] = ss.E_T\n    EZZ[1, 1] = ss.E_T2\n    EZZ[0, 2:] = q[1:]\n    EZZ[2:, 0] = q[1:]\n    EZZ[1, 2:] = ct[1:]\n    EZZ[2:, 1] = ct[1:]\n    for j in range(K - 1):\n        EZZ[j + 2, j + 2] = q[j + 1]\n    EZY = np.zeros(dim)\n    EZY[0] = ss.E_Y\n    EZY[1] = ss.E_TY\n    EZY[2:] = cy[1:]\n    try:\n        return np.linalg.solve(EZZ, EZY)\n    except np.linalg.LinAlgError:\n        return np.full(dim, np.nan)\n\n\ndef plim_ols_exposure(C, ss):\n    \"\"\"Plim of OLS regression Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    K = ss.K\n    q = C @ ss.p_A\n    cy = C @ ss.E_YD\n    dim = K\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1:] = q[1:]\n    EZZ[1:, 0] = q[1:]\n    for j in range(K - 1):\n        EZZ[j + 1, j + 1] = q[j + 1]\n    EZY = np.zeros(dim)\n    EZY[0] = ss.E_Y\n    EZY[1:] = cy[1:]\n    try:\n        return np.linalg.solve(EZZ, EZY)\n    except np.linalg.LinAlgError:\n        return np.full(dim, np.nan)\n\n\ndef plim_iv_single(C, ss):\n    \"\"\"Plim of Wald IV estimator with misclassified A.\"\"\"\n    FS_star = C @ ss.FS\n    if abs(FS_star[1]) < 1e-15:\n        return np.nan\n    return ss.RF / FS_star[1]\n\n\ndef get_tau_at_C(topo, C, ss):\n    if topo == 'iv':\n        return plim_iv_single(C, ss)\n    elif topo == 'exposure':\n        return plim_ols_exposure(C, ss)[1]\n    else:\n        return plim_ols_with_T(C, ss)[1]\n\n\ndef get_tau_true(topo, K, params, ss):\n    \"\"\"True causal parameter.\n\n    For correctly-identified topologies: tau_true = plim(I).\n    For protective topologies (collider, mbias): tau_true = DGP tau,\n    so B(0) = plim(I) - tau != 0 (existing bias from Berkson/M-bias).\n    \"\"\"\n    p = params[topo]\n    if topo == 'collider':\n        return p['tau']\n    elif topo == 'mbias':\n        return p['tau']\n    else:\n        return get_tau_at_C(topo, np.eye(K), ss)\n\n\n# ====================================================================\n# Batched bias curve computation (from original, unchanged)\n# ====================================================================\ndef compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):\n    K = C0.shape[0]\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        delta_max = 10.0\n    else:\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n\n    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)\n    n = len(deltas)\n    d = deltas[:, None]\n\n    if topo == 'iv':\n        FS0 = C0 @ ss.FS\n        fs_star = (1 - d) * ss.FS[None, :] + d * FS0[None, :]\n        denom = fs_star[:, 1]\n        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)\n    elif topo == 'exposure':\n        pA0 = C0 @ ss.p_A\n        YD0 = C0 @ ss.E_YD\n        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]\n        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]\n        dim = K\n        EZZ = np.zeros((n, dim, dim))\n        EZZ[:, 0, 0] = 1.0\n        EZZ[:, 0, 1:] = q[:, 1:]\n        EZZ[:, 1:, 0] = q[:, 1:]\n        for j in range(K - 1):\n            EZZ[:, j + 1, j + 1] = q[:, j + 1]\n        EZY = np.zeros((n, dim))\n        EZY[:, 0] = ss.E_Y\n        EZY[:, 1:] = cy[:, 1:]\n        try:\n            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]\n            taus = coefs[:, 1]\n        except np.linalg.LinAlgError:\n            taus = np.full(n, np.nan)\n    else:\n        pA0 = C0 @ ss.p_A\n        TD0 = C0 @ ss.E_TD\n        YD0 = C0 @ ss.E_YD\n        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]\n        ct = (1 - d) * ss.E_TD[None, :] + d * TD0[None, :]\n        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]\n        dim = K + 1\n        EZZ = np.zeros((n, dim, dim))\n        EZZ[:, 0, 0] = 1.0\n        EZZ[:, 0, 1] = ss.E_T\n        EZZ[:, 1, 0] = ss.E_T\n        EZZ[:, 1, 1] = ss.E_T2\n        EZZ[:, 0, 2:] = q[:, 1:]\n        EZZ[:, 2:, 0] = q[:, 1:]\n        EZZ[:, 1, 2:] = ct[:, 1:]\n        EZZ[:, 2:, 1] = ct[:, 1:]\n        for j in range(K - 1):\n            EZZ[:, j + 2, j + 2] = q[:, j + 1]\n        EZY = np.zeros((n, dim))\n        EZY[:, 0] = ss.E_Y\n        EZY[:, 1] = ss.E_TY\n        EZY[:, 2:] = cy[:, 1:]\n        try:\n            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]\n            taus = coefs[:, 1]\n        except np.linalg.LinAlgError:\n            taus = np.full(n, np.nan)\n\n    bias_abs = np.abs(taus - tau_true)\n    return deltas, bias_abs\n\n\ndef check_monotonicity(bias_abs, topo, tol=MONO_TOL):\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        return int(np.sum(diffs < -tol))\n    else:\n        return int(np.sum(diffs > tol))\n\n\n# ====================================================================\n# Precompute analytic sufficient statistics\n# ====================================================================\n_COMPUTE_SS = {\n    'confounding': lambda K, p: compute_confounding_ss(K, p),\n    'mediation':   lambda K, p: compute_mediation_ss(K, p),\n    'collider':    lambda K, p: compute_collider_ss(K, p),\n    'exposure':    lambda K, p: compute_exposure_ss(K, p),\n    'mbias':       lambda K, p: compute_mbias_ss(K, p),\n    'iv':          lambda K, p: compute_iv_ss(K, p),\n    'frontdoor':   lambda K, p: compute_frontdoor_ss(K, p),\n}\n\n\ndef precompute_all():\n    print(\"\\nPrecomputing analytic sufficient statistics...\")\n    sys.stdout.flush()\n    t0 = time.time()\n    all_ss = {}\n    all_tau_true = {}\n\n    for K in K_VALUES:\n        params = make_all_params(K)\n        for topo in ALL_TOPOS:\n            ss = _COMPUTE_SS[topo](K, params[topo])\n            tau_true = get_tau_true(topo, K, params, ss)\n            all_ss[(topo, K)] = ss\n            all_tau_true[(topo, K)] = tau_true\n\n    print(\"  Done ({:.3f}s). tau_true values:\".format(time.time() - t0))\n    for topo in ALL_TOPOS:\n        vals = [all_tau_true[(topo, K)] for K in K_VALUES]\n        vals_s = \", \".join(\n            f\"K{K}={v:.10f}\" if v is not None and not np.isnan(v) else f\"K{K}=NaN\"\n            for K, v in zip(K_VALUES, vals))\n        direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n        print(f\"    {topo:<14} [{direction}] {vals_s}\")\n    sys.stdout.flush()\n    return all_ss, all_tau_true\n\n\n# ====================================================================\n# Part 1: Random Verification\n# ====================================================================\ndef part1_random(all_ss, all_tau_true):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 1: Random Verification ({:,} C0 per topology x K)\".format(N_RANDOM))\n    print(\"  MONO_TOL = {:.0e} (analytic -- zero sampling noise)\".format(MONO_TOL))\n    print(\"=\" * 70)\n    sys.stdout.flush()\n\n    results = {}\n    total_tests = 0\n    total_violations = 0\n\n    for K in K_VALUES:\n        print(f\"\\n  K = {K}\")\n        print(f\"  {'Topology':<14} {'Direction':<10} {'Tested':>8} \"\n              f\"{'Violations':>11} {'NaN_curves':>11} {'Worst_mag':>12} {'Time':>7}\")\n        print(f\"  {'-' * 75}\")\n        sys.stdout.flush()\n\n        for topo in ALL_TOPOS:\n            t0 = time.time()\n            ss = all_ss[(topo, K)]\n            tau_true = all_tau_true[(topo, K)]\n\n            rng_C = np.random.default_rng(SEED * 2 + K * 1000 + TOPO_IDX[topo])\n            violations = 0\n            nan_curves = 0\n            worst_mag = 0.0\n\n            for i in range(N_RANDOM):\n                C0 = np.zeros((K, K))\n                for j in range(K):\n                    C0[:, j] = rng_C.dirichlet(np.ones(K))\n\n                _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)\n\n                n_nan = np.isnan(bias_abs).sum()\n                if n_nan > len(bias_abs) * 0.5:\n                    nan_curves += 1\n                    continue\n\n                n_viol = check_monotonicity(bias_abs, topo)\n                if n_viol > 0:\n                    violations += 1\n                    valid = ~np.isnan(bias_abs)\n                    ba = bias_abs[valid]\n                    diffs = np.diff(ba)\n                    if topo in NON_DECREASING:\n                        worst_mag = max(worst_mag, abs(diffs.min()))\n                    else:\n                        worst_mag = max(worst_mag, diffs.max())\n\n            elapsed = time.time() - t0\n            direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n            print(f\"  {topo:<14} {direction:<10} {N_RANDOM:>8} \"\n                  f\"{violations:>11} {nan_curves:>11} {worst_mag:>12.2e} {elapsed:>6.1f}s\")\n            sys.stdout.flush()\n\n            results[f\"{topo}_K{K}\"] = {\n                \"n_tested\": N_RANDOM,\n                \"violations\": violations,\n                \"nan_curves\": nan_curves,\n                \"direction\": direction,\n                \"worst_violation_magnitude\": float(worst_mag),\n                \"tau_true\": float(tau_true) if not np.isnan(tau_true) else None,\n            }\n            total_tests += N_RANDOM\n            total_violations += violations\n\n    print(f\"\\n  Grand total: {total_tests:,} tests, {total_violations} violations\")\n    return results\n\n\n# ====================================================================\n# Part 2: Adversarial Search\n# ====================================================================\ndef part2_adversarial(all_ss, all_tau_true):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 2: Adversarial Search ({ADV_N_STARTS} starts x \"\n          f\"{len(ADV_DELTA_PAIRS)} delta-pairs)\")\n    print(\"=\" * 70)\n    sys.stdout.flush()\n\n    results = {}\n\n    for K in K_ADVERSARIAL:\n        print(f\"\\n  K = {K}\")\n        print(f\"  {'Topology':<14} {'Direction':<10} {'best_obj':>12} \"\n              f\"{'Counterex':>11} {'Time':>7}\")\n        print(f\"  {'-' * 57}\")\n        sys.stdout.flush()\n\n        for topo in ALL_TOPOS:\n            t0 = time.time()\n            ss = all_ss[(topo, K)]\n            tau_true = all_tau_true[(topo, K)]\n\n            best_objective = np.inf\n            found_counterexample = False\n            rng_adv = np.random.default_rng(\n                SEED * 3 + K * 10000 + TOPO_IDX[topo] * 100)\n\n            for d1, d2 in ADV_DELTA_PAIRS:\n                for _ in range(ADV_N_STARTS):\n                    theta0 = rng_adv.normal(0, 1, K * K)\n\n                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,\n                                  _d1=d1, _d2=d2, _K=K):\n                        logits = theta.reshape(_K, _K)\n                        exp_l = np.exp(logits - logits.max(axis=0, keepdims=True))\n                        C0 = exp_l / exp_l.sum(axis=0, keepdims=True)\n\n                        C1 = (1 - _d1) * np.eye(_K) + _d1 * C0\n                        C2 = (1 - _d2) * np.eye(_K) + _d2 * C0\n\n                        tau1 = get_tau_at_C(_topo, C1, _ss)\n                        tau2 = get_tau_at_C(_topo, C2, _ss)\n\n                        if np.isnan(tau1) or np.isnan(tau2):\n                            return 0.0\n\n                        b1_sq = (tau1 - _tt) ** 2\n                        b2_sq = (tau2 - _tt) ** 2\n\n                        if _topo in NON_DECREASING:\n                            return b2_sq - b1_sq\n                        else:\n                            return b1_sq - b2_sq\n\n                    res = scipy_minimize(objective, theta0, method='L-BFGS-B',\n                                         options={'maxiter': 100, 'ftol': 1e-15})\n\n                    if res.fun < best_objective:\n                        best_objective = res.fun\n\n                    if res.fun < -1e-8:\n                        found_counterexample = True\n\n            elapsed = time.time() - t0\n            direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n            ce_str = \"YES!\" if found_counterexample else \"no\"\n            print(f\"  {topo:<14} {direction:<10} {best_objective:>12.2e} \"\n                  f\"{ce_str:>11} {elapsed:>6.1f}s\")\n            sys.stdout.flush()\n\n            results[f\"{topo}_K{K}\"] = {\n                \"n_starts\": ADV_N_STARTS * len(ADV_DELTA_PAIRS),\n                \"best_objective\": float(best_objective),\n                \"found_counterexample\": found_counterexample,\n                \"delta_pairs\": [[d1, d2] for d1, d2 in ADV_DELTA_PAIRS],\n            }\n\n    return results\n\n\n# ====================================================================\n# Main\n# ====================================================================\ndef main():\n    t_total = time.time()\n    print(\"Exp-D v2: Conjecture 1 Verification with ANALYTIC plim\")\n    print(f\"  Random: {N_RANDOM:,} C0 x {len(ALL_TOPOS)} topologies x K in {K_VALUES}\")\n    print(f\"  Adversarial: {ADV_N_STARTS} starts x {len(ADV_DELTA_PAIRS)} \"\n          f\"delta-pairs x K in {K_ADVERSARIAL}\")\n    print(f\"  GH quadrature: {N_GH} points/dim, MONO_TOL={MONO_TOL:.0e}\")\n    print(f\"  seed={SEED}\")\n    sys.stdout.flush()\n\n    all_ss, all_tau_true = precompute_all()\n\n    random_results = part1_random(all_ss, all_tau_true)\n    adversarial_results = part2_adversarial(all_ss, all_tau_true)\n\n    # Build output\n    total_random = sum(r['n_tested'] for r in random_results.values())\n    total_viol = sum(r['violations'] for r in random_results.values())\n    total_ce = sum(1 for r in adversarial_results.values()\n                   if r['found_counterexample'])\n\n    if total_viol == 0 and total_ce == 0:\n        summary = (f\"Zero violations across {total_random:,} random tests + \"\n                   f\"0 counterexamples found by adversarial search \"\n                   f\"(analytic plim, MONO_TOL={MONO_TOL:.0e})\")\n    else:\n        summary = (f\"{total_viol} violations across {total_random:,} random tests + \"\n                   f\"{total_ce} counterexamples found by adversarial search \"\n                   f\"(analytic plim, MONO_TOL={MONO_TOL:.0e})\")\n\n    output = {\n        \"method\": \"analytic_plim\",\n        \"gh_quadrature_points\": N_GH,\n        \"mono_tol\": MONO_TOL,\n        \"random_verification\": {},\n        \"adversarial_search\": {},\n        \"summary\": summary,\n    }\n\n    for topo in ALL_TOPOS:\n        rv = {}\n        for K in K_VALUES:\n            key = f\"{topo}_K{K}\"\n            if key in random_results:\n                rv[f\"K{K}\"] = random_results[key]\n        output[\"random_verification\"][topo] = rv\n\n    for topo in ALL_TOPOS:\n        av = {}\n        for K in K_ADVERSARIAL:\n            key = f\"{topo}_K{K}\"\n            if key in adversarial_results:\n                av[f\"K{K}\"] = adversarial_results[key]\n        output[\"adversarial_search\"][topo] = av\n\n    out_path = os.path.join(OUT_DIR, 'exp_d_conjecture_results_v2.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nJSON -> {out_path}\")\n\n    total_time = time.time() - t_total\n    print(f\"\\n{'=' * 70}\")\n    print(f\"SUMMARY: {summary}\")\n    print(f\"Total time: {total_time:.1f}s ({total_time/60:.1f}min)\")\n    print(f\"{'=' * 70}\")\n\n    # Print comparison note\n    print(\"\\nComparison with v1 (Monte Carlo, N=5M, MONO_TOL=1e-8):\")\n    print(\"  v1 found 141,514 violations across 210,000 tests\")\n    print(\"  v1 found 13 adversarial 'counterexamples'\")\n    print(f\"  v2 found {total_viol} violations across {total_random:,} tests\")\n    print(f\"  v2 found {total_ce} adversarial counterexamples\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 1025,
      "startLine": 1,
      "totalLines": 1025
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear understanding of the codebase. Let me summarize the key points:

1. `exp_d_conjecture_verify_v2.py` has the analytic sufficient statistics computation functions and bias curve computation that I need to reuse.
2. The key functions are:
   - `make_all_params(K)` - creates default DGP parameters
   - `_COMPUTE_SS[topo](K, params[topo])` - computes analytic sufficient statistics
   - `get_tau_true(topo, K, params, ss)` - gets true tau value
   - `compute_bias_curve(topo, C0, ss, tau_true, delta_step)` - computes bias curve along C(δ) = (1-δ)I + δ·C0
   - `check_monotonicity(bias_abs, topo, tol)` - checks monotonicity
   - `compute_iv_bias_curve_analytic(C0, ss, delta_step)` from `conjecture_dgp_sensitivity.py` - special IV handling

For the adversarial monotonicity test, I need to generate 4 different scenarios to test against.

I should sweep δ from 0 to 1 in steps of 0.01 to get 101 points, keeping the matrices column-stochastic throughout. For each scenario, I'll check whether the absolute bias stays monotonic as δ varies. The existing code can go beyond δ=1, but for this experiment I'm constraining it to [0,1].

Now I'm thinking through the β configurations the task specifies. I see that different topologies use β differently—some have it as direct treatment coefficients, others embed it in structures like `beta_A` or `beta_T`. The task's specification of "β length = K with β[0] = 0" points to a category-level coefficient vector that appears across most topologies, so I should standardize how β maps to each topology's parameter structure rather than treating them separately.

But I'm realizing the task references a function `compute_bias_for_topology` that doesn't actually exist in the codebase—the actual function is `compute_bias` which takes DGP parameters, not just β. I need to figure out what the task is really asking for and how to bridge this gap.

Looking at the existing experiment scripts like `exp_d_conjecture_verify_v2.py`, they show how to compute analytic plim values, which seems like the right approach here. The key insight is that β's meaning varies by topology—it represents the coefficients controlling how annotation categories affect the outcome, whether that's the exposure-to-outcome path, mediator-to-outcome path, or confounder-to-outcome path depending on the causal structure.

For topologies like collider and mbias that don't have a direct β parameter, I'll need to adapt by using the closest equivalent in their DGP. The cleanest approach is to modify the DGP parameters so the category effect vector aligns with the specified β pattern, where β[0] = 0 as the reference category and the remaining elements represent the differential effects of each category. Implementing the coefficient mapping...

For collider and m-bias, the β pattern doesn't map directly since these involve classification probabilities rather than outcome regression — I should apply β to `dY` for collider (controlling Y's effect on A) and to `a1` for m-bias (controlling U1's effect on A).

Now I'm settling on a consistent approach: modify `beta` for topologies that have it, `beta_A` for confounding, `dY` for collider, and `a1` for m-bias. Let me write the script efficiently.

Writing the test script... Setting up the experimental parameters with different K values, topologies, and beta configurations...

Now I'm defining functions to generate adversarial initial conditions—one that creates near-permutation matrices with controlled noise, and another for block-diagonal structures...

Defining sparse matrix generators... Writing the adversarial config dispatcher...

Actually, I'm realizing there's an issue with the task requirements—block_diag and near_uniform generate deterministic matrices given K, so they wouldn't produce 100 different random C₀ values like the other types do. I need to think about whether to randomize the block assignments or if the task description needs clarification. For block_diag, the randomness comes from varying which indices get assigned to which block across the 100 trials, though with only K=3 categories there are limited distinct partitions possible. For near_uniform, since it's completely deterministic, all 100 trials would produce identical C₀ matrices and curves, which is acceptable. Let me check the exact definition again — it specifies splitting the first ⌊K/2⌋ columns versus the remaining ones. So the block structure is completely deterministic—columns split at floor(K/2) with uniform mixing within each block and zero cross-block interaction. This means block_diag and near_uniform will produce identical results across all 100 runs, which is fine since the code is simpler this way. Now I need to figure out how to apply the different β configurations to each topology type. For collider, I'll map `dY = beta_vec` since it controls how Y affects selection probability, and for mbias, `a1 = beta_vec` since it determines how U1 influences A classification—these are the most analogous parameters for testing monotonicity across different coefficient structures. Now I need to think through what other modifications are needed.

Writing parameter modification function...

Now I'm setting up the nested loop structure to iterate through each combination of K values, beta configurations, and topologies, computing the sample size and true treatment effect for each scenario before moving into the adversarial type iterations.

For each adversarial type and its configurations, I'm generating adversarial confounding matrices and computing bias curves along the interpolation path from identity to the adversarial matrix. I notice the existing bias curve function uses a dynamic delta range based on the matrix's diagonal, but for this experiment I want to fix delta across [0, 1] with consistent step sizes to get 101 evaluation points.

Now I'm verifying that the interpolated matrix C(δ) = (1-δ)I + δC₀ stays column-stochastic throughout [0, 1]—the column sums remain 1 and all entries stay non-negative as long as C₀ is column-stochastic.

The existing `compute_bias_curve` function uses a different δ range, so I'll compute the bias curve myself to ensure I'm sampling δ from 0 to 1 in steps of 0.01, calculating the absolute difference between the biased and true transition probabilities at each point.

For the IV estimator, I need to handle the Wald approach carefully—I'll reference the analytic sensitivity method from the existing codebase to properly account for weak instrument concerns.

Actually, I can leverage `compute_bias_curve` directly since it already handles the delta sweep and computes delta_max based on the minimum diagonal element of C₀. For the adversarial matrices like near_perm and block_diag, I need to trace through how the diagonal values behave—particularly for block_diag where the diagonal structure depends on how columns are partitioned across blocks. The `compute_bias_curve` function from the existing module returns delta values up to delta_max, so I can just extract the first 101 points to get my [0,1] range. Alternatively, I'm writing a dedicated function that computes the bias curve directly for δ∈[0,1] with a fixed number of steps.

Defining the function body... The IV case also needs to detect sign flips from weak instruments. I'll use the analytic IV bias function for those topologies and the batched approach for others, truncating all delta values to stay within [0,1]. For performance, I'm realizing the precomputation of sufficient statistics per (K, topology, β_config) is the bottleneck, but once that's done, computing individual bias curves for each C₀ value should be fast enough—so I'll structure the script to leverage that. batched np.linalg.solve which is more efficient. So for each curve, I'm constructing and solving a batch of 101 linear systems of size at most 8×8, which should take around 0.1ms per curve. That puts the total runtime for all 56,700 curves at roughly 5.7 seconds, so the whole experiment should finish in under a minute.

Writing the experiment script... Setting up configuration parameters for the experiment, including monotonicity thresholds, different beta coefficient patterns like alternating and same-sign configurations, and adversarial matrix types to test against.

Writing configuration functions... Continuing with the function logic...

For the near_perm case, I'm extracting the epsilon value and creating a matrix that's mostly the permutation with some uniform noise mixed in. For block_diag, I'm splitting the classes into two groups and making each column uniform within its group. For sparse, I'm setting diagonal elements to the sparsity parameter and randomly assigning one off-diagonal element per column.

Now I'm moving into the bias curve computation function, which takes the transition matrix and evaluates how the bias changes across a range of delta values from 0 to 1.

For the instrumental variables case with analytic sufficient statistics, I'm checking whether we have a weak IV problem by examining if the first-stage F-statistic changes sign as delta varies—if it does or if the original F-statistic is essentially zero, the IV is weak and I return NaN values. Otherwise, I compute the absolute bias using the reduced form coefficient, the change in the first-stage statistic, and the interpolated F-statistic values across the delta range.

For regular sufficient statistics, I'm computing the full bias curve across all delta values and then extracting just the portion where delta is at most 1.0 to match the requested range.

Now I'm moving into a monotonicity analysis function that takes the bias curve and checks whether it's monotone increasing, counting any drops in the values.

Writing analysis functions... Setting up aggregation structures... Writing simulation loop... Writing worst case tracking... Writing output structure... Writing results output... Printing summary statistics by topology and adversarial type, then displaying the top five worst-case scenarios with their parameters...

Actually, I need to be careful with the `compute_bias_curve` function—it returns a variable number of points depending on `delta_max`, but I need exactly 101 points spanning δ from 0 to 1. Since the existing implementation generates at least 101 points when `delta_max ≥ 1.0`, I can just slice the first 101 entries.

But there's a complication with certain adversarial C₀ matrices: when `min_diag` equals 0 (which happens with near-permutation matrices at small ε or sparse matrices with low diagonal probability), the calculation for `delta_max` becomes problematic since it involves division by zero. I need to handle this edge case carefully to avoid infinite values.

Looking at the near-permutation case more closely, the diagonal elements depend on whether each index is a fixed point in the permutation. For fixed points, the diagonal value is higher (around 1 - ε(1 - 1/K)), while non-fixed points have much smaller diagonal values (ε/K). With concrete numbers like ε=0.05 and K=3, the non-fixed diagonal elements are quite small but still positive, giving me enough sampling points.

Now I'm checking the block diagonal case where split=1 creates unequal block sizes—the first block has one element while the second has two. This means the diagonal values vary: the first column has a diagonal of 1, while columns in the larger block drop to 0.5. The minimum diagonal is 0.5, which gives a delta_max of 2.0, still manageable. For the sparse case with p_diag=0.3, the minimum diagonal is 0.3 itself, yielding delta_max of 1.43. And for the near-uniform distribution with K=3 and ε=0.01, the diagonal elements are around 0.343, producing delta_max of 1.52. All of these are within acceptable bounds.

Since delta_max exceeds 1.0 in every scenario, I'll always get at least 101 sample points. But there's a subtlety with how the IV case is handled—the `compute_bias_curve` function uses a different approach internally than the analytic version, which explicitly detects weak-IV conditions by checking for denominator sign flips. I should handle IV and non-IV cases separately: detect weak-IV for the instrumental variable case and flag it, while using the standard bias curve computation for the others. Let me streamline the compute_curve function by implementing this directly.

Writing compute_curve function... I'm realizing the loop approach is inefficient—the batched `compute_bias_curve` function already handles vectorized operations much better. I should leverage that for speed, even though I need to handle the fixed [0,1] delta range and the IV case separately. Let me just call `compute_bias_curve` and extract what I need, treating NaN values as an indicator of weak instruments.

Writing the wrapper function... I see the issue—NaN values in the bias curve can come from the denominator approaching zero, which creates poles rather than indicating weak instruments. I need to detect sign flips in the first-stage coefficient across the δ range, since that's what actually signals a weak IV problem. Let me refine the weak IV detection logic...

Adding detection logic... Writing the final script...

I'm recognizing that block_diag and near_uniform produce identical results across all 100 trials since C₀ is deterministic, which is redundant but acceptable given the task constraints. I'm also considering edge cases like K=3 with block configurations to ensure robustness. Completing the column calculations and verifying the block diagonal structure for K=5 with blocks {0,1} and {2,3,4}, then checking the same pattern holds for K=7 with three blocks.

Now I'm ready to write out the full script. I should also think through edge cases—specifically what happens when tau_true is zero or undefined. For the exposure topology, tau_true should be non-zero since beta[1] is always non-zero in our configurations. For collider and mbias topologies, tau is set to 1.0 by default, so that's always non-zero. For other topologies, I'm computing tau from the causal structure, which should also be non-zero with our parameters.

Looking at the confounding case with alternating_small beta values: the treatment effect tau_true is 2.0 (the coefficient on T in the outcome equation), independent of the exposure coefficients. For exposure with the same beta configuration, tau_true equals the direct effect of D_1, which is 0.2—also non-zero. So across all topologies and parameter sets, I'm getting valid non-zero tau values.

Now I need to clarify the non-monotonicity definition. The threshold for flagging non-monotonicity is 0.001 on the absolute bias drops. For topologies where bias should be non-decreasing (like NO), I compute epsilon as the maximum of any negative differences; for non-increasing topologies like collider or m-bias, I flip the sign and look at positive differences instead. The task description mentions negative differences indicate non-monotonicity, but I need to verify this applies consistently across all topology types. I'm realizing the task only checks for non-decreasing monotonicity violations (drops in |B(δ)|), which applies to most topologies. For collider and mbias where non-increasing behavior is expected, a rise would be the actual violation, but the simplified task definition focuses on measuring maximum drops rather than rises. I need to handle both non-decreasing and non-increasing topologies correctly—for non-decreasing cases I'm looking at maximum drops, but for non-increasing cases I should track maximum rises instead. The task description focuses on the non-decreasing case since that's more common, but I'll implement both directions properly like the existing code does. Now I'm ready to write the full script, though I should first estimate the computational load: with 3 K values, 3 β configurations, and 7 topologies, that's 63 parameter combinations to process. topo, params) pairs.
For each pair × each adversarial type with configs:
  near_perm: 3 configs
  block_diag: 1 config
  sparse: 3 configs
  near_uniform: 2 configs
  Total: 9 configs
So 63 × 9 = 567 cells.
Each cell has 100 C₀ matrices.
Total curves: 567 × 100 = 56,700.

Each curve computation involves:
- For non-IV: batched solve of ~101 linear systems of size ≤8×8. This is very fast.
- For IV: simple arithmetic (no linear solve needed).

With numpy, solving 101 systems of 8×8 takes ~0.1ms. So 56,700 × 0.1ms = 5.67s for the core computation.

The precomputation of sufficient statistics for the 2D GH topologies (collider and mbias) with K=7 requires 10,000 quadrature points each, computing softmax over logits and weighted sums—roughly 1ms per topology, so about 18ms total across all parameter settings. Now I need to write the complete script, making sure to import from the existing module, implement the four adversarial C₀ types correctly, handle both non-decreasing and non-increasing topologies, detect IV weak instruments, and match the output format.

I notice the task mentions using `compute_bias_for_topology` from annot_sensitivity, but that function's signature doesn't align with what I need. The analytic approach from exp_d_conjecture_verify_v2 is cleaner and avoids sampling noise entirely. I'll use that instead.

The imports should work fine since the script is in the artifacts directory alongside exp_d_conjecture_verify_v2.py, and I'm adding artifacts to sys.path.

Examining the `compute_bias_curve` function from v2 more closely...

Writing the complete script... I'm checking whether `get_tau_true` will work correctly with my parameter structure—it expects a dict of all topologies' params, which matches what `make_params_with_beta` produces, so that should be fine. But I'm noticing a potential issue: for the IV topology, `compute_bias_curve` relies on `ss.FS` and `ss.RF` from the sufficient statistics, and I need to make sure `get_tau_true` is using compatible sufficient statistics when it calls `get_tau_at_C`. `bias_abs = np.abs(taus - tau_true)`, which becomes NaN when the denominator is near zero—that's expected behavior. For detecting weak IV cases, I'm checking if the first stage coefficient changes sign between the baseline and perturbed scenarios, which would indicate the denominator crosses zero within the interpolation range. I'll compute the exact crossing point and flag it as weak IV if it falls between 0 and 1. Now let me write out the full script with one more optimization to avoid redundant function calls.

Actually, I'm reconsidering the performance bottleneck here. With 56,700 calls to compute_bias_curve and each one solving 101 systems of 8×8 matrices, the linear algebra operations are going to dominate. Batching across different C₀ values would help, but restructuring the code for that isn't worth the added complexity when the whole experiment should still run in under a minute.

Let me just write the script and add progress tracking. One thing I need to be careful about: for the block_diag case with K=3 and split=1, the C₀ matrix has a repeated eigenvalue structure that could cause numerical issues, so I should verify it's being handled correctly when δ=1. different from each other and from the off-diagonal entries. Let me trace through the actual structure of the EZZ matrix more carefully by looking at how it's constructed in the code—I need to verify the exact pattern of which entries are zero and which contain the q values.

Looking at the determinant for a 3×3 case to understand when this matrix becomes singular...

Computing the determinant...

So the determinant equals q₀ · q₁ · q₂, which means the system is singular whenever any of the probability values equals zero. For the block diagonal case at δ=1 with K=3, the matrix C equals C₀, and I need to examine what happens to the misclassified probabilities. The determinant works out to be positive since both q[0] and q[1] are positive, so the system is actually solvable even in this edge case. I'm checking whether the parameters could cause q[k] to approach zero, but the DGP setup gives reasonable values that shouldn't trigger this issue. Now I need to decide whether to use the existing `compute_bias_curve` function or write my own loop—the tradeoff is that the existing function might compute more delta points than necessary.

I'm leaning toward using `compute_bias_curve` with a fine step size and just slicing to the [0,1] range, since the batched implementation is efficient enough. But I need to verify that delta_max is always at least 1.0 given the constraints on the diagonal elements of the transition matrix. Let me verify the minimum delta_max across different parameter combinations—checking near_perm with small epsilon values and various K sizes shows I'll consistently get at least 101 points from the arange call, so I'm confident using compute_bias_curve and slicing the results.

Now I need to handle a subtle edge case: the bias curve might have NaN values where the denominator approaches zero, which is distinct from the weak IV case where the denominator actually changes sign. I'll flag curves as weak_iv only when there's a sign change across [0,1], and for other curves with scattered NaN points, I'll just skip those values during analysis.

Writing the script now... Writing configuration setup... Writing configuration setup... Writing transition matrix functions...

Now I'm checking if we're in the 'iv' topology case and computing some crossing point logic based on the feature space and confusion matrix values. If that passes, I'm computing the full bias curve across delta values and checking whether we have enough samples to proceed.

I'm returning the bias values if we have sufficient data, then defining a function to measure monotonicity violations by looking at whether the bias is increasing or decreasing depending on the topology type. Finally, I'm setting up the main execution block with a random number generator and starting the adversarial monotonicity test.

Now I'm initializing accumulators to track results across different adversarial types, topologies, and K values...

Setting up the main nested loop to iterate through all combinations of K, beta configurations, and topologies, computing the true tau value for each configuration and skipping cases where tau is invalid or near zero.

Now I'm looping through each adversary type and configuration, generating multiple C0 matrices and computing curves to measure constraint violations, tracking weak curves and collecting epsilon values for valid results. Adding worst-case entries... Writing output structure... Writing results output... Printing diagnostic statistics...

Now I'm checking the parameter generation logic—specifically verifying that the confounding alpha vector and beta configuration are both the correct length relative to K, since they should both be K-1 dimensional. Looking at the parameter values for different configurations—the dY and a1 pools are being sliced correctly for each K value, and the alternating and same_sign variants are producing the expected coefficient arrays. Now I need to write this out to a file, but I'm realizing there might be an issue with how the compute function is being called with the topology and parameters.

The lambda functions in the verification script expect specific parameter keys for each topology—confounding needs p_A, alpha, beta_A, beta_T, and sigma_T; mediation needs tau, gamma, delta, and beta; collider needs tau, g, dT, and dY; and exposure needs beta and p_A. I'm concerned that modifying dY to have the first element be zero might affect the collider computation, so I should verify that the expected parameters are still present and compatible with what the functions expect. 0` means the reference category's U1 coefficient is 0, which matches the original params where a1[0] was already 0. Everything checks out, so I'm ready to finalize the script. I should also verify that the pool arrays are long enough for K=5 and K=7 in `make_all_params`, checking that the beta and alpha pools have sufficient elements for the larger category counts. Checking that all the parameter pools have the right dimensions for K=7: beta_A needs 6 elements which it has, and the remaining pools all need 7 elements each, which they do.

Now I'm ready to save the implementation and test it, but first I need to carefully parse the alternating_large beta configuration pattern to make sure I'm extending it correctly for K=7. I'm verifying the IV case logic in the bias computation—checking how the delta weighting combines with the feature space to produce the denominator for tau calculations.

Now I'm implementing the script properly, making sure to detect weak IV cases upfront by checking if the denominator crosses zero in the valid range before computing bias curves, which is more robust than handling NaNs afterward.

I need to verify that AnalyticIVSuffStats is imported...

Checking the imports...

I'm verifying that `compute_bias_curve` works with `AnalyticIVSuffStats` by confirming it accesses the right attributes—`FS` and `RF` for the IV case, and `p_A`, `E_TD`, `E_YD`, `E_T`, `E_T2`, `E_Y` for non-IV cases. Both stat classes have these, so we're good.

Now I need to handle the direction logic in `measure_violation` carefully: for non-decreasing topologies, violations occur when the bias curve drops (negative differences), while for non-increasing topologies, violations happen when it rises (positive differences). I'm setting up the logic to capture the maximum violation magnitude in each case.

I'm finalizing the script now, including the adversarial structure and parameters in the worst-case summary. Let me double-check the IV sufficient statistics computation to make sure it's correct when I modify parameters.

Checking IV computation... Writing bias calculation... So the monotonicity of the IV bias curve is completely independent of beta—the three configurations will show identical monotonicity patterns, just with different absolute magnitudes. Now I'm ready to implement the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "3bbacf48-81a7-424c-a0b9-67445c27960c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZishd7YrCtSrk7rJfijX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19384,
      "cache_read_input_tokens": 46251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19384
      },
      "output_tokens": 10,
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

### Assistant

_source line 16_

Now I have a clear picture of the codebase. The analytic plim approach in `exp_d_conjecture_verify_v2.py` is the right one to reuse. Writing the adversarial monotonicity test script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "9c260a9b-6b86-4d8a-b987-2a047839c504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZishd7YrCtSrk7rJfijX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19384,
      "cache_read_input_tokens": 46251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19384
      },
      "output_tokens": 10,
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

_source line 17_

<details open><summary>🔧 Tool call — Write · `toolu_019gDBC7UnoYSyk26XEMt3U4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nMF-1a: Adversarial Monotonicity Test for Conjecture 1.\n\nVerifies ε-approximate envelope monotonicity of |B(C(δ))| along\nC(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.\n\nGrid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nimport numpy as np\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom exp_d_conjecture_verify_v2 import (\n    ALL_TOPOS, NON_DECREASING, NON_INCREASING,\n    _COMPUTE_SS, make_all_params, get_tau_true,\n    compute_bias_curve,\n)\n\nK_VALUES = [3, 5, 7]\nN_DELTA = 101\nDELTA_STEP = 0.01\nN_C0 = 100\nSEED = 2024\nEPS_THRESHOLD = 0.001\n\nBETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']\nADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']\nADV_PARAMS = {\n    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],\n    'block_diag': [{}],\n    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],\n    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],\n}\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n\ndef make_beta_vec(name, K):\n    pools = {\n        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],\n        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],\n        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],\n    }\n    return np.array(pools[name][:K])\n\n\ndef make_params_with_beta(K, beta_name):\n    params = make_all_params(K)\n    bv = make_beta_vec(beta_name, K)\n    params['exposure']['beta'] = bv.copy()\n    params['iv']['beta'] = bv.copy()\n    params['mediation']['beta'] = bv.copy()\n    params['frontdoor']['beta'] = bv.copy()\n    params['confounding']['beta_A'] = bv[1:].copy()\n    params['collider']['dY'] = bv.copy()\n    params['mbias']['a1'] = bv.copy()\n    return params\n\n\ndef gen_C0(adv_type, cfg, K, rng):\n    if adv_type == 'near_perm':\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        e = cfg['eps']\n        return (1 - e) * P + e / K\n\n    if adv_type == 'block_diag':\n        split = max(1, K // 2)\n        C0 = np.zeros((K, K))\n        for j in range(K):\n            if j < split:\n                C0[:split, j] = 1.0 / split\n            else:\n                C0[split:, j] = 1.0 / (K - split)\n        return C0\n\n    if adv_type == 'sparse':\n        pd = cfg['p_diag']\n        C0 = np.zeros((K, K))\n        for k in range(K):\n            C0[k, k] = pd\n            off = [i for i in range(K) if i != k]\n            C0[rng.choice(off), k] = 1 - pd\n        return C0\n\n    if adv_type == 'near_uniform':\n        e = cfg['eps']\n        dv = 1.0 / K + e\n        ov = (1 - dv) / (K - 1)\n        C0 = np.full((K, K), ov)\n        np.fill_diagonal(C0, dv)\n        return C0\n\n\ndef compute_fixed_curve(topo, C0, ss, tau_true):\n    \"\"\"Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv).\"\"\"\n    if topo == 'iv':\n        FS = ss.FS\n        a = float(FS[1])\n        b = float((C0 @ FS)[1])\n        if abs(a) < 1e-15:\n            return None, True\n        if abs(a - b) > 1e-15:\n            d_cross = a / (a - b)\n            if 0 < d_cross < 1:\n                return None, True\n\n    deltas_full, bias_full = compute_bias_curve(\n        topo, C0, ss, tau_true, delta_step=DELTA_STEP)\n    n = min(N_DELTA, len(bias_full))\n    if n < N_DELTA:\n        return None, False\n    return bias_full[:N_DELTA], False\n\n\ndef measure_violation(bias_abs, topo):\n    \"\"\"Return max single-step violation magnitude.\"\"\"\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0.0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        drops = -diffs[diffs < 0]\n    else:\n        drops = diffs[diffs > 0]\n    return float(drops.max()) if len(drops) > 0 else 0.0\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"=\" * 78)\n    print(\"MF-1a: Adversarial Monotonicity Test\")\n    print(f\"  K={K_VALUES}  β={BETA_CONFIGS}\")\n    print(f\"  Adversarial: {ADV_TYPES}\")\n    print(f\"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}\")\n    print(\"=\" * 78)\n    sys.stdout.flush()\n\n    all_eps = []\n    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}\n    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}\n    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}\n    worst = []\n    total_weak_iv = 0\n    total_skipped = 0\n\n    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())\n    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs\n    cell_i = 0\n\n    for K in K_VALUES:\n        for beta_name in BETA_CONFIGS:\n            params = make_params_with_beta(K, beta_name)\n\n            for topo in ALL_TOPOS:\n                ss = _COMPUTE_SS[topo](K, params[topo])\n                tau_true = get_tau_true(topo, K, params, ss)\n\n                if np.isnan(tau_true) or abs(tau_true) < 1e-12:\n                    cell_i += n_adv_cfgs\n                    total_skipped += n_adv_cfgs * N_C0\n                    continue\n\n                for adv_type in ADV_TYPES:\n                    for adv_cfg in ADV_PARAMS[adv_type]:\n                        cell_i += 1\n                        cell_eps = []\n                        cell_nm = 0\n                        cell_weak = 0\n\n                        for _ in range(N_C0):\n                            C0 = gen_C0(adv_type, adv_cfg, K, rng)\n                            curve, weak = compute_fixed_curve(\n                                topo, C0, ss, tau_true)\n\n                            if weak:\n                                cell_weak += 1\n                                continue\n                            if curve is None:\n                                continue\n\n                            eps = measure_violation(curve, topo)\n                            cell_eps.append(eps)\n                            if eps > EPS_THRESHOLD:\n                                cell_nm += 1\n\n                        n_valid = len(cell_eps)\n                        if n_valid == 0:\n                            total_weak_iv += cell_weak\n                            continue\n\n                        mx = max(cell_eps)\n                        total_weak_iv += cell_weak\n                        all_eps.extend(cell_eps)\n\n                        for acc, key in [(by_adv, adv_type),\n                                         (by_topo, topo),\n                                         (by_K, str(K))]:\n                            acc[key]['n'] += n_valid\n                            acc[key]['nm'] += cell_nm\n                            acc[key]['mx'] = max(acc[key]['mx'], mx)\n\n                        if mx > EPS_THRESHOLD:\n                            worst.append({\n                                'topology': topo, 'K': K,\n                                'adversarial': adv_type,\n                                'adv_config': json.dumps(adv_cfg)\n                                              if adv_cfg else \"{}\",\n                                'beta': beta_name,\n                                'eps_abs': mx,\n                                'non_mono_frac': cell_nm / n_valid,\n                                'n_valid': n_valid,\n                                'weak_iv': cell_weak,\n                            })\n\n                        if cell_i % 63 == 0 or cell_i == n_cells:\n                            print(\n                                f\"  [{cell_i:>4}/{n_cells}] K={K} \"\n                                f\"{topo:<12} {adv_type:<14} \"\n                                f\"β={beta_name:<18} max_ε={mx:.6f} \"\n                                f\"nm={cell_nm}/{n_valid}  \"\n                                f\"({time.time()-t0:.1f}s)\")\n                            sys.stdout.flush()\n\n    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])\n    total_curves = len(all_eps)\n    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)\n\n    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}\n    fragile_topos = {'collider', 'mbias', 'iv'}\n\n    def fmt_acc(d):\n        return {k: {\n            'total_curves': v['n'],\n            'non_monotone_count': v['nm'],\n            'non_monotone_fraction': v['nm'] / max(v['n'], 1),\n            'max_eps_abs': v['mx'],\n        } for k, v in d.items()}\n\n    worst.sort(key=lambda x: -x['eps_abs'])\n    worst = worst[:20]\n\n    output = {\n        'description':\n            'Adversarial envelope monotonicity test for Conjecture 1',\n        'config': {\n            'K_values': K_VALUES,\n            'adversarial_types': ADV_TYPES,\n            'adversarial_params': ADV_PARAMS,\n            'topologies': ALL_TOPOS,\n            'beta_configs': BETA_CONFIGS,\n            'n_C0_per_cell': N_C0,\n            'n_delta_steps': N_DELTA,\n            'delta_step': DELTA_STEP,\n            'eps_threshold': EPS_THRESHOLD,\n            'seed': SEED,\n        },\n        'summary': {\n            'total_curves': total_curves,\n            'non_monotone_fraction':\n                total_nm / max(total_curves, 1),\n            'max_eps_abs': float(eps_arr.max()),\n            'median_eps_abs': float(np.median(eps_arr)),\n            'mean_eps_abs': float(np.mean(eps_arr)),\n            'p95_eps_abs': float(np.percentile(eps_arr, 95)),\n            'p99_eps_abs': float(np.percentile(eps_arr, 99)),\n            'safe_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in safe_topos)),\n            'fragile_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in fragile_topos)),\n            'total_weak_iv_filtered': total_weak_iv,\n            'total_skipped_zero_tau': total_skipped,\n        },\n        'by_adversarial_type': fmt_acc(by_adv),\n        'by_topology': fmt_acc(by_topo),\n        'by_K': fmt_acc(by_K),\n        'worst_cases': worst,\n        'elapsed_seconds': time.time() - t0,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n\n    print(f\"\\nJSON -> {out_path}\")\n    print(f\"\\n{'='*60}\")\n    print(f\"Total curves: {total_curves:,}  \"\n          f\"Non-monotone: {total_nm} \"\n          f\"({total_nm/max(total_curves,1)*100:.3f}%)\")\n    print(f\"Max ε_abs: {eps_arr.max():.6f}  \"\n          f\"Median: {np.median(eps_arr):.6f}\")\n    print(f\"Safe max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  \"\n          f\"Fragile max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}\")\n    print(f\"Weak-IV filtered: {total_weak_iv}\")\n\n    print(f\"\\nBy topology:\")\n    for t in ALL_TOPOS:\n        d = by_topo[t]\n        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'\n        print(f\"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy adversarial type:\")\n    for a in ADV_TYPES:\n        d = by_adv[a]\n        print(f\"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy K:\")\n    for k in K_VALUES:\n        d = by_K[str(k)]\n        print(f\"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    if worst:\n        print(f\"\\nWorst cases (top 5):\")\n        for w in worst[:5]:\n            print(f\"  {w['topology']:<14} K={w['K']} \"\n                  f\"{w['adversarial']:<14} \"\n                  f\"β={w['beta']:<18} ε={w['eps_abs']:.6f}\")\n\n    print(f\"\\nElapsed: {time.time()-t0:.1f}s\")\n    print('=' * 60)\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "eb9bb618-2a98-4679-a2e3-d044fe8c9e67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZishd7YrCtSrk7rJfijX4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19384,
      "cache_read_input_tokens": 46251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19384
      },
      "output_tokens": 10,
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

_source line 18 · 2026-05-23T17:46:19.722Z_

<details><summary>↩ Tool result · `toolu_019gDBC7UnoYSyk26XEMt3U4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "bd270f12-71e4-4feb-acf4-3b7201d1f73c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nMF-1a: Adversarial Monotonicity Test for Conjecture 1.\n\nVerifies ε-approximate envelope monotonicity of |B(C(δ))| along\nC(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.\n\nGrid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nimport numpy as np\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom exp_d_conjecture_verify_v2 import (\n    ALL_TOPOS, NON_DECREASING, NON_INCREASING,\n    _COMPUTE_SS, make_all_params, get_tau_true,\n    compute_bias_curve,\n)\n\nK_VALUES = [3, 5, 7]\nN_DELTA = 101\nDELTA_STEP = 0.01\nN_C0 = 100\nSEED = 2024\nEPS_THRESHOLD = 0.001\n\nBETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']\nADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']\nADV_PARAMS = {\n    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],\n    'block_diag': [{}],\n    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],\n    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],\n}\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n\ndef make_beta_vec(name, K):\n    pools = {\n        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],\n        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],\n        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],\n    }\n    return np.array(pools[name][:K])\n\n\ndef make_params_with_beta(K, beta_name):\n    params = make_all_params(K)\n    bv = make_beta_vec(beta_name, K)\n    params['exposure']['beta'] = bv.copy()\n    params['iv']['beta'] = bv.copy()\n    params['mediation']['beta'] = bv.copy()\n    params['frontdoor']['beta'] = bv.copy()\n    params['confounding']['beta_A'] = bv[1:].copy()\n    params['collider']['dY'] = bv.copy()\n    params['mbias']['a1'] = bv.copy()\n    return params\n\n\ndef gen_C0(adv_type, cfg, K, rng):\n    if adv_type == 'near_perm':\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        e = cfg['eps']\n        return (1 - e) * P + e / K\n\n    if adv_type == 'block_diag':\n        split = max(1, K // 2)\n        C0 = np.zeros((K, K))\n        for j in range(K):\n            if j < split:\n                C0[:split, j] = 1.0 / split\n            else:\n                C0[split:, j] = 1.0 / (K - split)\n        return C0\n\n    if adv_type == 'sparse':\n        pd = cfg['p_diag']\n        C0 = np.zeros((K, K))\n        for k in range(K):\n            C0[k, k] = pd\n            off = [i for i in range(K) if i != k]\n            C0[rng.choice(off), k] = 1 - pd\n        return C0\n\n    if adv_type == 'near_uniform':\n        e = cfg['eps']\n        dv = 1.0 / K + e\n        ov = (1 - dv) / (K - 1)\n        C0 = np.full((K, K), ov)\n        np.fill_diagonal(C0, dv)\n        return C0\n\n\ndef compute_fixed_curve(topo, C0, ss, tau_true):\n    \"\"\"Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv).\"\"\"\n    if topo == 'iv':\n        FS = ss.FS\n        a = float(FS[1])\n        b = float((C0 @ FS)[1])\n        if abs(a) < 1e-15:\n            return None, True\n        if abs(a - b) > 1e-15:\n            d_cross = a / (a - b)\n            if 0 < d_cross < 1:\n                return None, True\n\n    deltas_full, bias_full = compute_bias_curve(\n        topo, C0, ss, tau_true, delta_step=DELTA_STEP)\n    n = min(N_DELTA, len(bias_full))\n    if n < N_DELTA:\n        return None, False\n    return bias_full[:N_DELTA], False\n\n\ndef measure_violation(bias_abs, topo):\n    \"\"\"Return max single-step violation magnitude.\"\"\"\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0.0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        drops = -diffs[diffs < 0]\n    else:\n        drops = diffs[diffs > 0]\n    return float(drops.max()) if len(drops) > 0 else 0.0\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"=\" * 78)\n    print(\"MF-1a: Adversarial Monotonicity Test\")\n    print(f\"  K={K_VALUES}  β={BETA_CONFIGS}\")\n    print(f\"  Adversarial: {ADV_TYPES}\")\n    print(f\"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}\")\n    print(\"=\" * 78)\n    sys.stdout.flush()\n\n    all_eps = []\n    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}\n    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}\n    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}\n    worst = []\n    total_weak_iv = 0\n    total_skipped = 0\n\n    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())\n    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs\n    cell_i = 0\n\n    for K in K_VALUES:\n        for beta_name in BETA_CONFIGS:\n            params = make_params_with_beta(K, beta_name)\n\n            for topo in ALL_TOPOS:\n                ss = _COMPUTE_SS[topo](K, params[topo])\n                tau_true = get_tau_true(topo, K, params, ss)\n\n                if np.isnan(tau_true) or abs(tau_true) < 1e-12:\n                    cell_i += n_adv_cfgs\n                    total_skipped += n_adv_cfgs * N_C0\n                    continue\n\n                for adv_type in ADV_TYPES:\n                    for adv_cfg in ADV_PARAMS[adv_type]:\n                        cell_i += 1\n                        cell_eps = []\n                        cell_nm = 0\n                        cell_weak = 0\n\n                        for _ in range(N_C0):\n                            C0 = gen_C0(adv_type, adv_cfg, K, rng)\n                            curve, weak = compute_fixed_curve(\n                                topo, C0, ss, tau_true)\n\n                            if weak:\n                                cell_weak += 1\n                                continue\n                            if curve is None:\n                                continue\n\n                            eps = measure_violation(curve, topo)\n                            cell_eps.append(eps)\n                            if eps > EPS_THRESHOLD:\n                                cell_nm += 1\n\n                        n_valid = len(cell_eps)\n                        if n_valid == 0:\n                            total_weak_iv += cell_weak\n                            continue\n\n                        mx = max(cell_eps)\n                        total_weak_iv += cell_weak\n                        all_eps.extend(cell_eps)\n\n                        for acc, key in [(by_adv, adv_type),\n                                         (by_topo, topo),\n                                         (by_K, str(K))]:\n                            acc[key]['n'] += n_valid\n                            acc[key]['nm'] += cell_nm\n                            acc[key]['mx'] = max(acc[key]['mx'], mx)\n\n                        if mx > EPS_THRESHOLD:\n                            worst.append({\n                                'topology': topo, 'K': K,\n                                'adversarial': adv_type,\n                                'adv_config': json.dumps(adv_cfg)\n                                              if adv_cfg else \"{}\",\n                                'beta': beta_name,\n                                'eps_abs': mx,\n                                'non_mono_frac': cell_nm / n_valid,\n                                'n_valid': n_valid,\n                                'weak_iv': cell_weak,\n                            })\n\n                        if cell_i % 63 == 0 or cell_i == n_cells:\n                            print(\n                                f\"  [{cell_i:>4}/{n_cells}] K={K} \"\n                                f\"{topo:<12} {adv_type:<14} \"\n                                f\"β={beta_name:<18} max_ε={mx:.6f} \"\n                                f\"nm={cell_nm}/{n_valid}  \"\n                                f\"({time.time()-t0:.1f}s)\")\n                            sys.stdout.flush()\n\n    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])\n    total_curves = len(all_eps)\n    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)\n\n    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}\n    fragile_topos = {'collider', 'mbias', 'iv'}\n\n    def fmt_acc(d):\n        return {k: {\n            'total_curves': v['n'],\n            'non_monotone_count': v['nm'],\n            'non_monotone_fraction': v['nm'] / max(v['n'], 1),\n            'max_eps_abs': v['mx'],\n        } for k, v in d.items()}\n\n    worst.sort(key=lambda x: -x['eps_abs'])\n    worst = worst[:20]\n\n    output = {\n        'description':\n            'Adversarial envelope monotonicity test for Conjecture 1',\n        'config': {\n            'K_values': K_VALUES,\n            'adversarial_types': ADV_TYPES,\n            'adversarial_params': ADV_PARAMS,\n            'topologies': ALL_TOPOS,\n            'beta_configs': BETA_CONFIGS,\n            'n_C0_per_cell': N_C0,\n            'n_delta_steps': N_DELTA,\n            'delta_step': DELTA_STEP,\n            'eps_threshold': EPS_THRESHOLD,\n            'seed': SEED,\n        },\n        'summary': {\n            'total_curves': total_curves,\n            'non_monotone_fraction':\n                total_nm / max(total_curves, 1),\n            'max_eps_abs': float(eps_arr.max()),\n            'median_eps_abs': float(np.median(eps_arr)),\n            'mean_eps_abs': float(np.mean(eps_arr)),\n            'p95_eps_abs': float(np.percentile(eps_arr, 95)),\n            'p99_eps_abs': float(np.percentile(eps_arr, 99)),\n            'safe_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in safe_topos)),\n            'fragile_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in fragile_topos)),\n            'total_weak_iv_filtered': total_weak_iv,\n            'total_skipped_zero_tau': total_skipped,\n        },\n        'by_adversarial_type': fmt_acc(by_adv),\n        'by_topology': fmt_acc(by_topo),\n        'by_K': fmt_acc(by_K),\n        'worst_cases': worst,\n        'elapsed_seconds': time.time() - t0,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n\n    print(f\"\\nJSON -> {out_path}\")\n    print(f\"\\n{'='*60}\")\n    print(f\"Total curves: {total_curves:,}  \"\n          f\"Non-monotone: {total_nm} \"\n          f\"({total_nm/max(total_curves,1)*100:.3f}%)\")\n    print(f\"Max ε_abs: {eps_arr.max():.6f}  \"\n          f\"Median: {np.median(eps_arr):.6f}\")\n    print(f\"Safe max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  \"\n          f\"Fragile max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}\")\n    print(f\"Weak-IV filtered: {total_weak_iv}\")\n\n    print(f\"\\nBy topology:\")\n    for t in ALL_TOPOS:\n        d = by_topo[t]\n        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'\n        print(f\"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy adversarial type:\")\n    for a in ADV_TYPES:\n        d = by_adv[a]\n        print(f\"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy K:\")\n    for k in K_VALUES:\n        d = by_K[str(k)]\n        print(f\"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    if worst:\n        print(f\"\\nWorst cases (top 5):\")\n        for w in worst[:5]:\n            print(f\"  {w['topology']:<14} K={w['K']} \"\n                  f\"{w['adversarial']:<14} \"\n                  f\"β={w['beta']:<18} ε={w['eps_abs']:.6f}\")\n\n    print(f\"\\nElapsed: {time.time()-t0:.1f}s\")\n    print('=' * 60)\n\n\nif __name__ == '__main__':\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Running the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "512a2b33-84ff-459b-909f-3495e2ab051a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgDi6hfHjJ6weE8XemcdkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34163,
      "cache_read_input_tokens": 65635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34163
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01CZ9bhP4rz8aVJagmafiWUu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py 2>&1",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "78ddf18a-5757-4449-80b2-ff015a160532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgDi6hfHjJ6weE8XemcdkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34163,
      "cache_read_input_tokens": 65635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34163
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

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b9v5p203t",
  "tool_use_id": "toolu_01CZ9bhP4rz8aVJagmafiWUu",
  "description": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py 2>&1",
  "task_type": "local_bash",
  "uuid": "5633e4f1-ac9b-4a3b-9a2d-812bfdb19bd8",
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c"
}
```

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b9v5p203t",
  "tool_use_id": "toolu_01CZ9bhP4rz8aVJagmafiWUu",
  "status": "completed",
  "output_file": "",
  "summary": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py 2>&1",
  "uuid": "d9815c30-4a24-4c85-a9fe-c15f82e846e4",
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c"
}
```

---

### Tool result

_source line 23 · 2026-05-23T17:46:37.424Z_

<details><summary>↩ Tool result · `toolu_01CZ9bhP4rz8aVJagmafiWUu`</summary>

```text
==============================================================================
MF-1a: Adversarial Monotonicity Test
  K=[3, 5, 7]  β=['alternating_large', 'same_sign', 'alternating_small']
  Adversarial: ['near_perm', 'block_diag', 'sparse', 'near_uniform']
  N_C0=100  δ steps=101  ε threshold=0.001
==============================================================================
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py:682: RuntimeWarning: divide by zero encountered in divide
  taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
  [  63/567] K=3 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (1.3s)
  [ 126/567] K=3 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (2.5s)
  [ 189/567] K=3 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (3.8s)
  [ 252/567] K=5 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (5.2s)
  [ 315/567] K=5 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (6.7s)
  [ 378/567] K=5 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (8.1s)
  [ 441/567] K=7 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (10.8s)
  [ 504/567] K=7 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (12.6s)
  [ 567/567] K=7 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (14.3s)

JSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json

============================================================
Total curves: 54,611  Non-monotone: 6517 (11.933%)
Max ε_abs: 0.016365  Median: 0.000000
Safe max ε: 0.016365  Fragile max ε: 0.013177
Weak-IV filtered: 2089

By topology:
  confounding    [non-dec]  n=  8100  nm= 1706  (21.06%)  max_ε=0.016365
  mediation      [non-dec]  n=  8100  nm= 1612  (19.90%)  max_ε=0.013039
  collider       [non-inc]  n=  8100  nm= 1431  (17.67%)  max_ε=0.013177
  exposure       [non-dec]  n=  8100  nm=   55  (0.68%)  max_ε=0.008413
  mbias          [non-inc]  n=  8100  nm=  117  (1.44%)  max_ε=0.001426
  iv             [non-dec]  n=  6011  nm=    0  (0.00%)  max_ε=0.000000
  frontdoor      [non-dec]  n=  8100  nm= 1596  (19.70%)  max_ε=0.015828

By adversarial type:
  near_perm       n= 17279  nm= 6096  (35.28%)  max_ε=0.016365
  block_diag      n=  6300  nm=    0  (0.00%)  max_ε=0.000396
  sparse          n= 18432  nm=  421  (2.28%)  max_ε=0.002615
  near_uniform    n= 12600  nm=    0  (0.00%)  max_ε=0.000000

By K:
  K=3  n= 18068  nm= 2595  (14.36%)  max_ε=0.016365
  K=5  n= 18239  nm= 2177  (11.94%)  max_ε=0.013449
  K=7  n= 18304  nm= 1745  (9.53%)  max_ε=0.012282

Worst cases (top 5):
  confounding    K=3 near_perm      β=alternating_large  ε=0.016365
  frontdoor      K=3 near_perm      β=alternating_large  ε=0.015828
  confounding    K=5 near_perm      β=alternating_large  ε=0.013449
  collider       K=3 near_perm      β=alternating_large  ε=0.013177
  frontdoor      K=3 near_perm      β=alternating_large  ε=0.013120

Elapsed: 14.3s
============================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "136eb5ab-aa2e-4cb9-b6b0-c246509740b5",
  "tool_use_result": {
    "stdout": "==============================================================================\nMF-1a: Adversarial Monotonicity Test\n  K=[3, 5, 7]  β=['alternating_large', 'same_sign', 'alternating_small']\n  Adversarial: ['near_perm', 'block_diag', 'sparse', 'near_uniform']\n  N_C0=100  δ steps=101  ε threshold=0.001\n==============================================================================\n/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py:682: RuntimeWarning: divide by zero encountered in divide\n  taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)\n  [  63/567] K=3 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (1.3s)\n  [ 126/567] K=3 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (2.5s)\n  [ 189/567] K=3 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (3.8s)\n  [ 252/567] K=5 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (5.2s)\n  [ 315/567] K=5 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (6.7s)\n  [ 378/567] K=5 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (8.1s)\n  [ 441/567] K=7 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (10.8s)\n  [ 504/567] K=7 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (12.6s)\n  [ 567/567] K=7 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (14.3s)\n\nJSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json\n\n============================================================\nTotal curves: 54,611  Non-monotone: 6517 (11.933%)\nMax ε_abs: 0.016365  Median: 0.000000\nSafe max ε: 0.016365  Fragile max ε: 0.013177\nWeak-IV filtered: 2089\n\nBy topology:\n  confounding    [non-dec]  n=  8100  nm= 1706  (21.06%)  max_ε=0.016365\n  mediation      [non-dec]  n=  8100  nm= 1612  (19.90%)  max_ε=0.013039\n  collider       [non-inc]  n=  8100  nm= 1431  (17.67%)  max_ε=0.013177\n  exposure       [non-dec]  n=  8100  nm=   55  (0.68%)  max_ε=0.008413\n  mbias          [non-inc]  n=  8100  nm=  117  (1.44%)  max_ε=0.001426\n  iv             [non-dec]  n=  6011  nm=    0  (0.00%)  max_ε=0.000000\n  frontdoor      [non-dec]  n=  8100  nm= 1596  (19.70%)  max_ε=0.015828\n\nBy adversarial type:\n  near_perm       n= 17279  nm= 6096  (35.28%)  max_ε=0.016365\n  block_diag      n=  6300  nm=    0  (0.00%)  max_ε=0.000396\n  sparse          n= 18432  nm=  421  (2.28%)  max_ε=0.002615\n  near_uniform    n= 12600  nm=    0  (0.00%)  max_ε=0.000000\n\nBy K:\n  K=3  n= 18068  nm= 2595  (14.36%)  max_ε=0.016365\n  K=5  n= 18239  nm= 2177  (11.94%)  max_ε=0.013449\n  K=7  n= 18304  nm= 1745  (9.53%)  max_ε=0.012282\n\nWorst cases (top 5):\n  confounding    K=3 near_perm      β=alternating_large  ε=0.016365\n  frontdoor      K=3 near_perm      β=alternating_large  ε=0.015828\n  confounding    K=5 near_perm      β=alternating_large  ε=0.013449\n  collider       K=3 near_perm      β=alternating_large  ε=0.013177\n  frontdoor      K=3 near_perm      β=alternating_large  ε=0.013120\n\nElapsed: 14.3s\n============================================================",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
The experiment ran successfully in 14.3 seconds. Let me analyze the results:

1. **Total curves**: 54,611 (some IV curves filtered for weak IV)
2. **Non-monotone fraction**: 11.93% (6,517 curves with ε > 0.001)
3. **Max ε_abs**: 0.016365 — very small, confirming approximate monotonicity

Key findings:
- **near_perm is the most adversarial**: 35.28% non-monotone rate, max ε=0.016


- **block_diag and near_uniform** show perfect monotonicity with negligible violations, while sparse has only 2.28% non-monotone curves with tiny max ε values. Across topologies, confounding and frontdoor exhibit the most violations around 20%, though all remain extremely small. Increasing K consistently reduces violations, dropping from 14.36% at K=3 down to 9.53% at K=7, with the worst cases appearing in confounding scenarios with near_perm.

The maximum absolute violation of 0.016 across all conditions falls well below the paper's theoretical bound of 0.06, validating Conjecture 1 even under adversarial settings. Now I'm registering the artifact and preparing to report these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "d5442bad-f8ac-42dc-8bd5-33a51d727942",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9qR4EWjWDZjrwBqXGth8L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1671,
      "cache_read_input_tokens": 99798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1671
      },
      "output_tokens": 9,
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

### Assistant

_source line 25_

Experiment completed in 14.3s. Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "cba4507b-d60e-4947-99b2-65dcef25ab8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9qR4EWjWDZjrwBqXGth8L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1671,
      "cache_read_input_tokens": 99798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1671
      },
      "output_tokens": 9,
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

_source line 26_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014MnUsxUHEPGMKXcvi9yyVj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "cfd567cb-fc97-4866-9a64-57e512468ab1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9qR4EWjWDZjrwBqXGth8L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1671,
      "cache_read_input_tokens": 99798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1671
      },
      "output_tokens": 9,
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

_source line 27 · 2026-05-23T17:46:49.246Z_

<details><summary>↩ Tool result · `toolu_014MnUsxUHEPGMKXcvi9yyVj`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "eb5967bc-9702-4ba3-93fc-9ffd32d4e94c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01CzbDPce1d4Ta5xaW5zLiEn`</summary>

```json
{
  "name": "MF-1a Adversarial Monotonicity Test Results",
  "type": "data",
  "description": "Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.",
  "project": "causal_annot_error_attrib",
  "source_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json",
  "tags": [
    "conjecture1",
    "monotonicity",
    "adversarial",
    "MF-1a"
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
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "c8615fc5-44d1-4e35-bf11-25607bc2c3c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NT4RLHn9rWcYFTEWde8LP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 101469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1100
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

_source line 29 · 2026-05-23T17:46:56.870Z_

<details><summary>↩ Tool result · `toolu_01CzbDPce1d4Ta5xaW5zLiEn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_877baa\", \"name\": \"MF-1a Adversarial Monotonicity Test Results\", \"type\": \"data\", \"description\": \"Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.\", \"path\": \"projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results.json\", \"url\": null, \"project\": \"causal_annot_error_attrib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T17:46:56.702531+00:00\", \"tags\": [\"conjecture1\", \"monotonicity\", \"adversarial\", \"MF-1a\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "d479c7ae-035e-462e-85d4-6dcf8855bd42",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260523_877baa\\\", \\\"name\\\": \\\"MF-1a Adversarial Monotonicity Test Results\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.\\\", \\\"path\\\": \\\"projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"causal_annot_error_attrib\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-23T17:46:56.702531+00:00\\\", \\\"tags\\\": [\\\"conjecture1\\\", \\\"monotonicity\\\", \\\"adversarial\\\", \\\"MF-1a\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_877baa\", \"name\": \"MF-1a Adversarial Monotonicity Test Results\", \"type\": \"data\", \"description\": \"Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.\", \"path\": \"projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results.json\", \"url\": null, \"project\": \"causal_annot_error_attrib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T17:46:56.702531+00:00\", \"tags\": [\"conjecture1\", \"monotonicity\", \"adversarial\", \"MF-1a\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Done. Let me summarize the results for the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "f80dd6a2-c683-4c54-8f43-2687be78ea6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGnB9Jf926BCXwvs7faGKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 102569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 673
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

### Assistant

_source line 31_

**MF-1a 完成。** 54,611 条曲线，14.3s 运行。

核心发现：

| 维度 | max ε_abs | 非单调率 |
|------|-----------|----------|
| **总体** | **0.0164** | 11.9% |
| safe topos (conf/med/exp/fd) | 0.0164 | — |
| fragile topos (col/mbias/iv) | 0.0132 | — |

**按 adversarial 类型：**
- **near_perm**: 最具对抗性，35.3% 非单调，max ε=0.016
- **block_diag**: 0% 非单调（确定性结构，无违反）
- **sparse**: 2.3% 非单调，max ε=0.003
- **near_uniform**: 0% 非单调

**按 topology：**
- confounding/mediation/frontdoor 约 20% 曲线有微小违反（ε < 0.017）
- exposure 仅 0.68%，mbias 1.44%
- IV: 0 违反（过滤掉 2,089 条 weak-IV 曲线后）

**结论：** 所有 adversarial 结构下 max ε_abs = 0.016，远低于论文声称的 0.06 bound。Conjecture 1 的 ε-approximate envelope monotonicity 在 adversarial 条件下成立。违反集中在 near-permutation 矩阵 + alternating_large β + 小 K 的组合。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "uuid": "90c4585f-1827-44e7-a3c1-63253b56c3cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGnB9Jf926BCXwvs7faGKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 102569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 673
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

### Task result

_source line 32_

**MF-1a 完成。** 54,611 条曲线，14.3s 运行。

核心发现：

| 维度 | max ε_abs | 非单调率 |
|------|-----------|----------|
| **总体** | **0.0164** | 11.9% |
| safe topos (conf/med/exp/fd) | 0.0164 | — |
| fragile topos (col/mbias/iv) | 0.0132 | — |

**按 adversarial 类型：**
- **near_perm**: 最具对抗性，35.3% 非单调，max ε=0.016
- **block_diag**: 0% 非单调（确定性结构，无违反）
- **sparse**: 2.3% 非单调，max ε=0.003
- **near_uniform**: 0% 非单调

**按 topology：**
- confounding/mediation/frontdoor 约 20% 曲线有微小违反（ε < 0.017）
- exposure 仅 0.68%，mbias 1.44%
- IV: 0 违反（过滤掉 2,089 条 weak-IV 曲线后）

**结论：** 所有 adversarial 结构下 max ε_abs = 0.016，远低于论文声称的 0.06 bound。Conjecture 1 的 ε-approximate envelope monotonicity 在 adversarial 条件下成立。违反集中在 near-permutation 矩阵 + alternating_large β + 小 K 的组合。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 622985,
  "duration_api_ms": 609674,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "fa128911-6674-49cb-98cc-9c4b05c12b8c",
  "total_cost_usd": 1.70067375,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 91401,
    "cache_read_input_tokens": 454143,
    "output_tokens": 35978,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 91401,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 463,
        "cache_read_input_tokens": 102569,
        "cache_creation_input_tokens": 673,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 673
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2731,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002846,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 35978,
      "cacheReadInputTokens": 454143,
      "cacheCreationInputTokens": 91401,
      "webSearchRequests": 0,
      "costUSD": 1.69782775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "954107f7-a264-4d3a-b9dc-d5618eb7892b"
}
```

</details>

---
