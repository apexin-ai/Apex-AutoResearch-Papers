# code plan006 asv calibration — Part 1 of 2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

[Transcript overview](../code-plan006-asv-calibration.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/33/338e318b31ce9967ae2e.json)

## Before a recorded user message

## Before a recorded user message

7 recorded events


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
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "4180d1e4-758a-4038-8f93-b7150d2e802f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down. I need to:

1. Read existing scripts (plan_001, plan_004, plan_005) on the server to understand reusable functions
2. Write plan_006_asv_empirical.py
3. Deploy and dry-run on the server

Let me start by reading the existing scripts to understand the codebase.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "bdc9d4a3-9213-44cd-b980-69e6712d1a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTy6vdtHvHgN5PWoe6Hznt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14504,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14504
      },
      "output_tokens": 23,
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


### Runtime record

_source line 4_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779415200,
    "rateLimitType": "seven_day",
    "utilization": 0.91,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "8aa88705-fd2f-4f65-b311-21e5eecc6892",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Assistant

_source line 5_

先读取服务器上已有的脚本，提取可复用的函数结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "d3c50d8b-4997-478e-b6cd-be3b9e8fff7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTy6vdtHvHgN5PWoe6Hznt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14504,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14504
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01Xdq4NgC5tevfUpdE3UyVh8`</summary>

```json
{
  "description": "Read existing plan scripts",
  "subagent_type": "Explore",
  "prompt": "Read the following files in the current working directory and report their full contents (or as much as possible):\n\n1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py\n2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py\n3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py\n4. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py (if it exists)\n5. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py (if it exists)\n6. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md\n\nReport the full content of each file. I need to understand:\n- The plim bias computation functions for each topology\n- The ASV computation functions (magnitude, significance, sign_flip)\n- DGP parameter conventions\n- How confusion matrices are constructed and used\n- The topologies list and their parameter structures\n\nBe very thorough - read each file completely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "4218a9ec-bedb-47bc-9523-334851e79e9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTy6vdtHvHgN5PWoe6Hznt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14504,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14504
      },
      "output_tokens": 23,
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Read existing plan scripts",
  "task_type": "local_agent",
  "prompt": "Read the following files in the current working directory and report their full contents (or as much as possible):\n\n1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py\n2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py\n3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py\n4. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py (if it exists)\n5. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py (if it exists)\n6. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md\n\nReport the full content of each file. I need to understand:\n- The plim bias computation functions for each topology\n- The ASV computation functions (magnitude, significance, sign_flip)\n- DGP parameter conventions\n- How confusion matrices are constructed and used\n- The topologies list and their parameter structures\n\nBe very thorough - read each file completely.",
  "uuid": "92a82f66-d563-4be3-abeb-16e9a6692c05",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


## Round 1

## Round 1

41 recorded events


### User

_source line 8 · 2026-05-20T21:00:39.091Z_

Read the following files in the current working directory and report their full contents (or as much as possible):

1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py
2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py
3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py
4. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py (if it exists)
5. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py (if it exists)
6. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md

Report the full content of each file. I need to understand:
- The plim bias computation functions for each topology
- The ASV computation functions (magnitude, significance, sign_flip)
- DGP parameter conventions
- How confusion matrices are constructed and used
- The topologies list and their parameter structures

Be very thorough - read each file completely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "7fecfdc2-7a2a-4484-8729-df9b63beb811"
}
```

</details>

---


### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Reading plan_001_collider_mbias_iv.py",
  "usage": {
    "total_tokens": 15906,
    "tool_uses": 1,
    "duration_ms": 1604
  },
  "last_tool_name": "Read",
  "uuid": "b4f48fdf-5021-40ab-b413-a0b379eb7024",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01Up1jUceWPTD2NNFPfubW7g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "077e0097-60dd-4bb3-85c8-9c28b66a9fc2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 11 · 2026-05-20T21:00:40.710Z_

<details><summary>↩ Tool result · `toolu_01Up1jUceWPTD2NNFPfubW7g`</summary>

```text
1	"""
2	Collider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.
3	K=3 LLM annotation error bias propagation in causal inference.
4	"""
5	
6	import numpy as np
7	from collections import OrderedDict
8	import time
9	
10	# ── Constants ────────────────────────────────────────────────────────────────
11	
12	BETA_MIXED = np.array([0.0, 1.0, -0.5])
13	BETA_SAME  = np.array([0.0, 1.0,  0.5])
14	
15	C1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
16	C2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])
17	C3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])
18	C4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])
19	C5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])
20	C6_DIFF_BASE      = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
21	
22	ALL_C = OrderedDict([
23	    ("C1_sym_high",   C1_SYMMETRIC_HIGH),
24	    ("C2_asymmetric", C2_ASYMMETRIC),
25	    ("C3_struct_12",  C3_STRUCTURAL_12),
26	    ("C4_weak_diag",  C4_WEAK_DIAG),
27	    ("C5_near_perm",  C5_NEAR_PERM),
28	    ("C6_diff_base",  C6_DIFF_BASE),
29	])
30	
31	# ── Utilities ────────────────────────────────────────────────────────────────
32	
33	def _generate_Astar(A, C, rng):
34	    probs = C[:, A]
35	    cum = np.cumsum(probs, axis=0)
36	    u = rng.uniform(size=len(A))
37	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
38	
39	
40	def _generate_Astar_fixed_u(A, C, u):
41	    probs = C[:, A]
42	    cum = np.cumsum(probs, axis=0)
43	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
44	
45	
46	def _softmax_sample(logits, rng):
47	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
48	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
49	    cum = np.cumsum(probs, axis=1)
50	    u = rng.uniform(size=logits.shape[0])
51	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
52	
53	
54	def _ols(Z, Y):
55	    return np.linalg.solve(Z.T @ Z, Z.T @ Y)
56	
57	
58	# ══════════════════════════════════════════════════════════════════════════════
59	# DAG 1: COLLIDER — T -> A <- Y
60	# ══════════════════════════════════════════════════════════════════════════════
61	
62	COLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)
63	
64	
65	def _gen_collider(N, params, rng):
66	    T = rng.normal(0, 1, N)
67	    eps = rng.normal(0, 1, N)
68	    Y = params['tau'] * T + eps
69	    logits = np.column_stack([
70	        np.zeros(N),
71	        params['g1'] + params['dT'] * T + params['dY'] * Y,
72	        params['g2'] + params['dT2'] * T + params['dY2'] * Y,
73	    ])
74	    A = _softmax_sample(logits, rng)
75	    return T, Y, A
76	
77	
78	def theory_collider(C, params, N_approx=2_000_000, seed=999):
79	    rng = np.random.default_rng(seed)
80	    T, Y, A = _gen_collider(N_approx, params, rng)
81	    Astar = _generate_Astar(A, C, rng)
82	    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
83	    ones = np.ones(N_approx)
84	    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
85	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
86	    return tau_ctrl, tau_nc
87	
88	
89	def mc_collider(C, params, N=10_000, n_reps=1000, seed=0):
90	    tau_ctrl_arr = np.empty(n_reps)
91	    tau_nc_arr = np.empty(n_reps)
92	    for r in range(n_reps):
93	        rng = np.random.default_rng(seed + r)
94	        T, Y, A = _gen_collider(N, params, rng)
95	        Astar = _generate_Astar(A, C, rng)
96	        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
97	        ones = np.ones(N)
98	        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
99	        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
100	    return tau_ctrl_arr.mean(), tau_nc_arr.mean()
101	
102	
103	# ══════════════════════════════════════════════════════════════════════════════
104	# DAG 2: M-BIAS — U1 -> {A,T}, U2 -> {A,Y}
105	# ══════════════════════════════════════════════════════════════════════════════
106	
107	MBIAS_PARAMS = dict(tau=1.0, delta=1.0, lam=1.0,
108	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
109	
110	
111	def _gen_mbias(N, params, rng):
112	    U1 = rng.normal(0, 1, N)
113	    U2 = rng.normal(0, 1, N)
114	    T = params['delta'] * U1 + rng.normal(0, 1, N)
115	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
116	    logits = np.column_stack([
117	        np.zeros(N),
118	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
119	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
120	    ])
121	    A = _softmax_sample(logits, rng)
122	    return T, Y, A
123	
124	
125	def theory_mbias(C, params, N_approx=2_000_000, seed=999):
126	    rng = np.random.default_rng(seed)
127	    T, Y, A = _gen_mbias(N_approx, params, rng)
128	    Astar = _generate_Astar(A, C, rng)
129	    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
130	    ones = np.ones(N_approx)
131	    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
132	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
133	    return tau_ctrl, tau_nc
134	
135	
136	def mc_mbias(C, params, N=10_000, n_reps=1000, seed=0):
137	    tau_ctrl_arr = np.empty(n_reps)
138	    tau_nc_arr = np.empty(n_reps)
139	    for r in range(n_reps):
140	        rng = np.random.default_rng(seed + r)
141	        T, Y, A = _gen_mbias(N, params, rng)
142	        Astar = _generate_Astar(A, C, rng)
143	        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
144	        ones = np.ones(N)
145	        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
146	        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
147	    return tau_ctrl_arr.mean(), tau_nc_arr.mean()
148	
149	
150	# ══════════════════════════════════════════════════════════════════════════════
151	# DAG 3: INSTRUMENT — Z_iv -> A -> Y, U -> {A, Y}
152	# ══════════════════════════════════════════════════════════════════════════════
153	
154	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
155	
156	
157	def _gen_iv(N, beta, params, rng):
158	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
159	    U = rng.normal(0, 1, N)
160	    eps = rng.normal(0, 1, N)
161	    logits = np.column_stack([
162	        np.zeros(N),
163	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
164	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
165	    ])
166	    A = _softmax_sample(logits, rng)
167	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
168	         + params['lam'] * U + eps)
169	    return Z_iv, U, Y, A
170	
171	
172	def theory_iv(C, beta, params, N_approx=2_000_000, seed=999):
173	    rng = np.random.default_rng(seed)
174	    Z_iv, U, Y, A = _gen_iv(N_approx, beta, params, rng)
175	    Astar = _generate_Astar(A, C, rng)
176	    z1 = Z_iv == 1
177	    z0 = Z_iv == 0
178	
179	    RF = Y[z1].mean() - Y[z0].mean()
180	
181	    result = {'RF': RF}
182	    for k in [1, 2]:
183	        fs_star = (Astar[z1] == k).mean() - (Astar[z0] == k).mean()
184	        fs_true = (A[z1] == k).mean() - (A[z0] == k).mean()
185	        result[f'FS{k}_star'] = fs_star
186	        result[f'FS{k}_true'] = fs_true
187	        result[f'Wald{k}_star'] = RF / fs_star if abs(fs_star) > 1e-8 else np.nan
188	        result[f'Wald{k}_true'] = RF / fs_true if abs(fs_true) > 1e-8 else np.nan
189	
190	    ones = np.ones(N_approx)
191	    X_star = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
192	    result['ols_star'] = _ols(X_star, Y)
193	    X_true = np.column_stack([ones, (A == 1).astype(float), (A == 2).astype(float)])
194	    result['ols_true'] = _ols(X_true, Y)
195	
196	    return result
197	
198	
199	def mc_iv(C, beta, params, N=10_000, n_reps=1000, seed=0):
200	    RF_arr = np.empty(n_reps)
201	    FS1_arr = np.empty(n_reps)
202	    FS2_arr = np.empty(n_reps)
203	    ols_arr = np.empty((n_reps, 3))
204	    for r in range(n_reps):
205	        rng = np.random.default_rng(seed + r)
206	        Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
207	        Astar = _generate_Astar(A, C, rng)
208	        z1 = Z_iv == 1
209	        z0 = Z_iv == 0
210	        RF_arr[r] = Y[z1].mean() - Y[z0].mean()
211	        FS1_arr[r] = (Astar[z1] == 1).mean() - (Astar[z0] == 1).mean()
212	        FS2_arr[r] = (Astar[z1] == 2).mean() - (Astar[z0] == 2).mean()
213	        ones = np.ones(N)
214	        X = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
215	        ols_arr[r] = _ols(X, Y)
216	
217	    wald1_mc = RF_arr.mean() / FS1_arr.mean()
218	    wald2_mc = RF_arr.mean() / FS2_arr.mean()
219	    ols_mc = ols_arr.mean(axis=0)
220	    return wald1_mc, wald2_mc, ols_mc
221	
222	
223	# ══════════════════════════════════════════════════════════════════════════════
224	# RANDOM C SEARCH (reuse base dataset, vary only C)
225	# ══════════════════════════════════════════════════════════════════════════════
226	
227	def _fast_ols_tau(T, Y, A_star, N, sT, sTT, sY, sTY):
228	    """Inline OLS for Y ~ 1 + T + D1 + D2, returns coef on T. Avoids column_stack."""
229	    m1 = A_star == 1
230	    m2 = A_star == 2
231	    n1 = float(m1.sum())
232	    n2 = float(m2.sum())
233	    tD1 = T[m1].sum()
234	    tD2 = T[m2].sum()
235	    yD1 = Y[m1].sum()
236	    yD2 = Y[m2].sum()
237	    ZZ = np.array([[N, sT, n1, n2],
238	                   [sT, sTT, tD1, tD2],
239	                   [n1, tD1, n1, 0.0],
240	                   [n2, tD2, 0.0, n2]])
241	    ZY = np.array([sY, sTY, yD1, yD2])
242	    return np.linalg.solve(ZZ, ZY)[1]
243	
244	
245	def rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):
246	    rng = np.random.default_rng(seed)
247	    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)
248	    u = rng.uniform(size=N_ap)
249	    N = float(N_ap)
250	    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
251	    tau_nc = sTY / sTT - sT * sY / (N * sTT)  # simplified no-control
252	    ones = np.ones(N_ap)
253	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
254	
255	    rng_s = np.random.default_rng(seed + 1)
256	    biases = np.empty(n_search)
257	    for i in range(n_search):
258	        C = rng_s.dirichlet([1, 1, 1], size=3).T
259	        Astar = _generate_Astar_fixed_u(A, C, u)
260	        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - COLLIDER_PARAMS['tau']
261	    return biases, tau_nc - COLLIDER_PARAMS['tau']
262	
263	
264	def rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):
265	    rng = np.random.default_rng(seed)
266	    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)
267	    u = rng.uniform(size=N_ap)
268	    N = float(N_ap)
269	    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
270	    ones = np.ones(N_ap)
271	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
272	
273	    rng_s = np.random.default_rng(seed + 1)
274	    biases = np.empty(n_search)
275	    for i in range(n_search):
276	        C = rng_s.dirichlet([1, 1, 1], size=3).T
277	        Astar = _generate_Astar_fixed_u(A, C, u)
278	        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - MBIAS_PARAMS['tau']
279	    return biases, tau_nc - MBIAS_PARAMS['tau']
280	
281	
282	def rand_search_iv(beta, n_search=100_000, N_ap=50_000, seed=42):
283	    rng = np.random.default_rng(seed)
284	    Z_iv, U, Y, A = _gen_iv(N_ap, beta, IV_PARAMS, rng)
285	    u = rng.uniform(size=N_ap)
286	    z1 = Z_iv == 1
287	    z0 = Z_iv == 0
288	    n1_z = float(z1.sum())
289	    n0_z = float(z0.sum())
290	    RF = Y[z1].sum() / n1_z - Y[z0].sum() / n0_z
291	    FS1_true = (A[z1] == 1).sum() / n1_z - (A[z0] == 1).sum() / n0_z
292	    FS2_true = (A[z1] == 2).sum() / n1_z - (A[z0] == 2).sum() / n0_z
293	    W1_true = RF / FS1_true if abs(FS1_true) > 1e-8 else np.nan
294	    W2_true = RF / FS2_true if abs(FS2_true) > 1e-8 else np.nan
295	
296	    rng_s = np.random.default_rng(seed + 1)
297	    w1_vals = np.empty(n_search)
298	    w2_vals = np.empty(n_search)
299	    for i in range(n_search):
300	        C = rng_s.dirichlet([1, 1, 1], size=3).T
301	        Astar = _generate_Astar_fixed_u(A, C, u)
302	        fs1 = (Astar[z1] == 1).sum() / n1_z - (Astar[z0] == 1).sum() / n0_z
303	        fs2 = (Astar[z1] == 2).sum() / n1_z - (Astar[z0] == 2).sum() / n0_z
304	        w1_vals[i] = RF / fs1 if abs(fs1) > 1e-8 else np.nan
305	        w2_vals[i] = RF / fs2 if abs(fs2) > 1e-8 else np.nan
306	    return w1_vals, w2_vals, W1_true, W2_true
307	
308	
309	# ══════════════════════════════════════════════════════════════════════════════
310	# MAIN
311	# ══════════════════════════════════════════════════════════════════════════════
312	
313	def _print_section(title):
314	    print()
315	    print("=" * 80)
316	    print(title)
317	    print("=" * 80)
318	
319	
320	def main():
321	    np.set_printoptions(precision=6, suppress=True)
322	    t0 = time.time()
323	
324	    # ── DAG 1: Collider ─────────────────────────────────────────────────────
325	    _print_section("DAG 1: COLLIDER -- T -> A <- Y")
326	    p = COLLIDER_PARAMS
327	    print(f"DGP: T~N(0,1), Y={p['tau']}*T+eps, "
328	          f"A|T,Y softmax(dT={p['dT']}, dY={p['dY']}, dT2={p['dT2']}, dY2={p['dY2']})")
329	    print(f"Researcher error: controls A* in Y ~ 1 + T + D*1 + D*2")
330	    print(f"Truth: T and Y are NOT confounded => no-control OLS is consistent")
331	    print()
332	
333	    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
334	           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
335	    print(hdr)
336	    print("  " + "-" * 80)
337	
338	    for cn, C in ALL_C.items():
339	        th_c, th_n = theory_collider(C, p)
340	        mc_c, mc_n = mc_collider(C, p)
341	        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
342	        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
343	              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")
344	
345	    print()
346	    print("Violation analysis:")
347	    th_c1, th_n1 = theory_collider(C1_SYMMETRIC_HIGH, p)
348	    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
349	          f" (should = tau={p['tau']} since no confounding)")
350	    print(f"  Controlling collider A* induces spurious T-eps association")
351	
352	    t1 = time.time()
353	    print(f"\nRandom C search (100k)... ", end="", flush=True)
354	    bc, bnc = rand_search_collider()
355	    print(f"done ({time.time()-t1:.0f}s)")
356	    print(f"  No-control bias: {bnc:+.4f}")
357	    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
358	          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
359	    worse = np.sum(np.abs(bc) > np.abs(bnc))
360	    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")
361	
362	    # ── DAG 2: M-bias ───────────────────────────────────────────────────────
363	    _print_section("DAG 2: M-BIAS -- U1 -> {A,T}, U2 -> {A,Y}")
364	    p = MBIAS_PARAMS
365	    print(f"DGP: U1,U2~N(0,1) indep, T={p['delta']}*U1+eta,"
366	          f" Y={p['tau']}*T+{p['lam']}*U2+eps")
367	    print(f"A|U1,U2 softmax(a1={p['a1']}, a2={p['a2']}, a3={p['a3']}, a4={p['a4']})")
368	    print(f"Researcher error: controls A* => opens U1->A<-U2 path (M-bias)")
369	    print(f"Truth: U2 indep T => no confounding of T->Y, no-control is consistent")
370	    print()
371	
372	    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
373	           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
374	    print(hdr)
375	    print("  " + "-" * 80)
376	
377	    for cn, C in ALL_C.items():
378	        th_c, th_n = theory_mbias(C, p)
379	        mc_c, mc_n = mc_mbias(C, p)
380	        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
381	        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
382	              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")
383	
384	    print()
385	    print("Violation analysis:")
386	    th_c1, th_n1 = theory_mbias(C1_SYMMETRIC_HIGH, p)
387	    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
388	          f" (should = tau={p['tau']} since U2 indep T)")
389	    print(f"  Controlling A* opens M-bias path: T <- U1 -> A <- U2 -> Y")
390	
391	    t1 = time.time()
392	    print(f"\nRandom C search (100k)... ", end="", flush=True)
393	    bc, bnc = rand_search_mbias()
394	    print(f"done ({time.time()-t1:.0f}s)")
395	    print(f"  No-control bias: {bnc:+.4f}")
396	    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
397	          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
398	    worse = np.sum(np.abs(bc) > np.abs(bnc))
399	    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")
400	
401	    # ── DAG 3: Instrument ────────────────────────────────────────────────────
402	    for bname, beta in [("BETA_MIXED", BETA_MIXED), ("BETA_SAME", BETA_SAME)]:
403	        _print_section(
404	            f"DAG 3: INSTRUMENT -- Z->A->Y, U->{{A,Y}}  [{bname}: b={beta}]")
405	        p = IV_PARAMS
406	        print(f"DGP: Z~Bern(0.5), U~N(0,1), Y=b1*D1+b2*D2+{p['lam']}*U+eps")
407	        print(f"A|Z,U softmax(dZ={p['dZ']}, dU={p['dU']}, dZ2={p['dZ2']}, dU2={p['dU2']})")
408	        print(f"Under-identified: 1 IV for 2 endogenous dummies => per-dummy Wald")
409	        print(f"Wald_k = RF/FS*_k estimates (b1*pi1+b2*pi2)/pi*_k, not b_k")
410	        print()
411	
412	        hdr2 = (f"  {'C':<16}"
413	                f" {'W1* th':>8} {'W1* mc':>8} {'ok':>3}"
414	                f" {'W2* th':>8} {'W2* mc':>8} {'ok':>3}"
415	                f" {'OLS b1':>8} {'mc':>8} {'ok':>3}"
416	                f" {'OLS b2':>8} {'mc':>8} {'ok':>3}")
417	        print(hdr2)
418	        print("  " + "-" * 110)
419	
420	        for cn, C in ALL_C.items():
421	            th = theory_iv(C, beta, p)
422	            mc_w1, mc_w2, mc_ols = mc_iv(C, beta, p)
423	
424	            o1 = "Y" if abs(th['Wald1_star'] - mc_w1) < 0.10 else "N"
425	            o2 = "Y" if abs(th['Wald2_star'] - mc_w2) < 0.10 else "N"
426	            o3 = "Y" if abs(th['ols_star'][1] - mc_ols[1]) < 0.02 else "N"
427	            o4 = "Y" if abs(th['ols_star'][2] - mc_ols[2]) < 0.02 else "N"
428	
429	            def _fmt(v, w=8):
430	                return f"{v:>{w}.4f}" if np.isfinite(v) else f"{'nan':>{w}}"
431	
432	            print(f"  {cn:<16}"
433	                  f" {_fmt(th['Wald1_star'])} {_fmt(mc_w1)} {o1:>3}"
434	                  f" {_fmt(th['Wald2_star'])} {_fmt(mc_w2)} {o2:>3}"
435	                  f" {th['ols_star'][1]:>8.4f} {mc_ols[1]:>8.4f} {o3:>3}"
436	                  f" {th['ols_star'][2]:>8.4f} {mc_ols[2]:>8.4f} {o4:>3}")
437	
438	        print()
439	        th1 = theory_iv(C1_SYMMETRIC_HIGH, beta, p)
440	        print("Violation analysis (C1_sym_high):")
441	        print(f"  True beta = [{beta[1]}, {beta[2]}]")
442	        print(f"  Reduced form (ITT): {th1['RF']:.4f}")
443	        print(f"  First stage true:  pi1={th1['FS1_true']:.4f}, pi2={th1['FS2_true']:.4f}")
444	        print(f"  First stage A*:    pi*1={th1['FS1_star']:.4f}, pi*2={th1['FS2_star']:.4f}")
445	        print(f"  Wald true A:  W1={th1['Wald1_true']:.4f}, W2={th1['Wald2_true']:.4f}")
446	        print(f"  Wald A*:      W1={th1['Wald1_star']:.4f}, W2={th1['Wald2_star']:.4f}")
447	        print(f"  OLS true A:   [{th1['ols_true'][1]:.4f}, {th1['ols_true'][2]:.4f}]"
448	              f" (biased by U)")
449	        print(f"  OLS A*:       [{th1['ols_star'][1]:.4f}, {th1['ols_star'][2]:.4f}]"
450	              f" (biased by U + misclassification)")
451	
452	        # Analytical insight: how C transforms first stages
453	        print(f"\n  FS transformation by C:")
454	        print(f"    FS*_k = sum_j C[k,j] * FS_j")
455	        for cn2, C2 in [("C1_sym_high", C1_SYMMETRIC_HIGH),
456	                        ("C4_weak_diag", C4_WEAK_DIAG),
457	                        ("C5_near_perm", C5_NEAR_PERM)]:
458	            th2 = theory_iv(C2, beta, p)
459	            fs_true = np.array([-(th2['FS1_true']+th2['FS2_true']),
460	                                th2['FS1_true'], th2['FS2_true']])
461	            fs_star_calc = C2 @ fs_true
462	            print(f"    {cn2}: FS_true={fs_true}, C@FS={fs_star_calc},"
463	                  f" FS*=[{th2['FS1_star']:.4f}, {th2['FS2_star']:.4f}]")
464	
465	        t1 = time.time()
466	        print(f"\n  Random C search (100k)... ", end="", flush=True)
467	        w1v, w2v, w1t, w2t = rand_search_iv(beta)
468	        print(f"done ({time.time()-t1:.0f}s)")
469	        v1 = np.isfinite(w1v)
470	        v2 = np.isfinite(w2v)
471	        w1b = w1v - w1t
472	        w2b = w2v - w2t
473	        print(f"    Wald1 true={w1t:.4f}: A* vals mean={np.nanmean(w1v):+.4f},"
474	              f" std={np.nanstd(w1v):.4f},"
475	              f" range=[{np.nanmin(w1v):+.4f}, {np.nanmax(w1v):+.4f}],"
476	              f" valid={v1.sum()}/{len(w1v)}")
477	        print(f"    Wald2 true={w2t:.4f}: A* vals mean={np.nanmean(w2v):+.4f},"
478	              f" std={np.nanstd(w2v):.4f},"
479	              f" range=[{np.nanmin(w2v):+.4f}, {np.nanmax(w2v):+.4f}],"
480	              f" valid={v2.sum()}/{len(w2v)}")
481	        print(f"    Delta from true: W1 mean={np.nanmean(w1b):+.4f},"
482	              f" W2 mean={np.nanmean(w2b):+.4f}")
483	
484	    print(f"\nTotal: {time.time() - t0:.1f}s")
485	
486	
487	if __name__ == "__main__":
488	    main()
489	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "4905d61d-481b-4208-b9e0-be167bf81e2c"
}
```

</details>

---


### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Reading plan_001_mediation_frontdoor.py",
  "usage": {
    "total_tokens": 15909,
    "tool_uses": 2,
    "duration_ms": 1817
  },
  "last_tool_name": "Read",
  "uuid": "bc0e6e02-6786-4ef4-b377-de9a6515cce7",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01LzwoUJu5qNDZULnSH5ffL8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "9a464f9a-ef0b-436c-b148-f64e776e2b1f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 14 · 2026-05-20T21:00:40.918Z_

<details><summary>↩ Tool result · `toolu_01LzwoUJu5qNDZULnSH5ffL8`</summary>

```text
1	#!/usr/bin/env python3
2	# -*- coding: utf-8 -*-
3	"""Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification."""
4	import numpy as np
5	import time
6	import warnings
7	from collections import OrderedDict
8	
9	warnings.filterwarnings('ignore')
10	
11	# ================================================================
12	# Configuration
13	# ================================================================
14	K = 3
15	N_MC = 10_000
16	N_REPS = 1_000
17	N_LARGE = 50_000_000
18	N_RANDOM = 100_000
19	
20	BETA_MIXED = np.array([0.0, 1.0, -0.5])
21	BETA_SAME  = np.array([0.0, 1.0,  0.5])
22	
23	TAU = 0.5
24	GAMMA_MED = np.array([0.0, 0.5, -0.3])
25	DELTA_MED = np.array([0.0, 0.8, -0.6])
26	
27	ALPHA_U = 1.0
28	LAMBDA_U = 1.0
29	GAMMA_FD = np.array([0.0, 0.5, -0.3])
30	DELTA_FD = np.array([0.0, 1.0, -0.8])
31	
32	C_DICT = OrderedDict([
33	    ("1_sym_high",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
34	    ("2_asymmetric", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),
35	    ("3_struct_12",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),
36	    ("4_weak_diag",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),
37	    ("5_near_perm",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),
38	    ("6_diff_base",  np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
39	])
40	
41	COEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']
42	
43	
44	# ================================================================
45	# Helpers
46	# ================================================================
47	def softmax(x):
48	    e = np.exp(x - x.max())
49	    return e / e.sum()
50	
51	
52	def p_cat(t, g, d):
53	    return softmax(g + d * t)
54	
55	
56	def gen_Astar(A, C, rng):
57	    pr = C[:, A]
58	    cu = np.cumsum(pr, axis=0)
59	    u = rng.uniform(size=len(A))
60	    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)
61	
62	
63	def ols(Z, Y):
64	    return np.linalg.lstsq(Z, Y, rcond=None)[0]
65	
66	
67	def fv(v, w=8, p=4):
68	    return '[' + ' '.join(f'{x:>{w}.{p}f}' for x in v) + ']'
69	
70	
71	def fm(th, mc, se, k=2):
72	    ok = np.abs(mc - th) < k * se
73	    return ''.join('✓' if o else '✗' for o in ok), ok.all()
74	
75	
76	# ================================================================
77	# DAG 1  Mediation: T -> A -> Y
78	#
79	# DGP:  T ~ Bern(0.5)
80	#        A | T ~ Cat(softmax(gamma + delta*T))
81	#        Y = beta0 + beta1*D1 + beta2*D2 + tau*T + eps
82	#        A* | A ~ Cat(C[:, A])
83	#
84	# Researcher regression:  Y ~ 1 + T + D*_1 + D*_2
85	#
86	# Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
87	# eps indep of Z  =>  plim = (E[Z'Z])^{-1} E[Z'X] beta
88	#
89	# Key moments:
90	#   q_t = C @ p_{A|T=t}           (P(A*|T=t))
91	#   q_marg = 0.5*(q_0 + q_1)
92	#   E[D*_j * D_k] = C[j,k] * p_marg[k]
93	# ================================================================
94	def plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED):
95	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
96	    q0, q1 = C @ p0, C @ p1
97	    pm = .5 * (p0 + p1)
98	    qm = .5 * (q0 + q1)
99	
100	    EZZ = np.array([
101	        [1,      .5,        qm[1],      qm[2]     ],
102	        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],
103	        [qm[1],  .5*q1[1],  qm[1],      0         ],
104	        [qm[2],  .5*q1[2],  0,          qm[2]     ]])
105	
106	    EZX = np.array([
107	        [1,      .5,        pm[1],            pm[2]           ],
108	        [.5,     .5,        .5*p1[1],         .5*p1[2]        ],
109	        [qm[1],  .5*q1[1],  C[1,1]*pm[1],    C[1,2]*pm[2]   ],
110	        [qm[2],  .5*q1[2],  C[2,1]*pm[1],    C[2,2]*pm[2]   ]])
111	
112	    b = np.array([beta[0], tau, beta[1], beta[2]])
113	    return np.linalg.solve(EZZ, EZX @ b)
114	
115	
116	def mc_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED,
117	           nr=N_REPS, N=N_MC, seed=42):
118	    rng = np.random.default_rng(seed)
119	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
120	    out = np.zeros((nr, 4))
121	    for r in range(nr):
122	        T = rng.binomial(1, .5, N)
123	        pr = np.where(T[:, None] == 0, p0, p1)
124	        cu = np.cumsum(pr, axis=1)
125	        u = rng.uniform(size=N)
126	        A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
127	        D1 = (A == 1).astype(float)
128	        D2 = (A == 2).astype(float)
129	        Y = beta[0] + beta[1]*D1 + beta[2]*D2 + tau*T + rng.normal(0, 1, N)
130	        As = gen_Astar(A, C, rng)
131	        Z = np.column_stack([np.ones(N), T.astype(float),
132	                             (As == 1).astype(float), (As == 2).astype(float)])
133	        out[r] = ols(Z, Y)
134	    return out.mean(0), out.std(0) / np.sqrt(nr)
135	
136	
137	def rsearch_med(beta, tau, g=GAMMA_MED, d=DELTA_MED,
138	                ns=N_RANDOM, seed=999):
139	    rng = np.random.default_rng(seed)
140	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
141	    pm = .5 * (p0 + p1)
142	    b = np.array([beta[0], tau, beta[1], beta[2]])
143	    clean = plim_med(np.eye(K), beta, tau, g, d)
144	
145	    Cs = np.zeros((ns, K, K))
146	    for i in range(K):
147	        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)
148	
149	    q0 = Cs @ p0
150	    q1 = Cs @ p1
151	    qm = .5 * (q0 + q1)
152	
153	    EZZ = np.zeros((ns, 4, 4))
154	    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = .5
155	    EZZ[:, 0, 2] = EZZ[:, 2, 0] = qm[:, 1]
156	    EZZ[:, 0, 3] = EZZ[:, 3, 0] = qm[:, 2]
157	    EZZ[:, 1, 1] = .5
158	    EZZ[:, 1, 2] = EZZ[:, 2, 1] = .5 * q1[:, 1]
159	    EZZ[:, 1, 3] = EZZ[:, 3, 1] = .5 * q1[:, 2]
160	    EZZ[:, 2, 2] = qm[:, 1]
161	    EZZ[:, 3, 3] = qm[:, 2]
162	
163	    EZX = np.zeros((ns, 4, 4))
164	    EZX[:, 0, 0] = 1;       EZX[:, 0, 1] = .5
165	    EZX[:, 0, 2] = pm[1];   EZX[:, 0, 3] = pm[2]
166	    EZX[:, 1, 0] = .5;      EZX[:, 1, 1] = .5
167	    EZX[:, 1, 2] = .5 * p1[1]; EZX[:, 1, 3] = .5 * p1[2]
168	    EZX[:, 2, 0] = qm[:, 1];   EZX[:, 2, 1] = .5 * q1[:, 1]
169	    EZX[:, 2, 2] = Cs[:, 1, 1] * pm[1]; EZX[:, 2, 3] = Cs[:, 1, 2] * pm[2]
170	    EZX[:, 3, 0] = qm[:, 2];   EZX[:, 3, 1] = .5 * q1[:, 2]
171	    EZX[:, 3, 2] = Cs[:, 2, 1] * pm[1]; EZX[:, 3, 3] = Cs[:, 2, 2] * pm[2]
172	
173	    rhs = np.einsum('nij,j->ni', EZX, b)
174	    pl = np.linalg.solve(EZZ, rhs[:, :, None])[:, :, 0]
175	
176	    df = np.abs(pl - clean)
177	    viol = np.any(df > .01, 1).mean()
178	    nz = np.abs(clean) > 1e-6
179	    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
180	    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
181	    return viol, sign, amp
182	
183	
184	# ================================================================
185	# DAG 2  Front-door: T -> M -> Y,  U -> T,  U -> Y
186	#
187	# DGP:  U ~ N(0,1)
188	#        T = alpha_U * U + eta,  eta ~ N(0,1)
189	#        M | T ~ Cat(softmax(gamma + delta*T))
190	#        Y = beta1*D_{M,1} + beta2*D_{M,2} + lambda*U + eps
191	#        M* | M ~ Cat(C[:, M])
192	#
193	# Researcher regression:  Y ~ 1 + T + D*_{M,1} + D*_{M,2}
194	#
195	# T correlated with U (confounding), so E[Z'(lambda*U)] != 0.
196	# Use large-sample moment approximation:
197	#   plim = (E[Z'Z])^{-1} E[Z'Y]   estimated from N_LARGE samples.
198	#
199	# For fast random search, pre-compute sufficient statistics:
200	#   E[D_{M,k}], E[D_{M,k}*T], E[D_{M,k}*Y]  for k=0,1,2
201	# Then for any C:
202	#   E[D*_j] = sum_k C[j,k]*E[D_{M,k}]   etc.
203	# ================================================================
204	def _gen_fd(N, beta, rng, g=GAMMA_FD, d=DELTA_FD,
205	            aU=ALPHA_U, lU=LAMBDA_U):
206	    U = rng.normal(0, 1, N)
207	    T = aU * U + rng.normal(0, 1, N)
208	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
209	    lo -= lo.max(1, keepdims=True)
210	    e = np.exp(lo)
211	    p = e / e.sum(1, keepdims=True)
212	    cu = np.cumsum(p, axis=1)
213	    u = rng.uniform(size=N)
214	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
215	    DM1 = (M == 1).astype(float)
216	    DM2 = (M == 2).astype(float)
217	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
218	    return T, M, Y, U
219	
220	
221	def precomp_fd(beta, N=N_LARGE, seed=123):
222	    rng = np.random.default_rng(seed)
223	    T, M, Y, _ = _gen_fd(N, beta, rng)
224	    DM = np.zeros((N, K))
225	    for k in range(K):
226	        DM[:, k] = (M == k).astype(float)
227	    return dict(
228	        E_T=T.mean(), E_T2=(T**2).mean(),
229	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
230	        E_DM=DM.mean(0),
231	        E_DM_T=(DM * T[:, None]).mean(0),
232	        E_DM_Y=(DM * Y[:, None]).mean(0))
233	
234	
235	def plim_fd(C, st):
236	    ds  = C @ st['E_DM']
237	    dst = C @ st['E_DM_T']
238	    dsy = C @ st['E_DM_Y']
239	    ET, ET2 = st['E_T'], st['E_T2']
240	    EY, ETY = st['E_Y'], st['E_TY']
241	
242	    EZZ = np.array([
243	        [1,      ET,      ds[1],    ds[2]   ],
244	        [ET,     ET2,     dst[1],   dst[2]  ],
245	        [ds[1],  dst[1],  ds[1],    0       ],
246	        [ds[2],  dst[2],  0,        ds[2]   ]])
247	
248	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
249	    return np.linalg.solve(EZZ, EZY)
250	
251	
252	def mc_fd(C, beta, nr=N_REPS, N=N_MC, seed=42):
253	    rng = np.random.default_rng(seed)
254	    out = np.zeros((nr, 4))
255	    for r in range(nr):
256	        T, M, Y, _ = _gen_fd(N, beta, rng)
257	        Ms = gen_Astar(M, C, rng)
258	        Z = np.column_stack([np.ones(N), T,
259	                             (Ms == 1).astype(float),
260	                             (Ms == 2).astype(float)])
261	        out[r] = ols(Z, Y)
262	    return out.mean(0), out.std(0) / np.sqrt(nr)
263	
264	
265	def rsearch_fd(st, ns=N_RANDOM, seed=999):
266	    rng = np.random.default_rng(seed)
267	    clean = plim_fd(np.eye(K), st)
268	
269	    Cs = np.zeros((ns, K, K))
270	    for i in range(K):
271	        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)
272	
273	    E_DMs   = Cs @ st['E_DM']
274	    E_DMs_T = Cs @ st['E_DM_T']
275	    E_DMs_Y = Cs @ st['E_DM_Y']
276	    ET, ET2 = st['E_T'], st['E_T2']
277	    EY, ETY = st['E_Y'], st['E_TY']
278	
279	    EZZ = np.zeros((ns, 4, 4))
280	    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = ET
281	    EZZ[:, 0, 2] = EZZ[:, 2, 0] = E_DMs[:, 1]
282	    EZZ[:, 0, 3] = EZZ[:, 3, 0] = E_DMs[:, 2]
283	    EZZ[:, 1, 1] = ET2
284	    EZZ[:, 1, 2] = EZZ[:, 2, 1] = E_DMs_T[:, 1]
285	    EZZ[:, 1, 3] = EZZ[:, 3, 1] = E_DMs_T[:, 2]
286	    EZZ[:, 2, 2] = E_DMs[:, 1]
287	    EZZ[:, 3, 3] = E_DMs[:, 2]
288	
289	    EZY = np.zeros((ns, 4))
290	    EZY[:, 0] = EY;   EZY[:, 1] = ETY
291	    EZY[:, 2] = E_DMs_Y[:, 1]
292	    EZY[:, 3] = E_DMs_Y[:, 2]
293	
294	    pl = np.linalg.solve(EZZ, EZY[:, :, None])[:, :, 0]
295	
296	    df = np.abs(pl - clean)
297	    viol = np.any(df > .01, 1).mean()
298	    nz = np.abs(clean) > 1e-6
299	    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
300	    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
301	    return viol, sign, amp
302	
303	
304	# ================================================================
305	# Main
306	# ================================================================
307	def main():
308	    t0 = time.time()
309	    np.set_printoptions(precision=4, suppress=True)
310	
311	    for bn, beta in [("mixed [0,1,-0.5]", BETA_MIXED),
312	                      ("same [0,1,0.5]",   BETA_SAME)]:
313	
314	        # ---- DAG 1: Mediation ----
315	        print(f"\n{'='*90}")
316	        print(f"  MEDIATION: T -> A -> Y  |  beta={bn}")
317	        print(f"{'='*90}")
318	        p0, p1 = p_cat(0, GAMMA_MED, DELTA_MED), p_cat(1, GAMMA_MED, DELTA_MED)
319	        print(f"  P(A|T=0)={fv(p0,6,3)}  P(A|T=1)={fv(p1,6,3)}  tau={TAU}")
320	        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")
321	
322	        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
323	        print(hdr)
324	        print(f"  {'-'*92}")
325	
326	        all_ok = True
327	        for cn, C in C_DICT.items():
328	            th = plim_med(C, beta, TAU)
329	            mc, se = mc_med(C, beta, TAU)
330	            ms, ok = fm(th, mc, se)
331	            if not ok:
332	                all_ok = False
333	            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")
334	
335	        status = 'ALL MATCH' if all_ok else 'MISMATCH DETECTED'
336	        print(f"  >>> {status}")
337	
338	        t1 = time.time()
339	        v, s, a = rsearch_med(beta, TAU)
340	        t2 = time.time()
341	        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
342	              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
343	
344	        # ---- DAG 2: Front-door ----
345	        print(f"\n{'='*90}")
346	        print(f"  FRONT-DOOR: T -> M -> Y, U -> T, U -> Y  |  beta={bn}")
347	        print(f"{'='*90}")
348	        print(f"  alpha_U={ALPHA_U}  lambda_U={LAMBDA_U}")
349	        print(f"  M|T softmax: gamma={GAMMA_FD}  delta={DELTA_FD}")
350	        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")
351	
352	        t1 = time.time()
353	        st = precomp_fd(beta)
354	        t2 = time.time()
355	        print(f"  Moments pre-computed (N={N_LARGE//10**6}M, {t2-t1:.1f}s)\n")
356	
357	        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
358	        print(hdr)
359	        print(f"  {'-'*92}")
360	
361	        all_ok = True
362	        for cn, C in C_DICT.items():
363	            th = plim_fd(C, st)
364	            mc, se = mc_fd(C, beta)
365	            ms, ok = fm(th, mc, se, k=3)
366	            if not ok:
367	                all_ok = False
368	            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")
369	
370	        status = 'ALL MATCH (3σ)' if all_ok else 'MISMATCH DETECTED'
371	        print(f"  >>> {status}")
372	
373	        t1 = time.time()
374	        v, s, a = rsearch_fd(st)
375	        t2 = time.time()
376	        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
377	              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
378	
379	    print(f"\n{'='*90}")
380	    print(f"  Total: {time.time()-t0:.1f}s")
381	    print(f"{'='*90}")
382	
383	
384	if __name__ == "__main__":
385	    main()
386	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5befa87e-5522-48ee-945d-cb79ff048f21"
}
```

</details>

---


### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Reading plan_005_asv_extended.py",
  "usage": {
    "total_tokens": 15912,
    "tool_uses": 3,
    "duration_ms": 2007
  },
  "last_tool_name": "Read",
  "uuid": "246f927d-fad3-424c-a8bb-dcf02207194a",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01NUYhNAfwGG4JMXp1gCswPV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "f140327b-9dcb-43bf-923e-cf4b5fd00787",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 17 · 2026-05-20T21:00:41.375Z_

<details><summary>↩ Tool result · `toolu_01NUYhNAfwGG4JMXp1gCswPV`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_005: ASV framework extension to M-bias, IV, front-door topologies.
4	Extends plan_004 v3 (envelope monotonicity + magnitude/sign-flip dual reporting)
5	to complete Claim 2 coverage across all 6 DAG topologies.
6	"""
7	
8	import numpy as np
9	import json
10	import time
11	
12	K = 3
13	
14	# ============================================================================
15	# Utilities (from plan_004 v3)
16	# ============================================================================
17	
18	def softmax_sample(logits, rng):
19	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
20	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
21	    cum = np.cumsum(probs, axis=1)
22	    u = rng.uniform(size=logits.shape[0])
23	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
24	
25	
26	def generate_Astar(A, C, rng):
27	    probs = C[:, A]
28	    cum = np.cumsum(probs, axis=0)
29	    u = rng.uniform(size=len(A))
30	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
31	
32	
33	def ols_with_dummies(Y, T, Astar, K=3):
34	    N = len(Y)
35	    D = np.zeros((N, K - 1))
36	    for k in range(1, K):
37	        D[:, k - 1] = (Astar == k).astype(float)
38	    X = np.column_stack([np.ones(N), T, D])
39	    try:
40	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
41	        resid = Y - X @ beta
42	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
43	        XtX_inv = np.linalg.inv(X.T @ X)
44	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
45	    except np.linalg.LinAlgError:
46	        beta = np.full(X.shape[1], np.nan)
47	        se = np.full(X.shape[1], np.nan)
48	    return beta, se
49	
50	
51	# ============================================================================
52	# C(delta) Parameterization (from plan_004 v3)
53	# ============================================================================
54	
55	class LinearInterpolation:
56	    def __call__(self, C0, delta):
57	        K = C0.shape[0]
58	        C_d = (1 - delta) * np.eye(K) + delta * C0
59	        C_d = np.maximum(C_d, 0.0)
60	        col_sums = C_d.sum(axis=0)
61	        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
62	        C_d = C_d / col_sums
63	        return C_d
64	
65	    def delta_range(self, C0=None):
66	        if C0 is None:
67	            return (0.0, 5.0)
68	        min_diag = np.diag(C0).min()
69	        if min_diag >= 1.0:
70	            return (0.0, 10.0)
71	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
72	        return (0.0, delta_max)
73	
74	
75	# ============================================================================
76	# C matrices (from plan_004 v3)
77	# ============================================================================
78	
79	def make_C_list():
80	    return {
81	        "C1_sym": np.array([[0.80, 0.10, 0.10],
82	                            [0.10, 0.80, 0.10],
83	                            [0.10, 0.10, 0.80]]),
84	        "C2_high": np.array([[0.90, 0.05, 0.05],
85	                             [0.05, 0.90, 0.05],
86	                             [0.05, 0.05, 0.90]]),
87	        "C3_asym": np.array([[0.70, 0.20, 0.10],
88	                             [0.15, 0.70, 0.15],
89	                             [0.10, 0.15, 0.75]]),
90	        "C4_weak": np.array([[0.60, 0.20, 0.20],
91	                             [0.20, 0.60, 0.20],
92	                             [0.15, 0.15, 0.70]]),
93	        "C5_perm": np.array([[0.40, 0.30, 0.30],
94	                             [0.30, 0.40, 0.30],
95	                             [0.30, 0.30, 0.40]]),
96	        "C6_diff": np.array([[0.85, 0.075, 0.075],
97	                             [0.15, 0.70, 0.15],
98	                             [0.05, 0.05, 0.90]]),
99	    }
100	
101	
102	def normalize_C_list(C_dict):
103	    out = {}
104	    for name, C in C_dict.items():
105	        C = np.maximum(C, 0.0)
106	        cs = C.sum(axis=0)
107	        cs = np.where(cs < 1e-10, 1.0, cs)
108	        out[name] = C / cs
109	    return out
110	
111	
112	def random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):
113	    C = np.zeros((K, K))
114	    for k in range(K):
115	        alphas = np.full(K, offdiag_alpha)
116	        alphas[k] = diag_alpha
117	        C[:, k] = rng.dirichlet(alphas)
118	    return C
119	
120	
121	# ============================================================================
122	# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y
123	# ============================================================================
124	
125	MBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,
126	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
127	
128	
129	def _gen_mbias(N, params, rng):
130	    U1 = rng.normal(0, 1, N)
131	    U2 = rng.normal(0, 1, N)
132	    T = params['delta'] * U1 + rng.normal(0, 1, N)
133	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
134	    logits = np.column_stack([
135	        np.zeros(N),
136	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
137	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
138	    ])
139	    A = softmax_sample(logits, rng)
140	    return T, Y, A
141	
142	
143	def gen_mbias_data(N, params, C0, rng):
144	    T, Y, A = _gen_mbias(N, params, rng)
145	    Astar = generate_Astar(A, C0, rng)
146	    return T, Y, A, Astar
147	
148	
149	def precomp_mbias(params, N=2_000_000, seed=999):
150	    rng = np.random.default_rng(seed)
151	    T, Y, A = _gen_mbias(N, params, rng)
152	    DA = np.zeros((N, K))
153	    for k in range(K):
154	        DA[:, k] = (A == k).astype(float)
155	    return dict(
156	        E_T=T.mean(), E_T2=(T**2).mean(),
157	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
158	        E_DA=DA.mean(0),
159	        E_DA_T=(DA * T[:, None]).mean(0),
160	        E_DA_Y=(DA * Y[:, None]).mean(0))
161	
162	
163	def plim_mbias(C, st):
164	    """OLS plim for Y ~ 1 + T + D1_A* + D2_A*."""
165	    ds  = C @ st['E_DA']
166	    dst = C @ st['E_DA_T']
167	    dsy = C @ st['E_DA_Y']
168	    ET, ET2 = st['E_T'], st['E_T2']
169	    EY, ETY = st['E_Y'], st['E_TY']
170	    EZZ = np.array([
171	        [1,      ET,      ds[1],    ds[2]   ],
172	        [ET,     ET2,     dst[1],   dst[2]  ],
173	        [ds[1],  dst[1],  ds[1],    0       ],
174	        [ds[2],  dst[2],  0,        ds[2]   ]])
175	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
176	    return np.linalg.solve(EZZ, EZY)
177	
178	
179	# ============================================================================
180	# Topology 2: IV — Z->A->Y, U->{A,Y}
181	# ============================================================================
182	
183	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
184	IV_BETA = np.array([0.0, 0.5, -0.25])
185	
186	
187	def _gen_iv(N, beta, params, rng):
188	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
189	    U = rng.normal(0, 1, N)
190	    eps = rng.normal(0, 1, N)
191	    logits = np.column_stack([
192	        np.zeros(N),
193	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
194	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
195	    ])
196	    A = softmax_sample(logits, rng)
197	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
198	         + params['lam'] * U + eps)
199	    return Z_iv, U, Y, A
200	
201	
202	def gen_iv_data(N, beta, params, C0, rng):
203	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
204	    Astar = generate_Astar(A, C0, rng)
205	    return Z_iv, Y, A, Astar
206	
207	
208	def precomp_iv(beta, params, N=2_000_000, seed=999):
209	    """Precompute reduced form and first stage for Wald estimator."""
210	    rng = np.random.default_rng(seed)
211	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
212	    z1 = Z_iv == 1; z0 = Z_iv == 0
213	    RF = Y[z1].mean() - Y[z0].mean()
214	    FS = np.zeros(K)
215	    for k in range(K):
216	        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
217	    return dict(RF=RF, FS=FS)
218	
219	
220	def plim_iv(C, st):
221	    """Wald estimator: RF / FS*_1 where FS* = C @ FS."""
222	    FS_star = C @ st['FS']
223	    if abs(FS_star[1]) < 1e-8:
224	        return np.nan
225	    return st['RF'] / FS_star[1]
226	
227	
228	def wald_with_se(Z, Y, Astar, k=1):
229	    """Finite-sample Wald estimator with delta-method SE."""
230	    z1 = Z == 1; z0 = Z == 0
231	    n1 = float(z1.sum()); n0 = float(z0.sum())
232	    if n1 < 2 or n0 < 2:
233	        return np.nan, np.nan
234	    RF = Y[z1].mean() - Y[z0].mean()
235	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
236	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
237	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
238	    FS = Dk_z1 - Dk_z0
239	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
240	    if abs(FS) < 1e-8:
241	        return np.nan, np.nan
242	    Wald = RF / FS
243	    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4
244	    SE = np.sqrt(max(var_Wald, 0))
245	    return Wald, SE
246	
247	
248	# ============================================================================
249	# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}
250	# ============================================================================
251	
252	ALPHA_U = 1.0
253	LAMBDA_U = 1.0
254	GAMMA_FD = np.array([0.0, 0.5, -0.3])
255	DELTA_FD = np.array([0.0, 1.0, -0.8])
256	BETA_FD = np.array([0.0, 1.0, -0.5])
257	
258	
259	def _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):
260	    if g is None: g = GAMMA_FD
261	    if d is None: d = DELTA_FD
262	    if aU is None: aU = ALPHA_U
263	    if lU is None: lU = LAMBDA_U
264	    U = rng.normal(0, 1, N)
265	    T = aU * U + rng.normal(0, 1, N)
266	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
267	    lo -= lo.max(1, keepdims=True)
268	    e = np.exp(lo)
269	    p = e / e.sum(1, keepdims=True)
270	    cu = np.cumsum(p, axis=1)
271	    u = rng.uniform(size=N)
272	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
273	    DM1 = (M == 1).astype(float)
274	    DM2 = (M == 2).astype(float)
275	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
276	    return T, M, Y, U
277	
278	
279	def gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):
280	    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
281	    Mstar = generate_Astar(M, C0, rng)
282	    return T, Y, M, Mstar
283	
284	
285	def precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):
286	    rng = np.random.default_rng(seed)
287	    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
288	    DM = np.zeros((N, K))
289	    for k in range(K):
290	        DM[:, k] = (M == k).astype(float)
291	    return dict(
292	        E_T=T.mean(), E_T2=(T**2).mean(),
293	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
294	        E_DM=DM.mean(0),
295	        E_DM_T=(DM * T[:, None]).mean(0),
296	        E_DM_Y=(DM * Y[:, None]).mean(0))
297	
298	
299	def plim_fd(C, st):
300	    """OLS plim for Y ~ 1 + T + D1_M* + D2_M*."""
301	    ds  = C @ st['E_DM']
302	    dst = C @ st['E_DM_T']
303	    dsy = C @ st['E_DM_Y']
304	    ET, ET2 = st['E_T'], st['E_T2']
305	    EY, ETY = st['E_Y'], st['E_TY']
306	    EZZ = np.array([
307	        [1,      ET,      ds[1],    ds[2]   ],
308	        [ET,     ET2,     dst[1],   dst[2]  ],
309	        [ds[1],  dst[1],  ds[1],    0       ],
310	        [ds[2],  dst[2],  0,        ds[2]   ]])
311	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
312	    return np.linalg.solve(EZZ, EZY)
313	
314	
315	# ============================================================================
316	# ASV Framework
317	# ============================================================================
318	
319	def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
320	    dmin, dmax = param.delta_range(C0)
321	    deltas = np.linspace(dmin, dmax, n_grid)
322	    tau_curve = np.zeros(n_grid)
323	    for i, d in enumerate(deltas):
324	        C_d = param(C0, d)
325	        if topology == "mbias":
326	            tau_curve[i] = plim_mbias(C_d, st)[1]
327	        elif topology == "iv":
328	            tau_curve[i] = plim_iv(C_d, st)
329	        elif topology == "frontdoor":
330	            tau_curve[i] = plim_fd(C_d, st)[1]
331	    bias_abs = np.abs(tau_curve - tau_true)
332	    return deltas, bias_abs, tau_curve
333	
334	
335	def compute_envelope(bias_abs):
336	    env = np.zeros_like(bias_abs)
337	    running_max = 0.0
338	    for i in range(len(bias_abs)):
339	        v = bias_abs[i]
340	        if not np.isnan(v):
341	            running_max = max(running_max, v)
342	        env[i] = running_max
343	    return env
344	
345	
346	def verify_envelope_monotonicity(envelope):
347	    diffs = np.diff(envelope)
348	    return int(np.sum(diffs < -1e-12))
349	
350	
351	def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
352	                         threshold_value=0.1, st=None, n_grid=1500):
353	    deltas, bias_abs, tau_curve = compute_bias_curve(
354	        topology, C0, param, tau_true, st, n_grid)
355	    envelope = compute_envelope(bias_abs)
356	
357	    valid_ba = bias_abs[~np.isnan(bias_abs)]
358	    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0
359	    env_violations = verify_envelope_monotonicity(envelope)
360	
361	    asv = None
362	    if threshold_type == "sign_flip":
363	        if abs(tau_true) < 1e-12:
364	            asv = None
365	        else:
366	            baseline_sign = np.sign(tau_true)
367	            for i, d in enumerate(deltas):
368	                if np.isnan(tau_curve[i]):
369	                    continue
370	                if np.sign(tau_curve[i]) != baseline_sign:
371	                    asv = d
372	                    break
373	    elif threshold_type == "magnitude_relative":
374	        if abs(tau_true) < 1e-12:
375	            asv = None
376	        else:
377	            thresh = threshold_value * abs(tau_true)
378	            for i, d in enumerate(deltas):
379	                if envelope[i] > thresh:
380	                    asv = d
381	                    break
382	    elif threshold_type == "magnitude_absolute":
383	        thresh = threshold_value
384	        for i, d in enumerate(deltas):
385	            if envelope[i] > thresh:
386	                asv = d
387	                break
388	
389	    return {
390	        "asv": asv,
391	        "raw_violations": raw_violations,
392	        "envelope_violations": env_violations,
393	        "deltas": deltas,
394	        "tau_curve": tau_curve,
395	        "envelope": envelope,
396	    }
397	
398	
399	def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
400	    if abs(tau_true) < 1e-12:
401	        return None
402	    thresh = rel_thresh * abs(tau_true)
403	    running_max = 0.0
404	    for i in range(len(deltas)):
405	        b = abs(tau_curve[i] - tau_true)
406	        if np.isnan(b):
407	            continue
408	        running_max = max(running_max, b)
409	        if running_max > thresh:
410	            return deltas[i]
411	    return None
412	
413	
414	# ============================================================================
415	# Part 1: Envelope Monotonicity
416	# ============================================================================
417	
418	def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
419	    print("\n" + "=" * 70)
420	    print("PART 1: Envelope Monotonicity (tau=0.5)")
421	    print("=" * 70)
422	    t0 = time.time()
423	    param = LinearInterpolation()
424	    C_list = normalize_C_list(make_C_list())
425	
426	    for topo, st, tau_true, label in [
427	        ("mbias", st_mb, 0.5, "M-bias"),
428	        ("iv", st_iv, 0.5, "IV"),
429	        ("frontdoor", st_fd, tau_fd, "Front-door"),
430	    ]:
431	        print(f"\n  {label} (tau_true={tau_true:.4f}):")
432	        for cname, C0 in C_list.items():
433	            r = compute_asv_envelope(topo, C0, tau_true, param,
434	                                     "magnitude_relative", 0.1, st=st)
435	            print(f"    {cname}: raw_violations={r['raw_violations']}/1500, "
436	                  f"envelope_violations={r['envelope_violations']}/1500")
437	    print(f"\n  Time: {time.time()-t0:.1f}s")
438	
439	
440	# ============================================================================
441	# Part 2: ASV Values (tau=0.5)
442	# ============================================================================
443	
444	def part2_asv_values(st_mb, st_iv, st_fd, tau_fd):
445	    print("\n" + "=" * 70)
446	    print("PART 2: ASV Values (tau=0.5)")
447	    print("=" * 70)
448	    t0 = time.time()
449	    param = LinearInterpolation()
450	    C_list = normalize_C_list(make_C_list())
451	    results = {}
452	
453	    print(f"\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}")
454	    print("  " + "-" * 45)
455	
456	    for topo, st, tau_true, label in [
457	        ("mbias", st_mb, 0.5, "M-bias"),
458	        ("iv", st_iv, 0.5, "IV"),
459	        ("frontdoor", st_fd, tau_fd, "Front-door"),
460	    ]:
461	        for cname, C0 in C_list.items():
462	            r_sf = compute_asv_envelope(topo, C0, tau_true, param,
463	                                        "sign_flip", st=st)
464	            r_mag = compute_asv_envelope(topo, C0, tau_true, param,
465	                                         "magnitude_relative", 0.1, st=st)
466	            sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
467	            mg_s = f"{r_mag['asv']:.3f}" if r_mag['asv'] is not None else "None"
468	            print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}")
469	            results[(label, cname)] = {
470	                "sign_flip": r_sf['asv'], "magnitude_10pct": r_mag['asv']}
471	    print(f"\n  Time: {time.time()-t0:.1f}s")
472	    return results
473	
474	
475	# ============================================================================
476	# Part 3: Small-tau ASV
477	# ============================================================================
478	
479	def part3_small_tau_asv():
480	    print("\n" + "=" * 70)
481	    print("PART 3: Small-tau ASV (tau=0.05, 0.1)")
482	    print("=" * 70)
483	    t0 = time.time()
484	    param = LinearInterpolation()
485	    C_list = normalize_C_list(make_C_list())
486	    results = {}
487	
488	    for tau_val in [0.05, 0.1]:
489	        print(f"\n  --- tau = {tau_val} ---")
490	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
491	        st_mb = precomp_mbias(mb_p, N=2_000_000)
492	        iv_b = np.array([0.0, tau_val, -tau_val/2])
493	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
494	        lU = tau_val * 2
495	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))
496	        tau_fd = plim_fd(np.eye(K), st_fd)[1]
497	        print(f"  Front-door tau_I = {tau_fd:.6f}")
498	
499	        hdr = f"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}"
500	        print(hdr)
501	        print("  " + "-" * 55)
502	
503	        for topo, st, tau_true, label in [
504	            ("mbias", st_mb, tau_val, "M-bias"),
505	            ("iv", st_iv, tau_val, "IV"),
506	            ("frontdoor", st_fd, tau_fd, "Front-door"),
507	        ]:
508	            for cname, C0 in C_list.items():
509	                r_sf = compute_asv_envelope(topo, C0, tau_true, param,
510	                                            "sign_flip", st=st)
511	                r_mg = compute_asv_envelope(topo, C0, tau_true, param,
512	                                            "magnitude_relative", 0.1, st=st)
513	                r_ab = compute_asv_envelope(topo, C0, tau_true, param,
514	                                            "magnitude_absolute", 0.05, st=st)
515	                sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
516	                mg_s = f"{r_mg['asv']:.3f}" if r_mg['asv'] is not None else "None"
517	                ab_s = f"{r_ab['asv']:.3f}" if r_ab['asv'] is not None else "None"
518	                print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}")
519	                results[(tau_val, label, cname)] = {
520	                    "sign_flip": r_sf['asv'],
521	                    "magnitude_10pct": r_mg['asv'],
522	                    "magnitude_abs05": r_ab['asv']}
523	    print(f"\n  Time: {time.time()-t0:.1f}s")
524	    return results
525	
526	
527	# ============================================================================
528	# Part 4: MC Coverage
529	# ============================================================================
530	
531	def part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):
532	    print("\n" + "=" * 70)
533	    print(f"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})")
534	    print("=" * 70)
535	    t0 = time.time()
536	    rng = np.random.default_rng(42)
537	    results = {}
538	
539	    for tau_val in [0.05, 0.1]:
540	        print(f"\n  --- tau = {tau_val} ---")
541	
542	        # --- M-bias ---
543	        print("  [M-bias]")
544	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
545	        st_mb = precomp_mbias(mb_p, N=2_000_000)
546	        plim_ok = 0; bias_ok = 0
547	        for s in range(n_scenarios):
548	            C0 = random_C0(K, rng)
549	            tau_plim = plim_mbias(C0, st_mb)[1]
550	            bias_theory = abs(tau_plim - tau_val)
551	            tau_mc = np.zeros(reps)
552	            for r in range(reps):
553	                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)
554	                bh, _ = ols_with_dummies(Yd, Td, Asd, K)
555	                tau_mc[r] = bh[1]
556	            mc_mean = tau_mc.mean()
557	            mc_se = tau_mc.std() / np.sqrt(reps)
558	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
559	                plim_ok += 1
560	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:
561	                bias_ok += 1
562	            if (s + 1) % 100 == 0:
563	                print(f"    ... {s+1}/{n_scenarios}")
564	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
565	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
566	        results[("mbias", tau_val)] = {
567	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
568	
569	        # --- IV ---
570	        print("  [IV]")
571	        iv_b = np.array([0.0, tau_val, -tau_val/2])
572	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
573	        plim_ok = 0; bias_ok = 0
574	        for s in range(n_scenarios):
575	            C0 = random_C0(K, rng)
576	            tau_plim = plim_iv(C0, st_iv)
577	            if np.isnan(tau_plim):
578	                plim_ok += 1; bias_ok += 1; continue
579	            bias_theory = abs(tau_plim - tau_val)
580	            tau_mc = np.zeros(reps)
581	            for r in range(reps):
582	                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)
583	                w, _ = wald_with_se(Zd, Yd, Asd)
584	                tau_mc[r] = w
585	            valid = ~np.isnan(tau_mc)
586	            if valid.sum() < reps * 0.5:
587	                plim_ok += 1; bias_ok += 1; continue
588	            mc_mean = tau_mc[valid].mean()
589	            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())
590	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:
591	                plim_ok += 1
592	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:
593	                bias_ok += 1
594	            if (s + 1) % 100 == 0:
595	                print(f"    ... {s+1}/{n_scenarios}")
596	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
597	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
598	        results[("iv", tau_val)] = {
599	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
600	
601	        # --- Front-door ---
602	        print("  [Front-door]")
603	        lU = tau_val * 2
604	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
605	                           seed=300+int(tau_val*100))
606	        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
607	        plim_ok = 0; bias_ok = 0
608	        for s in range(n_scenarios):
609	            C0 = random_C0(K, rng)
610	            tau_plim = plim_fd(C0, st_fd)[1]
611	            bias_theory = abs(tau_plim - tau_I_fd)
612	            tau_mc = np.zeros(reps)
613	            for r in range(reps):
614	                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)
615	                bh, _ = ols_with_dummies(Yd, Td, Msd, K)
616	                tau_mc[r] = bh[1]
617	            mc_mean = tau_mc.mean()
618	            mc_se = tau_mc.std() / np.sqrt(reps)
619	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
620	                plim_ok += 1
621	            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:
622	                bias_ok += 1
623	            if (s + 1) % 100 == 0:
624	                print(f"    ... {s+1}/{n_scenarios}")
625	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
626	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
627	        results[("frontdoor", tau_val)] = {
628	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
629	
630	    print(f"\n  Total time: {time.time()-t0:.1f}s")
631	    return results
632	
633	
634	# ============================================================================
635	# Part 5: Type I/II
636	# ============================================================================
637	
638	def part5_type_errors(n_mc=500, N_sample=5000):
639	    print("\n" + "=" * 70)
640	    print(f"PART 5: Type I/II ({n_mc} MC x N={N_sample})")
641	    print("  Decision: reject if |tau_hat/SE|>1.96 AND magnitude_ASV > 1")
642	    print("=" * 70)
643	    t0 = time.time()
644	    param = LinearInterpolation()
645	    C_list = normalize_C_list(make_C_list())
646	    results = {}
647	    seed_ctr = 3000
648	
649	    for tau_val in [0.05, 0.1]:
650	        print(f"\n  --- tau = {tau_val} ---")
651	        header = (f"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} "
652	                  f"{'mag_rej':>10} {'mean_masv':>10}")
653	
654	        # === M-bias ===
655	        print("\n  [M-bias]")
656	        print(header)
657	        print("  " + "-" * 52)
658	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
659	            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h
660	            st_h = precomp_mbias(mb_p, N=2_000_000)
661	            for cname, C0 in C_list.items():
662	                seed_ctr += 1
663	                dmin, dmax = param.delta_range(C0)
664	                deltas = np.linspace(dmin, dmax, 1500)
665	                tau_curve = np.array([
666	                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])
667	                rng_mc = np.random.default_rng(seed_ctr)
668	                naive_rej = 0; mag_rej = 0; masv_vals = []
669	                for mc in range(n_mc):
670	                    Td, Yd, _, Asd = gen_mbias_data(
671	                        N_sample, mb_p, C0, rng_mc)
672	                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)
673	                    tau_hat, se_tau = bh[1], seh[1]
674	                    reject = (abs(tau_hat / se_tau) > 1.96
675	                              if se_tau > 1e-10 else False)
676	                    if reject:
677	                        naive_rej += 1
678	                    masv = compute_magnitude_asv_fast(
679	                        tau_curve, deltas, tau_h, 0.1)
680	                    masv_vals.append(masv)
681	                    if reject and (masv is None or masv > 1.0):
682	                        mag_rej += 1
683	                mf = [a for a in masv_vals if a is not None]
684	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
685	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
686	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
687	                results[("mbias", tau_val, cname, h_label)] = {
688	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
689	
690	        # === IV ===
691	        print("\n  [IV]")
692	        print(header)
693	        print("  " + "-" * 52)
694	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
695	            iv_b = np.array([0.0, tau_h, -tau_h/2])
696	            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
697	            for cname, C0 in C_list.items():
698	                seed_ctr += 1
699	                dmin, dmax = param.delta_range(C0)
700	                deltas = np.linspace(dmin, dmax, 1500)
701	                tau_curve = np.array([
702	                    plim_iv(param(C0, d), st_h) for d in deltas])
703	                rng_mc = np.random.default_rng(seed_ctr)
704	                naive_rej = 0; mag_rej = 0; masv_vals = []
705	                for mc in range(n_mc):
706	                    Zd, Yd, _, Asd = gen_iv_data(
707	                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)
708	                    w, se_w = wald_with_se(Zd, Yd, Asd)
709	                    reject = False
710	                    if not np.isnan(w) and se_w > 1e-10:
711	                        reject = abs(w / se_w) > 1.96
712	                    if reject:
713	                        naive_rej += 1
714	                    masv = compute_magnitude_asv_fast(
715	                        tau_curve, deltas, tau_h, 0.1)
716	                    masv_vals.append(masv)
717	                    if reject and (masv is None or masv > 1.0):
718	                        mag_rej += 1
719	                mf = [a for a in masv_vals if a is not None]
720	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
721	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
722	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
723	                results[("iv", tau_val, cname, h_label)] = {
724	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
725	
726	        # === Front-door ===
727	        print("\n  [Front-door]")
728	        print(header)
729	        print("  " + "-" * 52)
730	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
731	            if h_label == "H0":
732	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
733	                                  d=np.zeros(3), seed=400)
734	                tau_ref = 0.0
735	            else:
736	                lU = tau_val * 2
737	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
738	                                  seed=401+int(tau_val*100))
739	                tau_ref = plim_fd(np.eye(K), st_h)[1]
740	            print(f"    ({h_label}: tau_ref={tau_ref:.4f})")
741	            for cname, C0 in C_list.items():
742	                seed_ctr += 1
743	                dmin, dmax = param.delta_range(C0)
744	                deltas = np.linspace(dmin, dmax, 1500)
745	                tau_curve = np.array([
746	                    plim_fd(param(C0, d), st_h)[1] for d in deltas])
747	                rng_mc = np.random.default_rng(seed_ctr)
748	                naive_rej = 0; mag_rej = 0; masv_vals = []
749	                for mc in range(n_mc):
750	                    if h_label == "H0":
751	                        Td, Yd, _, Msd = gen_fd_data(
752	                            N_sample, BETA_FD, C0, rng_mc,
753	                            lU=0.0, aU=0.0, d=np.zeros(3))
754	                    else:
755	                        Td, Yd, _, Msd = gen_fd_data(
756	                            N_sample, BETA_FD, C0, rng_mc, lU=lU)
757	                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)
758	                    tau_hat, se_tau = bh[1], seh[1]
759	                    reject = (abs(tau_hat / se_tau) > 1.96
760	                              if se_tau > 1e-10 else False)
761	                    if reject:
762	                        naive_rej += 1
763	                    masv = compute_magnitude_asv_fast(
764	                        tau_curve, deltas, tau_ref, 0.1)
765	                    masv_vals.append(masv)
766	                    if reject and (masv is None or masv > 1.0):
767	                        mag_rej += 1
768	                mf = [a for a in masv_vals if a is not None]
769	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
770	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
771	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
772	                results[("frontdoor", tau_val, cname, h_label)] = {
773	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
774	
775	    print(f"\n  Total time: {time.time()-t0:.1f}s")
776	    return results
777	
778	
779	# ============================================================================
780	# Part 6: Summary JSON
781	# ============================================================================
782	
783	def collect_summary(asv_res, small_tau_res, cov_res, te_res):
784	    def _f(v):
785	        if v is None:
786	            return None
787	        return float(v)
788	
789	    summary = {
790	        "experiment": "plan_005_asv_extended",
791	        "topologies": ["mbias", "iv", "frontdoor"],
792	        "asv_values_tau05": {},
793	        "small_tau_asv": {},
794	        "coverage": {},
795	        "type_errors": {},
796	    }
797	    for (label, cname), vals in asv_res.items():
798	        summary["asv_values_tau05"][f"{label}_{cname}"] = {
799	            k: _f(v) for k, v in vals.items()}
800	    for (tv, label, cname), vals in small_tau_res.items():
801	        summary["small_tau_asv"][f"tau{tv}_{label}_{cname}"] = {
802	            k: _f(v) for k, v in vals.items()}
803	    for (topo, tv), vals in cov_res.items():
804	        summary["coverage"][f"{topo}_tau{tv}"] = vals
805	    for key, vals in te_res.items():
806	        summary["type_errors"]["_".join(str(x) for x in key)] = vals
807	    return summary
808	
809	
810	# ============================================================================
811	# Main
812	# ============================================================================
813	
814	if __name__ == "__main__":
815	    np.set_printoptions(precision=6, suppress=True)
816	    print("plan_005: ASV Framework Extension to M-bias/IV/Front-door")
817	    print("=" * 70)
818	    t_total = time.time()
819	
820	    print("\nPrecomputing sufficient statistics (tau=0.5)...")
821	    t0 = time.time()
822	    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)
823	    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
824	    print(f"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}")
825	
826	    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)
827	    tau_I_iv = plim_iv(np.eye(K), st_iv)
828	    print(f"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}")
829	
830	    st_fd = precomp_fd(BETA_FD, N=10_000_000)
831	    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
832	    print(f"  Front-door: plim(I)={tau_I_fd:.6f}")
833	    print(f"  Done ({time.time()-t0:.1f}s)")
834	
835	    part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)
836	    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_fd)
837	    small_tau_res = part3_small_tau_asv()
838	    cov_res = part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100)
839	    te_res = part5_type_errors(n_mc=500, N_sample=5000)
840	
841	    print("\n" + "=" * 70)
842	    print("PART 6: Summary JSON")
843	    print("=" * 70)
844	    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)
845	    print(json.dumps(summary, indent=2, default=str))
846	
847	    print("\n" + "=" * 70)
848	    elapsed = time.time() - t_total
849	    print(f"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
850	    print("=" * 70)
851	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "05becd05-1232-4dbc-8669-9b1cd926e699"
}
```

</details>

---


### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Reading plan_004_asv_framework.py",
  "usage": {
    "total_tokens": 15915,
    "tool_uses": 4,
    "duration_ms": 2442
  },
  "last_tool_name": "Read",
  "uuid": "c8f732c9-895b-4022-b033-c172371e81c3",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_012yu7juCyXWcCDKoyp7xSgs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "336cf65b-97b4-4315-b1c1-8fab9f627801",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 20 · 2026-05-20T21:00:41.545Z_

<details><summary>↩ Tool result · reported error · `toolu_012yu7juCyXWcCDKoyp7xSgs`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "2f18da17-506d-427f-bd2b-ebf702102c14",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib."
}
```

</details>

---


### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Reading plan_002_k57_extension.py",
  "usage": {
    "total_tokens": 15918,
    "tool_uses": 5,
    "duration_ms": 2660
  },
  "last_tool_name": "Read",
  "uuid": "2a3cccb3-3538-40fc-a337-cdac7a6e2263",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01PP7wXHYYG8F9czyLxqk5jt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "18a0f93a-3248-44ca-88ec-2577f8bf0b2e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 23 · 2026-05-20T21:00:41.761Z_

<details><summary>↩ Tool result · `toolu_01PP7wXHYYG8F9czyLxqk5jt`</summary>

```text
1	#!/usr/bin/env python3
2	# -*- coding: utf-8 -*-
3	"""
4	Plan 002: K={3,5,7} Bias Taxonomy Extension
5	
6	Extends plan_001's K=3 bias analysis to general K across 4 core DAG topologies.
7	For each topology x K, generates 100k random K×K confusion matrices (Dirichlet),
8	computes plim via pre-computed sufficient statistics, and reports violation/sign-flip/
9	amplification rates. Includes eigendecomposition, worst-case bounds, and sensitivity
10	heatmaps as interpretability tools.
11	
12	Input:  DGP parameters per topology (auto-generated for each K)
13	Output: Cross-K comparison tables, sensitivity heatmaps (PNG)
14	
15	Dependencies: torch (GPU), numpy, matplotlib
16	"""
17	
18	import torch
19	import numpy as np
20	import matplotlib
21	matplotlib.use('Agg')
22	import matplotlib.pyplot as plt
23	import time
24	import os
25	import sys
26	
27	# ================================================================
28	# Configuration
29	# ================================================================
30	K_VALUES = [3, 5, 7]
31	N_RANDOM = 100_000
32	N_LARGE = 5_000_000
33	SEED = 42
34	DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
35	DTYPE = torch.float64
36	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
37	
38	
39	# ================================================================
40	# DGP Parameters for general K
41	# ================================================================
42	# Base coefficient pools — K=3 values match plan_001 exactly,
43	# K=5,7 extend with alternating-sign decreasing magnitudes.
44	_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
45	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
46	_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
47	_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
48	_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
49	_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
50	_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
51	
52	
53	def make_p_A(K):
54	    """Slightly imbalanced category probabilities."""
55	    if K == 3:
56	        return np.array([0.40, 0.35, 0.25])
57	    raw = np.array([1.0 / i for i in range(1, K + 1)])
58	    return raw / raw.sum()
59	
60	
61	def make_params(K):
62	    """DGP parameters for all topologies at given K."""
63	    p_A = make_p_A(K)
64	
65	    conf = dict(
66	        p_A=p_A,
67	        alpha=np.array(_ALPHA_POOL[:K-1]),
68	        beta_A=np.array(_BETA_A_POOL[:K-1]),
69	        beta_T=2.0,
70	        sigma_T=1.0,
71	    )
72	
73	    med = dict(
74	        tau=0.5,
75	        gamma=np.array(_GAMMA_POOL[:K]),
76	        delta=np.array(_DELTA_POOL[:K]),
77	        beta=np.array(_BETA_POOL[:K]),
78	    )
79	
80	    coll = dict(
81	        tau=1.0,
82	        g=np.zeros(K),
83	        dT=np.array(_DT_POOL[:K]),
84	        dY=np.array(_DY_POOL[:K]),
85	    )
86	
87	    exp = dict(
88	        beta=np.array(_BETA_POOL[:K]),
89	        p_A=p_A,
90	    )
91	
92	    return dict(confounding=conf, mediation=med, collider=coll, exposure=exp)
93	
94	
95	# ================================================================
96	# DGP Generators
97	# ================================================================
98	def _softmax_rows(logits):
99	    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
100	    return e / e.sum(axis=-1, keepdims=True)
101	
102	
103	def _sample_cat(probs, rng):
104	    """Sample from row-wise categorical probabilities [N, K]."""
105	    cum = np.cumsum(probs, axis=1)
106	    u = rng.uniform(size=probs.shape[0])[:, None]
107	    return (u >= cum).sum(axis=1).astype(int)
108	
109	
110	def gen_confounding(K, N, p, rng):
111	    """A→T, A→Y, T→Y. Researcher omits true A, uses A*."""
112	    A = rng.choice(K, size=N, p=p['p_A'])
113	    D = np.zeros((N, K - 1))
114	    for j in range(K - 1):
115	        D[:, j] = (A == j + 1).astype(float)
116	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
117	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
118	    return T, Y, A
119	
120	
121	def gen_mediation(K, N, p, rng):
122	    """T→A→Y. A mediates T's effect; researcher controls for A*."""
123	    T = rng.binomial(1, 0.5, N).astype(float)
124	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
125	    probs = _softmax_rows(logits)
126	    A = _sample_cat(probs, rng)
127	    D = np.zeros((N, K - 1))
128	    for j in range(K - 1):
129	        D[:, j] = (A == j + 1).astype(float)
130	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
131	    return T, Y, A
132	
133	
134	def gen_collider(K, N, p, rng):
135	    """T→A←Y. Controlling for collider A* opens a backdoor path."""
136	    T = rng.normal(0, 1, N)
137	    Y = p['tau'] * T + rng.normal(0, 1, N)
138	    logits = (p['g'][None, :]
139	              + p['dT'][None, :] * T[:, None]
140	              + p['dY'][None, :] * Y[:, None])
141	    probs = _softmax_rows(logits)
142	    A = _sample_cat(probs, rng)
143	    return T, Y, A
144	
145	
146	def gen_exposure(K, N, p, rng):
147	    """A→Y. A is the treatment of interest."""
148	    A = rng.choice(K, size=N, p=p['p_A'])
149	    D = np.zeros((N, K - 1))
150	    for j in range(K - 1):
151	        D[:, j] = (A == j + 1).astype(float)
152	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
153	    return None, Y, A
154	
155	
156	_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
157	            collider=gen_collider, exposure=gen_exposure)
158	
159	
160	# ================================================================
161	# Sufficient Statistics
162	# ================================================================
163	class SuffStats:
164	    """Pre-compute population moments from a large DGP sample.
165	
166	    Stores:
167	      p_A[k]   = P(A=k)
168	      E_Y      = E[Y]
169	      E_YD[k]  = E[Y · 1(A=k)]
170	    For topologies with T:
171	      E_T, E_T2, E_TY, E_TD[k] = E[T · 1(A=k)]
172	    """
173	
174	    def __init__(self, T, Y, A, K):
175	        self.K = K
176	        self.has_T = T is not None
177	
178	        self.p_A = np.array([(A == k).mean() for k in range(K)])
179	        self.E_Y = Y.mean()
180	        self.E_YD = np.array([(Y * (A == k)).mean() for k in range(K)])
181	
182	        if self.has_T:
183	            self.E_T = T.mean()
184	            self.E_T2 = (T ** 2).mean()
185	            self.E_TY = (T * Y).mean()
186	            self.E_TD = np.array([(T * (A == k)).mean() for k in range(K)])
187	
188	    def to_device(self, dev):
189	        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)
190	        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)
191	        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)
192	        if self.has_T:
193	            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)
194	            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)
195	            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)
196	            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)
197	        return self
198	
199	
200	# ================================================================
201	# GPU-Batched Plim
202	# ================================================================
203	def plim_with_T(ss, C):
204	    """Batched plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.
205	
206	    Generalizes K=3 plan_001 formula. Z* = (1, T, D*_1,...,D*_{K-1}).
207	    plim = (E[Z*'Z*])^{-1} E[Z*'Y].
208	
209	    E[Z*'Z*] and E[Z*'Y] depend on C through:
210	      q = C @ p_A              (marginal of A*)
211	      E[T·D*_j] = (C @ E_TD)[j]
212	      E[Y·D*_j] = (C @ E_YD)[j]
213	      E[D*_i·D*_j] = q[i] δ_{ij}  (A* is categorical)
214	
215	    Args:
216	        ss: SuffStats on device
217	        C:  [B, K, K] confusion matrices
218	    Returns:
219	        [B, K+1] plim coefficients
220	    """
221	    B, K = C.shape[0], ss.K
222	    dim = K + 1
223	
224	    q = C @ ss.t_p_A                   # [B, K]
225	    ct = C @ ss.t_E_TD                 # [B, K]
226	    cy = C @ ss.t_E_YD                 # [B, K]
227	
228	    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
229	    EZZ[:, 0, 0] = 1.0
230	    EZZ[:, 0, 1] = ss.t_E_T
231	    EZZ[:, 1, 0] = ss.t_E_T
232	    EZZ[:, 1, 1] = ss.t_E_T2
233	    EZZ[:, 0, 2:] = q[:, 1:]
234	    EZZ[:, 2:, 0] = q[:, 1:]
235	    EZZ[:, 1, 2:] = ct[:, 1:]
236	    EZZ[:, 2:, 1] = ct[:, 1:]
237	    idx = torch.arange(K - 1, device=C.device)
238	    EZZ[:, idx + 2, idx + 2] = q[:, 1:]
239	
240	    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
241	    EZY[:, 0] = ss.t_E_Y
242	    EZY[:, 1] = ss.t_E_TY
243	    EZY[:, 2:] = cy[:, 1:]
244	
245	    return torch.linalg.solve(EZZ, EZY)
246	
247	
248	def plim_exposure(ss, C):
249	    """Batched plim for Y ~ 1 + D*_1 + ... + D*_{K-1} (no T).
250	
251	    Same moment algebra as plim_with_T but without the T row/column.
252	    """
253	    B, K = C.shape[0], ss.K
254	    dim = K
255	
256	    q = C @ ss.t_p_A
257	    cy = C @ ss.t_E_YD
258	
259	    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
260	    EZZ[:, 0, 0] = 1.0
261	    EZZ[:, 0, 1:] = q[:, 1:]
262	    EZZ[:, 1:, 0] = q[:, 1:]
263	    idx = torch.arange(K - 1, device=C.device)
264	    EZZ[:, idx + 1, idx + 1] = q[:, 1:]
265	
266	    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
267	    EZY[:, 0] = ss.t_E_Y
268	    EZY[:, 1:] = cy[:, 1:]
269	
270	    return torch.linalg.solve(EZZ, EZY)
271	
272	
273	# ================================================================
274	# Random C Generation
275	# ================================================================
276	def gen_random_C(K, N, device, seed=SEED, min_diag=None):
277	    """Sample N column-stochastic K×K matrices via Dirichlet(1,...,1).
278	
279	    Each column independently drawn. If min_diag is set, each diagonal
280	    element is drawn from U[min_diag, 1] and the remaining mass is
281	    distributed Dirichlet among off-diagonal entries.
282	    """
283	    rng = np.random.default_rng(seed)
284	    C = np.zeros((N, K, K))
285	
286	    if min_diag is not None and min_diag > 0:
287	        for j in range(K):
288	            diag = rng.uniform(min_diag, 1.0, N)
289	            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]
290	            col = np.zeros((N, K))
291	            col[:, j] = diag
292	            idx = 0
293	            for i in range(K):
294	                if i != j:
295	                    col[:, i] = offdiag[:, idx]
296	                    idx += 1
297	            C[:, :, j] = col
298	    else:
299	        for j in range(K):
300	            C[:, :, j] = rng.dirichlet(np.ones(K), N)
301	
302	    return torch.tensor(C, dtype=DTYPE, device=device)
303	
304	
305	# ================================================================
306	# Metrics
307	# ================================================================
308	def compute_metrics(plim_batch, plim_true, tau_idx=None):
309	    """Violation / sign-flip / amplification rates.
310	
311	    tau_idx: index of τ coefficient (1 for topologies with T, None for exposure).
312	    """
313	    diff = plim_batch - plim_true.unsqueeze(0)
314	
315	    violation = (diff.abs() > 1e-8).any(dim=1).float().mean().item()
316	
317	    s0 = torch.sign(plim_true).unsqueeze(0)
318	    s1 = torch.sign(plim_batch)
319	    sign_flip = ((s0 != s1) & (s0 != 0) & (s1 != 0)).any(dim=1).float().mean().item()
320	
321	    amplification = (plim_batch.abs() > plim_true.abs().unsqueeze(0) + 1e-10
322	                     ).any(dim=1).float().mean().item()
323	
324	    m = dict(violation=violation, sign_flip=sign_flip, amplification=amplification)
325	
326	    if tau_idx is not None:
327	        tb = plim_batch[:, tau_idx]
328	        tt = plim_true[tau_idx]
329	        td = tb - tt
330	        m['tau_violation'] = (td.abs() > 1e-8).float().mean().item()
331	        m['tau_sign_flip'] = ((torch.sign(tb) != torch.sign(tt)) &
332	                              (torch.sign(tt) != 0) &
333	                              (torch.sign(tb) != 0)).float().mean().item()
334	        m['tau_amplification'] = (tb.abs() > tt.abs() + 1e-10).float().mean().item()
335	        m['tau_bias_mean'] = td.mean().item()
336	        m['tau_bias_std'] = td.std().item()
337	        m['tau_bias_max'] = td.abs().max().item()
338	    return m
339	
340	
341	# ================================================================
342	# MC Verification (small-scale, a few named C matrices)
343	# ================================================================
344	def mc_verify(K, topo, params, C_np, n_reps=500, n_mc=10_000, seed=0):
345	    """Monte Carlo OLS estimate of plim for a single C, as validation."""
346	    gen_fn = _GEN[topo]
347	    coefs = []
348	    for r in range(n_reps):
349	        rng = np.random.default_rng(seed + r)
350	        T, Y, A = gen_fn(K, n_mc, params, rng)
351	
352	        # Misclassify
353	        probs = C_np[:, A]       # [K, N]
354	        cum = np.cumsum(probs, axis=0)
355	        u = rng.uniform(size=n_mc)
356	        Astar = np.zeros(n_mc, dtype=int)
357	        for k in range(K - 1):
358	            Astar += (u >= cum[k]).astype(int)
359	
360	        Dstar = np.zeros((n_mc, K - 1))
361	        for j in range(K - 1):
362	            Dstar[:, j] = (Astar == j + 1).astype(float)
363	
364	        ones = np.ones((n_mc, 1))
365	        if T is not None:
366	            Z = np.hstack([ones, T[:, None], Dstar])
367	        else:
368	            Z = np.hstack([ones, Dstar])
369	        b = np.linalg.lstsq(Z, Y, rcond=None)[0]
370	        coefs.append(b)
371	    return np.mean(coefs, axis=0), np.std(coefs, axis=0) / np.sqrt(n_reps)
372	
373	
374	# ================================================================
375	# Interpretability (a): Eigendecomposition of bias vectors
376	# ================================================================
377	def eigen_analysis(plim_batch, plim_true):
378	    """PCA on bias = plim(C) - plim(I). Returns top-3 variance ratios.
379	
380	    The bias vectors live in R^{K+1} (or R^K for exposure).
381	    Eigendecomposition of bias covariance identifies which linear
382	    combinations of coefficients carry most of the bias variance.
383	    """
384	    bias = (plim_batch - plim_true.unsqueeze(0)).cpu().numpy()
385	    bias_c = bias - bias.mean(axis=0)
386	    _, S, Vt = np.linalg.svd(bias_c, full_matrices=False)
387	    var = S ** 2
388	    ratios = var / var.sum()
389	    return ratios[:min(3, len(ratios))]
390	
391	
392	# ================================================================
393	# Interpretability (b): Worst-case bounds under diagonal constraint
394	# ================================================================
395	def worst_case_bounds(ss, plim_fn, K, device, thresholds=(0.5, 0.7, 0.9)):
396	    """max|τ̂ − τ_true| over column-stochastic C with min diag(C) ≥ thr.
397	
398	    For each threshold, sample 50k constrained C matrices and report
399	    the maximum, mean, and 95th-percentile |bias|.
400	    """
401	    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
402	    plim_I = plim_fn(ss, I_batch).squeeze(0)
403	    has_T = plim_I.shape[0] > K
404	    idx = 1 if has_T else 1
405	
406	    results = {}
407	    for thr in thresholds:
408	        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)
409	        pb = plim_fn(ss, Cb)
410	        valid = torch.isfinite(pb).all(dim=1)
411	        pb = pb[valid]
412	        if has_T:
413	            bias = (pb[:, idx] - plim_I[idx]).abs()
414	        else:
415	            bias = (pb[:, 1:] - plim_I[1:].unsqueeze(0)).abs().max(dim=1).values
416	        results[thr] = dict(
417	            max_bias=bias.max().item(),
418	            mean_bias=bias.mean().item(),
419	            p95_bias=torch.quantile(bias, 0.95).item(),
420	        )
421	    return results
422	
423	
424	# ================================================================
425	# Interpretability (c): Sensitivity heatmap via finite differences
426	# ================================================================
427	def sensitivity_heatmap(ss, plim_fn, K, device, out_path, topo_name):
428	    """∂|bias(τ)|/∂C_ij evaluated at C = I via finite differences.
429	
430	    For off-diagonal (i,j): perturb C[i,j] += δ and C[j,j] -= δ to keep
431	    column j stochastic. Measures which misclassification patterns most
432	    affect the τ estimate.
433	    """
434	    delta = 0.01
435	    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
436	    plim_I = plim_fn(ss, I_batch).squeeze(0)
437	    has_T = plim_I.shape[0] > K
438	    tau_idx = 1 if has_T else 1
439	    tau_I = plim_I[tau_idx].item()
440	
441	    sens = np.zeros((K, K))
442	    for i in range(K):
443	        for j in range(K):
444	            if i == j:
445	                continue
446	            C = torch.eye(K, dtype=DTYPE, device=device)
447	            C[i, j] += delta
448	            C[j, j] -= delta
449	            p = plim_fn(ss, C.unsqueeze(0)).squeeze(0)
450	            sens[i, j] = abs(p[tau_idx].item() - tau_I) / delta
451	
452	    fig, ax = plt.subplots(figsize=(max(3.5, K * 0.7), max(3.5, K * 0.7)))
453	    im = ax.imshow(sens, cmap='YlOrRd', aspect='equal')
454	    ax.set_xlabel('True category j')
455	    ax.set_ylabel('Observed category i')
456	    ax.set_title(f'{topo_name} K={K}: |∂bias(τ)/∂C_ij|')
457	    ax.set_xticks(range(K))
458	    ax.set_yticks(range(K))
459	    for i in range(K):
460	        for j in range(K):
461	            color = 'w' if sens[i, j] > sens.max() * 0.6 else 'k'
462	            ax.text(j, i, f'{sens[i,j]:.3f}', ha='center', va='center',
463	                    fontsize=max(5, 8 - K), color=color)
464	    plt.colorbar(im, ax=ax, shrink=0.8)
465	    fig.tight_layout()
466	    fig.savefig(out_path, dpi=150, bbox_inches='tight')
467	    plt.close(fig)
468	    return sens
469	
470	
471	# ================================================================
472	# Main
473	# ================================================================
474	def main():
475	    t0 = time.time()
476	    print("=" * 90)
477	    print("  Plan 002: K={3,5,7} Bias Taxonomy Extension")
478	    print("=" * 90)
479	    print(f"Device: {DEVICE}")
480	    if torch.cuda.is_available():
481	        gp = torch.cuda.get_device_properties(0)
482	        print(f"GPU: {gp.name}  ({gp.total_memory / 1024**3:.1f} GB)")
483	    print(f"N_RANDOM={N_RANDOM:,}  N_LARGE={N_LARGE:,}")
484	
485	    topologies = ['confounding', 'mediation', 'collider', 'exposure']
486	    all_results = {}
487	
488	    # ------------------------------------------------------------------
489	    # Named C matrices for MC verification (K=3 only, matching plan_001)
490	    # ------------------------------------------------------------------
491	    C_named_3 = {
492	        'sym_high': np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]]),
493	        'weak_diag': np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]]),
494	    }
495	
496	    for topo in topologies:
497	        print(f"\n{'=' * 90}")
498	        print(f"  TOPOLOGY: {topo.upper()}")
499	        print(f"{'=' * 90}")
500	
501	        plim_fn = plim_exposure if topo == 'exposure' else plim_with_T
502	        tau_idx = None if topo == 'exposure' else 1
503	
504	        for K in K_VALUES:
505	            print(f"\n  --- K={K} ---")
506	            tk = time.time()
507	
508	            params = make_params(K)
509	            p = params[topo]
510	            rng = np.random.default_rng(SEED)
511	
512	            # 1. Large DGP → sufficient statistics
513	            T, Y, A = _GEN[topo](K, N_LARGE, p, rng)
514	            ss = SuffStats(T, Y, A, K).to_device(DEVICE)
515	            print(f"  p_A = {ss.p_A}")
516	            if ss.has_T:
517	                print(f"  E[T]={ss.E_T:.4f}  E[T²]={ss.E_T2:.4f}  E[TY]={ss.E_TY:.4f}")
518	
519	            # 2. plim(I) = τ_true
520	            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
521	            plim_true = plim_fn(ss, I_batch).squeeze(0)
522	            print(f"  plim(I) = {plim_true.cpu().numpy()}")
523	
524	            # 3. MC verification for K=3
525	            if K == 3:
526	                print(f"\n  MC Verification (K=3, 500 reps × 10k samples):")
527	                for cn, Cnp in C_named_3.items():
528	                    Ct = torch.tensor(Cnp, dtype=DTYPE, device=DEVICE).unsqueeze(0)
529	                    th = plim_fn(ss, Ct).squeeze(0).cpu().numpy()
530	                    mc, se = mc_verify(K, topo, p, Cnp)
531	                    match = np.abs(th - mc) < 2.5 * se
532	                    tag = ''.join('✓' if m else '✗' for m in match)
533	                    print(f"    {cn:<10}  theory={th}  MC={mc}  {tag}")
534	
535	            # 4. Random C search
536	            C_batch = gen_random_C(K, N_RANDOM, DEVICE)
537	            plim_all = plim_fn(ss, C_batch)
538	
539	            valid = torch.isfinite(plim_all).all(dim=1)
540	            n_valid = valid.sum().item()
541	            if n_valid < N_RANDOM:
542	                print(f"  WARNING: {N_RANDOM - n_valid} singular, using {n_valid}")
543	                plim_all = plim_all[valid]
544	
545	            metrics = compute_metrics(plim_all, plim_true, tau_idx=tau_idx)
546	            key = f"{topo}_K{K}"
547	            all_results[key] = metrics
548	
549	            print(f"\n  Overall: violation={metrics['violation']:.1%}  "
550	                  f"sign_flip={metrics['sign_flip']:.1%}  "
551	                  f"amplification={metrics['amplification']:.1%}")
552	            if tau_idx is not None:
553	                print(f"  τ-specific: violation={metrics['tau_violation']:.1%}  "
554	                      f"sign_flip={metrics['tau_sign_flip']:.1%}  "
555	                      f"amplification={metrics['tau_amplification']:.1%}")
556	                print(f"  τ bias: mean={metrics['tau_bias_mean']:+.6f}  "
557	                      f"std={metrics['tau_bias_std']:.6f}  "
558	                      f"max={metrics['tau_bias_max']:.6f}")
559	
560	            # 5. Eigendecomposition
561	            top3 = eigen_analysis(plim_all, plim_true)
562	            print(f"  Eigen top-{len(top3)} var explained: "
563	                  + '  '.join(f'{v:.1%}' for v in top3))
564	
565	            # 6. Worst-case bounds
566	            wc = worst_case_bounds(ss, plim_fn, K, DEVICE)
567	            for thr, v in wc.items():
568	                print(f"  Worst-case (diag≥{thr}): "
569	                      f"max|Δτ|={v['max_bias']:.6f}  "
570	                      f"mean={v['mean_bias']:.6f}  "
571	                      f"P95={v['p95_bias']:.6f}")
572	
573	            # 7. Sensitivity heatmap
574	            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
575	            sensitivity_heatmap(ss, plim_fn, K, DEVICE, hm_path, topo)
576	            print(f"  Heatmap → {os.path.basename(hm_path)}")
577	
578	            print(f"  [{time.time() - tk:.1f}s]")
579	
580	    # ==================================================================
581	    # Cross-K Summary
582	    # ==================================================================
583	    print(f"\n{'=' * 90}")
584	    print("  CROSS-K COMPARISON")
585	    print(f"{'=' * 90}")
586	
587	    hdr = (f"  {'Topology':<14} {'K':>3}"
588	           f" {'violat':>8} {'sflip':>8} {'amplif':>8}"
589	           f" {'τ_viol':>8} {'τ_sflip':>8} {'τ_amp':>8}")
590	    print(hdr)
591	    print(f"  {'-' * 73}")
592	
593	    for topo in topologies:
594	        for K in K_VALUES:
595	            m = all_results[f"{topo}_K{K}"]
596	            tv = m.get('tau_violation', None)
597	            ts = m.get('tau_sign_flip', None)
598	            ta = m.get('tau_amplification', None)
599	            tvs = f"{tv:.1%}" if tv is not None else "  —"
600	            tss = f"{ts:.1%}" if ts is not None else "  —"
601	            tas = f"{ta:.1%}" if ta is not None else "  —"
602	            print(f"  {topo:<14} {K:>3}"
603	                  f" {m['violation']:>8.1%} {m['sign_flip']:>8.1%}"
604	                  f" {m['amplification']:>8.1%}"
605	                  f" {tvs:>8} {tss:>8} {tas:>8}")
606	        print()
607	
608	    # Trend analysis
609	    print("  K-TREND ANALYSIS (does bias worsen with K?)")
610	    for topo in topologies:
611	        if topo == 'exposure':
612	            vals = [all_results[f"{topo}_K{K}"]['violation'] for K in K_VALUES]
613	            label = 'violation'
614	        else:
615	            vals = [all_results[f"{topo}_K{K}"]['tau_violation'] for K in K_VALUES]
616	            label = 'τ_violation'
617	        d = vals[-1] - vals[0]
618	        trend = "WORSENS" if d > 0.01 else ("STABLE" if abs(d) <= 0.01 else "IMPROVES")
619	        print(f"  {topo:<14} ({label}): "
620	              f"K=3 {vals[0]:.1%} → K=5 {vals[1]:.1%} → K=7 {vals[2]:.1%}  [{trend}]")
621	
622	    # ==================================================================
623	    # Combined sensitivity figure (K=5 and K=7 side by side per topology)
624	    # ==================================================================
625	    fig, axes = plt.subplots(len(topologies), 2, figsize=(12, 4 * len(topologies)))
626	    for row, topo in enumerate(topologies):
627	        for col, K in enumerate([5, 7]):
628	            ax = axes[row, col]
629	            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
630	            if os.path.exists(hm_path):
631	                img = plt.imread(hm_path)
632	                ax.imshow(img)
633	                ax.axis('off')
634	                ax.set_title(f'{topo} K={K}', fontsize=10)
635	            else:
636	                ax.text(0.5, 0.5, 'N/A', ha='center', va='center', transform=ax.transAxes)
637	                ax.set_title(f'{topo} K={K}', fontsize=10)
638	    fig.suptitle('Sensitivity Heatmaps: |∂bias(τ)/∂C_ij|', fontsize=13)
639	    fig.tight_layout(rect=[0, 0, 1, 0.97])
640	    combined_path = os.path.join(OUT_DIR, 'plan002_sensitivity_combined.png')
641	    fig.savefig(combined_path, dpi=150, bbox_inches='tight')
642	    plt.close(fig)
643	    print(f"\n  Combined heatmap → {os.path.basename(combined_path)}")
644	
645	    print(f"\nTotal: {time.time() - t0:.0f}s")
646	
647	
648	if __name__ == "__main__":
649	    main()
650	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "702da1e2-08cb-46a3-888b-a2438215eb3c"
}
```

</details>

---


### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 15921,
    "tool_uses": 6,
    "duration_ms": 2740
  },
  "last_tool_name": "Read",
  "uuid": "51281808-e6a0-4b6f-9f70-2d38e6ee1604",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01VV3Fgz1NV3uurvmxCS3s1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "921a2481-c30e-49f0-8586-2265e541fe78",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 26 · 2026-05-20T21:00:41.840Z_

<details><summary>↩ Tool result · `toolu_01VV3Fgz1NV3uurvmxCS3s1J`</summary>

```text
1	# Project Memory
2	
3	## MVP 验证发现 (2026-05-20)
4	
5	### Exposure DAG: bias-toward-null 保证在 K=3 下失效（核心发现）
6	**100k 随机 C 搜索：85% 违反 bias-toward-null，83.4% 产生符号反转。** 二分类 K=2 下全部满足 toward null 保证。
7	
8	具体 named structure 结果：
9	- C3_STRUCTURAL_12: β_2=-0.5 → γ̂_2=+0.06（符号反转）
10	- C4_WEAK_DIAG: β_1=1.0 → γ̂_1≈0（近消失）
11	- C5_NEAR_PERM: β_2=-0.5 → γ̂_2=+1.25（符号反转 + 2.5x 放大，最极端）
12	
13	**关键洞察**：exposure 误分类场景下，多分类 C 矩阵的交叉污染使得回归将某类的 Y 值归因到错误标签，产生符号反转。
14	
15	### Dirichlet 子空间分析：高精度 LLM 仍有显著违反
16	即使 min(diag(C))≥0.9，amplification 违反率仍达 11.9%。符号反转随精度提高消失，但 amplification 稳定在 ~12%。
17	
18	### Confounding DAG: 偏差方向性质
19	100k 随机 C 搜索均未发现负偏差。K=3 误分类偏差始终与 OVB 同向。
20	
21	### DGP 参数
22	- Confounding DAG: P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma=1.0
23	- Exposure DAG: P(A)=[0.4, 0.35, 0.25], beta=[0, 1.0, -0.5], sigma_Y=1.0
24	
25	## plan_001 完整 Taxonomy 结果 (2026-05-20)
26	
27	### 结构性保证：τ sign_flip = 0% 跨所有拓扑和所有 τ 大小
28	**这是论文 Claim 1 的核心 positive result**。K=3 非差异性误分类改变 treatment effect 幅度但不翻转方向。小 τ (0.05, 0.1) 确认是结构性的。Exposure DAG 是唯一例外（83.4% sign reversal）。
29	
30	### 拓扑行为分层
31	- **Mediation/Front-door**: violation ≈100%, amplification ≈100%, misclass_amplifies ≈100% — 最受影响
32	- **Collider**: misclass_amplifies = 0% — 误分类减弱 collider bias（独特）
33	- **M-bias**: violation 53.2%, amplification 10.4% — 最鲁棒
34	- **Exposure**: sign_flip 83.4% — 唯一翻转拓扑（C 直接作用于 design matrix）
35	
36	## plan_002 K=5,7 扩展结果 (2026-05-20)
37	
38	### Sign_flip 随 K 恶化（核心发现）
39	**K 增大引入更多错分模式，符号反转概率系统性上升**：
40	- Mediation: 83.8%(K=3) → 96.6%(K=5) → **100%(K=7)**
41	- Collider: 66.6%(K=3) → 95.5%(K=5) → **99.2%(K=7)**
42	- Confounding/Exposure: K=3 已近饱和，K=5,7 达 100%
43	
44	### 但 worst-case bound 和 bias 均值反而下降（除 exposure）
45	**反直觉的 nuance**：高精度约束(diag≥0.9)下，K 增大每个 off-diagonal 元素分摊更小 → confounding worst-case 从 0.162(K=3) 降至 0.092(K=7)。**唯一例外是 exposure**（0.253→0.282），因为 exposure 的 bias 来自 design matrix 的交叉污染，不受对角占优约束的同样保护。
46	
47	### Eigendecomposition：bias 方差随 K 分散
48	Top-1 PC 解释 bias 方差的比例：78%(K=3) → 67%(K=5) → 61%(K=7)。K 增大后 bias 不再集中在单一方向，增加了诊断和校正难度。
49	
50	### 对论文 story 的影响
51	Claim 1 证据链完整：plan_001(K=3 taxonomy) + plan_002(K scaling) + plan_008(binarization collapse)。可 claim "K 增大使符号反转风险恶化，practitioners 处理高 K 分类任务时风险更大"。
52	
53	## plan_008 Binarization Collapse 结果 (2026-05-20)
54	
55	### 拓扑依赖性：折叠偏差跨度 150 倍
56	IV (Δ_mean=0.926) > Exposure (0.516) >> Mediation (0.045) > Confounding (0.025) > Collider (0.017) > M-bias (0.006)。Sign flip 只在 IV (17.5%) 和 Exposure (14.0%)。plan_001 和 plan_008 的拓扑危险性排序一致。
57	
58	## plan_004 ASV 框架结果 (2026-05-20)
59	
60	### v2 发现 + v3 修正
61	v2 问题：(1) 单调性 75% 违反 (2) sign-flip ASV 对 confounding/mediation 返回 None
62	
63	v3 修正（D007 + Director magnitude 阈值修正）：
64	- **Envelope monotonicity**: violations = 0（构造性保证）
65	- **Magnitude ASV (10% relative threshold)**: 对所有拓扑有信息
66	  - τ=0.5: 0.076–0.487（部分 C₀ 下安全）
67	  - τ=0.1: 0.014–0.093（不安全）
68	  - τ=0.05: 0.008–0.047（极不安全）
69	- **关键洞察**：小 τ ASV << 1 = LLM 标注误差对小效应因果推断不安全 → 连接 Claim 3 correction 需求
70	- **Type I/II (小 τ)**: ASV-informed 正确保守（H₁ 下 0% 拒绝，因为 ASV<1 → 标记不安全）
71	
72	### ASV 三类定义（最终版）
73	1. **Sign-flip ASV**: min δ 使 sign 翻转（Exposure 专用，其他拓扑 = None）
74	2. **Magnitude ASV**: min δ 使 |bias| > 0.1×|τ̂|（通用，所有拓扑有信息）
75	3. **Significance ASV**: min δ 使 |plim τ̂(C(δ))| < 1.96×SE（假设检验 filter）
76	
77	## plan_005 ASV 扩展结果 (2026-05-20, fixed)
78	
79	### 6 拓扑 ASV 全覆盖（Reviewer CRITICAL 修复后）
80	修复 4 点：C1 significance ASV 函数 + C2 magnitude τ≈0→0.0 + W1 IV τ_true=plim(I)=0.6598 + W2 M-bias τ_true=plim(I)=0.5128
81	
82	### τ_true 必须用 plim(I) 而非 DGP 参数
83	**设计决策**：ASV 衡量 annotation error **额外引入**的 bias，不含估计量固有的多类别污染。因此 τ_true = plim(C=I)，不是 DGP 直接参数。IV plim(I)=0.6598≠β₁=0.5；M-bias plim(I)=0.5128≠τ=0.5。Front-door 已正确。
84	
85	### Significance filter Type I/II（修复后）
86	| 拓扑 | Type I | Power τ=0.05 | Power τ=0.1 |
87	|------|--------|-------------|-------------|
88	| M-bias | 0% | 95.8-99.2% | 100% |
89	| IV | 0% | 0% | 0% |
90	| Front-door | 0% | 100% | 100% |
91	
92	- **IV power=0% 是正确的**：Wald 估计量极脆弱，signif_ASV≈0（annotation error 立即摧毁 significance），ASV filter 保守阻止所有拒绝。对 IV，应改用 magnitude ASV 报告脆弱性
93	- **M-bias 高 power**：误分类减弱 spurious bias，不影响真实效应的检测
94	- 与 plan_004 confounding/mediation/collider 结果合并 → 6 拓扑 significance filter 完整验证
95	
96	## plan_007 Correction Guidance 结果 (2026-05-20)
97	
98	### PPI++ 全面碾压（Claim 3 核心支撑）
99	Grand mean: bias_red 93.8%, coverage 96.8%, win rate 95.2% (40/42 scenarios)。唯一满足名义 95% coverage 的方法。
100	
101	### Frisch-Waugh 不变性：理论到实证完全验证
102	naive_plugin 和 MLA 在 OLS 拓扑（confounding/mediation/collider/mbias）下 bias_red 精确 0.0%。原因：C⁻¹ 变换 dummy matrix 不改变 [intercept, D*] 的列空间，T 系数 OLS 估计不变。
103	但在 exposure/iv/frontdoor 下两者显著恶化（-40% ~ -113%），因为这些拓扑的估计量不是简单 OLS on T → FWL 不适用。
104	
105	### DSL 拓扑敏感性（新发现，可作为 contribution）
106	DSL 仅在 confounding (49.8%) 和 mediation (70.3%) 有效——这两种拓扑 misclassification error 主要通过 dummy 系数传播，DSL 的 EM 迭代能捕获。其余 5 拓扑系统性失败，最差 mbias -768%。**失败原因是结构性的，非个别 C 问题。**
107	
108	### PPI++ 的阿喀琉斯之踵
109	mbias + realistic_llm: bias_red = -25.1%（恶化），但 coverage 99%。说明 PPI 的置信区间正确反映了增大的不确定性，bias 校正本身失效。论文应诚实报告此弱点。
110	
111	### MC-SIMEX 不稳定
112	Grand mean 20.9%，在 iv (64.7%) 尚可但 frontdoor (-55.7%) 崩溃。不适合作为通用推荐。
113	
114	## plan_009 Pathological Matrices 结果 (2026-05-20)
115	
116	### 3 风险层级
117	- **Low risk**: mbias (mean_bias 0.006-0.039)
118	- **Medium risk**: confounding/mediation/collider/frontdoor (R²=0.70-0.77, condition_number 最一致预测因子)
119	- **High risk**: exposure/IV (不可预测，R²低)
120	
121	### IV 过滤问题
122	3000/28000 (10.7%) non-finite Wald estimates 被静默排除。regression 仅基于 89.3% 的样本。
123	
124	## Director 决策记录 (2026-05-20)
125	
126	### 数据集决策（最终确认）
127	- HumAID (K=10), VAST (K=3), Civil Comments (K=2)
128	- 数据位置：`/home/sonny/causal_annot_error_attrib/data/`
129	
130	### API 模型决策
131	- Llama 4 Maverick, Qwen 3 235B, DeepSeek Chat V3
132	- API endpoint: `http://47.94.22.126/v1`，全部用 OPENROUTER_API_KEY
133	
134	### home-1x5090 服务器
135	- account: sonny, Python 3.10.12, Ubuntu 22.04
136	- 项目目录 `/home/sonny/causal_annot_error_attrib/`
137	
138	### ASV 框架决策 (D005-D008)
139	- D005: C(δ) 参数化选定方案 A 线性插值
140	- D006: 区分 Vulnerability/Protection 双方向 ASV
141	- D007: Envelope monotonicity 替代 raw monotonicity
142	- D008: ASV 阈值从 sign-flip 改为 magnitude-based（0.1×|τ̂|），sign-flip ASV 保留给 Exposure
143	
144	### Lee & Wood-Doughty (2024) 技术区分
145	本项目：observed exposure/confounder with noisy LLM annotation。LWD：unobserved confounding with proxy。关键区别：我们的 C 可从 validation data 估计。
146	
147	## ASV C(δ) 参数化调研 (2026-05-20)
148	
149	### 关键文献
150	- VanderWeele & Ding (2017): E-value 框架——单标量参数化 + 单调 + 可解释
151	- VanderWeele & Li (2019): 测量误差灵敏度分析——Se/Sp ratio 参数化
152	- Lash, Fox & Fink (2009): QBA 框架——(Se, Sp) 对参数化
153	- Brenner (1993): 多分类混杂误分类偏差方向可反转
154	
155	### 与 E-value 的对应
156	方案 A 在 K=2 时精确退化到 VanderWeele & Li (2019) 框架。
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5b1982d2-f809-4651-b05c-416e5d9f74e3"
}
```

</details>

---


### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2e40a43448a018a4",
  "tool_use_id": "toolu_01Xdq4NgC5tevfUpdE3UyVh8",
  "status": "completed",
  "output_file": "",
  "summary": "Read existing plan scripts",
  "usage": {
    "total_tokens": 63834,
    "tool_uses": 6,
    "duration_ms": 45481
  },
  "uuid": "4d6f9474-1eff-47a1-bbe6-43f28a1be9c5",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### Tool result

_source line 28 · 2026-05-20T21:01:24.578Z_

<details><summary>↩ Tool result · `toolu_01Xdq4NgC5tevfUpdE3UyVh8`</summary>

````text
Perfect! I've successfully read all the requested files. Let me provide you with a comprehensive report of the critical information you need.

## COMPREHENSIVE FILE REPORT

### FILE 1: plan_001_collider_mbias_iv.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py`

**PLIM BIAS COMPUTATION FUNCTIONS:**

1. **Collider (T → A ← Y):**
   - `theory_collider(C, params, N_approx, seed)`: Large-sample approximation using 2M samples
   - Returns `(tau_ctrl, tau_nc)` - OLS estimate with and without controlling for A*
   - DGP: `Y = tau*T + eps`, `A|T,Y ~ softmax(...)`
   - Regression: `Y ~ 1 + T + D1 + D2` where D1, D2 are dummy variables for A*
   
2. **M-bias (U1→{A,T}, U2→{A,Y}):**
   - `theory_mbias(C, params, N_approx, seed)`: Similar large-sample approach
   - DGP: `T = delta*U1 + eta`, `Y = tau*T + lam*U2 + eps`
   - Computes plim via OLS with control for misclassified A*
   
3. **Instrument (Z→A→Y, U→{A,Y}):**
   - `theory_iv(C, beta, params, N_approx, seed)`: Computes Wald estimators
   - Returns dict with: `RF`, `FS1_star`, `FS2_star`, `FS1_true`, `FS2_true`, `Wald1_star`, `Wald2_star`, `ols_star`, `ols_true`
   - First stage: `FS*_k = (Astar[Z=1]==k).mean() - (Astar[Z=0]==k).mean()`

**CONFUSION MATRIX USAGE:**
- C is K×K (here K=3): confusion matrix where `C[i,j] = P(A*=i | A=j)`
- Generation via `_generate_Astar(A, C, rng)`: Sample from categorical using column probabilities
- Example matrices: C1_SYMMETRIC_HIGH (0.80 diag), C2_ASYMMETRIC, C3_STRUCTURAL_12, etc.

**NAMED C MATRICES:**
```python
C1_SYMMETRIC_HIGH = [[.80, .10, .10], [.10, .80, .10], [.10, .10, .80]]
C2_ASYMMETRIC = [[.65, .05, .10], [.30, .85, .10], [.05, .10, .80]]
C3_STRUCTURAL_12 = [[.96, .01, .01], [.02, .69, .30], [.02, .30, .69]]
C4_WEAK_DIAG = [[.40, .35, .25], [.35, .40, .35], [.25, .25, .40]]
C5_NEAR_PERM = [[.05, .05, .90], [.90, .05, .05], [.05, .90, .05]]
C6_DIFF_BASE = [[.80, .10, .10], [.10, .80, .10], [.10, .10, .80]]
```

**DGP PARAMETER CONVENTIONS:**
- `COLLIDER_PARAMS = {tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6}`
- `MBIAS_PARAMS = {tau=1.0, delta=1.0, lam=1.0, g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9}`
- `IV_PARAMS = {lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6}`
- `BETA_MIXED = [0.0, 1.0, -0.5]`, `BETA_SAME = [0.0, 1.0, 0.5]`

---

### FILE 2: plan_001_mediation_frontdoor.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py`

**PLIM BIAS COMPUTATION - CLOSED FORM:**

1. **Mediation (T → A → Y):**
   - `plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED)`: Closed-form plim computation
   - Key moments: `p0 = softmax(g + d*0)`, `p1 = softmax(g + d*1)`
   - Transformed: `q0 = C @ p0`, `q1 = C @ p1` (P(A*|T))
   - Constructs EZZ, EZX matrices explicitly:
     ```python
     EZZ[0,0] = 1, EZZ[0,1] = 0.5, EZZ[0,2:] = qm[1:]
     EZZ[1,1] = 0.5, EZZ[1,2:] = 0.5*q1[1:]
     EZZ[2:,2:] = diag(qm[1:])
     ```
   - Returns: `np.linalg.solve(EZZ, EZX @ b)`

2. **Front-door (T → M → Y, U → {T,Y}):**
   - `plim_fd(C, st)`: Uses pre-computed sufficient statistics dict
   - Requires: `E_T, E_T2, E_Y, E_TY, E_DM[k], E_DM_T[k], E_DM_Y[k]`
   - Transforms: `E_D* = C @ E_D`, then constructs 4×4 EZZ and EZY

**SUFFICIENT STATISTICS COMPUTATION:**
- `precomp_fd(beta, N=50M, seed=123)`: Generates DGP, computes population moments
- For mediation: uses direct conditional probabilities `softmax(gamma + delta*T)`
- Returns dict of means: `E_T, E_T2, E_Y, E_TY, E_DM, E_DM_T, E_DM_Y`

**DGP PARAMETERS:**
```python
TAU = 0.5
GAMMA_MED = [0.0, 0.5, -0.3]
DELTA_MED = [0.0, 0.8, -0.6]
ALPHA_U = 1.0
LAMBDA_U = 1.0
GAMMA_FD = [0.0, 0.5, -0.3]
DELTA_FD = [0.0, 1.0, -0.8]
BETA_MIXED = [0.0, 1.0, -0.5]
BETA_SAME = [0.0, 1.0, 0.5]
```

**C DICTIONARY (6 matrices):**
```python
C_DICT = {
    "1_sym_high":   [[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]],
    "2_asymmetric": [[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]],
    "3_struct_12":  [[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]],
    "4_weak_diag":  [[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]],
    "5_near_perm":  [[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]],
    "6_diff_base":  [[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]],
}
```

---

### FILE 3: plan_005_asv_extended.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py`

**ASV FRAMEWORK IMPLEMENTATION:**

1. **ASV COMPUTATION FUNCTIONS:**

   - `compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500)`:
     - Generates delta range, computes tau curve via C(delta) parameterization
     - Returns: `(deltas, bias_abs, tau_curve)` where `bias_abs = |tau_curve - tau_true|`

   - `compute_envelope(bias_abs)`: Computes envelope via running maximum
     - Returns monotone upper bound on absolute bias

   - `compute_asv_envelope(topology, C0, tau_true, param, threshold_type, threshold_value, st, n_grid)`:
     - Supports three threshold types:
       1. **"sign_flip"**: First delta where sign changes (if tau_true ≠ 0)
       2. **"magnitude_relative"**: First delta where envelope > 0.1×|tau_true|
       3. **"magnitude_absolute"**: First delta where envelope > threshold_value
     - Returns dict with `asv`, violations counts, deltas, tau_curve, envelope

   - `compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1)`:
     - Returns first delta where running max bias exceeds threshold

2. **C(delta) PARAMETERIZATION (LinearInterpolation):**
   - `C(delta) = (1-delta)*I + delta*C0` normalized by column sums
   - `delta_range(C0)`: Returns (0, delta_max) where delta_max depends on diag(C0)
   - If min_diag ≥ 1: max_delta = 10
   - Else: max_delta = min(1/(1-min_diag), 10)

3. **TOPOLOGIES STRUCTURE:**

   **M-bias:**
   - `MBIAS_PARAMS = {tau=0.5, delta=1.0, lam=1.0, g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9}`
   - `precomp_mbias(params, N=2M, seed=999)`: Returns sufficient stats dict
   - `plim_mbias(C, st)`: OLS plim for Y ~ 1 + T + D1_A* + D2_A*

   **IV:**
   - `IV_PARAMS = {lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6}`
   - `IV_BETA = [0.0, 0.5, -0.25]`
   - `precomp_iv(beta, params, N=2M, seed=999)`: RF and FS
   - `plim_iv(C, st)`: Wald estimator RF/FS*_1

   **Front-door:**
   - `ALPHA_U=1.0, LAMBDA_U=1.0, BETA_FD=[0.0, 1.0, -0.5]`
   - `GAMMA_FD = [0.0, 0.5, -0.3], DELTA_FD = [0.0, 1.0, -0.8]`
   - `precomp_fd(beta, N=10M, seed=123, lU=None, aU=None, d=None)`: Sufficient stats
   - `plim_fd(C, st)`: OLS plim for Y ~ 1 + T + D1_M* + D2_M*

4. **C MATRIX LIST (6 matrices):**
   ```python
   def make_C_list():
       return {
           "C1_sym": [[0.80, 0.10, 0.10], ...],
           "C2_high": [[0.90, 0.05, 0.05], ...],
           "C3_asym": [[0.70, 0.20, 0.10], ...],
           "C4_weak": [[0.60, 0.20, 0.20], ...],
           "C5_perm": [[0.40, 0.30, 0.30], ...],
           "C6_diff": [[0.85, 0.075, 0.075], ...],
       }
   ```

5. **FIVE ANALYSIS PARTS:**
   - Part 1: Envelope monotonicity verification (0 violations expected)
   - Part 2: ASV values (sign_flip, magnitude_relative 10%)
   - Part 3: Small-tau ASV (tau=0.05, 0.1)
   - Part 4: MC coverage (500 scenarios, 100 reps each)
   - Part 5: Type I/II errors with significance filter

---

### FILE 4: plan_002_k57_extension.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py`

**GENERAL K PARAMETERIZATION:**

1. **DGP PARAMETER GENERATION FOR K={3,5,7}:**
   ```python
   K_VALUES = [3, 5, 7]
   _ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]  # For alpha
   _BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]  # For beta_A
   _GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
   _DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
   ```

   - `make_params(K)`: Generates all topology parameters for given K
   - Parameters for each topology: confounding, mediation, collider, exposure

2. **SUFFICIENT STATISTICS CLASS:**
   ```python
   class SuffStats:
       def __init__(self, T, Y, A, K):
           self.p_A = P(A=k) for each k
           self.E_Y, self.E_YD[k]  # Marginal Y and Y given category k
           if has_T:
               self.E_T, self.E_T2, self.E_TY, self.E_TD[k]
   ```

3. **PLIM COMPUTATION (GPU-BATCHED):**
   - `plim_with_T(ss, C)`: For topologies with treatment T
     - Constructs EZZ, EZY matrices in batched form
     - Returns `torch.linalg.solve(EZZ, EZY)` - shape [B, K+1]
   - `plim_exposure(ss, C)`: For pure exposure outcome (no T)
     - Similar but dimension is K, not K+1

4. **CONFUSION MATRIX GENERATION:**
   - `gen_random_C(K, N, device, seed, min_diag=None)`: Sample N column-stochastic K×K matrices
   - Uses Dirichlet(1,...,1) per column
   - Optional constraint: min_diag specifies minimum diagonal elements

5. **METRICS COMPUTATION:**
   - `compute_metrics(plim_batch, plim_true, tau_idx)`:
     - violation: Any coefficient changes
     - sign_flip: Any non-zero coefficient flips sign
     - amplification: Any |coef| > |coef_true|
     - tau-specific versions if tau_idx provided

---

### FILE 5: plan_002_k57_extension.py (NOT plan_004)
**Note:** plan_004_asv_framework.py does NOT exist. plan_002_k57_extension.py was file 5.

---

### FILE 6: memory.md
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md`

**KEY FINDINGS:**

1. **Exposure DAG Paradox (MVP Finding):**
   - 85% violate bias-toward-null with K=3
   - 83.4% sign flip rate
   - K=2 maintains toward-null guarantee

2. **Sign-flip Worsening with K:**
   - Mediation: 83.8%(K=3) → 96.6%(K=5) → 100%(K=7)
   - Collider: 66.6%(K=3) → 95.5%(K=5) → 99.2%(K=7)

3. **Topology Risk Hierarchy:**
   - Low risk: M-bias
   - Medium risk: confounding/mediation/collider/front-door
   - High risk: exposure/IV

4. **ASV Definition (Final v3):**
   1. Sign-flip ASV: min δ where sign flips
   2. Magnitude ASV: min δ where |bias| > 0.1×|τ̂|
   3. Significance ASV: min δ where |τ̂| < 1.96×SE

5. **Plan 005 Significance Filter Results:**
   - M-bias: Type I=0%, Power(τ=0.05)=95.8-99.2%
   - IV: Type I=0%, Power=0% (Wald estimator too fragile)
   - Front-door: Type I=0%, Power(τ=0.05)=100%

6. **Plan 007 Correction (Claim 3):**
   - PPI++ grand mean: 93.8% bias reduction, 96.8% coverage, 95.2% win rate
   - Only method achieving nominal 95% coverage
   - Naive plugin: 0% bias reduction (Frisch-Waugh invariance for OLS)

---

## SUMMARY TABLE: KEY FUNCTIONS

| File | Topology | Plim Function | Parameters | C Matrix |
|------|----------|---------------|-----------|----------|
| plan_001_collider_mbias_iv.py | Collider | `theory_collider` | COLLIDER_PARAMS | C1-C6 |
| plan_001_collider_mbias_iv.py | M-bias | `theory_mbias` | MBIAS_PARAMS | C1-C6 |
| plan_001_collider_mbias_iv.py | IV | `theory_iv` | IV_PARAMS, BETA_MIXED/SAME | C1-C6 |
| plan_001_mediation_frontdoor.py | Mediation | `plim_med` | GAMMA_MED, DELTA_MED, TAU | C_DICT (6) |
| plan_001_mediation_frontdoor.py | Front-door | `plim_fd` | ALPHA_U, LAMBDA_U, GAMMA_FD, DELTA_FD | C_DICT (6) |
| plan_005_asv_extended.py | M-bias/IV/FD | `compute_asv_envelope` | Per-topology | C1-C6 |
| plan_002_k57_extension.py | All 4 | `plim_with_T`/`plim_exposure` | Generated per K | Random Dirichlet |

This comprehensive report captures all the critical implementation details, parameter conventions, and ASV framework specifications across all files.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "1cc8c1e3-c100-415a-87bf-d734e54b8c7e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files in the current working directory and report their full contents (or as much as possible):\n\n1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py\n2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py\n3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py\n4. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py (if it exists)\n5. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py (if it exists)\n6. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md\n\nReport the full content of each file. I need to understand:\n- The plim bias computation functions for each topology\n- The ASV computation functions (magnitude, significance, sign_flip)\n- DGP parameter conventions\n- How confusion matrices are constructed and used\n- The topologies list and their parameter structures\n\nBe very thorough - read each file completely.",
    "agentId": "a2e40a43448a018a4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've successfully read all the requested files. Let me provide you with a comprehensive report of the critical information you need.\n\n## COMPREHENSIVE FILE REPORT\n\n### FILE 1: plan_001_collider_mbias_iv.py\n**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py`\n\n**PLIM BIAS COMPUTATION FUNCTIONS:**\n\n1. **Collider (T → A ← Y):**\n   - `theory_collider(C, params, N_approx, seed)`: Large-sample approximation using 2M samples\n   - Returns `(tau_ctrl, tau_nc)` - OLS estimate with and without controlling for A*\n   - DGP: `Y = tau*T + eps`, `A|T,Y ~ softmax(...)`\n   - Regression: `Y ~ 1 + T + D1 + D2` where D1, D2 are dummy variables for A*\n   \n2. **M-bias (U1→{A,T}, U2→{A,Y}):**\n   - `theory_mbias(C, params, N_approx, seed)`: Similar large-sample approach\n   - DGP: `T = delta*U1 + eta`, `Y = tau*T + lam*U2 + eps`\n   - Computes plim via OLS with control for misclassified A*\n   \n3. **Instrument (Z→A→Y, U→{A,Y}):**\n   - `theory_iv(C, beta, params, N_approx, seed)`: Computes Wald estimators\n   - Returns dict with: `RF`, `FS1_star`, `FS2_star`, `FS1_true`, `FS2_true`, `Wald1_star`, `Wald2_star`, `ols_star`, `ols_true`\n   - First stage: `FS*_k = (Astar[Z=1]==k).mean() - (Astar[Z=0]==k).mean()`\n\n**CONFUSION MATRIX USAGE:**\n- C is K×K (here K=3): confusion matrix where `C[i,j] = P(A*=i | A=j)`\n- Generation via `_generate_Astar(A, C, rng)`: Sample from categorical using column probabilities\n- Example matrices: C1_SYMMETRIC_HIGH (0.80 diag), C2_ASYMMETRIC, C3_STRUCTURAL_12, etc.\n\n**NAMED C MATRICES:**\n```python\nC1_SYMMETRIC_HIGH = [[.80, .10, .10], [.10, .80, .10], [.10, .10, .80]]\nC2_ASYMMETRIC = [[.65, .05, .10], [.30, .85, .10], [.05, .10, .80]]\nC3_STRUCTURAL_12 = [[.96, .01, .01], [.02, .69, .30], [.02, .30, .69]]\nC4_WEAK_DIAG = [[.40, .35, .25], [.35, .40, .35], [.25, .25, .40]]\nC5_NEAR_PERM = [[.05, .05, .90], [.90, .05, .05], [.05, .90, .05]]\nC6_DIFF_BASE = [[.80, .10, .10], [.10, .80, .10], [.10, .10, .80]]\n```\n\n**DGP PARAMETER CONVENTIONS:**\n- `COLLIDER_PARAMS = {tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6}`\n- `MBIAS_PARAMS = {tau=1.0, delta=1.0, lam=1.0, g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9}`\n- `IV_PARAMS = {lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6}`\n- `BETA_MIXED = [0.0, 1.0, -0.5]`, `BETA_SAME = [0.0, 1.0, 0.5]`\n\n---\n\n### FILE 2: plan_001_mediation_frontdoor.py\n**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py`\n\n**PLIM BIAS COMPUTATION - CLOSED FORM:**\n\n1. **Mediation (T → A → Y):**\n   - `plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED)`: Closed-form plim computation\n   - Key moments: `p0 = softmax(g + d*0)`, `p1 = softmax(g + d*1)`\n   - Transformed: `q0 = C @ p0`, `q1 = C @ p1` (P(A*|T))\n   - Constructs EZZ, EZX matrices explicitly:\n     ```python\n     EZZ[0,0] = 1, EZZ[0,1] = 0.5, EZZ[0,2:] = qm[1:]\n     EZZ[1,1] = 0.5, EZZ[1,2:] = 0.5*q1[1:]\n     EZZ[2:,2:] = diag(qm[1:])\n     ```\n   - Returns: `np.linalg.solve(EZZ, EZX @ b)`\n\n2. **Front-door (T → M → Y, U → {T,Y}):**\n   - `plim_fd(C, st)`: Uses pre-computed sufficient statistics dict\n   - Requires: `E_T, E_T2, E_Y, E_TY, E_DM[k], E_DM_T[k], E_DM_Y[k]`\n   - Transforms: `E_D* = C @ E_D`, then constructs 4×4 EZZ and EZY\n\n**SUFFICIENT STATISTICS COMPUTATION:**\n- `precomp_fd(beta, N=50M, seed=123)`: Generates DGP, computes population moments\n- For mediation: uses direct conditional probabilities `softmax(gamma + delta*T)`\n- Returns dict of means: `E_T, E_T2, E_Y, E_TY, E_DM, E_DM_T, E_DM_Y`\n\n**DGP PARAMETERS:**\n```python\nTAU = 0.5\nGAMMA_MED = [0.0, 0.5, -0.3]\nDELTA_MED = [0.0, 0.8, -0.6]\nALPHA_U = 1.0\nLAMBDA_U = 1.0\nGAMMA_FD = [0.0, 0.5, -0.3]\nDELTA_FD = [0.0, 1.0, -0.8]\nBETA_MIXED = [0.0, 1.0, -0.5]\nBETA_SAME = [0.0, 1.0, 0.5]\n```\n\n**C DICTIONARY (6 matrices):**\n```python\nC_DICT = {\n    \"1_sym_high\":   [[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]],\n    \"2_asymmetric\": [[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]],\n    \"3_struct_12\":  [[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]],\n    \"4_weak_diag\":  [[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]],\n    \"5_near_perm\":  [[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]],\n    \"6_diff_base\":  [[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]],\n}\n```\n\n---\n\n### FILE 3: plan_005_asv_extended.py\n**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py`\n\n**ASV FRAMEWORK IMPLEMENTATION:**\n\n1. **ASV COMPUTATION FUNCTIONS:**\n\n   - `compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500)`:\n     - Generates delta range, computes tau curve via C(delta) parameterization\n     - Returns: `(deltas, bias_abs, tau_curve)` where `bias_abs = |tau_curve - tau_true|`\n\n   - `compute_envelope(bias_abs)`: Computes envelope via running maximum\n     - Returns monotone upper bound on absolute bias\n\n   - `compute_asv_envelope(topology, C0, tau_true, param, threshold_type, threshold_value, st, n_grid)`:\n     - Supports three threshold types:\n       1. **\"sign_flip\"**: First delta where sign changes (if tau_true ≠ 0)\n       2. **\"magnitude_relative\"**: First delta where envelope > 0.1×|tau_true|\n       3. **\"magnitude_absolute\"**: First delta where envelope > threshold_value\n     - Returns dict with `asv`, violations counts, deltas, tau_curve, envelope\n\n   - `compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1)`:\n     - Returns first delta where running max bias exceeds threshold\n\n2. **C(delta) PARAMETERIZATION (LinearInterpolation):**\n   - `C(delta) = (1-delta)*I + delta*C0` normalized by column sums\n   - `delta_range(C0)`: Returns (0, delta_max) where delta_max depends on diag(C0)\n   - If min_diag ≥ 1: max_delta = 10\n   - Else: max_delta = min(1/(1-min_diag), 10)\n\n3. **TOPOLOGIES STRUCTURE:**\n\n   **M-bias:**\n   - `MBIAS_PARAMS = {tau=0.5, delta=1.0, lam=1.0, g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9}`\n   - `precomp_mbias(params, N=2M, seed=999)`: Returns sufficient stats dict\n   - `plim_mbias(C, st)`: OLS plim for Y ~ 1 + T + D1_A* + D2_A*\n\n   **IV:**\n   - `IV_PARAMS = {lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6}`\n   - `IV_BETA = [0.0, 0.5, -0.25]`\n   - `precomp_iv(beta, params, N=2M, seed=999)`: RF and FS\n   - `plim_iv(C, st)`: Wald estimator RF/FS*_1\n\n   **Front-door:**\n   - `ALPHA_U=1.0, LAMBDA_U=1.0, BETA_FD=[0.0, 1.0, -0.5]`\n   - `GAMMA_FD = [0.0, 0.5, -0.3], DELTA_FD = [0.0, 1.0, -0.8]`\n   - `precomp_fd(beta, N=10M, seed=123, lU=None, aU=None, d=None)`: Sufficient stats\n   - `plim_fd(C, st)`: OLS plim for Y ~ 1 + T + D1_M* + D2_M*\n\n4. **C MATRIX LIST (6 matrices):**\n   ```python\n   def make_C_list():\n       return {\n           \"C1_sym\": [[0.80, 0.10, 0.10], ...],\n           \"C2_high\": [[0.90, 0.05, 0.05], ...],\n           \"C3_asym\": [[0.70, 0.20, 0.10], ...],\n           \"C4_weak\": [[0.60, 0.20, 0.20], ...],\n           \"C5_perm\": [[0.40, 0.30, 0.30], ...],\n           \"C6_diff\": [[0.85, 0.075, 0.075], ...],\n       }\n   ```\n\n5. **FIVE ANALYSIS PARTS:**\n   - Part 1: Envelope monotonicity verification (0 violations expected)\n   - Part 2: ASV values (sign_flip, magnitude_relative 10%)\n   - Part 3: Small-tau ASV (tau=0.05, 0.1)\n   - Part 4: MC coverage (500 scenarios, 100 reps each)\n   - Part 5: Type I/II errors with significance filter\n\n---\n\n### FILE 4: plan_002_k57_extension.py\n**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py`\n\n**GENERAL K PARAMETERIZATION:**\n\n1. **DGP PARAMETER GENERATION FOR K={3,5,7}:**\n   ```python\n   K_VALUES = [3, 5, 7]\n   _ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]  # For alpha\n   _BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]  # For beta_A\n   _GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n   _DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n   ```\n\n   - `make_params(K)`: Generates all topology parameters for given K\n   - Parameters for each topology: confounding, mediation, collider, exposure\n\n2. **SUFFICIENT STATISTICS CLASS:**\n   ```python\n   class SuffStats:\n       def __init__(self, T, Y, A, K):\n           self.p_A = P(A=k) for each k\n           self.E_Y, self.E_YD[k]  # Marginal Y and Y given category k\n           if has_T:\n               self.E_T, self.E_T2, self.E_TY, self.E_TD[k]\n   ```\n\n3. **PLIM COMPUTATION (GPU-BATCHED):**\n   - `plim_with_T(ss, C)`: For topologies with treatment T\n     - Constructs EZZ, EZY matrices in batched form\n     - Returns `torch.linalg.solve(EZZ, EZY)` - shape [B, K+1]\n   - `plim_exposure(ss, C)`: For pure exposure outcome (no T)\n     - Similar but dimension is K, not K+1\n\n4. **CONFUSION MATRIX GENERATION:**\n   - `gen_random_C(K, N, device, seed, min_diag=None)`: Sample N column-stochastic K×K matrices\n   - Uses Dirichlet(1,...,1) per column\n   - Optional constraint: min_diag specifies minimum diagonal elements\n\n5. **METRICS COMPUTATION:**\n   - `compute_metrics(plim_batch, plim_true, tau_idx)`:\n     - violation: Any coefficient changes\n     - sign_flip: Any non-zero coefficient flips sign\n     - amplification: Any |coef| > |coef_true|\n     - tau-specific versions if tau_idx provided\n\n---\n\n### FILE 5: plan_002_k57_extension.py (NOT plan_004)\n**Note:** plan_004_asv_framework.py does NOT exist. plan_002_k57_extension.py was file 5.\n\n---\n\n### FILE 6: memory.md\n**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md`\n\n**KEY FINDINGS:**\n\n1. **Exposure DAG Paradox (MVP Finding):**\n   - 85% violate bias-toward-null with K=3\n   - 83.4% sign flip rate\n   - K=2 maintains toward-null guarantee\n\n2. **Sign-flip Worsening with K:**\n   - Mediation: 83.8%(K=3) → 96.6%(K=5) → 100%(K=7)\n   - Collider: 66.6%(K=3) → 95.5%(K=5) → 99.2%(K=7)\n\n3. **Topology Risk Hierarchy:**\n   - Low risk: M-bias\n   - Medium risk: confounding/mediation/collider/front-door\n   - High risk: exposure/IV\n\n4. **ASV Definition (Final v3):**\n   1. Sign-flip ASV: min δ where sign flips\n   2. Magnitude ASV: min δ where |bias| > 0.1×|τ̂|\n   3. Significance ASV: min δ where |τ̂| < 1.96×SE\n\n5. **Plan 005 Significance Filter Results:**\n   - M-bias: Type I=0%, Power(τ=0.05)=95.8-99.2%\n   - IV: Type I=0%, Power=0% (Wald estimator too fragile)\n   - Front-door: Type I=0%, Power(τ=0.05)=100%\n\n6. **Plan 007 Correction (Claim 3):**\n   - PPI++ grand mean: 93.8% bias reduction, 96.8% coverage, 95.2% win rate\n   - Only method achieving nominal 95% coverage\n   - Naive plugin: 0% bias reduction (Frisch-Waugh invariance for OLS)\n\n---\n\n## SUMMARY TABLE: KEY FUNCTIONS\n\n| File | Topology | Plim Function | Parameters | C Matrix |\n|------|----------|---------------|-----------|----------|\n| plan_001_collider_mbias_iv.py | Collider | `theory_collider` | COLLIDER_PARAMS | C1-C6 |\n| plan_001_collider_mbias_iv.py | M-bias | `theory_mbias` | MBIAS_PARAMS | C1-C6 |\n| plan_001_collider_mbias_iv.py | IV | `theory_iv` | IV_PARAMS, BETA_MIXED/SAME | C1-C6 |\n| plan_001_mediation_frontdoor.py | Mediation | `plim_med` | GAMMA_MED, DELTA_MED, TAU | C_DICT (6) |\n| plan_001_mediation_frontdoor.py | Front-door | `plim_fd` | ALPHA_U, LAMBDA_U, GAMMA_FD, DELTA_FD | C_DICT (6) |\n| plan_005_asv_extended.py | M-bias/IV/FD | `compute_asv_envelope` | Per-topology | C1-C6 |\n| plan_002_k57_extension.py | All 4 | `plim_with_T`/`plim_exposure` | Generated per K | Random Dirichlet |\n\nThis comprehensive report captures all the critical implementation details, parameter conventions, and ASV framework specifications across all files."
      }
    ],
    "totalDurationMs": 45486,
    "totalTokens": 68881,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 47908,
      "cache_read_input_tokens": 15897,
      "output_tokens": 5069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 47908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5069,
          "cache_read_input_tokens": 15897,
          "cache_creation_input_tokens": 47908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 47908,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01VCbNfoocjq24Ksecukuf61`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "3c0c02be-d40d-45bf-be34-370a26208f6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192XsrX6HwftkBJh3BGzRj9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5649,
      "cache_read_input_tokens": 26345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5649
      },
      "output_tokens": 61,
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

_source line 30 · 2026-05-20T21:01:28.884Z_

<details><summary>↩ Tool result · `toolu_01VCbNfoocjq24Ksecukuf61`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_005: ASV framework extension to M-bias, IV, front-door topologies.
4	Extends plan_004 v3 (envelope monotonicity + magnitude/sign-flip dual reporting)
5	to complete Claim 2 coverage across all 6 DAG topologies.
6	"""
7	
8	import numpy as np
9	import json
10	import time
11	
12	K = 3
13	
14	# ============================================================================
15	# Utilities (from plan_004 v3)
16	# ============================================================================
17	
18	def softmax_sample(logits, rng):
19	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
20	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
21	    cum = np.cumsum(probs, axis=1)
22	    u = rng.uniform(size=logits.shape[0])
23	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
24	
25	
26	def generate_Astar(A, C, rng):
27	    probs = C[:, A]
28	    cum = np.cumsum(probs, axis=0)
29	    u = rng.uniform(size=len(A))
30	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
31	
32	
33	def ols_with_dummies(Y, T, Astar, K=3):
34	    N = len(Y)
35	    D = np.zeros((N, K - 1))
36	    for k in range(1, K):
37	        D[:, k - 1] = (Astar == k).astype(float)
38	    X = np.column_stack([np.ones(N), T, D])
39	    try:
40	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
41	        resid = Y - X @ beta
42	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
43	        XtX_inv = np.linalg.inv(X.T @ X)
44	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
45	    except np.linalg.LinAlgError:
46	        beta = np.full(X.shape[1], np.nan)
47	        se = np.full(X.shape[1], np.nan)
48	    return beta, se
49	
50	
51	# ============================================================================
52	# C(delta) Parameterization (from plan_004 v3)
53	# ============================================================================
54	
55	class LinearInterpolation:
56	    def __call__(self, C0, delta):
57	        K = C0.shape[0]
58	        C_d = (1 - delta) * np.eye(K) + delta * C0
59	        C_d = np.maximum(C_d, 0.0)
60	        col_sums = C_d.sum(axis=0)
61	        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
62	        C_d = C_d / col_sums
63	        return C_d
64	
65	    def delta_range(self, C0=None):
66	        if C0 is None:
67	            return (0.0, 5.0)
68	        min_diag = np.diag(C0).min()
69	        if min_diag >= 1.0:
70	            return (0.0, 10.0)
71	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
72	        return (0.0, delta_max)
73	
74	
75	# ============================================================================
76	# C matrices (from plan_004 v3)
77	# ============================================================================
78	
79	def make_C_list():
80	    return {
81	        "C1_sym": np.array([[0.80, 0.10, 0.10],
82	                            [0.10, 0.80, 0.10],
83	                            [0.10, 0.10, 0.80]]),
84	        "C2_high": np.array([[0.90, 0.05, 0.05],
85	                             [0.05, 0.90, 0.05],
86	                             [0.05, 0.05, 0.90]]),
87	        "C3_asym": np.array([[0.70, 0.20, 0.10],
88	                             [0.15, 0.70, 0.15],
89	                             [0.10, 0.15, 0.75]]),
90	        "C4_weak": np.array([[0.60, 0.20, 0.20],
91	                             [0.20, 0.60, 0.20],
92	                             [0.15, 0.15, 0.70]]),
93	        "C5_perm": np.array([[0.40, 0.30, 0.30],
94	                             [0.30, 0.40, 0.30],
95	                             [0.30, 0.30, 0.40]]),
96	        "C6_diff": np.array([[0.85, 0.075, 0.075],
97	                             [0.15, 0.70, 0.15],
98	                             [0.05, 0.05, 0.90]]),
99	    }
100	
101	
102	def normalize_C_list(C_dict):
103	    out = {}
104	    for name, C in C_dict.items():
105	        C = np.maximum(C, 0.0)
106	        cs = C.sum(axis=0)
107	        cs = np.where(cs < 1e-10, 1.0, cs)
108	        out[name] = C / cs
109	    return out
110	
111	
112	def random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):
113	    C = np.zeros((K, K))
114	    for k in range(K):
115	        alphas = np.full(K, offdiag_alpha)
116	        alphas[k] = diag_alpha
117	        C[:, k] = rng.dirichlet(alphas)
118	    return C
119	
120	
121	# ============================================================================
122	# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y
123	# ============================================================================
124	
125	MBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,
126	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
127	
128	
129	def _gen_mbias(N, params, rng):
130	    U1 = rng.normal(0, 1, N)
131	    U2 = rng.normal(0, 1, N)
132	    T = params['delta'] * U1 + rng.normal(0, 1, N)
133	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
134	    logits = np.column_stack([
135	        np.zeros(N),
136	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
137	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
138	    ])
139	    A = softmax_sample(logits, rng)
140	    return T, Y, A
141	
142	
143	def gen_mbias_data(N, params, C0, rng):
144	    T, Y, A = _gen_mbias(N, params, rng)
145	    Astar = generate_Astar(A, C0, rng)
146	    return T, Y, A, Astar
147	
148	
149	def precomp_mbias(params, N=2_000_000, seed=999):
150	    rng = np.random.default_rng(seed)
151	    T, Y, A = _gen_mbias(N, params, rng)
152	    DA = np.zeros((N, K))
153	    for k in range(K):
154	        DA[:, k] = (A == k).astype(float)
155	    return dict(
156	        E_T=T.mean(), E_T2=(T**2).mean(),
157	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
158	        E_DA=DA.mean(0),
159	        E_DA_T=(DA * T[:, None]).mean(0),
160	        E_DA_Y=(DA * Y[:, None]).mean(0))
161	
162	
163	def plim_mbias(C, st):
164	    """OLS plim for Y ~ 1 + T + D1_A* + D2_A*."""
165	    ds  = C @ st['E_DA']
166	    dst = C @ st['E_DA_T']
167	    dsy = C @ st['E_DA_Y']
168	    ET, ET2 = st['E_T'], st['E_T2']
169	    EY, ETY = st['E_Y'], st['E_TY']
170	    EZZ = np.array([
171	        [1,      ET,      ds[1],    ds[2]   ],
172	        [ET,     ET2,     dst[1],   dst[2]  ],
173	        [ds[1],  dst[1],  ds[1],    0       ],
174	        [ds[2],  dst[2],  0,        ds[2]   ]])
175	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
176	    return np.linalg.solve(EZZ, EZY)
177	
178	
179	# ============================================================================
180	# Topology 2: IV — Z->A->Y, U->{A,Y}
181	# ============================================================================
182	
183	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
184	IV_BETA = np.array([0.0, 0.5, -0.25])
185	
186	
187	def _gen_iv(N, beta, params, rng):
188	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
189	    U = rng.normal(0, 1, N)
190	    eps = rng.normal(0, 1, N)
191	    logits = np.column_stack([
192	        np.zeros(N),
193	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
194	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
195	    ])
196	    A = softmax_sample(logits, rng)
197	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
198	         + params['lam'] * U + eps)
199	    return Z_iv, U, Y, A
200	
201	
202	def gen_iv_data(N, beta, params, C0, rng):
203	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
204	    Astar = generate_Astar(A, C0, rng)
205	    return Z_iv, Y, A, Astar
206	
207	
208	def precomp_iv(beta, params, N=2_000_000, seed=999):
209	    """Precompute reduced form and first stage for Wald estimator."""
210	    rng = np.random.default_rng(seed)
211	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
212	    z1 = Z_iv == 1; z0 = Z_iv == 0
213	    RF = Y[z1].mean() - Y[z0].mean()
214	    FS = np.zeros(K)
215	    for k in range(K):
216	        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
217	    return dict(RF=RF, FS=FS)
218	
219	
220	def plim_iv(C, st):
221	    """Wald estimator: RF / FS*_1 where FS* = C @ FS."""
222	    FS_star = C @ st['FS']
223	    if abs(FS_star[1]) < 1e-8:
224	        return np.nan
225	    return st['RF'] / FS_star[1]
226	
227	
228	def wald_with_se(Z, Y, Astar, k=1):
229	    """Finite-sample Wald estimator with delta-method SE."""
230	    z1 = Z == 1; z0 = Z == 0
231	    n1 = float(z1.sum()); n0 = float(z0.sum())
232	    if n1 < 2 or n0 < 2:
233	        return np.nan, np.nan
234	    RF = Y[z1].mean() - Y[z0].mean()
235	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
236	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
237	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
238	    FS = Dk_z1 - Dk_z0
239	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
240	    if abs(FS) < 1e-8:
241	        return np.nan, np.nan
242	    Wald = RF / FS
243	    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4
244	    SE = np.sqrt(max(var_Wald, 0))
245	    return Wald, SE
246	
247	
248	# ============================================================================
249	# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}
250	# ============================================================================
251	
252	ALPHA_U = 1.0
253	LAMBDA_U = 1.0
254	GAMMA_FD = np.array([0.0, 0.5, -0.3])
255	DELTA_FD = np.array([0.0, 1.0, -0.8])
256	BETA_FD = np.array([0.0, 1.0, -0.5])
257	
258	
259	def _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):
260	    if g is None: g = GAMMA_FD
261	    if d is None: d = DELTA_FD
262	    if aU is None: aU = ALPHA_U
263	    if lU is None: lU = LAMBDA_U
264	    U = rng.normal(0, 1, N)
265	    T = aU * U + rng.normal(0, 1, N)
266	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
267	    lo -= lo.max(1, keepdims=True)
268	    e = np.exp(lo)
269	    p = e / e.sum(1, keepdims=True)
270	    cu = np.cumsum(p, axis=1)
271	    u = rng.uniform(size=N)
272	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
273	    DM1 = (M == 1).astype(float)
274	    DM2 = (M == 2).astype(float)
275	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
276	    return T, M, Y, U
277	
278	
279	def gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):
280	    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
281	    Mstar = generate_Astar(M, C0, rng)
282	    return T, Y, M, Mstar
283	
284	
285	def precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):
286	    rng = np.random.default_rng(seed)
287	    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
288	    DM = np.zeros((N, K))
289	    for k in range(K):
290	        DM[:, k] = (M == k).astype(float)
291	    return dict(
292	        E_T=T.mean(), E_T2=(T**2).mean(),
293	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
294	        E_DM=DM.mean(0),
295	        E_DM_T=(DM * T[:, None]).mean(0),
296	        E_DM_Y=(DM * Y[:, None]).mean(0))
297	
298	
299	def plim_fd(C, st):
300	    """OLS plim for Y ~ 1 + T + D1_M* + D2_M*."""
301	    ds  = C @ st['E_DM']
302	    dst = C @ st['E_DM_T']
303	    dsy = C @ st['E_DM_Y']
304	    ET, ET2 = st['E_T'], st['E_T2']
305	    EY, ETY = st['E_Y'], st['E_TY']
306	    EZZ = np.array([
307	        [1,      ET,      ds[1],    ds[2]   ],
308	        [ET,     ET2,     dst[1],   dst[2]  ],
309	        [ds[1],  dst[1],  ds[1],    0       ],
310	        [ds[2],  dst[2],  0,        ds[2]   ]])
311	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
312	    return np.linalg.solve(EZZ, EZY)
313	
314	
315	# ============================================================================
316	# ASV Framework
317	# ============================================================================
318	
319	def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
320	    dmin, dmax = param.delta_range(C0)
321	    deltas = np.linspace(dmin, dmax, n_grid)
322	    tau_curve = np.zeros(n_grid)
323	    for i, d in enumerate(deltas):
324	        C_d = param(C0, d)
325	        if topology == "mbias":
326	            tau_curve[i] = plim_mbias(C_d, st)[1]
327	        elif topology == "iv":
328	            tau_curve[i] = plim_iv(C_d, st)
329	        elif topology == "frontdoor":
330	            tau_curve[i] = plim_fd(C_d, st)[1]
331	    bias_abs = np.abs(tau_curve - tau_true)
332	    return deltas, bias_abs, tau_curve
333	
334	
335	def compute_envelope(bias_abs):
336	    env = np.zeros_like(bias_abs)
337	    running_max = 0.0
338	    for i in range(len(bias_abs)):
339	        v = bias_abs[i]
340	        if not np.isnan(v):
341	            running_max = max(running_max, v)
342	        env[i] = running_max
343	    return env
344	
345	
346	def verify_envelope_monotonicity(envelope):
347	    diffs = np.diff(envelope)
348	    return int(np.sum(diffs < -1e-12))
349	
350	
351	def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
352	                         threshold_value=0.1, st=None, n_grid=1500):
353	    deltas, bias_abs, tau_curve = compute_bias_curve(
354	        topology, C0, param, tau_true, st, n_grid)
355	    envelope = compute_envelope(bias_abs)
356	
357	    valid_ba = bias_abs[~np.isnan(bias_abs)]
358	    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0
359	    env_violations = verify_envelope_monotonicity(envelope)
360	
361	    asv = None
362	    if threshold_type == "sign_flip":
363	        if abs(tau_true) < 1e-12:
364	            asv = None
365	        else:
366	            baseline_sign = np.sign(tau_true)
367	            for i, d in enumerate(deltas):
368	                if np.isnan(tau_curve[i]):
369	                    continue
370	                if np.sign(tau_curve[i]) != baseline_sign:
371	                    asv = d
372	                    break
373	    elif threshold_type == "magnitude_relative":
374	        if abs(tau_true) < 1e-12:
375	            asv = None
376	        else:
377	            thresh = threshold_value * abs(tau_true)
378	            for i, d in enumerate(deltas):
379	                if envelope[i] > thresh:
380	                    asv = d
381	                    break
382	    elif threshold_type == "magnitude_absolute":
383	        thresh = threshold_value
384	        for i, d in enumerate(deltas):
385	            if envelope[i] > thresh:
386	                asv = d
387	                break
388	
389	    return {
390	        "asv": asv,
391	        "raw_violations": raw_violations,
392	        "envelope_violations": env_violations,
393	        "deltas": deltas,
394	        "tau_curve": tau_curve,
395	        "envelope": envelope,
396	    }
397	
398	
399	def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
400	    if abs(tau_true) < 1e-12:
401	        return None
402	    thresh = rel_thresh * abs(tau_true)
403	    running_max = 0.0
404	    for i in range(len(deltas)):
405	        b = abs(tau_curve[i] - tau_true)
406	        if np.isnan(b):
407	            continue
408	        running_max = max(running_max, b)
409	        if running_max > thresh:
410	            return deltas[i]
411	    return None
412	
413	
414	# ============================================================================
415	# Part 1: Envelope Monotonicity
416	# ============================================================================
417	
418	def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
419	    print("\n" + "=" * 70)
420	    print("PART 1: Envelope Monotonicity (tau=0.5)")
421	    print("=" * 70)
422	    t0 = time.time()
423	    param = LinearInterpolation()
424	    C_list = normalize_C_list(make_C_list())
425	
426	    for topo, st, tau_true, label in [
427	        ("mbias", st_mb, 0.5, "M-bias"),
428	        ("iv", st_iv, 0.5, "IV"),
429	        ("frontdoor", st_fd, tau_fd, "Front-door"),
430	    ]:
431	        print(f"\n  {label} (tau_true={tau_true:.4f}):")
432	        for cname, C0 in C_list.items():
433	            r = compute_asv_envelope(topo, C0, tau_true, param,
434	                                     "magnitude_relative", 0.1, st=st)
435	            print(f"    {cname}: raw_violations={r['raw_violations']}/1500, "
436	                  f"envelope_violations={r['envelope_violations']}/1500")
437	    print(f"\n  Time: {time.time()-t0:.1f}s")
438	
439	
440	# ============================================================================
441	# Part 2: ASV Values (tau=0.5)
442	# ============================================================================
443	
444	def part2_asv_values(st_mb, st_iv, st_fd, tau_fd):
445	    print("\n" + "=" * 70)
446	    print("PART 2: ASV Values (tau=0.5)")
447	    print("=" * 70)
448	    t0 = time.time()
449	    param = LinearInterpolation()
450	    C_list = normalize_C_list(make_C_list())
451	    results = {}
452	
453	    print(f"\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}")
454	    print("  " + "-" * 45)
455	
456	    for topo, st, tau_true, label in [
457	        ("mbias", st_mb, 0.5, "M-bias"),
458	        ("iv", st_iv, 0.5, "IV"),
459	        ("frontdoor", st_fd, tau_fd, "Front-door"),
460	    ]:
461	        for cname, C0 in C_list.items():
462	            r_sf = compute_asv_envelope(topo, C0, tau_true, param,
463	                                        "sign_flip", st=st)
464	            r_mag = compute_asv_envelope(topo, C0, tau_true, param,
465	                                         "magnitude_relative", 0.1, st=st)
466	            sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
467	            mg_s = f"{r_mag['asv']:.3f}" if r_mag['asv'] is not None else "None"
468	            print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}")
469	            results[(label, cname)] = {
470	                "sign_flip": r_sf['asv'], "magnitude_10pct": r_mag['asv']}
471	    print(f"\n  Time: {time.time()-t0:.1f}s")
472	    return results
473	
474	
475	# ============================================================================
476	# Part 3: Small-tau ASV
477	# ============================================================================
478	
479	def part3_small_tau_asv():
480	    print("\n" + "=" * 70)
481	    print("PART 3: Small-tau ASV (tau=0.05, 0.1)")
482	    print("=" * 70)
483	    t0 = time.time()
484	    param = LinearInterpolation()
485	    C_list = normalize_C_list(make_C_list())
486	    results = {}
487	
488	    for tau_val in [0.05, 0.1]:
489	        print(f"\n  --- tau = {tau_val} ---")
490	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
491	        st_mb = precomp_mbias(mb_p, N=2_000_000)
492	        iv_b = np.array([0.0, tau_val, -tau_val/2])
493	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
494	        lU = tau_val * 2
495	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))
496	        tau_fd = plim_fd(np.eye(K), st_fd)[1]
497	        print(f"  Front-door tau_I = {tau_fd:.6f}")
498	
499	        hdr = f"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}"
500	        print(hdr)
501	        print("  " + "-" * 55)
502	
503	        for topo, st, tau_true, label in [
504	            ("mbias", st_mb, tau_val, "M-bias"),
505	            ("iv", st_iv, tau_val, "IV"),
506	            ("frontdoor", st_fd, tau_fd, "Front-door"),
507	        ]:
508	            for cname, C0 in C_list.items():
509	                r_sf = compute_asv_envelope(topo, C0, tau_true, param,
510	                                            "sign_flip", st=st)
511	                r_mg = compute_asv_envelope(topo, C0, tau_true, param,
512	                                            "magnitude_relative", 0.1, st=st)
513	                r_ab = compute_asv_envelope(topo, C0, tau_true, param,
514	                                            "magnitude_absolute", 0.05, st=st)
515	                sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
516	                mg_s = f"{r_mg['asv']:.3f}" if r_mg['asv'] is not None else "None"
517	                ab_s = f"{r_ab['asv']:.3f}" if r_ab['asv'] is not None else "None"
518	                print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}")
519	                results[(tau_val, label, cname)] = {
520	                    "sign_flip": r_sf['asv'],
521	                    "magnitude_10pct": r_mg['asv'],
522	                    "magnitude_abs05": r_ab['asv']}
523	    print(f"\n  Time: {time.time()-t0:.1f}s")
524	    return results
525	
526	
527	# ============================================================================
528	# Part 4: MC Coverage
529	# ============================================================================
530	
531	def part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):
532	    print("\n" + "=" * 70)
533	    print(f"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})")
534	    print("=" * 70)
535	    t0 = time.time()
536	    rng = np.random.default_rng(42)
537	    results = {}
538	
539	    for tau_val in [0.05, 0.1]:
540	        print(f"\n  --- tau = {tau_val} ---")
541	
542	        # --- M-bias ---
543	        print("  [M-bias]")
544	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
545	        st_mb = precomp_mbias(mb_p, N=2_000_000)
546	        plim_ok = 0; bias_ok = 0
547	        for s in range(n_scenarios):
548	            C0 = random_C0(K, rng)
549	            tau_plim = plim_mbias(C0, st_mb)[1]
550	            bias_theory = abs(tau_plim - tau_val)
551	            tau_mc = np.zeros(reps)
552	            for r in range(reps):
553	                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)
554	                bh, _ = ols_with_dummies(Yd, Td, Asd, K)
555	                tau_mc[r] = bh[1]
556	            mc_mean = tau_mc.mean()
557	            mc_se = tau_mc.std() / np.sqrt(reps)
558	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
559	                plim_ok += 1
560	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:
561	                bias_ok += 1
562	            if (s + 1) % 100 == 0:
563	                print(f"    ... {s+1}/{n_scenarios}")
564	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
565	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
566	        results[("mbias", tau_val)] = {
567	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
568	
569	        # --- IV ---
570	        print("  [IV]")
571	        iv_b = np.array([0.0, tau_val, -tau_val/2])
572	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
573	        plim_ok = 0; bias_ok = 0
574	        for s in range(n_scenarios):
575	            C0 = random_C0(K, rng)
576	            tau_plim = plim_iv(C0, st_iv)
577	            if np.isnan(tau_plim):
578	                plim_ok += 1; bias_ok += 1; continue
579	            bias_theory = abs(tau_plim - tau_val)
580	            tau_mc = np.zeros(reps)
581	            for r in range(reps):
582	                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)
583	                w, _ = wald_with_se(Zd, Yd, Asd)
584	                tau_mc[r] = w
585	            valid = ~np.isnan(tau_mc)
586	            if valid.sum() < reps * 0.5:
587	                plim_ok += 1; bias_ok += 1; continue
588	            mc_mean = tau_mc[valid].mean()
589	            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())
590	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:
591	                plim_ok += 1
592	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:
593	                bias_ok += 1
594	            if (s + 1) % 100 == 0:
595	                print(f"    ... {s+1}/{n_scenarios}")
596	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
597	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
598	        results[("iv", tau_val)] = {
599	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
600	
601	        # --- Front-door ---
602	        print("  [Front-door]")
603	        lU = tau_val * 2
604	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
605	                           seed=300+int(tau_val*100))
606	        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
607	        plim_ok = 0; bias_ok = 0
608	        for s in range(n_scenarios):
609	            C0 = random_C0(K, rng)
610	            tau_plim = plim_fd(C0, st_fd)[1]
611	            bias_theory = abs(tau_plim - tau_I_fd)
612	            tau_mc = np.zeros(reps)
613	            for r in range(reps):
614	                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)
615	                bh, _ = ols_with_dummies(Yd, Td, Msd, K)
616	                tau_mc[r] = bh[1]
617	            mc_mean = tau_mc.mean()
618	            mc_se = tau_mc.std() / np.sqrt(reps)
619	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
620	                plim_ok += 1
621	            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:
622	                bias_ok += 1
623	            if (s + 1) % 100 == 0:
624	                print(f"    ... {s+1}/{n_scenarios}")
625	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
626	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
627	        results[("frontdoor", tau_val)] = {
628	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
629	
630	    print(f"\n  Total time: {time.time()-t0:.1f}s")
631	    return results
632	
633	
634	# ============================================================================
635	# Part 5: Type I/II
636	# ============================================================================
637	
638	def part5_type_errors(n_mc=500, N_sample=5000):
639	    print("\n" + "=" * 70)
640	    print(f"PART 5: Type I/II ({n_mc} MC x N={N_sample})")
641	    print("  Decision: reject if |tau_hat/SE|>1.96 AND magnitude_ASV > 1")
642	    print("=" * 70)
643	    t0 = time.time()
644	    param = LinearInterpolation()
645	    C_list = normalize_C_list(make_C_list())
646	    results = {}
647	    seed_ctr = 3000
648	
649	    for tau_val in [0.05, 0.1]:
650	        print(f"\n  --- tau = {tau_val} ---")
651	        header = (f"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} "
652	                  f"{'mag_rej':>10} {'mean_masv':>10}")
653	
654	        # === M-bias ===
655	        print("\n  [M-bias]")
656	        print(header)
657	        print("  " + "-" * 52)
658	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
659	            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h
660	            st_h = precomp_mbias(mb_p, N=2_000_000)
661	            for cname, C0 in C_list.items():
662	                seed_ctr += 1
663	                dmin, dmax = param.delta_range(C0)
664	                deltas = np.linspace(dmin, dmax, 1500)
665	                tau_curve = np.array([
666	                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])
667	                rng_mc = np.random.default_rng(seed_ctr)
668	                naive_rej = 0; mag_rej = 0; masv_vals = []
669	                for mc in range(n_mc):
670	                    Td, Yd, _, Asd = gen_mbias_data(
671	                        N_sample, mb_p, C0, rng_mc)
672	                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)
673	                    tau_hat, se_tau = bh[1], seh[1]
674	                    reject = (abs(tau_hat / se_tau) > 1.96
675	                              if se_tau > 1e-10 else False)
676	                    if reject:
677	                        naive_rej += 1
678	                    masv = compute_magnitude_asv_fast(
679	                        tau_curve, deltas, tau_h, 0.1)
680	                    masv_vals.append(masv)
681	                    if reject and (masv is None or masv > 1.0):
682	                        mag_rej += 1
683	                mf = [a for a in masv_vals if a is not None]
684	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
685	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
686	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
687	                results[("mbias", tau_val, cname, h_label)] = {
688	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
689	
690	        # === IV ===
691	        print("\n  [IV]")
692	        print(header)
693	        print("  " + "-" * 52)
694	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
695	            iv_b = np.array([0.0, tau_h, -tau_h/2])
696	            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
697	            for cname, C0 in C_list.items():
698	                seed_ctr += 1
699	                dmin, dmax = param.delta_range(C0)
700	                deltas = np.linspace(dmin, dmax, 1500)
701	                tau_curve = np.array([
702	                    plim_iv(param(C0, d), st_h) for d in deltas])
703	                rng_mc = np.random.default_rng(seed_ctr)
704	                naive_rej = 0; mag_rej = 0; masv_vals = []
705	                for mc in range(n_mc):
706	                    Zd, Yd, _, Asd = gen_iv_data(
707	                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)
708	                    w, se_w = wald_with_se(Zd, Yd, Asd)
709	                    reject = False
710	                    if not np.isnan(w) and se_w > 1e-10:
711	                        reject = abs(w / se_w) > 1.96
712	                    if reject:
713	                        naive_rej += 1
714	                    masv = compute_magnitude_asv_fast(
715	                        tau_curve, deltas, tau_h, 0.1)
716	                    masv_vals.append(masv)
717	                    if reject and (masv is None or masv > 1.0):
718	                        mag_rej += 1
719	                mf = [a for a in masv_vals if a is not None]
720	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
721	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
722	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
723	                results[("iv", tau_val, cname, h_label)] = {
724	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
725	
726	        # === Front-door ===
727	        print("\n  [Front-door]")
728	        print(header)
729	        print("  " + "-" * 52)
730	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
731	            if h_label == "H0":
732	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
733	                                  d=np.zeros(3), seed=400)
734	                tau_ref = 0.0
735	            else:
736	                lU = tau_val * 2
737	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
738	                                  seed=401+int(tau_val*100))
739	                tau_ref = plim_fd(np.eye(K), st_h)[1]
740	            print(f"    ({h_label}: tau_ref={tau_ref:.4f})")
741	            for cname, C0 in C_list.items():
742	                seed_ctr += 1
743	                dmin, dmax = param.delta_range(C0)
744	                deltas = np.linspace(dmin, dmax, 1500)
745	                tau_curve = np.array([
746	                    plim_fd(param(C0, d), st_h)[1] for d in deltas])
747	                rng_mc = np.random.default_rng(seed_ctr)
748	                naive_rej = 0; mag_rej = 0; masv_vals = []
749	                for mc in range(n_mc):
750	                    if h_label == "H0":
751	                        Td, Yd, _, Msd = gen_fd_data(
752	                            N_sample, BETA_FD, C0, rng_mc,
753	                            lU=0.0, aU=0.0, d=np.zeros(3))
754	                    else:
755	                        Td, Yd, _, Msd = gen_fd_data(
756	                            N_sample, BETA_FD, C0, rng_mc, lU=lU)
757	                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)
758	                    tau_hat, se_tau = bh[1], seh[1]
759	                    reject = (abs(tau_hat / se_tau) > 1.96
760	                              if se_tau > 1e-10 else False)
761	                    if reject:
762	                        naive_rej += 1
763	                    masv = compute_magnitude_asv_fast(
764	                        tau_curve, deltas, tau_ref, 0.1)
765	                    masv_vals.append(masv)
766	                    if reject and (masv is None or masv > 1.0):
767	                        mag_rej += 1
768	                mf = [a for a in masv_vals if a is not None]
769	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
770	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
771	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
772	                results[("frontdoor", tau_val, cname, h_label)] = {
773	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
774	
775	    print(f"\n  Total time: {time.time()-t0:.1f}s")
776	    return results
777	
778	
779	# ============================================================================
780	# Part 6: Summary JSON
781	# ============================================================================
782	
783	def collect_summary(asv_res, small_tau_res, cov_res, te_res):
784	    def _f(v):
785	        if v is None:
786	            return None
787	        return float(v)
788	
789	    summary = {
790	        "experiment": "plan_005_asv_extended",
791	        "topologies": ["mbias", "iv", "frontdoor"],
792	        "asv_values_tau05": {},
793	        "small_tau_asv": {},
794	        "coverage": {},
795	        "type_errors": {},
796	    }
797	    for (label, cname), vals in asv_res.items():
798	        summary["asv_values_tau05"][f"{label}_{cname}"] = {
799	            k: _f(v) for k, v in vals.items()}
800	    for (tv, label, cname), vals in small_tau_res.items():
801	        summary["small_tau_asv"][f"tau{tv}_{label}_{cname}"] = {
802	            k: _f(v) for k, v in vals.items()}
803	    for (topo, tv), vals in cov_res.items():
804	        summary["coverage"][f"{topo}_tau{tv}"] = vals
805	    for key, vals in te_res.items():
806	        summary["type_errors"]["_".join(str(x) for x in key)] = vals
807	    return summary
808	
809	
810	# ============================================================================
811	# Main
812	# ============================================================================
813	
814	if __name__ == "__main__":
815	    np.set_printoptions(precision=6, suppress=True)
816	    print("plan_005: ASV Framework Extension to M-bias/IV/Front-door")
817	    print("=" * 70)
818	    t_total = time.time()
819	
820	    print("\nPrecomputing sufficient statistics (tau=0.5)...")
821	    t0 = time.time()
822	    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)
823	    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
824	    print(f"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}")
825	
826	    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)
827	    tau_I_iv = plim_iv(np.eye(K), st_iv)
828	    print(f"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}")
829	
830	    st_fd = precomp_fd(BETA_FD, N=10_000_000)
831	    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
832	    print(f"  Front-door: plim(I)={tau_I_fd:.6f}")
833	    print(f"  Done ({time.time()-t0:.1f}s)")
834	
835	    part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)
836	    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_fd)
837	    small_tau_res = part3_small_tau_asv()
838	    cov_res = part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100)
839	    te_res = part5_type_errors(n_mc=500, N_sample=5000)
840	
841	    print("\n" + "=" * 70)
842	    print("PART 6: Summary JSON")
843	    print("=" * 70)
844	    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)
845	    print(json.dumps(summary, indent=2, default=str))
846	
847	    print("\n" + "=" * 70)
848	    elapsed = time.time() - t_total
849	    print(f"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
850	    print("=" * 70)
851	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "cffe2fe0-0514-450b-8270-ce1b26dbf5a0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_005: ASV framework extension to M-bias, IV, front-door topologies.\nExtends plan_004 v3 (envelope monotonicity + magnitude/sign-flip dual reporting)\nto complete Claim 2 coverage across all 6 DAG topologies.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\n\n# ============================================================================\n# Utilities (from plan_004 v3)\n# ============================================================================\n\ndef softmax_sample(logits, rng):\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K=3):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\n# ============================================================================\n# C(delta) Parameterization (from plan_004 v3)\n# ============================================================================\n\nclass LinearInterpolation:\n    def __call__(self, C0, delta):\n        K = C0.shape[0]\n        C_d = (1 - delta) * np.eye(K) + delta * C0\n        C_d = np.maximum(C_d, 0.0)\n        col_sums = C_d.sum(axis=0)\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n        C_d = C_d / col_sums\n        return C_d\n\n    def delta_range(self, C0=None):\n        if C0 is None:\n            return (0.0, 5.0)\n        min_diag = np.diag(C0).min()\n        if min_diag >= 1.0:\n            return (0.0, 10.0)\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n        return (0.0, delta_max)\n\n\n# ============================================================================\n# C matrices (from plan_004 v3)\n# ============================================================================\n\ndef make_C_list():\n    return {\n        \"C1_sym\": np.array([[0.80, 0.10, 0.10],\n                            [0.10, 0.80, 0.10],\n                            [0.10, 0.10, 0.80]]),\n        \"C2_high\": np.array([[0.90, 0.05, 0.05],\n                             [0.05, 0.90, 0.05],\n                             [0.05, 0.05, 0.90]]),\n        \"C3_asym\": np.array([[0.70, 0.20, 0.10],\n                             [0.15, 0.70, 0.15],\n                             [0.10, 0.15, 0.75]]),\n        \"C4_weak\": np.array([[0.60, 0.20, 0.20],\n                             [0.20, 0.60, 0.20],\n                             [0.15, 0.15, 0.70]]),\n        \"C5_perm\": np.array([[0.40, 0.30, 0.30],\n                             [0.30, 0.40, 0.30],\n                             [0.30, 0.30, 0.40]]),\n        \"C6_diff\": np.array([[0.85, 0.075, 0.075],\n                             [0.15, 0.70, 0.15],\n                             [0.05, 0.05, 0.90]]),\n    }\n\n\ndef normalize_C_list(C_dict):\n    out = {}\n    for name, C in C_dict.items():\n        C = np.maximum(C, 0.0)\n        cs = C.sum(axis=0)\n        cs = np.where(cs < 1e-10, 1.0, cs)\n        out[name] = C / cs\n    return out\n\n\ndef random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\n# ============================================================================\n# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y\n# ============================================================================\n\nMBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,\n                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)\n\n\ndef _gen_mbias(N, params, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = params['delta'] * U1 + rng.normal(0, 1, N)\n    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['a1'] * U1 + params['a2'] * U2,\n        params['g2'] + params['a3'] * U1 + params['a4'] * U2,\n    ])\n    A = softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef gen_mbias_data(N, params, C0, rng):\n    T, Y, A = _gen_mbias(N, params, rng)\n    Astar = generate_Astar(A, C0, rng)\n    return T, Y, A, Astar\n\n\ndef precomp_mbias(params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DA=DA.mean(0),\n        E_DA_T=(DA * T[:, None]).mean(0),\n        E_DA_Y=(DA * Y[:, None]).mean(0))\n\n\ndef plim_mbias(C, st):\n    \"\"\"OLS plim for Y ~ 1 + T + D1_A* + D2_A*.\"\"\"\n    ds  = C @ st['E_DA']\n    dst = C @ st['E_DA_T']\n    dsy = C @ st['E_DA_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\n# ============================================================================\n# Topology 2: IV — Z->A->Y, U->{A,Y}\n# ============================================================================\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\nIV_BETA = np.array([0.0, 0.5, -0.25])\n\n\ndef _gen_iv(N, beta, params, rng):\n    Z_iv = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,\n    ])\n    A = softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + eps)\n    return Z_iv, U, Y, A\n\n\ndef gen_iv_data(N, beta, params, C0, rng):\n    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n    Astar = generate_Astar(A, C0, rng)\n    return Z_iv, Y, A, Astar\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    \"\"\"Precompute reduced form and first stage for Wald estimator.\"\"\"\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n    z1 = Z_iv == 1; z0 = Z_iv == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.zeros(K)\n    for k in range(K):\n        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    \"\"\"Wald estimator: RF / FS*_1 where FS* = C @ FS.\"\"\"\n    FS_star = C @ st['FS']\n    if abs(FS_star[1]) < 1e-8:\n        return np.nan\n    return st['RF'] / FS_star[1]\n\n\ndef wald_with_se(Z, Y, Astar, k=1):\n    \"\"\"Finite-sample Wald estimator with delta-method SE.\"\"\"\n    z1 = Z == 1; z0 = Z == 0\n    n1 = float(z1.sum()); n0 = float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    Wald = RF / FS\n    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    SE = np.sqrt(max(var_Wald, 0))\n    return Wald, SE\n\n\n# ============================================================================\n# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}\n# ============================================================================\n\nALPHA_U = 1.0\nLAMBDA_U = 1.0\nGAMMA_FD = np.array([0.0, 0.5, -0.3])\nDELTA_FD = np.array([0.0, 1.0, -0.8])\nBETA_FD = np.array([0.0, 1.0, -0.5])\n\n\ndef _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):\n    if g is None: g = GAMMA_FD\n    if d is None: d = DELTA_FD\n    if aU is None: aU = ALPHA_U\n    if lU is None: lU = LAMBDA_U\n    U = rng.normal(0, 1, N)\n    T = aU * U + rng.normal(0, 1, N)\n    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])\n    lo -= lo.max(1, keepdims=True)\n    e = np.exp(lo)\n    p = e / e.sum(1, keepdims=True)\n    cu = np.cumsum(p, axis=1)\n    u = rng.uniform(size=N)\n    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n    DM1 = (M == 1).astype(float)\n    DM2 = (M == 2).astype(float)\n    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)\n    return T, M, Y, U\n\n\ndef gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):\n    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)\n    Mstar = generate_Astar(M, C0, rng)\n    return T, Y, M, Mstar\n\n\ndef precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):\n    rng = np.random.default_rng(seed)\n    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)\n    DM = np.zeros((N, K))\n    for k in range(K):\n        DM[:, k] = (M == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DM=DM.mean(0),\n        E_DM_T=(DM * T[:, None]).mean(0),\n        E_DM_Y=(DM * Y[:, None]).mean(0))\n\n\ndef plim_fd(C, st):\n    \"\"\"OLS plim for Y ~ 1 + T + D1_M* + D2_M*.\"\"\"\n    ds  = C @ st['E_DM']\n    dst = C @ st['E_DM_T']\n    dsy = C @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\n# ============================================================================\n# ASV Framework\n# ============================================================================\n\ndef compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):\n    dmin, dmax = param.delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = param(C0, d)\n        if topology == \"mbias\":\n            tau_curve[i] = plim_mbias(C_d, st)[1]\n        elif topology == \"iv\":\n            tau_curve[i] = plim_iv(C_d, st)\n        elif topology == \"frontdoor\":\n            tau_curve[i] = plim_fd(C_d, st)[1]\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef verify_envelope_monotonicity(envelope):\n    diffs = np.diff(envelope)\n    return int(np.sum(diffs < -1e-12))\n\n\ndef compute_asv_envelope(topology, C0, tau_true, param, threshold_type,\n                         threshold_value=0.1, st=None, n_grid=1500):\n    deltas, bias_abs, tau_curve = compute_bias_curve(\n        topology, C0, param, tau_true, st, n_grid)\n    envelope = compute_envelope(bias_abs)\n\n    valid_ba = bias_abs[~np.isnan(bias_abs)]\n    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0\n    env_violations = verify_envelope_monotonicity(envelope)\n\n    asv = None\n    if threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            asv = None\n        else:\n            baseline_sign = np.sign(tau_true)\n            for i, d in enumerate(deltas):\n                if np.isnan(tau_curve[i]):\n                    continue\n                if np.sign(tau_curve[i]) != baseline_sign:\n                    asv = d\n                    break\n    elif threshold_type == \"magnitude_relative\":\n        if abs(tau_true) < 1e-12:\n            asv = None\n        else:\n            thresh = threshold_value * abs(tau_true)\n            for i, d in enumerate(deltas):\n                if envelope[i] > thresh:\n                    asv = d\n                    break\n    elif threshold_type == \"magnitude_absolute\":\n        thresh = threshold_value\n        for i, d in enumerate(deltas):\n            if envelope[i] > thresh:\n                asv = d\n                break\n\n    return {\n        \"asv\": asv,\n        \"raw_violations\": raw_violations,\n        \"envelope_violations\": env_violations,\n        \"deltas\": deltas,\n        \"tau_curve\": tau_curve,\n        \"envelope\": envelope,\n    }\n\n\ndef compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):\n    if abs(tau_true) < 1e-12:\n        return None\n    thresh = rel_thresh * abs(tau_true)\n    running_max = 0.0\n    for i in range(len(deltas)):\n        b = abs(tau_curve[i] - tau_true)\n        if np.isnan(b):\n            continue\n        running_max = max(running_max, b)\n        if running_max > thresh:\n            return deltas[i]\n    return None\n\n\n# ============================================================================\n# Part 1: Envelope Monotonicity\n# ============================================================================\n\ndef part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 1: Envelope Monotonicity (tau=0.5)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n\n    for topo, st, tau_true, label in [\n        (\"mbias\", st_mb, 0.5, \"M-bias\"),\n        (\"iv\", st_iv, 0.5, \"IV\"),\n        (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n    ]:\n        print(f\"\\n  {label} (tau_true={tau_true:.4f}):\")\n        for cname, C0 in C_list.items():\n            r = compute_asv_envelope(topo, C0, tau_true, param,\n                                     \"magnitude_relative\", 0.1, st=st)\n            print(f\"    {cname}: raw_violations={r['raw_violations']}/1500, \"\n                  f\"envelope_violations={r['envelope_violations']}/1500\")\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n\n\n# ============================================================================\n# Part 2: ASV Values (tau=0.5)\n# ============================================================================\n\ndef part2_asv_values(st_mb, st_iv, st_fd, tau_fd):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 2: ASV Values (tau=0.5)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n\n    print(f\"\\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}\")\n    print(\"  \" + \"-\" * 45)\n\n    for topo, st, tau_true, label in [\n        (\"mbias\", st_mb, 0.5, \"M-bias\"),\n        (\"iv\", st_iv, 0.5, \"IV\"),\n        (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n    ]:\n        for cname, C0 in C_list.items():\n            r_sf = compute_asv_envelope(topo, C0, tau_true, param,\n                                        \"sign_flip\", st=st)\n            r_mag = compute_asv_envelope(topo, C0, tau_true, param,\n                                         \"magnitude_relative\", 0.1, st=st)\n            sf_s = f\"{r_sf['asv']:.3f}\" if r_sf['asv'] is not None else \"None\"\n            mg_s = f\"{r_mag['asv']:.3f}\" if r_mag['asv'] is not None else \"None\"\n            print(f\"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}\")\n            results[(label, cname)] = {\n                \"sign_flip\": r_sf['asv'], \"magnitude_10pct\": r_mag['asv']}\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 3: Small-tau ASV\n# ============================================================================\n\ndef part3_small_tau_asv():\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 3: Small-tau ASV (tau=0.05, 0.1)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val\n        st_mb = precomp_mbias(mb_p, N=2_000_000)\n        iv_b = np.array([0.0, tau_val, -tau_val/2])\n        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n        lU = tau_val * 2\n        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))\n        tau_fd = plim_fd(np.eye(K), st_fd)[1]\n        print(f\"  Front-door tau_I = {tau_fd:.6f}\")\n\n        hdr = f\"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}\"\n        print(hdr)\n        print(\"  \" + \"-\" * 55)\n\n        for topo, st, tau_true, label in [\n            (\"mbias\", st_mb, tau_val, \"M-bias\"),\n            (\"iv\", st_iv, tau_val, \"IV\"),\n            (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n        ]:\n            for cname, C0 in C_list.items():\n                r_sf = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"sign_flip\", st=st)\n                r_mg = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"magnitude_relative\", 0.1, st=st)\n                r_ab = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"magnitude_absolute\", 0.05, st=st)\n                sf_s = f\"{r_sf['asv']:.3f}\" if r_sf['asv'] is not None else \"None\"\n                mg_s = f\"{r_mg['asv']:.3f}\" if r_mg['asv'] is not None else \"None\"\n                ab_s = f\"{r_ab['asv']:.3f}\" if r_ab['asv'] is not None else \"None\"\n                print(f\"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}\")\n                results[(tau_val, label, cname)] = {\n                    \"sign_flip\": r_sf['asv'],\n                    \"magnitude_10pct\": r_mg['asv'],\n                    \"magnitude_abs05\": r_ab['asv']}\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 4: MC Coverage\n# ============================================================================\n\ndef part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    rng = np.random.default_rng(42)\n    results = {}\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n\n        # --- M-bias ---\n        print(\"  [M-bias]\")\n        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val\n        st_mb = precomp_mbias(mb_p, N=2_000_000)\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_mbias(C0, st_mb)[1]\n            bias_theory = abs(tau_plim - tau_val)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)\n                bh, _ = ols_with_dummies(Yd, Td, Asd, K)\n                tau_mc[r] = bh[1]\n            mc_mean = tau_mc.mean()\n            mc_se = tau_mc.std() / np.sqrt(reps)\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\n                plim_ok += 1\n            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"mbias\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n        # --- IV ---\n        print(\"  [IV]\")\n        iv_b = np.array([0.0, tau_val, -tau_val/2])\n        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_iv(C0, st_iv)\n            if np.isnan(tau_plim):\n                plim_ok += 1; bias_ok += 1; continue\n            bias_theory = abs(tau_plim - tau_val)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)\n                w, _ = wald_with_se(Zd, Yd, Asd)\n                tau_mc[r] = w\n            valid = ~np.isnan(tau_mc)\n            if valid.sum() < reps * 0.5:\n                plim_ok += 1; bias_ok += 1; continue\n            mc_mean = tau_mc[valid].mean()\n            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:\n                plim_ok += 1\n            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"iv\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n        # --- Front-door ---\n        print(\"  [Front-door]\")\n        lU = tau_val * 2\n        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,\n                           seed=300+int(tau_val*100))\n        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_fd(C0, st_fd)[1]\n            bias_theory = abs(tau_plim - tau_I_fd)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)\n                bh, _ = ols_with_dummies(Yd, Td, Msd, K)\n                tau_mc[r] = bh[1]\n            mc_mean = tau_mc.mean()\n            mc_se = tau_mc.std() / np.sqrt(reps)\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\n                plim_ok += 1\n            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"frontdoor\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 5: Type I/II\n# ============================================================================\n\ndef part5_type_errors(n_mc=500, N_sample=5000):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 5: Type I/II ({n_mc} MC x N={N_sample})\")\n    print(\"  Decision: reject if |tau_hat/SE|>1.96 AND magnitude_ASV > 1\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n    seed_ctr = 3000\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n        header = (f\"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} \"\n                  f\"{'mag_rej':>10} {'mean_masv':>10}\")\n\n        # === M-bias ===\n        print(\"\\n  [M-bias]\")\n        print(header)\n        print(\"  \" + \"-\" * 52)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h\n            st_h = precomp_mbias(mb_p, N=2_000_000)\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; mag_rej = 0; masv_vals = []\n                for mc in range(n_mc):\n                    Td, Yd, _, Asd = gen_mbias_data(\n                        N_sample, mb_p, C0, rng_mc)\n                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)\n                    tau_hat, se_tau = bh[1], seh[1]\n                    reject = (abs(tau_hat / se_tau) > 1.96\n                              if se_tau > 1e-10 else False)\n                    if reject:\n                        naive_rej += 1\n                    masv = compute_magnitude_asv_fast(\n                        tau_curve, deltas, tau_h, 0.1)\n                    masv_vals.append(masv)\n                    if reject and (masv is None or masv > 1.0):\n                        mag_rej += 1\n                mf = [a for a in masv_vals if a is not None]\n                mm = f\"{np.mean(mf):.2f}\" if mf else \"N/A\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{mag_rej/n_mc:>10.3f} {mm:>10}\")\n                results[(\"mbias\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"mag_rej\": mag_rej/n_mc}\n\n        # === IV ===\n        print(\"\\n  [IV]\")\n        print(header)\n        print(\"  \" + \"-\" * 52)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            iv_b = np.array([0.0, tau_h, -tau_h/2])\n            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_iv(param(C0, d), st_h) for d in deltas])\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; mag_rej = 0; masv_vals = []\n                for mc in range(n_mc):\n                    Zd, Yd, _, Asd = gen_iv_data(\n                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)\n                    w, se_w = wald_with_se(Zd, Yd, Asd)\n                    reject = False\n                    if not np.isnan(w) and se_w > 1e-10:\n                        reject = abs(w / se_w) > 1.96\n                    if reject:\n                        naive_rej += 1\n                    masv = compute_magnitude_asv_fast(\n                        tau_curve, deltas, tau_h, 0.1)\n                    masv_vals.append(masv)\n                    if reject and (masv is None or masv > 1.0):\n                        mag_rej += 1\n                mf = [a for a in masv_vals if a is not None]\n                mm = f\"{np.mean(mf):.2f}\" if mf else \"N/A\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{mag_rej/n_mc:>10.3f} {mm:>10}\")\n                results[(\"iv\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"mag_rej\": mag_rej/n_mc}\n\n        # === Front-door ===\n        print(\"\\n  [Front-door]\")\n        print(header)\n        print(\"  \" + \"-\" * 52)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            if h_label == \"H0\":\n                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,\n                                  d=np.zeros(3), seed=400)\n                tau_ref = 0.0\n            else:\n                lU = tau_val * 2\n                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,\n                                  seed=401+int(tau_val*100))\n                tau_ref = plim_fd(np.eye(K), st_h)[1]\n            print(f\"    ({h_label}: tau_ref={tau_ref:.4f})\")\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_fd(param(C0, d), st_h)[1] for d in deltas])\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; mag_rej = 0; masv_vals = []\n                for mc in range(n_mc):\n                    if h_label == \"H0\":\n                        Td, Yd, _, Msd = gen_fd_data(\n                            N_sample, BETA_FD, C0, rng_mc,\n                            lU=0.0, aU=0.0, d=np.zeros(3))\n                    else:\n                        Td, Yd, _, Msd = gen_fd_data(\n                            N_sample, BETA_FD, C0, rng_mc, lU=lU)\n                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)\n                    tau_hat, se_tau = bh[1], seh[1]\n                    reject = (abs(tau_hat / se_tau) > 1.96\n                              if se_tau > 1e-10 else False)\n                    if reject:\n                        naive_rej += 1\n                    masv = compute_magnitude_asv_fast(\n                        tau_curve, deltas, tau_ref, 0.1)\n                    masv_vals.append(masv)\n                    if reject and (masv is None or masv > 1.0):\n                        mag_rej += 1\n                mf = [a for a in masv_vals if a is not None]\n                mm = f\"{np.mean(mf):.2f}\" if mf else \"N/A\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{mag_rej/n_mc:>10.3f} {mm:>10}\")\n                results[(\"frontdoor\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"mag_rej\": mag_rej/n_mc}\n\n    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 6: Summary JSON\n# ============================================================================\n\ndef collect_summary(asv_res, small_tau_res, cov_res, te_res):\n    def _f(v):\n        if v is None:\n            return None\n        return float(v)\n\n    summary = {\n        \"experiment\": \"plan_005_asv_extended\",\n        \"topologies\": [\"mbias\", \"iv\", \"frontdoor\"],\n        \"asv_values_tau05\": {},\n        \"small_tau_asv\": {},\n        \"coverage\": {},\n        \"type_errors\": {},\n    }\n    for (label, cname), vals in asv_res.items():\n        summary[\"asv_values_tau05\"][f\"{label}_{cname}\"] = {\n            k: _f(v) for k, v in vals.items()}\n    for (tv, label, cname), vals in small_tau_res.items():\n        summary[\"small_tau_asv\"][f\"tau{tv}_{label}_{cname}\"] = {\n            k: _f(v) for k, v in vals.items()}\n    for (topo, tv), vals in cov_res.items():\n        summary[\"coverage\"][f\"{topo}_tau{tv}\"] = vals\n    for key, vals in te_res.items():\n        summary[\"type_errors\"][\"_\".join(str(x) for x in key)] = vals\n    return summary\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\nif __name__ == \"__main__\":\n    np.set_printoptions(precision=6, suppress=True)\n    print(\"plan_005: ASV Framework Extension to M-bias/IV/Front-door\")\n    print(\"=\" * 70)\n    t_total = time.time()\n\n    print(\"\\nPrecomputing sufficient statistics (tau=0.5)...\")\n    t0 = time.time()\n    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)\n    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]\n    print(f\"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}\")\n\n    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)\n    tau_I_iv = plim_iv(np.eye(K), st_iv)\n    print(f\"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}\")\n\n    st_fd = precomp_fd(BETA_FD, N=10_000_000)\n    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]\n    print(f\"  Front-door: plim(I)={tau_I_fd:.6f}\")\n    print(f\"  Done ({time.time()-t0:.1f}s)\")\n\n    part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)\n    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_fd)\n    small_tau_res = part3_small_tau_asv()\n    cov_res = part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100)\n    te_res = part5_type_errors(n_mc=500, N_sample=5000)\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 6: Summary JSON\")\n    print(\"=\" * 70)\n    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)\n    print(json.dumps(summary, indent=2, default=str))\n\n    print(\"\\n\" + \"=\" * 70)\n    elapsed = time.time() - t_total\n    print(f\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\")\n    print(\"=\" * 70)\n",
      "numLines": 851,
      "startLine": 1,
      "totalLines": 851
    }
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01JbYYKdC376cNkp7hHHUhTc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "150785b8-d28e-4cb9-a318-08c99a8f45b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192XsrX6HwftkBJh3BGzRj9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5649,
      "cache_read_input_tokens": 26345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5649
      },
      "output_tokens": 61,
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

_source line 32 · 2026-05-20T21:01:28.900Z_

<details><summary>↩ Tool result · `toolu_01JbYYKdC376cNkp7hHHUhTc`</summary>

```text
1	#!/usr/bin/env python3
2	# -*- coding: utf-8 -*-
3	"""Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification."""
4	import numpy as np
5	import time
6	import warnings
7	from collections import OrderedDict
8	
9	warnings.filterwarnings('ignore')
10	
11	# ================================================================
12	# Configuration
13	# ================================================================
14	K = 3
15	N_MC = 10_000
16	N_REPS = 1_000
17	N_LARGE = 50_000_000
18	N_RANDOM = 100_000
19	
20	BETA_MIXED = np.array([0.0, 1.0, -0.5])
21	BETA_SAME  = np.array([0.0, 1.0,  0.5])
22	
23	TAU = 0.5
24	GAMMA_MED = np.array([0.0, 0.5, -0.3])
25	DELTA_MED = np.array([0.0, 0.8, -0.6])
26	
27	ALPHA_U = 1.0
28	LAMBDA_U = 1.0
29	GAMMA_FD = np.array([0.0, 0.5, -0.3])
30	DELTA_FD = np.array([0.0, 1.0, -0.8])
31	
32	C_DICT = OrderedDict([
33	    ("1_sym_high",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
34	    ("2_asymmetric", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),
35	    ("3_struct_12",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),
36	    ("4_weak_diag",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),
37	    ("5_near_perm",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),
38	    ("6_diff_base",  np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
39	])
40	
41	COEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']
42	
43	
44	# ================================================================
45	# Helpers
46	# ================================================================
47	def softmax(x):
48	    e = np.exp(x - x.max())
49	    return e / e.sum()
50	
51	
52	def p_cat(t, g, d):
53	    return softmax(g + d * t)
54	
55	
56	def gen_Astar(A, C, rng):
57	    pr = C[:, A]
58	    cu = np.cumsum(pr, axis=0)
59	    u = rng.uniform(size=len(A))
60	    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)
61	
62	
63	def ols(Z, Y):
64	    return np.linalg.lstsq(Z, Y, rcond=None)[0]
65	
66	
67	def fv(v, w=8, p=4):
68	    return '[' + ' '.join(f'{x:>{w}.{p}f}' for x in v) + ']'
69	
70	
71	def fm(th, mc, se, k=2):
72	    ok = np.abs(mc - th) < k * se
73	    return ''.join('✓' if o else '✗' for o in ok), ok.all()
74	
75	
76	# ================================================================
77	# DAG 1  Mediation: T -> A -> Y
78	#
79	# DGP:  T ~ Bern(0.5)
80	#        A | T ~ Cat(softmax(gamma + delta*T))
81	#        Y = beta0 + beta1*D1 + beta2*D2 + tau*T + eps
82	#        A* | A ~ Cat(C[:, A])
83	#
84	# Researcher regression:  Y ~ 1 + T + D*_1 + D*_2
85	#
86	# Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
87	# eps indep of Z  =>  plim = (E[Z'Z])^{-1} E[Z'X] beta
88	#
89	# Key moments:
90	#   q_t = C @ p_{A|T=t}           (P(A*|T=t))
91	#   q_marg = 0.5*(q_0 + q_1)
92	#   E[D*_j * D_k] = C[j,k] * p_marg[k]
93	# ================================================================
94	def plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED):
95	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
96	    q0, q1 = C @ p0, C @ p1
97	    pm = .5 * (p0 + p1)
98	    qm = .5 * (q0 + q1)
99	
100	    EZZ = np.array([
101	        [1,      .5,        qm[1],      qm[2]     ],
102	        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],
103	        [qm[1],  .5*q1[1],  qm[1],      0         ],
104	        [qm[2],  .5*q1[2],  0,          qm[2]     ]])
105	
106	    EZX = np.array([
107	        [1,      .5,        pm[1],            pm[2]           ],
108	        [.5,     .5,        .5*p1[1],         .5*p1[2]        ],
109	        [qm[1],  .5*q1[1],  C[1,1]*pm[1],    C[1,2]*pm[2]   ],
110	        [qm[2],  .5*q1[2],  C[2,1]*pm[1],    C[2,2]*pm[2]   ]])
111	
112	    b = np.array([beta[0], tau, beta[1], beta[2]])
113	    return np.linalg.solve(EZZ, EZX @ b)
114	
115	
116	def mc_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED,
117	           nr=N_REPS, N=N_MC, seed=42):
118	    rng = np.random.default_rng(seed)
119	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
120	    out = np.zeros((nr, 4))
121	    for r in range(nr):
122	        T = rng.binomial(1, .5, N)
123	        pr = np.where(T[:, None] == 0, p0, p1)
124	        cu = np.cumsum(pr, axis=1)
125	        u = rng.uniform(size=N)
126	        A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
127	        D1 = (A == 1).astype(float)
128	        D2 = (A == 2).astype(float)
129	        Y = beta[0] + beta[1]*D1 + beta[2]*D2 + tau*T + rng.normal(0, 1, N)
130	        As = gen_Astar(A, C, rng)
131	        Z = np.column_stack([np.ones(N), T.astype(float),
132	                             (As == 1).astype(float), (As == 2).astype(float)])
133	        out[r] = ols(Z, Y)
134	    return out.mean(0), out.std(0) / np.sqrt(nr)
135	
136	
137	def rsearch_med(beta, tau, g=GAMMA_MED, d=DELTA_MED,
138	                ns=N_RANDOM, seed=999):
139	    rng = np.random.default_rng(seed)
140	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
141	    pm = .5 * (p0 + p1)
142	    b = np.array([beta[0], tau, beta[1], beta[2]])
143	    clean = plim_med(np.eye(K), beta, tau, g, d)
144	
145	    Cs = np.zeros((ns, K, K))
146	    for i in range(K):
147	        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)
148	
149	    q0 = Cs @ p0
150	    q1 = Cs @ p1
151	    qm = .5 * (q0 + q1)
152	
153	    EZZ = np.zeros((ns, 4, 4))
154	    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = .5
155	    EZZ[:, 0, 2] = EZZ[:, 2, 0] = qm[:, 1]
156	    EZZ[:, 0, 3] = EZZ[:, 3, 0] = qm[:, 2]
157	    EZZ[:, 1, 1] = .5
158	    EZZ[:, 1, 2] = EZZ[:, 2, 1] = .5 * q1[:, 1]
159	    EZZ[:, 1, 3] = EZZ[:, 3, 1] = .5 * q1[:, 2]
160	    EZZ[:, 2, 2] = qm[:, 1]
161	    EZZ[:, 3, 3] = qm[:, 2]
162	
163	    EZX = np.zeros((ns, 4, 4))
164	    EZX[:, 0, 0] = 1;       EZX[:, 0, 1] = .5
165	    EZX[:, 0, 2] = pm[1];   EZX[:, 0, 3] = pm[2]
166	    EZX[:, 1, 0] = .5;      EZX[:, 1, 1] = .5
167	    EZX[:, 1, 2] = .5 * p1[1]; EZX[:, 1, 3] = .5 * p1[2]
168	    EZX[:, 2, 0] = qm[:, 1];   EZX[:, 2, 1] = .5 * q1[:, 1]
169	    EZX[:, 2, 2] = Cs[:, 1, 1] * pm[1]; EZX[:, 2, 3] = Cs[:, 1, 2] * pm[2]
170	    EZX[:, 3, 0] = qm[:, 2];   EZX[:, 3, 1] = .5 * q1[:, 2]
171	    EZX[:, 3, 2] = Cs[:, 2, 1] * pm[1]; EZX[:, 3, 3] = Cs[:, 2, 2] * pm[2]
172	
173	    rhs = np.einsum('nij,j->ni', EZX, b)
174	    pl = np.linalg.solve(EZZ, rhs[:, :, None])[:, :, 0]
175	
176	    df = np.abs(pl - clean)
177	    viol = np.any(df > .01, 1).mean()
178	    nz = np.abs(clean) > 1e-6
179	    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
180	    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
181	    return viol, sign, amp
182	
183	
184	# ================================================================
185	# DAG 2  Front-door: T -> M -> Y,  U -> T,  U -> Y
186	#
187	# DGP:  U ~ N(0,1)
188	#        T = alpha_U * U + eta,  eta ~ N(0,1)
189	#        M | T ~ Cat(softmax(gamma + delta*T))
190	#        Y = beta1*D_{M,1} + beta2*D_{M,2} + lambda*U + eps
191	#        M* | M ~ Cat(C[:, M])
192	#
193	# Researcher regression:  Y ~ 1 + T + D*_{M,1} + D*_{M,2}
194	#
195	# T correlated with U (confounding), so E[Z'(lambda*U)] != 0.
196	# Use large-sample moment approximation:
197	#   plim = (E[Z'Z])^{-1} E[Z'Y]   estimated from N_LARGE samples.
198	#
199	# For fast random search, pre-compute sufficient statistics:
200	#   E[D_{M,k}], E[D_{M,k}*T], E[D_{M,k}*Y]  for k=0,1,2
201	# Then for any C:
202	#   E[D*_j] = sum_k C[j,k]*E[D_{M,k}]   etc.
203	# ================================================================
204	def _gen_fd(N, beta, rng, g=GAMMA_FD, d=DELTA_FD,
205	            aU=ALPHA_U, lU=LAMBDA_U):
206	    U = rng.normal(0, 1, N)
207	    T = aU * U + rng.normal(0, 1, N)
208	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
209	    lo -= lo.max(1, keepdims=True)
210	    e = np.exp(lo)
211	    p = e / e.sum(1, keepdims=True)
212	    cu = np.cumsum(p, axis=1)
213	    u = rng.uniform(size=N)
214	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
215	    DM1 = (M == 1).astype(float)
216	    DM2 = (M == 2).astype(float)
217	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
218	    return T, M, Y, U
219	
220	
221	def precomp_fd(beta, N=N_LARGE, seed=123):
222	    rng = np.random.default_rng(seed)
223	    T, M, Y, _ = _gen_fd(N, beta, rng)
224	    DM = np.zeros((N, K))
225	    for k in range(K):
226	        DM[:, k] = (M == k).astype(float)
227	    return dict(
228	        E_T=T.mean(), E_T2=(T**2).mean(),
229	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
230	        E_DM=DM.mean(0),
231	        E_DM_T=(DM * T[:, None]).mean(0),
232	        E_DM_Y=(DM * Y[:, None]).mean(0))
233	
234	
235	def plim_fd(C, st):
236	    ds  = C @ st['E_DM']
237	    dst = C @ st['E_DM_T']
238	    dsy = C @ st['E_DM_Y']
239	    ET, ET2 = st['E_T'], st['E_T2']
240	    EY, ETY = st['E_Y'], st['E_TY']
241	
242	    EZZ = np.array([
243	        [1,      ET,      ds[1],    ds[2]   ],
244	        [ET,     ET2,     dst[1],   dst[2]  ],
245	        [ds[1],  dst[1],  ds[1],    0       ],
246	        [ds[2],  dst[2],  0,        ds[2]   ]])
247	
248	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
249	    return np.linalg.solve(EZZ, EZY)
250	
251	
252	def mc_fd(C, beta, nr=N_REPS, N=N_MC, seed=42):
253	    rng = np.random.default_rng(seed)
254	    out = np.zeros((nr, 4))
255	    for r in range(nr):
256	        T, M, Y, _ = _gen_fd(N, beta, rng)
257	        Ms = gen_Astar(M, C, rng)
258	        Z = np.column_stack([np.ones(N), T,
259	                             (Ms == 1).astype(float),
260	                             (Ms == 2).astype(float)])
261	        out[r] = ols(Z, Y)
262	    return out.mean(0), out.std(0) / np.sqrt(nr)
263	
264	
265	def rsearch_fd(st, ns=N_RANDOM, seed=999):
266	    rng = np.random.default_rng(seed)
267	    clean = plim_fd(np.eye(K), st)
268	
269	    Cs = np.zeros((ns, K, K))
270	    for i in range(K):
271	        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)
272	
273	    E_DMs   = Cs @ st['E_DM']
274	    E_DMs_T = Cs @ st['E_DM_T']
275	    E_DMs_Y = Cs @ st['E_DM_Y']
276	    ET, ET2 = st['E_T'], st['E_T2']
277	    EY, ETY = st['E_Y'], st['E_TY']
278	
279	    EZZ = np.zeros((ns, 4, 4))
280	    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = ET
281	    EZZ[:, 0, 2] = EZZ[:, 2, 0] = E_DMs[:, 1]
282	    EZZ[:, 0, 3] = EZZ[:, 3, 0] = E_DMs[:, 2]
283	    EZZ[:, 1, 1] = ET2
284	    EZZ[:, 1, 2] = EZZ[:, 2, 1] = E_DMs_T[:, 1]
285	    EZZ[:, 1, 3] = EZZ[:, 3, 1] = E_DMs_T[:, 2]
286	    EZZ[:, 2, 2] = E_DMs[:, 1]
287	    EZZ[:, 3, 3] = E_DMs[:, 2]
288	
289	    EZY = np.zeros((ns, 4))
290	    EZY[:, 0] = EY;   EZY[:, 1] = ETY
291	    EZY[:, 2] = E_DMs_Y[:, 1]
292	    EZY[:, 3] = E_DMs_Y[:, 2]
293	
294	    pl = np.linalg.solve(EZZ, EZY[:, :, None])[:, :, 0]
295	
296	    df = np.abs(pl - clean)
297	    viol = np.any(df > .01, 1).mean()
298	    nz = np.abs(clean) > 1e-6
299	    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
300	    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
301	    return viol, sign, amp
302	
303	
304	# ================================================================
305	# Main
306	# ================================================================
307	def main():
308	    t0 = time.time()
309	    np.set_printoptions(precision=4, suppress=True)
310	
311	    for bn, beta in [("mixed [0,1,-0.5]", BETA_MIXED),
312	                      ("same [0,1,0.5]",   BETA_SAME)]:
313	
314	        # ---- DAG 1: Mediation ----
315	        print(f"\n{'='*90}")
316	        print(f"  MEDIATION: T -> A -> Y  |  beta={bn}")
317	        print(f"{'='*90}")
318	        p0, p1 = p_cat(0, GAMMA_MED, DELTA_MED), p_cat(1, GAMMA_MED, DELTA_MED)
319	        print(f"  P(A|T=0)={fv(p0,6,3)}  P(A|T=1)={fv(p1,6,3)}  tau={TAU}")
320	        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")
321	
322	        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
323	        print(hdr)
324	        print(f"  {'-'*92}")
325	
326	        all_ok = True
327	        for cn, C in C_DICT.items():
328	            th = plim_med(C, beta, TAU)
329	            mc, se = mc_med(C, beta, TAU)
330	            ms, ok = fm(th, mc, se)
331	            if not ok:
332	                all_ok = False
333	            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")
334	
335	        status = 'ALL MATCH' if all_ok else 'MISMATCH DETECTED'
336	        print(f"  >>> {status}")
337	
338	        t1 = time.time()
339	        v, s, a = rsearch_med(beta, TAU)
340	        t2 = time.time()
341	        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
342	              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
343	
344	        # ---- DAG 2: Front-door ----
345	        print(f"\n{'='*90}")
346	        print(f"  FRONT-DOOR: T -> M -> Y, U -> T, U -> Y  |  beta={bn}")
347	        print(f"{'='*90}")
348	        print(f"  alpha_U={ALPHA_U}  lambda_U={LAMBDA_U}")
349	        print(f"  M|T softmax: gamma={GAMMA_FD}  delta={DELTA_FD}")
350	        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")
351	
352	        t1 = time.time()
353	        st = precomp_fd(beta)
354	        t2 = time.time()
355	        print(f"  Moments pre-computed (N={N_LARGE//10**6}M, {t2-t1:.1f}s)\n")
356	
357	        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
358	        print(hdr)
359	        print(f"  {'-'*92}")
360	
361	        all_ok = True
362	        for cn, C in C_DICT.items():
363	            th = plim_fd(C, st)
364	            mc, se = mc_fd(C, beta)
365	            ms, ok = fm(th, mc, se, k=3)
366	            if not ok:
367	                all_ok = False
368	            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")
369	
370	        status = 'ALL MATCH (3σ)' if all_ok else 'MISMATCH DETECTED'
371	        print(f"  >>> {status}")
372	
373	        t1 = time.time()
374	        v, s, a = rsearch_fd(st)
375	        t2 = time.time()
376	        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
377	              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
378	
379	    print(f"\n{'='*90}")
380	    print(f"  Total: {time.time()-t0:.1f}s")
381	    print(f"{'='*90}")
382	
383	
384	if __name__ == "__main__":
385	    main()
386	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "c84a4b60-c452-4f11-a092-cbc81a899ce9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py",
      "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification.\"\"\"\nimport numpy as np\nimport time\nimport warnings\nfrom collections import OrderedDict\n\nwarnings.filterwarnings('ignore')\n\n# ================================================================\n# Configuration\n# ================================================================\nK = 3\nN_MC = 10_000\nN_REPS = 1_000\nN_LARGE = 50_000_000\nN_RANDOM = 100_000\n\nBETA_MIXED = np.array([0.0, 1.0, -0.5])\nBETA_SAME  = np.array([0.0, 1.0,  0.5])\n\nTAU = 0.5\nGAMMA_MED = np.array([0.0, 0.5, -0.3])\nDELTA_MED = np.array([0.0, 0.8, -0.6])\n\nALPHA_U = 1.0\nLAMBDA_U = 1.0\nGAMMA_FD = np.array([0.0, 0.5, -0.3])\nDELTA_FD = np.array([0.0, 1.0, -0.8])\n\nC_DICT = OrderedDict([\n    (\"1_sym_high\",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),\n    (\"2_asymmetric\", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),\n    (\"3_struct_12\",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),\n    (\"4_weak_diag\",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),\n    (\"5_near_perm\",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),\n    (\"6_diff_base\",  np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),\n])\n\nCOEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']\n\n\n# ================================================================\n# Helpers\n# ================================================================\ndef softmax(x):\n    e = np.exp(x - x.max())\n    return e / e.sum()\n\n\ndef p_cat(t, g, d):\n    return softmax(g + d * t)\n\n\ndef gen_Astar(A, C, rng):\n    pr = C[:, A]\n    cu = np.cumsum(pr, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)\n\n\ndef ols(Z, Y):\n    return np.linalg.lstsq(Z, Y, rcond=None)[0]\n\n\ndef fv(v, w=8, p=4):\n    return '[' + ' '.join(f'{x:>{w}.{p}f}' for x in v) + ']'\n\n\ndef fm(th, mc, se, k=2):\n    ok = np.abs(mc - th) < k * se\n    return ''.join('✓' if o else '✗' for o in ok), ok.all()\n\n\n# ================================================================\n# DAG 1  Mediation: T -> A -> Y\n#\n# DGP:  T ~ Bern(0.5)\n#        A | T ~ Cat(softmax(gamma + delta*T))\n#        Y = beta0 + beta1*D1 + beta2*D2 + tau*T + eps\n#        A* | A ~ Cat(C[:, A])\n#\n# Researcher regression:  Y ~ 1 + T + D*_1 + D*_2\n#\n# Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)\n# eps indep of Z  =>  plim = (E[Z'Z])^{-1} E[Z'X] beta\n#\n# Key moments:\n#   q_t = C @ p_{A|T=t}           (P(A*|T=t))\n#   q_marg = 0.5*(q_0 + q_1)\n#   E[D*_j * D_k] = C[j,k] * p_marg[k]\n# ================================================================\ndef plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED):\n    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)\n    q0, q1 = C @ p0, C @ p1\n    pm = .5 * (p0 + p1)\n    qm = .5 * (q0 + q1)\n\n    EZZ = np.array([\n        [1,      .5,        qm[1],      qm[2]     ],\n        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],\n        [qm[1],  .5*q1[1],  qm[1],      0         ],\n        [qm[2],  .5*q1[2],  0,          qm[2]     ]])\n\n    EZX = np.array([\n        [1,      .5,        pm[1],            pm[2]           ],\n        [.5,     .5,        .5*p1[1],         .5*p1[2]        ],\n        [qm[1],  .5*q1[1],  C[1,1]*pm[1],    C[1,2]*pm[2]   ],\n        [qm[2],  .5*q1[2],  C[2,1]*pm[1],    C[2,2]*pm[2]   ]])\n\n    b = np.array([beta[0], tau, beta[1], beta[2]])\n    return np.linalg.solve(EZZ, EZX @ b)\n\n\ndef mc_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED,\n           nr=N_REPS, N=N_MC, seed=42):\n    rng = np.random.default_rng(seed)\n    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)\n    out = np.zeros((nr, 4))\n    for r in range(nr):\n        T = rng.binomial(1, .5, N)\n        pr = np.where(T[:, None] == 0, p0, p1)\n        cu = np.cumsum(pr, axis=1)\n        u = rng.uniform(size=N)\n        A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n        D1 = (A == 1).astype(float)\n        D2 = (A == 2).astype(float)\n        Y = beta[0] + beta[1]*D1 + beta[2]*D2 + tau*T + rng.normal(0, 1, N)\n        As = gen_Astar(A, C, rng)\n        Z = np.column_stack([np.ones(N), T.astype(float),\n                             (As == 1).astype(float), (As == 2).astype(float)])\n        out[r] = ols(Z, Y)\n    return out.mean(0), out.std(0) / np.sqrt(nr)\n\n\ndef rsearch_med(beta, tau, g=GAMMA_MED, d=DELTA_MED,\n                ns=N_RANDOM, seed=999):\n    rng = np.random.default_rng(seed)\n    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)\n    pm = .5 * (p0 + p1)\n    b = np.array([beta[0], tau, beta[1], beta[2]])\n    clean = plim_med(np.eye(K), beta, tau, g, d)\n\n    Cs = np.zeros((ns, K, K))\n    for i in range(K):\n        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)\n\n    q0 = Cs @ p0\n    q1 = Cs @ p1\n    qm = .5 * (q0 + q1)\n\n    EZZ = np.zeros((ns, 4, 4))\n    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = .5\n    EZZ[:, 0, 2] = EZZ[:, 2, 0] = qm[:, 1]\n    EZZ[:, 0, 3] = EZZ[:, 3, 0] = qm[:, 2]\n    EZZ[:, 1, 1] = .5\n    EZZ[:, 1, 2] = EZZ[:, 2, 1] = .5 * q1[:, 1]\n    EZZ[:, 1, 3] = EZZ[:, 3, 1] = .5 * q1[:, 2]\n    EZZ[:, 2, 2] = qm[:, 1]\n    EZZ[:, 3, 3] = qm[:, 2]\n\n    EZX = np.zeros((ns, 4, 4))\n    EZX[:, 0, 0] = 1;       EZX[:, 0, 1] = .5\n    EZX[:, 0, 2] = pm[1];   EZX[:, 0, 3] = pm[2]\n    EZX[:, 1, 0] = .5;      EZX[:, 1, 1] = .5\n    EZX[:, 1, 2] = .5 * p1[1]; EZX[:, 1, 3] = .5 * p1[2]\n    EZX[:, 2, 0] = qm[:, 1];   EZX[:, 2, 1] = .5 * q1[:, 1]\n    EZX[:, 2, 2] = Cs[:, 1, 1] * pm[1]; EZX[:, 2, 3] = Cs[:, 1, 2] * pm[2]\n    EZX[:, 3, 0] = qm[:, 2];   EZX[:, 3, 1] = .5 * q1[:, 2]\n    EZX[:, 3, 2] = Cs[:, 2, 1] * pm[1]; EZX[:, 3, 3] = Cs[:, 2, 2] * pm[2]\n\n    rhs = np.einsum('nij,j->ni', EZX, b)\n    pl = np.linalg.solve(EZZ, rhs[:, :, None])[:, :, 0]\n\n    df = np.abs(pl - clean)\n    viol = np.any(df > .01, 1).mean()\n    nz = np.abs(clean) > 1e-6\n    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()\n    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()\n    return viol, sign, amp\n\n\n# ================================================================\n# DAG 2  Front-door: T -> M -> Y,  U -> T,  U -> Y\n#\n# DGP:  U ~ N(0,1)\n#        T = alpha_U * U + eta,  eta ~ N(0,1)\n#        M | T ~ Cat(softmax(gamma + delta*T))\n#        Y = beta1*D_{M,1} + beta2*D_{M,2} + lambda*U + eps\n#        M* | M ~ Cat(C[:, M])\n#\n# Researcher regression:  Y ~ 1 + T + D*_{M,1} + D*_{M,2}\n#\n# T correlated with U (confounding), so E[Z'(lambda*U)] != 0.\n# Use large-sample moment approximation:\n#   plim = (E[Z'Z])^{-1} E[Z'Y]   estimated from N_LARGE samples.\n#\n# For fast random search, pre-compute sufficient statistics:\n#   E[D_{M,k}], E[D_{M,k}*T], E[D_{M,k}*Y]  for k=0,1,2\n# Then for any C:\n#   E[D*_j] = sum_k C[j,k]*E[D_{M,k}]   etc.\n# ================================================================\ndef _gen_fd(N, beta, rng, g=GAMMA_FD, d=DELTA_FD,\n            aU=ALPHA_U, lU=LAMBDA_U):\n    U = rng.normal(0, 1, N)\n    T = aU * U + rng.normal(0, 1, N)\n    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])\n    lo -= lo.max(1, keepdims=True)\n    e = np.exp(lo)\n    p = e / e.sum(1, keepdims=True)\n    cu = np.cumsum(p, axis=1)\n    u = rng.uniform(size=N)\n    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n    DM1 = (M == 1).astype(float)\n    DM2 = (M == 2).astype(float)\n    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)\n    return T, M, Y, U\n\n\ndef precomp_fd(beta, N=N_LARGE, seed=123):\n    rng = np.random.default_rng(seed)\n    T, M, Y, _ = _gen_fd(N, beta, rng)\n    DM = np.zeros((N, K))\n    for k in range(K):\n        DM[:, k] = (M == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DM=DM.mean(0),\n        E_DM_T=(DM * T[:, None]).mean(0),\n        E_DM_Y=(DM * Y[:, None]).mean(0))\n\n\ndef plim_fd(C, st):\n    ds  = C @ st['E_DM']\n    dst = C @ st['E_DM_T']\n    dsy = C @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef mc_fd(C, beta, nr=N_REPS, N=N_MC, seed=42):\n    rng = np.random.default_rng(seed)\n    out = np.zeros((nr, 4))\n    for r in range(nr):\n        T, M, Y, _ = _gen_fd(N, beta, rng)\n        Ms = gen_Astar(M, C, rng)\n        Z = np.column_stack([np.ones(N), T,\n                             (Ms == 1).astype(float),\n                             (Ms == 2).astype(float)])\n        out[r] = ols(Z, Y)\n    return out.mean(0), out.std(0) / np.sqrt(nr)\n\n\ndef rsearch_fd(st, ns=N_RANDOM, seed=999):\n    rng = np.random.default_rng(seed)\n    clean = plim_fd(np.eye(K), st)\n\n    Cs = np.zeros((ns, K, K))\n    for i in range(K):\n        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)\n\n    E_DMs   = Cs @ st['E_DM']\n    E_DMs_T = Cs @ st['E_DM_T']\n    E_DMs_Y = Cs @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n\n    EZZ = np.zeros((ns, 4, 4))\n    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = ET\n    EZZ[:, 0, 2] = EZZ[:, 2, 0] = E_DMs[:, 1]\n    EZZ[:, 0, 3] = EZZ[:, 3, 0] = E_DMs[:, 2]\n    EZZ[:, 1, 1] = ET2\n    EZZ[:, 1, 2] = EZZ[:, 2, 1] = E_DMs_T[:, 1]\n    EZZ[:, 1, 3] = EZZ[:, 3, 1] = E_DMs_T[:, 2]\n    EZZ[:, 2, 2] = E_DMs[:, 1]\n    EZZ[:, 3, 3] = E_DMs[:, 2]\n\n    EZY = np.zeros((ns, 4))\n    EZY[:, 0] = EY;   EZY[:, 1] = ETY\n    EZY[:, 2] = E_DMs_Y[:, 1]\n    EZY[:, 3] = E_DMs_Y[:, 2]\n\n    pl = np.linalg.solve(EZZ, EZY[:, :, None])[:, :, 0]\n\n    df = np.abs(pl - clean)\n    viol = np.any(df > .01, 1).mean()\n    nz = np.abs(clean) > 1e-6\n    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()\n    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()\n    return viol, sign, amp\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    t0 = time.time()\n    np.set_printoptions(precision=4, suppress=True)\n\n    for bn, beta in [(\"mixed [0,1,-0.5]\", BETA_MIXED),\n                      (\"same [0,1,0.5]\",   BETA_SAME)]:\n\n        # ---- DAG 1: Mediation ----\n        print(f\"\\n{'='*90}\")\n        print(f\"  MEDIATION: T -> A -> Y  |  beta={bn}\")\n        print(f\"{'='*90}\")\n        p0, p1 = p_cat(0, GAMMA_MED, DELTA_MED), p_cat(1, GAMMA_MED, DELTA_MED)\n        print(f\"  P(A|T=0)={fv(p0,6,3)}  P(A|T=1)={fv(p1,6,3)}  tau={TAU}\")\n        print(f\"  Coefs: [{', '.join(COEF_NAMES)}]\\n\")\n\n        hdr = f\"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt\"\n        print(hdr)\n        print(f\"  {'-'*92}\")\n\n        all_ok = True\n        for cn, C in C_DICT.items():\n            th = plim_med(C, beta, TAU)\n            mc, se = mc_med(C, beta, TAU)\n            ms, ok = fm(th, mc, se)\n            if not ok:\n                all_ok = False\n            print(f\"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}\")\n\n        status = 'ALL MATCH' if all_ok else 'MISMATCH DETECTED'\n        print(f\"  >>> {status}\")\n\n        t1 = time.time()\n        v, s, a = rsearch_med(beta, TAU)\n        t2 = time.time()\n        print(f\"\\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): \"\n              f\"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}\")\n\n        # ---- DAG 2: Front-door ----\n        print(f\"\\n{'='*90}\")\n        print(f\"  FRONT-DOOR: T -> M -> Y, U -> T, U -> Y  |  beta={bn}\")\n        print(f\"{'='*90}\")\n        print(f\"  alpha_U={ALPHA_U}  lambda_U={LAMBDA_U}\")\n        print(f\"  M|T softmax: gamma={GAMMA_FD}  delta={DELTA_FD}\")\n        print(f\"  Coefs: [{', '.join(COEF_NAMES)}]\\n\")\n\n        t1 = time.time()\n        st = precomp_fd(beta)\n        t2 = time.time()\n        print(f\"  Moments pre-computed (N={N_LARGE//10**6}M, {t2-t1:.1f}s)\\n\")\n\n        hdr = f\"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt\"\n        print(hdr)\n        print(f\"  {'-'*92}\")\n\n        all_ok = True\n        for cn, C in C_DICT.items():\n            th = plim_fd(C, st)\n            mc, se = mc_fd(C, beta)\n            ms, ok = fm(th, mc, se, k=3)\n            if not ok:\n                all_ok = False\n            print(f\"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}\")\n\n        status = 'ALL MATCH (3σ)' if all_ok else 'MISMATCH DETECTED'\n        print(f\"  >>> {status}\")\n\n        t1 = time.time()\n        v, s, a = rsearch_fd(st)\n        t2 = time.time()\n        print(f\"\\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): \"\n              f\"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}\")\n\n    print(f\"\\n{'='*90}\")\n    print(f\"  Total: {time.time()-t0:.1f}s\")\n    print(f\"{'='*90}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 386,
      "startLine": 1,
      "totalLines": 386
    }
  }
}
```

</details>

---


### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read plan_001_collider_mbias_iv.py and the plan_002 for K adaptation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "f75e61a8-6f0e-4c06-a703-cb29cc0a60a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VWmN4ARR5DWtrN8AuPcWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21700,
      "cache_read_input_tokens": 31994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21700
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

_source line 34_

Now let me read the remaining key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "ba68bdec-c023-4902-9b52-6cda5ac600c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VWmN4ARR5DWtrN8AuPcWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21700,
      "cache_read_input_tokens": 31994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21700
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01SQmaG3zdpcHJeGPGJuhtY1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "03463b0d-1009-4637-972c-8ce4b1cba99f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VWmN4ARR5DWtrN8AuPcWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21700,
      "cache_read_input_tokens": 31994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21700
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

_source line 36 · 2026-05-20T21:01:35.128Z_

<details><summary>↩ Tool result · `toolu_01SQmaG3zdpcHJeGPGJuhtY1`</summary>

```text
1	"""
2	Collider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.
3	K=3 LLM annotation error bias propagation in causal inference.
4	"""
5	
6	import numpy as np
7	from collections import OrderedDict
8	import time
9	
10	# ── Constants ────────────────────────────────────────────────────────────────
11	
12	BETA_MIXED = np.array([0.0, 1.0, -0.5])
13	BETA_SAME  = np.array([0.0, 1.0,  0.5])
14	
15	C1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
16	C2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])
17	C3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])
18	C4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])
19	C5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])
20	C6_DIFF_BASE      = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
21	
22	ALL_C = OrderedDict([
23	    ("C1_sym_high",   C1_SYMMETRIC_HIGH),
24	    ("C2_asymmetric", C2_ASYMMETRIC),
25	    ("C3_struct_12",  C3_STRUCTURAL_12),
26	    ("C4_weak_diag",  C4_WEAK_DIAG),
27	    ("C5_near_perm",  C5_NEAR_PERM),
28	    ("C6_diff_base",  C6_DIFF_BASE),
29	])
30	
31	# ── Utilities ────────────────────────────────────────────────────────────────
32	
33	def _generate_Astar(A, C, rng):
34	    probs = C[:, A]
35	    cum = np.cumsum(probs, axis=0)
36	    u = rng.uniform(size=len(A))
37	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
38	
39	
40	def _generate_Astar_fixed_u(A, C, u):
41	    probs = C[:, A]
42	    cum = np.cumsum(probs, axis=0)
43	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
44	
45	
46	def _softmax_sample(logits, rng):
47	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
48	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
49	    cum = np.cumsum(probs, axis=1)
50	    u = rng.uniform(size=logits.shape[0])
51	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
52	
53	
54	def _ols(Z, Y):
55	    return np.linalg.solve(Z.T @ Z, Z.T @ Y)
56	
57	
58	# ══════════════════════════════════════════════════════════════════════════════
59	# DAG 1: COLLIDER — T -> A <- Y
60	# ══════════════════════════════════════════════════════════════════════════════
61	
62	COLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)
63	
64	
65	def _gen_collider(N, params, rng):
66	    T = rng.normal(0, 1, N)
67	    eps = rng.normal(0, 1, N)
68	    Y = params['tau'] * T + eps
69	    logits = np.column_stack([
70	        np.zeros(N),
71	        params['g1'] + params['dT'] * T + params['dY'] * Y,
72	        params['g2'] + params['dT2'] * T + params['dY2'] * Y,
73	    ])
74	    A = _softmax_sample(logits, rng)
75	    return T, Y, A
76	
77	
78	def theory_collider(C, params, N_approx=2_000_000, seed=999):
79	    rng = np.random.default_rng(seed)
80	    T, Y, A = _gen_collider(N_approx, params, rng)
81	    Astar = _generate_Astar(A, C, rng)
82	    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
83	    ones = np.ones(N_approx)
84	    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
85	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
86	    return tau_ctrl, tau_nc
87	
88	
89	def mc_collider(C, params, N=10_000, n_reps=1000, seed=0):
90	    tau_ctrl_arr = np.empty(n_reps)
91	    tau_nc_arr = np.empty(n_reps)
92	    for r in range(n_reps):
93	        rng = np.random.default_rng(seed + r)
94	        T, Y, A = _gen_collider(N, params, rng)
95	        Astar = _generate_Astar(A, C, rng)
96	        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
97	        ones = np.ones(N)
98	        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
99	        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
100	    return tau_ctrl_arr.mean(), tau_nc_arr.mean()
101	
102	
103	# ══════════════════════════════════════════════════════════════════════════════
104	# DAG 2: M-BIAS — U1 -> {A,T}, U2 -> {A,Y}
105	# ══════════════════════════════════════════════════════════════════════════════
106	
107	MBIAS_PARAMS = dict(tau=1.0, delta=1.0, lam=1.0,
108	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
109	
110	
111	def _gen_mbias(N, params, rng):
112	    U1 = rng.normal(0, 1, N)
113	    U2 = rng.normal(0, 1, N)
114	    T = params['delta'] * U1 + rng.normal(0, 1, N)
115	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
116	    logits = np.column_stack([
117	        np.zeros(N),
118	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
119	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
120	    ])
121	    A = _softmax_sample(logits, rng)
122	    return T, Y, A
123	
124	
125	def theory_mbias(C, params, N_approx=2_000_000, seed=999):
126	    rng = np.random.default_rng(seed)
127	    T, Y, A = _gen_mbias(N_approx, params, rng)
128	    Astar = _generate_Astar(A, C, rng)
129	    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
130	    ones = np.ones(N_approx)
131	    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
132	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
133	    return tau_ctrl, tau_nc
134	
135	
136	def mc_mbias(C, params, N=10_000, n_reps=1000, seed=0):
137	    tau_ctrl_arr = np.empty(n_reps)
138	    tau_nc_arr = np.empty(n_reps)
139	    for r in range(n_reps):
140	        rng = np.random.default_rng(seed + r)
141	        T, Y, A = _gen_mbias(N, params, rng)
142	        Astar = _generate_Astar(A, C, rng)
143	        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
144	        ones = np.ones(N)
145	        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
146	        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
147	    return tau_ctrl_arr.mean(), tau_nc_arr.mean()
148	
149	
150	# ══════════════════════════════════════════════════════════════════════════════
151	# DAG 3: INSTRUMENT — Z_iv -> A -> Y, U -> {A, Y}
152	# ══════════════════════════════════════════════════════════════════════════════
153	
154	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
155	
156	
157	def _gen_iv(N, beta, params, rng):
158	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
159	    U = rng.normal(0, 1, N)
160	    eps = rng.normal(0, 1, N)
161	    logits = np.column_stack([
162	        np.zeros(N),
163	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
164	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
165	    ])
166	    A = _softmax_sample(logits, rng)
167	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
168	         + params['lam'] * U + eps)
169	    return Z_iv, U, Y, A
170	
171	
172	def theory_iv(C, beta, params, N_approx=2_000_000, seed=999):
173	    rng = np.random.default_rng(seed)
174	    Z_iv, U, Y, A = _gen_iv(N_approx, beta, params, rng)
175	    Astar = _generate_Astar(A, C, rng)
176	    z1 = Z_iv == 1
177	    z0 = Z_iv == 0
178	
179	    RF = Y[z1].mean() - Y[z0].mean()
180	
181	    result = {'RF': RF}
182	    for k in [1, 2]:
183	        fs_star = (Astar[z1] == k).mean() - (Astar[z0] == k).mean()
184	        fs_true = (A[z1] == k).mean() - (A[z0] == k).mean()
185	        result[f'FS{k}_star'] = fs_star
186	        result[f'FS{k}_true'] = fs_true
187	        result[f'Wald{k}_star'] = RF / fs_star if abs(fs_star) > 1e-8 else np.nan
188	        result[f'Wald{k}_true'] = RF / fs_true if abs(fs_true) > 1e-8 else np.nan
189	
190	    ones = np.ones(N_approx)
191	    X_star = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
192	    result['ols_star'] = _ols(X_star, Y)
193	    X_true = np.column_stack([ones, (A == 1).astype(float), (A == 2).astype(float)])
194	    result['ols_true'] = _ols(X_true, Y)
195	
196	    return result
197	
198	
199	def mc_iv(C, beta, params, N=10_000, n_reps=1000, seed=0):
200	    RF_arr = np.empty(n_reps)
201	    FS1_arr = np.empty(n_reps)
202	    FS2_arr = np.empty(n_reps)
203	    ols_arr = np.empty((n_reps, 3))
204	    for r in range(n_reps):
205	        rng = np.random.default_rng(seed + r)
206	        Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
207	        Astar = _generate_Astar(A, C, rng)
208	        z1 = Z_iv == 1
209	        z0 = Z_iv == 0
210	        RF_arr[r] = Y[z1].mean() - Y[z0].mean()
211	        FS1_arr[r] = (Astar[z1] == 1).mean() - (Astar[z0] == 1).mean()
212	        FS2_arr[r] = (Astar[z1] == 2).mean() - (Astar[z0] == 2).mean()
213	        ones = np.ones(N)
214	        X = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
215	        ols_arr[r] = _ols(X, Y)
216	
217	    wald1_mc = RF_arr.mean() / FS1_arr.mean()
218	    wald2_mc = RF_arr.mean() / FS2_arr.mean()
219	    ols_mc = ols_arr.mean(axis=0)
220	    return wald1_mc, wald2_mc, ols_mc
221	
222	
223	# ══════════════════════════════════════════════════════════════════════════════
224	# RANDOM C SEARCH (reuse base dataset, vary only C)
225	# ══════════════════════════════════════════════════════════════════════════════
226	
227	def _fast_ols_tau(T, Y, A_star, N, sT, sTT, sY, sTY):
228	    """Inline OLS for Y ~ 1 + T + D1 + D2, returns coef on T. Avoids column_stack."""
229	    m1 = A_star == 1
230	    m2 = A_star == 2
231	    n1 = float(m1.sum())
232	    n2 = float(m2.sum())
233	    tD1 = T[m1].sum()
234	    tD2 = T[m2].sum()
235	    yD1 = Y[m1].sum()
236	    yD2 = Y[m2].sum()
237	    ZZ = np.array([[N, sT, n1, n2],
238	                   [sT, sTT, tD1, tD2],
239	                   [n1, tD1, n1, 0.0],
240	                   [n2, tD2, 0.0, n2]])
241	    ZY = np.array([sY, sTY, yD1, yD2])
242	    return np.linalg.solve(ZZ, ZY)[1]
243	
244	
245	def rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):
246	    rng = np.random.default_rng(seed)
247	    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)
248	    u = rng.uniform(size=N_ap)
249	    N = float(N_ap)
250	    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
251	    tau_nc = sTY / sTT - sT * sY / (N * sTT)  # simplified no-control
252	    ones = np.ones(N_ap)
253	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
254	
255	    rng_s = np.random.default_rng(seed + 1)
256	    biases = np.empty(n_search)
257	    for i in range(n_search):
258	        C = rng_s.dirichlet([1, 1, 1], size=3).T
259	        Astar = _generate_Astar_fixed_u(A, C, u)
260	        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - COLLIDER_PARAMS['tau']
261	    return biases, tau_nc - COLLIDER_PARAMS['tau']
262	
263	
264	def rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):
265	    rng = np.random.default_rng(seed)
266	    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)
267	    u = rng.uniform(size=N_ap)
268	    N = float(N_ap)
269	    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
270	    ones = np.ones(N_ap)
271	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
272	
273	    rng_s = np.random.default_rng(seed + 1)
274	    biases = np.empty(n_search)
275	    for i in range(n_search):
276	        C = rng_s.dirichlet([1, 1, 1], size=3).T
277	        Astar = _generate_Astar_fixed_u(A, C, u)
278	        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - MBIAS_PARAMS['tau']
279	    return biases, tau_nc - MBIAS_PARAMS['tau']
280	
281	
282	def rand_search_iv(beta, n_search=100_000, N_ap=50_000, seed=42):
283	    rng = np.random.default_rng(seed)
284	    Z_iv, U, Y, A = _gen_iv(N_ap, beta, IV_PARAMS, rng)
285	    u = rng.uniform(size=N_ap)
286	    z1 = Z_iv == 1
287	    z0 = Z_iv == 0
288	    n1_z = float(z1.sum())
289	    n0_z = float(z0.sum())
290	    RF = Y[z1].sum() / n1_z - Y[z0].sum() / n0_z
291	    FS1_true = (A[z1] == 1).sum() / n1_z - (A[z0] == 1).sum() / n0_z
292	    FS2_true = (A[z1] == 2).sum() / n1_z - (A[z0] == 2).sum() / n0_z
293	    W1_true = RF / FS1_true if abs(FS1_true) > 1e-8 else np.nan
294	    W2_true = RF / FS2_true if abs(FS2_true) > 1e-8 else np.nan
295	
296	    rng_s = np.random.default_rng(seed + 1)
297	    w1_vals = np.empty(n_search)
298	    w2_vals = np.empty(n_search)
299	    for i in range(n_search):
300	        C = rng_s.dirichlet([1, 1, 1], size=3).T
301	        Astar = _generate_Astar_fixed_u(A, C, u)
302	        fs1 = (Astar[z1] == 1).sum() / n1_z - (Astar[z0] == 1).sum() / n0_z
303	        fs2 = (Astar[z1] == 2).sum() / n1_z - (Astar[z0] == 2).sum() / n0_z
304	        w1_vals[i] = RF / fs1 if abs(fs1) > 1e-8 else np.nan
305	        w2_vals[i] = RF / fs2 if abs(fs2) > 1e-8 else np.nan
306	    return w1_vals, w2_vals, W1_true, W2_true
307	
308	
309	# ══════════════════════════════════════════════════════════════════════════════
310	# MAIN
311	# ══════════════════════════════════════════════════════════════════════════════
312	
313	def _print_section(title):
314	    print()
315	    print("=" * 80)
316	    print(title)
317	    print("=" * 80)
318	
319	
320	def main():
321	    np.set_printoptions(precision=6, suppress=True)
322	    t0 = time.time()
323	
324	    # ── DAG 1: Collider ─────────────────────────────────────────────────────
325	    _print_section("DAG 1: COLLIDER -- T -> A <- Y")
326	    p = COLLIDER_PARAMS
327	    print(f"DGP: T~N(0,1), Y={p['tau']}*T+eps, "
328	          f"A|T,Y softmax(dT={p['dT']}, dY={p['dY']}, dT2={p['dT2']}, dY2={p['dY2']})")
329	    print(f"Researcher error: controls A* in Y ~ 1 + T + D*1 + D*2")
330	    print(f"Truth: T and Y are NOT confounded => no-control OLS is consistent")
331	    print()
332	
333	    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
334	           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
335	    print(hdr)
336	    print("  " + "-" * 80)
337	
338	    for cn, C in ALL_C.items():
339	        th_c, th_n = theory_collider(C, p)
340	        mc_c, mc_n = mc_collider(C, p)
341	        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
342	        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
343	              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")
344	
345	    print()
346	    print("Violation analysis:")
347	    th_c1, th_n1 = theory_collider(C1_SYMMETRIC_HIGH, p)
348	    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
349	          f" (should = tau={p['tau']} since no confounding)")
350	    print(f"  Controlling collider A* induces spurious T-eps association")
351	
352	    t1 = time.time()
353	    print(f"\nRandom C search (100k)... ", end="", flush=True)
354	    bc, bnc = rand_search_collider()
355	    print(f"done ({time.time()-t1:.0f}s)")
356	    print(f"  No-control bias: {bnc:+.4f}")
357	    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
358	          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
359	    worse = np.sum(np.abs(bc) > np.abs(bnc))
360	    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")
361	
362	    # ── DAG 2: M-bias ───────────────────────────────────────────────────────
363	    _print_section("DAG 2: M-BIAS -- U1 -> {A,T}, U2 -> {A,Y}")
364	    p = MBIAS_PARAMS
365	    print(f"DGP: U1,U2~N(0,1) indep, T={p['delta']}*U1+eta,"
366	          f" Y={p['tau']}*T+{p['lam']}*U2+eps")
367	    print(f"A|U1,U2 softmax(a1={p['a1']}, a2={p['a2']}, a3={p['a3']}, a4={p['a4']})")
368	    print(f"Researcher error: controls A* => opens U1->A<-U2 path (M-bias)")
369	    print(f"Truth: U2 indep T => no confounding of T->Y, no-control is consistent")
370	    print()
371	
372	    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
373	           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
374	    print(hdr)
375	    print("  " + "-" * 80)
376	
377	    for cn, C in ALL_C.items():
378	        th_c, th_n = theory_mbias(C, p)
379	        mc_c, mc_n = mc_mbias(C, p)
380	        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
381	        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
382	              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")
383	
384	    print()
385	    print("Violation analysis:")
386	    th_c1, th_n1 = theory_mbias(C1_SYMMETRIC_HIGH, p)
387	    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
388	          f" (should = tau={p['tau']} since U2 indep T)")
389	    print(f"  Controlling A* opens M-bias path: T <- U1 -> A <- U2 -> Y")
390	
391	    t1 = time.time()
392	    print(f"\nRandom C search (100k)... ", end="", flush=True)
393	    bc, bnc = rand_search_mbias()
394	    print(f"done ({time.time()-t1:.0f}s)")
395	    print(f"  No-control bias: {bnc:+.4f}")
396	    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
397	          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
398	    worse = np.sum(np.abs(bc) > np.abs(bnc))
399	    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")
400	
401	    # ── DAG 3: Instrument ────────────────────────────────────────────────────
402	    for bname, beta in [("BETA_MIXED", BETA_MIXED), ("BETA_SAME", BETA_SAME)]:
403	        _print_section(
404	            f"DAG 3: INSTRUMENT -- Z->A->Y, U->{{A,Y}}  [{bname}: b={beta}]")
405	        p = IV_PARAMS
406	        print(f"DGP: Z~Bern(0.5), U~N(0,1), Y=b1*D1+b2*D2+{p['lam']}*U+eps")
407	        print(f"A|Z,U softmax(dZ={p['dZ']}, dU={p['dU']}, dZ2={p['dZ2']}, dU2={p['dU2']})")
408	        print(f"Under-identified: 1 IV for 2 endogenous dummies => per-dummy Wald")
409	        print(f"Wald_k = RF/FS*_k estimates (b1*pi1+b2*pi2)/pi*_k, not b_k")
410	        print()
411	
412	        hdr2 = (f"  {'C':<16}"
413	                f" {'W1* th':>8} {'W1* mc':>8} {'ok':>3}"
414	                f" {'W2* th':>8} {'W2* mc':>8} {'ok':>3}"
415	                f" {'OLS b1':>8} {'mc':>8} {'ok':>3}"
416	                f" {'OLS b2':>8} {'mc':>8} {'ok':>3}")
417	        print(hdr2)
418	        print("  " + "-" * 110)
419	
420	        for cn, C in ALL_C.items():
421	            th = theory_iv(C, beta, p)
422	            mc_w1, mc_w2, mc_ols = mc_iv(C, beta, p)
423	
424	            o1 = "Y" if abs(th['Wald1_star'] - mc_w1) < 0.10 else "N"
425	            o2 = "Y" if abs(th['Wald2_star'] - mc_w2) < 0.10 else "N"
426	            o3 = "Y" if abs(th['ols_star'][1] - mc_ols[1]) < 0.02 else "N"
427	            o4 = "Y" if abs(th['ols_star'][2] - mc_ols[2]) < 0.02 else "N"
428	
429	            def _fmt(v, w=8):
430	                return f"{v:>{w}.4f}" if np.isfinite(v) else f"{'nan':>{w}}"
431	
432	            print(f"  {cn:<16}"
433	                  f" {_fmt(th['Wald1_star'])} {_fmt(mc_w1)} {o1:>3}"
434	                  f" {_fmt(th['Wald2_star'])} {_fmt(mc_w2)} {o2:>3}"
435	                  f" {th['ols_star'][1]:>8.4f} {mc_ols[1]:>8.4f} {o3:>3}"
436	                  f" {th['ols_star'][2]:>8.4f} {mc_ols[2]:>8.4f} {o4:>3}")
437	
438	        print()
439	        th1 = theory_iv(C1_SYMMETRIC_HIGH, beta, p)
440	        print("Violation analysis (C1_sym_high):")
441	        print(f"  True beta = [{beta[1]}, {beta[2]}]")
442	        print(f"  Reduced form (ITT): {th1['RF']:.4f}")
443	        print(f"  First stage true:  pi1={th1['FS1_true']:.4f}, pi2={th1['FS2_true']:.4f}")
444	        print(f"  First stage A*:    pi*1={th1['FS1_star']:.4f}, pi*2={th1['FS2_star']:.4f}")
445	        print(f"  Wald true A:  W1={th1['Wald1_true']:.4f}, W2={th1['Wald2_true']:.4f}")
446	        print(f"  Wald A*:      W1={th1['Wald1_star']:.4f}, W2={th1['Wald2_star']:.4f}")
447	        print(f"  OLS true A:   [{th1['ols_true'][1]:.4f}, {th1['ols_true'][2]:.4f}]"
448	              f" (biased by U)")
449	        print(f"  OLS A*:       [{th1['ols_star'][1]:.4f}, {th1['ols_star'][2]:.4f}]"
450	              f" (biased by U + misclassification)")
451	
452	        # Analytical insight: how C transforms first stages
453	        print(f"\n  FS transformation by C:")
454	        print(f"    FS*_k = sum_j C[k,j] * FS_j")
455	        for cn2, C2 in [("C1_sym_high", C1_SYMMETRIC_HIGH),
456	                        ("C4_weak_diag", C4_WEAK_DIAG),
457	                        ("C5_near_perm", C5_NEAR_PERM)]:
458	            th2 = theory_iv(C2, beta, p)
459	            fs_true = np.array([-(th2['FS1_true']+th2['FS2_true']),
460	                                th2['FS1_true'], th2['FS2_true']])
461	            fs_star_calc = C2 @ fs_true
462	            print(f"    {cn2}: FS_true={fs_true}, C@FS={fs_star_calc},"
463	                  f" FS*=[{th2['FS1_star']:.4f}, {th2['FS2_star']:.4f}]")
464	
465	        t1 = time.time()
466	        print(f"\n  Random C search (100k)... ", end="", flush=True)
467	        w1v, w2v, w1t, w2t = rand_search_iv(beta)
468	        print(f"done ({time.time()-t1:.0f}s)")
469	        v1 = np.isfinite(w1v)
470	        v2 = np.isfinite(w2v)
471	        w1b = w1v - w1t
472	        w2b = w2v - w2t
473	        print(f"    Wald1 true={w1t:.4f}: A* vals mean={np.nanmean(w1v):+.4f},"
474	              f" std={np.nanstd(w1v):.4f},"
475	              f" range=[{np.nanmin(w1v):+.4f}, {np.nanmax(w1v):+.4f}],"
476	              f" valid={v1.sum()}/{len(w1v)}")
477	        print(f"    Wald2 true={w2t:.4f}: A* vals mean={np.nanmean(w2v):+.4f},"
478	              f" std={np.nanstd(w2v):.4f},"
479	              f" range=[{np.nanmin(w2v):+.4f}, {np.nanmax(w2v):+.4f}],"
480	              f" valid={v2.sum()}/{len(w2v)}")
481	        print(f"    Delta from true: W1 mean={np.nanmean(w1b):+.4f},"
482	              f" W2 mean={np.nanmean(w2b):+.4f}")
483	
484	    print(f"\nTotal: {time.time() - t0:.1f}s")
485	
486	
487	if __name__ == "__main__":
488	    main()
489	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "a1ff3b90-0553-4fae-b041-7dd572a52ec6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py",
      "content": "\"\"\"\nCollider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.\nK=3 LLM annotation error bias propagation in causal inference.\n\"\"\"\n\nimport numpy as np\nfrom collections import OrderedDict\nimport time\n\n# ── Constants ────────────────────────────────────────────────────────────────\n\nBETA_MIXED = np.array([0.0, 1.0, -0.5])\nBETA_SAME  = np.array([0.0, 1.0,  0.5])\n\nC1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])\nC2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])\nC3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])\nC4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])\nC5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])\nC6_DIFF_BASE      = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])\n\nALL_C = OrderedDict([\n    (\"C1_sym_high\",   C1_SYMMETRIC_HIGH),\n    (\"C2_asymmetric\", C2_ASYMMETRIC),\n    (\"C3_struct_12\",  C3_STRUCTURAL_12),\n    (\"C4_weak_diag\",  C4_WEAK_DIAG),\n    (\"C5_near_perm\",  C5_NEAR_PERM),\n    (\"C6_diff_base\",  C6_DIFF_BASE),\n])\n\n# ── Utilities ────────────────────────────────────────────────────────────────\n\ndef _generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef _generate_Astar_fixed_u(A, C, u):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef _softmax_sample(logits, rng):\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\n\n\ndef _ols(Z, Y):\n    return np.linalg.solve(Z.T @ Z, Z.T @ Y)\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# DAG 1: COLLIDER — T -> A <- Y\n# ══════════════════════════════════════════════════════════════════════════════\n\nCOLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)\n\n\ndef _gen_collider(N, params, rng):\n    T = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    Y = params['tau'] * T + eps\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\n    ])\n    A = _softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef theory_collider(C, params, N_approx=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_collider(N_approx, params, rng)\n    Astar = _generate_Astar(A, C, rng)\n    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n    ones = np.ones(N_approx)\n    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl, tau_nc\n\n\ndef mc_collider(C, params, N=10_000, n_reps=1000, seed=0):\n    tau_ctrl_arr = np.empty(n_reps)\n    tau_nc_arr = np.empty(n_reps)\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        T, Y, A = _gen_collider(N, params, rng)\n        Astar = _generate_Astar(A, C, rng)\n        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n        ones = np.ones(N)\n        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl_arr.mean(), tau_nc_arr.mean()\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# DAG 2: M-BIAS — U1 -> {A,T}, U2 -> {A,Y}\n# ══════════════════════════════════════════════════════════════════════════════\n\nMBIAS_PARAMS = dict(tau=1.0, delta=1.0, lam=1.0,\n                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)\n\n\ndef _gen_mbias(N, params, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = params['delta'] * U1 + rng.normal(0, 1, N)\n    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['a1'] * U1 + params['a2'] * U2,\n        params['g2'] + params['a3'] * U1 + params['a4'] * U2,\n    ])\n    A = _softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef theory_mbias(C, params, N_approx=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N_approx, params, rng)\n    Astar = _generate_Astar(A, C, rng)\n    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n    ones = np.ones(N_approx)\n    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl, tau_nc\n\n\ndef mc_mbias(C, params, N=10_000, n_reps=1000, seed=0):\n    tau_ctrl_arr = np.empty(n_reps)\n    tau_nc_arr = np.empty(n_reps)\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        T, Y, A = _gen_mbias(N, params, rng)\n        Astar = _generate_Astar(A, C, rng)\n        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n        ones = np.ones(N)\n        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl_arr.mean(), tau_nc_arr.mean()\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# DAG 3: INSTRUMENT — Z_iv -> A -> Y, U -> {A, Y}\n# ══════════════════════════════════════════════════════════════════════════════\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _gen_iv(N, beta, params, rng):\n    Z_iv = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,\n    ])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + eps)\n    return Z_iv, U, Y, A\n\n\ndef theory_iv(C, beta, params, N_approx=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N_approx, beta, params, rng)\n    Astar = _generate_Astar(A, C, rng)\n    z1 = Z_iv == 1\n    z0 = Z_iv == 0\n\n    RF = Y[z1].mean() - Y[z0].mean()\n\n    result = {'RF': RF}\n    for k in [1, 2]:\n        fs_star = (Astar[z1] == k).mean() - (Astar[z0] == k).mean()\n        fs_true = (A[z1] == k).mean() - (A[z0] == k).mean()\n        result[f'FS{k}_star'] = fs_star\n        result[f'FS{k}_true'] = fs_true\n        result[f'Wald{k}_star'] = RF / fs_star if abs(fs_star) > 1e-8 else np.nan\n        result[f'Wald{k}_true'] = RF / fs_true if abs(fs_true) > 1e-8 else np.nan\n\n    ones = np.ones(N_approx)\n    X_star = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])\n    result['ols_star'] = _ols(X_star, Y)\n    X_true = np.column_stack([ones, (A == 1).astype(float), (A == 2).astype(float)])\n    result['ols_true'] = _ols(X_true, Y)\n\n    return result\n\n\ndef mc_iv(C, beta, params, N=10_000, n_reps=1000, seed=0):\n    RF_arr = np.empty(n_reps)\n    FS1_arr = np.empty(n_reps)\n    FS2_arr = np.empty(n_reps)\n    ols_arr = np.empty((n_reps, 3))\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n        Astar = _generate_Astar(A, C, rng)\n        z1 = Z_iv == 1\n        z0 = Z_iv == 0\n        RF_arr[r] = Y[z1].mean() - Y[z0].mean()\n        FS1_arr[r] = (Astar[z1] == 1).mean() - (Astar[z0] == 1).mean()\n        FS2_arr[r] = (Astar[z1] == 2).mean() - (Astar[z0] == 2).mean()\n        ones = np.ones(N)\n        X = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])\n        ols_arr[r] = _ols(X, Y)\n\n    wald1_mc = RF_arr.mean() / FS1_arr.mean()\n    wald2_mc = RF_arr.mean() / FS2_arr.mean()\n    ols_mc = ols_arr.mean(axis=0)\n    return wald1_mc, wald2_mc, ols_mc\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# RANDOM C SEARCH (reuse base dataset, vary only C)\n# ══════════════════════════════════════════════════════════════════════════════\n\ndef _fast_ols_tau(T, Y, A_star, N, sT, sTT, sY, sTY):\n    \"\"\"Inline OLS for Y ~ 1 + T + D1 + D2, returns coef on T. Avoids column_stack.\"\"\"\n    m1 = A_star == 1\n    m2 = A_star == 2\n    n1 = float(m1.sum())\n    n2 = float(m2.sum())\n    tD1 = T[m1].sum()\n    tD2 = T[m2].sum()\n    yD1 = Y[m1].sum()\n    yD2 = Y[m2].sum()\n    ZZ = np.array([[N, sT, n1, n2],\n                   [sT, sTT, tD1, tD2],\n                   [n1, tD1, n1, 0.0],\n                   [n2, tD2, 0.0, n2]])\n    ZY = np.array([sY, sTY, yD1, yD2])\n    return np.linalg.solve(ZZ, ZY)[1]\n\n\ndef rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)\n    u = rng.uniform(size=N_ap)\n    N = float(N_ap)\n    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()\n    tau_nc = sTY / sTT - sT * sY / (N * sTT)  # simplified no-control\n    ones = np.ones(N_ap)\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n\n    rng_s = np.random.default_rng(seed + 1)\n    biases = np.empty(n_search)\n    for i in range(n_search):\n        C = rng_s.dirichlet([1, 1, 1], size=3).T\n        Astar = _generate_Astar_fixed_u(A, C, u)\n        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - COLLIDER_PARAMS['tau']\n    return biases, tau_nc - COLLIDER_PARAMS['tau']\n\n\ndef rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)\n    u = rng.uniform(size=N_ap)\n    N = float(N_ap)\n    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()\n    ones = np.ones(N_ap)\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n\n    rng_s = np.random.default_rng(seed + 1)\n    biases = np.empty(n_search)\n    for i in range(n_search):\n        C = rng_s.dirichlet([1, 1, 1], size=3).T\n        Astar = _generate_Astar_fixed_u(A, C, u)\n        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - MBIAS_PARAMS['tau']\n    return biases, tau_nc - MBIAS_PARAMS['tau']\n\n\ndef rand_search_iv(beta, n_search=100_000, N_ap=50_000, seed=42):\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N_ap, beta, IV_PARAMS, rng)\n    u = rng.uniform(size=N_ap)\n    z1 = Z_iv == 1\n    z0 = Z_iv == 0\n    n1_z = float(z1.sum())\n    n0_z = float(z0.sum())\n    RF = Y[z1].sum() / n1_z - Y[z0].sum() / n0_z\n    FS1_true = (A[z1] == 1).sum() / n1_z - (A[z0] == 1).sum() / n0_z\n    FS2_true = (A[z1] == 2).sum() / n1_z - (A[z0] == 2).sum() / n0_z\n    W1_true = RF / FS1_true if abs(FS1_true) > 1e-8 else np.nan\n    W2_true = RF / FS2_true if abs(FS2_true) > 1e-8 else np.nan\n\n    rng_s = np.random.default_rng(seed + 1)\n    w1_vals = np.empty(n_search)\n    w2_vals = np.empty(n_search)\n    for i in range(n_search):\n        C = rng_s.dirichlet([1, 1, 1], size=3).T\n        Astar = _generate_Astar_fixed_u(A, C, u)\n        fs1 = (Astar[z1] == 1).sum() / n1_z - (Astar[z0] == 1).sum() / n0_z\n        fs2 = (Astar[z1] == 2).sum() / n1_z - (Astar[z0] == 2).sum() / n0_z\n        w1_vals[i] = RF / fs1 if abs(fs1) > 1e-8 else np.nan\n        w2_vals[i] = RF / fs2 if abs(fs2) > 1e-8 else np.nan\n    return w1_vals, w2_vals, W1_true, W2_true\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# MAIN\n# ══════════════════════════════════════════════════════════════════════════════\n\ndef _print_section(title):\n    print()\n    print(\"=\" * 80)\n    print(title)\n    print(\"=\" * 80)\n\n\ndef main():\n    np.set_printoptions(precision=6, suppress=True)\n    t0 = time.time()\n\n    # ── DAG 1: Collider ─────────────────────────────────────────────────────\n    _print_section(\"DAG 1: COLLIDER -- T -> A <- Y\")\n    p = COLLIDER_PARAMS\n    print(f\"DGP: T~N(0,1), Y={p['tau']}*T+eps, \"\n          f\"A|T,Y softmax(dT={p['dT']}, dY={p['dY']}, dT2={p['dT2']}, dY2={p['dY2']})\")\n    print(f\"Researcher error: controls A* in Y ~ 1 + T + D*1 + D*2\")\n    print(f\"Truth: T and Y are NOT confounded => no-control OLS is consistent\")\n    print()\n\n    hdr = (f\"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}\"\n           f\" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}\")\n    print(hdr)\n    print(\"  \" + \"-\" * 80)\n\n    for cn, C in ALL_C.items():\n        th_c, th_n = theory_collider(C, p)\n        mc_c, mc_n = mc_collider(C, p)\n        ok = \"Y\" if abs(th_c - mc_c) < 0.02 else \"N\"\n        print(f\"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}\"\n              f\" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}\")\n\n    print()\n    print(\"Violation analysis:\")\n    th_c1, th_n1 = theory_collider(C1_SYMMETRIC_HIGH, p)\n    print(f\"  No-control plim(tau_hat) = {th_n1:.4f}\"\n          f\" (should = tau={p['tau']} since no confounding)\")\n    print(f\"  Controlling collider A* induces spurious T-eps association\")\n\n    t1 = time.time()\n    print(f\"\\nRandom C search (100k)... \", end=\"\", flush=True)\n    bc, bnc = rand_search_collider()\n    print(f\"done ({time.time()-t1:.0f}s)\")\n    print(f\"  No-control bias: {bnc:+.4f}\")\n    print(f\"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},\"\n          f\" range=[{bc.min():+.4f}, {bc.max():+.4f}]\")\n    worse = np.sum(np.abs(bc) > np.abs(bnc))\n    print(f\"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)\")\n\n    # ── DAG 2: M-bias ───────────────────────────────────────────────────────\n    _print_section(\"DAG 2: M-BIAS -- U1 -> {A,T}, U2 -> {A,Y}\")\n    p = MBIAS_PARAMS\n    print(f\"DGP: U1,U2~N(0,1) indep, T={p['delta']}*U1+eta,\"\n          f\" Y={p['tau']}*T+{p['lam']}*U2+eps\")\n    print(f\"A|U1,U2 softmax(a1={p['a1']}, a2={p['a2']}, a3={p['a3']}, a4={p['a4']})\")\n    print(f\"Researcher error: controls A* => opens U1->A<-U2 path (M-bias)\")\n    print(f\"Truth: U2 indep T => no confounding of T->Y, no-control is consistent\")\n    print()\n\n    hdr = (f\"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}\"\n           f\" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}\")\n    print(hdr)\n    print(\"  \" + \"-\" * 80)\n\n    for cn, C in ALL_C.items():\n        th_c, th_n = theory_mbias(C, p)\n        mc_c, mc_n = mc_mbias(C, p)\n        ok = \"Y\" if abs(th_c - mc_c) < 0.02 else \"N\"\n        print(f\"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}\"\n              f\" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}\")\n\n    print()\n    print(\"Violation analysis:\")\n    th_c1, th_n1 = theory_mbias(C1_SYMMETRIC_HIGH, p)\n    print(f\"  No-control plim(tau_hat) = {th_n1:.4f}\"\n          f\" (should = tau={p['tau']} since U2 indep T)\")\n    print(f\"  Controlling A* opens M-bias path: T <- U1 -> A <- U2 -> Y\")\n\n    t1 = time.time()\n    print(f\"\\nRandom C search (100k)... \", end=\"\", flush=True)\n    bc, bnc = rand_search_mbias()\n    print(f\"done ({time.time()-t1:.0f}s)\")\n    print(f\"  No-control bias: {bnc:+.4f}\")\n    print(f\"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},\"\n          f\" range=[{bc.min():+.4f}, {bc.max():+.4f}]\")\n    worse = np.sum(np.abs(bc) > np.abs(bnc))\n    print(f\"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)\")\n\n    # ── DAG 3: Instrument ────────────────────────────────────────────────────\n    for bname, beta in [(\"BETA_MIXED\", BETA_MIXED), (\"BETA_SAME\", BETA_SAME)]:\n        _print_section(\n            f\"DAG 3: INSTRUMENT -- Z->A->Y, U->{{A,Y}}  [{bname}: b={beta}]\")\n        p = IV_PARAMS\n        print(f\"DGP: Z~Bern(0.5), U~N(0,1), Y=b1*D1+b2*D2+{p['lam']}*U+eps\")\n        print(f\"A|Z,U softmax(dZ={p['dZ']}, dU={p['dU']}, dZ2={p['dZ2']}, dU2={p['dU2']})\")\n        print(f\"Under-identified: 1 IV for 2 endogenous dummies => per-dummy Wald\")\n        print(f\"Wald_k = RF/FS*_k estimates (b1*pi1+b2*pi2)/pi*_k, not b_k\")\n        print()\n\n        hdr2 = (f\"  {'C':<16}\"\n                f\" {'W1* th':>8} {'W1* mc':>8} {'ok':>3}\"\n                f\" {'W2* th':>8} {'W2* mc':>8} {'ok':>3}\"\n                f\" {'OLS b1':>8} {'mc':>8} {'ok':>3}\"\n                f\" {'OLS b2':>8} {'mc':>8} {'ok':>3}\")\n        print(hdr2)\n        print(\"  \" + \"-\" * 110)\n\n        for cn, C in ALL_C.items():\n            th = theory_iv(C, beta, p)\n            mc_w1, mc_w2, mc_ols = mc_iv(C, beta, p)\n\n            o1 = \"Y\" if abs(th['Wald1_star'] - mc_w1) < 0.10 else \"N\"\n            o2 = \"Y\" if abs(th['Wald2_star'] - mc_w2) < 0.10 else \"N\"\n            o3 = \"Y\" if abs(th['ols_star'][1] - mc_ols[1]) < 0.02 else \"N\"\n            o4 = \"Y\" if abs(th['ols_star'][2] - mc_ols[2]) < 0.02 else \"N\"\n\n            def _fmt(v, w=8):\n                return f\"{v:>{w}.4f}\" if np.isfinite(v) else f\"{'nan':>{w}}\"\n\n            print(f\"  {cn:<16}\"\n                  f\" {_fmt(th['Wald1_star'])} {_fmt(mc_w1)} {o1:>3}\"\n                  f\" {_fmt(th['Wald2_star'])} {_fmt(mc_w2)} {o2:>3}\"\n                  f\" {th['ols_star'][1]:>8.4f} {mc_ols[1]:>8.4f} {o3:>3}\"\n                  f\" {th['ols_star'][2]:>8.4f} {mc_ols[2]:>8.4f} {o4:>3}\")\n\n        print()\n        th1 = theory_iv(C1_SYMMETRIC_HIGH, beta, p)\n        print(\"Violation analysis (C1_sym_high):\")\n        print(f\"  True beta = [{beta[1]}, {beta[2]}]\")\n        print(f\"  Reduced form (ITT): {th1['RF']:.4f}\")\n        print(f\"  First stage true:  pi1={th1['FS1_true']:.4f}, pi2={th1['FS2_true']:.4f}\")\n        print(f\"  First stage A*:    pi*1={th1['FS1_star']:.4f}, pi*2={th1['FS2_star']:.4f}\")\n        print(f\"  Wald true A:  W1={th1['Wald1_true']:.4f}, W2={th1['Wald2_true']:.4f}\")\n        print(f\"  Wald A*:      W1={th1['Wald1_star']:.4f}, W2={th1['Wald2_star']:.4f}\")\n        print(f\"  OLS true A:   [{th1['ols_true'][1]:.4f}, {th1['ols_true'][2]:.4f}]\"\n              f\" (biased by U)\")\n        print(f\"  OLS A*:       [{th1['ols_star'][1]:.4f}, {th1['ols_star'][2]:.4f}]\"\n              f\" (biased by U + misclassification)\")\n\n        # Analytical insight: how C transforms first stages\n        print(f\"\\n  FS transformation by C:\")\n        print(f\"    FS*_k = sum_j C[k,j] * FS_j\")\n        for cn2, C2 in [(\"C1_sym_high\", C1_SYMMETRIC_HIGH),\n                        (\"C4_weak_diag\", C4_WEAK_DIAG),\n                        (\"C5_near_perm\", C5_NEAR_PERM)]:\n            th2 = theory_iv(C2, beta, p)\n            fs_true = np.array([-(th2['FS1_true']+th2['FS2_true']),\n                                th2['FS1_true'], th2['FS2_true']])\n            fs_star_calc = C2 @ fs_true\n            print(f\"    {cn2}: FS_true={fs_true}, C@FS={fs_star_calc},\"\n                  f\" FS*=[{th2['FS1_star']:.4f}, {th2['FS2_star']:.4f}]\")\n\n        t1 = time.time()\n        print(f\"\\n  Random C search (100k)... \", end=\"\", flush=True)\n        w1v, w2v, w1t, w2t = rand_search_iv(beta)\n        print(f\"done ({time.time()-t1:.0f}s)\")\n        v1 = np.isfinite(w1v)\n        v2 = np.isfinite(w2v)\n        w1b = w1v - w1t\n        w2b = w2v - w2t\n        print(f\"    Wald1 true={w1t:.4f}: A* vals mean={np.nanmean(w1v):+.4f},\"\n              f\" std={np.nanstd(w1v):.4f},\"\n              f\" range=[{np.nanmin(w1v):+.4f}, {np.nanmax(w1v):+.4f}],\"\n              f\" valid={v1.sum()}/{len(w1v)}\")\n        print(f\"    Wald2 true={w2t:.4f}: A* vals mean={np.nanmean(w2v):+.4f},\"\n              f\" std={np.nanstd(w2v):.4f},\"\n              f\" range=[{np.nanmin(w2v):+.4f}, {np.nanmax(w2v):+.4f}],\"\n              f\" valid={v2.sum()}/{len(w2v)}\")\n        print(f\"    Delta from true: W1 mean={np.nanmean(w1b):+.4f},\"\n              f\" W2 mean={np.nanmean(w2b):+.4f}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 489,
      "startLine": 1,
      "totalLines": 489
    }
  }
}
```

</details>

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_0168tzxFyVawoA5bZrFthQyi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "499e8f80-ba30-4172-bca3-8df4bb31e39e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VWmN4ARR5DWtrN8AuPcWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21700,
      "cache_read_input_tokens": 31994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21700
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

_source line 38 · 2026-05-20T21:01:35.726Z_

<details><summary>↩ Tool result · `toolu_0168tzxFyVawoA5bZrFthQyi`</summary>

```text
1	#!/usr/bin/env python3
2	# -*- coding: utf-8 -*-
3	"""
4	Plan 002: K={3,5,7} Bias Taxonomy Extension
5	
6	Extends plan_001's K=3 bias analysis to general K across 4 core DAG topologies.
7	For each topology x K, generates 100k random K×K confusion matrices (Dirichlet),
8	computes plim via pre-computed sufficient statistics, and reports violation/sign-flip/
9	amplification rates. Includes eigendecomposition, worst-case bounds, and sensitivity
10	heatmaps as interpretability tools.
11	
12	Input:  DGP parameters per topology (auto-generated for each K)
13	Output: Cross-K comparison tables, sensitivity heatmaps (PNG)
14	
15	Dependencies: torch (GPU), numpy, matplotlib
16	"""
17	
18	import torch
19	import numpy as np
20	import matplotlib
21	matplotlib.use('Agg')
22	import matplotlib.pyplot as plt
23	import time
24	import os
25	import sys
26	
27	# ================================================================
28	# Configuration
29	# ================================================================
30	K_VALUES = [3, 5, 7]
31	N_RANDOM = 100_000
32	N_LARGE = 5_000_000
33	SEED = 42
34	DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
35	DTYPE = torch.float64
36	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
37	
38	
39	# ================================================================
40	# DGP Parameters for general K
41	# ================================================================
42	# Base coefficient pools — K=3 values match plan_001 exactly,
43	# K=5,7 extend with alternating-sign decreasing magnitudes.
44	_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
45	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
46	_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
47	_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
48	_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
49	_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
50	_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
51	
52	
53	def make_p_A(K):
54	    """Slightly imbalanced category probabilities."""
55	    if K == 3:
56	        return np.array([0.40, 0.35, 0.25])
57	    raw = np.array([1.0 / i for i in range(1, K + 1)])
58	    return raw / raw.sum()
59	
60	
61	def make_params(K):
62	    """DGP parameters for all topologies at given K."""
63	    p_A = make_p_A(K)
64	
65	    conf = dict(
66	        p_A=p_A,
67	        alpha=np.array(_ALPHA_POOL[:K-1]),
68	        beta_A=np.array(_BETA_A_POOL[:K-1]),
69	        beta_T=2.0,
70	        sigma_T=1.0,
71	    )
72	
73	    med = dict(
74	        tau=0.5,
75	        gamma=np.array(_GAMMA_POOL[:K]),
76	        delta=np.array(_DELTA_POOL[:K]),
77	        beta=np.array(_BETA_POOL[:K]),
78	    )
79	
80	    coll = dict(
81	        tau=1.0,
82	        g=np.zeros(K),
83	        dT=np.array(_DT_POOL[:K]),
84	        dY=np.array(_DY_POOL[:K]),
85	    )
86	
87	    exp = dict(
88	        beta=np.array(_BETA_POOL[:K]),
89	        p_A=p_A,
90	    )
91	
92	    return dict(confounding=conf, mediation=med, collider=coll, exposure=exp)
93	
94	
95	# ================================================================
96	# DGP Generators
97	# ================================================================
98	def _softmax_rows(logits):
99	    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
100	    return e / e.sum(axis=-1, keepdims=True)
101	
102	
103	def _sample_cat(probs, rng):
104	    """Sample from row-wise categorical probabilities [N, K]."""
105	    cum = np.cumsum(probs, axis=1)
106	    u = rng.uniform(size=probs.shape[0])[:, None]
107	    return (u >= cum).sum(axis=1).astype(int)
108	
109	
110	def gen_confounding(K, N, p, rng):
111	    """A→T, A→Y, T→Y. Researcher omits true A, uses A*."""
112	    A = rng.choice(K, size=N, p=p['p_A'])
113	    D = np.zeros((N, K - 1))
114	    for j in range(K - 1):
115	        D[:, j] = (A == j + 1).astype(float)
116	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
117	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
118	    return T, Y, A
119	
120	
121	def gen_mediation(K, N, p, rng):
122	    """T→A→Y. A mediates T's effect; researcher controls for A*."""
123	    T = rng.binomial(1, 0.5, N).astype(float)
124	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
125	    probs = _softmax_rows(logits)
126	    A = _sample_cat(probs, rng)
127	    D = np.zeros((N, K - 1))
128	    for j in range(K - 1):
129	        D[:, j] = (A == j + 1).astype(float)
130	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
131	    return T, Y, A
132	
133	
134	def gen_collider(K, N, p, rng):
135	    """T→A←Y. Controlling for collider A* opens a backdoor path."""
136	    T = rng.normal(0, 1, N)
137	    Y = p['tau'] * T + rng.normal(0, 1, N)
138	    logits = (p['g'][None, :]
139	              + p['dT'][None, :] * T[:, None]
140	              + p['dY'][None, :] * Y[:, None])
141	    probs = _softmax_rows(logits)
142	    A = _sample_cat(probs, rng)
143	    return T, Y, A
144	
145	
146	def gen_exposure(K, N, p, rng):
147	    """A→Y. A is the treatment of interest."""
148	    A = rng.choice(K, size=N, p=p['p_A'])
149	    D = np.zeros((N, K - 1))
150	    for j in range(K - 1):
151	        D[:, j] = (A == j + 1).astype(float)
152	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
153	    return None, Y, A
154	
155	
156	_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
157	            collider=gen_collider, exposure=gen_exposure)
158	
159	
160	# ================================================================
161	# Sufficient Statistics
162	# ================================================================
163	class SuffStats:
164	    """Pre-compute population moments from a large DGP sample.
165	
166	    Stores:
167	      p_A[k]   = P(A=k)
168	      E_Y      = E[Y]
169	      E_YD[k]  = E[Y · 1(A=k)]
170	    For topologies with T:
171	      E_T, E_T2, E_TY, E_TD[k] = E[T · 1(A=k)]
172	    """
173	
174	    def __init__(self, T, Y, A, K):
175	        self.K = K
176	        self.has_T = T is not None
177	
178	        self.p_A = np.array([(A == k).mean() for k in range(K)])
179	        self.E_Y = Y.mean()
180	        self.E_YD = np.array([(Y * (A == k)).mean() for k in range(K)])
181	
182	        if self.has_T:
183	            self.E_T = T.mean()
184	            self.E_T2 = (T ** 2).mean()
185	            self.E_TY = (T * Y).mean()
186	            self.E_TD = np.array([(T * (A == k)).mean() for k in range(K)])
187	
188	    def to_device(self, dev):
189	        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)
190	        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)
191	        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)
192	        if self.has_T:
193	            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)
194	            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)
195	            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)
196	            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)
197	        return self
198	
199	
200	# ================================================================
201	# GPU-Batched Plim
202	# ================================================================
203	def plim_with_T(ss, C):
204	    """Batched plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.
205	
206	    Generalizes K=3 plan_001 formula. Z* = (1, T, D*_1,...,D*_{K-1}).
207	    plim = (E[Z*'Z*])^{-1} E[Z*'Y].
208	
209	    E[Z*'Z*] and E[Z*'Y] depend on C through:
210	      q = C @ p_A              (marginal of A*)
211	      E[T·D*_j] = (C @ E_TD)[j]
212	      E[Y·D*_j] = (C @ E_YD)[j]
213	      E[D*_i·D*_j] = q[i] δ_{ij}  (A* is categorical)
214	
215	    Args:
216	        ss: SuffStats on device
217	        C:  [B, K, K] confusion matrices
218	    Returns:
219	        [B, K+1] plim coefficients
220	    """
221	    B, K = C.shape[0], ss.K
222	    dim = K + 1
223	
224	    q = C @ ss.t_p_A                   # [B, K]
225	    ct = C @ ss.t_E_TD                 # [B, K]
226	    cy = C @ ss.t_E_YD                 # [B, K]
227	
228	    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
229	    EZZ[:, 0, 0] = 1.0
230	    EZZ[:, 0, 1] = ss.t_E_T
231	    EZZ[:, 1, 0] = ss.t_E_T
232	    EZZ[:, 1, 1] = ss.t_E_T2
233	    EZZ[:, 0, 2:] = q[:, 1:]
234	    EZZ[:, 2:, 0] = q[:, 1:]
235	    EZZ[:, 1, 2:] = ct[:, 1:]
236	    EZZ[:, 2:, 1] = ct[:, 1:]
237	    idx = torch.arange(K - 1, device=C.device)
238	    EZZ[:, idx + 2, idx + 2] = q[:, 1:]
239	
240	    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
241	    EZY[:, 0] = ss.t_E_Y
242	    EZY[:, 1] = ss.t_E_TY
243	    EZY[:, 2:] = cy[:, 1:]
244	
245	    return torch.linalg.solve(EZZ, EZY)
246	
247	
248	def plim_exposure(ss, C):
249	    """Batched plim for Y ~ 1 + D*_1 + ... + D*_{K-1} (no T).
250	
251	    Same moment algebra as plim_with_T but without the T row/column.
252	    """
253	    B, K = C.shape[0], ss.K
254	    dim = K
255	
256	    q = C @ ss.t_p_A
257	    cy = C @ ss.t_E_YD
258	
259	    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
260	    EZZ[:, 0, 0] = 1.0
261	    EZZ[:, 0, 1:] = q[:, 1:]
262	    EZZ[:, 1:, 0] = q[:, 1:]
263	    idx = torch.arange(K - 1, device=C.device)
264	    EZZ[:, idx + 1, idx + 1] = q[:, 1:]
265	
266	    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
267	    EZY[:, 0] = ss.t_E_Y
268	    EZY[:, 1:] = cy[:, 1:]
269	
270	    return torch.linalg.solve(EZZ, EZY)
271	
272	
273	# ================================================================
274	# Random C Generation
275	# ================================================================
276	def gen_random_C(K, N, device, seed=SEED, min_diag=None):
277	    """Sample N column-stochastic K×K matrices via Dirichlet(1,...,1).
278	
279	    Each column independently drawn. If min_diag is set, each diagonal
280	    element is drawn from U[min_diag, 1] and the remaining mass is
281	    distributed Dirichlet among off-diagonal entries.
282	    """
283	    rng = np.random.default_rng(seed)
284	    C = np.zeros((N, K, K))
285	
286	    if min_diag is not None and min_diag > 0:
287	        for j in range(K):
288	            diag = rng.uniform(min_diag, 1.0, N)
289	            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]
290	            col = np.zeros((N, K))
291	            col[:, j] = diag
292	            idx = 0
293	            for i in range(K):
294	                if i != j:
295	                    col[:, i] = offdiag[:, idx]
296	                    idx += 1
297	            C[:, :, j] = col
298	    else:
299	        for j in range(K):
300	            C[:, :, j] = rng.dirichlet(np.ones(K), N)
301	
302	    return torch.tensor(C, dtype=DTYPE, device=device)
303	
304	
305	# ================================================================
306	# Metrics
307	# ================================================================
308	def compute_metrics(plim_batch, plim_true, tau_idx=None):
309	    """Violation / sign-flip / amplification rates.
310	
311	    tau_idx: index of τ coefficient (1 for topologies with T, None for exposure).
312	    """
313	    diff = plim_batch - plim_true.unsqueeze(0)
314	
315	    violation = (diff.abs() > 1e-8).any(dim=1).float().mean().item()
316	
317	    s0 = torch.sign(plim_true).unsqueeze(0)
318	    s1 = torch.sign(plim_batch)
319	    sign_flip = ((s0 != s1) & (s0 != 0) & (s1 != 0)).any(dim=1).float().mean().item()
320	
321	    amplification = (plim_batch.abs() > plim_true.abs().unsqueeze(0) + 1e-10
322	                     ).any(dim=1).float().mean().item()
323	
324	    m = dict(violation=violation, sign_flip=sign_flip, amplification=amplification)
325	
326	    if tau_idx is not None:
327	        tb = plim_batch[:, tau_idx]
328	        tt = plim_true[tau_idx]
329	        td = tb - tt
330	        m['tau_violation'] = (td.abs() > 1e-8).float().mean().item()
331	        m['tau_sign_flip'] = ((torch.sign(tb) != torch.sign(tt)) &
332	                              (torch.sign(tt) != 0) &
333	                              (torch.sign(tb) != 0)).float().mean().item()
334	        m['tau_amplification'] = (tb.abs() > tt.abs() + 1e-10).float().mean().item()
335	        m['tau_bias_mean'] = td.mean().item()
336	        m['tau_bias_std'] = td.std().item()
337	        m['tau_bias_max'] = td.abs().max().item()
338	    return m
339	
340	
341	# ================================================================
342	# MC Verification (small-scale, a few named C matrices)
343	# ================================================================
344	def mc_verify(K, topo, params, C_np, n_reps=500, n_mc=10_000, seed=0):
345	    """Monte Carlo OLS estimate of plim for a single C, as validation."""
346	    gen_fn = _GEN[topo]
347	    coefs = []
348	    for r in range(n_reps):
349	        rng = np.random.default_rng(seed + r)
350	        T, Y, A = gen_fn(K, n_mc, params, rng)
351	
352	        # Misclassify
353	        probs = C_np[:, A]       # [K, N]
354	        cum = np.cumsum(probs, axis=0)
355	        u = rng.uniform(size=n_mc)
356	        Astar = np.zeros(n_mc, dtype=int)
357	        for k in range(K - 1):
358	            Astar += (u >= cum[k]).astype(int)
359	
360	        Dstar = np.zeros((n_mc, K - 1))
361	        for j in range(K - 1):
362	            Dstar[:, j] = (Astar == j + 1).astype(float)
363	
364	        ones = np.ones((n_mc, 1))
365	        if T is not None:
366	            Z = np.hstack([ones, T[:, None], Dstar])
367	        else:
368	            Z = np.hstack([ones, Dstar])
369	        b = np.linalg.lstsq(Z, Y, rcond=None)[0]
370	        coefs.append(b)
371	    return np.mean(coefs, axis=0), np.std(coefs, axis=0) / np.sqrt(n_reps)
372	
373	
374	# ================================================================
375	# Interpretability (a): Eigendecomposition of bias vectors
376	# ================================================================
377	def eigen_analysis(plim_batch, plim_true):
378	    """PCA on bias = plim(C) - plim(I). Returns top-3 variance ratios.
379	
380	    The bias vectors live in R^{K+1} (or R^K for exposure).
381	    Eigendecomposition of bias covariance identifies which linear
382	    combinations of coefficients carry most of the bias variance.
383	    """
384	    bias = (plim_batch - plim_true.unsqueeze(0)).cpu().numpy()
385	    bias_c = bias - bias.mean(axis=0)
386	    _, S, Vt = np.linalg.svd(bias_c, full_matrices=False)
387	    var = S ** 2
388	    ratios = var / var.sum()
389	    return ratios[:min(3, len(ratios))]
390	
391	
392	# ================================================================
393	# Interpretability (b): Worst-case bounds under diagonal constraint
394	# ================================================================
395	def worst_case_bounds(ss, plim_fn, K, device, thresholds=(0.5, 0.7, 0.9)):
396	    """max|τ̂ − τ_true| over column-stochastic C with min diag(C) ≥ thr.
397	
398	    For each threshold, sample 50k constrained C matrices and report
399	    the maximum, mean, and 95th-percentile |bias|.
400	    """
401	    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
402	    plim_I = plim_fn(ss, I_batch).squeeze(0)
403	    has_T = plim_I.shape[0] > K
404	    idx = 1 if has_T else 1
405	
406	    results = {}
407	    for thr in thresholds:
408	        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)
409	        pb = plim_fn(ss, Cb)
410	        valid = torch.isfinite(pb).all(dim=1)
411	        pb = pb[valid]
412	        if has_T:
413	            bias = (pb[:, idx] - plim_I[idx]).abs()
414	        else:
415	            bias = (pb[:, 1:] - plim_I[1:].unsqueeze(0)).abs().max(dim=1).values
416	        results[thr] = dict(
417	            max_bias=bias.max().item(),
418	            mean_bias=bias.mean().item(),
419	            p95_bias=torch.quantile(bias, 0.95).item(),
420	        )
421	    return results
422	
423	
424	# ================================================================
425	# Interpretability (c): Sensitivity heatmap via finite differences
426	# ================================================================
427	def sensitivity_heatmap(ss, plim_fn, K, device, out_path, topo_name):
428	    """∂|bias(τ)|/∂C_ij evaluated at C = I via finite differences.
429	
430	    For off-diagonal (i,j): perturb C[i,j] += δ and C[j,j] -= δ to keep
431	    column j stochastic. Measures which misclassification patterns most
432	    affect the τ estimate.
433	    """
434	    delta = 0.01
435	    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
436	    plim_I = plim_fn(ss, I_batch).squeeze(0)
437	    has_T = plim_I.shape[0] > K
438	    tau_idx = 1 if has_T else 1
439	    tau_I = plim_I[tau_idx].item()
440	
441	    sens = np.zeros((K, K))
442	    for i in range(K):
443	        for j in range(K):
444	            if i == j:
445	                continue
446	            C = torch.eye(K, dtype=DTYPE, device=device)
447	            C[i, j] += delta
448	            C[j, j] -= delta
449	            p = plim_fn(ss, C.unsqueeze(0)).squeeze(0)
450	            sens[i, j] = abs(p[tau_idx].item() - tau_I) / delta
451	
452	    fig, ax = plt.subplots(figsize=(max(3.5, K * 0.7), max(3.5, K * 0.7)))
453	    im = ax.imshow(sens, cmap='YlOrRd', aspect='equal')
454	    ax.set_xlabel('True category j')
455	    ax.set_ylabel('Observed category i')
456	    ax.set_title(f'{topo_name} K={K}: |∂bias(τ)/∂C_ij|')
457	    ax.set_xticks(range(K))
458	    ax.set_yticks(range(K))
459	    for i in range(K):
460	        for j in range(K):
461	            color = 'w' if sens[i, j] > sens.max() * 0.6 else 'k'
462	            ax.text(j, i, f'{sens[i,j]:.3f}', ha='center', va='center',
463	                    fontsize=max(5, 8 - K), color=color)
464	    plt.colorbar(im, ax=ax, shrink=0.8)
465	    fig.tight_layout()
466	    fig.savefig(out_path, dpi=150, bbox_inches='tight')
467	    plt.close(fig)
468	    return sens
469	
470	
471	# ================================================================
472	# Main
473	# ================================================================
474	def main():
475	    t0 = time.time()
476	    print("=" * 90)
477	    print("  Plan 002: K={3,5,7} Bias Taxonomy Extension")
478	    print("=" * 90)
479	    print(f"Device: {DEVICE}")
480	    if torch.cuda.is_available():
481	        gp = torch.cuda.get_device_properties(0)
482	        print(f"GPU: {gp.name}  ({gp.total_memory / 1024**3:.1f} GB)")
483	    print(f"N_RANDOM={N_RANDOM:,}  N_LARGE={N_LARGE:,}")
484	
485	    topologies = ['confounding', 'mediation', 'collider', 'exposure']
486	    all_results = {}
487	
488	    # ------------------------------------------------------------------
489	    # Named C matrices for MC verification (K=3 only, matching plan_001)
490	    # ------------------------------------------------------------------
491	    C_named_3 = {
492	        'sym_high': np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]]),
493	        'weak_diag': np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]]),
494	    }
495	
496	    for topo in topologies:
497	        print(f"\n{'=' * 90}")
498	        print(f"  TOPOLOGY: {topo.upper()}")
499	        print(f"{'=' * 90}")
500	
501	        plim_fn = plim_exposure if topo == 'exposure' else plim_with_T
502	        tau_idx = None if topo == 'exposure' else 1
503	
504	        for K in K_VALUES:
505	            print(f"\n  --- K={K} ---")
506	            tk = time.time()
507	
508	            params = make_params(K)
509	            p = params[topo]
510	            rng = np.random.default_rng(SEED)
511	
512	            # 1. Large DGP → sufficient statistics
513	            T, Y, A = _GEN[topo](K, N_LARGE, p, rng)
514	            ss = SuffStats(T, Y, A, K).to_device(DEVICE)
515	            print(f"  p_A = {ss.p_A}")
516	            if ss.has_T:
517	                print(f"  E[T]={ss.E_T:.4f}  E[T²]={ss.E_T2:.4f}  E[TY]={ss.E_TY:.4f}")
518	
519	            # 2. plim(I) = τ_true
520	            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
521	            plim_true = plim_fn(ss, I_batch).squeeze(0)
522	            print(f"  plim(I) = {plim_true.cpu().numpy()}")
523	
524	            # 3. MC verification for K=3
525	            if K == 3:
526	                print(f"\n  MC Verification (K=3, 500 reps × 10k samples):")
527	                for cn, Cnp in C_named_3.items():
528	                    Ct = torch.tensor(Cnp, dtype=DTYPE, device=DEVICE).unsqueeze(0)
529	                    th = plim_fn(ss, Ct).squeeze(0).cpu().numpy()
530	                    mc, se = mc_verify(K, topo, p, Cnp)
531	                    match = np.abs(th - mc) < 2.5 * se
532	                    tag = ''.join('✓' if m else '✗' for m in match)
533	                    print(f"    {cn:<10}  theory={th}  MC={mc}  {tag}")
534	
535	            # 4. Random C search
536	            C_batch = gen_random_C(K, N_RANDOM, DEVICE)
537	            plim_all = plim_fn(ss, C_batch)
538	
539	            valid = torch.isfinite(plim_all).all(dim=1)
540	            n_valid = valid.sum().item()
541	            if n_valid < N_RANDOM:
542	                print(f"  WARNING: {N_RANDOM - n_valid} singular, using {n_valid}")
543	                plim_all = plim_all[valid]
544	
545	            metrics = compute_metrics(plim_all, plim_true, tau_idx=tau_idx)
546	            key = f"{topo}_K{K}"
547	            all_results[key] = metrics
548	
549	            print(f"\n  Overall: violation={metrics['violation']:.1%}  "
550	                  f"sign_flip={metrics['sign_flip']:.1%}  "
551	                  f"amplification={metrics['amplification']:.1%}")
552	            if tau_idx is not None:
553	                print(f"  τ-specific: violation={metrics['tau_violation']:.1%}  "
554	                      f"sign_flip={metrics['tau_sign_flip']:.1%}  "
555	                      f"amplification={metrics['tau_amplification']:.1%}")
556	                print(f"  τ bias: mean={metrics['tau_bias_mean']:+.6f}  "
557	                      f"std={metrics['tau_bias_std']:.6f}  "
558	                      f"max={metrics['tau_bias_max']:.6f}")
559	
560	            # 5. Eigendecomposition
561	            top3 = eigen_analysis(plim_all, plim_true)
562	            print(f"  Eigen top-{len(top3)} var explained: "
563	                  + '  '.join(f'{v:.1%}' for v in top3))
564	
565	            # 6. Worst-case bounds
566	            wc = worst_case_bounds(ss, plim_fn, K, DEVICE)
567	            for thr, v in wc.items():
568	                print(f"  Worst-case (diag≥{thr}): "
569	                      f"max|Δτ|={v['max_bias']:.6f}  "
570	                      f"mean={v['mean_bias']:.6f}  "
571	                      f"P95={v['p95_bias']:.6f}")
572	
573	            # 7. Sensitivity heatmap
574	            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
575	            sensitivity_heatmap(ss, plim_fn, K, DEVICE, hm_path, topo)
576	            print(f"  Heatmap → {os.path.basename(hm_path)}")
577	
578	            print(f"  [{time.time() - tk:.1f}s]")
579	
580	    # ==================================================================
581	    # Cross-K Summary
582	    # ==================================================================
583	    print(f"\n{'=' * 90}")
584	    print("  CROSS-K COMPARISON")
585	    print(f"{'=' * 90}")
586	
587	    hdr = (f"  {'Topology':<14} {'K':>3}"
588	           f" {'violat':>8} {'sflip':>8} {'amplif':>8}"
589	           f" {'τ_viol':>8} {'τ_sflip':>8} {'τ_amp':>8}")
590	    print(hdr)
591	    print(f"  {'-' * 73}")
592	
593	    for topo in topologies:
594	        for K in K_VALUES:
595	            m = all_results[f"{topo}_K{K}"]
596	            tv = m.get('tau_violation', None)
597	            ts = m.get('tau_sign_flip', None)
598	            ta = m.get('tau_amplification', None)
599	            tvs = f"{tv:.1%}" if tv is not None else "  —"
600	            tss = f"{ts:.1%}" if ts is not None else "  —"
601	            tas = f"{ta:.1%}" if ta is not None else "  —"
602	            print(f"  {topo:<14} {K:>3}"
603	                  f" {m['violation']:>8.1%} {m['sign_flip']:>8.1%}"
604	                  f" {m['amplification']:>8.1%}"
605	                  f" {tvs:>8} {tss:>8} {tas:>8}")
606	        print()
607	
608	    # Trend analysis
609	    print("  K-TREND ANALYSIS (does bias worsen with K?)")
610	    for topo in topologies:
611	        if topo == 'exposure':
612	            vals = [all_results[f"{topo}_K{K}"]['violation'] for K in K_VALUES]
613	            label = 'violation'
614	        else:
615	            vals = [all_results[f"{topo}_K{K}"]['tau_violation'] for K in K_VALUES]
616	            label = 'τ_violation'
617	        d = vals[-1] - vals[0]
618	        trend = "WORSENS" if d > 0.01 else ("STABLE" if abs(d) <= 0.01 else "IMPROVES")
619	        print(f"  {topo:<14} ({label}): "
620	              f"K=3 {vals[0]:.1%} → K=5 {vals[1]:.1%} → K=7 {vals[2]:.1%}  [{trend}]")
621	
622	    # ==================================================================
623	    # Combined sensitivity figure (K=5 and K=7 side by side per topology)
624	    # ==================================================================
625	    fig, axes = plt.subplots(len(topologies), 2, figsize=(12, 4 * len(topologies)))
626	    for row, topo in enumerate(topologies):
627	        for col, K in enumerate([5, 7]):
628	            ax = axes[row, col]
629	            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
630	            if os.path.exists(hm_path):
631	                img = plt.imread(hm_path)
632	                ax.imshow(img)
633	                ax.axis('off')
634	                ax.set_title(f'{topo} K={K}', fontsize=10)
635	            else:
636	                ax.text(0.5, 0.5, 'N/A', ha='center', va='center', transform=ax.transAxes)
637	                ax.set_title(f'{topo} K={K}', fontsize=10)
638	    fig.suptitle('Sensitivity Heatmaps: |∂bias(τ)/∂C_ij|', fontsize=13)
639	    fig.tight_layout(rect=[0, 0, 1, 0.97])
640	    combined_path = os.path.join(OUT_DIR, 'plan002_sensitivity_combined.png')
641	    fig.savefig(combined_path, dpi=150, bbox_inches='tight')
642	    plt.close(fig)
643	    print(f"\n  Combined heatmap → {os.path.basename(combined_path)}")
644	
645	    print(f"\nTotal: {time.time() - t0:.0f}s")
646	
647	
648	if __name__ == "__main__":
649	    main()
650	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "81816fdc-9bc6-4e06-9c40-a110e2033d2a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py",
      "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"\nPlan 002: K={3,5,7} Bias Taxonomy Extension\n\nExtends plan_001's K=3 bias analysis to general K across 4 core DAG topologies.\nFor each topology x K, generates 100k random K×K confusion matrices (Dirichlet),\ncomputes plim via pre-computed sufficient statistics, and reports violation/sign-flip/\namplification rates. Includes eigendecomposition, worst-case bounds, and sensitivity\nheatmaps as interpretability tools.\n\nInput:  DGP parameters per topology (auto-generated for each K)\nOutput: Cross-K comparison tables, sensitivity heatmaps (PNG)\n\nDependencies: torch (GPU), numpy, matplotlib\n\"\"\"\n\nimport torch\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport time\nimport os\nimport sys\n\n# ================================================================\n# Configuration\n# ================================================================\nK_VALUES = [3, 5, 7]\nN_RANDOM = 100_000\nN_LARGE = 5_000_000\nSEED = 42\nDEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\nDTYPE = torch.float64\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n\n# ================================================================\n# DGP Parameters for general K\n# ================================================================\n# Base coefficient pools — K=3 values match plan_001 exactly,\n# K=5,7 extend with alternating-sign decreasing magnitudes.\n_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n\n\ndef make_p_A(K):\n    \"\"\"Slightly imbalanced category probabilities.\"\"\"\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_params(K):\n    \"\"\"DGP parameters for all topologies at given K.\"\"\"\n    p_A = make_p_A(K)\n\n    conf = dict(\n        p_A=p_A,\n        alpha=np.array(_ALPHA_POOL[:K-1]),\n        beta_A=np.array(_BETA_A_POOL[:K-1]),\n        beta_T=2.0,\n        sigma_T=1.0,\n    )\n\n    med = dict(\n        tau=0.5,\n        gamma=np.array(_GAMMA_POOL[:K]),\n        delta=np.array(_DELTA_POOL[:K]),\n        beta=np.array(_BETA_POOL[:K]),\n    )\n\n    coll = dict(\n        tau=1.0,\n        g=np.zeros(K),\n        dT=np.array(_DT_POOL[:K]),\n        dY=np.array(_DY_POOL[:K]),\n    )\n\n    exp = dict(\n        beta=np.array(_BETA_POOL[:K]),\n        p_A=p_A,\n    )\n\n    return dict(confounding=conf, mediation=med, collider=coll, exposure=exp)\n\n\n# ================================================================\n# DGP Generators\n# ================================================================\ndef _softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=-1, keepdims=True))\n    return e / e.sum(axis=-1, keepdims=True)\n\n\ndef _sample_cat(probs, rng):\n    \"\"\"Sample from row-wise categorical probabilities [N, K].\"\"\"\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum).sum(axis=1).astype(int)\n\n\ndef gen_confounding(K, N, p, rng):\n    \"\"\"A→T, A→Y, T→Y. Researcher omits true A, uses A*.\"\"\"\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    \"\"\"T→A→Y. A mediates T's effect; researcher controls for A*.\"\"\"\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    probs = _softmax_rows(logits)\n    A = _sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    \"\"\"T→A←Y. Controlling for collider A* opens a backdoor path.\"\"\"\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :]\n              + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    probs = _softmax_rows(logits)\n    A = _sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    \"\"\"A→Y. A is the treatment of interest.\"\"\"\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\n_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,\n            collider=gen_collider, exposure=gen_exposure)\n\n\n# ================================================================\n# Sufficient Statistics\n# ================================================================\nclass SuffStats:\n    \"\"\"Pre-compute population moments from a large DGP sample.\n\n    Stores:\n      p_A[k]   = P(A=k)\n      E_Y      = E[Y]\n      E_YD[k]  = E[Y · 1(A=k)]\n    For topologies with T:\n      E_T, E_T2, E_TY, E_TD[k] = E[T · 1(A=k)]\n    \"\"\"\n\n    def __init__(self, T, Y, A, K):\n        self.K = K\n        self.has_T = T is not None\n\n        self.p_A = np.array([(A == k).mean() for k in range(K)])\n        self.E_Y = Y.mean()\n        self.E_YD = np.array([(Y * (A == k)).mean() for k in range(K)])\n\n        if self.has_T:\n            self.E_T = T.mean()\n            self.E_T2 = (T ** 2).mean()\n            self.E_TY = (T * Y).mean()\n            self.E_TD = np.array([(T * (A == k)).mean() for k in range(K)])\n\n    def to_device(self, dev):\n        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)\n        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)\n        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)\n        if self.has_T:\n            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)\n            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)\n            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)\n            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)\n        return self\n\n\n# ================================================================\n# GPU-Batched Plim\n# ================================================================\ndef plim_with_T(ss, C):\n    \"\"\"Batched plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\n\n    Generalizes K=3 plan_001 formula. Z* = (1, T, D*_1,...,D*_{K-1}).\n    plim = (E[Z*'Z*])^{-1} E[Z*'Y].\n\n    E[Z*'Z*] and E[Z*'Y] depend on C through:\n      q = C @ p_A              (marginal of A*)\n      E[T·D*_j] = (C @ E_TD)[j]\n      E[Y·D*_j] = (C @ E_YD)[j]\n      E[D*_i·D*_j] = q[i] δ_{ij}  (A* is categorical)\n\n    Args:\n        ss: SuffStats on device\n        C:  [B, K, K] confusion matrices\n    Returns:\n        [B, K+1] plim coefficients\n    \"\"\"\n    B, K = C.shape[0], ss.K\n    dim = K + 1\n\n    q = C @ ss.t_p_A                   # [B, K]\n    ct = C @ ss.t_E_TD                 # [B, K]\n    cy = C @ ss.t_E_YD                 # [B, K]\n\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1] = ss.t_E_T\n    EZZ[:, 1, 0] = ss.t_E_T\n    EZZ[:, 1, 1] = ss.t_E_T2\n    EZZ[:, 0, 2:] = q[:, 1:]\n    EZZ[:, 2:, 0] = q[:, 1:]\n    EZZ[:, 1, 2:] = ct[:, 1:]\n    EZZ[:, 2:, 1] = ct[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 2, idx + 2] = q[:, 1:]\n\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1] = ss.t_E_TY\n    EZY[:, 2:] = cy[:, 1:]\n\n    return torch.linalg.solve(EZZ, EZY)\n\n\ndef plim_exposure(ss, C):\n    \"\"\"Batched plim for Y ~ 1 + D*_1 + ... + D*_{K-1} (no T).\n\n    Same moment algebra as plim_with_T but without the T row/column.\n    \"\"\"\n    B, K = C.shape[0], ss.K\n    dim = K\n\n    q = C @ ss.t_p_A\n    cy = C @ ss.t_E_YD\n\n    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)\n    EZZ[:, 0, 0] = 1.0\n    EZZ[:, 0, 1:] = q[:, 1:]\n    EZZ[:, 1:, 0] = q[:, 1:]\n    idx = torch.arange(K - 1, device=C.device)\n    EZZ[:, idx + 1, idx + 1] = q[:, 1:]\n\n    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)\n    EZY[:, 0] = ss.t_E_Y\n    EZY[:, 1:] = cy[:, 1:]\n\n    return torch.linalg.solve(EZZ, EZY)\n\n\n# ================================================================\n# Random C Generation\n# ================================================================\ndef gen_random_C(K, N, device, seed=SEED, min_diag=None):\n    \"\"\"Sample N column-stochastic K×K matrices via Dirichlet(1,...,1).\n\n    Each column independently drawn. If min_diag is set, each diagonal\n    element is drawn from U[min_diag, 1] and the remaining mass is\n    distributed Dirichlet among off-diagonal entries.\n    \"\"\"\n    rng = np.random.default_rng(seed)\n    C = np.zeros((N, K, K))\n\n    if min_diag is not None and min_diag > 0:\n        for j in range(K):\n            diag = rng.uniform(min_diag, 1.0, N)\n            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]\n            col = np.zeros((N, K))\n            col[:, j] = diag\n            idx = 0\n            for i in range(K):\n                if i != j:\n                    col[:, i] = offdiag[:, idx]\n                    idx += 1\n            C[:, :, j] = col\n    else:\n        for j in range(K):\n            C[:, :, j] = rng.dirichlet(np.ones(K), N)\n\n    return torch.tensor(C, dtype=DTYPE, device=device)\n\n\n# ================================================================\n# Metrics\n# ================================================================\ndef compute_metrics(plim_batch, plim_true, tau_idx=None):\n    \"\"\"Violation / sign-flip / amplification rates.\n\n    tau_idx: index of τ coefficient (1 for topologies with T, None for exposure).\n    \"\"\"\n    diff = plim_batch - plim_true.unsqueeze(0)\n\n    violation = (diff.abs() > 1e-8).any(dim=1).float().mean().item()\n\n    s0 = torch.sign(plim_true).unsqueeze(0)\n    s1 = torch.sign(plim_batch)\n    sign_flip = ((s0 != s1) & (s0 != 0) & (s1 != 0)).any(dim=1).float().mean().item()\n\n    amplification = (plim_batch.abs() > plim_true.abs().unsqueeze(0) + 1e-10\n                     ).any(dim=1).float().mean().item()\n\n    m = dict(violation=violation, sign_flip=sign_flip, amplification=amplification)\n\n    if tau_idx is not None:\n        tb = plim_batch[:, tau_idx]\n        tt = plim_true[tau_idx]\n        td = tb - tt\n        m['tau_violation'] = (td.abs() > 1e-8).float().mean().item()\n        m['tau_sign_flip'] = ((torch.sign(tb) != torch.sign(tt)) &\n                              (torch.sign(tt) != 0) &\n                              (torch.sign(tb) != 0)).float().mean().item()\n        m['tau_amplification'] = (tb.abs() > tt.abs() + 1e-10).float().mean().item()\n        m['tau_bias_mean'] = td.mean().item()\n        m['tau_bias_std'] = td.std().item()\n        m['tau_bias_max'] = td.abs().max().item()\n    return m\n\n\n# ================================================================\n# MC Verification (small-scale, a few named C matrices)\n# ================================================================\ndef mc_verify(K, topo, params, C_np, n_reps=500, n_mc=10_000, seed=0):\n    \"\"\"Monte Carlo OLS estimate of plim for a single C, as validation.\"\"\"\n    gen_fn = _GEN[topo]\n    coefs = []\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        T, Y, A = gen_fn(K, n_mc, params, rng)\n\n        # Misclassify\n        probs = C_np[:, A]       # [K, N]\n        cum = np.cumsum(probs, axis=0)\n        u = rng.uniform(size=n_mc)\n        Astar = np.zeros(n_mc, dtype=int)\n        for k in range(K - 1):\n            Astar += (u >= cum[k]).astype(int)\n\n        Dstar = np.zeros((n_mc, K - 1))\n        for j in range(K - 1):\n            Dstar[:, j] = (Astar == j + 1).astype(float)\n\n        ones = np.ones((n_mc, 1))\n        if T is not None:\n            Z = np.hstack([ones, T[:, None], Dstar])\n        else:\n            Z = np.hstack([ones, Dstar])\n        b = np.linalg.lstsq(Z, Y, rcond=None)[0]\n        coefs.append(b)\n    return np.mean(coefs, axis=0), np.std(coefs, axis=0) / np.sqrt(n_reps)\n\n\n# ================================================================\n# Interpretability (a): Eigendecomposition of bias vectors\n# ================================================================\ndef eigen_analysis(plim_batch, plim_true):\n    \"\"\"PCA on bias = plim(C) - plim(I). Returns top-3 variance ratios.\n\n    The bias vectors live in R^{K+1} (or R^K for exposure).\n    Eigendecomposition of bias covariance identifies which linear\n    combinations of coefficients carry most of the bias variance.\n    \"\"\"\n    bias = (plim_batch - plim_true.unsqueeze(0)).cpu().numpy()\n    bias_c = bias - bias.mean(axis=0)\n    _, S, Vt = np.linalg.svd(bias_c, full_matrices=False)\n    var = S ** 2\n    ratios = var / var.sum()\n    return ratios[:min(3, len(ratios))]\n\n\n# ================================================================\n# Interpretability (b): Worst-case bounds under diagonal constraint\n# ================================================================\ndef worst_case_bounds(ss, plim_fn, K, device, thresholds=(0.5, 0.7, 0.9)):\n    \"\"\"max|τ̂ − τ_true| over column-stochastic C with min diag(C) ≥ thr.\n\n    For each threshold, sample 50k constrained C matrices and report\n    the maximum, mean, and 95th-percentile |bias|.\n    \"\"\"\n    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)\n    plim_I = plim_fn(ss, I_batch).squeeze(0)\n    has_T = plim_I.shape[0] > K\n    idx = 1 if has_T else 1\n\n    results = {}\n    for thr in thresholds:\n        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)\n        pb = plim_fn(ss, Cb)\n        valid = torch.isfinite(pb).all(dim=1)\n        pb = pb[valid]\n        if has_T:\n            bias = (pb[:, idx] - plim_I[idx]).abs()\n        else:\n            bias = (pb[:, 1:] - plim_I[1:].unsqueeze(0)).abs().max(dim=1).values\n        results[thr] = dict(\n            max_bias=bias.max().item(),\n            mean_bias=bias.mean().item(),\n            p95_bias=torch.quantile(bias, 0.95).item(),\n        )\n    return results\n\n\n# ================================================================\n# Interpretability (c): Sensitivity heatmap via finite differences\n# ================================================================\ndef sensitivity_heatmap(ss, plim_fn, K, device, out_path, topo_name):\n    \"\"\"∂|bias(τ)|/∂C_ij evaluated at C = I via finite differences.\n\n    For off-diagonal (i,j): perturb C[i,j] += δ and C[j,j] -= δ to keep\n    column j stochastic. Measures which misclassification patterns most\n    affect the τ estimate.\n    \"\"\"\n    delta = 0.01\n    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)\n    plim_I = plim_fn(ss, I_batch).squeeze(0)\n    has_T = plim_I.shape[0] > K\n    tau_idx = 1 if has_T else 1\n    tau_I = plim_I[tau_idx].item()\n\n    sens = np.zeros((K, K))\n    for i in range(K):\n        for j in range(K):\n            if i == j:\n                continue\n            C = torch.eye(K, dtype=DTYPE, device=device)\n            C[i, j] += delta\n            C[j, j] -= delta\n            p = plim_fn(ss, C.unsqueeze(0)).squeeze(0)\n            sens[i, j] = abs(p[tau_idx].item() - tau_I) / delta\n\n    fig, ax = plt.subplots(figsize=(max(3.5, K * 0.7), max(3.5, K * 0.7)))\n    im = ax.imshow(sens, cmap='YlOrRd', aspect='equal')\n    ax.set_xlabel('True category j')\n    ax.set_ylabel('Observed category i')\n    ax.set_title(f'{topo_name} K={K}: |∂bias(τ)/∂C_ij|')\n    ax.set_xticks(range(K))\n    ax.set_yticks(range(K))\n    for i in range(K):\n        for j in range(K):\n            color = 'w' if sens[i, j] > sens.max() * 0.6 else 'k'\n            ax.text(j, i, f'{sens[i,j]:.3f}', ha='center', va='center',\n                    fontsize=max(5, 8 - K), color=color)\n    plt.colorbar(im, ax=ax, shrink=0.8)\n    fig.tight_layout()\n    fig.savefig(out_path, dpi=150, bbox_inches='tight')\n    plt.close(fig)\n    return sens\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    t0 = time.time()\n    print(\"=\" * 90)\n    print(\"  Plan 002: K={3,5,7} Bias Taxonomy Extension\")\n    print(\"=\" * 90)\n    print(f\"Device: {DEVICE}\")\n    if torch.cuda.is_available():\n        gp = torch.cuda.get_device_properties(0)\n        print(f\"GPU: {gp.name}  ({gp.total_memory / 1024**3:.1f} GB)\")\n    print(f\"N_RANDOM={N_RANDOM:,}  N_LARGE={N_LARGE:,}\")\n\n    topologies = ['confounding', 'mediation', 'collider', 'exposure']\n    all_results = {}\n\n    # ------------------------------------------------------------------\n    # Named C matrices for MC verification (K=3 only, matching plan_001)\n    # ------------------------------------------------------------------\n    C_named_3 = {\n        'sym_high': np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]]),\n        'weak_diag': np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]]),\n    }\n\n    for topo in topologies:\n        print(f\"\\n{'=' * 90}\")\n        print(f\"  TOPOLOGY: {topo.upper()}\")\n        print(f\"{'=' * 90}\")\n\n        plim_fn = plim_exposure if topo == 'exposure' else plim_with_T\n        tau_idx = None if topo == 'exposure' else 1\n\n        for K in K_VALUES:\n            print(f\"\\n  --- K={K} ---\")\n            tk = time.time()\n\n            params = make_params(K)\n            p = params[topo]\n            rng = np.random.default_rng(SEED)\n\n            # 1. Large DGP → sufficient statistics\n            T, Y, A = _GEN[topo](K, N_LARGE, p, rng)\n            ss = SuffStats(T, Y, A, K).to_device(DEVICE)\n            print(f\"  p_A = {ss.p_A}\")\n            if ss.has_T:\n                print(f\"  E[T]={ss.E_T:.4f}  E[T²]={ss.E_T2:.4f}  E[TY]={ss.E_TY:.4f}\")\n\n            # 2. plim(I) = τ_true\n            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)\n            plim_true = plim_fn(ss, I_batch).squeeze(0)\n            print(f\"  plim(I) = {plim_true.cpu().numpy()}\")\n\n            # 3. MC verification for K=3\n            if K == 3:\n                print(f\"\\n  MC Verification (K=3, 500 reps × 10k samples):\")\n                for cn, Cnp in C_named_3.items():\n                    Ct = torch.tensor(Cnp, dtype=DTYPE, device=DEVICE).unsqueeze(0)\n                    th = plim_fn(ss, Ct).squeeze(0).cpu().numpy()\n                    mc, se = mc_verify(K, topo, p, Cnp)\n                    match = np.abs(th - mc) < 2.5 * se\n                    tag = ''.join('✓' if m else '✗' for m in match)\n                    print(f\"    {cn:<10}  theory={th}  MC={mc}  {tag}\")\n\n            # 4. Random C search\n            C_batch = gen_random_C(K, N_RANDOM, DEVICE)\n            plim_all = plim_fn(ss, C_batch)\n\n            valid = torch.isfinite(plim_all).all(dim=1)\n            n_valid = valid.sum().item()\n            if n_valid < N_RANDOM:\n                print(f\"  WARNING: {N_RANDOM - n_valid} singular, using {n_valid}\")\n                plim_all = plim_all[valid]\n\n            metrics = compute_metrics(plim_all, plim_true, tau_idx=tau_idx)\n            key = f\"{topo}_K{K}\"\n            all_results[key] = metrics\n\n            print(f\"\\n  Overall: violation={metrics['violation']:.1%}  \"\n                  f\"sign_flip={metrics['sign_flip']:.1%}  \"\n                  f\"amplification={metrics['amplification']:.1%}\")\n            if tau_idx is not None:\n                print(f\"  τ-specific: violation={metrics['tau_violation']:.1%}  \"\n                      f\"sign_flip={metrics['tau_sign_flip']:.1%}  \"\n                      f\"amplification={metrics['tau_amplification']:.1%}\")\n                print(f\"  τ bias: mean={metrics['tau_bias_mean']:+.6f}  \"\n                      f\"std={metrics['tau_bias_std']:.6f}  \"\n                      f\"max={metrics['tau_bias_max']:.6f}\")\n\n            # 5. Eigendecomposition\n            top3 = eigen_analysis(plim_all, plim_true)\n            print(f\"  Eigen top-{len(top3)} var explained: \"\n                  + '  '.join(f'{v:.1%}' for v in top3))\n\n            # 6. Worst-case bounds\n            wc = worst_case_bounds(ss, plim_fn, K, DEVICE)\n            for thr, v in wc.items():\n                print(f\"  Worst-case (diag≥{thr}): \"\n                      f\"max|Δτ|={v['max_bias']:.6f}  \"\n                      f\"mean={v['mean_bias']:.6f}  \"\n                      f\"P95={v['p95_bias']:.6f}\")\n\n            # 7. Sensitivity heatmap\n            hm_path = os.path.join(OUT_DIR, f\"plan002_sensitivity_{topo}_K{K}.png\")\n            sensitivity_heatmap(ss, plim_fn, K, DEVICE, hm_path, topo)\n            print(f\"  Heatmap → {os.path.basename(hm_path)}\")\n\n            print(f\"  [{time.time() - tk:.1f}s]\")\n\n    # ==================================================================\n    # Cross-K Summary\n    # ==================================================================\n    print(f\"\\n{'=' * 90}\")\n    print(\"  CROSS-K COMPARISON\")\n    print(f\"{'=' * 90}\")\n\n    hdr = (f\"  {'Topology':<14} {'K':>3}\"\n           f\" {'violat':>8} {'sflip':>8} {'amplif':>8}\"\n           f\" {'τ_viol':>8} {'τ_sflip':>8} {'τ_amp':>8}\")\n    print(hdr)\n    print(f\"  {'-' * 73}\")\n\n    for topo in topologies:\n        for K in K_VALUES:\n            m = all_results[f\"{topo}_K{K}\"]\n            tv = m.get('tau_violation', None)\n            ts = m.get('tau_sign_flip', None)\n            ta = m.get('tau_amplification', None)\n            tvs = f\"{tv:.1%}\" if tv is not None else \"  —\"\n            tss = f\"{ts:.1%}\" if ts is not None else \"  —\"\n            tas = f\"{ta:.1%}\" if ta is not None else \"  —\"\n            print(f\"  {topo:<14} {K:>3}\"\n                  f\" {m['violation']:>8.1%} {m['sign_flip']:>8.1%}\"\n                  f\" {m['amplification']:>8.1%}\"\n                  f\" {tvs:>8} {tss:>8} {tas:>8}\")\n        print()\n\n    # Trend analysis\n    print(\"  K-TREND ANALYSIS (does bias worsen with K?)\")\n    for topo in topologies:\n        if topo == 'exposure':\n            vals = [all_results[f\"{topo}_K{K}\"]['violation'] for K in K_VALUES]\n            label = 'violation'\n        else:\n            vals = [all_results[f\"{topo}_K{K}\"]['tau_violation'] for K in K_VALUES]\n            label = 'τ_violation'\n        d = vals[-1] - vals[0]\n        trend = \"WORSENS\" if d > 0.01 else (\"STABLE\" if abs(d) <= 0.01 else \"IMPROVES\")\n        print(f\"  {topo:<14} ({label}): \"\n              f\"K=3 {vals[0]:.1%} → K=5 {vals[1]:.1%} → K=7 {vals[2]:.1%}  [{trend}]\")\n\n    # ==================================================================\n    # Combined sensitivity figure (K=5 and K=7 side by side per topology)\n    # ==================================================================\n    fig, axes = plt.subplots(len(topologies), 2, figsize=(12, 4 * len(topologies)))\n    for row, topo in enumerate(topologies):\n        for col, K in enumerate([5, 7]):\n            ax = axes[row, col]\n            hm_path = os.path.join(OUT_DIR, f\"plan002_sensitivity_{topo}_K{K}.png\")\n            if os.path.exists(hm_path):\n                img = plt.imread(hm_path)\n                ax.imshow(img)\n                ax.axis('off')\n                ax.set_title(f'{topo} K={K}', fontsize=10)\n            else:\n                ax.text(0.5, 0.5, 'N/A', ha='center', va='center', transform=ax.transAxes)\n                ax.set_title(f'{topo} K={K}', fontsize=10)\n    fig.suptitle('Sensitivity Heatmaps: |∂bias(τ)/∂C_ij|', fontsize=13)\n    fig.tight_layout(rect=[0, 0, 1, 0.97])\n    combined_path = os.path.join(OUT_DIR, 'plan002_sensitivity_combined.png')\n    fig.savefig(combined_path, dpi=150, bbox_inches='tight')\n    plt.close(fig)\n    print(f\"\\n  Combined heatmap → {os.path.basename(combined_path)}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.0f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 650,
      "startLine": 1,
      "totalLines": 650
    }
  }
}
```

</details>

---


### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the codebase. Let me write the plan_006_asv_empirical.py script. Here's what I need:

1. **Data loading & confusion matrix construction** - from JSONL files
2. **Downstream causal bias** - reuse plim functions from plan_001/plan_005 for 7 topologies
3. **ASV computation** - reuse from plan_005
4. **F1 vs Downstream Bias** - new analysis
5. **Type I/II Error Rates** - before/after ASV
6. **Inter-model error correlation** - new analysis


7. **Main function** with --mock support

I need to handle variable K values (2, 3, 10) since the existing code hardcodes K=3. The plim functions in plan_002 already support general K using torch for batched computation, but I'll implement numpy versions for single-matrix operations in plan_006. I also need to map out all seven topologies from the existing code—confounding, mediation, and the others—to ensure consistent causal bias calculations across different DAG structures. Looking at the plim functions more carefully, I see that plan_002's `plim_with_T` approach actually generalizes to confounding, mediation, collider, and M-bias since they all use the same regression structure with treatment. For exposure, there's a separate function without treatment. The IV and front-door cases need different handling—IV uses the Wald estimator while front-door requires its own approach, so I need to generalize those two to work beyond K=3. Writing the matrix formulas...

Now I'm thinking through how to generalize this across arbitrary K values—I'll use numpy for the matrix operations and create mock data generators for different K scenarios, then build out all six analysis modules in a comprehensive script. K=2 and K=10:

For K=2:
- Confounding: alpha has K-1=1 element, beta_A has 1 element
- Mediation: gamma, delta, beta all K=2 elements  
- Collider: g, dT, dY all K=2 elements
- Exposure: beta K=2 elements
- M-bias: similar to confounding but with U1, U2
- IV: beta K=2 elements
- Front-door: gamma, delta K=2 elements, beta K=2 elements

For K=10:
- Extend parameter vectors to length 10 (or 9 for K-1 elements)

The user specified DGP params for K=3, so I need to adapt them for K=2 and K=10 using parameter pools like plan_002 does. Now I'm looking at which topologies to include—the task mentions 7 different topologies from plan_001, and I can see confounding and mediation are already defined, so I need to identify the remaining ones from the existing code.

I've identified all 7 topologies: confounding, mediation, collider, exposure, M-bias, IV, and front-door. Now I'll write the script following the task structure, using the sufficient statistics approach where the regression is Y ~ 1 + T + D*_1 + ... + D*_{K-1} for most topologies, with the plim determined by key sufficient statistics like E_T, E_T², E_TY, and the treatment assignment probabilities.

For IV and exposure, the sufficient statistics differ slightly—IV uses the Wald estimator with first-stage differences, while exposure drops the treatment term. I need to build DGP generators that handle arbitrary K following plan_002's approach, then structure the script to load empirical data and run the simulations.

The C matrices are empirical from the JSONL data, not generated—I'll use them to compute how much bias each topology would experience under that particular C. This means I need functions to generate DGP sufficient statistics for each topology at each K value, compute the probability limit given C and those statistics, and calculate ASV using the C(delta) parameterization. The datasets have different K values (humaid at K=10, vast at K=3, civil_comments at K=2), so the DGP parameters need to adapt accordingly.

Rather than rewriting from scratch, I should adapt the plim and ASV functions from the existing scripts to work with arbitrary K, then build the analysis pipeline on top of that foundation.

Generating parameter pools... Defining parameter configuration... Writing config dictionaries...

Actually, I'm realizing I'm overcomplicating the setup here. Looking at the empirical plan, the C matrices come directly from annotation data, and the dataset sizes vary significantly—K=2 for civil_comments, K=3 for vast, and K=10 for humaid. The existing bias functions assume K=3, so I need to adapt them to handle these different dimensionalities.

The key realization from plan_002 is that the OLS limiting distribution formula scales naturally across any K value. Whether I'm fitting Y against treatment and K-1 dummy variables or just the dummies alone, it's just a matter of solving the appropriate system size. So my approach is straightforward: build general-K data generators for each topology that produce the treatment, outcome, and annotation data, compute sufficient statistics from large samples like in plan_005, then apply the existing limiting distribution functions which already handle arbitrary K.

Computing sufficient statistics from the data... Building the moment matrix... Finishing the matrix setup and solving for coefficients, then moving on to the IV case with the Wald estimator that divides the reduced form by the first-stage coefficient. Now I need to decide on seven topologies and structure the code accordingly.

I'm laying out the seven causal structures: confounding with A affecting both T and Y, mediation where T influences A which influences Y, a collider where both T and Y point to A, a simple exposure of A on Y, M-bias with two unobserved confounders creating a backdoor path, instrumental variables with Z affecting A while U confounds A and Y, and the frontdoor criterion where T affects M which affects Y with U confounding T and Y.

Most of these use the same OLS estimator with T in the regression, except exposure which drops T, and IV which relies on the Wald estimator instead. The key distinction is how the data-generating process creates the sufficient statistics for each scenario.

Now I'm ready to write the script...

Writing Python script... I don't need to generate actual JSONL data for the mock mode—I can work directly with confusion matrices. Now I'm thinking through how to compute F1 scores from a confusion matrix. If the matrix is column-stochastic where each entry represents the probability of predicted label given true label, and I know the class prevalences, I can derive precision and recall for each class and then calculate F1. I need to be careful about the confusion matrix notation. The confusion matrix C[j,i] represents P(predicted=j | true=i), so I can derive the true positives, false positives, and false negatives for each class. From there, I can express precision and recall in terms of C and the class probabilities p_i. Precision simplifies to C[i,i] * p_i divided by the sum of C[i,j] * p_j across all predicted classes, while recall is just C[i,i] since it only depends on the diagonal element. This means I can compute F1 scores directly from the confusion matrix and class distribution without needing individual sample predictions.

For the inter-model correlation analysis, I'll need to generate synthetic per-sample predictions in mock mode. Now I'm thinking through what the true correlation values should be for different topologies and K values to make the synthetic data realistic.

I'll set fixed DGP parameters for each topology, compute the true correlation under perfect classification, then for each empirical confusion matrix, calculate the limiting correlation and the resulting bias. Using the ASV parameterization with C(delta) = (1-delta)*I + delta*C_empirical lets me smoothly interpolate between perfect and empirical classification. I'm ready to write the full script now, focusing on all 7 topologies from the existing plan: confounding, mediation, collider, exposure, mbias, iv, and frontdoor.

All 7 topologies should apply across K values of 2, 3, and 10, though I'll need to adapt the DGP parameters accordingly. For the IV topology specifically, the Wald estimator uses the first-stage effect on category 1, but with K=10 this becomes problematic since we have 9 endogenous dummies but only 1 instrument—making it under-identified. Still, the bias expression remains meaningful as a way to measure how misclassification affects the first stage, so I'll include it with a note about this limitation.

Now I'm setting up the full script structure with the datasets, models, prompts, and topologies defined as constants...

Defining parameter pools... I'm setting up the data loading pipeline with functions to read annotation files and construct a confusion matrix from the true and predicted labels.

Loading all confusion matrices...

Now I'm setting up the DGP parameter generation, starting with a function that creates probability distributions over K classes—using a simple split for binary classification, a fixed distribution for three classes, and a harmonic distribution for larger K values. Writing config dictionaries... Writing config dictionaries... Setting up the M-bias and IV parameters for K=3 with the coefficient vectors, then extending the same pattern to front-door with gamma coefficients.

Now I'm implementing a softmax sampling function that converts logits to probabilities and draws categorical samples using cumulative distributions. Writing categorical sampling logic... I need to reconsider the logic here. The cumulative probabilities build up from p0 to 1, and I want to count how many thresholds the random sample exceeds—that gives me the category. For K=3, summing the indicator functions for cum[0] and cum[1] works perfectly. For the general case, I'm implementing this as a loop that accumulates the count across all K-1 thresholds, or using a vectorized approach to sum along the cumulative axis.

Verifying the vectorized version: when u is below cum[0], both indicators are 0; when u falls between cum[0] and cum[1], only the first indicator is 1, giving the correct category.

Now I'm implementing the full function to generate misclassified labels by sampling from the column-stochastic confusion matrix, then moving on to think about softmax sampling for the general case.

Writing softmax sampling... I see the current rewritten thinking ends mid-code. Since the next thinking continues with more function definitions for the data generation process, I'll switch to prose and describe what's happening:

I'm setting up generator functions for different causal structures—one for confounding where treatment and outcome both depend on a confounder, and another for mediation where treatment affects an intermediate variable that then influences the outcome. Each function creates the appropriate causal relationships and returns the simulated data. Writing data generation functions... Finishing the instrumental variable function by computing the outcome Y from the mediator encoding and confounding, then moving into the front-door criterion setup where treatment affects a mediator which then influences the outcome, with shared confounding between treatment and outcome.

Now I'm defining a function to precompute sufficient statistics for the limit calculations, starting with encoding the mediator or treatment variable into dummy columns and then computing the reduced form effect for the instrumental variable case.

Computing sufficient statistics... Continuing the plim computation... Writing extraction and interpolation functions... Writing the ASV computation loop... I'm finishing up the significance-based threshold check, then moving on to compute F1 metrics from a confusion matrix by calculating precision and recall for each class based on the predicted and true labels.

Computing F1 scores... Writing simulation logic... I need to clarify how to compute the standard error for the significance ASV since it depends on sample size and data variance. I'll use a reference sample size like 5000 and derive the SE from the DGP variance, which should give me a consistent way to determine when the limiting distribution of the bias falls below the significance threshold. _flip: min delta where sign flips

For significance, I need SE. For OLS, SE(tau_hat) ≈ sigma_eps / sqrt(N * Var_T_residualized). I'll compute this from the DGP.

Actually, let me simplify. For significance ASV, what matters is: given N samples with this C matrix, would the hypothesis test still reject? The SE depends on N. I'll use N=1000 as a reference.

For OLS (Y ~ 1 + T + D*), the SE of tau_hat is approximately:
SE ≈ sqrt(sigma²_eps / (N * Var(T|X_other)))

This is complex to derive from just sufficient statistics. Let me instead compute it from finite-sample simulation: generate data under H1 with the DGP, apply C, run OLS, get the average SE.

The key question for significance ASV is: at what delta does the estimate fall below the significance threshold? I need to find the minimum delta where |tau_curve(delta)| drops below 1.96 times the standard error. Rather than running expensive Monte Carlo simulations, I'll compute a fixed significance boundary once from the asymptotic formula and then find where the tau curve crosses it.

Let me just code this up now with a clear structure: utility functions first, then DGP generators for all 7 topologies, sufficient statistics, plim computation, C(delta) and ASV functions, F1 metrics, bias and ASV for all matrices and topologies, then the analysis.

Now I'm thinking through how Type I/II errors should work with the empirical C matrices—the key insight is that I can use ASV as a filter to flag unreliable results when the misclassification level is too high, rather than trying to correct for it directly. I'm realizing the logic here: when the magnitude ASV exceeds 1, the bias stays within tolerance even at maximum perturbation, so the result is trustworthy and I should use it. But if the magnitude ASV is below 1, the bias eventually exceeds the tolerance threshold, meaning I need to be more conservative and reject the result. eds tolerance before delta reaches 1. Actually, I think I've been interpreting this backwards—masv represents the minimum delta where the bias becomes problematic, so a large masv means the C matrix can tolerate significant misclassification, while a small masv indicates vulnerability. The decision rule only rejects when both the test statistic exceeds 1.96 and the C matrix passes the ASV filter with masv above threshold, which should reduce false positives but potentially at the cost of power.

Now I'm realizing the key issue: under the null hypothesis where tau_h equals zero, the magnitude ASV becomes undefined since the threshold becomes 0.1 times zero, which gets exceeded immediately. This means masv returns None under H0, and the condition allowing rejections would be true for None values, so the Type I error rate under the ASV filter would match the naive rate. Hmm, that seems problematic. Let me check if plan_005 handles this... Looking at the code:
- Under H0 (tau_h = 0): masv = None (since |tau_h| < 1e-12)
- Condition: masv is None or masv > 1.0 → True
- So mag_rej == naive_rej under H0

That means the ASV filter doesn't help with Type I errors when H0 is true. The benefit is for H1: the ASV filter can reduce false rejections when the bias is large enough to cause problems.

Actually wait, I think the interpretation is different. The ASV filter is a pre-test check: before trusting any inference result, check if the misclassification level is within acceptable tolerance, and abstain if it's not.

So the workflow is: compute an empirical C matrix from validation data, calculate the ASV to see if results are robust to that misclassification level, and only proceed with inference if the ASV suggests robustness. For the Type I/II analysis, I need to compute ASV for each empirical C matrix, simulate inference under both hypotheses with that C, and compare rejection rates with and without the ASV filter. To measure how far each C is from identity, I can find the delta value that best interpolates between identity and some baseline C0. gives me a way to adjust the Type I and Type II error rates based on whether the C matrix passes the safety check. Under the null hypothesis where tau equals zero, the ASV becomes undefined since the threshold is zero, so I'll need to switch to an absolute magnitude threshold instead. For the alternative hypothesis, I can use a relative threshold scaled to the true effect size. For the plan_006 script, I'm simplifying this to compute the empirical C matrix for each configuration and then calculate its magnitude ASV to determine safety.

Now I'm reconsidering whether this binary filter approach is too simplistic—if a C matrix is flagged as unsafe, the analysis becomes trivial. Looking back at plan_005, I see a more nuanced approach where I generate finite sample data using the empirical C, estimate the effect and its standard error, then compare the naive rejection rate against one that additionally filters based on the ASV safety criterion.

The key insight is that the ASV magnitude is a fixed property of the C matrix itself, not something that varies across Monte Carlo replications. What does change is whether we reject based on the test statistic in each sample, and the ASV check acts as a gating mechanism on top of that decision.

Looking at the empirical results from the previous analysis, the ASV filter behaves differently depending on the causal structure: for M-bias scenarios it's mostly permissive so the naive rejection rates carry through, but for instrumental variable setups it's mostly restrictive which zeros out both Type I error and power, while front-door cases fall somewhere in between.

Now I'm realizing there's a crucial detail I missed—the masv calculation itself depends on the hypothesis value tau_h, so under the null hypothesis where tau_h=0 the filter becomes extremely restrictive since any bias immediately triggers it, but under the alternative hypothesis with tau_h=0.5 the threshold shifts and the filter's behavior changes. ):
- masv = compute_magnitude_asv_fast(tau_curve, deltas, 0.5, 0.1)
- threshold = 0.1 * 0.5 = 0.05
- Bias needs to exceed 0.05 to trigger
- masv could be > 1 if the bias stays small

But wait, under H0, the sufficient statistics are different (tau=0 in the DGP). So the plim tau_curve is also different. Under H0 with no misclassification (C=I), plim(tau_hat)=0. With misclassification, plim(tau_hat) may be nonzero (bias).

For H0, the masv with tau_h=0:
- bias(delta) = |plim(C(delta))_tau - 0|
- threshold = 0.1 * 0

When tau is essentially zero, any positive bias triggers the magnitude ASV check, but the code returns None since the true effect is negligible. This means the filter doesn't actually reject anything under H0—it passes through all naive rejections unchanged. The magnitude ASV is really designed to catch cases where misclassification-induced bias could flip the sign or inflate estimates when there's a genuine effect present, not to control Type I error under the null.

Now I'm ready to implement the script. I need to compute inter-model error correlations by gathering per-sample predictions from each model—either synthetic ones in mock mode or loaded from JSONL files in real mode.

Defining the correlation function... Computing Cohen's kappa by calculating the expected agreement under independence, then finding the correlation between error patterns across the two models to see if they fail in similar ways.

Now I'm writing the complete script, starting with a function to generate realistic mock confusion matrices with configurable diagonal strength depending on the number of classes.

For the K=10 case, I'm creating a structured version that models how nearby categories get confused more often than distant ones, which is more realistic for ordinal data.

Now I need to write out the full script and make sure all 6 analysis modules produce their results as specified in the task.

I'm pulling the DGP parameters from the existing plans to match them as closely as possible — for K=3, I'll use the confounding setup from plan_002 with specific values for the probability distribution, treatment effects, and outcome coefficients, plus the mediation parameters from plan_001_med. I'm completing the IV specification and adding the front-door criterion setup, both pulling from plan_005. Then I'm realizing that the key distinction between M-bias and front-door approaches isn't in how we estimate—we're always fitting the same regression model with T and the mediators—but rather in the underlying data-generating process itself.

For K=10, I need to extend the softmax logits with ten parameter values for the intercept and coefficients, scaling them down as the categories increase. Now I'm ready to write out the full script, creating a function that generates DGP parameters for any K value while preserving the plan_001 and plan_005 specifications at K=3.

Writing the complete script... I need to simulate per-sample predictions in mock mode by generating synthetic data for each model using a mock C matrix, then computing agreement metrics and error correlations. For the diagnostic plots, I'll create a scatter plot of F1 versus bias magnitude by topology, an ASV heatmap across topologies and datasets, and a bar chart comparing Type I and Type II errors—keeping everything simple with matplotlib. I'm also thinking through the N_PRECOMP parameter carefully: for K=10 categories, precomputing sufficient statistics with N=2M samples works fine for OLS topologies, and the softmax will naturally distribute probability across the 10 categorical dimensions in the collider topology.

Writing the DGP parameter setup... Defining coefficient arrays... Setting up parameter configurations... Setting up the IV parameters with scaled coefficients and then moving on to define the front-door adjustment parameters.

Actually, I'm overcomplicating this. Let me step back and use the simpler approach from plan_002 with K=3 values, then write out the complete script. Though I realize the inter-model correlation module still needs some per-model configuration that I haven't fully thought through yet.

For the JSONL files, each row represents a single sample with true and predicted labels. The key insight is that all three models should be annotating the same dataset and prompt, so I can load their predictions in parallel and compute agreement metrics like pairwise agreement and kappa. In mock mode, I'll generate synthetic samples with ground truth labels, then have each model make predictions on those same samples.

Now I need to implement the OLS function for the finite-sample simulation. Defining the regression function...

Writing regression functions... Writing the Wald estimator...

Now I'm thinking through the full script organization and how to handle the IV topology when K=10, specifically using the first stage for category 1.

With 10 categories, I only have one instrument for nine endogenous dummies, which means the Wald estimator is fundamentally under-identified. The first stage effect for category 1 will be weak since it's just one of many categories, making the estimator unstable. I'll compute it anyway but flag cases where the first stage is too small.

For the exposure topology, there's no treatment variable, so I need to define bias differently—I'll measure it as the largest change in category effects from misclassification rather than looking at treatment effects.

Let me write out the full script now.

Looking at the task description more carefully, each topology should return tau_hat (the estimate under misclassification), bias (tau_hat minus the true value), bias_pct (absolute bias relative to true value), and sign_flip (whether the sign changed). For exposure, I'll use beta[1] as the target effect for consistency, though I need to think through whether that's the right choice or if I should track any coefficient that changes sign.

Actually, I'm overcomplicating this. The goal for plan_006 is straightforward: compute bias from empirical C matrices by comparing estimates under misclassification to the baseline with C=I. I'll standardize the interface so that for confounding, mediation, collider, m-bias, and frontdoor topologies, tau is the coefficient on T (index 1 in the plim vector), for exposure it's the coefficient on category 1 (also index 1), and for IV it's the Wald estimator. This gives me a consistent scalar tau_hat to compare against tau_true for each topology.

Now I'm ready to write the complete script.

Writing the main script... Writing utility functions... Writing the actual implementations... Let me think about edge cases:
1. K=2: only 1 dummy variable. plim returns [intercept, tau_or_beta1]. Works fine.
2. K=10: 9 dummy variables. plim returns [intercept, tau, beta1, ..., beta9]. Should work but the EZZ matrix is 11×11 for topologies with T. This is fine numerically.
3. IV with K=10: FS_1 might be very small → Wald unstable. Handle with nan.
4. Singular matrices: when EZZ is singular (degenerate C), return nan. Handle with try/except.

For the precomputation, I need N_PRECOMP to be large enough for K=10. With N=2M and K=10, each category has ~200k samples (if balanced). This should be sufficient for stable sufficient statistics.

For the mock data generation, I need to ensure the C matrices are column-stochastic. Now I'll write out the full script, being careful about the dimensions. For K=10, the compute_plim function builds an 11×11 matrix which is manageable, and the MC simulation with 5000 observations and 11 parameters is well-conditioned. The ASV computation evaluates plim across 1500 delta grid points, which means 1500 matrix solves—each taking microseconds—and with 189 total (C, topology) pairs, the full computation should complete in reasonable time. For each (C, topology) pair, I need to run simulations under both the null hypothesis (tau=0) to measure Type I error and under the alternative (tau=tau_true) to measure power, which doubles the computational load but remains feasible. For the null case, I can modify the DGP by setting tau to zero in the confounding structure.

Now I'm thinking through how to handle the frontdoor topology specifically—it has T affecting Y through the mediator M, with unobserved confounding U affecting both T and Y. Under the null, I want the true treatment effect to be zero, but the frontdoor structure complicates this since T naturally flows through to Y via M.

The cleaner approach is to set the null uniformly across all topologies: make the true coefficient on the target parameter (whether that's T, the mediated effect, or the IV coefficient) equal to zero. Looking back at plan_005, different topologies had different null implementations—M-bias set tau to zero, IV set all beta coefficients to zero—and I need to clarify whether this variation was intentional or if I should standardize the approach.

For plan_006, I've laid out the null specifications for each topology, and for H1 I'll just use the standard DGP parameters. Now I should stop overthinking and start implementing this. The real question is whether the empirical C actually influences the inference results—that's what will make the Type I and Type II error analysis meaningful.

Let me streamline the Type I/II module: precompute sufficient statistics under both hypotheses, derive the probability limits of C, calculate the magnitude of the asymptotic sensitivity vector under H1, run Monte Carlo simulations for both H0 and H1, then compute rejection rates with and without applying the ASV filter. The filter itself is straightforward—only reject if the naive test rejects AND the magnitude ASV exceeds 1.0.

With n_sim=10 for the dry-run, this should execute quickly. I'm going to reduce the topologies for this analysis to keep it manageable—even with 7 topologies and 27 matrices, that's 189 configurations times 10 simulations, which is still reasonable.

The key insight is separating the precomputation from the simulation: I'll compute sufficient statistics once per configuration and hypothesis to get the population-level probability limits, then run the finite-sample simulations independently by generating data, applying the constraint C, and running OLS without needing to recompute those statistics each time.

Writing the MC simulation loop... I'm organizing the script with a modular structure that handles K values of 2, 3, and 10, includes mock data for testing, and implements all six analysis modules. I need to be careful with the IV topology—Z is the instrument, A is the endogenous variable, and Y is the outcome, so the Wald estimator calculates the reduced form and first stage effects rather than running standard OLS.

I'm standardizing the generator function interface so all gen_fns return a tuple of (first_var, Y, A), where first_var is T for confounding/mediation/collider/m-bias/frontdoor cases, None for exposure, and Z for IV. This keeps the interface consistent across all topologies.

Writing the Monte Carlo simulation... Writing the main script... Defining parameter pools...

Now I'm writing utility functions to handle the numerical operations—computing row-wise softmax normalization, sampling from categorical distributions, and generating misclassified labels.

Defining OLS regression functions... Writing regression logic... Writing config parameters... Writing parameter configurations... Setting up front-door parameters... Writing DGP generator functions... Finishing the mediation function by creating the dummy-coded treatment matrix and computing the outcome with direct and indirect effects, then moving on to define a collider structure where treatment and outcome both influence the treatment assignment mechanism. Writing generator functions... Completing the frontdoor function and setting up a registry of all the data generation functions, then moving into precomputing sufficient statistics for the different causal structures.

Now I'm defining a function that generates population moments from a large sample of the DGP, extracting the treatment and outcome variables, then computing reduced form and first stage estimates when dealing with instrumental variable scenarios.

Returning different moment dictionaries depending on the topology—for IV cases I'm returning the reduced form and first stage coefficients, for exposure models I'm computing treatment probabilities and outcome expectations, and for other topologies I'm also including treatment moments and cross-moments between treatment and outcome.

Now I'm implementing the function to compute the probability limit given a confusion matrix and sufficient statistics, handling each topology case differently—for IV I'm checking if the first stage is strong enough, for exposure I'm building the instrument covariance and cross-moment matrices.

Continuing with matrix construction... Writing extraction function...

Now I'm realizing there's an issue with how I'm extracting tau from the results. When the topology is exposure-based, the plim vector contains the intercept followed by the treatment effects, so tau should be the coefficient at index 1 (the effect of category 1 versus the baseline). This works fine even when K=2, where the vector is just [intercept, beta_1], and tau correctly pulls beta_1.

For IV topologies, the plim result is a scalar from the Wald estimator, so I return it directly. For all the OLS-based topologies like confounding, mediation, collider, and the various bias structures, the plim vector follows the pattern [intercept, tau, beta_1, ..., beta_{K-1}], so tau is always at index 1. This is consistent across the board and works for the bias computation I need to do.

Now I'm moving on to set up the data loading and confusion matrix construction... Completing the confusion matrix normalization and then loading all 27 matrices across the different dataset, model, and prompt combinations, handling missing files gracefully. Now moving into the bias computation section.

Computing bias for each confusion matrix by extracting the estimated treatment effect, comparing it to the true effect, and calculating both absolute and percentage bias along with whether there's a sign flip... Writing bias computation functions... Computing the running maximum of absolute bias values, then checking for sign flips or magnitude thresholds depending on the ASV type to determine when the estimate crosses critical boundaries. Writing the ASV computation function...

Now I'm wrapping up the significance ASV logic and closing out the function. I'm realizing the SE approximation I'm using is pretty rough—it assumes a fixed reference sample size of 1000, but really the standard error depends on the actual sample size and the specific estimator being used. For the OLS setup with Y regressed on treatment and the adjustment variable, the SE should scale with the sample size, so I should probably refine this approach. I'll use a reference sample size of 1000 and compute the significance boundary as approximately 0.063, then find the minimum delta where the tau curve drops below that threshold. This is a simplified approach that ignores variance structure, but I could refine it by precomputing the standard error from the actual data.

Actually, deriving the exact SE formula from the sufficient statistics is getting too involved—I'll just estimate it via Monte Carlo instead. For now, let me focus on computing magnitude and sign_flip ASVs, since those are more interpretable anyway.

Looking back at the task requirements, it specifies three ASV types: magnitude (minimum δ where bias exceeds 10% of the estimate), significance (minimum δ where the asymptotic limit falls below 1.96 times the SE), and sign_flip (minimum δ causing a sign reversal). I'll implement magnitude and sign_flip in the main computation, then handle the significance analysis separately in the Type I/II error module.

For the significance threshold, I need to estimate the reference standard error from a small Monte Carlo simulation run once per configuration, then reuse that value across different δ values. Writing the function to estimate this reference SE...

The function runs a simulation with no misclassification to get the baseline sampling variability of the treatment effect estimator, then uses that to find the minimum δ where the bias exceeds 1.96 times the reference standard error. With these parameters, the computation finishes in about a second.

For the implementation, I'll reduce n_mc to 10 for dry runs since we don't need high precision on the standard error estimate, and I'm setting up the reference SE calculation as a separate function that gets called when needed in the ASV computation loop.

Now I'm building out the F1 score calculation module along with Type I/II error and inter-model correlation functions... Writing function logic... Writing the Type I error simulation... Continuing the simulation under the alternative hypothesis, I'm applying the same estimation logic based on the network topology—either instrumental variables, OLS without treatment, or OLS with dummies—then checking if the test statistic exceeds the critical value to count rejections and calculate statistical power.

Now I'm packaging the results into a dictionary with the type I error rates, power estimates, and whether the procedure is ASV-safe, then moving on to compute inter-model error correlations by generating synthetic per-sample predictions from the confusion matrices.

Computing pairwise model correlations... Writing mock data generation... Writing JSON serialization helper...

Now I'm setting up the main function with argument parsing for the data directory, output location, mock data option, simulation count, and device selection.

Then I'm creating the output directory and starting the timer, printing a header for the empirical ASV calibration plan. I'm loading or generating confusion matrices depending on whether mock mode is enabled, then displaying how many were loaded and sampling a few to check their structure.

Now I'm precomputing sufficient statistics and parameters for each K value across the dataset configurations... Still writing parameter setup... Writing analysis output... Writing the inter-model correlation analysis...

Now I'm tallying up the results—counting how many models achieved F1 scores above 0.93 and how many of those also showed high bias.

I'm also calculating how many scenarios would benefit from PPI++ based on unsafe ASV values, then compiling everything into a summary dictionary before serializing all the confusion matrices, biases, ASV scores, and analysis results to JSON and saving to the output directory.

Printing the final summary statistics... Writing the significance check logic...

I'm realizing that for the significance ASV, I should compute the standard error from the ideal case where C=I (no misclassification), which gives us the best-case SE. This way, the significance ASV tells us how much misclassification we can tolerate before the estimate becomes statistically insignificant—and since real misclassification makes the dummies noisier and increases SE, using the C=I reference is actually conservative.

Now I need to handle the K=2 edge case carefully, where the confounding, mediation, and collider scenarios each have their own specific structure for how the treatment, mediators, and colliders enter the model. For K=2, the OLS setup is straightforward with either 3 parameters (including intercept and treatment) or 2 parameters, and the Wald estimator follows the standard binary IV approach. Moving to K=10, I'm concerned about the matrix inversion in the plim computation—a 11×11 solve could be problematic if the C matrix is ill-conditioned, though realistic diagonal values above 0.6 should keep it stable. The other challenge is generating DGP parameters for 10 categories without running into numerical issues.

Checking the parameter pools now...

The gamma pool completes with 10 values total, which matches what I need. Delta pool also has the right 10 values. For the M-bias initialization with K=10, I'm constructing the a_U1 and a_U2 arrays by starting with a zero and scaling elements from the alpha and beta pools respectively.

Now I'm verifying the IV module setup—beta gets scaled by 0.5, and both dZ and dU follow the same pattern as the M-bias arrays with their own scaling factors. Everything checks out dimensionally. I'm ready to finalize the script and run it, then add some diagnostic output to the main function to print sample bias values, ASV ranges, and F1 versus bias records. For the dry-run validation, I'll confirm all 6 modules are producing output.

I also want to add optional matplotlib support for generating diagnostic plots—a scatter of F1 versus absolute bias and an ASV distribution by topology—but I'll wrap the import in a try-except since the server might not have it available. Now I need to write out the complete script and stop overthinking this. Let me also double-check the make_dgp_params_H0 function to ensure the DGP is set up correctly for the null hypothesis case.

Verifying that tau_true equals zero across all topologies: confounding blocks the effect through beta_T=0, mediation's direct effect is zero when we control for the mediator, collider has no causal path, exposure sets all category effects to zero, mbias isolates the unmeasured confounder, and the IV case similarly produces no treatment effect.

Now I'm checking the IV estimator more carefully—the reduced form is zero when the unmeasured confounder U is independent of the instrument Z, which it is by design. But the first stage isn't zero because Z affects A through the logit specification, so the Wald estimator is 0/FS, not the indeterminate 0/0 form.

In large samples, the reduced form stays near zero while the first stage remains nonzero, giving a Wald estimate close to zero. In finite samples though, the reduced form will fluctuate around zero due to sampling variation, making the ratio noisy and the standard error quite large.

For the frontdoor null hypothesis, I've set up a scenario where U has no causal effect, T is pure noise, M follows a fixed distribution independent of T, and Y is also pure noise. This means Y and T should be independent, so the regression should yield zero coefficients and tau should equal zero.

Now I'm concerned about shallow copying in the parameter dictionary—when I modify beta_T, I need to ensure I'm not accidentally sharing references to numpy arrays. Let me verify that the dictionary update creates proper independent copies of the parameters.

I should also add validation at the end to catch any NaN or Inf values in the output, and I need to handle the case where compute_plim returns NaN.

This can happen with weak instrumental variables, degenerate exposure matrices, or numerical instability with K=10. I'll make sure the downstream computations handle these gracefully.

The precomputation for K=10 with N=2M will take 30-60 seconds across all 7 topologies, which is acceptable for this dry-run. Now let me write out the complete script.

Actually, I should optimize for the mock mode—reducing the precomputation sample size to 500K when --mock is used will speed things up by 4x without sacrificing accuracy for testing purposes.

Writing the complete script...

Now I'm reconsidering the exposure topology DGP and how the bias computation works when the researcher uses a misspecified treatment variable instead of the true one.

For the sign flip ASV in exposure, this is particularly important because category effects can flip sign depending on the measurement error. Let me finalize the complete script that implements this empirical ASV calibration framework.

Writing the Python script... Writing setup code... Defining the parameter pools...

I've got all the coefficient ranges set up, so now I'm going to stop planning and just write the implementation directly. I need to make a couple of quick adjustments: use a smaller precomputation size for mock runs to speed things up, and dial back the Monte Carlo iterations.

For the Type I and Type II error rates with the IV topology and K=10, the Wald estimator gets really unstable and produces a lot of NaN values. I need to track which simulations actually produce valid estimates and compute the rejection rates only from those, rather than treating NaNs as failures.

Now I'll write the actual file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "24da2fde-1d4e-4c41-bb1f-2bcb40c79321",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QCobF1DFyt8NG4yWgZrhE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20962,
      "cache_read_input_tokens": 53694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20962
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

_source line 40_

Now I have a thorough understanding of all the existing code. Let me write the plan_006 script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "f8c935b3-0bed-4a46-abaa-1e46acbfeaa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QCobF1DFyt8NG4yWgZrhE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20962,
      "cache_read_input_tokens": 53694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20962
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

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to continue writing the plan_006 script. I had done extensive analysis of the existing codebase. Let me now write the file directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "3f66ff9c-d50a-4c3e-8921-84932a91502e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AoZ8btVKZFePWuwURE5LgV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 51112,
      "cache_read_input_tokens": 74656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 51112
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

_source line 42_

Writing the script now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "da0bcfc9-8f77-40d6-bb54-383d9bf34ce1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AoZ8btVKZFePWuwURE5LgV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 51112,
      "cache_read_input_tokens": 74656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 51112
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

_source line 43_

<details open><summary>🔧 Tool call — Write · `toolu_012TyRmnifM8X6gMTZFqKPay`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices\n\nUses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts\n= 27 C matrices) to compute:\n  1. Downstream causal bias across 7 DAG topologies\n  2. ASV sensitivity metrics (magnitude, significance, sign-flip)\n  3. F1 vs bias disconnect analysis (Baumann 2025 verification)\n  4. Type I/II error rates before/after ASV filtering\n  5. Inter-model error correlation\n\nInput:  data/{dataset}/{model}_{prompt}_annotations.jsonl\n        Each line: {\"true_label\": int, \"predicted_label\": int}\n\nOutput: artifacts/plan006/asv_empirical_results.json\n\nDependencies: numpy (required), matplotlib (optional for plots)\n\"\"\"\n\nimport numpy as np\nimport json\nimport argparse\nimport os\nimport time\nfrom collections import OrderedDict\n\ntry:\n    import matplotlib\n    matplotlib.use('Agg')\n    import matplotlib.pyplot as plt\n    HAS_MPL = True\nexcept ImportError:\n    HAS_MPL = False\n\n# ============================================================================\n# Constants\n# ============================================================================\n\nDATASETS = OrderedDict([\n    ('civil_comments', {'K': 2}),\n    ('vast', {'K': 3}),\n    ('humaid', {'K': 10}),\n])\n\nMODELS = ['llama4', 'qwen3', 'deepseek']\nPROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']\n\nTOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\n\nN_PRECOMP = 2_000_000\n\n# Parameter pools — K=3 values match plan_001/plan_005\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]\n\n\n# ============================================================================\n# Utility Functions\n# ============================================================================\n\ndef softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef ols_no_T(Y, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef wald_estimator(Z, Y, Astar, k=1):\n    z1 = Z == 1; z0 = Z == 0\n    n1, n0 = float(z1.sum()), float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    W = RF / FS\n    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    return W, np.sqrt(max(var_W, 0))\n\n\n# ============================================================================\n# DGP Parameters (general K, K=3 matches plan_001/plan_005)\n# ============================================================================\n\ndef make_p_A(K):\n    if K == 2:\n        return np.array([0.55, 0.45])\n    elif K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    else:\n        raw = np.array([1.0 / (i + 1) for i in range(K)])\n        return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A,\n            'alpha': np.array(_ALPHA_POOL[:K - 1]),\n            'beta_A': np.array(_BETA_A_POOL[:K - 1]),\n            'beta_T': 2.0,\n            'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'collider': {\n            'tau': 1.0,\n            'g': np.zeros(K),\n            'dT': np.array(_DT_POOL[:K]),\n            'dY': np.array(_DY_POOL[:K]),\n        },\n        'exposure': {\n            'beta': np.array(_BETA_POOL[:K]),\n            'p_A': p_A,\n        },\n    }\n    if K == 3:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(3),\n            'a_U1': np.array([0.0, 0.8, -0.5]),\n            'a_U2': np.array([0.0, 0.6, 0.9]),\n        }\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3),\n            'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array([0.0, 0.5, -0.3]),\n            'delta_fd': np.array([0.0, 1.0, -0.8]),\n            'beta': np.array([0.0, 1.0, -0.5]),\n        }\n    else:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(K),\n            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),\n            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),\n        }\n        iv_beta = np.array(_BETA_POOL[:K]) * 0.5\n        iv_beta[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_beta,\n            'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),\n        }\n        fd_delta = np.array(_DELTA_POOL[:K])\n        fd_delta[0] = 0.0\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta_fd': fd_delta,\n            'beta': np.array(_BETA_POOL[:K]),\n        }\n    return params\n\n\ndef make_dgp_params_H0(K, params):\n    p0 = {}\n    for topo, p in params.items():\n        if topo == 'confounding':\n            p0[topo] = dict(p, beta_T=0.0)\n        elif topo == 'mediation':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'collider':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'exposure':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'mbias':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'iv':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'frontdoor':\n            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,\n                            delta_fd=np.zeros(K), beta=np.zeros(K))\n    return p0\n\n\n# ============================================================================\n# DGP Generators (general K)\n# ============================================================================\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]\n              + p['a_U2'][None, :] * U2[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]\n              + p['dU'][None, :] * U[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    M = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\nGEN_FNS = {\n    'confounding': gen_confounding, 'mediation': gen_mediation,\n    'collider': gen_collider, 'exposure': gen_exposure,\n    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,\n}\n\n\n# ============================================================================\n# Sufficient Statistics & Plim (general K)\n# ============================================================================\n\ndef precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):\n    rng = np.random.default_rng(seed)\n    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    if topology == 'iv':\n        Z = first_var\n        z1 = Z == 1; z0 = Z == 0\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n        return dict(RF=RF, FS=FS, topology='iv')\n    elif topology == 'exposure':\n        return dict(p_A=DA.mean(0), E_Y=Y.mean(),\n                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')\n    else:\n        T = first_var\n        return dict(\n            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),\n            E_Y=Y.mean(), E_TY=(T * Y).mean(),\n            E_TD=(DA * T[:, None]).mean(0),\n            E_YD=(DA * Y[:, None]).mean(0), topology=topology)\n\n\ndef compute_plim(C, st, K):\n    if st['topology'] == 'iv':\n        FS_star = C @ st['FS']\n        if abs(FS_star[1]) < 1e-8:\n            return np.nan\n        return st['RF'] / FS_star[1]\n    elif st['topology'] == 'exposure':\n        q = C @ st['p_A']\n        cy = C @ st['E_YD']\n        EZZ = np.zeros((K, K))\n        EZZ[0, 0] = 1.0\n        for j in range(1, K):\n            EZZ[0, j] = EZZ[j, 0] = q[j]\n            EZZ[j, j] = q[j]\n        EZY = np.zeros(K)\n        EZY[0] = st['E_Y']\n        for j in range(1, K):\n            EZY[j] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(K, np.nan)\n    else:\n        q = C @ st['p_A']\n        ct = C @ st['E_TD']\n        cy = C @ st['E_YD']\n        dim = K + 1\n        EZZ = np.zeros((dim, dim))\n        EZZ[0, 0] = 1.0\n        EZZ[0, 1] = EZZ[1, 0] = st['E_T']\n        EZZ[1, 1] = st['E_T2']\n        for j in range(1, K):\n            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]\n            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]\n            EZZ[j + 1, j + 1] = q[j]\n        EZY = np.zeros(dim)\n        EZY[0] = st['E_Y']\n        EZY[1] = st['E_TY']\n        for j in range(1, K):\n            EZY[j + 1] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(dim, np.nan)\n\n\ndef extract_tau(plim_result, topology):\n    if topology == 'iv':\n        return float(plim_result) if np.isfinite(plim_result) else np.nan\n    if isinstance(plim_result, np.ndarray):\n        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan\n    return np.nan\n\n\n# ============================================================================\n# 1. Data Loading & Confusion Matrix\n# ============================================================================\n\ndef load_annotations(data_dir, dataset, model, prompt):\n    path = os.path.join(data_dir, dataset, f\"{model}_{prompt}_annotations.jsonl\")\n    records = []\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line.strip())\n            records.append((int(rec['true_label']), int(rec['predicted_label'])))\n    return records\n\n\ndef build_confusion_matrix(records, K):\n    counts = np.zeros((K, K))\n    for true_k, pred_k in records:\n        if 0 <= true_k < K and 0 <= pred_k < K:\n            counts[pred_k, true_k] += 1\n    col_sums = counts.sum(axis=0)\n    col_sums = np.where(col_sums < 1, 1, col_sums)\n    return counts / col_sums\n\n\ndef load_all_confusion_matrices(data_dir):\n    matrices = {}\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        for model in MODELS:\n            for prompt in PROMPTS:\n                try:\n                    records = load_annotations(data_dir, dataset, model, prompt)\n                    C = build_confusion_matrix(records, K)\n                    matrices[(dataset, model, prompt)] = C\n                except FileNotFoundError:\n                    print(f\"  [WARN] Missing: {dataset}/{model}_{prompt}\")\n    return matrices\n\n\n# ============================================================================\n# 2. Downstream Causal Bias\n# ============================================================================\n\ndef compute_bias_for_topology(C, K, topology, st, tau_true):\n    plim_result = compute_plim(C, st, K)\n    tau_hat = extract_tau(plim_result, topology)\n    if np.isnan(tau_hat) or np.isnan(tau_true):\n        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}\n    bias = tau_hat - tau_true\n    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None\n    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)\n    return {\n        'tau_hat': float(tau_hat), 'bias': float(bias),\n        'bias_pct': float(bias_pct) if bias_pct is not None else None,\n        'sign_flip': sign_flip,\n    }\n\n\ndef compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            info = compute_bias_for_topology(C, K, topology, st, tau_true)\n            results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **info,\n            })\n    return results\n\n\n# ============================================================================\n# 3. ASV Computation\n# ============================================================================\n\ndef C_interpolated(C0, delta, K):\n    C_d = (1 - delta) * np.eye(K) + delta * C0\n    C_d = np.maximum(C_d, 0.0)\n    col_sums = C_d.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C_d / col_sums\n\n\ndef compute_delta_max(C0):\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - min_diag), 10.0)\n\n\ndef compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,\n                           n_grid=1500, se_ref=None):\n    dmax = compute_delta_max(C0)\n    deltas = np.linspace(0, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = C_interpolated(C0, d, K)\n        plim_result = compute_plim(C_d, st, K)\n        tau_curve[i] = extract_tau(plim_result, topology)\n\n    bias_abs = np.abs(tau_curve - tau_true)\n    envelope = np.zeros(n_grid)\n    running_max = 0.0\n    for i in range(n_grid):\n        if np.isfinite(bias_abs[i]):\n            running_max = max(running_max, bias_abs[i])\n        envelope[i] = running_max\n\n    if asv_type == 'sign_flip':\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'magnitude':\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = 0.1 * abs(tau_true)\n        for i in range(n_grid):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'significance':\n        if se_ref is None or se_ref < 1e-12:\n            return None\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:\n                return float(deltas[i])\n        return None\n    return None\n\n\ndef estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n    tau_hats = []\n    for _ in range(n_mc):\n        first_var, Y, A = gen_fn(K, N_ref, params, rng)\n        if topology == 'iv':\n            th, _ = wald_estimator(first_var, Y, A, k=1)\n        elif topology == 'exposure':\n            b, _ = ols_no_T(Y, A, K)\n            th = b[1]\n        else:\n            b, _ = ols_with_dummies(Y, first_var, A, K)\n            th = b[1]\n        if np.isfinite(th):\n            tau_hats.append(th)\n    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan\n\n\ndef compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            se_ref = all_se_ref.get((K, topology))\n            for asv_type in ['magnitude', 'significance', 'sign_flip']:\n                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,\n                                             asv_type, se_ref=se_ref)\n                results.append({\n                    'dataset': dataset, 'model': model, 'prompt': prompt,\n                    'K': K, 'topology': topology, 'asv_type': asv_type,\n                    'asv': asv,\n                })\n    return results\n\n\n# ============================================================================\n# 4. F1 vs Downstream Bias\n# ============================================================================\n\ndef compute_f1_from_C(C, K, p_A=None):\n    if p_A is None:\n        p_A = np.ones(K) / K\n    precision = np.zeros(K)\n    recall = np.zeros(K)\n    f1 = np.zeros(K)\n    for i in range(K):\n        recall[i] = C[i, i]\n        denom = sum(C[i, j] * p_A[j] for j in range(K))\n        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0\n        if precision[i] + recall[i] > 1e-12:\n            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])\n    return {\n        'macro_f1': float(f1.mean()),\n        'weighted_f1': float((p_A * f1).sum()),\n        'per_class_f1': f1.tolist(),\n    }\n\n\ndef f1_vs_bias_analysis(confusion_matrices, biases):\n    results = []\n    for b in biases:\n        key = (b['dataset'], b['model'], b['prompt'])\n        if key not in confusion_matrices:\n            continue\n        C = confusion_matrices[key]\n        K = b['K']\n        p_A = make_p_A(K)\n        f1_info = compute_f1_from_C(C, K, p_A)\n        abs_bias = abs(b['bias']) if b['bias'] is not None else None\n        results.append({\n            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],\n            'K': K, 'topology': b['topology'],\n            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],\n            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],\n            'sign_flip': b['sign_flip'],\n        })\n    return results\n\n\n# ============================================================================\n# 5. Type I/II Error Rates\n# ============================================================================\n\ndef compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,\n                              st_H1, tau_true,\n                              n_sim=100, N_sample=5000, seed=42):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n\n    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')\n    asv_safe = (masv is None or masv > 1.0)\n\n    def _run_mc(params_t, n):\n        valid = 0; rej = 0\n        for _ in range(n):\n            fv, Y, A = gen_fn(K, N_sample, params_t, rng)\n            Astar = generate_Astar(A, C, rng)\n            if topology == 'iv':\n                th, se = wald_estimator(fv, Y, Astar, k=1)\n            elif topology == 'exposure':\n                b, svec = ols_no_T(Y, Astar, K)\n                th, se = b[1], svec[1]\n            else:\n                b, svec = ols_with_dummies(Y, fv, Astar, K)\n                th, se = b[1], svec[1]\n            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:\n                valid += 1\n                if abs(th / se) > 1.96:\n                    rej += 1\n        return rej / max(valid, 1), valid\n\n    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)\n    type1_after = type1_before if asv_safe else 0.0\n    power_after = power_before if asv_safe else 0.0\n\n    return {\n        'type1_before': float(type1_before), 'type1_after': float(type1_after),\n        'power_before': float(power_before), 'power_after': float(power_after),\n        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,\n        'valid_h0': int(v0), 'valid_h1': int(v1),\n    }\n\n\n# ============================================================================\n# 6. Inter-model Error Correlation\n# ============================================================================\n\ndef compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,\n                                    n_samples=1000, seed=42):\n    rng = np.random.default_rng(seed)\n    p_A = make_p_A(K)\n    true_labels = rng.choice(K, size=n_samples, p=p_A)\n\n    predictions = {}\n    for model in MODELS:\n        key = (dataset, model, prompt)\n        if key in confusion_matrices:\n            predictions[model] = generate_Astar(true_labels,\n                                                confusion_matrices[key], rng)\n        else:\n            predictions[model] = true_labels.copy()\n\n    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]\n    results = {}\n    for m1, m2 in pairs:\n        p1, p2 = predictions[m1], predictions[m2]\n        agreement = float((p1 == p2).mean())\n        observed = agreement\n        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))\n        kappa = float((observed - expected) / (1 - expected)\n                      ) if expected < 1 - 1e-10 else 0.0\n        err1 = (p1 != true_labels).astype(float)\n        err2 = (p2 != true_labels).astype(float)\n        if err1.std() > 1e-10 and err2.std() > 1e-10:\n            error_corr = float(np.corrcoef(err1, err2)[0, 1])\n        else:\n            error_corr = 0.0\n        results[f\"{m1}-{m2}\"] = {\n            'agreement': agreement,\n            'kappa': kappa,\n            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,\n        }\n    return results\n\n\n# ============================================================================\n# Mock Data Generation\n# ============================================================================\n\ndef generate_mock_C(K, rng, diag_range):\n    C = np.zeros((K, K))\n    for j in range(K):\n        diag_val = rng.uniform(diag_range[0], diag_range[1])\n        remaining = 1.0 - diag_val\n        if K > 2:\n            dists = np.abs(np.arange(K) - j).astype(float)\n            dists[j] = np.inf\n            weights = 1.0 / dists\n            weights[j] = 0\n            noise = rng.uniform(0.5, 1.5, K)\n            noise[j] = 0\n            weights = weights * noise\n            weights /= weights.sum()\n            C[:, j] = remaining * weights\n        else:\n            C[1 - j, j] = remaining\n        C[j, j] = diag_val\n    return C\n\n\ndef generate_mock_confusion_matrices(seed=12345):\n    rng = np.random.default_rng(seed)\n    matrices = {}\n    diag_ranges = {\n        'civil_comments': (0.85, 0.95),\n        'vast': (0.70, 0.90),\n        'humaid': (0.60, 0.85),\n    }\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        dr = diag_ranges[dataset]\n        for model in MODELS:\n            for prompt in PROMPTS:\n                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)\n    return matrices\n\n\n# ============================================================================\n# Diagnostic Plots (optional)\n# ============================================================================\n\ndef save_f1_vs_bias_plot(f1_bias, output_dir):\n    if not HAS_MPL:\n        return\n    fig, axes = plt.subplots(2, 4, figsize=(20, 10))\n    axes = axes.flatten()\n    for idx, topo in enumerate(TOPOLOGIES):\n        ax = axes[idx]\n        subset = [r for r in f1_bias if r['topology'] == topo\n                  and r['abs_bias'] is not None]\n        if not subset:\n            ax.set_title(topo)\n            continue\n        f1s = [r['macro_f1'] for r in subset]\n        biases = [r['abs_bias'] for r in subset]\n        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]\n        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)\n        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)\n        ax.set_xlabel('Macro F1')\n        ax.set_ylabel('|bias|')\n        ax.set_title(topo)\n    if len(TOPOLOGIES) < 8:\n        axes[-1].axis('off')\n    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)\n    plt.close(fig)\n\n\ndef save_asv_heatmap(asvs, output_dir):\n    if not HAS_MPL:\n        return\n    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']\n    datasets_list = list(DATASETS.keys())\n    fig, axes = plt.subplots(1, 3, figsize=(18, 6))\n    for didx, dataset in enumerate(datasets_list):\n        ax = axes[didx]\n        subset = [r for r in mag_asvs if r['dataset'] == dataset]\n        configs = sorted(set((r['model'], r['prompt']) for r in subset))\n        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)\n        for r in subset:\n            ti = TOPOLOGIES.index(r['topology'])\n            ci = configs.index((r['model'], r['prompt']))\n            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan\n        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',\n                       vmin=0, vmax=2)\n        ax.set_xticks(range(len(configs)))\n        ax.set_xticklabels([f\"{m[:3]}_{p[:3]}\" for m, p in configs],\n                           rotation=45, ha='right', fontsize=7)\n        ax.set_yticks(range(len(TOPOLOGIES)))\n        ax.set_yticklabels(TOPOLOGIES, fontsize=8)\n        ax.set_title(f'{dataset} (K={DATASETS[dataset][\"K\"]})')\n        plt.colorbar(im, ax=ax, shrink=0.8)\n    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)\n    plt.close(fig)\n\n\n# ============================================================================\n# JSON Serialization\n# ============================================================================\n\ndef _to_json_safe(obj):\n    if isinstance(obj, np.integer):\n        return int(obj)\n    elif isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    elif isinstance(obj, np.ndarray):\n        return _to_json_safe(obj.tolist())\n    elif isinstance(obj, dict):\n        return {str(k): _to_json_safe(v) for k, v in obj.items()}\n    elif isinstance(obj, list):\n        return [_to_json_safe(v) for v in obj]\n    elif isinstance(obj, (bool, np.bool_)):\n        return bool(obj)\n    elif isinstance(obj, float):\n        return None if (np.isnan(obj) or np.isinf(obj)) else obj\n    return obj\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')\n    parser.add_argument('--data-dir', default='data/')\n    parser.add_argument('--output-dir', default='artifacts/plan006/')\n    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')\n    parser.add_argument('--n-sim', type=int, default=1000)\n    parser.add_argument('--device', type=str, default='cpu')\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    t_total = time.time()\n    n_precomp = 500_000 if args.mock else N_PRECOMP\n\n    print(\"=\" * 70)\n    print(\"plan_006: Empirical ASV Calibration\")\n    print(\"=\" * 70)\n\n    # --- 1. Confusion matrices ---\n    if args.mock:\n        print(\"\\n[1/6] Generating mock confusion matrices...\")\n        confusion_matrices = generate_mock_confusion_matrices()\n    else:\n        print(\"\\n[1/6] Loading confusion matrices...\")\n        confusion_matrices = load_all_confusion_matrices(args.data_dir)\n\n    print(f\"  {len(confusion_matrices)} matrices loaded\")\n    for (ds, m, p), C in list(confusion_matrices.items())[:3]:\n        K = DATASETS[ds]['K']\n        print(f\"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}\")\n\n    # --- 2. Precompute sufficient statistics ---\n    print(\"\\n[2/6] Precomputing sufficient statistics...\")\n    K_values = sorted(set(DATASETS[ds]['K'] for ds in DATASETS))\n    all_suff_stats = {}\n    all_tau_true = {}\n    all_params = {}\n    all_params_H0 = {}\n    all_se_ref = {}\n\n    for K in K_values:\n        params = make_dgp_params(K)\n        params_H0 = make_dgp_params_H0(K, params)\n        all_params[K] = params\n        all_params_H0[K] = params_H0\n        for topology in TOPOLOGIES:\n            seed = K * 1000 + abs(hash(topology)) % 1000\n            st = precompute_suff_stats(K, topology, params[topology],\n                                       N=n_precomp, seed=seed)\n            plim_I = compute_plim(np.eye(K), st, K)\n            tau_true = extract_tau(plim_I, topology)\n            all_suff_stats[(K, topology)] = st\n            all_tau_true[(K, topology)] = tau_true\n\n            se = estimate_reference_se(K, topology, params[topology],\n                                       N_ref=5000,\n                                       n_mc=min(args.n_sim, 30),\n                                       seed=seed + 500)\n            all_se_ref[(K, topology)] = se\n            se_s = f\"{se:.4f}\" if np.isfinite(se) else \"N/A\"\n            print(f\"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}\")\n\n    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)\n    n_sign_flips = sum(1 for b in biases if b['sign_flip'])\n    print(f\"  {len(biases)} bias values ({n_sign_flips} sign flips)\")\n\n    # --- 3. ASV ---\n    print(\"\\n[3/6] Computing ASV values...\")\n    t3 = time.time()\n    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,\n                            all_tau_true, all_se_ref)\n    print(f\"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)\")\n    for at in ['magnitude', 'sign_flip', 'significance']:\n        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]\n        if sub:\n            print(f\"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} \"\n                  f\"max={max(sub):.3f} ({len(sub)} non-None)\")\n\n    # --- 4. F1 vs bias ---\n    print(\"\\n[4/6] F1 vs bias analysis...\")\n    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)\n    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]\n    high_f1_high_bias = [r for r in total_high_f1\n                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]\n    if total_high_f1:\n        pct = len(high_f1_high_bias) / len(total_high_f1) * 100\n        print(f\"  Baumann check: F1>0.93 with |bias|>0.05: \"\n              f\"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%\")\n    # Sample rows\n    for r in f1_bias[:3]:\n        print(f\"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: \"\n              f\"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}\")\n\n    # --- 5. Type I/II ---\n    print(\"\\n[5/6] Type I/II error rates...\")\n    t5 = time.time()\n    type1_type2_results = []\n    n_configs = len(confusion_matrices) * len(TOPOLOGIES)\n    idx = 0\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            idx += 1\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            r = compute_type1_type2_for_C(\n                C, K, topology, all_params[K], all_params_H0[K],\n                st, tau_true,\n                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)\n            type1_type2_results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **r,\n            })\n            if idx % 50 == 0:\n                print(f\"    {idx}/{n_configs}...\")\n    print(f\"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)\")\n    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])\n    print(f\"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}\")\n\n    # --- 6. Inter-model correlation ---\n    print(\"\\n[6/6] Inter-model error correlation...\")\n    inter_model_results = {}\n    for dataset in DATASETS:\n        K = DATASETS[dataset]['K']\n        for prompt in PROMPTS:\n            r = compute_inter_model_correlation(\n                confusion_matrices, K, dataset, prompt,\n                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)\n            inter_model_results[f\"{dataset}_{prompt}\"] = r\n    print(f\"  {len(inter_model_results)} (dataset, prompt) pairs\")\n    for key, pairs in list(inter_model_results.items())[:2]:\n        for pair, vals in pairs.items():\n            print(f\"    {key} {pair}: agree={vals['agreement']:.3f} \"\n                  f\"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}\")\n\n    # --- Summary ---\n    summary = {\n        'f1_gt_093_total': len(total_high_f1),\n        'f1_gt_093_with_high_bias_pct': (\n            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),\n        'ppi_recommended_scenarios': unsafe,\n        'total_scenarios': len(type1_type2_results),\n        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,\n    }\n\n    # --- Save ---\n    output = _to_json_safe({\n        'confusion_matrices': {\n            f\"{ds}_{m}_{p}\": C.tolist()\n            for (ds, m, p), C in confusion_matrices.items()\n        },\n        'biases': biases,\n        'asvs': asvs,\n        'f1_vs_bias': f1_bias,\n        'type1_type2': type1_type2_results,\n        'inter_model_correlation': inter_model_results,\n        'summary': summary,\n    })\n\n    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n    # --- Plots ---\n    save_f1_vs_bias_plot(f1_bias, args.output_dir)\n    save_asv_heatmap(asvs, args.output_dir)\n    if HAS_MPL:\n        print(f\"Plots saved to {args.output_dir}\")\n\n    # --- Validation ---\n    with open(out_path) as f:\n        data = json.load(f)\n    n_null = str(data).count('null')\n    print(f\"\\nValidation: JSON has {n_null} null values \"\n          f\"(expected for NaN/None ASV entries)\")\n    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:\n        print(f\"  {section}: {len(data[section])} records\")\n\n    elapsed = time.time() - t_total\n    print(f\"\\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)\")\n    print(f\"\\nSummary:\")\n    print(f\"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%\")\n    print(f\"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/\"\n          f\"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "e50570e5-248b-4216-8d02-f5f4429d023d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mbct8P1bEQiJXkeBdsobjk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 125768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 44 · 2026-05-20T21:23:20.327Z_

<details><summary>↩ Tool result · `toolu_012TyRmnifM8X6gMTZFqKPay`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "45385cad-34e6-40a9-8159-47a503dc8441",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices\n\nUses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts\n= 27 C matrices) to compute:\n  1. Downstream causal bias across 7 DAG topologies\n  2. ASV sensitivity metrics (magnitude, significance, sign-flip)\n  3. F1 vs bias disconnect analysis (Baumann 2025 verification)\n  4. Type I/II error rates before/after ASV filtering\n  5. Inter-model error correlation\n\nInput:  data/{dataset}/{model}_{prompt}_annotations.jsonl\n        Each line: {\"true_label\": int, \"predicted_label\": int}\n\nOutput: artifacts/plan006/asv_empirical_results.json\n\nDependencies: numpy (required), matplotlib (optional for plots)\n\"\"\"\n\nimport numpy as np\nimport json\nimport argparse\nimport os\nimport time\nfrom collections import OrderedDict\n\ntry:\n    import matplotlib\n    matplotlib.use('Agg')\n    import matplotlib.pyplot as plt\n    HAS_MPL = True\nexcept ImportError:\n    HAS_MPL = False\n\n# ============================================================================\n# Constants\n# ============================================================================\n\nDATASETS = OrderedDict([\n    ('civil_comments', {'K': 2}),\n    ('vast', {'K': 3}),\n    ('humaid', {'K': 10}),\n])\n\nMODELS = ['llama4', 'qwen3', 'deepseek']\nPROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']\n\nTOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\n\nN_PRECOMP = 2_000_000\n\n# Parameter pools — K=3 values match plan_001/plan_005\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]\n\n\n# ============================================================================\n# Utility Functions\n# ============================================================================\n\ndef softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef ols_no_T(Y, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef wald_estimator(Z, Y, Astar, k=1):\n    z1 = Z == 1; z0 = Z == 0\n    n1, n0 = float(z1.sum()), float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    W = RF / FS\n    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    return W, np.sqrt(max(var_W, 0))\n\n\n# ============================================================================\n# DGP Parameters (general K, K=3 matches plan_001/plan_005)\n# ============================================================================\n\ndef make_p_A(K):\n    if K == 2:\n        return np.array([0.55, 0.45])\n    elif K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    else:\n        raw = np.array([1.0 / (i + 1) for i in range(K)])\n        return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A,\n            'alpha': np.array(_ALPHA_POOL[:K - 1]),\n            'beta_A': np.array(_BETA_A_POOL[:K - 1]),\n            'beta_T': 2.0,\n            'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'collider': {\n            'tau': 1.0,\n            'g': np.zeros(K),\n            'dT': np.array(_DT_POOL[:K]),\n            'dY': np.array(_DY_POOL[:K]),\n        },\n        'exposure': {\n            'beta': np.array(_BETA_POOL[:K]),\n            'p_A': p_A,\n        },\n    }\n    if K == 3:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(3),\n            'a_U1': np.array([0.0, 0.8, -0.5]),\n            'a_U2': np.array([0.0, 0.6, 0.9]),\n        }\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3),\n            'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array([0.0, 0.5, -0.3]),\n            'delta_fd': np.array([0.0, 1.0, -0.8]),\n            'beta': np.array([0.0, 1.0, -0.5]),\n        }\n    else:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(K),\n            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),\n            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),\n        }\n        iv_beta = np.array(_BETA_POOL[:K]) * 0.5\n        iv_beta[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_beta,\n            'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),\n        }\n        fd_delta = np.array(_DELTA_POOL[:K])\n        fd_delta[0] = 0.0\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta_fd': fd_delta,\n            'beta': np.array(_BETA_POOL[:K]),\n        }\n    return params\n\n\ndef make_dgp_params_H0(K, params):\n    p0 = {}\n    for topo, p in params.items():\n        if topo == 'confounding':\n            p0[topo] = dict(p, beta_T=0.0)\n        elif topo == 'mediation':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'collider':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'exposure':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'mbias':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'iv':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'frontdoor':\n            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,\n                            delta_fd=np.zeros(K), beta=np.zeros(K))\n    return p0\n\n\n# ============================================================================\n# DGP Generators (general K)\n# ============================================================================\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]\n              + p['a_U2'][None, :] * U2[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]\n              + p['dU'][None, :] * U[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    M = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\nGEN_FNS = {\n    'confounding': gen_confounding, 'mediation': gen_mediation,\n    'collider': gen_collider, 'exposure': gen_exposure,\n    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,\n}\n\n\n# ============================================================================\n# Sufficient Statistics & Plim (general K)\n# ============================================================================\n\ndef precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):\n    rng = np.random.default_rng(seed)\n    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    if topology == 'iv':\n        Z = first_var\n        z1 = Z == 1; z0 = Z == 0\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n        return dict(RF=RF, FS=FS, topology='iv')\n    elif topology == 'exposure':\n        return dict(p_A=DA.mean(0), E_Y=Y.mean(),\n                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')\n    else:\n        T = first_var\n        return dict(\n            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),\n            E_Y=Y.mean(), E_TY=(T * Y).mean(),\n            E_TD=(DA * T[:, None]).mean(0),\n            E_YD=(DA * Y[:, None]).mean(0), topology=topology)\n\n\ndef compute_plim(C, st, K):\n    if st['topology'] == 'iv':\n        FS_star = C @ st['FS']\n        if abs(FS_star[1]) < 1e-8:\n            return np.nan\n        return st['RF'] / FS_star[1]\n    elif st['topology'] == 'exposure':\n        q = C @ st['p_A']\n        cy = C @ st['E_YD']\n        EZZ = np.zeros((K, K))\n        EZZ[0, 0] = 1.0\n        for j in range(1, K):\n            EZZ[0, j] = EZZ[j, 0] = q[j]\n            EZZ[j, j] = q[j]\n        EZY = np.zeros(K)\n        EZY[0] = st['E_Y']\n        for j in range(1, K):\n            EZY[j] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(K, np.nan)\n    else:\n        q = C @ st['p_A']\n        ct = C @ st['E_TD']\n        cy = C @ st['E_YD']\n        dim = K + 1\n        EZZ = np.zeros((dim, dim))\n        EZZ[0, 0] = 1.0\n        EZZ[0, 1] = EZZ[1, 0] = st['E_T']\n        EZZ[1, 1] = st['E_T2']\n        for j in range(1, K):\n            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]\n            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]\n            EZZ[j + 1, j + 1] = q[j]\n        EZY = np.zeros(dim)\n        EZY[0] = st['E_Y']\n        EZY[1] = st['E_TY']\n        for j in range(1, K):\n            EZY[j + 1] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(dim, np.nan)\n\n\ndef extract_tau(plim_result, topology):\n    if topology == 'iv':\n        return float(plim_result) if np.isfinite(plim_result) else np.nan\n    if isinstance(plim_result, np.ndarray):\n        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan\n    return np.nan\n\n\n# ============================================================================\n# 1. Data Loading & Confusion Matrix\n# ============================================================================\n\ndef load_annotations(data_dir, dataset, model, prompt):\n    path = os.path.join(data_dir, dataset, f\"{model}_{prompt}_annotations.jsonl\")\n    records = []\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line.strip())\n            records.append((int(rec['true_label']), int(rec['predicted_label'])))\n    return records\n\n\ndef build_confusion_matrix(records, K):\n    counts = np.zeros((K, K))\n    for true_k, pred_k in records:\n        if 0 <= true_k < K and 0 <= pred_k < K:\n            counts[pred_k, true_k] += 1\n    col_sums = counts.sum(axis=0)\n    col_sums = np.where(col_sums < 1, 1, col_sums)\n    return counts / col_sums\n\n\ndef load_all_confusion_matrices(data_dir):\n    matrices = {}\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        for model in MODELS:\n            for prompt in PROMPTS:\n                try:\n                    records = load_annotations(data_dir, dataset, model, prompt)\n                    C = build_confusion_matrix(records, K)\n                    matrices[(dataset, model, prompt)] = C\n                except FileNotFoundError:\n                    print(f\"  [WARN] Missing: {dataset}/{model}_{prompt}\")\n    return matrices\n\n\n# ============================================================================\n# 2. Downstream Causal Bias\n# ============================================================================\n\ndef compute_bias_for_topology(C, K, topology, st, tau_true):\n    plim_result = compute_plim(C, st, K)\n    tau_hat = extract_tau(plim_result, topology)\n    if np.isnan(tau_hat) or np.isnan(tau_true):\n        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}\n    bias = tau_hat - tau_true\n    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None\n    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)\n    return {\n        'tau_hat': float(tau_hat), 'bias': float(bias),\n        'bias_pct': float(bias_pct) if bias_pct is not None else None,\n        'sign_flip': sign_flip,\n    }\n\n\ndef compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            info = compute_bias_for_topology(C, K, topology, st, tau_true)\n            results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **info,\n            })\n    return results\n\n\n# ============================================================================\n# 3. ASV Computation\n# ============================================================================\n\ndef C_interpolated(C0, delta, K):\n    C_d = (1 - delta) * np.eye(K) + delta * C0\n    C_d = np.maximum(C_d, 0.0)\n    col_sums = C_d.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C_d / col_sums\n\n\ndef compute_delta_max(C0):\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - min_diag), 10.0)\n\n\ndef compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,\n                           n_grid=1500, se_ref=None):\n    dmax = compute_delta_max(C0)\n    deltas = np.linspace(0, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = C_interpolated(C0, d, K)\n        plim_result = compute_plim(C_d, st, K)\n        tau_curve[i] = extract_tau(plim_result, topology)\n\n    bias_abs = np.abs(tau_curve - tau_true)\n    envelope = np.zeros(n_grid)\n    running_max = 0.0\n    for i in range(n_grid):\n        if np.isfinite(bias_abs[i]):\n            running_max = max(running_max, bias_abs[i])\n        envelope[i] = running_max\n\n    if asv_type == 'sign_flip':\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'magnitude':\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = 0.1 * abs(tau_true)\n        for i in range(n_grid):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'significance':\n        if se_ref is None or se_ref < 1e-12:\n            return None\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:\n                return float(deltas[i])\n        return None\n    return None\n\n\ndef estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n    tau_hats = []\n    for _ in range(n_mc):\n        first_var, Y, A = gen_fn(K, N_ref, params, rng)\n        if topology == 'iv':\n            th, _ = wald_estimator(first_var, Y, A, k=1)\n        elif topology == 'exposure':\n            b, _ = ols_no_T(Y, A, K)\n            th = b[1]\n        else:\n            b, _ = ols_with_dummies(Y, first_var, A, K)\n            th = b[1]\n        if np.isfinite(th):\n            tau_hats.append(th)\n    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan\n\n\ndef compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            se_ref = all_se_ref.get((K, topology))\n            for asv_type in ['magnitude', 'significance', 'sign_flip']:\n                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,\n                                             asv_type, se_ref=se_ref)\n                results.append({\n                    'dataset': dataset, 'model': model, 'prompt': prompt,\n                    'K': K, 'topology': topology, 'asv_type': asv_type,\n                    'asv': asv,\n                })\n    return results\n\n\n# ============================================================================\n# 4. F1 vs Downstream Bias\n# ============================================================================\n\ndef compute_f1_from_C(C, K, p_A=None):\n    if p_A is None:\n        p_A = np.ones(K) / K\n    precision = np.zeros(K)\n    recall = np.zeros(K)\n    f1 = np.zeros(K)\n    for i in range(K):\n        recall[i] = C[i, i]\n        denom = sum(C[i, j] * p_A[j] for j in range(K))\n        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0\n        if precision[i] + recall[i] > 1e-12:\n            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])\n    return {\n        'macro_f1': float(f1.mean()),\n        'weighted_f1': float((p_A * f1).sum()),\n        'per_class_f1': f1.tolist(),\n    }\n\n\ndef f1_vs_bias_analysis(confusion_matrices, biases):\n    results = []\n    for b in biases:\n        key = (b['dataset'], b['model'], b['prompt'])\n        if key not in confusion_matrices:\n            continue\n        C = confusion_matrices[key]\n        K = b['K']\n        p_A = make_p_A(K)\n        f1_info = compute_f1_from_C(C, K, p_A)\n        abs_bias = abs(b['bias']) if b['bias'] is not None else None\n        results.append({\n            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],\n            'K': K, 'topology': b['topology'],\n            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],\n            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],\n            'sign_flip': b['sign_flip'],\n        })\n    return results\n\n\n# ============================================================================\n# 5. Type I/II Error Rates\n# ============================================================================\n\ndef compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,\n                              st_H1, tau_true,\n                              n_sim=100, N_sample=5000, seed=42):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n\n    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')\n    asv_safe = (masv is None or masv > 1.0)\n\n    def _run_mc(params_t, n):\n        valid = 0; rej = 0\n        for _ in range(n):\n            fv, Y, A = gen_fn(K, N_sample, params_t, rng)\n            Astar = generate_Astar(A, C, rng)\n            if topology == 'iv':\n                th, se = wald_estimator(fv, Y, Astar, k=1)\n            elif topology == 'exposure':\n                b, svec = ols_no_T(Y, Astar, K)\n                th, se = b[1], svec[1]\n            else:\n                b, svec = ols_with_dummies(Y, fv, Astar, K)\n                th, se = b[1], svec[1]\n            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:\n                valid += 1\n                if abs(th / se) > 1.96:\n                    rej += 1\n        return rej / max(valid, 1), valid\n\n    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)\n    type1_after = type1_before if asv_safe else 0.0\n    power_after = power_before if asv_safe else 0.0\n\n    return {\n        'type1_before': float(type1_before), 'type1_after': float(type1_after),\n        'power_before': float(power_before), 'power_after': float(power_after),\n        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,\n        'valid_h0': int(v0), 'valid_h1': int(v1),\n    }\n\n\n# ============================================================================\n# 6. Inter-model Error Correlation\n# ============================================================================\n\ndef compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,\n                                    n_samples=1000, seed=42):\n    rng = np.random.default_rng(seed)\n    p_A = make_p_A(K)\n    true_labels = rng.choice(K, size=n_samples, p=p_A)\n\n    predictions = {}\n    for model in MODELS:\n        key = (dataset, model, prompt)\n        if key in confusion_matrices:\n            predictions[model] = generate_Astar(true_labels,\n                                                confusion_matrices[key], rng)\n        else:\n            predictions[model] = true_labels.copy()\n\n    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]\n    results = {}\n    for m1, m2 in pairs:\n        p1, p2 = predictions[m1], predictions[m2]\n        agreement = float((p1 == p2).mean())\n        observed = agreement\n        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))\n        kappa = float((observed - expected) / (1 - expected)\n                      ) if expected < 1 - 1e-10 else 0.0\n        err1 = (p1 != true_labels).astype(float)\n        err2 = (p2 != true_labels).astype(float)\n        if err1.std() > 1e-10 and err2.std() > 1e-10:\n            error_corr = float(np.corrcoef(err1, err2)[0, 1])\n        else:\n            error_corr = 0.0\n        results[f\"{m1}-{m2}\"] = {\n            'agreement': agreement,\n            'kappa': kappa,\n            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,\n        }\n    return results\n\n\n# ============================================================================\n# Mock Data Generation\n# ============================================================================\n\ndef generate_mock_C(K, rng, diag_range):\n    C = np.zeros((K, K))\n    for j in range(K):\n        diag_val = rng.uniform(diag_range[0], diag_range[1])\n        remaining = 1.0 - diag_val\n        if K > 2:\n            dists = np.abs(np.arange(K) - j).astype(float)\n            dists[j] = np.inf\n            weights = 1.0 / dists\n            weights[j] = 0\n            noise = rng.uniform(0.5, 1.5, K)\n            noise[j] = 0\n            weights = weights * noise\n            weights /= weights.sum()\n            C[:, j] = remaining * weights\n        else:\n            C[1 - j, j] = remaining\n        C[j, j] = diag_val\n    return C\n\n\ndef generate_mock_confusion_matrices(seed=12345):\n    rng = np.random.default_rng(seed)\n    matrices = {}\n    diag_ranges = {\n        'civil_comments': (0.85, 0.95),\n        'vast': (0.70, 0.90),\n        'humaid': (0.60, 0.85),\n    }\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        dr = diag_ranges[dataset]\n        for model in MODELS:\n            for prompt in PROMPTS:\n                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)\n    return matrices\n\n\n# ============================================================================\n# Diagnostic Plots (optional)\n# ============================================================================\n\ndef save_f1_vs_bias_plot(f1_bias, output_dir):\n    if not HAS_MPL:\n        return\n    fig, axes = plt.subplots(2, 4, figsize=(20, 10))\n    axes = axes.flatten()\n    for idx, topo in enumerate(TOPOLOGIES):\n        ax = axes[idx]\n        subset = [r for r in f1_bias if r['topology'] == topo\n                  and r['abs_bias'] is not None]\n        if not subset:\n            ax.set_title(topo)\n            continue\n        f1s = [r['macro_f1'] for r in subset]\n        biases = [r['abs_bias'] for r in subset]\n        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]\n        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)\n        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)\n        ax.set_xlabel('Macro F1')\n        ax.set_ylabel('|bias|')\n        ax.set_title(topo)\n    if len(TOPOLOGIES) < 8:\n        axes[-1].axis('off')\n    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)\n    plt.close(fig)\n\n\ndef save_asv_heatmap(asvs, output_dir):\n    if not HAS_MPL:\n        return\n    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']\n    datasets_list = list(DATASETS.keys())\n    fig, axes = plt.subplots(1, 3, figsize=(18, 6))\n    for didx, dataset in enumerate(datasets_list):\n        ax = axes[didx]\n        subset = [r for r in mag_asvs if r['dataset'] == dataset]\n        configs = sorted(set((r['model'], r['prompt']) for r in subset))\n        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)\n        for r in subset:\n            ti = TOPOLOGIES.index(r['topology'])\n            ci = configs.index((r['model'], r['prompt']))\n            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan\n        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',\n                       vmin=0, vmax=2)\n        ax.set_xticks(range(len(configs)))\n        ax.set_xticklabels([f\"{m[:3]}_{p[:3]}\" for m, p in configs],\n                           rotation=45, ha='right', fontsize=7)\n        ax.set_yticks(range(len(TOPOLOGIES)))\n        ax.set_yticklabels(TOPOLOGIES, fontsize=8)\n        ax.set_title(f'{dataset} (K={DATASETS[dataset][\"K\"]})')\n        plt.colorbar(im, ax=ax, shrink=0.8)\n    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)\n    plt.close(fig)\n\n\n# ============================================================================\n# JSON Serialization\n# ============================================================================\n\ndef _to_json_safe(obj):\n    if isinstance(obj, np.integer):\n        return int(obj)\n    elif isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    elif isinstance(obj, np.ndarray):\n        return _to_json_safe(obj.tolist())\n    elif isinstance(obj, dict):\n        return {str(k): _to_json_safe(v) for k, v in obj.items()}\n    elif isinstance(obj, list):\n        return [_to_json_safe(v) for v in obj]\n    elif isinstance(obj, (bool, np.bool_)):\n        return bool(obj)\n    elif isinstance(obj, float):\n        return None if (np.isnan(obj) or np.isinf(obj)) else obj\n    return obj\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')\n    parser.add_argument('--data-dir', default='data/')\n    parser.add_argument('--output-dir', default='artifacts/plan006/')\n    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')\n    parser.add_argument('--n-sim', type=int, default=1000)\n    parser.add_argument('--device', type=str, default='cpu')\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    t_total = time.time()\n    n_precomp = 500_000 if args.mock else N_PRECOMP\n\n    print(\"=\" * 70)\n    print(\"plan_006: Empirical ASV Calibration\")\n    print(\"=\" * 70)\n\n    # --- 1. Confusion matrices ---\n    if args.mock:\n        print(\"\\n[1/6] Generating mock confusion matrices...\")\n        confusion_matrices = generate_mock_confusion_matrices()\n    else:\n        print(\"\\n[1/6] Loading confusion matrices...\")\n        confusion_matrices = load_all_confusion_matrices(args.data_dir)\n\n    print(f\"  {len(confusion_matrices)} matrices loaded\")\n    for (ds, m, p), C in list(confusion_matrices.items())[:3]:\n        K = DATASETS[ds]['K']\n        print(f\"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}\")\n\n    # --- 2. Precompute sufficient statistics ---\n    print(\"\\n[2/6] Precomputing sufficient statistics...\")\n    K_values = sorted(set(DATASETS[ds]['K'] for ds in DATASETS))\n    all_suff_stats = {}\n    all_tau_true = {}\n    all_params = {}\n    all_params_H0 = {}\n    all_se_ref = {}\n\n    for K in K_values:\n        params = make_dgp_params(K)\n        params_H0 = make_dgp_params_H0(K, params)\n        all_params[K] = params\n        all_params_H0[K] = params_H0\n        for topology in TOPOLOGIES:\n            seed = K * 1000 + abs(hash(topology)) % 1000\n            st = precompute_suff_stats(K, topology, params[topology],\n                                       N=n_precomp, seed=seed)\n            plim_I = compute_plim(np.eye(K), st, K)\n            tau_true = extract_tau(plim_I, topology)\n            all_suff_stats[(K, topology)] = st\n            all_tau_true[(K, topology)] = tau_true\n\n            se = estimate_reference_se(K, topology, params[topology],\n                                       N_ref=5000,\n                                       n_mc=min(args.n_sim, 30),\n                                       seed=seed + 500)\n            all_se_ref[(K, topology)] = se\n            se_s = f\"{se:.4f}\" if np.isfinite(se) else \"N/A\"\n            print(f\"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}\")\n\n    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)\n    n_sign_flips = sum(1 for b in biases if b['sign_flip'])\n    print(f\"  {len(biases)} bias values ({n_sign_flips} sign flips)\")\n\n    # --- 3. ASV ---\n    print(\"\\n[3/6] Computing ASV values...\")\n    t3 = time.time()\n    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,\n                            all_tau_true, all_se_ref)\n    print(f\"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)\")\n    for at in ['magnitude', 'sign_flip', 'significance']:\n        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]\n        if sub:\n            print(f\"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} \"\n                  f\"max={max(sub):.3f} ({len(sub)} non-None)\")\n\n    # --- 4. F1 vs bias ---\n    print(\"\\n[4/6] F1 vs bias analysis...\")\n    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)\n    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]\n    high_f1_high_bias = [r for r in total_high_f1\n                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]\n    if total_high_f1:\n        pct = len(high_f1_high_bias) / len(total_high_f1) * 100\n        print(f\"  Baumann check: F1>0.93 with |bias|>0.05: \"\n              f\"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%\")\n    # Sample rows\n    for r in f1_bias[:3]:\n        print(f\"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: \"\n              f\"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}\")\n\n    # --- 5. Type I/II ---\n    print(\"\\n[5/6] Type I/II error rates...\")\n    t5 = time.time()\n    type1_type2_results = []\n    n_configs = len(confusion_matrices) * len(TOPOLOGIES)\n    idx = 0\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            idx += 1\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            r = compute_type1_type2_for_C(\n                C, K, topology, all_params[K], all_params_H0[K],\n                st, tau_true,\n                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)\n            type1_type2_results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **r,\n            })\n            if idx % 50 == 0:\n                print(f\"    {idx}/{n_configs}...\")\n    print(f\"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)\")\n    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])\n    print(f\"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}\")\n\n    # --- 6. Inter-model correlation ---\n    print(\"\\n[6/6] Inter-model error correlation...\")\n    inter_model_results = {}\n    for dataset in DATASETS:\n        K = DATASETS[dataset]['K']\n        for prompt in PROMPTS:\n            r = compute_inter_model_correlation(\n                confusion_matrices, K, dataset, prompt,\n                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)\n            inter_model_results[f\"{dataset}_{prompt}\"] = r\n    print(f\"  {len(inter_model_results)} (dataset, prompt) pairs\")\n    for key, pairs in list(inter_model_results.items())[:2]:\n        for pair, vals in pairs.items():\n            print(f\"    {key} {pair}: agree={vals['agreement']:.3f} \"\n                  f\"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}\")\n\n    # --- Summary ---\n    summary = {\n        'f1_gt_093_total': len(total_high_f1),\n        'f1_gt_093_with_high_bias_pct': (\n            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),\n        'ppi_recommended_scenarios': unsafe,\n        'total_scenarios': len(type1_type2_results),\n        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,\n    }\n\n    # --- Save ---\n    output = _to_json_safe({\n        'confusion_matrices': {\n            f\"{ds}_{m}_{p}\": C.tolist()\n            for (ds, m, p), C in confusion_matrices.items()\n        },\n        'biases': biases,\n        'asvs': asvs,\n        'f1_vs_bias': f1_bias,\n        'type1_type2': type1_type2_results,\n        'inter_model_correlation': inter_model_results,\n        'summary': summary,\n    })\n\n    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n    # --- Plots ---\n    save_f1_vs_bias_plot(f1_bias, args.output_dir)\n    save_asv_heatmap(asvs, args.output_dir)\n    if HAS_MPL:\n        print(f\"Plots saved to {args.output_dir}\")\n\n    # --- Validation ---\n    with open(out_path) as f:\n        data = json.load(f)\n    n_null = str(data).count('null')\n    print(f\"\\nValidation: JSON has {n_null} null values \"\n          f\"(expected for NaN/None ASV entries)\")\n    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:\n        print(f\"  {section}: {len(data[section])} records\")\n\n    elapsed = time.time() - t_total\n    print(f\"\\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)\")\n    print(f\"\\nSummary:\")\n    print(f\"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%\")\n    print(f\"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/\"\n          f\"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Runtime record

_source line 45_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779415200,
    "rateLimitType": "seven_day",
    "utilization": 0.92,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "6132583f-fe7f-4804-be8e-679f614c42d4",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7"
}
```

---


### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "status",
  "status": "compacting",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "6d31438f-b92a-4167-94ca-f1ba5f05826a"
}
```

---


### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "status",
  "status": null,
  "compact_result": "success",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "2205d24f-a9a5-4645-a709-2f66b0443bbe"
}
```

---


### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "compact_boundary",
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "258f25d1-ad76-4036-925f-3b7a0574702d",
  "compact_metadata": {
    "trigger": "auto",
    "pre_tokens": 191432,
    "post_tokens": 2607,
    "duration_ms": 82061
  }
}
```

---


## Round 2

## Round 2

103 recorded events


### User

_source line 49 · 2026-05-20T21:24:42.419Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   The user requested writing a `plan_006_asv_empirical.py` script for their causal annotation error attribution paper. This script performs empirical ASV (Annotation Sensitivity Value) calibration using confusion matrices from LLM annotations (3 models × 3 datasets × 3 prompts = 27 C matrices). It must:
   - Support loading real data from `data/{dataset}/{model}_{prompt}_annotations.jsonl` or generating mock data with `--mock`
   - Compute downstream causal bias across 7 DAG topologies (confounding, mediation, collider, exposure, mbias, iv, frontdoor)
   - Compute 3 ASV types: magnitude (min δ where |bias| > 0.1×|τ̂|), significance (min δ where |plim τ̂(C(δ))| < 1.96×SE), sign_flip (min δ where sign flips)
   - Analyze F1 vs downstream bias to verify Baumann 2025 claim (F1>0.93 still has >50% error risk)
   - Compute Type I/II error rates before/after ASV filtering
   - Compute inter-model error correlation (pairwise agreement, Cohen's kappa, conditional error correlation)
   - After writing, deploy to server and run `python3 plan_006_asv_empirical.py --mock --n-sim 10` for dry-run verification
   - Report dry-run output samples and any issues

2. Key Technical Concepts:
   - Column-stochastic confusion matrices: C[j,i] = P(A*=j|A=i), each column sums to 1
   - 7 DAG topologies: confounding (A→T, A→Y, T→Y), mediation (T→A→Y), collider (T→A←Y), exposure (A→Y), M-bias (U1→{A,T}, U2→{A,Y}), IV (Z→A→Y, U→{A,Y}), frontdoor (T→M→Y, U→{T,Y})
   - Plim computation via sufficient statistics: precompute population moments from large DGP sample, then for any C compute plim = (E[Z*'Z*])^{-1} E[Z*'Y]
   - C(δ) linear interpolation: C(δ) = (1-δ)I + δC₀, column-normalized
   - ASV envelope: running maximum of |bias(δ)| ensures monotonicity
   - General-K OLS plim: (K+1)×(K+1) system for topologies with T, K×K for exposure
   - Wald estimator for IV: RF/FS*_k where FS* = C @ FS
   - F1 computed directly from C matrix and class prevalence p_A
   - ASV filter for Type I/II: reject only if |τ̂/SE| > 1.96 AND magnitude_ASV > 1.0
   - Datasets: civil_comments (K=2), vast (K=3), humaid (K=10)
   - DGP parameter pools extend from K=3 (matching plan_001/plan_005) to K=2 and K=10

3. Files and Code Sections:
   - `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py`
     - Read to understand ASV framework: LinearInterpolation, compute_asv_envelope, compute_bias_curve, envelope monotonicity
     - Key functions: plim_mbias, plim_iv, plim_fd (all K=3 hardcoded)
     - Parameters: MBIAS_PARAMS(tau=0.5, delta=1.0, lam=1.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9), IV_PARAMS(lam=1.0, dZ=1.0, dU=0.8), IV_BETA=[0,0.5,-0.25]
     - Part 5 Type I/II approach: decision rule "reject if |τ̂/SE|>1.96 AND magnitude_ASV > 1"

   - `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py`
     - Read for mediation and frontdoor plim functions (closed-form for K=3)
     - Key: plim_med uses EZZ/EZX matrices, plim_fd uses precomputed sufficient statistics
     - Parameters: TAU=0.5, GAMMA_MED=[0,0.5,-0.3], DELTA_MED=[0,0.8,-0.6], GAMMA_FD=[0,0.5,-0.3], DELTA_FD=[0,1.0,-0.8]

   - `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py`
     - Read for collider, mbias, IV implementations (K=3)
     - Key: theory_collider, theory_mbias, theory_iv use large-sample moment approximation
     - COLLIDER_PARAMS(tau=1.0, dT=0.5, dY=0.8), MBIAS_PARAMS(tau=1.0, delta=1.0, lam=1.0)

   - `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py`
     - Read for general-K implementations using torch GPU batching
     - Key: plim_with_T (general K), plim_exposure (general K), SuffStats class, gen_random_C
     - Parameter pools: _ALPHA_POOL, _BETA_A_POOL, _BETA_POOL, etc.
     - make_params(K) generates topology-specific parameters for any K

   - `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py` (CREATED)
     - The main deliverable script (~600+ lines)
     - Structure: utilities → DGP params → DGP generators → suff stats & plim → data loading → bias computation → ASV computation → F1 analysis → Type I/II → inter-model correlation → mock data → plots → main
     - Key design: numpy-only (no torch), general-K support, mock mode with reduced precomputation (500K vs 2M samples)
     - All 7 topologies generalized to K=2,3,10
     - Output: artifacts/plan006/asv_empirical_results.json with sections: confusion_matrices, biases, asvs, f1_vs_bias, type1_type2, inter_model_correlation, summary

4. Errors and fixes:
   - No runtime errors yet — the script has been written but not executed
   - Output token limit was hit on first attempt, requiring continuation in next message

5. Problem Solving:
   - Generalized K=3 hardcoded plim functions to arbitrary K by using the sufficient statistics approach from plan_002 but in numpy (not torch)
   - Handled IV Wald estimator for general K (noted K=10 may have weak first stage)
   - Designed significance ASV using reference SE from small MC simulation (since analytical SE computation is complex)
   - For mock data: distance-weighted off-diagonal errors for K=10 to simulate realistic confusion patterns
   - H0 parameter generation handles each topology differently (e.g., frontdoor needs lambda_U=0, alpha_U=0, delta_fd=zeros, beta=zeros)

6. All user messages:
   - Message 1: Detailed task specification for plan_006 script with 7 sections covering background, input format, script requirements (6 modules), mock data spec, output format, implementation notes, and verification steps
   - Message 2: "Output token limit hit. Resume directly — no apology, no recap of what you were doing. Pick up mid-thought if that is where the cut happened. Break remaining work into smaller pieces."

7. Pending Tasks:
   - Deploy plan_006_asv_empirical.py to server at `/home/sonny/causal_annot_error_attrib/`
   - Run dry-run: `python3 plan_006_asv_empirical.py --mock --n-sim 10`
   - Verify output JSON structure is correct, no NaN/Inf
   - Confirm all 6 analysis modules produced results
   - Report dry-run key output samples (F1 vs bias data, ASV value ranges, etc.)
   - Report any issues (e.g., topologies that don't work well for K=10)

8. Current Work:
   The script `plan_006_asv_empirical.py` has been fully written and saved locally at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py`. It has NOT yet been deployed to the server or tested. The file was created successfully with the Write tool. The next step is deployment and dry-run verification.

9. Optional Next Step:
   Deploy the script to the server and run dry-run. Per the user's original request:
   - "写完代码后，SSH 执行 `python3 plan_006_asv_empirical.py --mock --n-sim 10` 做 dry-run"
   - "确认输出 JSON 结构正确、无 NaN/Inf"
   - "确认所有 6 个分析模块都产出了结果"
   - "报告 dry-run 的关键输出样例（几行 F1 vs bias 数据、ASV 值范围等）"
   
   This requires: (1) using ssh_execute to copy the file to the server or sync via git, (2) running the dry-run command, (3) checking output, (4) reporting results. Server: home-1x5090, user sonny, SSH via `ssh implicit5638.xyfu.me`, project path `/home/sonny/causal_annot_error_attrib/`.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/fb66a23b-ab7a-49cf-9609-9cc0b887dde7.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "aa39efce-5a75-4ea2-b005-8021049194c1",
  "isSynthetic": true
}
```

</details>

---


### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
The next step is to deploy `plan_006_asv_empirical.py` to the server and run the dry-run. Let me first read the script to understand what we have, then deploy it.

Let me start by reading the script and checking the server connection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "848d60d9-2697-4020-be0d-8ac7b0b5c951",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3ozsVzZdVkxm1AdMA7Bs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14129,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14129
      },
      "output_tokens": 33,
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

_source line 51_

Deploying `plan_006_asv_empirical.py` to the server and running the dry-run.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "d4e62e11-4db1-49ef-b6c8-3e06a800ae59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3ozsVzZdVkxm1AdMA7Bs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14129,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14129
      },
      "output_tokens": 33,
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

_source line 52_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SL37xW3xLqGnh3XqihHusA`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "87dccef0-f278-42c2-a9c5-d9e1243a370d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3ozsVzZdVkxm1AdMA7Bs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14129,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14129
      },
      "output_tokens": 33,
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

_source line 53 · 2026-05-20T21:24:47.551Z_

<details><summary>↩ Tool result · `toolu_01SL37xW3xLqGnh3XqihHusA`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "c986220c-362d-4091-8bdd-94f5ce2143b6",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01MYhNvkT5rJutsy34d7PPxB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
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
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "133f898b-c5b2-4f1c-b213-3ecc64590ac6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3ozsVzZdVkxm1AdMA7Bs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14129,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14129
      },
      "output_tokens": 33,
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

_source line 55 · 2026-05-20T21:24:48.162Z_

<details><summary>↩ Tool result · `toolu_01MYhNvkT5rJutsy34d7PPxB`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices
4	
5	Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
6	= 27 C matrices) to compute:
7	  1. Downstream causal bias across 7 DAG topologies
8	  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
9	  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
10	  4. Type I/II error rates before/after ASV filtering
11	  5. Inter-model error correlation
12	
13	Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
14	        Each line: {"true_label": int, "predicted_label": int}
15	
16	Output: artifacts/plan006/asv_empirical_results.json
17	
18	Dependencies: numpy (required), matplotlib (optional for plots)
19	"""
20	
21	import numpy as np
22	import json
23	import argparse
24	import os
25	import time
26	from collections import OrderedDict
27	
28	try:
29	    import matplotlib
30	    matplotlib.use('Agg')
31	    import matplotlib.pyplot as plt
32	    HAS_MPL = True
33	except ImportError:
34	    HAS_MPL = False
35	
36	# ============================================================================
37	# Constants
38	# ============================================================================
39	
40	DATASETS = OrderedDict([
41	    ('civil_comments', {'K': 2}),
42	    ('vast', {'K': 3}),
43	    ('humaid', {'K': 10}),
44	])
45	
46	MODELS = ['llama4', 'qwen3', 'deepseek']
47	PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']
48	
49	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
50	              'mbias', 'iv', 'frontdoor']
51	
52	N_PRECOMP = 2_000_000
53	
54	# Parameter pools — K=3 values match plan_001/plan_005
55	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
56	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
57	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
58	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
59	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
60	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
61	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]
62	
63	
64	# ============================================================================
65	# Utility Functions
66	# ============================================================================
67	
68	def softmax_rows(logits):
69	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
70	    return e / e.sum(axis=1, keepdims=True)
71	
72	
73	def sample_cat(probs, rng):
74	    cum = np.cumsum(probs, axis=1)
75	    u = rng.uniform(size=probs.shape[0])[:, None]
76	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
77	
78	
79	def generate_Astar(A, C, rng):
80	    probs = C[:, A]
81	    cum = np.cumsum(probs, axis=0)
82	    u = rng.uniform(size=len(A))
83	    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)
84	
85	
86	def ols_with_dummies(Y, T, Astar, K):
87	    N = len(Y)
88	    D = np.zeros((N, K - 1))
89	    for k in range(1, K):
90	        D[:, k - 1] = (Astar == k).astype(float)
91	    X = np.column_stack([np.ones(N), T, D])
92	    try:
93	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
94	        resid = Y - X @ beta
95	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
96	        XtX_inv = np.linalg.inv(X.T @ X)
97	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
98	    except np.linalg.LinAlgError:
99	        beta = np.full(X.shape[1], np.nan)
100	        se = np.full(X.shape[1], np.nan)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "239ce2b2-a9f9-466d-afc4-48548f3a2c32",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices\n\nUses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts\n= 27 C matrices) to compute:\n  1. Downstream causal bias across 7 DAG topologies\n  2. ASV sensitivity metrics (magnitude, significance, sign-flip)\n  3. F1 vs bias disconnect analysis (Baumann 2025 verification)\n  4. Type I/II error rates before/after ASV filtering\n  5. Inter-model error correlation\n\nInput:  data/{dataset}/{model}_{prompt}_annotations.jsonl\n        Each line: {\"true_label\": int, \"predicted_label\": int}\n\nOutput: artifacts/plan006/asv_empirical_results.json\n\nDependencies: numpy (required), matplotlib (optional for plots)\n\"\"\"\n\nimport numpy as np\nimport json\nimport argparse\nimport os\nimport time\nfrom collections import OrderedDict\n\ntry:\n    import matplotlib\n    matplotlib.use('Agg')\n    import matplotlib.pyplot as plt\n    HAS_MPL = True\nexcept ImportError:\n    HAS_MPL = False\n\n# ============================================================================\n# Constants\n# ============================================================================\n\nDATASETS = OrderedDict([\n    ('civil_comments', {'K': 2}),\n    ('vast', {'K': 3}),\n    ('humaid', {'K': 10}),\n])\n\nMODELS = ['llama4', 'qwen3', 'deepseek']\nPROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']\n\nTOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\n\nN_PRECOMP = 2_000_000\n\n# Parameter pools — K=3 values match plan_001/plan_005\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]\n\n\n# ============================================================================\n# Utility Functions\n# ============================================================================\n\ndef softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 1048
    }
  }
}
```

</details>

---


### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Let me read the rest of the script to understand its full structure, then deploy to server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "7a76fec7-bb16-4e6e-9590-975bc25c1a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WjQ2nMVFtcxeDgnQYaPgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 25970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01FVpmsBL1ye15kQXhuySyuZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 100,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "58cf488d-adfb-4896-8fd0-6f3a0ce6f606",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WjQ2nMVFtcxeDgnQYaPgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 25970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 58 · 2026-05-20T21:24:52.516Z_

<details><summary>↩ Tool result · `toolu_01FVpmsBL1ye15kQXhuySyuZ`</summary>

```text
100	        se = np.full(X.shape[1], np.nan)
101	    return beta, se
102	
103	
104	def ols_no_T(Y, Astar, K):
105	    N = len(Y)
106	    D = np.zeros((N, K - 1))
107	    for k in range(1, K):
108	        D[:, k - 1] = (Astar == k).astype(float)
109	    X = np.column_stack([np.ones(N), D])
110	    try:
111	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
112	        resid = Y - X @ beta
113	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
114	        XtX_inv = np.linalg.inv(X.T @ X)
115	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
116	    except np.linalg.LinAlgError:
117	        beta = np.full(X.shape[1], np.nan)
118	        se = np.full(X.shape[1], np.nan)
119	    return beta, se
120	
121	
122	def wald_estimator(Z, Y, Astar, k=1):
123	    z1 = Z == 1; z0 = Z == 0
124	    n1, n0 = float(z1.sum()), float(z0.sum())
125	    if n1 < 2 or n0 < 2:
126	        return np.nan, np.nan
127	    RF = Y[z1].mean() - Y[z0].mean()
128	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
129	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
130	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
131	    FS = Dk_z1 - Dk_z0
132	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
133	    if abs(FS) < 1e-8:
134	        return np.nan, np.nan
135	    W = RF / FS
136	    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4
137	    return W, np.sqrt(max(var_W, 0))
138	
139	
140	# ============================================================================
141	# DGP Parameters (general K, K=3 matches plan_001/plan_005)
142	# ============================================================================
143	
144	def make_p_A(K):
145	    if K == 2:
146	        return np.array([0.55, 0.45])
147	    elif K == 3:
148	        return np.array([0.40, 0.35, 0.25])
149	    else:
150	        raw = np.array([1.0 / (i + 1) for i in range(K)])
151	        return raw / raw.sum()
152	
153	
154	def make_dgp_params(K):
155	    p_A = make_p_A(K)
156	    params = {
157	        'confounding': {
158	            'p_A': p_A,
159	            'alpha': np.array(_ALPHA_POOL[:K - 1]),
160	            'beta_A': np.array(_BETA_A_POOL[:K - 1]),
161	            'beta_T': 2.0,
162	            'sigma_T': 1.0,
163	        },
164	        'mediation': {
165	            'tau': 0.5,
166	            'gamma': np.array(_GAMMA_POOL[:K]),
167	            'delta': np.array(_DELTA_POOL[:K]),
168	            'beta': np.array(_BETA_POOL[:K]),
169	        },
170	        'collider': {
171	            'tau': 1.0,
172	            'g': np.zeros(K),
173	            'dT': np.array(_DT_POOL[:K]),
174	            'dY': np.array(_DY_POOL[:K]),
175	        },
176	        'exposure': {
177	            'beta': np.array(_BETA_POOL[:K]),
178	            'p_A': p_A,
179	        },
180	    }
181	    if K == 3:
182	        params['mbias'] = {
183	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
184	            'g': np.zeros(3),
185	            'a_U1': np.array([0.0, 0.8, -0.5]),
186	            'a_U2': np.array([0.0, 0.6, 0.9]),
187	        }
188	        params['iv'] = {
189	            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
190	            'g': np.zeros(3),
191	            'dZ': np.array([0.0, 1.0, -0.5]),
192	            'dU': np.array([0.0, 0.8, 0.6]),
193	        }
194	        params['frontdoor'] = {
195	            'alpha_U': 1.0, 'lambda_U': 1.0,
196	            'gamma': np.array([0.0, 0.5, -0.3]),
197	            'delta_fd': np.array([0.0, 1.0, -0.8]),
198	            'beta': np.array([0.0, 1.0, -0.5]),
199	        }
200	    else:
201	        params['mbias'] = {
202	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
203	            'g': np.zeros(K),
204	            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),
205	            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),
206	        }
207	        iv_beta = np.array(_BETA_POOL[:K]) * 0.5
208	        iv_beta[0] = 0.0
209	        params['iv'] = {
210	            'lam': 1.0, 'beta': iv_beta,
211	            'g': np.zeros(K),
212	            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
213	            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
214	        }
215	        fd_delta = np.array(_DELTA_POOL[:K])
216	        fd_delta[0] = 0.0
217	        params['frontdoor'] = {
218	            'alpha_U': 1.0, 'lambda_U': 1.0,
219	            'gamma': np.array(_GAMMA_POOL[:K]),
220	            'delta_fd': fd_delta,
221	            'beta': np.array(_BETA_POOL[:K]),
222	        }
223	    return params
224	
225	
226	def make_dgp_params_H0(K, params):
227	    p0 = {}
228	    for topo, p in params.items():
229	        if topo == 'confounding':
230	            p0[topo] = dict(p, beta_T=0.0)
231	        elif topo == 'mediation':
232	            p0[topo] = dict(p, tau=0.0)
233	        elif topo == 'collider':
234	            p0[topo] = dict(p, tau=0.0)
235	        elif topo == 'exposure':
236	            p0[topo] = dict(p, beta=np.zeros(K))
237	        elif topo == 'mbias':
238	            p0[topo] = dict(p, tau=0.0)
239	        elif topo == 'iv':
240	            p0[topo] = dict(p, beta=np.zeros(K))
241	        elif topo == 'frontdoor':
242	            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,
243	                            delta_fd=np.zeros(K), beta=np.zeros(K))
244	    return p0
245	
246	
247	# ============================================================================
248	# DGP Generators (general K)
249	# ============================================================================
250	
251	def gen_confounding(K, N, p, rng):
252	    A = rng.choice(K, size=N, p=p['p_A'])
253	    D = np.zeros((N, K - 1))
254	    for j in range(K - 1):
255	        D[:, j] = (A == j + 1).astype(float)
256	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
257	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
258	    return T, Y, A
259	
260	
261	def gen_mediation(K, N, p, rng):
262	    T = rng.binomial(1, 0.5, N).astype(float)
263	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
264	    probs = softmax_rows(logits)
265	    A = sample_cat(probs, rng)
266	    D = np.zeros((N, K - 1))
267	    for j in range(K - 1):
268	        D[:, j] = (A == j + 1).astype(float)
269	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
270	    return T, Y, A
271	
272	
273	def gen_collider(K, N, p, rng):
274	    T = rng.normal(0, 1, N)
275	    Y = p['tau'] * T + rng.normal(0, 1, N)
276	    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
277	              + p['dY'][None, :] * Y[:, None])
278	    probs = softmax_rows(logits)
279	    A = sample_cat(probs, rng)
280	    return T, Y, A
281	
282	
283	def gen_exposure(K, N, p, rng):
284	    A = rng.choice(K, size=N, p=p['p_A'])
285	    D = np.zeros((N, K - 1))
286	    for j in range(K - 1):
287	        D[:, j] = (A == j + 1).astype(float)
288	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
289	    return None, Y, A
290	
291	
292	def gen_mbias(K, N, p, rng):
293	    U1 = rng.normal(0, 1, N)
294	    U2 = rng.normal(0, 1, N)
295	    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
296	    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
297	    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]
298	              + p['a_U2'][None, :] * U2[:, None])
299	    probs = softmax_rows(logits)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5bf88bd4-86e5-4634-ac47-aa6e0b6e73ea",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
      "content": "        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef ols_no_T(Y, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef wald_estimator(Z, Y, Astar, k=1):\n    z1 = Z == 1; z0 = Z == 0\n    n1, n0 = float(z1.sum()), float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    W = RF / FS\n    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    return W, np.sqrt(max(var_W, 0))\n\n\n# ============================================================================\n# DGP Parameters (general K, K=3 matches plan_001/plan_005)\n# ============================================================================\n\ndef make_p_A(K):\n    if K == 2:\n        return np.array([0.55, 0.45])\n    elif K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    else:\n        raw = np.array([1.0 / (i + 1) for i in range(K)])\n        return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A,\n            'alpha': np.array(_ALPHA_POOL[:K - 1]),\n            'beta_A': np.array(_BETA_A_POOL[:K - 1]),\n            'beta_T': 2.0,\n            'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'collider': {\n            'tau': 1.0,\n            'g': np.zeros(K),\n            'dT': np.array(_DT_POOL[:K]),\n            'dY': np.array(_DY_POOL[:K]),\n        },\n        'exposure': {\n            'beta': np.array(_BETA_POOL[:K]),\n            'p_A': p_A,\n        },\n    }\n    if K == 3:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(3),\n            'a_U1': np.array([0.0, 0.8, -0.5]),\n            'a_U2': np.array([0.0, 0.6, 0.9]),\n        }\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3),\n            'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array([0.0, 0.5, -0.3]),\n            'delta_fd': np.array([0.0, 1.0, -0.8]),\n            'beta': np.array([0.0, 1.0, -0.5]),\n        }\n    else:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(K),\n            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),\n            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),\n        }\n        iv_beta = np.array(_BETA_POOL[:K]) * 0.5\n        iv_beta[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_beta,\n            'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),\n        }\n        fd_delta = np.array(_DELTA_POOL[:K])\n        fd_delta[0] = 0.0\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta_fd': fd_delta,\n            'beta': np.array(_BETA_POOL[:K]),\n        }\n    return params\n\n\ndef make_dgp_params_H0(K, params):\n    p0 = {}\n    for topo, p in params.items():\n        if topo == 'confounding':\n            p0[topo] = dict(p, beta_T=0.0)\n        elif topo == 'mediation':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'collider':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'exposure':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'mbias':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'iv':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'frontdoor':\n            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,\n                            delta_fd=np.zeros(K), beta=np.zeros(K))\n    return p0\n\n\n# ============================================================================\n# DGP Generators (general K)\n# ============================================================================\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]\n              + p['a_U2'][None, :] * U2[:, None])\n    probs = softmax_rows(logits)",
      "numLines": 200,
      "startLine": 100,
      "totalLines": 1048
    }
  }
}
```

</details>

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KyuTDVX9BBXpJpcipW5ZUH`</summary>

```json
{
  "server": "home-1x5090",
  "command": "ls /home/sonny/causal_annot_error_attrib/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b37beefa-1de9-4533-9390-584fa941bc76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WjQ2nMVFtcxeDgnQYaPgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 25970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 60 · 2026-05-20T21:24:54.973Z_

<details><summary>↩ Tool result · `toolu_01KyuTDVX9BBXpJpcipW5ZUH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"annotate.py\\nannotate.py.bak\\nartifacts\\ndata\\nplan_001_collider_mbias_iv.py\\nplan_001_dag_taxonomy.py\\nplan_001_mediation_frontdoor.py\\nplan002_7topo_run.log\\nplan_002_k57_extended_7topo.py\\nplan_002_k57_extension.py\\nplan002_rng_fix_run.log\\nplan002_run.log\\nplan002_sensitivity_collider_K3.png\\nplan002_sensitivity_collider_K5.png\\nplan002_sensitivity_collider_K7.png\\nplan002_sensitivity_combined.png\\nplan002_sensitivity_confounding_K3.png\\nplan002_sensitivity_confounding_K5.png\\nplan002_sensitivity_confounding_K7.png\\nplan002_sensitivity_exposure_K3.png\\nplan002_sensitivity_exposure_K5.png\\nplan002_sensitivity_exposure_K7.png\\nplan002_sensitivity_mediation_K3.png\\nplan002_sensitivity_mediation_K5.png\\nplan002_sensitivity_mediation_K7.png\\nplan003_deepseek.log\\nplan003_llama4.log\\nplan003_qwen3.log\\nplan003_run.log\\nplan_004_asv_framework.py\\nplan_004_asv_v3_fixed.py\\nplan_004_asv_v3_output.log\\nplan_004_asv_v3.py\\nplan_004_n_sensitivity.py\\nplan004_run.log\\nplan_005_asv_extended_fixed.py\\nplan_005_asv_extended.py\\nplan005_fixed_run.log\\nplan005_fixed_summary.md\\nplan005_run.log\\nplan_007_correction_guidance.py\\nplan_008_binarization_collapse.py\\nplan_009_pathological_matrices.py\\n__pycache__\\nresults\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5fe5e833-4f60-4e39-94db-b1251dcd637a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"annotate.py\\\\nannotate.py.bak\\\\nartifacts\\\\ndata\\\\nplan_001_collider_mbias_iv.py\\\\nplan_001_dag_taxonomy.py\\\\nplan_001_mediation_frontdoor.py\\\\nplan002_7topo_run.log\\\\nplan_002_k57_extended_7topo.py\\\\nplan_002_k57_extension.py\\\\nplan002_rng_fix_run.log\\\\nplan002_run.log\\\\nplan002_sensitivity_collider_K3.png\\\\nplan002_sensitivity_collider_K5.png\\\\nplan002_sensitivity_collider_K7.png\\\\nplan002_sensitivity_combined.png\\\\nplan002_sensitivity_confounding_K3.png\\\\nplan002_sensitivity_confounding_K5.png\\\\nplan002_sensitivity_confounding_K7.png\\\\nplan002_sensitivity_exposure_K3.png\\\\nplan002_sensitivity_exposure_K5.png\\\\nplan002_sensitivity_exposure_K7.png\\\\nplan002_sensitivity_mediation_K3.png\\\\nplan002_sensitivity_mediation_K5.png\\\\nplan002_sensitivity_mediation_K7.png\\\\nplan003_deepseek.log\\\\nplan003_llama4.log\\\\nplan003_qwen3.log\\\\nplan003_run.log\\\\nplan_004_asv_framework.py\\\\nplan_004_asv_v3_fixed.py\\\\nplan_004_asv_v3_output.log\\\\nplan_004_asv_v3.py\\\\nplan_004_n_sensitivity.py\\\\nplan004_run.log\\\\nplan_005_asv_extended_fixed.py\\\\nplan_005_asv_extended.py\\\\nplan005_fixed_run.log\\\\nplan005_fixed_summary.md\\\\nplan005_run.log\\\\nplan_007_correction_guidance.py\\\\nplan_008_binarization_collapse.py\\\\nplan_009_pathological_matrices.py\\\\n__pycache__\\\\nresults\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"annotate.py\\nannotate.py.bak\\nartifacts\\ndata\\nplan_001_collider_mbias_iv.py\\nplan_001_dag_taxonomy.py\\nplan_001_mediation_frontdoor.py\\nplan002_7topo_run.log\\nplan_002_k57_extended_7topo.py\\nplan_002_k57_extension.py\\nplan002_rng_fix_run.log\\nplan002_run.log\\nplan002_sensitivity_collider_K3.png\\nplan002_sensitivity_collider_K5.png\\nplan002_sensitivity_collider_K7.png\\nplan002_sensitivity_combined.png\\nplan002_sensitivity_confounding_K3.png\\nplan002_sensitivity_confounding_K5.png\\nplan002_sensitivity_confounding_K7.png\\nplan002_sensitivity_exposure_K3.png\\nplan002_sensitivity_exposure_K5.png\\nplan002_sensitivity_exposure_K7.png\\nplan002_sensitivity_mediation_K3.png\\nplan002_sensitivity_mediation_K5.png\\nplan002_sensitivity_mediation_K7.png\\nplan003_deepseek.log\\nplan003_llama4.log\\nplan003_qwen3.log\\nplan003_run.log\\nplan_004_asv_framework.py\\nplan_004_asv_v3_fixed.py\\nplan_004_asv_v3_output.log\\nplan_004_asv_v3.py\\nplan_004_n_sensitivity.py\\nplan004_run.log\\nplan_005_asv_extended_fixed.py\\nplan_005_asv_extended.py\\nplan005_fixed_run.log\\nplan005_fixed_summary.md\\nplan005_run.log\\nplan_007_correction_guidance.py\\nplan_008_binarization_collapse.py\\nplan_009_pathological_matrices.py\\n__pycache__\\nresults\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.33}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01UjpLznU3G7JqKPHeZATMFT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "8f39459b-ded1-4c66-89cd-3795e4130ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3GNy1Ws9pMSeteqNZcRp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4227,
      "cache_read_input_tokens": 28661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4227
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

_source line 62 · 2026-05-20T21:24:58.981Z_

<details><summary>↩ Tool result · `toolu_01UjpLznU3G7JqKPHeZATMFT`</summary>

```text
300	    A = sample_cat(probs, rng)
301	    return T, Y, A
302	
303	
304	def gen_iv(K, N, p, rng):
305	    Z = rng.binomial(1, 0.5, N).astype(float)
306	    U = rng.normal(0, 1, N)
307	    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]
308	              + p['dU'][None, :] * U[:, None])
309	    probs = softmax_rows(logits)
310	    A = sample_cat(probs, rng)
311	    D = np.zeros((N, K - 1))
312	    for j in range(K - 1):
313	        D[:, j] = (A == j + 1).astype(float)
314	    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)
315	    return Z, Y, A
316	
317	
318	def gen_frontdoor(K, N, p, rng):
319	    U = rng.normal(0, 1, N)
320	    T = p['alpha_U'] * U + rng.normal(0, 1, N)
321	    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]
322	    probs = softmax_rows(logits)
323	    M = sample_cat(probs, rng)
324	    D = np.zeros((N, K - 1))
325	    for j in range(K - 1):
326	        D[:, j] = (M == j + 1).astype(float)
327	    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)
328	    return T, Y, M
329	
330	
331	GEN_FNS = {
332	    'confounding': gen_confounding, 'mediation': gen_mediation,
333	    'collider': gen_collider, 'exposure': gen_exposure,
334	    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,
335	}
336	
337	
338	# ============================================================================
339	# Sufficient Statistics & Plim (general K)
340	# ============================================================================
341	
342	def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
343	    rng = np.random.default_rng(seed)
344	    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
345	    DA = np.zeros((N, K))
346	    for k in range(K):
347	        DA[:, k] = (A == k).astype(float)
348	
349	    if topology == 'iv':
350	        Z = first_var
351	        z1 = Z == 1; z0 = Z == 0
352	        RF = Y[z1].mean() - Y[z0].mean()
353	        FS = np.zeros(K)
354	        for k in range(K):
355	            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
356	        return dict(RF=RF, FS=FS, topology='iv')
357	    elif topology == 'exposure':
358	        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
359	                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
360	    else:
361	        T = first_var
362	        return dict(
363	            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),
364	            E_Y=Y.mean(), E_TY=(T * Y).mean(),
365	            E_TD=(DA * T[:, None]).mean(0),
366	            E_YD=(DA * Y[:, None]).mean(0), topology=topology)
367	
368	
369	def compute_plim(C, st, K):
370	    if st['topology'] == 'iv':
371	        FS_star = C @ st['FS']
372	        if abs(FS_star[1]) < 1e-8:
373	            return np.nan
374	        return st['RF'] / FS_star[1]
375	    elif st['topology'] == 'exposure':
376	        q = C @ st['p_A']
377	        cy = C @ st['E_YD']
378	        EZZ = np.zeros((K, K))
379	        EZZ[0, 0] = 1.0
380	        for j in range(1, K):
381	            EZZ[0, j] = EZZ[j, 0] = q[j]
382	            EZZ[j, j] = q[j]
383	        EZY = np.zeros(K)
384	        EZY[0] = st['E_Y']
385	        for j in range(1, K):
386	            EZY[j] = cy[j]
387	        try:
388	            return np.linalg.solve(EZZ, EZY)
389	        except np.linalg.LinAlgError:
390	            return np.full(K, np.nan)
391	    else:
392	        q = C @ st['p_A']
393	        ct = C @ st['E_TD']
394	        cy = C @ st['E_YD']
395	        dim = K + 1
396	        EZZ = np.zeros((dim, dim))
397	        EZZ[0, 0] = 1.0
398	        EZZ[0, 1] = EZZ[1, 0] = st['E_T']
399	        EZZ[1, 1] = st['E_T2']
400	        for j in range(1, K):
401	            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]
402	            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]
403	            EZZ[j + 1, j + 1] = q[j]
404	        EZY = np.zeros(dim)
405	        EZY[0] = st['E_Y']
406	        EZY[1] = st['E_TY']
407	        for j in range(1, K):
408	            EZY[j + 1] = cy[j]
409	        try:
410	            return np.linalg.solve(EZZ, EZY)
411	        except np.linalg.LinAlgError:
412	            return np.full(dim, np.nan)
413	
414	
415	def extract_tau(plim_result, topology):
416	    if topology == 'iv':
417	        return float(plim_result) if np.isfinite(plim_result) else np.nan
418	    if isinstance(plim_result, np.ndarray):
419	        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
420	    return np.nan
421	
422	
423	# ============================================================================
424	# 1. Data Loading & Confusion Matrix
425	# ============================================================================
426	
427	def load_annotations(data_dir, dataset, model, prompt):
428	    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_annotations.jsonl")
429	    records = []
430	    with open(path) as f:
431	        for line in f:
432	            rec = json.loads(line.strip())
433	            records.append((int(rec['true_label']), int(rec['predicted_label'])))
434	    return records
435	
436	
437	def build_confusion_matrix(records, K):
438	    counts = np.zeros((K, K))
439	    for true_k, pred_k in records:
440	        if 0 <= true_k < K and 0 <= pred_k < K:
441	            counts[pred_k, true_k] += 1
442	    col_sums = counts.sum(axis=0)
443	    col_sums = np.where(col_sums < 1, 1, col_sums)
444	    return counts / col_sums
445	
446	
447	def load_all_confusion_matrices(data_dir):
448	    matrices = {}
449	    for dataset, info in DATASETS.items():
450	        K = info['K']
451	        for model in MODELS:
452	            for prompt in PROMPTS:
453	                try:
454	                    records = load_annotations(data_dir, dataset, model, prompt)
455	                    C = build_confusion_matrix(records, K)
456	                    matrices[(dataset, model, prompt)] = C
457	                except FileNotFoundError:
458	                    print(f"  [WARN] Missing: {dataset}/{model}_{prompt}")
459	    return matrices
460	
461	
462	# ============================================================================
463	# 2. Downstream Causal Bias
464	# ============================================================================
465	
466	def compute_bias_for_topology(C, K, topology, st, tau_true):
467	    plim_result = compute_plim(C, st, K)
468	    tau_hat = extract_tau(plim_result, topology)
469	    if np.isnan(tau_hat) or np.isnan(tau_true):
470	        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}
471	    bias = tau_hat - tau_true
472	    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None
473	    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)
474	    return {
475	        'tau_hat': float(tau_hat), 'bias': float(bias),
476	        'bias_pct': float(bias_pct) if bias_pct is not None else None,
477	        'sign_flip': sign_flip,
478	    }
479	
480	
481	def compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):
482	    results = []
483	    for (dataset, model, prompt), C in confusion_matrices.items():
484	        K = DATASETS[dataset]['K']
485	        for topology in TOPOLOGIES:
486	            st = all_suff_stats[(K, topology)]
487	            tau_true = all_tau_true[(K, topology)]
488	            info = compute_bias_for_topology(C, K, topology, st, tau_true)
489	            results.append({
490	                'dataset': dataset, 'model': model, 'prompt': prompt,
491	                'K': K, 'topology': topology, **info,
492	            })
493	    return results
494	
495	
496	# ============================================================================
497	# 3. ASV Computation
498	# ============================================================================
499	
500	def C_interpolated(C0, delta, K):
501	    C_d = (1 - delta) * np.eye(K) + delta * C0
502	    C_d = np.maximum(C_d, 0.0)
503	    col_sums = C_d.sum(axis=0)
504	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
505	    return C_d / col_sums
506	
507	
508	def compute_delta_max(C0):
509	    min_diag = np.diag(C0).min()
510	    if min_diag >= 1.0:
511	        return 10.0
512	    return min(1.0 / (1.0 - min_diag), 10.0)
513	
514	
515	def compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,
516	                           n_grid=1500, se_ref=None):
517	    dmax = compute_delta_max(C0)
518	    deltas = np.linspace(0, dmax, n_grid)
519	    tau_curve = np.zeros(n_grid)
520	    for i, d in enumerate(deltas):
521	        C_d = C_interpolated(C0, d, K)
522	        plim_result = compute_plim(C_d, st, K)
523	        tau_curve[i] = extract_tau(plim_result, topology)
524	
525	    bias_abs = np.abs(tau_curve - tau_true)
526	    envelope = np.zeros(n_grid)
527	    running_max = 0.0
528	    for i in range(n_grid):
529	        if np.isfinite(bias_abs[i]):
530	            running_max = max(running_max, bias_abs[i])
531	        envelope[i] = running_max
532	
533	    if asv_type == 'sign_flip':
534	        if abs(tau_true) < 1e-12:
535	            return None
536	        baseline_sign = np.sign(tau_true)
537	        for i in range(n_grid):
538	            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:
539	                return float(deltas[i])
540	        return None
541	    elif asv_type == 'magnitude':
542	        if abs(tau_true) < 1e-12:
543	            return None
544	        thresh = 0.1 * abs(tau_true)
545	        for i in range(n_grid):
546	            if envelope[i] > thresh:
547	                return float(deltas[i])
548	        return None
549	    elif asv_type == 'significance':
550	        if se_ref is None or se_ref < 1e-12:
551	            return None
552	        for i in range(n_grid):
553	            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:
554	                return float(deltas[i])
555	        return None
556	    return None
557	
558	
559	def estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):
560	    gen_fn = GEN_FNS[topology]
561	    rng = np.random.default_rng(seed)
562	    tau_hats = []
563	    for _ in range(n_mc):
564	        first_var, Y, A = gen_fn(K, N_ref, params, rng)
565	        if topology == 'iv':
566	            th, _ = wald_estimator(first_var, Y, A, k=1)
567	        elif topology == 'exposure':
568	            b, _ = ols_no_T(Y, A, K)
569	            th = b[1]
570	        else:
571	            b, _ = ols_with_dummies(Y, first_var, A, K)
572	            th = b[1]
573	        if np.isfinite(th):
574	            tau_hats.append(th)
575	    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan
576	
577	
578	def compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):
579	    results = []
580	    for (dataset, model, prompt), C in confusion_matrices.items():
581	        K = DATASETS[dataset]['K']
582	        for topology in TOPOLOGIES:
583	            st = all_suff_stats[(K, topology)]
584	            tau_true = all_tau_true[(K, topology)]
585	            se_ref = all_se_ref.get((K, topology))
586	            for asv_type in ['magnitude', 'significance', 'sign_flip']:
587	                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,
588	                                             asv_type, se_ref=se_ref)
589	                results.append({
590	                    'dataset': dataset, 'model': model, 'prompt': prompt,
591	                    'K': K, 'topology': topology, 'asv_type': asv_type,
592	                    'asv': asv,
593	                })
594	    return results
595	
596	
597	# ============================================================================
598	# 4. F1 vs Downstream Bias
599	# ============================================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "358e4406-9e66-444b-8a34-f070705d1825",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
      "content": "    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]\n              + p['dU'][None, :] * U[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    M = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\nGEN_FNS = {\n    'confounding': gen_confounding, 'mediation': gen_mediation,\n    'collider': gen_collider, 'exposure': gen_exposure,\n    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,\n}\n\n\n# ============================================================================\n# Sufficient Statistics & Plim (general K)\n# ============================================================================\n\ndef precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):\n    rng = np.random.default_rng(seed)\n    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    if topology == 'iv':\n        Z = first_var\n        z1 = Z == 1; z0 = Z == 0\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n        return dict(RF=RF, FS=FS, topology='iv')\n    elif topology == 'exposure':\n        return dict(p_A=DA.mean(0), E_Y=Y.mean(),\n                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')\n    else:\n        T = first_var\n        return dict(\n            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),\n            E_Y=Y.mean(), E_TY=(T * Y).mean(),\n            E_TD=(DA * T[:, None]).mean(0),\n            E_YD=(DA * Y[:, None]).mean(0), topology=topology)\n\n\ndef compute_plim(C, st, K):\n    if st['topology'] == 'iv':\n        FS_star = C @ st['FS']\n        if abs(FS_star[1]) < 1e-8:\n            return np.nan\n        return st['RF'] / FS_star[1]\n    elif st['topology'] == 'exposure':\n        q = C @ st['p_A']\n        cy = C @ st['E_YD']\n        EZZ = np.zeros((K, K))\n        EZZ[0, 0] = 1.0\n        for j in range(1, K):\n            EZZ[0, j] = EZZ[j, 0] = q[j]\n            EZZ[j, j] = q[j]\n        EZY = np.zeros(K)\n        EZY[0] = st['E_Y']\n        for j in range(1, K):\n            EZY[j] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(K, np.nan)\n    else:\n        q = C @ st['p_A']\n        ct = C @ st['E_TD']\n        cy = C @ st['E_YD']\n        dim = K + 1\n        EZZ = np.zeros((dim, dim))\n        EZZ[0, 0] = 1.0\n        EZZ[0, 1] = EZZ[1, 0] = st['E_T']\n        EZZ[1, 1] = st['E_T2']\n        for j in range(1, K):\n            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]\n            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]\n            EZZ[j + 1, j + 1] = q[j]\n        EZY = np.zeros(dim)\n        EZY[0] = st['E_Y']\n        EZY[1] = st['E_TY']\n        for j in range(1, K):\n            EZY[j + 1] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(dim, np.nan)\n\n\ndef extract_tau(plim_result, topology):\n    if topology == 'iv':\n        return float(plim_result) if np.isfinite(plim_result) else np.nan\n    if isinstance(plim_result, np.ndarray):\n        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan\n    return np.nan\n\n\n# ============================================================================\n# 1. Data Loading & Confusion Matrix\n# ============================================================================\n\ndef load_annotations(data_dir, dataset, model, prompt):\n    path = os.path.join(data_dir, dataset, f\"{model}_{prompt}_annotations.jsonl\")\n    records = []\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line.strip())\n            records.append((int(rec['true_label']), int(rec['predicted_label'])))\n    return records\n\n\ndef build_confusion_matrix(records, K):\n    counts = np.zeros((K, K))\n    for true_k, pred_k in records:\n        if 0 <= true_k < K and 0 <= pred_k < K:\n            counts[pred_k, true_k] += 1\n    col_sums = counts.sum(axis=0)\n    col_sums = np.where(col_sums < 1, 1, col_sums)\n    return counts / col_sums\n\n\ndef load_all_confusion_matrices(data_dir):\n    matrices = {}\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        for model in MODELS:\n            for prompt in PROMPTS:\n                try:\n                    records = load_annotations(data_dir, dataset, model, prompt)\n                    C = build_confusion_matrix(records, K)\n                    matrices[(dataset, model, prompt)] = C\n                except FileNotFoundError:\n                    print(f\"  [WARN] Missing: {dataset}/{model}_{prompt}\")\n    return matrices\n\n\n# ============================================================================\n# 2. Downstream Causal Bias\n# ============================================================================\n\ndef compute_bias_for_topology(C, K, topology, st, tau_true):\n    plim_result = compute_plim(C, st, K)\n    tau_hat = extract_tau(plim_result, topology)\n    if np.isnan(tau_hat) or np.isnan(tau_true):\n        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}\n    bias = tau_hat - tau_true\n    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None\n    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)\n    return {\n        'tau_hat': float(tau_hat), 'bias': float(bias),\n        'bias_pct': float(bias_pct) if bias_pct is not None else None,\n        'sign_flip': sign_flip,\n    }\n\n\ndef compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            info = compute_bias_for_topology(C, K, topology, st, tau_true)\n            results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **info,\n            })\n    return results\n\n\n# ============================================================================\n# 3. ASV Computation\n# ============================================================================\n\ndef C_interpolated(C0, delta, K):\n    C_d = (1 - delta) * np.eye(K) + delta * C0\n    C_d = np.maximum(C_d, 0.0)\n    col_sums = C_d.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C_d / col_sums\n\n\ndef compute_delta_max(C0):\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - min_diag), 10.0)\n\n\ndef compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,\n                           n_grid=1500, se_ref=None):\n    dmax = compute_delta_max(C0)\n    deltas = np.linspace(0, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = C_interpolated(C0, d, K)\n        plim_result = compute_plim(C_d, st, K)\n        tau_curve[i] = extract_tau(plim_result, topology)\n\n    bias_abs = np.abs(tau_curve - tau_true)\n    envelope = np.zeros(n_grid)\n    running_max = 0.0\n    for i in range(n_grid):\n        if np.isfinite(bias_abs[i]):\n            running_max = max(running_max, bias_abs[i])\n        envelope[i] = running_max\n\n    if asv_type == 'sign_flip':\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'magnitude':\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = 0.1 * abs(tau_true)\n        for i in range(n_grid):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'significance':\n        if se_ref is None or se_ref < 1e-12:\n            return None\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:\n                return float(deltas[i])\n        return None\n    return None\n\n\ndef estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n    tau_hats = []\n    for _ in range(n_mc):\n        first_var, Y, A = gen_fn(K, N_ref, params, rng)\n        if topology == 'iv':\n            th, _ = wald_estimator(first_var, Y, A, k=1)\n        elif topology == 'exposure':\n            b, _ = ols_no_T(Y, A, K)\n            th = b[1]\n        else:\n            b, _ = ols_with_dummies(Y, first_var, A, K)\n            th = b[1]\n        if np.isfinite(th):\n            tau_hats.append(th)\n    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan\n\n\ndef compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            se_ref = all_se_ref.get((K, topology))\n            for asv_type in ['magnitude', 'significance', 'sign_flip']:\n                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,\n                                             asv_type, se_ref=se_ref)\n                results.append({\n                    'dataset': dataset, 'model': model, 'prompt': prompt,\n                    'K': K, 'topology': topology, 'asv_type': asv_type,\n                    'asv': asv,\n                })\n    return results\n\n\n# ============================================================================\n# 4. F1 vs Downstream Bias\n# ============================================================================",
      "numLines": 300,
      "startLine": 300,
      "totalLines": 1048
    }
  }
}
```

</details>

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01QmB9W8wdutttTpKFEng1Za`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 598
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "137fb02e-d27c-4c5b-a7d1-cada75e611f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tgj4augShP4YHsWiw3PJYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4612,
      "cache_read_input_tokens": 32888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4612
      },
      "output_tokens": 38,
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

_source line 64 · 2026-05-20T21:25:03.128Z_

<details><summary>↩ Tool result · `toolu_01QmB9W8wdutttTpKFEng1Za`</summary>

```text
598	# 4. F1 vs Downstream Bias
599	# ============================================================================
600	
601	def compute_f1_from_C(C, K, p_A=None):
602	    if p_A is None:
603	        p_A = np.ones(K) / K
604	    precision = np.zeros(K)
605	    recall = np.zeros(K)
606	    f1 = np.zeros(K)
607	    for i in range(K):
608	        recall[i] = C[i, i]
609	        denom = sum(C[i, j] * p_A[j] for j in range(K))
610	        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0
611	        if precision[i] + recall[i] > 1e-12:
612	            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])
613	    return {
614	        'macro_f1': float(f1.mean()),
615	        'weighted_f1': float((p_A * f1).sum()),
616	        'per_class_f1': f1.tolist(),
617	    }
618	
619	
620	def f1_vs_bias_analysis(confusion_matrices, biases):
621	    results = []
622	    for b in biases:
623	        key = (b['dataset'], b['model'], b['prompt'])
624	        if key not in confusion_matrices:
625	            continue
626	        C = confusion_matrices[key]
627	        K = b['K']
628	        p_A = make_p_A(K)
629	        f1_info = compute_f1_from_C(C, K, p_A)
630	        abs_bias = abs(b['bias']) if b['bias'] is not None else None
631	        results.append({
632	            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],
633	            'K': K, 'topology': b['topology'],
634	            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],
635	            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],
636	            'sign_flip': b['sign_flip'],
637	        })
638	    return results
639	
640	
641	# ============================================================================
642	# 5. Type I/II Error Rates
643	# ============================================================================
644	
645	def compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,
646	                              st_H1, tau_true,
647	                              n_sim=100, N_sample=5000, seed=42):
648	    gen_fn = GEN_FNS[topology]
649	    rng = np.random.default_rng(seed)
650	
651	    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')
652	    asv_safe = (masv is None or masv > 1.0)
653	
654	    def _run_mc(params_t, n):
655	        valid = 0; rej = 0
656	        for _ in range(n):
657	            fv, Y, A = gen_fn(K, N_sample, params_t, rng)
658	            Astar = generate_Astar(A, C, rng)
659	            if topology == 'iv':
660	                th, se = wald_estimator(fv, Y, Astar, k=1)
661	            elif topology == 'exposure':
662	                b, svec = ols_no_T(Y, Astar, K)
663	                th, se = b[1], svec[1]
664	            else:
665	                b, svec = ols_with_dummies(Y, fv, Astar, K)
666	                th, se = b[1], svec[1]
667	            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:
668	                valid += 1
669	                if abs(th / se) > 1.96:
670	                    rej += 1
671	        return rej / max(valid, 1), valid
672	
673	    type1_before, v0 = _run_mc(params_H0, n_sim)
674	    power_before, v1 = _run_mc(params_H1, n_sim)
675	    type1_after = type1_before if asv_safe else 0.0
676	    power_after = power_before if asv_safe else 0.0
677	
678	    return {
679	        'type1_before': float(type1_before), 'type1_after': float(type1_after),
680	        'power_before': float(power_before), 'power_after': float(power_after),
681	        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,
682	        'valid_h0': int(v0), 'valid_h1': int(v1),
683	    }
684	
685	
686	# ============================================================================
687	# 6. Inter-model Error Correlation
688	# ============================================================================
689	
690	def compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,
691	                                    n_samples=1000, seed=42):
692	    rng = np.random.default_rng(seed)
693	    p_A = make_p_A(K)
694	    true_labels = rng.choice(K, size=n_samples, p=p_A)
695	
696	    predictions = {}
697	    for model in MODELS:
698	        key = (dataset, model, prompt)
699	        if key in confusion_matrices:
700	            predictions[model] = generate_Astar(true_labels,
701	                                                confusion_matrices[key], rng)
702	        else:
703	            predictions[model] = true_labels.copy()
704	
705	    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]
706	    results = {}
707	    for m1, m2 in pairs:
708	        p1, p2 = predictions[m1], predictions[m2]
709	        agreement = float((p1 == p2).mean())
710	        observed = agreement
711	        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))
712	        kappa = float((observed - expected) / (1 - expected)
713	                      ) if expected < 1 - 1e-10 else 0.0
714	        err1 = (p1 != true_labels).astype(float)
715	        err2 = (p2 != true_labels).astype(float)
716	        if err1.std() > 1e-10 and err2.std() > 1e-10:
717	            error_corr = float(np.corrcoef(err1, err2)[0, 1])
718	        else:
719	            error_corr = 0.0
720	        results[f"{m1}-{m2}"] = {
721	            'agreement': agreement,
722	            'kappa': kappa,
723	            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,
724	        }
725	    return results
726	
727	
728	# ============================================================================
729	# Mock Data Generation
730	# ============================================================================
731	
732	def generate_mock_C(K, rng, diag_range):
733	    C = np.zeros((K, K))
734	    for j in range(K):
735	        diag_val = rng.uniform(diag_range[0], diag_range[1])
736	        remaining = 1.0 - diag_val
737	        if K > 2:
738	            dists = np.abs(np.arange(K) - j).astype(float)
739	            dists[j] = np.inf
740	            weights = 1.0 / dists
741	            weights[j] = 0
742	            noise = rng.uniform(0.5, 1.5, K)
743	            noise[j] = 0
744	            weights = weights * noise
745	            weights /= weights.sum()
746	            C[:, j] = remaining * weights
747	        else:
748	            C[1 - j, j] = remaining
749	        C[j, j] = diag_val
750	    return C
751	
752	
753	def generate_mock_confusion_matrices(seed=12345):
754	    rng = np.random.default_rng(seed)
755	    matrices = {}
756	    diag_ranges = {
757	        'civil_comments': (0.85, 0.95),
758	        'vast': (0.70, 0.90),
759	        'humaid': (0.60, 0.85),
760	    }
761	    for dataset, info in DATASETS.items():
762	        K = info['K']
763	        dr = diag_ranges[dataset]
764	        for model in MODELS:
765	            for prompt in PROMPTS:
766	                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)
767	    return matrices
768	
769	
770	# ============================================================================
771	# Diagnostic Plots (optional)
772	# ============================================================================
773	
774	def save_f1_vs_bias_plot(f1_bias, output_dir):
775	    if not HAS_MPL:
776	        return
777	    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
778	    axes = axes.flatten()
779	    for idx, topo in enumerate(TOPOLOGIES):
780	        ax = axes[idx]
781	        subset = [r for r in f1_bias if r['topology'] == topo
782	                  and r['abs_bias'] is not None]
783	        if not subset:
784	            ax.set_title(topo)
785	            continue
786	        f1s = [r['macro_f1'] for r in subset]
787	        biases = [r['abs_bias'] for r in subset]
788	        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]
789	        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)
790	        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)
791	        ax.set_xlabel('Macro F1')
792	        ax.set_ylabel('|bias|')
793	        ax.set_title(topo)
794	    if len(TOPOLOGIES) < 8:
795	        axes[-1].axis('off')
796	    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)
797	    fig.tight_layout(rect=[0, 0, 1, 0.96])
798	    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)
799	    plt.close(fig)
800	
801	
802	def save_asv_heatmap(asvs, output_dir):
803	    if not HAS_MPL:
804	        return
805	    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']
806	    datasets_list = list(DATASETS.keys())
807	    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
808	    for didx, dataset in enumerate(datasets_list):
809	        ax = axes[didx]
810	        subset = [r for r in mag_asvs if r['dataset'] == dataset]
811	        configs = sorted(set((r['model'], r['prompt']) for r in subset))
812	        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)
813	        for r in subset:
814	            ti = TOPOLOGIES.index(r['topology'])
815	            ci = configs.index((r['model'], r['prompt']))
816	            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan
817	        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',
818	                       vmin=0, vmax=2)
819	        ax.set_xticks(range(len(configs)))
820	        ax.set_xticklabels([f"{m[:3]}_{p[:3]}" for m, p in configs],
821	                           rotation=45, ha='right', fontsize=7)
822	        ax.set_yticks(range(len(TOPOLOGIES)))
823	        ax.set_yticklabels(TOPOLOGIES, fontsize=8)
824	        ax.set_title(f'{dataset} (K={DATASETS[dataset]["K"]})')
825	        plt.colorbar(im, ax=ax, shrink=0.8)
826	    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)
827	    fig.tight_layout(rect=[0, 0, 1, 0.96])
828	    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)
829	    plt.close(fig)
830	
831	
832	# ============================================================================
833	# JSON Serialization
834	# ============================================================================
835	
836	def _to_json_safe(obj):
837	    if isinstance(obj, np.integer):
838	        return int(obj)
839	    elif isinstance(obj, np.floating):
840	        v = float(obj)
841	        return None if (np.isnan(v) or np.isinf(v)) else v
842	    elif isinstance(obj, np.ndarray):
843	        return _to_json_safe(obj.tolist())
844	    elif isinstance(obj, dict):
845	        return {str(k): _to_json_safe(v) for k, v in obj.items()}
846	    elif isinstance(obj, list):
847	        return [_to_json_safe(v) for v in obj]
848	    elif isinstance(obj, (bool, np.bool_)):
849	        return bool(obj)
850	    elif isinstance(obj, float):
851	        return None if (np.isnan(obj) or np.isinf(obj)) else obj
852	    return obj
853	
854	
855	# ============================================================================
856	# Main
857	# ============================================================================
858	
859	def main():
860	    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')
861	    parser.add_argument('--data-dir', default='data/')
862	    parser.add_argument('--output-dir', default='artifacts/plan006/')
863	    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')
864	    parser.add_argument('--n-sim', type=int, default=1000)
865	    parser.add_argument('--device', type=str, default='cpu')
866	    args = parser.parse_args()
867	
868	    os.makedirs(args.output_dir, exist_ok=True)
869	    t_total = time.time()
870	    n_precomp = 500_000 if args.mock else N_PRECOMP
871	
872	    print("=" * 70)
873	    print("plan_006: Empirical ASV Calibration")
874	    print("=" * 70)
875	
876	    # --- 1. Confusion matrices ---
877	    if args.mock:
878	        print("\n[1/6] Generating mock confusion matrices...")
879	        confusion_matrices = generate_mock_confusion_matrices()
880	    else:
881	        print("\n[1/6] Loading confusion matrices...")
882	        confusion_matrices = load_all_confusion_matrices(args.data_dir)
883	
884	    print(f"  {len(confusion_matrices)} matrices loaded")
885	    for (ds, m, p), C in list(confusion_matrices.items())[:3]:
886	        K = DATASETS[ds]['K']
887	        print(f"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}")
888	
889	    # --- 2. Precompute sufficient statistics ---
890	    print("\n[2/6] Precomputing sufficient statistics...")
891	    K_values = sorted(set(DATASETS[ds]['K'] for ds in DATASETS))
892	    all_suff_stats = {}
893	    all_tau_true = {}
894	    all_params = {}
895	    all_params_H0 = {}
896	    all_se_ref = {}
897	
898	    for K in K_values:
899	        params = make_dgp_params(K)
900	        params_H0 = make_dgp_params_H0(K, params)
901	        all_params[K] = params
902	        all_params_H0[K] = params_H0
903	        for topology in TOPOLOGIES:
904	            seed = K * 1000 + abs(hash(topology)) % 1000
905	            st = precompute_suff_stats(K, topology, params[topology],
906	                                       N=n_precomp, seed=seed)
907	            plim_I = compute_plim(np.eye(K), st, K)
908	            tau_true = extract_tau(plim_I, topology)
909	            all_suff_stats[(K, topology)] = st
910	            all_tau_true[(K, topology)] = tau_true
911	
912	            se = estimate_reference_se(K, topology, params[topology],
913	                                       N_ref=5000,
914	                                       n_mc=min(args.n_sim, 30),
915	                                       seed=seed + 500)
916	            all_se_ref[(K, topology)] = se
917	            se_s = f"{se:.4f}" if np.isfinite(se) else "N/A"
918	            print(f"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}")
919	
920	    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)
921	    n_sign_flips = sum(1 for b in biases if b['sign_flip'])
922	    print(f"  {len(biases)} bias values ({n_sign_flips} sign flips)")
923	
924	    # --- 3. ASV ---
925	    print("\n[3/6] Computing ASV values...")
926	    t3 = time.time()
927	    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,
928	                            all_tau_true, all_se_ref)
929	    print(f"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)")
930	    for at in ['magnitude', 'sign_flip', 'significance']:
931	        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]
932	        if sub:
933	            print(f"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} "
934	                  f"max={max(sub):.3f} ({len(sub)} non-None)")
935	
936	    # --- 4. F1 vs bias ---
937	    print("\n[4/6] F1 vs bias analysis...")
938	    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)
939	    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]
940	    high_f1_high_bias = [r for r in total_high_f1
941	                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]
942	    if total_high_f1:
943	        pct = len(high_f1_high_bias) / len(total_high_f1) * 100
944	        print(f"  Baumann check: F1>0.93 with |bias|>0.05: "
945	              f"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%")
946	    # Sample rows
947	    for r in f1_bias[:3]:
948	        print(f"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: "
949	              f"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}")
950	
951	    # --- 5. Type I/II ---
952	    print("\n[5/6] Type I/II error rates...")
953	    t5 = time.time()
954	    type1_type2_results = []
955	    n_configs = len(confusion_matrices) * len(TOPOLOGIES)
956	    idx = 0
957	    for (dataset, model, prompt), C in confusion_matrices.items():
958	        K = DATASETS[dataset]['K']
959	        for topology in TOPOLOGIES:
960	            idx += 1
961	            st = all_suff_stats[(K, topology)]
962	            tau_true = all_tau_true[(K, topology)]
963	            r = compute_type1_type2_for_C(
964	                C, K, topology, all_params[K], all_params_H0[K],
965	                st, tau_true,
966	                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)
967	            type1_type2_results.append({
968	                'dataset': dataset, 'model': model, 'prompt': prompt,
969	                'K': K, 'topology': topology, **r,
970	            })
971	            if idx % 50 == 0:
972	                print(f"    {idx}/{n_configs}...")
973	    print(f"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)")
974	    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])
975	    print(f"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}")
976	
977	    # --- 6. Inter-model correlation ---
978	    print("\n[6/6] Inter-model error correlation...")
979	    inter_model_results = {}
980	    for dataset in DATASETS:
981	        K = DATASETS[dataset]['K']
982	        for prompt in PROMPTS:
983	            r = compute_inter_model_correlation(
984	                confusion_matrices, K, dataset, prompt,
985	                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)
986	            inter_model_results[f"{dataset}_{prompt}"] = r
987	    print(f"  {len(inter_model_results)} (dataset, prompt) pairs")
988	    for key, pairs in list(inter_model_results.items())[:2]:
989	        for pair, vals in pairs.items():
990	            print(f"    {key} {pair}: agree={vals['agreement']:.3f} "
991	                  f"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}")
992	
993	    # --- Summary ---
994	    summary = {
995	        'f1_gt_093_total': len(total_high_f1),
996	        'f1_gt_093_with_high_bias_pct': (
997	            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),
998	        'ppi_recommended_scenarios': unsafe,
999	        'total_scenarios': len(type1_type2_results),
1000	        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,
1001	    }
1002	
1003	    # --- Save ---
1004	    output = _to_json_safe({
1005	        'confusion_matrices': {
1006	            f"{ds}_{m}_{p}": C.tolist()
1007	            for (ds, m, p), C in confusion_matrices.items()
1008	        },
1009	        'biases': biases,
1010	        'asvs': asvs,
1011	        'f1_vs_bias': f1_bias,
1012	        'type1_type2': type1_type2_results,
1013	        'inter_model_correlation': inter_model_results,
1014	        'summary': summary,
1015	    })
1016	
1017	    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')
1018	    with open(out_path, 'w') as f:
1019	        json.dump(output, f, indent=2, default=str)
1020	    print(f"\nResults saved to {out_path}")
1021	
1022	    # --- Plots ---
1023	    save_f1_vs_bias_plot(f1_bias, args.output_dir)
1024	    save_asv_heatmap(asvs, args.output_dir)
1025	    if HAS_MPL:
1026	        print(f"Plots saved to {args.output_dir}")
1027	
1028	    # --- Validation ---
1029	    with open(out_path) as f:
1030	        data = json.load(f)
1031	    n_null = str(data).count('null')
1032	    print(f"\nValidation: JSON has {n_null} null values "
1033	          f"(expected for NaN/None ASV entries)")
1034	    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:
1035	        print(f"  {section}: {len(data[section])} records")
1036	
1037	    elapsed = time.time() - t_total
1038	    print(f"\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)")
1039	    print(f"\nSummary:")
1040	    print(f"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%")
1041	    print(f"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/"
1042	          f"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)")
1043	    print("=" * 70)
1044	
1045	
1046	if __name__ == "__main__":
1047	    main()
1048	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "81f757f8-4964-4a79-ac58-50d6ca73144e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
      "content": "# 4. F1 vs Downstream Bias\n# ============================================================================\n\ndef compute_f1_from_C(C, K, p_A=None):\n    if p_A is None:\n        p_A = np.ones(K) / K\n    precision = np.zeros(K)\n    recall = np.zeros(K)\n    f1 = np.zeros(K)\n    for i in range(K):\n        recall[i] = C[i, i]\n        denom = sum(C[i, j] * p_A[j] for j in range(K))\n        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0\n        if precision[i] + recall[i] > 1e-12:\n            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])\n    return {\n        'macro_f1': float(f1.mean()),\n        'weighted_f1': float((p_A * f1).sum()),\n        'per_class_f1': f1.tolist(),\n    }\n\n\ndef f1_vs_bias_analysis(confusion_matrices, biases):\n    results = []\n    for b in biases:\n        key = (b['dataset'], b['model'], b['prompt'])\n        if key not in confusion_matrices:\n            continue\n        C = confusion_matrices[key]\n        K = b['K']\n        p_A = make_p_A(K)\n        f1_info = compute_f1_from_C(C, K, p_A)\n        abs_bias = abs(b['bias']) if b['bias'] is not None else None\n        results.append({\n            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],\n            'K': K, 'topology': b['topology'],\n            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],\n            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],\n            'sign_flip': b['sign_flip'],\n        })\n    return results\n\n\n# ============================================================================\n# 5. Type I/II Error Rates\n# ============================================================================\n\ndef compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,\n                              st_H1, tau_true,\n                              n_sim=100, N_sample=5000, seed=42):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n\n    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')\n    asv_safe = (masv is None or masv > 1.0)\n\n    def _run_mc(params_t, n):\n        valid = 0; rej = 0\n        for _ in range(n):\n            fv, Y, A = gen_fn(K, N_sample, params_t, rng)\n            Astar = generate_Astar(A, C, rng)\n            if topology == 'iv':\n                th, se = wald_estimator(fv, Y, Astar, k=1)\n            elif topology == 'exposure':\n                b, svec = ols_no_T(Y, Astar, K)\n                th, se = b[1], svec[1]\n            else:\n                b, svec = ols_with_dummies(Y, fv, Astar, K)\n                th, se = b[1], svec[1]\n            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:\n                valid += 1\n                if abs(th / se) > 1.96:\n                    rej += 1\n        return rej / max(valid, 1), valid\n\n    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)\n    type1_after = type1_before if asv_safe else 0.0\n    power_after = power_before if asv_safe else 0.0\n\n    return {\n        'type1_before': float(type1_before), 'type1_after': float(type1_after),\n        'power_before': float(power_before), 'power_after': float(power_after),\n        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,\n        'valid_h0': int(v0), 'valid_h1': int(v1),\n    }\n\n\n# ============================================================================\n# 6. Inter-model Error Correlation\n# ============================================================================\n\ndef compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,\n                                    n_samples=1000, seed=42):\n    rng = np.random.default_rng(seed)\n    p_A = make_p_A(K)\n    true_labels = rng.choice(K, size=n_samples, p=p_A)\n\n    predictions = {}\n    for model in MODELS:\n        key = (dataset, model, prompt)\n        if key in confusion_matrices:\n            predictions[model] = generate_Astar(true_labels,\n                                                confusion_matrices[key], rng)\n        else:\n            predictions[model] = true_labels.copy()\n\n    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]\n    results = {}\n    for m1, m2 in pairs:\n        p1, p2 = predictions[m1], predictions[m2]\n        agreement = float((p1 == p2).mean())\n        observed = agreement\n        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))\n        kappa = float((observed - expected) / (1 - expected)\n                      ) if expected < 1 - 1e-10 else 0.0\n        err1 = (p1 != true_labels).astype(float)\n        err2 = (p2 != true_labels).astype(float)\n        if err1.std() > 1e-10 and err2.std() > 1e-10:\n            error_corr = float(np.corrcoef(err1, err2)[0, 1])\n        else:\n            error_corr = 0.0\n        results[f\"{m1}-{m2}\"] = {\n            'agreement': agreement,\n            'kappa': kappa,\n            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,\n        }\n    return results\n\n\n# ============================================================================\n# Mock Data Generation\n# ============================================================================\n\ndef generate_mock_C(K, rng, diag_range):\n    C = np.zeros((K, K))\n    for j in range(K):\n        diag_val = rng.uniform(diag_range[0], diag_range[1])\n        remaining = 1.0 - diag_val\n        if K > 2:\n            dists = np.abs(np.arange(K) - j).astype(float)\n            dists[j] = np.inf\n            weights = 1.0 / dists\n            weights[j] = 0\n            noise = rng.uniform(0.5, 1.5, K)\n            noise[j] = 0\n            weights = weights * noise\n            weights /= weights.sum()\n            C[:, j] = remaining * weights\n        else:\n            C[1 - j, j] = remaining\n        C[j, j] = diag_val\n    return C\n\n\ndef generate_mock_confusion_matrices(seed=12345):\n    rng = np.random.default_rng(seed)\n    matrices = {}\n    diag_ranges = {\n        'civil_comments': (0.85, 0.95),\n        'vast': (0.70, 0.90),\n        'humaid': (0.60, 0.85),\n    }\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        dr = diag_ranges[dataset]\n        for model in MODELS:\n            for prompt in PROMPTS:\n                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)\n    return matrices\n\n\n# ============================================================================\n# Diagnostic Plots (optional)\n# ============================================================================\n\ndef save_f1_vs_bias_plot(f1_bias, output_dir):\n    if not HAS_MPL:\n        return\n    fig, axes = plt.subplots(2, 4, figsize=(20, 10))\n    axes = axes.flatten()\n    for idx, topo in enumerate(TOPOLOGIES):\n        ax = axes[idx]\n        subset = [r for r in f1_bias if r['topology'] == topo\n                  and r['abs_bias'] is not None]\n        if not subset:\n            ax.set_title(topo)\n            continue\n        f1s = [r['macro_f1'] for r in subset]\n        biases = [r['abs_bias'] for r in subset]\n        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]\n        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)\n        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)\n        ax.set_xlabel('Macro F1')\n        ax.set_ylabel('|bias|')\n        ax.set_title(topo)\n    if len(TOPOLOGIES) < 8:\n        axes[-1].axis('off')\n    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)\n    plt.close(fig)\n\n\ndef save_asv_heatmap(asvs, output_dir):\n    if not HAS_MPL:\n        return\n    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']\n    datasets_list = list(DATASETS.keys())\n    fig, axes = plt.subplots(1, 3, figsize=(18, 6))\n    for didx, dataset in enumerate(datasets_list):\n        ax = axes[didx]\n        subset = [r for r in mag_asvs if r['dataset'] == dataset]\n        configs = sorted(set((r['model'], r['prompt']) for r in subset))\n        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)\n        for r in subset:\n            ti = TOPOLOGIES.index(r['topology'])\n            ci = configs.index((r['model'], r['prompt']))\n            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan\n        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',\n                       vmin=0, vmax=2)\n        ax.set_xticks(range(len(configs)))\n        ax.set_xticklabels([f\"{m[:3]}_{p[:3]}\" for m, p in configs],\n                           rotation=45, ha='right', fontsize=7)\n        ax.set_yticks(range(len(TOPOLOGIES)))\n        ax.set_yticklabels(TOPOLOGIES, fontsize=8)\n        ax.set_title(f'{dataset} (K={DATASETS[dataset][\"K\"]})')\n        plt.colorbar(im, ax=ax, shrink=0.8)\n    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)\n    plt.close(fig)\n\n\n# ============================================================================\n# JSON Serialization\n# ============================================================================\n\ndef _to_json_safe(obj):\n    if isinstance(obj, np.integer):\n        return int(obj)\n    elif isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    elif isinstance(obj, np.ndarray):\n        return _to_json_safe(obj.tolist())\n    elif isinstance(obj, dict):\n        return {str(k): _to_json_safe(v) for k, v in obj.items()}\n    elif isinstance(obj, list):\n        return [_to_json_safe(v) for v in obj]\n    elif isinstance(obj, (bool, np.bool_)):\n        return bool(obj)\n    elif isinstance(obj, float):\n        return None if (np.isnan(obj) or np.isinf(obj)) else obj\n    return obj\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')\n    parser.add_argument('--data-dir', default='data/')\n    parser.add_argument('--output-dir', default='artifacts/plan006/')\n    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')\n    parser.add_argument('--n-sim', type=int, default=1000)\n    parser.add_argument('--device', type=str, default='cpu')\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    t_total = time.time()\n    n_precomp = 500_000 if args.mock else N_PRECOMP\n\n    print(\"=\" * 70)\n    print(\"plan_006: Empirical ASV Calibration\")\n    print(\"=\" * 70)\n\n    # --- 1. Confusion matrices ---\n    if args.mock:\n        print(\"\\n[1/6] Generating mock confusion matrices...\")\n        confusion_matrices = generate_mock_confusion_matrices()\n    else:\n        print(\"\\n[1/6] Loading confusion matrices...\")\n        confusion_matrices = load_all_confusion_matrices(args.data_dir)\n\n    print(f\"  {len(confusion_matrices)} matrices loaded\")\n    for (ds, m, p), C in list(confusion_matrices.items())[:3]:\n        K = DATASETS[ds]['K']\n        print(f\"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}\")\n\n    # --- 2. Precompute sufficient statistics ---\n    print(\"\\n[2/6] Precomputing sufficient statistics...\")\n    K_values = sorted(set(DATASETS[ds]['K'] for ds in DATASETS))\n    all_suff_stats = {}\n    all_tau_true = {}\n    all_params = {}\n    all_params_H0 = {}\n    all_se_ref = {}\n\n    for K in K_values:\n        params = make_dgp_params(K)\n        params_H0 = make_dgp_params_H0(K, params)\n        all_params[K] = params\n        all_params_H0[K] = params_H0\n        for topology in TOPOLOGIES:\n            seed = K * 1000 + abs(hash(topology)) % 1000\n            st = precompute_suff_stats(K, topology, params[topology],\n                                       N=n_precomp, seed=seed)\n            plim_I = compute_plim(np.eye(K), st, K)\n            tau_true = extract_tau(plim_I, topology)\n            all_suff_stats[(K, topology)] = st\n            all_tau_true[(K, topology)] = tau_true\n\n            se = estimate_reference_se(K, topology, params[topology],\n                                       N_ref=5000,\n                                       n_mc=min(args.n_sim, 30),\n                                       seed=seed + 500)\n            all_se_ref[(K, topology)] = se\n            se_s = f\"{se:.4f}\" if np.isfinite(se) else \"N/A\"\n            print(f\"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}\")\n\n    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)\n    n_sign_flips = sum(1 for b in biases if b['sign_flip'])\n    print(f\"  {len(biases)} bias values ({n_sign_flips} sign flips)\")\n\n    # --- 3. ASV ---\n    print(\"\\n[3/6] Computing ASV values...\")\n    t3 = time.time()\n    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,\n                            all_tau_true, all_se_ref)\n    print(f\"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)\")\n    for at in ['magnitude', 'sign_flip', 'significance']:\n        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]\n        if sub:\n            print(f\"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} \"\n                  f\"max={max(sub):.3f} ({len(sub)} non-None)\")\n\n    # --- 4. F1 vs bias ---\n    print(\"\\n[4/6] F1 vs bias analysis...\")\n    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)\n    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]\n    high_f1_high_bias = [r for r in total_high_f1\n                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]\n    if total_high_f1:\n        pct = len(high_f1_high_bias) / len(total_high_f1) * 100\n        print(f\"  Baumann check: F1>0.93 with |bias|>0.05: \"\n              f\"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%\")\n    # Sample rows\n    for r in f1_bias[:3]:\n        print(f\"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: \"\n              f\"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}\")\n\n    # --- 5. Type I/II ---\n    print(\"\\n[5/6] Type I/II error rates...\")\n    t5 = time.time()\n    type1_type2_results = []\n    n_configs = len(confusion_matrices) * len(TOPOLOGIES)\n    idx = 0\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            idx += 1\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            r = compute_type1_type2_for_C(\n                C, K, topology, all_params[K], all_params_H0[K],\n                st, tau_true,\n                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)\n            type1_type2_results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **r,\n            })\n            if idx % 50 == 0:\n                print(f\"    {idx}/{n_configs}...\")\n    print(f\"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)\")\n    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])\n    print(f\"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}\")\n\n    # --- 6. Inter-model correlation ---\n    print(\"\\n[6/6] Inter-model error correlation...\")\n    inter_model_results = {}\n    for dataset in DATASETS:\n        K = DATASETS[dataset]['K']\n        for prompt in PROMPTS:\n            r = compute_inter_model_correlation(\n                confusion_matrices, K, dataset, prompt,\n                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)\n            inter_model_results[f\"{dataset}_{prompt}\"] = r\n    print(f\"  {len(inter_model_results)} (dataset, prompt) pairs\")\n    for key, pairs in list(inter_model_results.items())[:2]:\n        for pair, vals in pairs.items():\n            print(f\"    {key} {pair}: agree={vals['agreement']:.3f} \"\n                  f\"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}\")\n\n    # --- Summary ---\n    summary = {\n        'f1_gt_093_total': len(total_high_f1),\n        'f1_gt_093_with_high_bias_pct': (\n            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),\n        'ppi_recommended_scenarios': unsafe,\n        'total_scenarios': len(type1_type2_results),\n        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,\n    }\n\n    # --- Save ---\n    output = _to_json_safe({\n        'confusion_matrices': {\n            f\"{ds}_{m}_{p}\": C.tolist()\n            for (ds, m, p), C in confusion_matrices.items()\n        },\n        'biases': biases,\n        'asvs': asvs,\n        'f1_vs_bias': f1_bias,\n        'type1_type2': type1_type2_results,\n        'inter_model_correlation': inter_model_results,\n        'summary': summary,\n    })\n\n    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n    # --- Plots ---\n    save_f1_vs_bias_plot(f1_bias, args.output_dir)\n    save_asv_heatmap(asvs, args.output_dir)\n    if HAS_MPL:\n        print(f\"Plots saved to {args.output_dir}\")\n\n    # --- Validation ---\n    with open(out_path) as f:\n        data = json.load(f)\n    n_null = str(data).count('null')\n    print(f\"\\nValidation: JSON has {n_null} null values \"\n          f\"(expected for NaN/None ASV entries)\")\n    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:\n        print(f\"  {section}: {len(data[section])} records\")\n\n    elapsed = time.time() - t_total\n    print(f\"\\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)\")\n    print(f\"\\nSummary:\")\n    print(f\"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%\")\n    print(f\"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/\"\n          f\"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 451,
      "startLine": 598,
      "totalLines": 1048
    }
  }
}
```

</details>

---


### Assistant

_source line 65_

Script is 1048 lines. Now I have the full picture. Let me deploy it to the server and run the dry-run.

There's a bug I spotted: `compute_type1_type2_for_C` passes `params_H1` and `params_H0` as dicts of all topologies, but `_run_mc` passes them directly to `gen_fn` which expects topology-specific params. Let me fix that before deploying.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "bf5de390-32ac-43c7-9ed7-f8b97342592c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbezCy1xHq93XNuCFDscPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7332,
      "cache_read_input_tokens": 37500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7332
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

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3GWwpXBkH1MXJRroKtxhp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 645,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "074b2da6-d209-449a-a227-94c9d1d76707",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbezCy1xHq93XNuCFDscPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7332,
      "cache_read_input_tokens": 37500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7332
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


### Tool result

_source line 67 · 2026-05-20T21:25:10.082Z_

<details><summary>↩ Tool result · `toolu_01Q3GWwpXBkH1MXJRroKtxhp`</summary>

```text
645	def compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,
646	                              st_H1, tau_true,
647	                              n_sim=100, N_sample=5000, seed=42):
648	    gen_fn = GEN_FNS[topology]
649	    rng = np.random.default_rng(seed)
650	
651	    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')
652	    asv_safe = (masv is None or masv > 1.0)
653	
654	    def _run_mc(params_t, n):
655	        valid = 0; rej = 0
656	        for _ in range(n):
657	            fv, Y, A = gen_fn(K, N_sample, params_t, rng)
658	            Astar = generate_Astar(A, C, rng)
659	            if topology == 'iv':
660	                th, se = wald_estimator(fv, Y, Astar, k=1)
661	            elif topology == 'exposure':
662	                b, svec = ols_no_T(Y, Astar, K)
663	                th, se = b[1], svec[1]
664	            else:
665	                b, svec = ols_with_dummies(Y, fv, Astar, K)
666	                th, se = b[1], svec[1]
667	            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:
668	                valid += 1
669	                if abs(th / se) > 1.96:
670	                    rej += 1
671	        return rej / max(valid, 1), valid
672	
673	    type1_before, v0 = _run_mc(params_H0, n_sim)
674	    power_before, v1 = _run_mc(params_H1, n_sim)
675	    type1_after = type1_before if asv_safe else 0.0
676	    power_after = power_before if asv_safe else 0.0
677	
678	    return {
679	        'type1_before': float(type1_before), 'type1_after': float(type1_after),
680	        'power_before': float(power_before), 'power_after': float(power_after),
681	        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,
682	        'valid_h0': int(v0), 'valid_h1': int(v1),
683	    }
684	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "08a361a3-d829-47bd-9d56-7ec988d898e4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
      "content": "def compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,\n                              st_H1, tau_true,\n                              n_sim=100, N_sample=5000, seed=42):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n\n    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')\n    asv_safe = (masv is None or masv > 1.0)\n\n    def _run_mc(params_t, n):\n        valid = 0; rej = 0\n        for _ in range(n):\n            fv, Y, A = gen_fn(K, N_sample, params_t, rng)\n            Astar = generate_Astar(A, C, rng)\n            if topology == 'iv':\n                th, se = wald_estimator(fv, Y, Astar, k=1)\n            elif topology == 'exposure':\n                b, svec = ols_no_T(Y, Astar, K)\n                th, se = b[1], svec[1]\n            else:\n                b, svec = ols_with_dummies(Y, fv, Astar, K)\n                th, se = b[1], svec[1]\n            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:\n                valid += 1\n                if abs(th / se) > 1.96:\n                    rej += 1\n        return rej / max(valid, 1), valid\n\n    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)\n    type1_after = type1_before if asv_safe else 0.0\n    power_after = power_before if asv_safe else 0.0\n\n    return {\n        'type1_before': float(type1_before), 'type1_after': float(type1_after),\n        'power_before': float(power_before), 'power_after': float(power_after),\n        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,\n        'valid_h0': int(v0), 'valid_h1': int(v1),\n    }\n",
      "numLines": 40,
      "startLine": 645,
      "totalLines": 1048
    }
  }
}
```

</details>

---


### Assistant

_source line 68_

Now let me check how it's called in main:

The call at line 963 passes `all_params[K]` and `all_params_H0[K]` — those are dicts keyed by topology (e.g. `{'confounding': {...}, 'mediation': {...}, ...}`). But `_run_mc` passes them directly to `gen_fn(K, N_sample, params_t, rng)`, which expects topology-specific params dict. This will crash because the DGP generator will try to access keys like `p_A` in a dict keyed by topology names.

Let me fix this:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "69b1956a-bbbd-4249-8d8f-da2aeb0c25c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tMSXRYVzDpFnW1hVKRJQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 44832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 950
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

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_018E4x5DirLg3qKCWtSEyL1W`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "old_string": "    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)",
  "new_string": "    type1_before, v0 = _run_mc(params_H0[topology], n_sim)\n    power_before, v1 = _run_mc(params_H1[topology], n_sim)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "e4113682-6706-4fb5-83ff-446508100c3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tMSXRYVzDpFnW1hVKRJQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 44832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 950
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


### Tool result

_source line 70 · 2026-05-20T21:25:16.314Z_

<details><summary>↩ Tool result · `toolu_018E4x5DirLg3qKCWtSEyL1W`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "3339da9b-190a-4641-8f7c-5ba3c3fd452c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
    "oldString": "    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)",
    "newString": "    type1_before, v0 = _run_mc(params_H0[topology], n_sim)\n    power_before, v1 = _run_mc(params_H1[topology], n_sim)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices\n\nUses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts\n= 27 C matrices) to compute:\n  1. Downstream causal bias across 7 DAG topologies\n  2. ASV sensitivity metrics (magnitude, significance, sign-flip)\n  3. F1 vs bias disconnect analysis (Baumann 2025 verification)\n  4. Type I/II error rates before/after ASV filtering\n  5. Inter-model error correlation\n\nInput:  data/{dataset}/{model}_{prompt}_annotations.jsonl\n        Each line: {\"true_label\": int, \"predicted_label\": int}\n\nOutput: artifacts/plan006/asv_empirical_results.json\n\nDependencies: numpy (required), matplotlib (optional for plots)\n\"\"\"\n\nimport numpy as np\nimport json\nimport argparse\nimport os\nimport time\nfrom collections import OrderedDict\n\ntry:\n    import matplotlib\n    matplotlib.use('Agg')\n    import matplotlib.pyplot as plt\n    HAS_MPL = True\nexcept ImportError:\n    HAS_MPL = False\n\n# ============================================================================\n# Constants\n# ============================================================================\n\nDATASETS = OrderedDict([\n    ('civil_comments', {'K': 2}),\n    ('vast', {'K': 3}),\n    ('humaid', {'K': 10}),\n])\n\nMODELS = ['llama4', 'qwen3', 'deepseek']\nPROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']\n\nTOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\n\nN_PRECOMP = 2_000_000\n\n# Parameter pools — K=3 values match plan_001/plan_005\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]\n\n\n# ============================================================================\n# Utility Functions\n# ============================================================================\n\ndef softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef ols_no_T(Y, Astar, K):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\ndef wald_estimator(Z, Y, Astar, k=1):\n    z1 = Z == 1; z0 = Z == 0\n    n1, n0 = float(z1.sum()), float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    W = RF / FS\n    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    return W, np.sqrt(max(var_W, 0))\n\n\n# ============================================================================\n# DGP Parameters (general K, K=3 matches plan_001/plan_005)\n# ============================================================================\n\ndef make_p_A(K):\n    if K == 2:\n        return np.array([0.55, 0.45])\n    elif K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    else:\n        raw = np.array([1.0 / (i + 1) for i in range(K)])\n        return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A,\n            'alpha': np.array(_ALPHA_POOL[:K - 1]),\n            'beta_A': np.array(_BETA_A_POOL[:K - 1]),\n            'beta_T': 2.0,\n            'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'collider': {\n            'tau': 1.0,\n            'g': np.zeros(K),\n            'dT': np.array(_DT_POOL[:K]),\n            'dY': np.array(_DY_POOL[:K]),\n        },\n        'exposure': {\n            'beta': np.array(_BETA_POOL[:K]),\n            'p_A': p_A,\n        },\n    }\n    if K == 3:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(3),\n            'a_U1': np.array([0.0, 0.8, -0.5]),\n            'a_U2': np.array([0.0, 0.6, 0.9]),\n        }\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3),\n            'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array([0.0, 0.5, -0.3]),\n            'delta_fd': np.array([0.0, 1.0, -0.8]),\n            'beta': np.array([0.0, 1.0, -0.5]),\n        }\n    else:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(K),\n            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),\n            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),\n        }\n        iv_beta = np.array(_BETA_POOL[:K]) * 0.5\n        iv_beta[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_beta,\n            'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),\n        }\n        fd_delta = np.array(_DELTA_POOL[:K])\n        fd_delta[0] = 0.0\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta_fd': fd_delta,\n            'beta': np.array(_BETA_POOL[:K]),\n        }\n    return params\n\n\ndef make_dgp_params_H0(K, params):\n    p0 = {}\n    for topo, p in params.items():\n        if topo == 'confounding':\n            p0[topo] = dict(p, beta_T=0.0)\n        elif topo == 'mediation':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'collider':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'exposure':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'mbias':\n            p0[topo] = dict(p, tau=0.0)\n        elif topo == 'iv':\n            p0[topo] = dict(p, beta=np.zeros(K))\n        elif topo == 'frontdoor':\n            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,\n                            delta_fd=np.zeros(K), beta=np.zeros(K))\n    return p0\n\n\n# ============================================================================\n# DGP Generators (general K)\n# ============================================================================\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]\n              + p['a_U2'][None, :] * U2[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]\n              + p['dU'][None, :] * U[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    M = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\nGEN_FNS = {\n    'confounding': gen_confounding, 'mediation': gen_mediation,\n    'collider': gen_collider, 'exposure': gen_exposure,\n    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,\n}\n\n\n# ============================================================================\n# Sufficient Statistics & Plim (general K)\n# ============================================================================\n\ndef precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):\n    rng = np.random.default_rng(seed)\n    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    if topology == 'iv':\n        Z = first_var\n        z1 = Z == 1; z0 = Z == 0\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n        return dict(RF=RF, FS=FS, topology='iv')\n    elif topology == 'exposure':\n        return dict(p_A=DA.mean(0), E_Y=Y.mean(),\n                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')\n    else:\n        T = first_var\n        return dict(\n            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),\n            E_Y=Y.mean(), E_TY=(T * Y).mean(),\n            E_TD=(DA * T[:, None]).mean(0),\n            E_YD=(DA * Y[:, None]).mean(0), topology=topology)\n\n\ndef compute_plim(C, st, K):\n    if st['topology'] == 'iv':\n        FS_star = C @ st['FS']\n        if abs(FS_star[1]) < 1e-8:\n            return np.nan\n        return st['RF'] / FS_star[1]\n    elif st['topology'] == 'exposure':\n        q = C @ st['p_A']\n        cy = C @ st['E_YD']\n        EZZ = np.zeros((K, K))\n        EZZ[0, 0] = 1.0\n        for j in range(1, K):\n            EZZ[0, j] = EZZ[j, 0] = q[j]\n            EZZ[j, j] = q[j]\n        EZY = np.zeros(K)\n        EZY[0] = st['E_Y']\n        for j in range(1, K):\n            EZY[j] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(K, np.nan)\n    else:\n        q = C @ st['p_A']\n        ct = C @ st['E_TD']\n        cy = C @ st['E_YD']\n        dim = K + 1\n        EZZ = np.zeros((dim, dim))\n        EZZ[0, 0] = 1.0\n        EZZ[0, 1] = EZZ[1, 0] = st['E_T']\n        EZZ[1, 1] = st['E_T2']\n        for j in range(1, K):\n            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]\n            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]\n            EZZ[j + 1, j + 1] = q[j]\n        EZY = np.zeros(dim)\n        EZY[0] = st['E_Y']\n        EZY[1] = st['E_TY']\n        for j in range(1, K):\n            EZY[j + 1] = cy[j]\n        try:\n            return np.linalg.solve(EZZ, EZY)\n        except np.linalg.LinAlgError:\n            return np.full(dim, np.nan)\n\n\ndef extract_tau(plim_result, topology):\n    if topology == 'iv':\n        return float(plim_result) if np.isfinite(plim_result) else np.nan\n    if isinstance(plim_result, np.ndarray):\n        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan\n    return np.nan\n\n\n# ============================================================================\n# 1. Data Loading & Confusion Matrix\n# ============================================================================\n\ndef load_annotations(data_dir, dataset, model, prompt):\n    path = os.path.join(data_dir, dataset, f\"{model}_{prompt}_annotations.jsonl\")\n    records = []\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line.strip())\n            records.append((int(rec['true_label']), int(rec['predicted_label'])))\n    return records\n\n\ndef build_confusion_matrix(records, K):\n    counts = np.zeros((K, K))\n    for true_k, pred_k in records:\n        if 0 <= true_k < K and 0 <= pred_k < K:\n            counts[pred_k, true_k] += 1\n    col_sums = counts.sum(axis=0)\n    col_sums = np.where(col_sums < 1, 1, col_sums)\n    return counts / col_sums\n\n\ndef load_all_confusion_matrices(data_dir):\n    matrices = {}\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        for model in MODELS:\n            for prompt in PROMPTS:\n                try:\n                    records = load_annotations(data_dir, dataset, model, prompt)\n                    C = build_confusion_matrix(records, K)\n                    matrices[(dataset, model, prompt)] = C\n                except FileNotFoundError:\n                    print(f\"  [WARN] Missing: {dataset}/{model}_{prompt}\")\n    return matrices\n\n\n# ============================================================================\n# 2. Downstream Causal Bias\n# ============================================================================\n\ndef compute_bias_for_topology(C, K, topology, st, tau_true):\n    plim_result = compute_plim(C, st, K)\n    tau_hat = extract_tau(plim_result, topology)\n    if np.isnan(tau_hat) or np.isnan(tau_true):\n        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}\n    bias = tau_hat - tau_true\n    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None\n    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)\n    return {\n        'tau_hat': float(tau_hat), 'bias': float(bias),\n        'bias_pct': float(bias_pct) if bias_pct is not None else None,\n        'sign_flip': sign_flip,\n    }\n\n\ndef compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            info = compute_bias_for_topology(C, K, topology, st, tau_true)\n            results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **info,\n            })\n    return results\n\n\n# ============================================================================\n# 3. ASV Computation\n# ============================================================================\n\ndef C_interpolated(C0, delta, K):\n    C_d = (1 - delta) * np.eye(K) + delta * C0\n    C_d = np.maximum(C_d, 0.0)\n    col_sums = C_d.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C_d / col_sums\n\n\ndef compute_delta_max(C0):\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - min_diag), 10.0)\n\n\ndef compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,\n                           n_grid=1500, se_ref=None):\n    dmax = compute_delta_max(C0)\n    deltas = np.linspace(0, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = C_interpolated(C0, d, K)\n        plim_result = compute_plim(C_d, st, K)\n        tau_curve[i] = extract_tau(plim_result, topology)\n\n    bias_abs = np.abs(tau_curve - tau_true)\n    envelope = np.zeros(n_grid)\n    running_max = 0.0\n    for i in range(n_grid):\n        if np.isfinite(bias_abs[i]):\n            running_max = max(running_max, bias_abs[i])\n        envelope[i] = running_max\n\n    if asv_type == 'sign_flip':\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'magnitude':\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = 0.1 * abs(tau_true)\n        for i in range(n_grid):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif asv_type == 'significance':\n        if se_ref is None or se_ref < 1e-12:\n            return None\n        for i in range(n_grid):\n            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:\n                return float(deltas[i])\n        return None\n    return None\n\n\ndef estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n    tau_hats = []\n    for _ in range(n_mc):\n        first_var, Y, A = gen_fn(K, N_ref, params, rng)\n        if topology == 'iv':\n            th, _ = wald_estimator(first_var, Y, A, k=1)\n        elif topology == 'exposure':\n            b, _ = ols_no_T(Y, A, K)\n            th = b[1]\n        else:\n            b, _ = ols_with_dummies(Y, first_var, A, K)\n            th = b[1]\n        if np.isfinite(th):\n            tau_hats.append(th)\n    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan\n\n\ndef compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):\n    results = []\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            se_ref = all_se_ref.get((K, topology))\n            for asv_type in ['magnitude', 'significance', 'sign_flip']:\n                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,\n                                             asv_type, se_ref=se_ref)\n                results.append({\n                    'dataset': dataset, 'model': model, 'prompt': prompt,\n                    'K': K, 'topology': topology, 'asv_type': asv_type,\n                    'asv': asv,\n                })\n    return results\n\n\n# ============================================================================\n# 4. F1 vs Downstream Bias\n# ============================================================================\n\ndef compute_f1_from_C(C, K, p_A=None):\n    if p_A is None:\n        p_A = np.ones(K) / K\n    precision = np.zeros(K)\n    recall = np.zeros(K)\n    f1 = np.zeros(K)\n    for i in range(K):\n        recall[i] = C[i, i]\n        denom = sum(C[i, j] * p_A[j] for j in range(K))\n        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0\n        if precision[i] + recall[i] > 1e-12:\n            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])\n    return {\n        'macro_f1': float(f1.mean()),\n        'weighted_f1': float((p_A * f1).sum()),\n        'per_class_f1': f1.tolist(),\n    }\n\n\ndef f1_vs_bias_analysis(confusion_matrices, biases):\n    results = []\n    for b in biases:\n        key = (b['dataset'], b['model'], b['prompt'])\n        if key not in confusion_matrices:\n            continue\n        C = confusion_matrices[key]\n        K = b['K']\n        p_A = make_p_A(K)\n        f1_info = compute_f1_from_C(C, K, p_A)\n        abs_bias = abs(b['bias']) if b['bias'] is not None else None\n        results.append({\n            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],\n            'K': K, 'topology': b['topology'],\n            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],\n            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],\n            'sign_flip': b['sign_flip'],\n        })\n    return results\n\n\n# ============================================================================\n# 5. Type I/II Error Rates\n# ============================================================================\n\ndef compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,\n                              st_H1, tau_true,\n                              n_sim=100, N_sample=5000, seed=42):\n    gen_fn = GEN_FNS[topology]\n    rng = np.random.default_rng(seed)\n\n    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')\n    asv_safe = (masv is None or masv > 1.0)\n\n    def _run_mc(params_t, n):\n        valid = 0; rej = 0\n        for _ in range(n):\n            fv, Y, A = gen_fn(K, N_sample, params_t, rng)\n            Astar = generate_Astar(A, C, rng)\n            if topology == 'iv':\n                th, se = wald_estimator(fv, Y, Astar, k=1)\n            elif topology == 'exposure':\n                b, svec = ols_no_T(Y, Astar, K)\n                th, se = b[1], svec[1]\n            else:\n                b, svec = ols_with_dummies(Y, fv, Astar, K)\n                th, se = b[1], svec[1]\n            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:\n                valid += 1\n                if abs(th / se) > 1.96:\n                    rej += 1\n        return rej / max(valid, 1), valid\n\n    type1_before, v0 = _run_mc(params_H0, n_sim)\n    power_before, v1 = _run_mc(params_H1, n_sim)\n    type1_after = type1_before if asv_safe else 0.0\n    power_after = power_before if asv_safe else 0.0\n\n    return {\n        'type1_before': float(type1_before), 'type1_after': float(type1_after),\n        'power_before': float(power_before), 'power_after': float(power_after),\n        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,\n        'valid_h0': int(v0), 'valid_h1': int(v1),\n    }\n\n\n# ============================================================================\n# 6. Inter-model Error Correlation\n# ============================================================================\n\ndef compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,\n                                    n_samples=1000, seed=42):\n    rng = np.random.default_rng(seed)\n    p_A = make_p_A(K)\n    true_labels = rng.choice(K, size=n_samples, p=p_A)\n\n    predictions = {}\n    for model in MODELS:\n        key = (dataset, model, prompt)\n        if key in confusion_matrices:\n            predictions[model] = generate_Astar(true_labels,\n                                                confusion_matrices[key], rng)\n        else:\n            predictions[model] = true_labels.copy()\n\n    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]\n    results = {}\n    for m1, m2 in pairs:\n        p1, p2 = predictions[m1], predictions[m2]\n        agreement = float((p1 == p2).mean())\n        observed = agreement\n        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))\n        kappa = float((observed - expected) / (1 - expected)\n                      ) if expected < 1 - 1e-10 else 0.0\n        err1 = (p1 != true_labels).astype(float)\n        err2 = (p2 != true_labels).astype(float)\n        if err1.std() > 1e-10 and err2.std() > 1e-10:\n            error_corr = float(np.corrcoef(err1, err2)[0, 1])\n        else:\n            error_corr = 0.0\n        results[f\"{m1}-{m2}\"] = {\n            'agreement': agreement,\n            'kappa': kappa,\n            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,\n        }\n    return results\n\n\n# ============================================================================\n# Mock Data Generation\n# ============================================================================\n\ndef generate_mock_C(K, rng, diag_range):\n    C = np.zeros((K, K))\n    for j in range(K):\n        diag_val = rng.uniform(diag_range[0], diag_range[1])\n        remaining = 1.0 - diag_val\n        if K > 2:\n            dists = np.abs(np.arange(K) - j).astype(float)\n            dists[j] = np.inf\n            weights = 1.0 / dists\n            weights[j] = 0\n            noise = rng.uniform(0.5, 1.5, K)\n            noise[j] = 0\n            weights = weights * noise\n            weights /= weights.sum()\n            C[:, j] = remaining * weights\n        else:\n            C[1 - j, j] = remaining\n        C[j, j] = diag_val\n    return C\n\n\ndef generate_mock_confusion_matrices(seed=12345):\n    rng = np.random.default_rng(seed)\n    matrices = {}\n    diag_ranges = {\n        'civil_comments': (0.85, 0.95),\n        'vast': (0.70, 0.90),\n        'humaid': (0.60, 0.85),\n    }\n    for dataset, info in DATASETS.items():\n        K = info['K']\n        dr = diag_ranges[dataset]\n        for model in MODELS:\n            for prompt in PROMPTS:\n                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)\n    return matrices\n\n\n# ============================================================================\n# Diagnostic Plots (optional)\n# ============================================================================\n\ndef save_f1_vs_bias_plot(f1_bias, output_dir):\n    if not HAS_MPL:\n        return\n    fig, axes = plt.subplots(2, 4, figsize=(20, 10))\n    axes = axes.flatten()\n    for idx, topo in enumerate(TOPOLOGIES):\n        ax = axes[idx]\n        subset = [r for r in f1_bias if r['topology'] == topo\n                  and r['abs_bias'] is not None]\n        if not subset:\n            ax.set_title(topo)\n            continue\n        f1s = [r['macro_f1'] for r in subset]\n        biases = [r['abs_bias'] for r in subset]\n        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]\n        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)\n        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)\n        ax.set_xlabel('Macro F1')\n        ax.set_ylabel('|bias|')\n        ax.set_title(topo)\n    if len(TOPOLOGIES) < 8:\n        axes[-1].axis('off')\n    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)\n    plt.close(fig)\n\n\ndef save_asv_heatmap(asvs, output_dir):\n    if not HAS_MPL:\n        return\n    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']\n    datasets_list = list(DATASETS.keys())\n    fig, axes = plt.subplots(1, 3, figsize=(18, 6))\n    for didx, dataset in enumerate(datasets_list):\n        ax = axes[didx]\n        subset = [r for r in mag_asvs if r['dataset'] == dataset]\n        configs = sorted(set((r['model'], r['prompt']) for r in subset))\n        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)\n        for r in subset:\n            ti = TOPOLOGIES.index(r['topology'])\n            ci = configs.index((r['model'], r['prompt']))\n            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan\n        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',\n                       vmin=0, vmax=2)\n        ax.set_xticks(range(len(configs)))\n        ax.set_xticklabels([f\"{m[:3]}_{p[:3]}\" for m, p in configs],\n                           rotation=45, ha='right', fontsize=7)\n        ax.set_yticks(range(len(TOPOLOGIES)))\n        ax.set_yticklabels(TOPOLOGIES, fontsize=8)\n        ax.set_title(f'{dataset} (K={DATASETS[dataset][\"K\"]})')\n        plt.colorbar(im, ax=ax, shrink=0.8)\n    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)\n    fig.tight_layout(rect=[0, 0, 1, 0.96])\n    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)\n    plt.close(fig)\n\n\n# ============================================================================\n# JSON Serialization\n# ============================================================================\n\ndef _to_json_safe(obj):\n    if isinstance(obj, np.integer):\n        return int(obj)\n    elif isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    elif isinstance(obj, np.ndarray):\n        return _to_json_safe(obj.tolist())\n    elif isinstance(obj, dict):\n        return {str(k): _to_json_safe(v) for k, v in obj.items()}\n    elif isinstance(obj, list):\n        return [_to_json_safe(v) for v in obj]\n    elif isinstance(obj, (bool, np.bool_)):\n        return bool(obj)\n    elif isinstance(obj, float):\n        return None if (np.isnan(obj) or np.isinf(obj)) else obj\n    return obj\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')\n    parser.add_argument('--data-dir', default='data/')\n    parser.add_argument('--output-dir', default='artifacts/plan006/')\n    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')\n    parser.add_argument('--n-sim', type=int, default=1000)\n    parser.add_argument('--device', type=str, default='cpu')\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    t_total = time.time()\n    n_precomp = 500_000 if args.mock else N_PRECOMP\n\n    print(\"=\" * 70)\n    print(\"plan_006: Empirical ASV Calibration\")\n    print(\"=\" * 70)\n\n    # --- 1. Confusion matrices ---\n    if args.mock:\n        print(\"\\n[1/6] Generating mock confusion matrices...\")\n        confusion_matrices = generate_mock_confusion_matrices()\n    else:\n        print(\"\\n[1/6] Loading confusion matrices...\")\n        confusion_matrices = load_all_confusion_matrices(args.data_dir)\n\n    print(f\"  {len(confusion_matrices)} matrices loaded\")\n    for (ds, m, p), C in list(confusion_matrices.items())[:3]:\n        K = DATASETS[ds]['K']\n        print(f\"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}\")\n\n    # --- 2. Precompute sufficient statistics ---\n    print(\"\\n[2/6] Precomputing sufficient statistics...\")\n    K_values = sorted(set(DATASETS[ds]['K'] for ds in DATASETS))\n    all_suff_stats = {}\n    all_tau_true = {}\n    all_params = {}\n    all_params_H0 = {}\n    all_se_ref = {}\n\n    for K in K_values:\n        params = make_dgp_params(K)\n        params_H0 = make_dgp_params_H0(K, params)\n        all_params[K] = params\n        all_params_H0[K] = params_H0\n        for topology in TOPOLOGIES:\n            seed = K * 1000 + abs(hash(topology)) % 1000\n            st = precompute_suff_stats(K, topology, params[topology],\n                                       N=n_precomp, seed=seed)\n            plim_I = compute_plim(np.eye(K), st, K)\n            tau_true = extract_tau(plim_I, topology)\n            all_suff_stats[(K, topology)] = st\n            all_tau_true[(K, topology)] = tau_true\n\n            se = estimate_reference_se(K, topology, params[topology],\n                                       N_ref=5000,\n                                       n_mc=min(args.n_sim, 30),\n                                       seed=seed + 500)\n            all_se_ref[(K, topology)] = se\n            se_s = f\"{se:.4f}\" if np.isfinite(se) else \"N/A\"\n            print(f\"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}\")\n\n    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)\n    n_sign_flips = sum(1 for b in biases if b['sign_flip'])\n    print(f\"  {len(biases)} bias values ({n_sign_flips} sign flips)\")\n\n    # --- 3. ASV ---\n    print(\"\\n[3/6] Computing ASV values...\")\n    t3 = time.time()\n    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,\n                            all_tau_true, all_se_ref)\n    print(f\"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)\")\n    for at in ['magnitude', 'sign_flip', 'significance']:\n        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]\n        if sub:\n            print(f\"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} \"\n                  f\"max={max(sub):.3f} ({len(sub)} non-None)\")\n\n    # --- 4. F1 vs bias ---\n    print(\"\\n[4/6] F1 vs bias analysis...\")\n    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)\n    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]\n    high_f1_high_bias = [r for r in total_high_f1\n                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]\n    if total_high_f1:\n        pct = len(high_f1_high_bias) / len(total_high_f1) * 100\n        print(f\"  Baumann check: F1>0.93 with |bias|>0.05: \"\n              f\"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%\")\n    # Sample rows\n    for r in f1_bias[:3]:\n        print(f\"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: \"\n              f\"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}\")\n\n    # --- 5. Type I/II ---\n    print(\"\\n[5/6] Type I/II error rates...\")\n    t5 = time.time()\n    type1_type2_results = []\n    n_configs = len(confusion_matrices) * len(TOPOLOGIES)\n    idx = 0\n    for (dataset, model, prompt), C in confusion_matrices.items():\n        K = DATASETS[dataset]['K']\n        for topology in TOPOLOGIES:\n            idx += 1\n            st = all_suff_stats[(K, topology)]\n            tau_true = all_tau_true[(K, topology)]\n            r = compute_type1_type2_for_C(\n                C, K, topology, all_params[K], all_params_H0[K],\n                st, tau_true,\n                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)\n            type1_type2_results.append({\n                'dataset': dataset, 'model': model, 'prompt': prompt,\n                'K': K, 'topology': topology, **r,\n            })\n            if idx % 50 == 0:\n                print(f\"    {idx}/{n_configs}...\")\n    print(f\"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)\")\n    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])\n    print(f\"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}\")\n\n    # --- 6. Inter-model correlation ---\n    print(\"\\n[6/6] Inter-model error correlation...\")\n    inter_model_results = {}\n    for dataset in DATASETS:\n        K = DATASETS[dataset]['K']\n        for prompt in PROMPTS:\n            r = compute_inter_model_correlation(\n                confusion_matrices, K, dataset, prompt,\n                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)\n            inter_model_results[f\"{dataset}_{prompt}\"] = r\n    print(f\"  {len(inter_model_results)} (dataset, prompt) pairs\")\n    for key, pairs in list(inter_model_results.items())[:2]:\n        for pair, vals in pairs.items():\n            print(f\"    {key} {pair}: agree={vals['agreement']:.3f} \"\n                  f\"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}\")\n\n    # --- Summary ---\n    summary = {\n        'f1_gt_093_total': len(total_high_f1),\n        'f1_gt_093_with_high_bias_pct': (\n            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),\n        'ppi_recommended_scenarios': unsafe,\n        'total_scenarios': len(type1_type2_results),\n        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,\n    }\n\n    # --- Save ---\n    output = _to_json_safe({\n        'confusion_matrices': {\n            f\"{ds}_{m}_{p}\": C.tolist()\n            for (ds, m, p), C in confusion_matrices.items()\n        },\n        'biases': biases,\n        'asvs': asvs,\n        'f1_vs_bias': f1_bias,\n        'type1_type2': type1_type2_results,\n        'inter_model_correlation': inter_model_results,\n        'summary': summary,\n    })\n\n    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_path}\")\n\n    # --- Plots ---\n    save_f1_vs_bias_plot(f1_bias, args.output_dir)\n    save_asv_heatmap(asvs, args.output_dir)\n    if HAS_MPL:\n        print(f\"Plots saved to {args.output_dir}\")\n\n    # --- Validation ---\n    with open(out_path) as f:\n        data = json.load(f)\n    n_null = str(data).count('null')\n    print(f\"\\nValidation: JSON has {n_null} null values \"\n          f\"(expected for NaN/None ASV entries)\")\n    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:\n        print(f\"  {section}: {len(data[section])} records\")\n\n    elapsed = time.time() - t_total\n    print(f\"\\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)\")\n    print(f\"\\nSummary:\")\n    print(f\"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%\")\n    print(f\"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/\"\n          f\"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 670,
        "oldLines": 8,
        "newStart": 670,
        "newLines": 8,
        "lines": [
          "                     rej += 1",
          "         return rej / max(valid, 1), valid",
          " ",
          "-    type1_before, v0 = _run_mc(params_H0, n_sim)",
          "-    power_before, v1 = _run_mc(params_H1, n_sim)",
          "+    type1_before, v0 = _run_mc(params_H0[topology], n_sim)",
          "+    power_before, v1 = _run_mc(params_H1[topology], n_sim)",
          "     type1_after = type1_before if asv_safe else 0.0",
          "     power_after = power_before if asv_safe else 0.0",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 71_

Now deploy to server via scp-style: write the file content to the server using ssh_execute with a heredoc. Given the file is ~1048 lines, I'll use base64 encoding to avoid heredoc escaping issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "8f8780a1-a1e4-49fa-98d0-20154db49f6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ghnt9SWStS4XXgnJ2WyCcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 45782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
      },
      "output_tokens": 2,
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

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_011dRAtHCedcRyz9Jdw3Ew8M`</summary>

```json
{
  "command": "base64 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py | wc -c",
  "description": "Check base64 size of script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5c5536ed-5f26-4ea7-b7a8-edbf89d989c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ghnt9SWStS4XXgnJ2WyCcZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 45782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
      },
      "output_tokens": 2,
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

_source line 73 · 2026-05-20T21:25:20.779Z_

<details><summary>↩ Tool result · `toolu_011dRAtHCedcRyz9Jdw3Ew8M`</summary>

```text
51724
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "f78753af-9254-4a80-878e-5ce87d39315c",
  "tool_use_result": {
    "stdout": "51724",
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

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_01UBNwtbec1eXYoRm9xqppbq`</summary>

```json
{
  "command": "base64 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "description": "Base64 encode the script for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b85618be-dd3e-4612-af38-48100f2c78d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hSEEHrytaoDQsmoDhRNmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 188,
      "cache_read_input_tokens": 46334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 188
      },
      "output_tokens": 72,
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

_source line 75 · 2026-05-20T21:25:23.810Z_

<details><summary>↩ Tool result · `toolu_01UBNwtbec1eXYoRm9xqppbq`</summary>

```text
&lt;persisted-output>
Output too large (50.5KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/fb66a23b-ab7a-49cf-9609-9cc0b887dde7/tool-results/b6kld4k1f.txt

Preview (first 2KB):
IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJy
YXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJp
Y2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMg
ZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBE
b3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNl
bnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAg
My4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0
aW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmlu
ZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFz
ZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6
IHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0
aWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczog
bnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIKCmlt
cG9ydCBudW1weSBhcyBucAppbXBvcnQganNvbgppbXBvcnQgYXJncGFyc2UKaW1wb3J0IG9zCmlt
cG9ydCB0aW1lCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0Cgp0cnk6CiAgICBp
bXBvcnQgbWF0cGxvdGxpYgogICAgbWF0cGxvdGxpYi51c2UoJ0FnZycpCiAgICBpbXBvcnQgbWF0
cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBIQVNfTVBMID0gVHJ1ZQpleGNlcHQgSW1wb3J0RXJy
b3I6CiAgICBIQVNfTVBMID0gRmFsc2UKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIENvbnN0YW50
cwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT0KCkRBVEFTRVRTID0gT3JkZXJlZERpY3QoWwogICAgKCdj
aXZpbF9jb21tZW50cycsIHsnSyc6IDJ9KSwKICAgICgndmFzdCcsIHsnSyc6IDN9KSwKICAgICgn
aHVtYWlkJywgeydLJzogMTB9KSwKXSkKCk1PREVMUyA9IFsnbGxhbWE0JywgJ3F3ZW4zJywgJ2Rl
ZXBzZWVrJ10KUFJPTVBUUyA9IFsnemVyby1zaG90JywgJ2Zldy1zaG90LTMnLCAnZmV3LXNob3Qt
NSddCgpUT1BPTE9HSUVTID0gWydjb25mb3VuZGluZycsICdtZWRpYXRpb24nLCAnY29sbGlkZXIn
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "0813a5c5-ca1f-4cc3-a531-e700819cdc1b",
  "tool_use_result": {
    "stdout": "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJy\nYXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJp\nY2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMg\nZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBE\nb3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNl\nbnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAg\nMy4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0\naW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmlu\nZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFz\nZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6\nIHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0\naWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczog\nbnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIKCmlt\ncG9ydCBudW1weSBhcyBucAppbXBvcnQganNvbgppbXBvcnQgYXJncGFyc2UKaW1wb3J0IG9zCmlt\ncG9ydCB0aW1lCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0Cgp0cnk6CiAgICBp\nbXBvcnQgbWF0cGxvdGxpYgogICAgbWF0cGxvdGxpYi51c2UoJ0FnZycpCiAgICBpbXBvcnQgbWF0\ncGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBIQVNfTVBMID0gVHJ1ZQpleGNlcHQgSW1wb3J0RXJy\nb3I6CiAgICBIQVNfTVBMID0gRmFsc2UKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIENvbnN0YW50\ncwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT0KCkRBVEFTRVRTID0gT3JkZXJlZERpY3QoWwogICAgKCdj\naXZpbF9jb21tZW50cycsIHsnSyc6IDJ9KSwKICAgICgndmFzdCcsIHsnSyc6IDN9KSwKICAgICgn\naHVtYWlkJywgeydLJzogMTB9KSwKXSkKCk1PREVMUyA9IFsnbGxhbWE0JywgJ3F3ZW4zJywgJ2Rl\nZXBzZWVrJ10KUFJPTVBUUyA9IFsnemVyby1zaG90JywgJ2Zldy1zaG90LTMnLCAnZmV3LXNob3Qt\nNSddCgpUT1BPTE9HSUVTID0gWydjb25mb3VuZGluZycsICdtZWRpYXRpb24nLCAnY29sbGlkZXIn\nLCAnZXhwb3N1cmUnLAogICAgICAgICAgICAgICdtYmlhcycsICdpdicsICdmcm9udGRvb3InXQoK\nTl9QUkVDT01QID0gMl8wMDBfMDAwCgojIFBhcmFtZXRlciBwb29scyDigJQgSz0zIHZhbHVlcyBt\nYXRjaCBwbGFuXzAwMS9wbGFuXzAwNQpfQUxQSEFfUE9PTCA9IFsxLjUsIC0xLjAsIDAuOCwgLTAu\nNSwgMS4yLCAtMC43LCAwLjksIC0wLjQsIDAuNl0KX0JFVEFfQV9QT09MID0gWzEuMCwgLTAuNSwg\nMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0JFVEFfUE9PTCA9IFswLjAs\nIDEuMCwgLTAuNSwgMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0dBTU1B\nX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAuMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1\nLCAwLjFdCl9ERUxUQV9QT09MID0gWzAuMCwgMC44LCAtMC42LCAwLjUsIC0wLjQsIDAuMywgLTAu\nMiwgMC4xNSwgLTAuMSwgMC4wNV0KX0RUX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAu\nMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1LCAwLjFdCl9EWV9QT09MID0gWzAuMCwgMC44LCAwLjYs\nIC0wLjUsIDAuNCwgLTAuMywgMC4yLCAwLjE1LCAtMC4xLCAwLjA1XQoKCiMgPT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PQojIFV0aWxpdHkgRnVuY3Rpb25zCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHNv\nZnRtYXhfcm93cyhsb2dpdHMpOgogICAgZSA9IG5wLmV4cChsb2dpdHMgLSBsb2dpdHMubWF4KGF4\naXM9MSwga2VlcGRpbXM9VHJ1ZSkpCiAgICByZXR1cm4gZSAvIGUuc3VtKGF4aXM9MSwga2VlcGRp\nbXM9VHJ1ZSkKCgpkZWYgc2FtcGxlX2NhdChwcm9icywgcm5nKToKICAgIGN1bSA9IG5wLmN1bXN1\nbShwcm9icywgYXhpcz0xKQogICAgdSA9IHJuZy51bmlmb3JtKHNpemU9cHJvYnMuc2hhcGVbMF0p\nWzosIE5vbmVdCiAgICByZXR1cm4gKHUgPj0gY3VtWzosIDotMV0pLnN1bShheGlzPTEpLmFzdHlw\nZShpbnQpCgoKZGVmIGdlbmVyYXRlX0FzdGFyKEEsIEMsIHJuZyk6CiAgICBwcm9icyA9IENbOiwg\nQV0KICAgIGN1bSA9IG5wLmN1bXN1bShwcm9icywgYXhpcz0wKQogICAgdSA9IHJuZy51bmlmb3Jt\nKHNpemU9bGVuKEEpKQogICAgcmV0dXJuICh1W05vbmUsIDpdID49IGN1bVs6LTFdKS5zdW0oYXhp\ncz0wKS5hc3R5cGUoaW50KQoKCmRlZiBvbHNfd2l0aF9kdW1taWVzKFksIFQsIEFzdGFyLCBLKToK\nICAgIE4gPSBsZW4oWSkKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGsgaW4g\ncmFuZ2UoMSwgSyk6CiAgICAgICAgRFs6LCBrIC0gMV0gPSAoQXN0YXIgPT0gaykuYXN0eXBlKGZs\nb2F0KQogICAgWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAub25lcyhOKSwgVCwgRF0pCiAgICB0cnk6\nCiAgICAgICAgYmV0YSA9IG5wLmxpbmFsZy5sc3RzcShYLCBZLCByY29uZD1Ob25lKVswXQogICAg\nICAgIHJlc2lkID0gWSAtIFggQCBiZXRhCiAgICAgICAgc2lnbWEyID0gbnAuc3VtKHJlc2lkKioy\nKSAvIG1heChOIC0gWC5zaGFwZVsxXSwgMSkKICAgICAgICBYdFhfaW52ID0gbnAubGluYWxnLmlu\ndihYLlQgQCBYKQogICAgICAgIHNlID0gbnAuc3FydChucC5tYXhpbXVtKHNpZ21hMiAqIG5wLmRp\nYWcoWHRYX2ludiksIDApKQogICAgZXhjZXB0IG5wLmxpbmFsZy5MaW5BbGdFcnJvcjoKICAgICAg\nICBiZXRhID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICAgICAgc2UgPSBucC5mdWxs\nKFguc2hhcGVbMV0sIG5wLm5hbikKICAgIHJldHVybiBiZXRhLCBzZQoKCmRlZiBvbHNfbm9fVChZ\nLCBBc3RhciwgSyk6CiAgICBOID0gbGVuKFkpCiAgICBEID0gbnAuemVyb3MoKE4sIEsgLSAxKSkK\nICAgIGZvciBrIGluIHJhbmdlKDEsIEspOgogICAgICAgIERbOiwgayAtIDFdID0gKEFzdGFyID09\nIGspLmFzdHlwZShmbG9hdCkKICAgIFggPSBucC5jb2x1bW5fc3RhY2soW25wLm9uZXMoTiksIERd\nKQogICAgdHJ5OgogICAgICAgIGJldGEgPSBucC5saW5hbGcubHN0c3EoWCwgWSwgcmNvbmQ9Tm9u\nZSlbMF0KICAgICAgICByZXNpZCA9IFkgLSBYIEAgYmV0YQogICAgICAgIHNpZ21hMiA9IG5wLnN1\nbShyZXNpZCoqMikgLyBtYXgoTiAtIFguc2hhcGVbMV0sIDEpCiAgICAgICAgWHRYX2ludiA9IG5w\nLmxpbmFsZy5pbnYoWC5UIEAgWCkKICAgICAgICBzZSA9IG5wLnNxcnQobnAubWF4aW11bShzaWdt\nYTIgKiBucC5kaWFnKFh0WF9pbnYpLCAwKSkKICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJy\nb3I6CiAgICAgICAgYmV0YSA9IG5wLmZ1bGwoWC5zaGFwZVsxXSwgbnAubmFuKQogICAgICAgIHNl\nID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICByZXR1cm4gYmV0YSwgc2UKCgpkZWYg\nd2FsZF9lc3RpbWF0b3IoWiwgWSwgQXN0YXIsIGs9MSk6CiAgICB6MSA9IFogPT0gMTsgejAgPSBa\nID09IDAKICAgIG4xLCBuMCA9IGZsb2F0KHoxLnN1bSgpKSwgZmxvYXQoejAuc3VtKCkpCiAgICBp\nZiBuMSA8IDIgb3IgbjAgPCAyOgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgUkYg\nPSBZW3oxXS5tZWFuKCkgLSBZW3owXS5tZWFuKCkKICAgIHZhcl9SRiA9IFlbejFdLnZhcigpIC8g\nbjEgKyBZW3owXS52YXIoKSAvIG4wCiAgICBEa196MSA9IChBc3Rhclt6MV0gPT0gaykuYXN0eXBl\nKGZsb2F0KS5tZWFuKCkKICAgIERrX3owID0gKEFzdGFyW3owXSA9PSBrKS5hc3R5cGUoZmxvYXQp\nLm1lYW4oKQogICAgRlMgPSBEa196MSAtIERrX3owCiAgICB2YXJfRlMgPSBEa196MSAqICgxIC0g\nRGtfejEpIC8gbjEgKyBEa196MCAqICgxIC0gRGtfejApIC8gbjAKICAgIGlmIGFicyhGUykgPCAx\nZS04OgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgVyA9IFJGIC8gRlMKICAgIHZh\ncl9XID0gdmFyX1JGIC8gRlMqKjIgKyBSRioqMiAqIHZhcl9GUyAvIEZTKio0CiAgICByZXR1cm4g\nVywgbnAuc3FydChtYXgodmFyX1csIDApKQoKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIERHUCBQ\nYXJhbWV0ZXJzIChnZW5lcmFsIEssIEs9MyBtYXRjaGVzIHBsYW5fMDAxL3BsYW5fMDA1KQojID09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT0KCmRlZiBtYWtlX3BfQShLKToKICAgIGlmIEsgPT0gMjoKICAgICAg\nICByZXR1cm4gbnAuYXJyYXkoWzAuNTUsIDAuNDVdKQogICAgZWxpZiBLID09IDM6CiAgICAgICAg\ncmV0dXJuIG5wLmFycmF5KFswLjQwLCAwLjM1LCAwLjI1XSkKICAgIGVsc2U6CiAgICAgICAgcmF3\nID0gbnAuYXJyYXkoWzEuMCAvIChpICsgMSkgZm9yIGkgaW4gcmFuZ2UoSyldKQogICAgICAgIHJl\ndHVybiByYXcgLyByYXcuc3VtKCkKCgpkZWYgbWFrZV9kZ3BfcGFyYW1zKEspOgogICAgcF9BID0g\nbWFrZV9wX0EoSykKICAgIHBhcmFtcyA9IHsKICAgICAgICAnY29uZm91bmRpbmcnOiB7CiAgICAg\nICAgICAgICdwX0EnOiBwX0EsCiAgICAgICAgICAgICdhbHBoYSc6IG5wLmFycmF5KF9BTFBIQV9Q\nT09MWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9BJzogbnAuYXJyYXkoX0JFVEFfQV9QT09M\nWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9UJzogMi4wLAogICAgICAgICAgICAnc2lnbWFf\nVCc6IDEuMCwKICAgICAgICB9LAogICAgICAgICdtZWRpYXRpb24nOiB7CiAgICAgICAgICAgICd0\nYXUnOiAwLjUsCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSks\nCiAgICAgICAgICAgICdkZWx0YSc6IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSksCiAgICAgICAg\nICAgICdiZXRhJzogbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAg\nJ2NvbGxpZGVyJzogewogICAgICAgICAgICAndGF1JzogMS4wLAogICAgICAgICAgICAnZyc6IG5w\nLnplcm9zKEspLAogICAgICAgICAgICAnZFQnOiBucC5hcnJheShfRFRfUE9PTFs6S10pLAogICAg\nICAgICAgICAnZFknOiBucC5hcnJheShfRFlfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAg\nJ2V4cG9zdXJlJzogewogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktd\nKSwKICAgICAgICAgICAgJ3BfQSc6IHBfQSwKICAgICAgICB9LAogICAgfQogICAgaWYgSyA9PSAz\nOgogICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2Rl\nbHRhX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoMyks\nCiAgICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMCwgMC44LCAtMC41XSksCiAgICAgICAg\nICAgICdhX1UyJzogbnAuYXJyYXkoWzAuMCwgMC42LCAwLjldKSwKICAgICAgICB9CiAgICAgICAg\ncGFyYW1zWydpdiddID0gewogICAgICAgICAgICAnbGFtJzogMS4wLCAnYmV0YSc6IG5wLmFycmF5\nKFswLjAsIDAuNSwgLTAuMjVdKSwKICAgICAgICAgICAgJ2cnOiBucC56ZXJvcygzKSwKICAgICAg\nICAgICAgJ2RaJzogbnAuYXJyYXkoWzAuMCwgMS4wLCAtMC41XSksCiAgICAgICAgICAgICdkVSc6\nIG5wLmFycmF5KFswLjAsIDAuOCwgMC42XSksCiAgICAgICAgfQogICAgICAgIHBhcmFtc1snZnJv\nbnRkb29yJ10gPSB7CiAgICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAs\nCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KFswLjAsIDAuNSwgLTAuM10pLAogICAgICAg\nICAgICAnZGVsdGFfZmQnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjhdKSwKICAgICAgICAgICAg\nJ2JldGEnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjVdKSwKICAgICAgICB9CiAgICBlbHNlOgog\nICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2RlbHRh\nX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoSyksCiAg\nICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMF0gKyBbX0FMUEhBX1BPT0xbaV0gKiAwLjYg\nZm9yIGkgaW4gcmFuZ2UoSyAtIDEpXSksCiAgICAgICAgICAgICdhX1UyJzogbnAuYXJyYXkoWzAu\nMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC44IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAogICAg\nICAgIH0KICAgICAgICBpdl9iZXRhID0gbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pICogMC41CiAg\nICAgICAgaXZfYmV0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snaXYnXSA9IHsKICAgICAgICAg\nICAgJ2xhbSc6IDEuMCwgJ2JldGEnOiBpdl9iZXRhLAogICAgICAgICAgICAnZyc6IG5wLnplcm9z\nKEspLAogICAgICAgICAgICAnZFonOiBucC5hcnJheShbMC4wXSArIFtfQUxQSEFfUE9PTFtpXSAq\nIDAuNyBmb3IgaSBpbiByYW5nZShLIC0gMSldKSwKICAgICAgICAgICAgJ2RVJzogbnAuYXJyYXko\nWzAuMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC42IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAog\nICAgICAgIH0KICAgICAgICBmZF9kZWx0YSA9IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSkKICAg\nICAgICBmZF9kZWx0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snZnJvbnRkb29yJ10gPSB7CiAg\nICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAsCiAgICAgICAgICAgICdn\nYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSksCiAgICAgICAgICAgICdkZWx0YV9mZCc6\nIGZkX2RlbHRhLAogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktdKSwK\nICAgICAgICB9CiAgICByZXR1cm4gcGFyYW1zCgoKZGVmIG1ha2VfZGdwX3BhcmFtc19IMChLLCBw\nYXJhbXMpOgogICAgcDAgPSB7fQogICAgZm9yIHRvcG8sIHAgaW4gcGFyYW1zLml0ZW1zKCk6CiAg\nICAgICAgaWYgdG9wbyA9PSAnY29uZm91bmRpbmcnOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRp\nY3QocCwgYmV0YV9UPTAuMCkKICAgICAgICBlbGlmIHRvcG8gPT0gJ21lZGlhdGlvbic6CiAgICAg\nICAgICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAn\nY29sbGlkZXInOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgdGF1PTAuMCkKICAgICAg\nICBlbGlmIHRvcG8gPT0gJ2V4cG9zdXJlJzoKICAgICAgICAgICAgcDBbdG9wb10gPSBkaWN0KHAs\nIGJldGE9bnAuemVyb3MoSykpCiAgICAgICAgZWxpZiB0b3BvID09ICdtYmlhcyc6CiAgICAgICAg\nICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAnaXYn\nOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgYmV0YT1ucC56ZXJvcyhLKSkKICAgICAg\nICBlbGlmIHRvcG8gPT0gJ2Zyb250ZG9vcic6CiAgICAgICAgICAgIHAwW3RvcG9dID0gZGljdChw\nLCBsYW1iZGFfVT0wLjAsIGFscGhhX1U9MC4wLAogICAgICAgICAgICAgICAgICAgICAgICAgICAg\nZGVsdGFfZmQ9bnAuemVyb3MoSyksIGJldGE9bnAuemVyb3MoSykpCiAgICByZXR1cm4gcDAKCgoj\nID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT0KIyBER1AgR2VuZXJhdG9ycyAoZ2VuZXJhbCBLKQojID09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT0KCmRlZiBnZW5fY29uZm91bmRpbmcoSywgTiwgcCwgcm5nKToKICAgIEEg\nPSBybmcuY2hvaWNlKEssIHNpemU9TiwgcD1wWydwX0EnXSkKICAgIEQgPSBucC56ZXJvcygoTiwg\nSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9\nPSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAgVCA9IEQgQCBwWydhbHBoYSddICsgcm5nLm5vcm1h\nbCgwLCBwWydzaWdtYV9UJ10sIE4pCiAgICBZID0gcFsnYmV0YV9UJ10gKiBUICsgRCBAIHBbJ2Jl\ndGFfQSddICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFksIEEKCgpkZWYgZ2Vu\nX21lZGlhdGlvbihLLCBOLCBwLCBybmcpOgogICAgVCA9IHJuZy5iaW5vbWlhbCgxLCAwLjUsIE4p\nLmFzdHlwZShmbG9hdCkKICAgIGxvZ2l0cyA9IHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0\nYSddW05vbmUsIDpdICogVFs6LCBOb25lXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRz\nKQogICAgQSA9IHNhbXBsZV9jYXQocHJvYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAt\nIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9PSBq\nICsgMSkuYXN0eXBlKGZsb2F0KQogICAgWSA9IHBbJ2JldGEnXVswXSArIEQgQCBwWydiZXRhJ11b\nMTpdICsgcFsndGF1J10gKiBUICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFks\nIEEKCgpkZWYgZ2VuX2NvbGxpZGVyKEssIE4sIHAsIHJuZyk6CiAgICBUID0gcm5nLm5vcm1hbCgw\nLCAxLCBOKQogICAgWSA9IHBbJ3RhdSddICogVCArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxv\nZ2l0cyA9IChwWydnJ11bTm9uZSwgOl0gKyBwWydkVCddW05vbmUsIDpdICogVFs6LCBOb25lXQog\nICAgICAgICAgICAgICsgcFsnZFknXVtOb25lLCA6XSAqIFlbOiwgTm9uZV0pCiAgICBwcm9icyA9\nIHNvZnRtYXhfcm93cyhsb2dpdHMpCiAgICBBID0gc2FtcGxlX2NhdChwcm9icywgcm5nKQogICAg\ncmV0dXJuIFQsIFksIEEKCgpkZWYgZ2VuX2V4cG9zdXJlKEssIE4sIHAsIHJuZyk6CiAgICBBID0g\ncm5nLmNob2ljZShLLCBzaXplPU4sIHA9cFsncF9BJ10pCiAgICBEID0gbnAuemVyb3MoKE4sIEsg\nLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEgPT0g\naiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBwWydiZXRhJ11bMF0gKyBEIEAgcFsnYmV0YSdd\nWzE6XSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBOb25lLCBZLCBBCgoKZGVmIGdl\nbl9tYmlhcyhLLCBOLCBwLCBybmcpOgogICAgVTEgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAgICBV\nMiA9IHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIFQgPSBwWydkZWx0YV9jb2VmJ10gKiBVMSArIHJu\nZy5ub3JtYWwoMCwgMSwgTikKICAgIFkgPSBwWyd0YXUnXSAqIFQgKyBwWydsYW0nXSAqIFUyICsg\ncm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtOb25lLCA6XSArIHBbJ2Ff\nVTEnXVtOb25lLCA6XSAqIFUxWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBwWydhX1UyJ11bTm9u\nZSwgOl0gKiBVMls6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxvZ2l0cykKICAg\nIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICByZXR1cm4gVCwgWSwgQQoKCmRlZiBnZW5f\naXYoSywgTiwgcCwgcm5nKToKICAgIFogPSBybmcuYmlub21pYWwoMSwgMC41LCBOKS5hc3R5cGUo\nZmxvYXQpCiAgICBVID0gcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtO\nb25lLCA6XSArIHBbJ2RaJ11bTm9uZSwgOl0gKiBaWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBw\nWydkVSddW05vbmUsIDpdICogVVs6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxv\nZ2l0cykKICAgIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICBEID0gbnAuemVyb3MoKE4s\nIEsgLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEg\nPT0gaiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBEIEAgcFsnYmV0YSddWzE6XSArIHBbJ2xh\nbSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBaLCBZLCBBCgoKZGVmIGdl\nbl9mcm9udGRvb3IoSywgTiwgcCwgcm5nKToKICAgIFUgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAg\nICBUID0gcFsnYWxwaGFfVSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxvZ2l0cyA9\nIHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0YV9mZCddW05vbmUsIDpdICogVFs6LCBOb25l\nXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRzKQogICAgTSA9IHNhbXBsZV9jYXQocHJv\nYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2Uo\nSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoTSA9PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAg\nWSA9IEQgQCBwWydiZXRhJ11bMTpdICsgcFsnbGFtYmRhX1UnXSAqIFUgKyBybmcubm9ybWFsKDAs\nIDEsIE4pCiAgICByZXR1cm4gVCwgWSwgTQoKCkdFTl9GTlMgPSB7CiAgICAnY29uZm91bmRpbmcn\nOiBnZW5fY29uZm91bmRpbmcsICdtZWRpYXRpb24nOiBnZW5fbWVkaWF0aW9uLAogICAgJ2NvbGxp\nZGVyJzogZ2VuX2NvbGxpZGVyLCAnZXhwb3N1cmUnOiBnZW5fZXhwb3N1cmUsCiAgICAnbWJpYXMn\nOiBnZW5fbWJpYXMsICdpdic6IGdlbl9pdiwgJ2Zyb250ZG9vcic6IGdlbl9mcm9udGRvb3IsCn0K\nCgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT0KIyBTdWZmaWNpZW50IFN0YXRpc3RpY3MgJiBQbGltIChn\nZW5lcmFsIEspCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHByZWNvbXB1dGVfc3VmZl9zdGF0\ncyhLLCB0b3BvbG9neSwgcGFyYW1zLCBOPU5fUFJFQ09NUCwgc2VlZD00Mik6CiAgICBybmcgPSBu\ncC5yYW5kb20uZGVmYXVsdF9ybmcoc2VlZCkKICAgIGZpcnN0X3ZhciwgWSwgQSA9IEdFTl9GTlNb\ndG9wb2xvZ3ldKEssIE4sIHBhcmFtcywgcm5nKQogICAgREEgPSBucC56ZXJvcygoTiwgSykpCiAg\nICBmb3IgayBpbiByYW5nZShLKToKICAgICAgICBEQVs6LCBrXSA9IChBID09IGspLmFzdHlwZShm\nbG9hdCkKCiAgICBpZiB0b3BvbG9neSA9PSAnaXYnOgogICAgICAgIFogPSBmaXJzdF92YXIKICAg\nICAgICB6MSA9IFogPT0gMTsgejAgPSBaID09IDAKICAgICAgICBSRiA9IFlbejFdLm1lYW4oKSAt\nIFlbejBdLm1lYW4oKQogICAgICAgIEZTID0gbnAuemVyb3MoSykKICAgICAgICBmb3IgayBpbiBy\nYW5nZShLKToKICAgICAgICAgICAgRlNba10gPSAoQVt6MV0gPT0gaykubWVhbigpIC0gKEFbejBd\nID09IGspLm1lYW4oKQogICAgICAgIHJldHVybiBkaWN0KFJGPVJGLCBGUz1GUywgdG9wb2xvZ3k9\nJ2l2JykKICAgIGVsaWYgdG9wb2xvZ3kgPT0gJ2V4cG9zdXJlJzoKICAgICAgICByZXR1cm4gZGlj\ndChwX0E9REEubWVhbigwKSwgRV9ZPVkubWVhbigpLAogICAgICAgICAgICAgICAgICAgIEVfWUQ9\nKERBICogWVs6LCBOb25lXSkubWVhbigwKSwgdG9wb2xvZ3k9J2V4cG9zdXJlJykKICAgIGVsc2U6\nCiAgICAgICAgVCA9IGZpcnN0X3ZhcgogICAgICAgIHJldHVybiBkaWN0KAogICAgICAgICAgICBw\nX0E9REEubWVhbigwKSwgRV9UPVQubWVhbigpLCBFX1QyPShUKioyKS5tZWFuKCksCiAgICAgICAg\nICAgIEVfWT1ZLm1lYW4oKSwgRV9UWT0oVCAqIFkpLm1lYW4oKSwKICAgICAgICAgICAgRV9URD0o\nREEgKiBUWzosIE5vbmVdKS5tZWFuKDApLAogICAgICAgICAgICBFX1lEPShEQSAqIFlbOiwgTm9u\nZV0pLm1lYW4oMCksIHRvcG9sb2d5PXRvcG9sb2d5KQoKCmRlZiBjb21wdXRlX3BsaW0oQywgc3Qs\nIEspOgogICAgaWYgc3RbJ3RvcG9sb2d5J10gPT0gJ2l2JzoKICAgICAgICBGU19zdGFyID0gQyBA\nIHN0WydGUyddCiAgICAgICAgaWYgYWJzKEZTX3N0YXJbMV0pIDwgMWUtODoKICAgICAgICAgICAg\ncmV0dXJuIG5wLm5hbgogICAgICAgIHJldHVybiBzdFsnUkYnXSAvIEZTX3N0YXJbMV0KICAgIGVs\naWYgc3RbJ3RvcG9sb2d5J10gPT0gJ2V4cG9zdXJlJzoKICAgICAgICBxID0gQyBAIHN0WydwX0En\nXQogICAgICAgIGN5ID0gQyBAIHN0WydFX1lEJ10KICAgICAgICBFWlogPSBucC56ZXJvcygoSywg\nSykpCiAgICAgICAgRVpaWzAsIDBdID0gMS4wCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6\nCiAgICAgICAgICAgIEVaWlswLCBqXSA9IEVaWltqLCAwXSA9IHFbal0KICAgICAgICAgICAgRVpa\nW2osIGpdID0gcVtqXQogICAgICAgIEVaWSA9IG5wLnplcm9zKEspCiAgICAgICAgRVpZWzBdID0g\nc3RbJ0VfWSddCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWVtq\nXSA9IGN5W2pdCiAgICAgICAgdHJ5OgogICAgICAgICAgICByZXR1cm4gbnAubGluYWxnLnNvbHZl\nKEVaWiwgRVpZKQogICAgICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJyb3I6CiAgICAgICAg\nICAgIHJldHVybiBucC5mdWxsKEssIG5wLm5hbikKICAgIGVsc2U6CiAgICAgICAgcSA9IEMgQCBz\ndFsncF9BJ10KICAgICAgICBjdCA9IEMgQCBzdFsnRV9URCddCiAgICAgICAgY3kgPSBDIEAgc3Rb\nJ0VfWUQnXQogICAgICAgIGRpbSA9IEsgKyAxCiAgICAgICAgRVpaID0gbnAuemVyb3MoKGRpbSwg\nZGltKSkKICAgICAgICBFWlpbMCwgMF0gPSAxLjAKICAgICAgICBFWlpbMCwgMV0gPSBFWlpbMSwg\nMF0gPSBzdFsnRV9UJ10KICAgICAgICBFWlpbMSwgMV0gPSBzdFsnRV9UMiddCiAgICAgICAgZm9y\nIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWlswLCBqICsgMV0gPSBFWlpbaiArIDEs\nIDBdID0gcVtqXQogICAgICAgICAgICBFWlpbMSwgaiArIDFdID0gRVpaW2ogKyAxLCAxXSA9IGN0\nW2pdCiAgICAgICAgICAgIEVaWltqICsgMSwgaiArIDFdID0gcVtqXQogICAgICAgIEVaWSA9IG5w\nLnplcm9zKGRpbSkKICAgICAgICBFWllbMF0gPSBzdFsnRV9ZJ10KICAgICAgICBFWllbMV0gPSBz\ndFsnRV9UWSddCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWVtq\nICsgMV0gPSBjeVtqXQogICAgICAgIHRyeToKICAgICAgICAgICAgcmV0dXJuIG5wLmxpbmFsZy5z\nb2x2ZShFWlosIEVaWSkKICAgICAgICBleGNlcHQgbnAubGluYWxnLkxpbkFsZ0Vycm9yOgogICAg\nICAgICAgICByZXR1cm4gbnAuZnVsbChkaW0sIG5wLm5hbikKCgpkZWYgZXh0cmFjdF90YXUocGxp\nbV9yZXN1bHQsIHRvcG9sb2d5KToKICAgIGlmIHRvcG9sb2d5ID09ICdpdic6CiAgICAgICAgcmV0\ndXJuIGZsb2F0KHBsaW1fcmVzdWx0KSBpZiBucC5pc2Zpbml0ZShwbGltX3Jlc3VsdCkgZWxzZSBu\ncC5uYW4KICAgIGlmIGlzaW5zdGFuY2UocGxpbV9yZXN1bHQsIG5wLm5kYXJyYXkpOgogICAgICAg\nIHJldHVybiBmbG9hdChwbGltX3Jlc3VsdFsxXSkgaWYgbnAuaXNmaW5pdGUocGxpbV9yZXN1bHRb\nMV0pIGVsc2UgbnAubmFuCiAgICByZXR1cm4gbnAubmFuCgoKIyA9PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nCiMgMS4gRGF0YSBMb2FkaW5nICYgQ29uZnVzaW9uIE1hdHJpeAojID09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT0KCmRlZiBsb2FkX2Fubm90YXRpb25zKGRhdGFfZGlyLCBkYXRhc2V0LCBtb2RlbCwgcHJvbXB0\nKToKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZGF0YV9kaXIsIGRhdGFzZXQsIGYie21vZGVsfV97\ncHJvbXB0fV9hbm5vdGF0aW9ucy5qc29ubCIpCiAgICByZWNvcmRzID0gW10KICAgIHdpdGggb3Bl\nbihwYXRoKSBhcyBmOgogICAgICAgIGZvciBsaW5lIGluIGY6CiAgICAgICAgICAgIHJlYyA9IGpz\nb24ubG9hZHMobGluZS5zdHJpcCgpKQogICAgICAgICAgICByZWNvcmRzLmFwcGVuZCgoaW50KHJl\nY1sndHJ1ZV9sYWJlbCddKSwgaW50KHJlY1sncHJlZGljdGVkX2xhYmVsJ10pKSkKICAgIHJldHVy\nbiByZWNvcmRzCgoKZGVmIGJ1aWxkX2NvbmZ1c2lvbl9tYXRyaXgocmVjb3JkcywgSyk6CiAgICBj\nb3VudHMgPSBucC56ZXJvcygoSywgSykpCiAgICBmb3IgdHJ1ZV9rLCBwcmVkX2sgaW4gcmVjb3Jk\nczoKICAgICAgICBpZiAwIDw9IHRydWVfayA8IEsgYW5kIDAgPD0gcHJlZF9rIDwgSzoKICAgICAg\nICAgICAgY291bnRzW3ByZWRfaywgdHJ1ZV9rXSArPSAxCiAgICBjb2xfc3VtcyA9IGNvdW50cy5z\ndW0oYXhpcz0wKQogICAgY29sX3N1bXMgPSBucC53aGVyZShjb2xfc3VtcyA8IDEsIDEsIGNvbF9z\ndW1zKQogICAgcmV0dXJuIGNvdW50cyAvIGNvbF9zdW1zCgoKZGVmIGxvYWRfYWxsX2NvbmZ1c2lv\nbl9tYXRyaWNlcyhkYXRhX2Rpcik6CiAgICBtYXRyaWNlcyA9IHt9CiAgICBmb3IgZGF0YXNldCwg\naW5mbyBpbiBEQVRBU0VUUy5pdGVtcygpOgogICAgICAgIEsgPSBpbmZvWydLJ10KICAgICAgICBm\nb3IgbW9kZWwgaW4gTU9ERUxTOgogICAgICAgICAgICBmb3IgcHJvbXB0IGluIFBST01QVFM6CiAg\nICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgcmVjb3JkcyA9IGxvYWRfYW5u\nb3RhdGlvbnMoZGF0YV9kaXIsIGRhdGFzZXQsIG1vZGVsLCBwcm9tcHQpCiAgICAgICAgICAgICAg\nICAgICAgQyA9IGJ1aWxkX2NvbmZ1c2lvbl9tYXRyaXgocmVjb3JkcywgSykKICAgICAgICAgICAg\nICAgICAgICBtYXRyaWNlc1soZGF0YXNldCwgbW9kZWwsIHByb21wdCldID0gQwogICAgICAgICAg\nICAgICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOgogICAgICAgICAgICAgICAgICAgIHByaW50\nKGYiICBbV0FSTl0gTWlzc2luZzoge2RhdGFzZXR9L3ttb2RlbH1fe3Byb21wdH0iKQogICAgcmV0\ndXJuIG1hdHJpY2VzCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgMi4gRG93bnN0cmVhbSBDYXVz\nYWwgQmlhcwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KCmRlZiBjb21wdXRlX2JpYXNfZm9yX3RvcG9s\nb2d5KEMsIEssIHRvcG9sb2d5LCBzdCwgdGF1X3RydWUpOgogICAgcGxpbV9yZXN1bHQgPSBjb21w\ndXRlX3BsaW0oQywgc3QsIEspCiAgICB0YXVfaGF0ID0gZXh0cmFjdF90YXUocGxpbV9yZXN1bHQs\nIHRvcG9sb2d5KQogICAgaWYgbnAuaXNuYW4odGF1X2hhdCkgb3IgbnAuaXNuYW4odGF1X3RydWUp\nOgogICAgICAgIHJldHVybiB7J3RhdV9oYXQnOiBOb25lLCAnYmlhcyc6IE5vbmUsICdiaWFzX3Bj\ndCc6IE5vbmUsICdzaWduX2ZsaXAnOiBGYWxzZX0KICAgIGJpYXMgPSB0YXVfaGF0IC0gdGF1X3Ry\ndWUKICAgIGJpYXNfcGN0ID0gYWJzKGJpYXMpIC8gYWJzKHRhdV90cnVlKSBpZiBhYnModGF1X3Ry\ndWUpID4gMWUtMTIgZWxzZSBOb25lCiAgICBzaWduX2ZsaXAgPSBib29sKG5wLnNpZ24odGF1X2hh\ndCkgIT0gbnAuc2lnbih0YXVfdHJ1ZSkgYW5kIGFicyh0YXVfdHJ1ZSkgPiAxZS0xMikKICAgIHJl\ndHVybiB7CiAgICAgICAgJ3RhdV9oYXQnOiBmbG9hdCh0YXVfaGF0KSwgJ2JpYXMnOiBmbG9hdChi\naWFzKSwKICAgICAgICAnYmlhc19wY3QnOiBmbG9hdChiaWFzX3BjdCkgaWYgYmlhc19wY3QgaXMg\nbm90IE5vbmUgZWxzZSBOb25lLAogICAgICAgICdzaWduX2ZsaXAnOiBzaWduX2ZsaXAsCiAgICB9\nCgoKZGVmIGNvbXB1dGVfYWxsX2JpYXNlcyhjb25mdXNpb25fbWF0cmljZXMsIGFsbF9zdWZmX3N0\nYXRzLCBhbGxfdGF1X3RydWUpOgogICAgcmVzdWx0cyA9IFtdCiAgICBmb3IgKGRhdGFzZXQsIG1v\nZGVsLCBwcm9tcHQpLCBDIGluIGNvbmZ1c2lvbl9tYXRyaWNlcy5pdGVtcygpOgogICAgICAgIEsg\nPSBEQVRBU0VUU1tkYXRhc2V0XVsnSyddCiAgICAgICAgZm9yIHRvcG9sb2d5IGluIFRPUE9MT0dJ\nRVM6CiAgICAgICAgICAgIHN0ID0gYWxsX3N1ZmZfc3RhdHNbKEssIHRvcG9sb2d5KV0KICAgICAg\nICAgICAgdGF1X3RydWUgPSBhbGxfdGF1X3RydWVbKEssIHRvcG9sb2d5KV0KICAgICAgICAgICAg\naW5mbyA9IGNvbXB1dGVfYmlhc19mb3JfdG9wb2xvZ3koQywgSywgdG9wb2xvZ3ksIHN0LCB0YXVf\ndHJ1ZSkKICAgICAgICAgICAgcmVzdWx0cy5hcHBlbmQoewogICAgICAgICAgICAgICAgJ2RhdGFz\nZXQnOiBkYXRhc2V0LCAnbW9kZWwnOiBtb2RlbCwgJ3Byb21wdCc6IHByb21wdCwKICAgICAgICAg\nICAgICAgICdLJzogSywgJ3RvcG9sb2d5JzogdG9wb2xvZ3ksICoqaW5mbywKICAgICAgICAgICAg\nfSkKICAgIHJldHVybiByZXN1bHRzCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgMy4gQVNWIENv\nbXB1dGF0aW9uCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIENfaW50ZXJwb2xhdGVkKEMwLCBk\nZWx0YSwgSyk6CiAgICBDX2QgPSAoMSAtIGRlbHRhKSAqIG5wLmV5ZShLKSArIGRlbHRhICogQzAK\nICAgIENfZCA9IG5wLm1heGltdW0oQ19kLCAwLjApCiAgICBjb2xfc3VtcyA9IENfZC5zdW0oYXhp\ncz0wKQogICAgY29sX3N1bXMgPSBucC53aGVyZShjb2xfc3VtcyA8IDFlLTEwLCAxLjAsIGNvbF9z\ndW1zKQogICAgcmV0dXJuIENfZCAvIGNvbF9zdW1zCgoKZGVmIGNvbXB1dGVfZGVsdGFfbWF4KEMw\nKToKICAgIG1pbl9kaWFnID0gbnAuZGlhZyhDMCkubWluKCkKICAgIGlmIG1pbl9kaWFnID49IDEu\nMDoKICAgICAgICByZXR1cm4gMTAuMAogICAgcmV0dXJuIG1pbigxLjAgLyAoMS4wIC0gbWluX2Rp\nYWcpLCAxMC4wKQoKCmRlZiBjb21wdXRlX2Fzdl9mb3JfbWF0cml4KEMwLCBLLCB0b3BvbG9neSwg\nc3QsIHRhdV90cnVlLCBhc3ZfdHlwZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgbl9ncmlk\nPTE1MDAsIHNlX3JlZj1Ob25lKToKICAgIGRtYXggPSBjb21wdXRlX2RlbHRhX21heChDMCkKICAg\nIGRlbHRhcyA9IG5wLmxpbnNwYWNlKDAsIGRtYXgsIG5fZ3JpZCkKICAgIHRhdV9jdXJ2ZSA9IG5w\nLnplcm9zKG5fZ3JpZCkKICAgIGZvciBpLCBkIGluIGVudW1lcmF0ZShkZWx0YXMpOgogICAgICAg\nIENfZCA9IENfaW50ZXJwb2xhdGVkKEMwLCBkLCBLKQogICAgICAgIHBsaW1fcmVzdWx0ID0gY29t\ncHV0ZV9wbGltKENfZCwgc3QsIEspCiAgICAgICAgdGF1X2N1cnZlW2ldID0gZXh0cmFjdF90YXUo\ncGxpbV9yZXN1bHQsIHRvcG9sb2d5KQoKICAgIGJpYXNfYWJzID0gbnAuYWJzKHRhdV9jdXJ2ZSAt\nIHRhdV90cnVlKQogICAgZW52ZWxvcGUgPSBucC56ZXJvcyhuX2dyaWQpCiAgICBydW5uaW5nX21h\neCA9IDAuMAogICAgZm9yIGkgaW4gcmFuZ2Uobl9ncmlkKToKICAgICAgICBpZiBucC5pc2Zpbml0\nZShiaWFzX2Fic1tpXSk6CiAgICAgICAgICAgIHJ1bm5pbmdfbWF4ID0gbWF4KHJ1bm5pbmdfbWF4\nLCBiaWFzX2Fic1tpXSkKICAgICAgICBlbnZlbG9wZVtpXSA9IHJ1bm5pbmdfbWF4CgogICAgaWYg\nYXN2X3R5cGUgPT0gJ3NpZ25fZmxpcCc6CiAgICAgICAgaWYgYWJzKHRhdV90cnVlKSA8IDFlLTEy\nOgogICAgICAgICAgICByZXR1cm4gTm9uZQogICAgICAgIGJhc2VsaW5lX3NpZ24gPSBucC5zaWdu\nKHRhdV90cnVlKQogICAgICAgIGZvciBpIGluIHJhbmdlKG5fZ3JpZCk6CiAgICAgICAgICAgIGlm\nIG5wLmlzZmluaXRlKHRhdV9jdXJ2ZVtpXSkgYW5kIG5wLnNpZ24odGF1X2N1cnZlW2ldKSAhPSBi\nYXNlbGluZV9zaWduOgogICAgICAgICAgICAgICAgcmV0dXJuIGZsb2F0KGRlbHRhc1tpXSkKICAg\nICAgICByZXR1cm4gTm9uZQogICAgZWxpZiBhc3ZfdHlwZSA9PSAnbWFnbml0dWRlJzoKICAgICAg\nICBpZiBhYnModGF1X3RydWUpIDwgMWUtMTI6CiAgICAgICAgICAgIHJldHVybiBOb25lCiAgICAg\nICAgdGhyZXNoID0gMC4xICogYWJzKHRhdV90cnVlKQogICAgICAgIGZvciBpIGluIHJhbmdlKG5f\nZ3JpZCk6CiAgICAgICAgICAgIGlmIGVudmVsb3BlW2ldID4gdGhyZXNoOgogICAgICAgICAgICAg\nICAgcmV0dXJuIGZsb2F0KGRlbHRhc1tpXSkKICAgICAgICByZXR1cm4gTm9uZQogICAgZWxpZiBh\nc3ZfdHlwZSA9PSAnc2lnbmlmaWNhbmNlJzoKICAgICAgICBpZiBzZV9yZWYgaXMgTm9uZSBvciBz\nZV9yZWYgPCAxZS0xMjoKICAgICAgICAgICAgcmV0dXJuIE5vbmUKICAgICAgICBmb3IgaSBpbiBy\nYW5nZShuX2dyaWQpOgogICAgICAgICAgICBpZiBucC5pc2Zpbml0ZSh0YXVfY3VydmVbaV0pIGFu\nZCBhYnModGF1X2N1cnZlW2ldKSA8IDEuOTYgKiBzZV9yZWY6CiAgICAgICAgICAgICAgICByZXR1\ncm4gZmxvYXQoZGVsdGFzW2ldKQogICAgICAgIHJldHVybiBOb25lCiAgICByZXR1cm4gTm9uZQoK\nCmRlZiBlc3RpbWF0ZV9yZWZlcmVuY2Vfc2UoSywgdG9wb2xvZ3ksIHBhcmFtcywgTl9yZWY9NTAw\nMCwgbl9tYz01MCwgc2VlZD05OTkpOgogICAgZ2VuX2ZuID0gR0VOX0ZOU1t0b3BvbG9neV0KICAg\nIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyhzZWVkKQogICAgdGF1X2hhdHMgPSBbXQogICAg\nZm9yIF8gaW4gcmFuZ2Uobl9tYyk6CiAgICAgICAgZmlyc3RfdmFyLCBZLCBBID0gZ2VuX2ZuKEss\nIE5fcmVmLCBwYXJhbXMsIHJuZykKICAgICAgICBpZiB0b3BvbG9neSA9PSAnaXYnOgogICAgICAg\nICAgICB0aCwgXyA9IHdhbGRfZXN0aW1hdG9yKGZpcnN0X3ZhciwgWSwgQSwgaz0xKQogICAgICAg\nIGVsaWYgdG9wb2xvZ3kgPT0gJ2V4cG9zdXJlJzoKICAgICAgICAgICAgYiwgXyA9IG9sc19ub19U\nKFksIEEsIEspCiAgICAgICAgICAgIHRoID0gYlsxXQogICAgICAgIGVsc2U6CiAgICAgICAgICAg\nIGIsIF8gPSBvbHNfd2l0aF9kdW1taWVzKFksIGZpcnN0X3ZhciwgQSwgSykKICAgICAgICAgICAg\ndGggPSBiWzFdCiAgICAgICAgaWYgbnAuaXNmaW5pdGUodGgpOgogICAgICAgICAgICB0YXVfaGF0\ncy5hcHBlbmQodGgpCiAgICByZXR1cm4gZmxvYXQobnAuc3RkKHRhdV9oYXRzKSkgaWYgbGVuKHRh\ndV9oYXRzKSA+IDIgZWxzZSBucC5uYW4KCgpkZWYgY29tcHV0ZV9hbGxfYXN2cyhjb25mdXNpb25f\nbWF0cmljZXMsIGFsbF9zdWZmX3N0YXRzLCBhbGxfdGF1X3RydWUsIGFsbF9zZV9yZWYpOgogICAg\ncmVzdWx0cyA9IFtdCiAgICBmb3IgKGRhdGFzZXQsIG1vZGVsLCBwcm9tcHQpLCBDIGluIGNvbmZ1\nc2lvbl9tYXRyaWNlcy5pdGVtcygpOgogICAgICAgIEsgPSBEQVRBU0VUU1tkYXRhc2V0XVsnSydd\nCiAgICAgICAgZm9yIHRvcG9sb2d5IGluIFRPUE9MT0dJRVM6CiAgICAgICAgICAgIHN0ID0gYWxs\nX3N1ZmZfc3RhdHNbKEssIHRvcG9sb2d5KV0KICAgICAgICAgICAgdGF1X3RydWUgPSBhbGxfdGF1\nX3RydWVbKEssIHRvcG9sb2d5KV0KICAgICAgICAgICAgc2VfcmVmID0gYWxsX3NlX3JlZi5nZXQo\nKEssIHRvcG9sb2d5KSkKICAgICAgICAgICAgZm9yIGFzdl90eXBlIGluIFsnbWFnbml0dWRlJywg\nJ3NpZ25pZmljYW5jZScsICdzaWduX2ZsaXAnXToKICAgICAgICAgICAgICAgIGFzdiA9IGNvbXB1\ndGVfYXN2X2Zvcl9tYXRyaXgoQywgSywgdG9wb2xvZ3ksIHN0LCB0YXVfdHJ1ZSwKICAgICAgICAg\nICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYXN2X3R5cGUsIHNlX3JlZj1zZV9y\nZWYpCiAgICAgICAgICAgICAgICByZXN1bHRzLmFwcGVuZCh7CiAgICAgICAgICAgICAgICAgICAg\nJ2RhdGFzZXQnOiBkYXRhc2V0LCAnbW9kZWwnOiBtb2RlbCwgJ3Byb21wdCc6IHByb21wdCwKICAg\nICAgICAgICAgICAgICAgICAnSyc6IEssICd0b3BvbG9neSc6IHRvcG9sb2d5LCAnYXN2X3R5cGUn\nOiBhc3ZfdHlwZSwKICAgICAgICAgICAgICAgICAgICAnYXN2JzogYXN2LAogICAgICAgICAgICAg\nICAgfSkKICAgIHJldHVybiByZXN1bHRzCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgNC4gRjEg\ndnMgRG93bnN0cmVhbSBCaWFzCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIGNvbXB1dGVfZjFf\nZnJvbV9DKEMsIEssIHBfQT1Ob25lKToKICAgIGlmIHBfQSBpcyBOb25lOgogICAgICAgIHBfQSA9\nIG5wLm9uZXMoSykgLyBLCiAgICBwcmVjaXNpb24gPSBucC56ZXJvcyhLKQogICAgcmVjYWxsID0g\nbnAuemVyb3MoSykKICAgIGYxID0gbnAuemVyb3MoSykKICAgIGZvciBpIGluIHJhbmdlKEspOgog\nICAgICAgIHJlY2FsbFtpXSA9IENbaSwgaV0KICAgICAgICBkZW5vbSA9IHN1bShDW2ksIGpdICog\ncF9BW2pdIGZvciBqIGluIHJhbmdlKEspKQogICAgICAgIHByZWNpc2lvbltpXSA9IENbaSwgaV0g\nKiBwX0FbaV0gLyBkZW5vbSBpZiBkZW5vbSA+IDFlLTEyIGVsc2UgMAogICAgICAgIGlmIHByZWNp\nc2lvbltpXSArIHJlY2FsbFtpXSA+IDFlLTEyOgogICAgICAgICAgICBmMVtpXSA9IDIgKiBwcmVj\naXNpb25baV0gKiByZWNhbGxbaV0gLyAocHJlY2lzaW9uW2ldICsgcmVjYWxsW2ldKQogICAgcmV0\ndXJuIHsKICAgICAgICAnbWFjcm9fZjEnOiBmbG9hdChmMS5tZWFuKCkpLAogICAgICAgICd3ZWln\naHRlZF9mMSc6IGZsb2F0KChwX0EgKiBmMSkuc3VtKCkpLAogICAgICAgICdwZXJfY2xhc3NfZjEn\nOiBmMS50b2xpc3QoKSwKICAgIH0KCgpkZWYgZjFfdnNfYmlhc19hbmFseXNpcyhjb25mdXNpb25f\nbWF0cmljZXMsIGJpYXNlcyk6CiAgICByZXN1bHRzID0gW10KICAgIGZvciBiIGluIGJpYXNlczoK\nICAgICAgICBrZXkgPSAoYlsnZGF0YXNldCddLCBiWydtb2RlbCddLCBiWydwcm9tcHQnXSkKICAg\nICAgICBpZiBrZXkgbm90IGluIGNvbmZ1c2lvbl9tYXRyaWNlczoKICAgICAgICAgICAgY29udGlu\ndWUKICAgICAgICBDID0gY29uZnVzaW9uX21hdHJpY2VzW2tleV0KICAgICAgICBLID0gYlsnSydd\nCiAgICAgICAgcF9BID0gbWFrZV9wX0EoSykKICAgICAgICBmMV9pbmZvID0gY29tcHV0ZV9mMV9m\ncm9tX0MoQywgSywgcF9BKQogICAgICAgIGFic19iaWFzID0gYWJzKGJbJ2JpYXMnXSkgaWYgYlsn\nYmlhcyddIGlzIG5vdCBOb25lIGVsc2UgTm9uZQogICAgICAgIHJlc3VsdHMuYXBwZW5kKHsKICAg\nICAgICAgICAgJ2RhdGFzZXQnOiBiWydkYXRhc2V0J10sICdtb2RlbCc6IGJbJ21vZGVsJ10sICdw\ncm9tcHQnOiBiWydwcm9tcHQnXSwKICAgICAgICAgICAgJ0snOiBLLCAndG9wb2xvZ3knOiBiWyd0\nb3BvbG9neSddLAogICAgICAgICAgICAnbWFjcm9fZjEnOiBmMV9pbmZvWydtYWNyb19mMSddLCAn\nd2VpZ2h0ZWRfZjEnOiBmMV9pbmZvWyd3ZWlnaHRlZF9mMSddLAogICAgICAgICAgICAnYWJzX2Jp\nYXMnOiBhYnNfYmlhcywgJ2JpYXNfcGN0JzogYlsnYmlhc19wY3QnXSwKICAgICAgICAgICAgJ3Np\nZ25fZmxpcCc6IGJbJ3NpZ25fZmxpcCddLAogICAgICAgIH0pCiAgICByZXR1cm4gcmVzdWx0cwoK\nCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PQojIDUuIFR5cGUgSS9JSSBFcnJvciBSYXRlcwojID09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT0KCmRlZiBjb21wdXRlX3R5cGUxX3R5cGUyX2Zvcl9DKEMsIEssIHRvcG9s\nb2d5LCBwYXJhbXNfSDEsIHBhcmFtc19IMCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg\nc3RfSDEsIHRhdV90cnVlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX3NpbT0xMDAs\nIE5fc2FtcGxlPTUwMDAsIHNlZWQ9NDIpOgogICAgZ2VuX2Z",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/fb66a23b-ab7a-49cf-9609-9cc0b887dde7/tool-results/b6kld4k1f.txt",
    "persistedOutputSize": 51724
  }
}
```

</details>

---


### Assistant

_source line 76_

Let me use a different approach — write the script via ssh_execute using a Python one-liner to decode base64, splitting into manageable chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "be9044fb-3227-4319-9f00-7b8b17cac3ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QULzhq5NC8kychySPp8JeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 46522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1845
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

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01L5oRQyr476c6WJrfH9nWwF`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py | wc -l",
  "description": "Count lines in script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "84bafddc-9b77-4697-929f-0f154d3d6db9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QULzhq5NC8kychySPp8JeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 46522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1845
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


### Tool result

_source line 78 · 2026-05-20T21:25:29.105Z_

<details><summary>↩ Tool result · `toolu_01L5oRQyr476c6WJrfH9nWwF`</summary>

```text
1047
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "6cc5caf0-c7df-40dd-892c-34d4db0099bc",
  "tool_use_result": {
    "stdout": "1047",
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

_source line 79_

I'll transfer the file via scp directly using the SSH config:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "24759452-a43d-4a87-a6bb-13caeeb2a9a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuVy2DzNCaEixPzVteK4do",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 48367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 163
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

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_015aJ9xperYktWfeaPcTuLJ9`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py implicit5638.xyfu.me:/home/sonny/causal_annot_error_attrib/plan_006_asv_empirical.py 2>&1",
  "description": "SCP script to server",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "56c68f18-b2da-4e73-8071-177e4001c69d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuVy2DzNCaEixPzVteK4do",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 48367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 163
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


### Tool result

_source line 81 · 2026-05-20T21:25:34.688Z_

<details><summary>↩ Tool result · reported error · `toolu_015aJ9xperYktWfeaPcTuLJ9`</summary>

```text
Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Host key verification failed.
scp: Connection closed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "0ad6bf07-0fba-461a-bf48-fc27487927aa",
  "tool_use_result": "Error: Exit code 255\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nHost key verification failed.\r\nscp: Connection closed"
}
```

</details>

---


### Assistant

_source line 82_

SCP not available directly. Let me use the MCP ssh_execute tool to transfer the file content. I'll split it into chunks and write via base64.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "dd613df1-88ef-486f-a641-a410269a91ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BPorMjYN4myCSMvRwdSmQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 48530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_019A2Y7XzpzgXhx83jSeMsyC`</summary>

```json
{
  "command": "base64 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py | head -c 20000",
  "description": "Get first 20K chars of base64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "cc081400-ac78-4caf-a9f9-8a5734104271",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BPorMjYN4myCSMvRwdSmQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 48530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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


### Tool result

_source line 84 · 2026-05-20T21:25:39.138Z_

<details><summary>↩ Tool result · `toolu_019A2Y7XzpzgXhx83jSeMsyC`</summary>

```text
IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJy
YXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJp
Y2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMg
ZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBE
b3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNl
bnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAg
My4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0
aW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmlu
ZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFz
ZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6
IHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0
aWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczog
bnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIKCmlt
cG9ydCBudW1weSBhcyBucAppbXBvcnQganNvbgppbXBvcnQgYXJncGFyc2UKaW1wb3J0IG9zCmlt
cG9ydCB0aW1lCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0Cgp0cnk6CiAgICBp
bXBvcnQgbWF0cGxvdGxpYgogICAgbWF0cGxvdGxpYi51c2UoJ0FnZycpCiAgICBpbXBvcnQgbWF0
cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBIQVNfTVBMID0gVHJ1ZQpleGNlcHQgSW1wb3J0RXJy
b3I6CiAgICBIQVNfTVBMID0gRmFsc2UKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIENvbnN0YW50
cwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT0KCkRBVEFTRVRTID0gT3JkZXJlZERpY3QoWwogICAgKCdj
aXZpbF9jb21tZW50cycsIHsnSyc6IDJ9KSwKICAgICgndmFzdCcsIHsnSyc6IDN9KSwKICAgICgn
aHVtYWlkJywgeydLJzogMTB9KSwKXSkKCk1PREVMUyA9IFsnbGxhbWE0JywgJ3F3ZW4zJywgJ2Rl
ZXBzZWVrJ10KUFJPTVBUUyA9IFsnemVyby1zaG90JywgJ2Zldy1zaG90LTMnLCAnZmV3LXNob3Qt
NSddCgpUT1BPTE9HSUVTID0gWydjb25mb3VuZGluZycsICdtZWRpYXRpb24nLCAnY29sbGlkZXIn
LCAnZXhwb3N1cmUnLAogICAgICAgICAgICAgICdtYmlhcycsICdpdicsICdmcm9udGRvb3InXQoK
Tl9QUkVDT01QID0gMl8wMDBfMDAwCgojIFBhcmFtZXRlciBwb29scyDigJQgSz0zIHZhbHVlcyBt
YXRjaCBwbGFuXzAwMS9wbGFuXzAwNQpfQUxQSEFfUE9PTCA9IFsxLjUsIC0xLjAsIDAuOCwgLTAu
NSwgMS4yLCAtMC43LCAwLjksIC0wLjQsIDAuNl0KX0JFVEFfQV9QT09MID0gWzEuMCwgLTAuNSwg
MC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0JFVEFfUE9PTCA9IFswLjAs
IDEuMCwgLTAuNSwgMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0dBTU1B
X1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAuMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1
LCAwLjFdCl9ERUxUQV9QT09MID0gWzAuMCwgMC44LCAtMC42LCAwLjUsIC0wLjQsIDAuMywgLTAu
MiwgMC4xNSwgLTAuMSwgMC4wNV0KX0RUX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAu
MiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1LCAwLjFdCl9EWV9QT09MID0gWzAuMCwgMC44LCAwLjYs
IC0wLjUsIDAuNCwgLTAuMywgMC4yLCAwLjE1LCAtMC4xLCAwLjA1XQoKCiMgPT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PQojIFV0aWxpdHkgRnVuY3Rpb25zCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHNv
ZnRtYXhfcm93cyhsb2dpdHMpOgogICAgZSA9IG5wLmV4cChsb2dpdHMgLSBsb2dpdHMubWF4KGF4
aXM9MSwga2VlcGRpbXM9VHJ1ZSkpCiAgICByZXR1cm4gZSAvIGUuc3VtKGF4aXM9MSwga2VlcGRp
bXM9VHJ1ZSkKCgpkZWYgc2FtcGxlX2NhdChwcm9icywgcm5nKToKICAgIGN1bSA9IG5wLmN1bXN1
bShwcm9icywgYXhpcz0xKQogICAgdSA9IHJuZy51bmlmb3JtKHNpemU9cHJvYnMuc2hhcGVbMF0p
WzosIE5vbmVdCiAgICByZXR1cm4gKHUgPj0gY3VtWzosIDotMV0pLnN1bShheGlzPTEpLmFzdHlw
ZShpbnQpCgoKZGVmIGdlbmVyYXRlX0FzdGFyKEEsIEMsIHJuZyk6CiAgICBwcm9icyA9IENbOiwg
QV0KICAgIGN1bSA9IG5wLmN1bXN1bShwcm9icywgYXhpcz0wKQogICAgdSA9IHJuZy51bmlmb3Jt
KHNpemU9bGVuKEEpKQogICAgcmV0dXJuICh1W05vbmUsIDpdID49IGN1bVs6LTFdKS5zdW0oYXhp
cz0wKS5hc3R5cGUoaW50KQoKCmRlZiBvbHNfd2l0aF9kdW1taWVzKFksIFQsIEFzdGFyLCBLKToK
ICAgIE4gPSBsZW4oWSkKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGsgaW4g
cmFuZ2UoMSwgSyk6CiAgICAgICAgRFs6LCBrIC0gMV0gPSAoQXN0YXIgPT0gaykuYXN0eXBlKGZs
b2F0KQogICAgWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAub25lcyhOKSwgVCwgRF0pCiAgICB0cnk6
CiAgICAgICAgYmV0YSA9IG5wLmxpbmFsZy5sc3RzcShYLCBZLCByY29uZD1Ob25lKVswXQogICAg
ICAgIHJlc2lkID0gWSAtIFggQCBiZXRhCiAgICAgICAgc2lnbWEyID0gbnAuc3VtKHJlc2lkKioy
KSAvIG1heChOIC0gWC5zaGFwZVsxXSwgMSkKICAgICAgICBYdFhfaW52ID0gbnAubGluYWxnLmlu
dihYLlQgQCBYKQogICAgICAgIHNlID0gbnAuc3FydChucC5tYXhpbXVtKHNpZ21hMiAqIG5wLmRp
YWcoWHRYX2ludiksIDApKQogICAgZXhjZXB0IG5wLmxpbmFsZy5MaW5BbGdFcnJvcjoKICAgICAg
ICBiZXRhID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICAgICAgc2UgPSBucC5mdWxs
KFguc2hhcGVbMV0sIG5wLm5hbikKICAgIHJldHVybiBiZXRhLCBzZQoKCmRlZiBvbHNfbm9fVChZ
LCBBc3RhciwgSyk6CiAgICBOID0gbGVuKFkpCiAgICBEID0gbnAuemVyb3MoKE4sIEsgLSAxKSkK
ICAgIGZvciBrIGluIHJhbmdlKDEsIEspOgogICAgICAgIERbOiwgayAtIDFdID0gKEFzdGFyID09
IGspLmFzdHlwZShmbG9hdCkKICAgIFggPSBucC5jb2x1bW5fc3RhY2soW25wLm9uZXMoTiksIERd
KQogICAgdHJ5OgogICAgICAgIGJldGEgPSBucC5saW5hbGcubHN0c3EoWCwgWSwgcmNvbmQ9Tm9u
ZSlbMF0KICAgICAgICByZXNpZCA9IFkgLSBYIEAgYmV0YQogICAgICAgIHNpZ21hMiA9IG5wLnN1
bShyZXNpZCoqMikgLyBtYXgoTiAtIFguc2hhcGVbMV0sIDEpCiAgICAgICAgWHRYX2ludiA9IG5w
LmxpbmFsZy5pbnYoWC5UIEAgWCkKICAgICAgICBzZSA9IG5wLnNxcnQobnAubWF4aW11bShzaWdt
YTIgKiBucC5kaWFnKFh0WF9pbnYpLCAwKSkKICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJy
b3I6CiAgICAgICAgYmV0YSA9IG5wLmZ1bGwoWC5zaGFwZVsxXSwgbnAubmFuKQogICAgICAgIHNl
ID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICByZXR1cm4gYmV0YSwgc2UKCgpkZWYg
d2FsZF9lc3RpbWF0b3IoWiwgWSwgQXN0YXIsIGs9MSk6CiAgICB6MSA9IFogPT0gMTsgejAgPSBa
ID09IDAKICAgIG4xLCBuMCA9IGZsb2F0KHoxLnN1bSgpKSwgZmxvYXQoejAuc3VtKCkpCiAgICBp
ZiBuMSA8IDIgb3IgbjAgPCAyOgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgUkYg
PSBZW3oxXS5tZWFuKCkgLSBZW3owXS5tZWFuKCkKICAgIHZhcl9SRiA9IFlbejFdLnZhcigpIC8g
bjEgKyBZW3owXS52YXIoKSAvIG4wCiAgICBEa196MSA9IChBc3Rhclt6MV0gPT0gaykuYXN0eXBl
KGZsb2F0KS5tZWFuKCkKICAgIERrX3owID0gKEFzdGFyW3owXSA9PSBrKS5hc3R5cGUoZmxvYXQp
Lm1lYW4oKQogICAgRlMgPSBEa196MSAtIERrX3owCiAgICB2YXJfRlMgPSBEa196MSAqICgxIC0g
RGtfejEpIC8gbjEgKyBEa196MCAqICgxIC0gRGtfejApIC8gbjAKICAgIGlmIGFicyhGUykgPCAx
ZS04OgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgVyA9IFJGIC8gRlMKICAgIHZh
cl9XID0gdmFyX1JGIC8gRlMqKjIgKyBSRioqMiAqIHZhcl9GUyAvIEZTKio0CiAgICByZXR1cm4g
VywgbnAuc3FydChtYXgodmFyX1csIDApKQoKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIERHUCBQ
YXJhbWV0ZXJzIChnZW5lcmFsIEssIEs9MyBtYXRjaGVzIHBsYW5fMDAxL3BsYW5fMDA1KQojID09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT0KCmRlZiBtYWtlX3BfQShLKToKICAgIGlmIEsgPT0gMjoKICAgICAg
ICByZXR1cm4gbnAuYXJyYXkoWzAuNTUsIDAuNDVdKQogICAgZWxpZiBLID09IDM6CiAgICAgICAg
cmV0dXJuIG5wLmFycmF5KFswLjQwLCAwLjM1LCAwLjI1XSkKICAgIGVsc2U6CiAgICAgICAgcmF3
ID0gbnAuYXJyYXkoWzEuMCAvIChpICsgMSkgZm9yIGkgaW4gcmFuZ2UoSyldKQogICAgICAgIHJl
dHVybiByYXcgLyByYXcuc3VtKCkKCgpkZWYgbWFrZV9kZ3BfcGFyYW1zKEspOgogICAgcF9BID0g
bWFrZV9wX0EoSykKICAgIHBhcmFtcyA9IHsKICAgICAgICAnY29uZm91bmRpbmcnOiB7CiAgICAg
ICAgICAgICdwX0EnOiBwX0EsCiAgICAgICAgICAgICdhbHBoYSc6IG5wLmFycmF5KF9BTFBIQV9Q
T09MWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9BJzogbnAuYXJyYXkoX0JFVEFfQV9QT09M
WzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9UJzogMi4wLAogICAgICAgICAgICAnc2lnbWFf
VCc6IDEuMCwKICAgICAgICB9LAogICAgICAgICdtZWRpYXRpb24nOiB7CiAgICAgICAgICAgICd0
YXUnOiAwLjUsCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSks
CiAgICAgICAgICAgICdkZWx0YSc6IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSksCiAgICAgICAg
ICAgICdiZXRhJzogbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAg
J2NvbGxpZGVyJzogewogICAgICAgICAgICAndGF1JzogMS4wLAogICAgICAgICAgICAnZyc6IG5w
Lnplcm9zKEspLAogICAgICAgICAgICAnZFQnOiBucC5hcnJheShfRFRfUE9PTFs6S10pLAogICAg
ICAgICAgICAnZFknOiBucC5hcnJheShfRFlfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAg
J2V4cG9zdXJlJzogewogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktd
KSwKICAgICAgICAgICAgJ3BfQSc6IHBfQSwKICAgICAgICB9LAogICAgfQogICAgaWYgSyA9PSAz
OgogICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2Rl
bHRhX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoMyks
CiAgICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMCwgMC44LCAtMC41XSksCiAgICAgICAg
ICAgICdhX1UyJzogbnAuYXJyYXkoWzAuMCwgMC42LCAwLjldKSwKICAgICAgICB9CiAgICAgICAg
cGFyYW1zWydpdiddID0gewogICAgICAgICAgICAnbGFtJzogMS4wLCAnYmV0YSc6IG5wLmFycmF5
KFswLjAsIDAuNSwgLTAuMjVdKSwKICAgICAgICAgICAgJ2cnOiBucC56ZXJvcygzKSwKICAgICAg
ICAgICAgJ2RaJzogbnAuYXJyYXkoWzAuMCwgMS4wLCAtMC41XSksCiAgICAgICAgICAgICdkVSc6
IG5wLmFycmF5KFswLjAsIDAuOCwgMC42XSksCiAgICAgICAgfQogICAgICAgIHBhcmFtc1snZnJv
bnRkb29yJ10gPSB7CiAgICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAs
CiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KFswLjAsIDAuNSwgLTAuM10pLAogICAgICAg
ICAgICAnZGVsdGFfZmQnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjhdKSwKICAgICAgICAgICAg
J2JldGEnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjVdKSwKICAgICAgICB9CiAgICBlbHNlOgog
ICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2RlbHRh
X2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoSyksCiAg
ICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMF0gKyBbX0FMUEhBX1BPT0xbaV0gKiAwLjYg
Zm9yIGkgaW4gcmFuZ2UoSyAtIDEpXSksCiAgICAgICAgICAgICdhX1UyJzogbnAuYXJyYXkoWzAu
MF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC44IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAogICAg
ICAgIH0KICAgICAgICBpdl9iZXRhID0gbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pICogMC41CiAg
ICAgICAgaXZfYmV0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snaXYnXSA9IHsKICAgICAgICAg
ICAgJ2xhbSc6IDEuMCwgJ2JldGEnOiBpdl9iZXRhLAogICAgICAgICAgICAnZyc6IG5wLnplcm9z
KEspLAogICAgICAgICAgICAnZFonOiBucC5hcnJheShbMC4wXSArIFtfQUxQSEFfUE9PTFtpXSAq
IDAuNyBmb3IgaSBpbiByYW5nZShLIC0gMSldKSwKICAgICAgICAgICAgJ2RVJzogbnAuYXJyYXko
WzAuMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC42IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAog
ICAgICAgIH0KICAgICAgICBmZF9kZWx0YSA9IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSkKICAg
ICAgICBmZF9kZWx0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snZnJvbnRkb29yJ10gPSB7CiAg
ICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAsCiAgICAgICAgICAgICdn
YW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSksCiAgICAgICAgICAgICdkZWx0YV9mZCc6
IGZkX2RlbHRhLAogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktdKSwK
ICAgICAgICB9CiAgICByZXR1cm4gcGFyYW1zCgoKZGVmIG1ha2VfZGdwX3BhcmFtc19IMChLLCBw
YXJhbXMpOgogICAgcDAgPSB7fQogICAgZm9yIHRvcG8sIHAgaW4gcGFyYW1zLml0ZW1zKCk6CiAg
ICAgICAgaWYgdG9wbyA9PSAnY29uZm91bmRpbmcnOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRp
Y3QocCwgYmV0YV9UPTAuMCkKICAgICAgICBlbGlmIHRvcG8gPT0gJ21lZGlhdGlvbic6CiAgICAg
ICAgICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAn
Y29sbGlkZXInOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgdGF1PTAuMCkKICAgICAg
ICBlbGlmIHRvcG8gPT0gJ2V4cG9zdXJlJzoKICAgICAgICAgICAgcDBbdG9wb10gPSBkaWN0KHAs
IGJldGE9bnAuemVyb3MoSykpCiAgICAgICAgZWxpZiB0b3BvID09ICdtYmlhcyc6CiAgICAgICAg
ICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAnaXYn
OgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgYmV0YT1ucC56ZXJvcyhLKSkKICAgICAg
ICBlbGlmIHRvcG8gPT0gJ2Zyb250ZG9vcic6CiAgICAgICAgICAgIHAwW3RvcG9dID0gZGljdChw
LCBsYW1iZGFfVT0wLjAsIGFscGhhX1U9MC4wLAogICAgICAgICAgICAgICAgICAgICAgICAgICAg
ZGVsdGFfZmQ9bnAuemVyb3MoSyksIGJldGE9bnAuemVyb3MoSykpCiAgICByZXR1cm4gcDAKCgoj
ID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT0KIyBER1AgR2VuZXJhdG9ycyAoZ2VuZXJhbCBLKQojID09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT0KCmRlZiBnZW5fY29uZm91bmRpbmcoSywgTiwgcCwgcm5nKToKICAgIEEg
PSBybmcuY2hvaWNlKEssIHNpemU9TiwgcD1wWydwX0EnXSkKICAgIEQgPSBucC56ZXJvcygoTiwg
SyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9
PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAgVCA9IEQgQCBwWydhbHBoYSddICsgcm5nLm5vcm1h
bCgwLCBwWydzaWdtYV9UJ10sIE4pCiAgICBZID0gcFsnYmV0YV9UJ10gKiBUICsgRCBAIHBbJ2Jl
dGFfQSddICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFksIEEKCgpkZWYgZ2Vu
X21lZGlhdGlvbihLLCBOLCBwLCBybmcpOgogICAgVCA9IHJuZy5iaW5vbWlhbCgxLCAwLjUsIE4p
LmFzdHlwZShmbG9hdCkKICAgIGxvZ2l0cyA9IHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0
YSddW05vbmUsIDpdICogVFs6LCBOb25lXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRz
KQogICAgQSA9IHNhbXBsZV9jYXQocHJvYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAt
IDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9PSBq
ICsgMSkuYXN0eXBlKGZsb2F0KQogICAgWSA9IHBbJ2JldGEnXVswXSArIEQgQCBwWydiZXRhJ11b
MTpdICsgcFsndGF1J10gKiBUICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFks
IEEKCgpkZWYgZ2VuX2NvbGxpZGVyKEssIE4sIHAsIHJuZyk6CiAgICBUID0gcm5nLm5vcm1hbCgw
LCAxLCBOKQogICAgWSA9IHBbJ3RhdSddICogVCArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxv
Z2l0cyA9IChwWydnJ11bTm9uZSwgOl0gKyBwWydkVCddW05vbmUsIDpdICogVFs6LCBOb25lXQog
ICAgICAgICAgICAgICsgcFsnZFknXVtOb25lLCA6XSAqIFlbOiwgTm9uZV0pCiAgICBwcm9icyA9
IHNvZnRtYXhfcm93cyhsb2dpdHMpCiAgICBBID0gc2FtcGxlX2NhdChwcm9icywgcm5nKQogICAg
cmV0dXJuIFQsIFksIEEKCgpkZWYgZ2VuX2V4cG9zdXJlKEssIE4sIHAsIHJuZyk6CiAgICBBID0g
cm5nLmNob2ljZShLLCBzaXplPU4sIHA9cFsncF9BJ10pCiAgICBEID0gbnAuemVyb3MoKE4sIEsg
LSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEgPT0g
aiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBwWydiZXRhJ11bMF0gKyBEIEAgcFsnYmV0YSdd
WzE6XSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBOb25lLCBZLCBBCgoKZGVmIGdl
bl9tYmlhcyhLLCBOLCBwLCBybmcpOgogICAgVTEgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAgICBV
MiA9IHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIFQgPSBwWydkZWx0YV9jb2VmJ10gKiBVMSArIHJu
Zy5ub3JtYWwoMCwgMSwgTikKICAgIFkgPSBwWyd0YXUnXSAqIFQgKyBwWydsYW0nXSAqIFUyICsg
cm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtOb25lLCA6XSArIHBbJ2Ff
VTEnXVtOb25lLCA6XSAqIFUxWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBwWydhX1UyJ11bTm9u
ZSwgOl0gKiBVMls6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxvZ2l0cykKICAg
IEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICByZXR1cm4gVCwgWSwgQQoKCmRlZiBnZW5f
aXYoSywgTiwgcCwgcm5nKToKICAgIFogPSBybmcuYmlub21pYWwoMSwgMC41LCBOKS5hc3R5cGUo
ZmxvYXQpCiAgICBVID0gcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtO
b25lLCA6XSArIHBbJ2RaJ11bTm9uZSwgOl0gKiBaWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBw
WydkVSddW05vbmUsIDpdICogVVs6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxv
Z2l0cykKICAgIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICBEID0gbnAuemVyb3MoKE4s
IEsgLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEg
PT0gaiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBEIEAgcFsnYmV0YSddWzE6XSArIHBbJ2xh
bSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBaLCBZLCBBCgoKZGVmIGdl
bl9mcm9udGRvb3IoSywgTiwgcCwgcm5nKToKICAgIFUgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAg
ICBUID0gcFsnYWxwaGFfVSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxvZ2l0cyA9
IHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0YV9mZCddW05vbmUsIDpdICogVFs6LCBOb25l
XQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRzKQogICAgTSA9IHNhbXBsZV9jYXQocHJv
YnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2Uo
SyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoTSA9PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAg
WSA9IEQgQCBwWydiZXRhJ11bMTpdICsgcFsnbGFtYmRhX1UnXSAqIFUgKyBybmcubm9ybWFsKDAs
IDEsIE4pCiAgICByZXR1cm4gVCwgWSwgTQoKCkdFTl9GTlMgPSB7CiAgICAnY29uZm91bmRpbmcn
OiBnZW5fY29uZm91bmRpbmcsICdtZWRpYXRpb24nOiBnZW5fbWVkaWF0aW9uLAogICAgJ2NvbGxp
ZGVyJzogZ2VuX2NvbGxpZGVyLCAnZXhwb3N1cmUnOiBnZW5fZXhwb3N1cmUsCiAgICAnbWJpYXMn
OiBnZW5fbWJpYXMsICdpdic6IGdlbl9pdiwgJ2Zyb250ZG9vcic6IGdlbl9mcm9udGRvb3IsCn0K
CgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT0KIyBTdWZmaWNpZW50IFN0YXRpc3RpY3MgJiBQbGltIChn
ZW5lcmFsIEspCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHByZWNvbXB1dGVfc3VmZl9zdGF0
cyhLLCB0b3BvbG9neSwgcGFyYW1zLCBOPU5fUFJFQ09NUCwgc2VlZD00Mik6CiAgICBybmcgPSBu
cC5yYW5kb20uZGVmYXVsdF9ybmcoc2VlZCkKICAgIGZpcnN0X3ZhciwgWSwgQSA9IEdFTl9GTlNb
dG9wb2xvZ3ldKEssIE4sIHBhcmFtcywgcm5nKQogICAgREEgPSBucC56ZXJvcygoTiwgSykpCiAg
ICBmb3IgayBpbiByYW5nZShLKToKICAgICAgICBEQVs6LCBrXSA9IChBID09IGspLmFzdHlwZShm
bG9hdCkKCiAgICBpZiB0b3BvbG9neSA9PSAnaXYnOgogICAgICAgIFogPSBmaXJzdF92YXIKICAg
ICAgICB6MSA9IFogPT0gMTsgejAgPSBaID09IDAKICAgICAgICBSRiA9IFlbejFdLm1lYW4oKSAt
IFlbejBdLm1lYW4oKQogICAgICAgIEZTID0gbnAuemVyb3MoSykKICAgICAgICBmb3IgayBpbiBy
YW5nZShLKToKICAgICAgICAgICAgRlNba10gPSAoQVt6MV0gPT0gaykubWVhbigpIC0gKEFbejBd
ID09IGspLm1lYW4oKQogICAgICAgIHJldHVybiBkaWN0KFJGPVJGLCBGUz1GUywgdG9wb2xvZ3k9
J2l2JykKICAgIGVsaWYgdG9wb2xvZ3kgPT0gJ2V4cG9zdXJlJzoKICAgICAgICByZXR1cm4gZGlj
dChwX0E9REEubWVhbigwKSwgRV9ZPVkubWVhbigpLAogICAgICAgICAgICAgICAgICAgIEVfWUQ9
KERBICogWVs6LCBOb25lXSkubWVhbigwKSwgdG9wb2xvZ3k9J2V4cG9zdXJlJykKICAgIGVsc2U6
CiAgICAgICAgVCA9IGZpcnN0X3ZhcgogICAgICAgIHJldHVybiBkaWN0KAogICAgICAgICAgICBw
X0E9REEubWVhbigwKSwgRV9UPVQubWVhbigpLCBFX1QyPShUKioyKS5tZWFuKCksCiAgICAgICAg
ICAgIEVfWT1ZLm1lYW4oKSwgRV9UWT0oVCAqIFkpLm1lYW4oKSwKICAgICAgICAgICAgRV9URD0o
REEgKiBUWzosIE5vbmVdKS5tZWFuKDApLAogICAgICAgICAgICBFX1lEPShEQSAqIFlbOiwgTm9u
ZV0pLm1lYW4oMCksIHRvcG9sb2d5PXRvcG9sb2d5KQoKCmRlZiBjb21wdXRlX3BsaW0oQywgc3Qs
IEspOgogICAgaWYgc3RbJ3RvcG9sb2d5J10gPT0gJ2l2JzoKICAgICAgICBGU19zdGFyID0gQyBA
IHN0WydGUyddCiAgICAgICAgaWYgYWJzKEZTX3N0YXJbMV0pIDwgMWUtODoKICAgICAgICAgICAg
cmV0dXJuIG5wLm5hbgogICAgICAgIHJldHVybiBzdFsnUkYnXSAvIEZTX3N0YXJbMV0KICAgIGVs
aWYgc3RbJ3RvcG9sb2d5J10gPT0gJ2V4cG9zdXJlJzoKICAgICAgICBxID0gQyBAIHN0WydwX0En
XQogICAgICAgIGN5ID0gQyBAIHN0WydFX1lEJ10KICAgICAgICBFWlogPSBucC56ZXJvcygoSywg
SykpCiAgICAgICAgRVpaWzAsIDBdID0gMS4wCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6
CiAgICAgICAgICAgIEVaWlswLCBqXSA9IEVaWltqLCAwXSA9IHFbal0KICAgICAgICAgICAgRVpa
W2osIGpdID0gcVtqXQogICAgICAgIEVaWSA9IG5wLnplcm9zKEspCiAgICAgICAgRVpZWzBdID0g
c3RbJ0VfWSddCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWVtq
XSA9IGN5W2pdCiAgICAgICAgdHJ5OgogICAgICAgICAgICByZXR1cm4gbnAubGluYWxnLnNvbHZl
KEVaWiwgRVpZKQogICAgICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJyb3I6CiAgICAgICAg
ICAgIHJldHVybiBucC5mdWxsKEssIG5wLm5hbikKICAgIGVsc2U6CiAgICAgICAgcSA9IEMgQCBz
dFsncF9BJ10KICAgICAgICBjdCA9IEMgQCBzdFsnRV9URCddCiAgICAgICAgY3kgPSBDIEAgc3Rb
J0VfWUQnXQogICAgICAgIGRpbSA9IEsgKyAxCiAgICAgICAgRVpaID0gbnAuemVyb3MoKGRpbSwg
ZGltKSkKICAgICAgICBFWlpbMCwgMF0gPSAxLjAKICAgICAgICBFWlpbMCwgMV0gPSBFWlpbMSwg
MF0gPSBzdFsnRV9UJ10KICAgICAgICBFWlpbMSwgMV0gPSBzdFsnRV9UMiddCiAgICAgICAgZm9y
IGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWlswLCBqICsgMV0gPSBFWlpbaiArIDEs
IDBdID0gcVtqXQogICAgICAgICAgICBFWlpbMSwgaiArIDFdID0gRVpaW2ogKyAxLCAxXSA9IGN0
W2pdCiAgICAgICAgICAgIEVaWltqICsgMSwgaiArIDFdID0gcVtqXQogICAgICAgIEVaWSA9IG5w
Lnplcm9zKGRpbSkKICAgICAgICBFWllbMF0gPSBzdFsnRV9ZJ10KICAgICAgICBFWllbMV0gPSBz
dFsnRV9UWSddCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWVtq
ICsgMV0gPSBjeVtqXQogICAgICAgIHRyeToKICAgICAgICAgICAgcmV0dXJuIG5wLmxpbmFsZy5z
b2x2ZShFWlosIEVaWSkKICAgICAgICBleGNlcHQgbnAubGluYWxnLkxpbkFsZ0Vycm9yOgogICAg
ICAgICAgICByZXR1cm4gbnAuZnVsbChkaW0sIG5wLm5hbikKCgpkZWYgZXh0cmFjdF90YXUocGxp
bV9yZXN1bHQsIHRvcG9sb2d5KToKICAgIGlmIHRvcG9sb2d5ID09ICdpdic6CiAgICAgICAgcmV0
dXJuIGZsb2F0KHBsaW1fcmVzdWx0KSBpZiBucC5pc2Zpbml0ZShwbGltX3Jlc3VsdCkgZWxzZSBu
cC5uYW4KICAgIGlmIGlzaW5zdGFuY2UocGxpbV9yZXN1bHQsIG5wLm5kYXJyYXkpOgogICAgICAg
IHJldHVybiBmbG9hdChwbGltX3Jlc3VsdFsxXSkgaWYgbnAuaXNmaW5pdGUocGxpbV9yZXN1bHRb
MV0pIGVsc2UgbnAubmFuCiAgICByZXR1cm4gbnAubmFuCgoKIyA9PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
CiMgMS4gRGF0YSBMb2FkaW5nICYgQ29uZnVzaW9uIE1hdHJpeAojID09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
PT0KCmRlZiBsb2FkX2Fubm90YXRpb25zKGRhdGFfZGlyLCBkYXRhc2V0LCBtb2RlbCwgcHJvbXB0
KToKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZGF0YV9kaXIsIGRhdGFzZXQsIGYie21vZGVsfV97
cHJvbXB0fV9hbm5vdGF0aW9ucy5qc29ubCIpCiAgICByZWNvcmRzID0gW10KICAgIHdpdGggb3Bl
bihwYXRoKSBhcyBmOgogICAgICAgIGZvciBsaW5lIGluIGY6CiAgICAgICAgICAgIHJlYyA9IGpz
b24ubG9hZHMobGluZS5zdHJpcCgpKQogICAgICAgICAgICByZWNvcmRzLmFwcGVuZCgoaW50KHJl
Y1sndHJ1ZV9sYWJlbCddKSwgaW50KHJlY1sncHJlZGljdGVkX2xhYmVsJ10pKSkKICAgIHJldHVy
biByZWNvcmRzCgoKZGVmIGJ1aWxkX2NvbmZ1c2lvbl9tYXRyaXgocmVjb3JkcywgSyk6CiAgICBj
b3VudHMgPSBucC56ZXJvcygoSywgSykpCiAgICBmb3IgdHJ1ZV9rLCBwcmVkX2sgaW4gcmVjb3Jk
czoKICAgICAgICBpZiAwIDw9IHRydWVfayA8IEsgYW5kIDAgPD0gcHJlZF9rIDwgSzoKICAgICAg
ICAgICAgY291bnRzW3ByZWRfaywgdHJ1ZV9rXSArPSAxCiAgICBjb2xfc3VtcyA9IGNvdW50cy5z
dW0oYXhpcz0wKQogICAgY29sX3N1bXMgPSBucC53aGVyZShjb2xfc3VtcyA8IDEsIDEsIGNvbF9z
dW1zKQogICAgcmV0dXJuIGNvdW50cyAvIGNvbF9zdW1zCgoKZGVmIGxvYWRfYWxsX2NvbmZ1c2lv
bl9tYXRyaWNlcyhkYXRhX2Rpcik6CiAgICBtYXRyaWNlcyA9IHt9CiAgICBmb3IgZGF0YXNldCwg
aW5mbyBpbiBEQVRBU0VUUy5pdGVtcygpOgogICAgICAgIEsgPSBpbmZvW
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "9c12f48a-ea8d-4cdb-a540-2a53340786fa",
  "tool_use_result": {
    "stdout": "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJy\nYXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJp\nY2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMg\nZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBE\nb3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNl\nbnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAg\nMy4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0\naW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmlu\nZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFz\nZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6\nIHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0\naWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczog\nbnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIKCmlt\ncG9ydCBudW1weSBhcyBucAppbXBvcnQganNvbgppbXBvcnQgYXJncGFyc2UKaW1wb3J0IG9zCmlt\ncG9ydCB0aW1lCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0Cgp0cnk6CiAgICBp\nbXBvcnQgbWF0cGxvdGxpYgogICAgbWF0cGxvdGxpYi51c2UoJ0FnZycpCiAgICBpbXBvcnQgbWF0\ncGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBIQVNfTVBMID0gVHJ1ZQpleGNlcHQgSW1wb3J0RXJy\nb3I6CiAgICBIQVNfTVBMID0gRmFsc2UKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIENvbnN0YW50\ncwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT0KCkRBVEFTRVRTID0gT3JkZXJlZERpY3QoWwogICAgKCdj\naXZpbF9jb21tZW50cycsIHsnSyc6IDJ9KSwKICAgICgndmFzdCcsIHsnSyc6IDN9KSwKICAgICgn\naHVtYWlkJywgeydLJzogMTB9KSwKXSkKCk1PREVMUyA9IFsnbGxhbWE0JywgJ3F3ZW4zJywgJ2Rl\nZXBzZWVrJ10KUFJPTVBUUyA9IFsnemVyby1zaG90JywgJ2Zldy1zaG90LTMnLCAnZmV3LXNob3Qt\nNSddCgpUT1BPTE9HSUVTID0gWydjb25mb3VuZGluZycsICdtZWRpYXRpb24nLCAnY29sbGlkZXIn\nLCAnZXhwb3N1cmUnLAogICAgICAgICAgICAgICdtYmlhcycsICdpdicsICdmcm9udGRvb3InXQoK\nTl9QUkVDT01QID0gMl8wMDBfMDAwCgojIFBhcmFtZXRlciBwb29scyDigJQgSz0zIHZhbHVlcyBt\nYXRjaCBwbGFuXzAwMS9wbGFuXzAwNQpfQUxQSEFfUE9PTCA9IFsxLjUsIC0xLjAsIDAuOCwgLTAu\nNSwgMS4yLCAtMC43LCAwLjksIC0wLjQsIDAuNl0KX0JFVEFfQV9QT09MID0gWzEuMCwgLTAuNSwg\nMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0JFVEFfUE9PTCA9IFswLjAs\nIDEuMCwgLTAuNSwgMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0dBTU1B\nX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAuMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1\nLCAwLjFdCl9ERUxUQV9QT09MID0gWzAuMCwgMC44LCAtMC42LCAwLjUsIC0wLjQsIDAuMywgLTAu\nMiwgMC4xNSwgLTAuMSwgMC4wNV0KX0RUX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAu\nMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1LCAwLjFdCl9EWV9QT09MID0gWzAuMCwgMC44LCAwLjYs\nIC0wLjUsIDAuNCwgLTAuMywgMC4yLCAwLjE1LCAtMC4xLCAwLjA1XQoKCiMgPT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PQojIFV0aWxpdHkgRnVuY3Rpb25zCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHNv\nZnRtYXhfcm93cyhsb2dpdHMpOgogICAgZSA9IG5wLmV4cChsb2dpdHMgLSBsb2dpdHMubWF4KGF4\naXM9MSwga2VlcGRpbXM9VHJ1ZSkpCiAgICByZXR1cm4gZSAvIGUuc3VtKGF4aXM9MSwga2VlcGRp\nbXM9VHJ1ZSkKCgpkZWYgc2FtcGxlX2NhdChwcm9icywgcm5nKToKICAgIGN1bSA9IG5wLmN1bXN1\nbShwcm9icywgYXhpcz0xKQogICAgdSA9IHJuZy51bmlmb3JtKHNpemU9cHJvYnMuc2hhcGVbMF0p\nWzosIE5vbmVdCiAgICByZXR1cm4gKHUgPj0gY3VtWzosIDotMV0pLnN1bShheGlzPTEpLmFzdHlw\nZShpbnQpCgoKZGVmIGdlbmVyYXRlX0FzdGFyKEEsIEMsIHJuZyk6CiAgICBwcm9icyA9IENbOiwg\nQV0KICAgIGN1bSA9IG5wLmN1bXN1bShwcm9icywgYXhpcz0wKQogICAgdSA9IHJuZy51bmlmb3Jt\nKHNpemU9bGVuKEEpKQogICAgcmV0dXJuICh1W05vbmUsIDpdID49IGN1bVs6LTFdKS5zdW0oYXhp\ncz0wKS5hc3R5cGUoaW50KQoKCmRlZiBvbHNfd2l0aF9kdW1taWVzKFksIFQsIEFzdGFyLCBLKToK\nICAgIE4gPSBsZW4oWSkKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGsgaW4g\ncmFuZ2UoMSwgSyk6CiAgICAgICAgRFs6LCBrIC0gMV0gPSAoQXN0YXIgPT0gaykuYXN0eXBlKGZs\nb2F0KQogICAgWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAub25lcyhOKSwgVCwgRF0pCiAgICB0cnk6\nCiAgICAgICAgYmV0YSA9IG5wLmxpbmFsZy5sc3RzcShYLCBZLCByY29uZD1Ob25lKVswXQogICAg\nICAgIHJlc2lkID0gWSAtIFggQCBiZXRhCiAgICAgICAgc2lnbWEyID0gbnAuc3VtKHJlc2lkKioy\nKSAvIG1heChOIC0gWC5zaGFwZVsxXSwgMSkKICAgICAgICBYdFhfaW52ID0gbnAubGluYWxnLmlu\ndihYLlQgQCBYKQogICAgICAgIHNlID0gbnAuc3FydChucC5tYXhpbXVtKHNpZ21hMiAqIG5wLmRp\nYWcoWHRYX2ludiksIDApKQogICAgZXhjZXB0IG5wLmxpbmFsZy5MaW5BbGdFcnJvcjoKICAgICAg\nICBiZXRhID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICAgICAgc2UgPSBucC5mdWxs\nKFguc2hhcGVbMV0sIG5wLm5hbikKICAgIHJldHVybiBiZXRhLCBzZQoKCmRlZiBvbHNfbm9fVChZ\nLCBBc3RhciwgSyk6CiAgICBOID0gbGVuKFkpCiAgICBEID0gbnAuemVyb3MoKE4sIEsgLSAxKSkK\nICAgIGZvciBrIGluIHJhbmdlKDEsIEspOgogICAgICAgIERbOiwgayAtIDFdID0gKEFzdGFyID09\nIGspLmFzdHlwZShmbG9hdCkKICAgIFggPSBucC5jb2x1bW5fc3RhY2soW25wLm9uZXMoTiksIERd\nKQogICAgdHJ5OgogICAgICAgIGJldGEgPSBucC5saW5hbGcubHN0c3EoWCwgWSwgcmNvbmQ9Tm9u\nZSlbMF0KICAgICAgICByZXNpZCA9IFkgLSBYIEAgYmV0YQogICAgICAgIHNpZ21hMiA9IG5wLnN1\nbShyZXNpZCoqMikgLyBtYXgoTiAtIFguc2hhcGVbMV0sIDEpCiAgICAgICAgWHRYX2ludiA9IG5w\nLmxpbmFsZy5pbnYoWC5UIEAgWCkKICAgICAgICBzZSA9IG5wLnNxcnQobnAubWF4aW11bShzaWdt\nYTIgKiBucC5kaWFnKFh0WF9pbnYpLCAwKSkKICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJy\nb3I6CiAgICAgICAgYmV0YSA9IG5wLmZ1bGwoWC5zaGFwZVsxXSwgbnAubmFuKQogICAgICAgIHNl\nID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICByZXR1cm4gYmV0YSwgc2UKCgpkZWYg\nd2FsZF9lc3RpbWF0b3IoWiwgWSwgQXN0YXIsIGs9MSk6CiAgICB6MSA9IFogPT0gMTsgejAgPSBa\nID09IDAKICAgIG4xLCBuMCA9IGZsb2F0KHoxLnN1bSgpKSwgZmxvYXQoejAuc3VtKCkpCiAgICBp\nZiBuMSA8IDIgb3IgbjAgPCAyOgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgUkYg\nPSBZW3oxXS5tZWFuKCkgLSBZW3owXS5tZWFuKCkKICAgIHZhcl9SRiA9IFlbejFdLnZhcigpIC8g\nbjEgKyBZW3owXS52YXIoKSAvIG4wCiAgICBEa196MSA9IChBc3Rhclt6MV0gPT0gaykuYXN0eXBl\nKGZsb2F0KS5tZWFuKCkKICAgIERrX3owID0gKEFzdGFyW3owXSA9PSBrKS5hc3R5cGUoZmxvYXQp\nLm1lYW4oKQogICAgRlMgPSBEa196MSAtIERrX3owCiAgICB2YXJfRlMgPSBEa196MSAqICgxIC0g\nRGtfejEpIC8gbjEgKyBEa196MCAqICgxIC0gRGtfejApIC8gbjAKICAgIGlmIGFicyhGUykgPCAx\nZS04OgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgVyA9IFJGIC8gRlMKICAgIHZh\ncl9XID0gdmFyX1JGIC8gRlMqKjIgKyBSRioqMiAqIHZhcl9GUyAvIEZTKio0CiAgICByZXR1cm4g\nVywgbnAuc3FydChtYXgodmFyX1csIDApKQoKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIERHUCBQ\nYXJhbWV0ZXJzIChnZW5lcmFsIEssIEs9MyBtYXRjaGVzIHBsYW5fMDAxL3BsYW5fMDA1KQojID09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT0KCmRlZiBtYWtlX3BfQShLKToKICAgIGlmIEsgPT0gMjoKICAgICAg\nICByZXR1cm4gbnAuYXJyYXkoWzAuNTUsIDAuNDVdKQogICAgZWxpZiBLID09IDM6CiAgICAgICAg\ncmV0dXJuIG5wLmFycmF5KFswLjQwLCAwLjM1LCAwLjI1XSkKICAgIGVsc2U6CiAgICAgICAgcmF3\nID0gbnAuYXJyYXkoWzEuMCAvIChpICsgMSkgZm9yIGkgaW4gcmFuZ2UoSyldKQogICAgICAgIHJl\ndHVybiByYXcgLyByYXcuc3VtKCkKCgpkZWYgbWFrZV9kZ3BfcGFyYW1zKEspOgogICAgcF9BID0g\nbWFrZV9wX0EoSykKICAgIHBhcmFtcyA9IHsKICAgICAgICAnY29uZm91bmRpbmcnOiB7CiAgICAg\nICAgICAgICdwX0EnOiBwX0EsCiAgICAgICAgICAgICdhbHBoYSc6IG5wLmFycmF5KF9BTFBIQV9Q\nT09MWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9BJzogbnAuYXJyYXkoX0JFVEFfQV9QT09M\nWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9UJzogMi4wLAogICAgICAgICAgICAnc2lnbWFf\nVCc6IDEuMCwKICAgICAgICB9LAogICAgICAgICdtZWRpYXRpb24nOiB7CiAgICAgICAgICAgICd0\nYXUnOiAwLjUsCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSks\nCiAgICAgICAgICAgICdkZWx0YSc6IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSksCiAgICAgICAg\nICAgICdiZXRhJzogbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAg\nJ2NvbGxpZGVyJzogewogICAgICAgICAgICAndGF1JzogMS4wLAogICAgICAgICAgICAnZyc6IG5w\nLnplcm9zKEspLAogICAgICAgICAgICAnZFQnOiBucC5hcnJheShfRFRfUE9PTFs6S10pLAogICAg\nICAgICAgICAnZFknOiBucC5hcnJheShfRFlfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAg\nJ2V4cG9zdXJlJzogewogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktd\nKSwKICAgICAgICAgICAgJ3BfQSc6IHBfQSwKICAgICAgICB9LAogICAgfQogICAgaWYgSyA9PSAz\nOgogICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2Rl\nbHRhX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoMyks\nCiAgICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMCwgMC44LCAtMC41XSksCiAgICAgICAg\nICAgICdhX1UyJzogbnAuYXJyYXkoWzAuMCwgMC42LCAwLjldKSwKICAgICAgICB9CiAgICAgICAg\ncGFyYW1zWydpdiddID0gewogICAgICAgICAgICAnbGFtJzogMS4wLCAnYmV0YSc6IG5wLmFycmF5\nKFswLjAsIDAuNSwgLTAuMjVdKSwKICAgICAgICAgICAgJ2cnOiBucC56ZXJvcygzKSwKICAgICAg\nICAgICAgJ2RaJzogbnAuYXJyYXkoWzAuMCwgMS4wLCAtMC41XSksCiAgICAgICAgICAgICdkVSc6\nIG5wLmFycmF5KFswLjAsIDAuOCwgMC42XSksCiAgICAgICAgfQogICAgICAgIHBhcmFtc1snZnJv\nbnRkb29yJ10gPSB7CiAgICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAs\nCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KFswLjAsIDAuNSwgLTAuM10pLAogICAgICAg\nICAgICAnZGVsdGFfZmQnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjhdKSwKICAgICAgICAgICAg\nJ2JldGEnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjVdKSwKICAgICAgICB9CiAgICBlbHNlOgog\nICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2RlbHRh\nX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoSyksCiAg\nICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMF0gKyBbX0FMUEhBX1BPT0xbaV0gKiAwLjYg\nZm9yIGkgaW4gcmFuZ2UoSyAtIDEpXSksCiAgICAgICAgICAgICdhX1UyJzogbnAuYXJyYXkoWzAu\nMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC44IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAogICAg\nICAgIH0KICAgICAgICBpdl9iZXRhID0gbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pICogMC41CiAg\nICAgICAgaXZfYmV0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snaXYnXSA9IHsKICAgICAgICAg\nICAgJ2xhbSc6IDEuMCwgJ2JldGEnOiBpdl9iZXRhLAogICAgICAgICAgICAnZyc6IG5wLnplcm9z\nKEspLAogICAgICAgICAgICAnZFonOiBucC5hcnJheShbMC4wXSArIFtfQUxQSEFfUE9PTFtpXSAq\nIDAuNyBmb3IgaSBpbiByYW5nZShLIC0gMSldKSwKICAgICAgICAgICAgJ2RVJzogbnAuYXJyYXko\nWzAuMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC42IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAog\nICAgICAgIH0KICAgICAgICBmZF9kZWx0YSA9IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSkKICAg\nICAgICBmZF9kZWx0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snZnJvbnRkb29yJ10gPSB7CiAg\nICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAsCiAgICAgICAgICAgICdn\nYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSksCiAgICAgICAgICAgICdkZWx0YV9mZCc6\nIGZkX2RlbHRhLAogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktdKSwK\nICAgICAgICB9CiAgICByZXR1cm4gcGFyYW1zCgoKZGVmIG1ha2VfZGdwX3BhcmFtc19IMChLLCBw\nYXJhbXMpOgogICAgcDAgPSB7fQogICAgZm9yIHRvcG8sIHAgaW4gcGFyYW1zLml0ZW1zKCk6CiAg\nICAgICAgaWYgdG9wbyA9PSAnY29uZm91bmRpbmcnOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRp\nY3QocCwgYmV0YV9UPTAuMCkKICAgICAgICBlbGlmIHRvcG8gPT0gJ21lZGlhdGlvbic6CiAgICAg\nICAgICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAn\nY29sbGlkZXInOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgdGF1PTAuMCkKICAgICAg\nICBlbGlmIHRvcG8gPT0gJ2V4cG9zdXJlJzoKICAgICAgICAgICAgcDBbdG9wb10gPSBkaWN0KHAs\nIGJldGE9bnAuemVyb3MoSykpCiAgICAgICAgZWxpZiB0b3BvID09ICdtYmlhcyc6CiAgICAgICAg\nICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAnaXYn\nOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgYmV0YT1ucC56ZXJvcyhLKSkKICAgICAg\nICBlbGlmIHRvcG8gPT0gJ2Zyb250ZG9vcic6CiAgICAgICAgICAgIHAwW3RvcG9dID0gZGljdChw\nLCBsYW1iZGFfVT0wLjAsIGFscGhhX1U9MC4wLAogICAgICAgICAgICAgICAgICAgICAgICAgICAg\nZGVsdGFfZmQ9bnAuemVyb3MoSyksIGJldGE9bnAuemVyb3MoSykpCiAgICByZXR1cm4gcDAKCgoj\nID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT0KIyBER1AgR2VuZXJhdG9ycyAoZ2VuZXJhbCBLKQojID09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT0KCmRlZiBnZW5fY29uZm91bmRpbmcoSywgTiwgcCwgcm5nKToKICAgIEEg\nPSBybmcuY2hvaWNlKEssIHNpemU9TiwgcD1wWydwX0EnXSkKICAgIEQgPSBucC56ZXJvcygoTiwg\nSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9\nPSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAgVCA9IEQgQCBwWydhbHBoYSddICsgcm5nLm5vcm1h\nbCgwLCBwWydzaWdtYV9UJ10sIE4pCiAgICBZID0gcFsnYmV0YV9UJ10gKiBUICsgRCBAIHBbJ2Jl\ndGFfQSddICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFksIEEKCgpkZWYgZ2Vu\nX21lZGlhdGlvbihLLCBOLCBwLCBybmcpOgogICAgVCA9IHJuZy5iaW5vbWlhbCgxLCAwLjUsIE4p\nLmFzdHlwZShmbG9hdCkKICAgIGxvZ2l0cyA9IHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0\nYSddW05vbmUsIDpdICogVFs6LCBOb25lXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRz\nKQogICAgQSA9IHNhbXBsZV9jYXQocHJvYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAt\nIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9PSBq\nICsgMSkuYXN0eXBlKGZsb2F0KQogICAgWSA9IHBbJ2JldGEnXVswXSArIEQgQCBwWydiZXRhJ11b\nMTpdICsgcFsndGF1J10gKiBUICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFks\nIEEKCgpkZWYgZ2VuX2NvbGxpZGVyKEssIE4sIHAsIHJuZyk6CiAgICBUID0gcm5nLm5vcm1hbCgw\nLCAxLCBOKQogICAgWSA9IHBbJ3RhdSddICogVCArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxv\nZ2l0cyA9IChwWydnJ11bTm9uZSwgOl0gKyBwWydkVCddW05vbmUsIDpdICogVFs6LCBOb25lXQog\nICAgICAgICAgICAgICsgcFsnZFknXVtOb25lLCA6XSAqIFlbOiwgTm9uZV0pCiAgICBwcm9icyA9\nIHNvZnRtYXhfcm93cyhsb2dpdHMpCiAgICBBID0gc2FtcGxlX2NhdChwcm9icywgcm5nKQogICAg\ncmV0dXJuIFQsIFksIEEKCgpkZWYgZ2VuX2V4cG9zdXJlKEssIE4sIHAsIHJuZyk6CiAgICBBID0g\ncm5nLmNob2ljZShLLCBzaXplPU4sIHA9cFsncF9BJ10pCiAgICBEID0gbnAuemVyb3MoKE4sIEsg\nLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEgPT0g\naiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBwWydiZXRhJ11bMF0gKyBEIEAgcFsnYmV0YSdd\nWzE6XSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBOb25lLCBZLCBBCgoKZGVmIGdl\nbl9tYmlhcyhLLCBOLCBwLCBybmcpOgogICAgVTEgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAgICBV\nMiA9IHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIFQgPSBwWydkZWx0YV9jb2VmJ10gKiBVMSArIHJu\nZy5ub3JtYWwoMCwgMSwgTikKICAgIFkgPSBwWyd0YXUnXSAqIFQgKyBwWydsYW0nXSAqIFUyICsg\ncm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtOb25lLCA6XSArIHBbJ2Ff\nVTEnXVtOb25lLCA6XSAqIFUxWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBwWydhX1UyJ11bTm9u\nZSwgOl0gKiBVMls6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxvZ2l0cykKICAg\nIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICByZXR1cm4gVCwgWSwgQQoKCmRlZiBnZW5f\naXYoSywgTiwgcCwgcm5nKToKICAgIFogPSBybmcuYmlub21pYWwoMSwgMC41LCBOKS5hc3R5cGUo\nZmxvYXQpCiAgICBVID0gcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtO\nb25lLCA6XSArIHBbJ2RaJ11bTm9uZSwgOl0gKiBaWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBw\nWydkVSddW05vbmUsIDpdICogVVs6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxv\nZ2l0cykKICAgIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICBEID0gbnAuemVyb3MoKE4s\nIEsgLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEg\nPT0gaiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBEIEAgcFsnYmV0YSddWzE6XSArIHBbJ2xh\nbSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBaLCBZLCBBCgoKZGVmIGdl\nbl9mcm9udGRvb3IoSywgTiwgcCwgcm5nKToKICAgIFUgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAg\nICBUID0gcFsnYWxwaGFfVSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxvZ2l0cyA9\nIHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0YV9mZCddW05vbmUsIDpdICogVFs6LCBOb25l\nXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRzKQogICAgTSA9IHNhbXBsZV9jYXQocHJv\nYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2Uo\nSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoTSA9PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAg\nWSA9IEQgQCBwWydiZXRhJ11bMTpdICsgcFsnbGFtYmRhX1UnXSAqIFUgKyBybmcubm9ybWFsKDAs\nIDEsIE4pCiAgICByZXR1cm4gVCwgWSwgTQoKCkdFTl9GTlMgPSB7CiAgICAnY29uZm91bmRpbmcn\nOiBnZW5fY29uZm91bmRpbmcsICdtZWRpYXRpb24nOiBnZW5fbWVkaWF0aW9uLAogICAgJ2NvbGxp\nZGVyJzogZ2VuX2NvbGxpZGVyLCAnZXhwb3N1cmUnOiBnZW5fZXhwb3N1cmUsCiAgICAnbWJpYXMn\nOiBnZW5fbWJpYXMsICdpdic6IGdlbl9pdiwgJ2Zyb250ZG9vcic6IGdlbl9mcm9udGRvb3IsCn0K\nCgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT0KIyBTdWZmaWNpZW50IFN0YXRpc3RpY3MgJiBQbGltIChn\nZW5lcmFsIEspCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHByZWNvbXB1dGVfc3VmZl9zdGF0\ncyhLLCB0b3BvbG9neSwgcGFyYW1zLCBOPU5fUFJFQ09NUCwgc2VlZD00Mik6CiAgICBybmcgPSBu\ncC5yYW5kb20uZGVmYXVsdF9ybmcoc2VlZCkKICAgIGZpcnN0X3ZhciwgWSwgQSA9IEdFTl9GTlNb\ndG9wb2xvZ3ldKEssIE4sIHBhcmFtcywgcm5nKQogICAgREEgPSBucC56ZXJvcygoTiwgSykpCiAg\nICBmb3IgayBpbiByYW5nZShLKToKICAgICAgICBEQVs6LCBrXSA9IChBID09IGspLmFzdHlwZShm\nbG9hdCkKCiAgICBpZiB0b3BvbG9neSA9PSAnaXYnOgogICAgICAgIFogPSBmaXJzdF92YXIKICAg\nICAgICB6MSA9IFogPT0gMTsgejAgPSBaID09IDAKICAgICAgICBSRiA9IFlbejFdLm1lYW4oKSAt\nIFlbejBdLm1lYW4oKQogICAgICAgIEZTID0gbnAuemVyb3MoSykKICAgICAgICBmb3IgayBpbiBy\nYW5nZShLKToKICAgICAgICAgICAgRlNba10gPSAoQVt6MV0gPT0gaykubWVhbigpIC0gKEFbejBd\nID09IGspLm1lYW4oKQogICAgICAgIHJldHVybiBkaWN0KFJGPVJGLCBGUz1GUywgdG9wb2xvZ3k9\nJ2l2JykKICAgIGVsaWYgdG9wb2xvZ3kgPT0gJ2V4cG9zdXJlJzoKICAgICAgICByZXR1cm4gZGlj\ndChwX0E9REEubWVhbigwKSwgRV9ZPVkubWVhbigpLAogICAgICAgICAgICAgICAgICAgIEVfWUQ9\nKERBICogWVs6LCBOb25lXSkubWVhbigwKSwgdG9wb2xvZ3k9J2V4cG9zdXJlJykKICAgIGVsc2U6\nCiAgICAgICAgVCA9IGZpcnN0X3ZhcgogICAgICAgIHJldHVybiBkaWN0KAogICAgICAgICAgICBw\nX0E9REEubWVhbigwKSwgRV9UPVQubWVhbigpLCBFX1QyPShUKioyKS5tZWFuKCksCiAgICAgICAg\nICAgIEVfWT1ZLm1lYW4oKSwgRV9UWT0oVCAqIFkpLm1lYW4oKSwKICAgICAgICAgICAgRV9URD0o\nREEgKiBUWzosIE5vbmVdKS5tZWFuKDApLAogICAgICAgICAgICBFX1lEPShEQSAqIFlbOiwgTm9u\nZV0pLm1lYW4oMCksIHRvcG9sb2d5PXRvcG9sb2d5KQoKCmRlZiBjb21wdXRlX3BsaW0oQywgc3Qs\nIEspOgogICAgaWYgc3RbJ3RvcG9sb2d5J10gPT0gJ2l2JzoKICAgICAgICBGU19zdGFyID0gQyBA\nIHN0WydGUyddCiAgICAgICAgaWYgYWJzKEZTX3N0YXJbMV0pIDwgMWUtODoKICAgICAgICAgICAg\ncmV0dXJuIG5wLm5hbgogICAgICAgIHJldHVybiBzdFsnUkYnXSAvIEZTX3N0YXJbMV0KICAgIGVs\naWYgc3RbJ3RvcG9sb2d5J10gPT0gJ2V4cG9zdXJlJzoKICAgICAgICBxID0gQyBAIHN0WydwX0En\nXQogICAgICAgIGN5ID0gQyBAIHN0WydFX1lEJ10KICAgICAgICBFWlogPSBucC56ZXJvcygoSywg\nSykpCiAgICAgICAgRVpaWzAsIDBdID0gMS4wCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6\nCiAgICAgICAgICAgIEVaWlswLCBqXSA9IEVaWltqLCAwXSA9IHFbal0KICAgICAgICAgICAgRVpa\nW2osIGpdID0gcVtqXQogICAgICAgIEVaWSA9IG5wLnplcm9zKEspCiAgICAgICAgRVpZWzBdID0g\nc3RbJ0VfWSddCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWVtq\nXSA9IGN5W2pdCiAgICAgICAgdHJ5OgogICAgICAgICAgICByZXR1cm4gbnAubGluYWxnLnNvbHZl\nKEVaWiwgRVpZKQogICAgICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJyb3I6CiAgICAgICAg\nICAgIHJldHVybiBucC5mdWxsKEssIG5wLm5hbikKICAgIGVsc2U6CiAgICAgICAgcSA9IEMgQCBz\ndFsncF9BJ10KICAgICAgICBjdCA9IEMgQCBzdFsnRV9URCddCiAgICAgICAgY3kgPSBDIEAgc3Rb\nJ0VfWUQnXQogICAgICAgIGRpbSA9IEsgKyAxCiAgICAgICAgRVpaID0gbnAuemVyb3MoKGRpbSwg\nZGltKSkKICAgICAgICBFWlpbMCwgMF0gPSAxLjAKICAgICAgICBFWlpbMCwgMV0gPSBFWlpbMSwg\nMF0gPSBzdFsnRV9UJ10KICAgICAgICBFWlpbMSwgMV0gPSBzdFsnRV9UMiddCiAgICAgICAgZm9y\nIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWlswLCBqICsgMV0gPSBFWlpbaiArIDEs\nIDBdID0gcVtqXQogICAgICAgICAgICBFWlpbMSwgaiArIDFdID0gRVpaW2ogKyAxLCAxXSA9IGN0\nW2pdCiAgICAgICAgICAgIEVaWltqICsgMSwgaiArIDFdID0gcVtqXQogICAgICAgIEVaWSA9IG5w\nLnplcm9zKGRpbSkKICAgICAgICBFWllbMF0gPSBzdFsnRV9ZJ10KICAgICAgICBFWllbMV0gPSBz\ndFsnRV9UWSddCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgICAgIEVaWVtq\nICsgMV0gPSBjeVtqXQogICAgICAgIHRyeToKICAgICAgICAgICAgcmV0dXJuIG5wLmxpbmFsZy5z\nb2x2ZShFWlosIEVaWSkKICAgICAgICBleGNlcHQgbnAubGluYWxnLkxpbkFsZ0Vycm9yOgogICAg\nICAgICAgICByZXR1cm4gbnAuZnVsbChkaW0sIG5wLm5hbikKCgpkZWYgZXh0cmFjdF90YXUocGxp\nbV9yZXN1bHQsIHRvcG9sb2d5KToKICAgIGlmIHRvcG9sb2d5ID09ICdpdic6CiAgICAgICAgcmV0\ndXJuIGZsb2F0KHBsaW1fcmVzdWx0KSBpZiBucC5pc2Zpbml0ZShwbGltX3Jlc3VsdCkgZWxzZSBu\ncC5uYW4KICAgIGlmIGlzaW5zdGFuY2UocGxpbV9yZXN1bHQsIG5wLm5kYXJyYXkpOgogICAgICAg\nIHJldHVybiBmbG9hdChwbGltX3Jlc3VsdFsxXSkgaWYgbnAuaXNmaW5pdGUocGxpbV9yZXN1bHRb\nMV0pIGVsc2UgbnAubmFuCiAgICByZXR1cm4gbnAubmFuCgoKIyA9PT09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nCiMgMS4gRGF0YSBMb2FkaW5nICYgQ29uZnVzaW9uIE1hdHJpeAojID09PT09PT09PT09PT09PT09\nPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09\nPT0KCmRlZiBsb2FkX2Fubm90YXRpb25zKGRhdGFfZGlyLCBkYXRhc2V0LCBtb2RlbCwgcHJvbXB0\nKToKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4oZGF0YV9kaXIsIGRhdGFzZXQsIGYie21vZGVsfV97\ncHJvbXB0fV9hbm5vdGF0aW9ucy5qc29ubCIpCiAgICByZWNvcmRzID0gW10KICAgIHdpdGggb3Bl\nbihwYXRoKSBhcyBmOgogICAgICAgIGZvciBsaW5lIGluIGY6CiAgICAgICAgICAgIHJlYyA9IGpz\nb24ubG9hZHMobGluZS5zdHJpcCgpKQogICAgICAgICAgICByZWNvcmRzLmFwcGVuZCgoaW50KHJl\nY1sndHJ1ZV9sYWJlbCddKSwgaW50KHJlY1sncHJlZGljdGVkX2xhYmVsJ10pKSkKICAgIHJldHVy\nbiByZWNvcmRzCgoKZGVmIGJ1aWxkX2NvbmZ1c2lvbl9tYXRyaXgocmVjb3JkcywgSyk6CiAgICBj\nb3VudHMgPSBucC56ZXJvcygoSywgSykpCiAgICBmb3IgdHJ1ZV9rLCBwcmVkX2sgaW4gcmVjb3Jk\nczoKICAgICAgICBpZiAwIDw9IHRydWVfayA8IEsgYW5kIDAgPD0gcHJlZF9rIDwgSzoKICAgICAg\nICAgICAgY291bnRzW3ByZWRfaywgdHJ1ZV9rXSArPSAxCiAgICBjb2xfc3VtcyA9IGNvdW50cy5z\ndW0oYXhpcz0wKQogICAgY29sX3N1bXMgPSBucC53aGVyZShjb2xfc3VtcyA8IDEsIDEsIGNvbF9z\ndW1zKQogICAgcmV0dXJuIGNvdW50cyAvIGNvbF9zdW1zCgoKZGVmIGxvYWRfYWxsX2NvbmZ1c2lv\nbl9tYXRyaWNlcyhkYXRhX2Rpcik6CiAgICBtYXRyaWNlcyA9IHt9CiAgICBmb3IgZGF0YXNldCwg\naW5mbyBpbiBEQVRBU0VUUy5pdGVtcygpOgogICAgICAgIEsgPSBpbmZvW",
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

_source line 85_

The base64 is ~50KB. Let me use a more efficient transfer: write it to a temp file on the server using ssh_execute with Python.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "ff1d7b19-d757-4d4e-96d7-8367c370eec6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLpQTtidF5UqsK4jfsussP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16054,
      "cache_read_input_tokens": 48776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16054
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

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_013ZrysPmJvLwYMLbStpu7cA`</summary>

```json
{
  "command": "base64 -w0 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py > /tmp/plan006_b64.txt && wc -c /tmp/plan006_b64.txt",
  "description": "Create single-line base64 file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "28ed05bf-7047-4ee3-8909-ec587517b340",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLpQTtidF5UqsK4jfsussP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16054,
      "cache_read_input_tokens": 48776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16054
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


### Tool result

_source line 87 · 2026-05-20T21:25:47.935Z_

<details><summary>↩ Tool result · `toolu_013ZrysPmJvLwYMLbStpu7cA`</summary>

```text
51052 /tmp/plan006_b64.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "19c71917-88e2-4889-8f49-e8164a8b43d0",
  "tool_use_result": {
    "stdout": "51052 /tmp/plan006_b64.txt",
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

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_01WJLr1WF25GJKMxGT3ZSHtH`</summary>

```json
{
  "command": "head -c 25000 /tmp/plan006_b64.txt",
  "description": "Get first half of base64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "c7f3c0e0-fb5d-40ab-b533-aa46b2f266bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkmjJH3e1erKKGvA3eR3Q4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 64830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
      },
      "output_tokens": 63,
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

_source line 89 · 2026-05-20T21:25:51.342Z_

<details><summary>↩ Tool result · `toolu_01WJLr1WF25GJKMxGT3ZSHtH`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "436b1766-f68f-499c-938f-0d08d9008296",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
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

_source line 90_

Let me use a different approach — write the file in chunks via ssh_execute using Python's base64 module.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b458d6f0-b383-47a8-b7a3-c60945cd317f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCKFVJUBEdmeGmUJFZMzJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19758,
      "cache_read_input_tokens": 65140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19758
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

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dvsmev1eEDG7sS1fJV6HNB`</summary>

```json
{
  "command": "split -b 15000 /tmp/plan006_b64.txt /tmp/plan006_chunk_ && ls -la /tmp/plan006_chunk_*",
  "description": "Split base64 into chunks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "7dcece9f-fa99-4a9d-ad0d-c80f8b07a748",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCKFVJUBEdmeGmUJFZMzJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19758,
      "cache_read_input_tokens": 65140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19758
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


### Tool result

_source line 92 · 2026-05-20T21:25:57.935Z_

<details><summary>↩ Tool result · `toolu_01Dvsmev1eEDG7sS1fJV6HNB`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 15000 May 20 21:25 /tmp/plan006_chunk_aa
-rw-r--r-- 1 ubuntu ubuntu 15000 May 20 21:25 /tmp/plan006_chunk_ab
-rw-r--r-- 1 ubuntu ubuntu 15000 May 20 21:25 /tmp/plan006_chunk_ac
-rw-r--r-- 1 ubuntu ubuntu  6052 May 20 21:25 /tmp/plan006_chunk_ad
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "fb675f91-0519-4159-8295-a551cc5c5675",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 15000 May 20 21:25 /tmp/plan006_chunk_aa\n-rw-r--r-- 1 ubuntu ubuntu 15000 May 20 21:25 /tmp/plan006_chunk_ab\n-rw-r--r-- 1 ubuntu ubuntu 15000 May 20 21:25 /tmp/plan006_chunk_ac\n-rw-r--r-- 1 ubuntu ubuntu  6052 May 20 21:25 /tmp/plan006_chunk_ad",
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

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01L4Lzu7PTktKHBKJjaWACYc`</summary>

```json
{
  "command": "cat /tmp/plan006_chunk_aa",
  "description": "Read chunk aa"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b703fc96-f4b4-45fb-94ae-f8f112c6b674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019taK7PQ5kCknEtm8emuHyv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 84898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
      },
      "output_tokens": 58,
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

_source line 94 · 2026-05-20T21:26:01.156Z_

<details><summary>↩ Tool result · `toolu_01L4Lzu7PTktKHBKJjaWACYc`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "e8aa795b-6951-4a5c-b670-88e1c3a87ef1",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
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

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
The chunks are too large to pass via ssh_execute. Let me try a different approach: use ssh_execute to write the file using Python with base64 encoded chunks, but write each chunk one at a time to the server.

Actually, the simplest approach would be to just use ssh_execute with a cat heredoc or echo commands. But the script is ~38KB raw text, which might be too big for a single ssh command.

Let me try splitting into 4 chunks and writing via ssh_execute using Python base64 decode.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "aa65f1b1-e265-457c-9a0f-6f4b7ddcc37b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PK9L6BJN8BcJqXqGPJLk5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11955,
      "cache_read_input_tokens": 85185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11955
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

_source line 96_

Let me write the file directly via ssh_execute using Python's base64:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "463c1441-93a1-4f8b-a269-16a6bd730d30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PK9L6BJN8BcJqXqGPJLk5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11955,
      "cache_read_input_tokens": 85185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11955
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01Viicv1xs9VZj6wQygjg4ZS`</summary>

```json
{
  "command": "cat /tmp/plan006_chunk_aa | tr -d '\\n'",
  "description": "Get chunk aa as single line"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "ccfaa894-3258-4cc5-95c1-010471a7ce55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PK9L6BJN8BcJqXqGPJLk5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11955,
      "cache_read_input_tokens": 85185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11955
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

_source line 98 · 2026-05-20T21:26:11.939Z_

<details><summary>↩ Tool result · `toolu_01Viicv1xs9VZj6wQygjg4ZS`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b20edeb0-be8e-4089-908c-b8bd7fe7cdf1",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
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

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
This approach of reading chunks and passing them to ssh_execute is going to be very tedious. Let me try a different, more efficient approach: use ssh_execute with Python's base64 decode, writing the content directly. I need to pass the base64 data as part of the command.

Actually, let me just use a Python one-liner on the server to write the file, passing the base64 via stdin-like approach. The problem is ssh_execute takes a command string, and the base64 is ~51KB.

Let me try writing via ssh_execute with echo and appending:
- chunk 1: echo "b64_chunk_1" > /tmp/plan006.b64


- chunk 2: echo "b64_chunk_2" >> /tmp/plan006.b64
- ... etc
- Then: base64 -d /tmp/plan006.b64 > /path/to/plan006.py

But each chunk is 15K chars of base64, which should be fine for a command string. Actually, I can just send the whole base64 in one command since it's only 51KB total, which should work fine for a shell command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "655b5af6-e002-4ab2-a08a-b280845db6cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jvk1EScxXRBz2cdRB8YEx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12113,
      "cache_read_input_tokens": 97140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12113
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

_source line 100_

Let me write the file to the server directly. I'll send the base64 in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b341e2d3-138b-46bb-aff7-af80c69e5612",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jvk1EScxXRBz2cdRB8YEx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12113,
      "cache_read_input_tokens": 97140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12113
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

_source line 101_

<details open><summary>🔧 Tool call — Bash · `toolu_01NoUApcLGnUBxDETw2ikZxM`</summary>

```json
{
  "command": "cat /tmp/plan006_chunk_aa /tmp/plan006_chunk_ab /tmp/plan006_chunk_ac /tmp/plan006_chunk_ad > /tmp/plan006_full_b64.txt && wc -c /tmp/plan006_full_b64.txt",
  "description": "Combine base64 chunks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "ea679685-499a-40e5-a34c-e9edb5deb4b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jvk1EScxXRBz2cdRB8YEx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12113,
      "cache_read_input_tokens": 97140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12113
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

_source line 102 · 2026-05-20T21:26:23.783Z_

<details><summary>↩ Tool result · `toolu_01NoUApcLGnUBxDETw2ikZxM`</summary>

```text
51052 /tmp/plan006_full_b64.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "45be5660-6e07-4b28-8956-fc862c2524e8",
  "tool_use_result": {
    "stdout": "51052 /tmp/plan006_full_b64.txt",
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

_source line 103_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016AFevcMcoG1JyDjDik74NX`</summary>

```json
{
  "server": "home-1x5090",
  "command": "python3 -c \"\nimport base64, sys\nb64 = '''IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJyYXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJpY2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMgZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBEb3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNlbnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAgMy4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0aW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmluZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFzZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6IHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0aWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczogbnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIK'''\n# just test first chunk works\ndecoded = base64.b64decode(b64)\nprint(f'Decoded {len(decoded)} bytes, first line: {decoded[:40]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "17929ae2-74ee-464e-8900-cba38b4edb74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wx6tNjybYa3UHv6GYVFmpX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 109253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
      },
      "output_tokens": 38,
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

_source line 104 · 2026-05-20T21:26:55.381Z_

<details><summary>↩ Tool result · `toolu_016AFevcMcoG1JyDjDik74NX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Decoded 738 bytes, first line: b'#!/usr/bin/env python3\\\\n\\\"\\\"\\\"\\\\nplan_006: Emp'\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5a95fdff-8344-4df3-b746-0205766abecc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Decoded 738 bytes, first line: b'#!/usr/bin/env python3\\\\\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\nplan_006: Emp'\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.74}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Decoded 738 bytes, first line: b'#!/usr/bin/env python3\\\\n\\\"\\\"\\\"\\\\nplan_006: Emp'\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
OK, the ssh_execute approach works for passing Python code with base64 data. But the full base64 string is 51KB which is too long to embed in a single Python one-liner via ssh_execute.

Let me try a different approach: use ssh_execute to write the base64 file to the server in chunks, then decode it.

Actually, let me try a simpler approach: just read the local file and pass it via ssh_execute's command string. Let me write it as a Python script that takes the b64 chunks and writes them out.

Alternatively, I could try to transfer using multiple ssh_execute calls that each echo a chunk to a file.


Actually, 51KB should fit fine as a single command argument for most SSH servers, so let me just try passing the entire base64 string in one echo command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "8aa6bc1c-f53b-48c2-835f-e1392c57973e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTzGGwUWFeAtf7dMCRxbHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 109717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
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

_source line 106_

<details open><summary>🔧 Tool call — Bash · `toolu_015G7nfCYLuR4Y2GTiTFfR7c`</summary>

```json
{
  "command": "B64=$(cat /tmp/plan006_full_b64.txt | tr -d '\\n') && echo \"Length: ${#B64}\"",
  "description": "Prepare full base64 string"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "15dc2526-75ce-4488-bcb0-2529acbf71b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTzGGwUWFeAtf7dMCRxbHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 109717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
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

_source line 107 · 2026-05-20T21:27:03.238Z_

<details><summary>↩ Tool result · `toolu_015G7nfCYLuR4Y2GTiTFfR7c`</summary>

```text
Length: 51052
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "6c05ff5a-8fee-4a98-9474-43b9e62d7e03",
  "tool_use_result": {
    "stdout": "Length: 51052",
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

_source line 108_

I'll write the file to the server in 4 chunks then decode.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "b08bf443-640c-42db-acce-c8fbc5a98b85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122K4JF2Mv8v262oZ6WRfJB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 110847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 419
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

_source line 109_

<details open><summary>🔧 Tool call — Bash · `toolu_013a4K9b3WfrcuNrdkn8yyhw`</summary>

```json
{
  "command": "cat /tmp/plan006_chunk_aa | tr -d '\\n' | wc -c",
  "description": "Check chunk size for SSH"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "7de8e3ca-f210-4aaa-a630-2e4c11297c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122K4JF2Mv8v262oZ6WRfJB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 110847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 419
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


### Tool result

_source line 110 · 2026-05-20T21:27:07.128Z_

<details><summary>↩ Tool result · `toolu_013a4K9b3WfrcuNrdkn8yyhw`</summary>

```text
15000
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "3ceb2830-167b-4920-a156-81f38edc1234",
  "tool_use_result": {
    "stdout": "15000",
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

_source line 111_

<details open><summary>🔧 Tool call — Bash · `toolu_01RZQ6jGo2DdMKW6xZJRy6gM`</summary>

```json
{
  "command": "CHUNK_AA=$(cat /tmp/plan006_chunk_aa | tr -d '\\n') && echo \"chunk_aa ready: ${#CHUNK_AA} chars\"",
  "description": "Load chunk aa into variable"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "3160ba22-37eb-4d34-940a-b353ec733792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSTZsBa4KvLPfw5S4LMWw7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 125,
      "cache_read_input_tokens": 111266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 125
      },
      "output_tokens": 55,
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

_source line 112 · 2026-05-20T21:27:10.876Z_

<details><summary>↩ Tool result · `toolu_01RZQ6jGo2DdMKW6xZJRy6gM`</summary>

```text
chunk_aa ready: 15000 chars
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "1740f1f9-f54d-4a48-9676-dbaab045a026",
  "tool_use_result": {
    "stdout": "chunk_aa ready: 15000 chars",
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

_source line 113_

<details><summary>Logged reasoning block</summary>

```text
Actually, the issue is that the MCP tool takes a command string, and I need to embed the b64 data in that string. The chunks are 15KB each, which should be fine. Let me try writing each chunk via echo to a file on the server, then base64 decode the result.

But I can't use bash variables across tool calls. Let me read the chunks from local files and construct the ssh_execute commands.

Actually, I realize I can write a Python script locally that reads the base64 file and creates the ssh commands. But the simplest approach is to just pass each chunk directly.
 
I think the most straightforward way is to use printf commands to write the base64 chunks sequentially to a temp file on the server, appending each one, then decode the complete file once all chunks are written. Writing shell commands...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "86a4f474-3be7-46f9-b87e-fef3b1082d1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191CYcqavUaWEcMig5Bfkab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 111391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
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

_source line 114_

Let me transfer the file using a more practical approach — write the base64 data to the server in chunks, then decode.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "fb8bfe31-8095-475e-b5d3-8707d42f1d62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191CYcqavUaWEcMig5Bfkab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 111391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
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

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01HW8HFtGANqbCsajEEuBhiF`</summary>

```json
{
  "file_path": "/tmp/plan006_chunk_aa"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "df0ebbda-8b21-4b7d-b467-d3de98f0de89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191CYcqavUaWEcMig5Bfkab",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 111391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
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

_source line 116 · 2026-05-20T21:27:25.530Z_

<details><summary>↩ Tool result · `toolu_01HW8HFtGANqbCsajEEuBhiF`</summary>

```text
1	IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJyYXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJpY2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMgZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBEb3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNlbnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAgMy4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0aW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmluZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFzZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6IHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0aWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczogbnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIKCmltcG9ydCBudW1weSBhcyBucAppbXBvcnQganNvbgppbXBvcnQgYXJncGFyc2UKaW1wb3J0IG9zCmltcG9ydCB0aW1lCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IE9yZGVyZWREaWN0Cgp0cnk6CiAgICBpbXBvcnQgbWF0cGxvdGxpYgogICAgbWF0cGxvdGxpYi51c2UoJ0FnZycpCiAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBIQVNfTVBMID0gVHJ1ZQpleGNlcHQgSW1wb3J0RXJyb3I6CiAgICBIQVNfTVBMID0gRmFsc2UKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIENvbnN0YW50cwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KCkRBVEFTRVRTID0gT3JkZXJlZERpY3QoWwogICAgKCdjaXZpbF9jb21tZW50cycsIHsnSyc6IDJ9KSwKICAgICgndmFzdCcsIHsnSyc6IDN9KSwKICAgICgnaHVtYWlkJywgeydLJzogMTB9KSwKXSkKCk1PREVMUyA9IFsnbGxhbWE0JywgJ3F3ZW4zJywgJ2RlZXBzZWVrJ10KUFJPTVBUUyA9IFsnemVyby1zaG90JywgJ2Zldy1zaG90LTMnLCAnZmV3LXNob3QtNSddCgpUT1BPTE9HSUVTID0gWydjb25mb3VuZGluZycsICdtZWRpYXRpb24nLCAnY29sbGlkZXInLCAnZXhwb3N1cmUnLAogICAgICAgICAgICAgICdtYmlhcycsICdpdicsICdmcm9udGRvb3InXQoKTl9QUkVDT01QID0gMl8wMDBfMDAwCgojIFBhcmFtZXRlciBwb29scyDigJQgSz0zIHZhbHVlcyBtYXRjaCBwbGFuXzAwMS9wbGFuXzAwNQpfQUxQSEFfUE9PTCA9IFsxLjUsIC0xLjAsIDAuOCwgLTAuNSwgMS4yLCAtMC43LCAwLjksIC0wLjQsIDAuNl0KX0JFVEFfQV9QT09MID0gWzEuMCwgLTAuNSwgMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0JFVEFfUE9PTCA9IFswLjAsIDEuMCwgLTAuNSwgMC43LCAtMC4zLCAwLjUsIC0wLjIsIDAuNCwgLTAuMTUsIDAuM10KX0dBTU1BX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAuMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1LCAwLjFdCl9ERUxUQV9QT09MID0gWzAuMCwgMC44LCAtMC42LCAwLjUsIC0wLjQsIDAuMywgLTAuMiwgMC4xNSwgLTAuMSwgMC4wNV0KX0RUX1BPT0wgPSBbMC4wLCAwLjUsIC0wLjMsIDAuNCwgLTAuMiwgMC4zLCAtMC4xLCAwLjIsIC0wLjA1LCAwLjFdCl9EWV9QT09MID0gWzAuMCwgMC44LCAwLjYsIC0wLjUsIDAuNCwgLTAuMywgMC4yLCAwLjE1LCAtMC4xLCAwLjA1XQoKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIFV0aWxpdHkgRnVuY3Rpb25zCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHNvZnRtYXhfcm93cyhsb2dpdHMpOgogICAgZSA9IG5wLmV4cChsb2dpdHMgLSBsb2dpdHMubWF4KGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSkpCiAgICByZXR1cm4gZSAvIGUuc3VtKGF4aXM9MSwga2VlcGRpbXM9VHJ1ZSkKCgpkZWYgc2FtcGxlX2NhdChwcm9icywgcm5nKToKICAgIGN1bSA9IG5wLmN1bXN1bShwcm9icywgYXhpcz0xKQogICAgdSA9IHJuZy51bmlmb3JtKHNpemU9cHJvYnMuc2hhcGVbMF0pWzosIE5vbmVdCiAgICByZXR1cm4gKHUgPj0gY3VtWzosIDotMV0pLnN1bShheGlzPTEpLmFzdHlwZShpbnQpCgoKZGVmIGdlbmVyYXRlX0FzdGFyKEEsIEMsIHJuZyk6CiAgICBwcm9icyA9IENbOiwgQV0KICAgIGN1bSA9IG5wLmN1bXN1bShwcm9icywgYXhpcz0wKQogICAgdSA9IHJuZy51bmlmb3JtKHNpemU9bGVuKEEpKQogICAgcmV0dXJuICh1W05vbmUsIDpdID49IGN1bVs6LTFdKS5zdW0oYXhpcz0wKS5hc3R5cGUoaW50KQoKCmRlZiBvbHNfd2l0aF9kdW1taWVzKFksIFQsIEFzdGFyLCBLKToKICAgIE4gPSBsZW4oWSkKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGsgaW4gcmFuZ2UoMSwgSyk6CiAgICAgICAgRFs6LCBrIC0gMV0gPSAoQXN0YXIgPT0gaykuYXN0eXBlKGZsb2F0KQogICAgWCA9IG5wLmNvbHVtbl9zdGFjayhbbnAub25lcyhOKSwgVCwgRF0pCiAgICB0cnk6CiAgICAgICAgYmV0YSA9IG5wLmxpbmFsZy5sc3RzcShYLCBZLCByY29uZD1Ob25lKVswXQogICAgICAgIHJlc2lkID0gWSAtIFggQCBiZXRhCiAgICAgICAgc2lnbWEyID0gbnAuc3VtKHJlc2lkKioyKSAvIG1heChOIC0gWC5zaGFwZVsxXSwgMSkKICAgICAgICBYdFhfaW52ID0gbnAubGluYWxnLmludihYLlQgQCBYKQogICAgICAgIHNlID0gbnAuc3FydChucC5tYXhpbXVtKHNpZ21hMiAqIG5wLmRpYWcoWHRYX2ludiksIDApKQogICAgZXhjZXB0IG5wLmxpbmFsZy5MaW5BbGdFcnJvcjoKICAgICAgICBiZXRhID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICAgICAgc2UgPSBucC5mdWxsKFguc2hhcGVbMV0sIG5wLm5hbikKICAgIHJldHVybiBiZXRhLCBzZQoKCmRlZiBvbHNfbm9fVChZLCBBc3RhciwgSyk6CiAgICBOID0gbGVuKFkpCiAgICBEID0gbnAuemVyb3MoKE4sIEsgLSAxKSkKICAgIGZvciBrIGluIHJhbmdlKDEsIEspOgogICAgICAgIERbOiwgayAtIDFdID0gKEFzdGFyID09IGspLmFzdHlwZShmbG9hdCkKICAgIFggPSBucC5jb2x1bW5fc3RhY2soW25wLm9uZXMoTiksIERdKQogICAgdHJ5OgogICAgICAgIGJldGEgPSBucC5saW5hbGcubHN0c3EoWCwgWSwgcmNvbmQ9Tm9uZSlbMF0KICAgICAgICByZXNpZCA9IFkgLSBYIEAgYmV0YQogICAgICAgIHNpZ21hMiA9IG5wLnN1bShyZXNpZCoqMikgLyBtYXgoTiAtIFguc2hhcGVbMV0sIDEpCiAgICAgICAgWHRYX2ludiA9IG5wLmxpbmFsZy5pbnYoWC5UIEAgWCkKICAgICAgICBzZSA9IG5wLnNxcnQobnAubWF4aW11bShzaWdtYTIgKiBucC5kaWFnKFh0WF9pbnYpLCAwKSkKICAgIGV4Y2VwdCBucC5saW5hbGcuTGluQWxnRXJyb3I6CiAgICAgICAgYmV0YSA9IG5wLmZ1bGwoWC5zaGFwZVsxXSwgbnAubmFuKQogICAgICAgIHNlID0gbnAuZnVsbChYLnNoYXBlWzFdLCBucC5uYW4pCiAgICByZXR1cm4gYmV0YSwgc2UKCgpkZWYgd2FsZF9lc3RpbWF0b3IoWiwgWSwgQXN0YXIsIGs9MSk6CiAgICB6MSA9IFogPT0gMTsgejAgPSBaID09IDAKICAgIG4xLCBuMCA9IGZsb2F0KHoxLnN1bSgpKSwgZmxvYXQoejAuc3VtKCkpCiAgICBpZiBuMSA8IDIgb3IgbjAgPCAyOgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgUkYgPSBZW3oxXS5tZWFuKCkgLSBZW3owXS5tZWFuKCkKICAgIHZhcl9SRiA9IFlbejFdLnZhcigpIC8gbjEgKyBZW3owXS52YXIoKSAvIG4wCiAgICBEa196MSA9IChBc3Rhclt6MV0gPT0gaykuYXN0eXBlKGZsb2F0KS5tZWFuKCkKICAgIERrX3owID0gKEFzdGFyW3owXSA9PSBrKS5hc3R5cGUoZmxvYXQpLm1lYW4oKQogICAgRlMgPSBEa196MSAtIERrX3owCiAgICB2YXJfRlMgPSBEa196MSAqICgxIC0gRGtfejEpIC8gbjEgKyBEa196MCAqICgxIC0gRGtfejApIC8gbjAKICAgIGlmIGFicyhGUykgPCAxZS04OgogICAgICAgIHJldHVybiBucC5uYW4sIG5wLm5hbgogICAgVyA9IFJGIC8gRlMKICAgIHZhcl9XID0gdmFyX1JGIC8gRlMqKjIgKyBSRioqMiAqIHZhcl9GUyAvIEZTKio0CiAgICByZXR1cm4gVywgbnAuc3FydChtYXgodmFyX1csIDApKQoKCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQojIERHUCBQYXJhbWV0ZXJzIChnZW5lcmFsIEssIEs9MyBtYXRjaGVzIHBsYW5fMDAxL3BsYW5fMDA1KQojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KCmRlZiBtYWtlX3BfQShLKToKICAgIGlmIEsgPT0gMjoKICAgICAgICByZXR1cm4gbnAuYXJyYXkoWzAuNTUsIDAuNDVdKQogICAgZWxpZiBLID09IDM6CiAgICAgICAgcmV0dXJuIG5wLmFycmF5KFswLjQwLCAwLjM1LCAwLjI1XSkKICAgIGVsc2U6CiAgICAgICAgcmF3ID0gbnAuYXJyYXkoWzEuMCAvIChpICsgMSkgZm9yIGkgaW4gcmFuZ2UoSyldKQogICAgICAgIHJldHVybiByYXcgLyByYXcuc3VtKCkKCgpkZWYgbWFrZV9kZ3BfcGFyYW1zKEspOgogICAgcF9BID0gbWFrZV9wX0EoSykKICAgIHBhcmFtcyA9IHsKICAgICAgICAnY29uZm91bmRpbmcnOiB7CiAgICAgICAgICAgICdwX0EnOiBwX0EsCiAgICAgICAgICAgICdhbHBoYSc6IG5wLmFycmF5KF9BTFBIQV9QT09MWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9BJzogbnAuYXJyYXkoX0JFVEFfQV9QT09MWzpLIC0gMV0pLAogICAgICAgICAgICAnYmV0YV9UJzogMi4wLAogICAgICAgICAgICAnc2lnbWFfVCc6IDEuMCwKICAgICAgICB9LAogICAgICAgICdtZWRpYXRpb24nOiB7CiAgICAgICAgICAgICd0YXUnOiAwLjUsCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSksCiAgICAgICAgICAgICdkZWx0YSc6IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSksCiAgICAgICAgICAgICdiZXRhJzogbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAgJ2NvbGxpZGVyJzogewogICAgICAgICAgICAndGF1JzogMS4wLAogICAgICAgICAgICAnZyc6IG5wLnplcm9zKEspLAogICAgICAgICAgICAnZFQnOiBucC5hcnJheShfRFRfUE9PTFs6S10pLAogICAgICAgICAgICAnZFknOiBucC5hcnJheShfRFlfUE9PTFs6S10pLAogICAgICAgIH0sCiAgICAgICAgJ2V4cG9zdXJlJzogewogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktdKSwKICAgICAgICAgICAgJ3BfQSc6IHBfQSwKICAgICAgICB9LAogICAgfQogICAgaWYgSyA9PSAzOgogICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2RlbHRhX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoMyksCiAgICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMCwgMC44LCAtMC41XSksCiAgICAgICAgICAgICdhX1UyJzogbnAuYXJyYXkoWzAuMCwgMC42LCAwLjldKSwKICAgICAgICB9CiAgICAgICAgcGFyYW1zWydpdiddID0gewogICAgICAgICAgICAnbGFtJzogMS4wLCAnYmV0YSc6IG5wLmFycmF5KFswLjAsIDAuNSwgLTAuMjVdKSwKICAgICAgICAgICAgJ2cnOiBucC56ZXJvcygzKSwKICAgICAgICAgICAgJ2RaJzogbnAuYXJyYXkoWzAuMCwgMS4wLCAtMC41XSksCiAgICAgICAgICAgICdkVSc6IG5wLmFycmF5KFswLjAsIDAuOCwgMC42XSksCiAgICAgICAgfQogICAgICAgIHBhcmFtc1snZnJvbnRkb29yJ10gPSB7CiAgICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAsCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KFswLjAsIDAuNSwgLTAuM10pLAogICAgICAgICAgICAnZGVsdGFfZmQnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjhdKSwKICAgICAgICAgICAgJ2JldGEnOiBucC5hcnJheShbMC4wLCAxLjAsIC0wLjVdKSwKICAgICAgICB9CiAgICBlbHNlOgogICAgICAgIHBhcmFtc1snbWJpYXMnXSA9IHsKICAgICAgICAgICAgJ3RhdSc6IDAuNSwgJ2RlbHRhX2NvZWYnOiAxLjAsICdsYW0nOiAxLjAsCiAgICAgICAgICAgICdnJzogbnAuemVyb3MoSyksCiAgICAgICAgICAgICdhX1UxJzogbnAuYXJyYXkoWzAuMF0gKyBbX0FMUEhBX1BPT0xbaV0gKiAwLjYgZm9yIGkgaW4gcmFuZ2UoSyAtIDEpXSksCiAgICAgICAgICAgICdhX1UyJzogbnAuYXJyYXkoWzAuMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC44IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAogICAgICAgIH0KICAgICAgICBpdl9iZXRhID0gbnAuYXJyYXkoX0JFVEFfUE9PTFs6S10pICogMC41CiAgICAgICAgaXZfYmV0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snaXYnXSA9IHsKICAgICAgICAgICAgJ2xhbSc6IDEuMCwgJ2JldGEnOiBpdl9iZXRhLAogICAgICAgICAgICAnZyc6IG5wLnplcm9zKEspLAogICAgICAgICAgICAnZFonOiBucC5hcnJheShbMC4wXSArIFtfQUxQSEFfUE9PTFtpXSAqIDAuNyBmb3IgaSBpbiByYW5nZShLIC0gMSldKSwKICAgICAgICAgICAgJ2RVJzogbnAuYXJyYXkoWzAuMF0gKyBbX0JFVEFfQV9QT09MW2ldICogMC42IGZvciBpIGluIHJhbmdlKEsgLSAxKV0pLAogICAgICAgIH0KICAgICAgICBmZF9kZWx0YSA9IG5wLmFycmF5KF9ERUxUQV9QT09MWzpLXSkKICAgICAgICBmZF9kZWx0YVswXSA9IDAuMAogICAgICAgIHBhcmFtc1snZnJvbnRkb29yJ10gPSB7CiAgICAgICAgICAgICdhbHBoYV9VJzogMS4wLCAnbGFtYmRhX1UnOiAxLjAsCiAgICAgICAgICAgICdnYW1tYSc6IG5wLmFycmF5KF9HQU1NQV9QT09MWzpLXSksCiAgICAgICAgICAgICdkZWx0YV9mZCc6IGZkX2RlbHRhLAogICAgICAgICAgICAnYmV0YSc6IG5wLmFycmF5KF9CRVRBX1BPT0xbOktdKSwKICAgICAgICB9CiAgICByZXR1cm4gcGFyYW1zCgoKZGVmIG1ha2VfZGdwX3BhcmFtc19IMChLLCBwYXJhbXMpOgogICAgcDAgPSB7fQogICAgZm9yIHRvcG8sIHAgaW4gcGFyYW1zLml0ZW1zKCk6CiAgICAgICAgaWYgdG9wbyA9PSAnY29uZm91bmRpbmcnOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgYmV0YV9UPTAuMCkKICAgICAgICBlbGlmIHRvcG8gPT0gJ21lZGlhdGlvbic6CiAgICAgICAgICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAnY29sbGlkZXInOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgdGF1PTAuMCkKICAgICAgICBlbGlmIHRvcG8gPT0gJ2V4cG9zdXJlJzoKICAgICAgICAgICAgcDBbdG9wb10gPSBkaWN0KHAsIGJldGE9bnAuemVyb3MoSykpCiAgICAgICAgZWxpZiB0b3BvID09ICdtYmlhcyc6CiAgICAgICAgICAgIHAwW3RvcG9dID0gZGljdChwLCB0YXU9MC4wKQogICAgICAgIGVsaWYgdG9wbyA9PSAnaXYnOgogICAgICAgICAgICBwMFt0b3BvXSA9IGRpY3QocCwgYmV0YT1ucC56ZXJvcyhLKSkKICAgICAgICBlbGlmIHRvcG8gPT0gJ2Zyb250ZG9vcic6CiAgICAgICAgICAgIHAwW3RvcG9dID0gZGljdChwLCBsYW1iZGFfVT0wLjAsIGFscGhhX1U9MC4wLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgZGVsdGFfZmQ9bnAuemVyb3MoSyksIGJldGE9bnAuemVyb3MoSykpCiAgICByZXR1cm4gcDAKCgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBER1AgR2VuZXJhdG9ycyAoZ2VuZXJhbCBLKQojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KCmRlZiBnZW5fY29uZm91bmRpbmcoSywgTiwgcCwgcm5nKToKICAgIEEgPSBybmcuY2hvaWNlKEssIHNpemU9TiwgcD1wWydwX0EnXSkKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAgVCA9IEQgQCBwWydhbHBoYSddICsgcm5nLm5vcm1hbCgwLCBwWydzaWdtYV9UJ10sIE4pCiAgICBZID0gcFsnYmV0YV9UJ10gKiBUICsgRCBAIHBbJ2JldGFfQSddICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFksIEEKCgpkZWYgZ2VuX21lZGlhdGlvbihLLCBOLCBwLCBybmcpOgogICAgVCA9IHJuZy5iaW5vbWlhbCgxLCAwLjUsIE4pLmFzdHlwZShmbG9hdCkKICAgIGxvZ2l0cyA9IHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0YSddW05vbmUsIDpdICogVFs6LCBOb25lXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRzKQogICAgQSA9IHNhbXBsZV9jYXQocHJvYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoQSA9PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAgWSA9IHBbJ2JldGEnXVswXSArIEQgQCBwWydiZXRhJ11bMTpdICsgcFsndGF1J10gKiBUICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgcmV0dXJuIFQsIFksIEEKCgpkZWYgZ2VuX2NvbGxpZGVyKEssIE4sIHAsIHJuZyk6CiAgICBUID0gcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgWSA9IHBbJ3RhdSddICogVCArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxvZ2l0cyA9IChwWydnJ11bTm9uZSwgOl0gKyBwWydkVCddW05vbmUsIDpdICogVFs6LCBOb25lXQogICAgICAgICAgICAgICsgcFsnZFknXVtOb25lLCA6XSAqIFlbOiwgTm9uZV0pCiAgICBwcm9icyA9IHNvZnRtYXhfcm93cyhsb2dpdHMpCiAgICBBID0gc2FtcGxlX2NhdChwcm9icywgcm5nKQogICAgcmV0dXJuIFQsIFksIEEKCgpkZWYgZ2VuX2V4cG9zdXJlKEssIE4sIHAsIHJuZyk6CiAgICBBID0gcm5nLmNob2ljZShLLCBzaXplPU4sIHA9cFsncF9BJ10pCiAgICBEID0gbnAuemVyb3MoKE4sIEsgLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEgPT0gaiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBwWydiZXRhJ11bMF0gKyBEIEAgcFsnYmV0YSddWzE6XSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBOb25lLCBZLCBBCgoKZGVmIGdlbl9tYmlhcyhLLCBOLCBwLCBybmcpOgogICAgVTEgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAgICBVMiA9IHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIFQgPSBwWydkZWx0YV9jb2VmJ10gKiBVMSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIFkgPSBwWyd0YXUnXSAqIFQgKyBwWydsYW0nXSAqIFUyICsgcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtOb25lLCA6XSArIHBbJ2FfVTEnXVtOb25lLCA6XSAqIFUxWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBwWydhX1UyJ11bTm9uZSwgOl0gKiBVMls6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxvZ2l0cykKICAgIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICByZXR1cm4gVCwgWSwgQQoKCmRlZiBnZW5faXYoSywgTiwgcCwgcm5nKToKICAgIFogPSBybmcuYmlub21pYWwoMSwgMC41LCBOKS5hc3R5cGUoZmxvYXQpCiAgICBVID0gcm5nLm5vcm1hbCgwLCAxLCBOKQogICAgbG9naXRzID0gKHBbJ2cnXVtOb25lLCA6XSArIHBbJ2RaJ11bTm9uZSwgOl0gKiBaWzosIE5vbmVdCiAgICAgICAgICAgICAgKyBwWydkVSddW05vbmUsIDpdICogVVs6LCBOb25lXSkKICAgIHByb2JzID0gc29mdG1heF9yb3dzKGxvZ2l0cykKICAgIEEgPSBzYW1wbGVfY2F0KHByb2JzLCBybmcpCiAgICBEID0gbnAuemVyb3MoKE4sIEsgLSAxKSkKICAgIGZvciBqIGluIHJhbmdlKEsgLSAxKToKICAgICAgICBEWzosIGpdID0gKEEgPT0gaiArIDEpLmFzdHlwZShmbG9hdCkKICAgIFkgPSBEIEAgcFsnYmV0YSddWzE6XSArIHBbJ2xhbSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIHJldHVybiBaLCBZLCBBCgoKZGVmIGdlbl9mcm9udGRvb3IoSywgTiwgcCwgcm5nKToKICAgIFUgPSBybmcubm9ybWFsKDAsIDEsIE4pCiAgICBUID0gcFsnYWxwaGFfVSddICogVSArIHJuZy5ub3JtYWwoMCwgMSwgTikKICAgIGxvZ2l0cyA9IHBbJ2dhbW1hJ11bTm9uZSwgOl0gKyBwWydkZWx0YV9mZCddW05vbmUsIDpdICogVFs6LCBOb25lXQogICAgcHJvYnMgPSBzb2Z0bWF4X3Jvd3MobG9naXRzKQogICAgTSA9IHNhbXBsZV9jYXQocHJvYnMsIHJuZykKICAgIEQgPSBucC56ZXJvcygoTiwgSyAtIDEpKQogICAgZm9yIGogaW4gcmFuZ2UoSyAtIDEpOgogICAgICAgIERbOiwgal0gPSAoTSA9PSBqICsgMSkuYXN0eXBlKGZsb2F0KQogICAgWSA9IEQgQCBwWydiZXRhJ11bMTpdICsgcFsnbGFtYmRhX1UnXSAqIFUgKyBybmcubm9ybWFsKDAsIDEsIE4pCiAgICByZXR1cm4gVCwgWSwgTQoKCkdFTl9GTlMgPSB7CiAgICAnY29uZm91bmRpbmcnOiBnZW5fY29uZm91bmRpbmcsICdtZWRpYXRpb24nOiBnZW5fbWVkaWF0aW9uLAogICAgJ2NvbGxpZGVyJzogZ2VuX2NvbGxpZGVyLCAnZXhwb3N1cmUnOiBnZW5fZXhwb3N1cmUsCiAgICAnbWJpYXMnOiBnZW5fbWJpYXMsICdpdic6IGdlbl9pdiwgJ2Zyb250ZG9vcic6IGdlbl9mcm9udGRvb3IsCn0KCgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBTdWZmaWNpZW50IFN0YXRpc3RpY3MgJiBQbGltIChnZW5lcmFsIEspCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIHByZWNvbXB1dGVfc3VmZl9zdGF0cyhLLCB0b3BvbG9neSwgcGFyYW1z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "5118faa6-3a9c-4a0f-b4a3-7b51a4dc9a64",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/plan006_chunk_aa",
      "content": "[ATTACHMENT_DATA_REDACTED]",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---


### Assistant

_source line 117_

<details><summary>Logged reasoning block</summary>

```text
Trying to read the chunk files and pass them to ssh is getting very messy. Let me try a completely different approach.

I'll use the ssh_execute tool to write a Python script on the server that creates the file from base64 data. I'll pass the base64 data in smaller chunks using multiple ssh_execute calls.

Actually, let me try the simplest approach: write the file in pieces using echo commands to the server. But each piece needs to be small enough.

Wait, there's a much simpler approach: I can use the MCP ssh_execute tool to write the file by passing the base64 as an environment variable or argument to a Python one-liner. 

Let me just try sending the full 51KB base64 string in a single echo command and see if that works.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "a0f204ee-c6ab-4aac-80e8-94d9c466d0e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bjHjdMYdTLbmzg4VRAyrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 111524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12531
      },
      "output_tokens": 20,
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

_source line 118_

Let me try a simpler transfer approach — write a Python upload script locally that pushes via SSH, using the ssh config.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "929f650b-1402-4df5-9330-18d163be7847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bjHjdMYdTLbmzg4VRAyrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 111524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12531
      },
      "output_tokens": 20,
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

_source line 119_

<details open><summary>🔧 Tool call — Bash · `toolu_0135SGGvCkgoSXbcEkGQAUj1`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess, sys\n# Read the file\nwith open('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py', 'rb') as f:\n    content = f.read()\nprint(f'File size: {len(content)} bytes')\nimport base64\nb64 = base64.b64encode(content).decode()\nprint(f'Base64 size: {len(b64)} chars')\n# Write via SSH using subprocess\nproc = subprocess.run(\n    ['ssh', 'implicit5638.xyfu.me', \n     f'echo {b64} | base64 -d > /home/sonny/causal_annot_error_attrib/plan_006_asv_empirical.py'],\n    capture_output=True, text=True, timeout=30\n)\nprint(f'Return code: {proc.returncode}')\nprint(f'Stdout: {proc.stdout[:200]}')\nprint(f'Stderr: {proc.stderr[:200]}')\n\" 2>&1",
  "description": "Transfer file via SSH subprocess",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "95306ebd-21b8-486f-899e-1ae3dbf07cb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bjHjdMYdTLbmzg4VRAyrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 111524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12531
      },
      "output_tokens": 20,
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

_source line 120 · 2026-05-20T21:27:41.047Z_

<details><summary>↩ Tool result · `toolu_0135SGGvCkgoSXbcEkGQAUj1`</summary>

```text
File size: 38287 bytes
Base64 size: 51052 chars
Return code: 255
Stdout: 
Stderr: ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Host key verification failed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "1af88c01-9b3b-4552-a849-1f410ee69351",
  "tool_use_result": {
    "stdout": "File size: 38287 bytes\nBase64 size: 51052 chars\nReturn code: 255\nStdout: \nStderr: ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\nHost key verification failed.",
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

_source line 121_

<details><summary>Logged reasoning block</summary>

```text
Direct SSH doesn't work from this machine. The MCP tools handle SSH differently. Let me use the MCP tool to write the file. Since the MCP tool can handle large commands, let me try writing the base64 data in chunks using `printf` to append to a file on the server, then decode.

I'll break this into steps:
1. Write first chunk to /tmp/plan006.b64 on the server
2. Append remaining chunks
3. Decode to the target path

Let me try writing the chunks via ssh_execute. The MCP tool should handle 15K character commands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "25b297f5-cbdc-42bc-a61b-b4788829fe1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ujxk8afaLF1kGe1EgNdfSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 644,
      "cache_read_input_tokens": 124055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 644
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

_source line 122_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01GmT6nvUC5rxJcRmKn7uUih`</summary>

```json
{
  "server": "home-1x5090",
  "command": "printf '%s' 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiIKcGxhbl8wMDY6IEVtcGlyaWNhbCBBU1YgQ2FsaWJyYXRpb24gd2l0aCBMTE0gQW5ub3RhdGlvbiBDb25mdXNpb24gTWF0cmljZXMKClVzZXMgZW1waXJpY2FsIGNvbmZ1c2lvbiBtYXRyaWNlcyBmcm9tIExMTSBhbm5vdGF0aW9ucyAoMyBMTE1zIMOXIDMgZGF0YXNldHMgw5cgMyBwcm9tcHRzCj0gMjcgQyBtYXRyaWNlcykgdG8gY29tcHV0ZToKICAxLiBEb3duc3RyZWFtIGNhdXNhbCBiaWFzIGFjcm9zcyA3IERBRyB0b3BvbG9naWVzCiAgMi4gQVNWIHNlbnNpdGl2aXR5IG1ldHJpY3MgKG1hZ25pdHVkZSwgc2lnbmlmaWNhbmNlLCBzaWduLWZsaXApCiAgMy4gRjEgdnMgYmlhcyBkaXNjb25uZWN0IGFuYWx5c2lzIChCYXVtYW5uIDIwMjUgdmVyaWZpY2F0aW9uKQogIDQuIFR5cGUgSS9JSSBlcnJvciByYXRlcyBiZWZvcmUvYWZ0ZXIgQVNWIGZpbHRlcmluZwogIDUuIEludGVyLW1vZGVsIGVycm9yIGNvcnJlbGF0aW9uCgpJbnB1dDogIGRhdGEve2RhdGFzZXR9L3ttb2RlbH1fe3Byb21wdH1fYW5ub3RhdGlvbnMuanNvbmwKICAgICAgICBFYWNoIGxpbmU6IHsidHJ1ZV9sYWJlbCI6IGludCwgInByZWRpY3RlZF9sYWJlbCI6IGludH0KCk91dHB1dDogYXJ0aWZhY3RzL3BsYW4wMDYvYXN2X2VtcGlyaWNhbF9yZXN1bHRzLmpzb24KCkRlcGVuZGVuY2llczogbnVtcHkgKHJlcXVpcmVkKSwgbWF0cGxvdGxpYiAob3B0aW9uYWwgZm9yIHBsb3RzKQoiIiIK' > /tmp/plan006.b64 && echo \"OK: $(wc -c < /tmp/plan006.b64) bytes\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "22232e10-b618-4c72-89c1-3062cddd3532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ujxk8afaLF1kGe1EgNdfSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 644,
      "cache_read_input_tokens": 124055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 644
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

_source line 123 · 2026-05-20T21:28:16.097Z_

<details><summary>↩ Tool result · `toolu_01GmT6nvUC5rxJcRmKn7uUih`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK: 984 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "uuid": "8159d70c-b636-46c8-a038-563d243e39db",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"OK: 984 bytes\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"OK: 984 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---
