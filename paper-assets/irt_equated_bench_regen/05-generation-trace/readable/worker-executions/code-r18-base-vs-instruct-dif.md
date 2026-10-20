# code r18 base vs instruct dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_code_r18_base_vs_instruct_dif_20260522T174522.log`
- **Structured JSON:** [`d867315ed26da2670ab7.json`](../../sessions/d8/d867315ed26da2670ab7.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
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
  "uuid": "f8193b23-b0fb-49ea-ac2f-e6ff6b61c5b3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779489600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "383eccc8-d058-4c2b-8750-337ff7a88d53",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Create a single script that classifies models as base vs instruct, runs MH-DIF separately for each group, does comparison analysis, and outputs results
2. The script should be at `artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py`

Let me start by examining the existing code and data to understand the structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "ed8f88fa-0a1e-45e6-a07e-e6c323ecf53e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sr48gbE4QS5i3a3Yst1nBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14091,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14091
      },
      "output_tokens": 29,
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

先看现有数据和参考代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "fdcac243-2db0-42aa-b219-0d5ac750597f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sr48gbE4QS5i3a3Yst1nBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14091,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14091
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01Y5RrvEELuin7ddvFck7QAD`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore data and reference code",
  "prompt": "I need to understand the data and reference code for building a base vs instruct DIF analysis script. Please find and read:\n\n1. The MH-DIF function `mh_dif_c_pct_vec` in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` - read the full function implementation\n\n2. The cleaned MMLU analysis CSV structure - read a few lines of `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv` to see the columns\n\n3. Check what's in the response_matrix_index.npz - specifically what model_names look like (a sample of names)\n\n4. Check the structure of response_matrix.npz\n\nReport the full MH-DIF function code, the CSV columns, and a sample of model names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "125ba190-1c06-435c-a779-bc8dbe7ac254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sr48gbE4QS5i3a3Yst1nBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14091,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14091
      },
      "output_tokens": 29,
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
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "description": "Explore data and reference code",
  "task_type": "local_agent",
  "prompt": "I need to understand the data and reference code for building a base vs instruct DIF analysis script. Please find and read:\n\n1. The MH-DIF function `mh_dif_c_pct_vec` in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` - read the full function implementation\n\n2. The cleaned MMLU analysis CSV structure - read a few lines of `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv` to see the columns\n\n3. Check what's in the response_matrix_index.npz - specifically what model_names look like (a sample of names)\n\n4. Check the structure of response_matrix.npz\n\nReport the full MH-DIF function code, the CSV columns, and a sample of model names.",
  "uuid": "db0ea706-bcf3-4310-9d0c-bd2fb9125a19",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

## Round 1

35 recorded events

### User

_source line 8 · 2026-05-22T17:45:43.855Z_

I need to understand the data and reference code for building a base vs instruct DIF analysis script. Please find and read:

1. The MH-DIF function `mh_dif_c_pct_vec` in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` - read the full function implementation

2. The cleaned MMLU analysis CSV structure - read a few lines of `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv` to see the columns

3. Check what's in the response_matrix_index.npz - specifically what model_names look like (a sample of names)

4. Check the structure of response_matrix.npz

Report the full MH-DIF function code, the CSV columns, and a sample of model names.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "f5a0083c-f342-49e4-81d1-a9b949e0cf66"
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
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "description": "Reading artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py",
  "usage": {
    "total_tokens": 15656,
    "tool_uses": 1,
    "duration_ms": 1894
  },
  "last_tool_name": "Read",
  "uuid": "37453ebd-fa22-4d79-a94a-d4f966d7908e",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01EWRpFeeGW8gcyWr5ar2sjN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "6babe32f-a377-426b-b40d-93720346b073",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q3eRWoeQpaWPvnyXVe6qK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15643,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15643,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 11 · 2026-05-22T17:45:45.767Z_

<details><summary>↩ Tool result · `toolu_01EWRpFeeGW8gcyWr5ar2sjN`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	mmlu_bootstrap_ci.py — MMLU bootstrap 95% CI for MH-DIF C%.
4	
5	Vectorized total-score stratification (~100x faster than per-item rest-score).
6	For J=12508, total-score ≈ rest-score (diff < 0.3pp); validated at startup.
7	"""
8	
9	import numpy as np
10	import pandas as pd
11	from scipy.stats import chi2 as chi2_dist
12	from scipy.sparse import load_npz
13	from pathlib import Path
14	from multiprocessing import Pool
15	import time
16	import warnings
17	
18	warnings.filterwarnings("ignore", category=RuntimeWarning)
19	
20	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/"
21	            "projects/irt_equated_bench_regen/artifacts")
22	OUT = BASE / "plan_028_bootstrap_ci"
23	OUT.mkdir(exist_ok=True)
24	
25	N_BOOTSTRAP = 1000
26	N_CONTROL = 20
27	SEED = 42
28	N_STRATA = 5
29	
30	
31	# ════════════════════════════════════════════════════════════════════════
32	#  VECTORIZED MH-DIF (total-score stratification)
33	# ════════════════════════════════════════════════════════════════════════
34	def mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):
35	    """Fully vectorized MH-DIF → C%. Stratifies on total score (not rest)."""
36	    n_ref, J = X_ref.shape
37	    n_foc = X_foc.shape[0]
38	
39	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
40	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
41	    s_all = np.concatenate([tot_ref, tot_foc])
42	
43	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
44	    n_bins = len(edges) - 1
45	    if n_bins < 1:
46	        return 0.0
47	
48	    k_ref = np.digitize(tot_ref, edges[1:-1])
49	    k_foc = np.digitize(tot_foc, edges[1:-1])
50	
51	    n1 = np.zeros(n_bins, dtype=np.float64)
52	    n0 = np.zeros(n_bins, dtype=np.float64)
53	    A = np.zeros((n_bins, J), dtype=np.float64)
54	    C = np.zeros((n_bins, J), dtype=np.float64)
55	
56	    for k in range(n_bins):
57	        mr = (k_ref == k)
58	        mf = (k_foc == k)
59	        n1[k] = mr.sum()
60	        n0[k] = mf.sum()
61	        if mr.any():
62	            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
63	        if mf.any():
64	            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)
65	
66	    B = n1[:, None] - A
67	    D = n0[:, None] - C
68	    Nk = (n1 + n0)[:, None]
69	    m1 = A + C
70	    m0 = B + D
71	
72	    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
73	             (Nk > 1) & (m1 > 0) & (m0 > 0))
74	
75	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
76	    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)
77	
78	    finite_mask = (Rj > 0) & (Sj > 0)
79	
80	    with np.errstate(divide="ignore", invalid="ignore"):
81	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
82	
83	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
84	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
85	
86	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
87	    sum_var = np.where(
88	        valid,
89	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
90	        0,
91	    ).sum(axis=0)
92	
93	    chi2_j = np.where(
94	        sum_var > 0,
95	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
96	        0,
97	    )
98	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
99	
100	    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
101	    return is_c.sum() / J * 100
102	
103	
104	# ════════════════════════════════════════════════════════════════════════
105	#  REST-SCORE MH-DIF (validation only)
106	# ════════════════════════════════════════════════════════════════════════
107	def mh_dif_c_pct_rest(X_ref, X_foc, n_strata=N_STRATA):
108	    """Per-item rest-score MH-DIF (reference implementation)."""
109	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
110	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
111	    J = X_ref.shape[1]
112	    n_c = 0
113	    qs = np.linspace(0, 1, n_strata + 1)
114	    nr = len(tot_ref)
115	    nf = len(tot_foc)
116	    s_buf = np.empty(nr + nf, dtype=np.float64)
117	
118	    for j in range(J):
119	        s_buf[:nr] = tot_ref - X_ref[:, j]
120	        s_buf[nr:] = tot_foc - X_foc[:, j]
121	        edges = np.unique(np.quantile(s_buf, qs))
122	        nb = len(edges) - 1
123	        if nb < 1:
124	            continue
125	        kr = np.digitize(s_buf[:nr], edges[1:-1])
126	        kf = np.digitize(s_buf[nr:], edges[1:-1])
127	
128	        R = S = sd = sv = 0.0
129	        n_ok = 0
130	        for k in range(nb):
131	            mr = (kr == k)
132	            mf = (kf == k)
133	            n1 = int(mr.sum())
134	            n0 = int(mf.sum())
135	            if n1 == 0 or n0 == 0:
136	                continue
137	            Ak = float(X_ref[mr, j].sum())
138	            Bk = n1 - Ak
139	            Ck = float(X_foc[mf, j].sum())
140	            Dk = n0 - Ck
141	            Nk = n1 + n0
142	            m1k = Ak + Ck
143	            m0k = Bk + Dk
144	            if m1k == 0 or m0k == 0 or Nk <= 1:
145	                continue
146	            n_ok += 1
147	            R += Ak * Dk / Nk
148	            S += Bk * Ck / Nk
149	            sd += Ak - n1 * m1k / Nk
150	            sv += n1 * n0 * m1k * m0k / (Nk * Nk * (Nk - 1))
151	
152	        if n_ok == 0 or (R == 0 and S == 0):
153	            continue
154	        if S == 0:
155	            delta = -np.inf
156	        elif R == 0:
157	            delta = np.inf
158	        else:
159	            delta = -2.35 * np.log(R / S)
160	        pval = (1 - chi2_dist.cdf(max(abs(sd) - 0.5, 0) ** 2 / sv, df=1)
161	                if sv > 0 else 1.0)
162	        if np.isfinite(delta) and abs(delta) >= 1.5 and pval < 0.05:
163	            n_c += 1
164	
165	    return n_c / J * 100
166	
167	
168	# ════════════════════════════════════════════════════════════════════════
169	#  MULTIPROCESSING BOOTSTRAP
170	# ════════════════════════════════════════════════════════════════════════
171	_Xr = None
172	_Xf = None
173	
174	
175	def _init(Xr, Xf):
176	    global _Xr, _Xf
177	    _Xr = Xr
178	    _Xf = Xf
179	
180	
181	def _boot_one(seed):
182	    rng = np.random.RandomState(seed)
183	    ir = rng.randint(0, _Xr.shape[0], size=_Xr.shape[0])
184	    jf = rng.randint(0, _Xf.shape[0], size=_Xf.shape[0])
185	    return mh_dif_c_pct_vec(_Xr[ir], _Xf[jf])
186	
187	
188	# ════════════════════════════════════════════════════════════════════════
189	#  MAIN
190	# ════════════════════════════════════════════════════════════════════════
191	def main():
192	    t_total = time.time()
193	    print(f"MMLU Bootstrap CI — N={N_BOOTSTRAP}, seed={SEED}")
194	    print(f"Output: {OUT}\n")
195	
196	    # ── Load ──
197	    print("Loading MMLU response matrix...")
198	    t0 = time.time()
199	    X = load_npz(BASE / "response_matrix.npz").toarray().astype(np.int8)
200	    idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
201	    model_names = idx["model_names"]
202	    meta = pd.read_csv(BASE / "model_metadata.csv")
203	    cohort = dict(zip(meta["model_name"], meta["cohort_temporal"]))
204	    print(f"  {X.shape[0]} models × {X.shape[1]} items ({time.time()-t0:.1f}s)")
205	
206	    name2row = {n: i for i, n in enumerate(model_names)}
207	    ref_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == "2023"])
208	    foc_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == "2024"])
209	    print(f"  Cohorts: ref(2023)={len(ref_idx)}, foc(2024)={len(foc_idx)}")
210	
211	    X_ref = X[ref_idx]
212	    X_foc = X[foc_idx]
213	    del X
214	
215	    # ── Validate total-score vs rest-score ──
216	    print("\nValidation: total-score vs rest-score stratification...")
217	    t0 = time.time()
218	    c_vec = mh_dif_c_pct_vec(X_ref, X_foc)
219	    t_vec = time.time() - t0
220	    print(f"  Vectorized (total-score): C% = {c_vec:.2f}% ({t_vec:.2f}s)")
221	
222	    t0 = time.time()
223	    c_rest = mh_dif_c_pct_rest(X_ref, X_foc)
224	    t_rest = time.time() - t0
225	    print(f"  Original  (rest-score):   C% = {c_rest:.2f}% ({t_rest:.1f}s)")
226	    diff_pp = abs(c_vec - c_rest)
227	    print(f"  Difference: {diff_pp:.2f}pp  |  Speedup: {t_rest/t_vec:.0f}x")
228	
229	    use_rest = diff_pp > 1.0
230	    if use_rest:
231	        print("  WARNING: >1pp gap — using rest-score (slow path)")
232	
233	    # ── Sanity check N=10 ──
234	    print(f"\nSanity check: N=10 bootstrap...")
235	    rng = np.random.RandomState(SEED)
236	    fn = mh_dif_c_pct_rest if use_rest else mh_dif_c_pct_vec
237	    sanity = []
238	    for i in range(10):
239	        ir = rng.randint(0, len(ref_idx), size=len(ref_idx))
240	        jf = rng.randint(0, len(foc_idx), size=len(foc_idx))
241	        sanity.append(fn(X_ref[ir], X_foc[jf]))
242	    print(f"  C% range: [{min(sanity):.1f}%, {max(sanity):.1f}%], "
243	          f"mean={np.mean(sanity):.1f}%  (expect ≈31%)")
244	
245	    # ── Full bootstrap N=1000 ──
246	    print(f"\nBootstrap N={N_BOOTSTRAP} (2 processes)...")
247	    seeds = list(range(SEED, SEED + N_BOOTSTRAP))
248	    boot_cs = np.zeros(N_BOOTSTRAP)
249	    t_start = time.time()
250	
251	    with Pool(2, initializer=_init, initargs=(X_ref, X_foc)) as pool:
252	        for i, c in enumerate(pool.imap(
253	                _boot_one if not use_rest else _boot_one, seeds)):
254	            boot_cs[i] = c
255	            done = i + 1
256	            if done % 100 == 0 or done == 1:
257	                el = time.time() - t_start
258	                eta = (N_BOOTSTRAP - done) / (done / el) / 60
259	                print(f"  [{done}/{N_BOOTSTRAP}] C%={c:.2f}%  "
260	                      f"running mean={boot_cs[:done].mean():.2f}%  "
261	                      f"({el:.0f}s, ETA {eta:.0f}min)")
262	
263	    ci_lo = np.percentile(boot_cs, 2.5)
264	    ci_hi = np.percentile(boot_cs, 97.5)
265	    b_mean = boot_cs.mean()
266	    b_std = boot_cs.std()
267	
268	    print(f"\n  Original C% = {c_rest:.2f}% (rest-score)")
269	    print(f"  95% CI: [{ci_lo:.2f}%, {ci_hi:.2f}%]")
270	    print(f"  Boot mean={b_mean:.2f}%, std={b_std:.2f}%, "
271	          f"bias={b_mean - c_vec:+.2f}pp")
272	
273	    # ── Random-split control ──
274	    print(f"\nRandom-split control (N={N_CONTROL})...")
275	    combined = np.vstack([X_ref, X_foc])
276	    rng_c = np.random.RandomState(SEED + 9999)
277	    ctrl = []
278	    for i in range(N_CONTROL):
279	        perm = rng_c.permutation(combined.shape[0])
280	        Xr = combined[perm[: len(ref_idx)]]
281	        Xf = combined[perm[len(ref_idx): len(ref_idx) + len(foc_idx)]]
282	        ctrl.append(mh_dif_c_pct_vec(Xr, Xf))
283	        if (i + 1) % 5 == 0:
284	            print(f"  [{i+1}/{N_CONTROL}] C%={ctrl[-1]:.2f}%")
285	
286	    ctrl_mean = np.mean(ctrl)
287	    ctrl_std = np.std(ctrl)
288	    print(f"  Control: mean={ctrl_mean:.2f}%, std={ctrl_std:.2f}%, "
289	          f"range=[{min(ctrl):.2f}%, {max(ctrl):.2f}%]")
290	
291	    # ── Save ──
292	    pd.DataFrame({"bootstrap_id": range(N_BOOTSTRAP), "c_pct": boot_cs}).to_csv(
293	        OUT / "mmlu_bootstrap_results.csv", index=False)
294	
295	    summary = pd.DataFrame([{
296	        "benchmark": "mmlu",
297	        "original_c_pct_rest": c_rest,
298	        "original_c_pct_vec": c_vec,
299	        "ci_lower": ci_lo,
300	        "ci_upper": ci_hi,
301	        "boot_mean": b_mean,
302	        "boot_std": b_std,
303	        "n_bootstrap": N_BOOTSTRAP,
304	        "n_ref": len(ref_idx),
305	        "n_foc": len(foc_idx),
306	        "n_items": X_ref.shape[1],
307	        "ctrl_mean": ctrl_mean,
308	        "ctrl_std": ctrl_std,
309	    }])
310	    summary.to_csv(OUT / "mmlu_bootstrap_summary.csv", index=False)
311	
312	    elapsed = time.time() - t_total
313	    temporal_vs_ctrl = ("confirms DIF is temporal, not spurious"
314	                        if ctrl_mean < ci_lo
315	                        else "control overlaps temporal — interpret with caution")
316	
317	    report = f"""# MMLU Bootstrap 95% CI for MH-DIF C%
318	
319	## Method
320	
321	- Bootstrap resampling of **models** (not items), N={N_BOOTSTRAP}
322	- Per bootstrap: resample N_ref={len(ref_idx)} (2023) and N_foc={len(foc_idx)} (2024) with replacement
323	- MH-DIF with {N_STRATA}-stratum total-score matching
324	- Validated against rest-score: diff = {diff_pp:.2f}pp (speedup {t_rest/t_vec:.0f}x)
325	- 95% CI via percentile method [2.5th, 97.5th]
326	- Seed = {SEED}
327	
328	## Results
329	
330	| Metric | Value |
331	|--------|-------|
332	| Original C% (rest-score) | {c_rest:.2f}% |
333	| Original C% (total-score) | {c_vec:.2f}% |
334	| Bootstrap 95% CI | [{ci_lo:.2f}%, {ci_hi:.2f}%] |
335	| Bootstrap mean | {b_mean:.2f}% |
336	| Bootstrap SD | {b_std:.2f}% |
337	| Bias (mean − original) | {b_mean - c_vec:+.2f}pp |
338	| CI width | {ci_hi - ci_lo:.2f}pp |
339	
340	## Random-Split Control (N={N_CONTROL})
341	
342	| Metric | Value |
343	|--------|-------|
344	| Control mean C% | {ctrl_mean:.2f}% |
345	| Control SD | {ctrl_std:.2f}% |
346	| Control range | [{min(ctrl):.2f}%, {max(ctrl):.2f}%] |
347	
348	## Interpretation
349	
350	- 95% CI [{ci_lo:.1f}%, {ci_hi:.1f}%] — {'narrow, estimate is stable' if (ci_hi - ci_lo) < 10 else 'moderate width'}
351	- Control C% = {ctrl_mean:.1f}% vs temporal C% = {c_rest:.1f}% — {temporal_vs_ctrl}
352	
353	Runtime: {elapsed / 60:.1f} min
354	"""
355	    (OUT / "mmlu_bootstrap_report.md").write_text(report)
356	
357	    print(f"\nSaved: mmlu_bootstrap_results.csv, mmlu_bootstrap_summary.csv, "
358	          f"mmlu_bootstrap_report.md")
359	    print(f"Total: {elapsed / 60:.1f} min")
360	
361	
362	if __name__ == "__main__":
363	    main()
364	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "253968d9-8b68-462b-89bf-233b948e0bda"
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
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "description": "Reading artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv",
  "usage": {
    "total_tokens": 15661,
    "tool_uses": 2,
    "duration_ms": 2351
  },
  "last_tool_name": "Read",
  "uuid": "be38fcc5-a174-483e-b63c-402854093245",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01TeUR9rCj76bs3oaxA1EkxU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "fc9abbe9-d90a-4d2a-932a-60c0bc7b1dbc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q3eRWoeQpaWPvnyXVe6qK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15643,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15643,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 14 · 2026-05-22T17:45:46.214Z_

<details><summary>↩ Tool result · `toolu_01TeUR9rCj76bs3oaxA1EkxU`</summary>

```text
1	model_name,score_full,score_cleaned,rank_full,rank_cleaned,rank_change,abs_rank_change,family,cohort_temporal
2	0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other
3	0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other
4	0-hero/Matter-0.1-7B-boost,0.6534218100415734,0.680093131548312,2811,2791,-20,20,unknown,other
5	0-hero/Matter-0.1-7B-boost-DPO,0.6549408378637672,0.6817229336437718,2776,2751,-25,25,,other
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "e4821a41-b670-4043-9926-1493b34b2e76"
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
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 15666,
    "tool_uses": 3,
    "duration_ms": 2539
  },
  "last_tool_name": "Bash",
  "uuid": "2fbfaff4-878b-4970-85d5-ee2aa48f0221",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_015D9M9YxMfYcm3eqDXxNaUM`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "53ad2636-ff33-454c-955d-41e24d9c4861",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q3eRWoeQpaWPvnyXVe6qK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15643,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15643,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 17 · 2026-05-22T17:45:46.567Z_

<details><summary>↩ Tool result · `toolu_015D9M9YxMfYcm3eqDXxNaUM`</summary>

```text
total 580
drwxr-xr-x  4 ubuntu ubuntu   4096 May 21 13:48 .
drwxr-xr-x 84 ubuntu ubuntu   4096 May 22 17:45 ..
-rw-r--r--  1 ubuntu ubuntu 517398 May 21 13:37 cleaned_mmlu_analysis.csv
drwxr-xr-x  2 ubuntu ubuntu   4096 May 21 13:49 data
-rw-r--r--  1 ubuntu ubuntu    785 May 21 13:48 dif_vs_random_comparison.csv
-rw-r--r--  1 ubuntu ubuntu   4791 May 21 13:37 per_subject_dif_concentration.csv
-rw-r--r--  1 ubuntu ubuntu  10868 May 21 13:37 plan_032_dif_cleaned_mmlu.py
-rw-r--r--  1 ubuntu ubuntu   9912 May 21 13:47 plan_032_random_baseline.py
-rw-r--r--  1 ubuntu ubuntu   8307 May 21 13:48 plan_032_report.md
-rw-r--r--  1 ubuntu ubuntu   1224 May 21 13:48 random_baseline_report.md
-rw-r--r--  1 ubuntu ubuntu   3209 May 21 13:48 random_baseline_summary.csv
drwxr-xr-x  2 ubuntu ubuntu   4096 May 21 13:40 report
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "d949a8d2-ba69-4c72-8078-5915bdbc4843"
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
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "description": "Running cd /home/ubuntu/.agent-ml-research-idea_gen_0520_…",
  "usage": {
    "total_tokens": 23490,
    "tool_uses": 4,
    "duration_ms": 6691
  },
  "last_tool_name": "Bash",
  "uuid": "ae15773a-7f39-442e-ab21-74a9eb493bc8",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_0189VcLMkyP2mQcFCkhUgaLo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts && python3 << 'EOF'\nimport numpy as np\nfrom scipy.sparse import load_npz\n\n# Load and inspect response_matrix_index.npz\nidx = np.load('response_matrix_index.npz', allow_pickle=True)\nmodel_names = idx['model_names']\nprint(\"=== response_matrix_index.npz ===\")\nprint(f\"Keys: {list(idx.files)}\")\nprint(f\"Model names shape: {model_names.shape}\")\nprint(f\"\\nFirst 10 model names:\")\nfor i, name in enumerate(model_names[:10]):\n    print(f\"  [{i}] {name}\")\nprint(f\"\\nLast 5 model names:\")\nfor i, name in enumerate(model_names[-5:], start=len(model_names)-5):\n    print(f\"  [{i}] {name}\")\n\n# Load and inspect response_matrix.npz\nprint(\"\\n=== response_matrix.npz ===\")\nX = load_npz('response_matrix.npz')\nprint(f\"Type: {type(X)}\")\nprint(f\"Shape: {X.shape}\")\nprint(f\"Dtype: {X.dtype}\")\nprint(f\"Sparsity: {1 - (X.nnz / (X.shape[0] * X.shape[1])):.2%}\")\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "f9643a1e-1dd6-4fc1-bf4f-31eeec8f1522",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Epts9wSgrSS9u1kCqFjmfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7818,
      "cache_read_input_tokens": 15643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7818,
        "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-22T17:45:51.984Z_

<details><summary>↩ Tool result · `toolu_0189VcLMkyP2mQcFCkhUgaLo`</summary>

```text
=== response_matrix_index.npz ===
Keys: ['model_names', 'item_ids']
Model names shape: (5227,)

First 10 model names:
  [0] 0-hero/Matter-0.1-7B
  [1] 0-hero/Matter-0.1-7B-DPO-preview
  [2] 0-hero/Matter-0.1-7B-boost
  [3] 0-hero/Matter-0.1-7B-boost-DPO
  [4] 0-hero/Matter-0.1-7B-boost-DPO-preview
  [5] 0-hero/Matter-0.1-Slim-7B
  [6] 0-hero/Matter-0.1-Slim-7B-A
  [7] 0-hero/Matter-0.1-Slim-7B-B
  [8] 0-hero/Matter-0.1-Slim-7B-C
  [9] 0-hero/Matter-0.1-Slim-7B-C-DPO

Last 5 model names:
  [5222] zorobin/mistral-class-shishya-7b-ep3
  [5223] zorobin/mistral-class-shishya-all-hal-7b-ep3
  [5224] zyh3826/20231206094523-pretrain-Llama-2-13b-hf-76000
  [5225] zyh3826/GML-Mistral-merged-v1
  [5226] zyh3826/llama2-13b-ft-openllm-leaderboard-v1

=== response_matrix.npz ===
Type: &lt;class 'scipy.sparse._csr.csr_matrix'>
Shape: (5227, 12508)
Dtype: int8
Sparsity: 40.88%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "25b30519-5fc5-4126-998a-04d644c3d0cf"
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
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "description": "Running head -1 /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 24418,
    "tool_uses": 5,
    "duration_ms": 9665
  },
  "last_tool_name": "Bash",
  "uuid": "deceef1a-d95b-4781-997e-7c25562ed741",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_019XGqfgf49Zs9MZNYB7yuHL`</summary>

```json
{
  "command": "head -1 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv | tr ',' '\\n' | nl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "65585b12-1803-4aa2-837e-521b5f566060",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PW1mCuA1d7GUQ6zyJpoX8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 23461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 927,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-22T17:45:53.591Z_

<details><summary>↩ Tool result · `toolu_019XGqfgf49Zs9MZNYB7yuHL`</summary>

```text
     1	model_name
     2	score_full
     3	score_cleaned
     4	rank_full
     5	rank_cleaned
     6	rank_change
     7	abs_rank_change
     8	family
     9	cohort_temporal
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "8451f928-3315-46c6-9ae6-89e706aa61d5"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a6ad6397e8c91d2f6",
  "tool_use_id": "toolu_01Y5RrvEELuin7ddvFck7QAD",
  "status": "completed",
  "output_file": "",
  "summary": "Explore data and reference code",
  "usage": {
    "total_tokens": 24638,
    "tool_uses": 5,
    "duration_ms": 27253
  },
  "uuid": "c0ca2831-cc38-4c1d-b013-3b4a2dd5256e",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool result

_source line 25 · 2026-05-22T17:46:11.115Z_

<details><summary>↩ Tool result · `toolu_01Y5RrvEELuin7ddvFck7QAD`</summary>

````text
Perfect! Now I have all the information needed. Let me compile the complete report.

## Summary Report

### 1. MH-DIF Function: `mh_dif_c_pct_vec` (Full Implementation)

Located at: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` (lines 34–101)

```python
def mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):
    """Fully vectorized MH-DIF → C%. Stratifies on total score (not rest)."""
    n_ref, J = X_ref.shape
    n_foc = X_foc.shape[0]

    tot_ref = X_ref.sum(axis=1).astype(np.float64)
    tot_foc = X_foc.sum(axis=1).astype(np.float64)
    s_all = np.concatenate([tot_ref, tot_foc])

    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
    n_bins = len(edges) - 1
    if n_bins < 1:
        return 0.0

    k_ref = np.digitize(tot_ref, edges[1:-1])
    k_foc = np.digitize(tot_foc, edges[1:-1])

    n1 = np.zeros(n_bins, dtype=np.float64)
    n0 = np.zeros(n_bins, dtype=np.float64)
    A = np.zeros((n_bins, J), dtype=np.float64)
    C = np.zeros((n_bins, J), dtype=np.float64)

    for k in range(n_bins):
        mr = (k_ref == k)
        mf = (k_foc == k)
        n1[k] = mr.sum()
        n0[k] = mf.sum()
        if mr.any():
            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
        if mf.any():
            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)

    B = n1[:, None] - A
    D = n0[:, None] - C
    Nk = (n1 + n0)[:, None]
    m1 = A + C
    m0 = B + D

    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
             (Nk > 1) & (m1 > 0) & (m0 > 0))

    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)

    finite_mask = (Rj > 0) & (Sj > 0)

    with np.errstate(divide="ignore", invalid="ignore"):
        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)

    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)

    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
    sum_var = np.where(
        valid,
        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
        0,
    ).sum(axis=0)

    chi2_j = np.where(
        sum_var > 0,
        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
        0,
    )
    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)

    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
    return is_c.sum() / J * 100
```

**Key characteristics:**
- Uses **total-score stratification** (not per-item rest-score) for ~100x speed improvement
- Stratifies into n_strata=5 bins based on quantiles
- For each stratum k and item j, computes the Mantel-Haenszel log-odds ratio: delta_j = -2.35 * log(Rj/Sj)
- Tests DIF at two thresholds: |delta_j| >= 1.5 AND chi-square p-value < 0.05
- Returns the percentage of items flagged as having DIF (C%)

### 2. Cleaned MMLU Analysis CSV Structure

**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv`

**Columns (9 total):**
1. `model_name` — unique model identifier (e.g., "0-hero/Matter-0.1-7B")
2. `score_full` — performance score on full MMLU dataset
3. `score_cleaned` — performance score on cleaned subset
4. `rank_full` — ranking based on full score
5. `rank_cleaned` — ranking based on cleaned score
6. `rank_change` — signed rank change (negative = improved rank)
7. `abs_rank_change` — absolute value of rank change
8. `family` — model family designation (e.g., "unknown", blank for unlabeled)
9. `cohort_temporal` — temporal cohort assignment ("2023", "2024", "other")

**Sample rows (first 4 data rows):**
```
0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other
0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other
0-hero/Matter-0.1-7B-boost,0.6534218100415734,0.680093131548312,2811,2791,-20,20,unknown,other
0-hero/Matter-0.1-7B-boost-DPO,0.6549408378637672,0.6817229336437718,2776,2751,-25,25,,other
```

### 3. Response Matrix Data Structure

**response_matrix.npz:**
- **Shape:** 5227 models × 12508 items
- **Type:** scipy.sparse.csr_matrix (CSR sparse format)
- **Data type:** int8 (binary: 0/1 for incorrect/correct)
- **Sparsity:** 40.88% (59.12% non-zero, fully populated with responses)

**response_matrix_index.npz:**
- **Keys:** `model_names`, `item_ids`
- **model_names:** Array of 5227 unique model identifiers (e.g., "0-hero/Matter-0.1-7B", "zorobin/mistral-class-shishya-7b-ep3")

**Sample model names (first 10):**
```
0-hero/Matter-0.1-7B
0-hero/Matter-0.1-7B-DPO-preview
0-hero/Matter-0.1-7B-boost
0-hero/Matter-0.1-7B-boost-DPO
0-hero/Matter-0.1-7B-boost-DPO-preview
0-hero/Matter-0.1-Slim-7B
0-hero/Matter-0.1-Slim-7B-A
0-hero/Matter-0.1-Slim-7B-B
0-hero/Matter-0.1-Slim-7B-C
0-hero/Matter-0.1-Slim-7B-C-DPO
```

This data is ready for building a base vs instruct DIF analysis script. The MH-DIF function provides stratified total-score matching (5 strata default), and you can segment models by the `cohort_temporal` column to compare 2023 vs 2024 performance, or use the `family` column for base vs instruct groupings.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "5b4e293a-9fed-409f-9d59-9d2935fd1b92",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the data and reference code for building a base vs instruct DIF analysis script. Please find and read:\n\n1. The MH-DIF function `mh_dif_c_pct_vec` in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` - read the full function implementation\n\n2. The cleaned MMLU analysis CSV structure - read a few lines of `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv` to see the columns\n\n3. Check what's in the response_matrix_index.npz - specifically what model_names look like (a sample of names)\n\n4. Check the structure of response_matrix.npz\n\nReport the full MH-DIF function code, the CSV columns, and a sample of model names.",
    "agentId": "a6ad6397e8c91d2f6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile the complete report.\n\n## Summary Report\n\n### 1. MH-DIF Function: `mh_dif_c_pct_vec` (Full Implementation)\n\nLocated at: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` (lines 34–101)\n\n```python\ndef mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Fully vectorized MH-DIF → C%. Stratifies on total score (not rest).\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return is_c.sum() / J * 100\n```\n\n**Key characteristics:**\n- Uses **total-score stratification** (not per-item rest-score) for ~100x speed improvement\n- Stratifies into n_strata=5 bins based on quantiles\n- For each stratum k and item j, computes the Mantel-Haenszel log-odds ratio: delta_j = -2.35 * log(Rj/Sj)\n- Tests DIF at two thresholds: |delta_j| >= 1.5 AND chi-square p-value < 0.05\n- Returns the percentage of items flagged as having DIF (C%)\n\n### 2. Cleaned MMLU Analysis CSV Structure\n\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv`\n\n**Columns (9 total):**\n1. `model_name` — unique model identifier (e.g., \"0-hero/Matter-0.1-7B\")\n2. `score_full` — performance score on full MMLU dataset\n3. `score_cleaned` — performance score on cleaned subset\n4. `rank_full` — ranking based on full score\n5. `rank_cleaned` — ranking based on cleaned score\n6. `rank_change` — signed rank change (negative = improved rank)\n7. `abs_rank_change` — absolute value of rank change\n8. `family` — model family designation (e.g., \"unknown\", blank for unlabeled)\n9. `cohort_temporal` — temporal cohort assignment (\"2023\", \"2024\", \"other\")\n\n**Sample rows (first 4 data rows):**\n```\n0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other\n0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other\n0-hero/Matter-0.1-7B-boost,0.6534218100415734,0.680093131548312,2811,2791,-20,20,unknown,other\n0-hero/Matter-0.1-7B-boost-DPO,0.6549408378637672,0.6817229336437718,2776,2751,-25,25,,other\n```\n\n### 3. Response Matrix Data Structure\n\n**response_matrix.npz:**\n- **Shape:** 5227 models × 12508 items\n- **Type:** scipy.sparse.csr_matrix (CSR sparse format)\n- **Data type:** int8 (binary: 0/1 for incorrect/correct)\n- **Sparsity:** 40.88% (59.12% non-zero, fully populated with responses)\n\n**response_matrix_index.npz:**\n- **Keys:** `model_names`, `item_ids`\n- **model_names:** Array of 5227 unique model identifiers (e.g., \"0-hero/Matter-0.1-7B\", \"zorobin/mistral-class-shishya-7b-ep3\")\n\n**Sample model names (first 10):**\n```\n0-hero/Matter-0.1-7B\n0-hero/Matter-0.1-7B-DPO-preview\n0-hero/Matter-0.1-7B-boost\n0-hero/Matter-0.1-7B-boost-DPO\n0-hero/Matter-0.1-7B-boost-DPO-preview\n0-hero/Matter-0.1-Slim-7B\n0-hero/Matter-0.1-Slim-7B-A\n0-hero/Matter-0.1-Slim-7B-B\n0-hero/Matter-0.1-Slim-7B-C\n0-hero/Matter-0.1-Slim-7B-C-DPO\n```\n\nThis data is ready for building a base vs instruct DIF analysis script. The MH-DIF function provides stratified total-score matching (5 strata default), and you can segment models by the `cohort_temporal` column to compare 2023 vs 2024 performance, or use the `family` column for base vs instruct groupings."
      }
    ],
    "totalDurationMs": 27255,
    "totalTokens": 26846,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 24388,
      "output_tokens": 2233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2233,
          "cache_read_input_tokens": 24388,
          "cache_creation_input_tokens": 219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 219,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 3,
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_018tWFQfDG2c7SbfyExDarcY`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "5f87f0d1-aa5f-4dbf-a679-d6871619c355",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LUb8MrWwH1PMEJsrK8PiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 25932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2708
      },
      "output_tokens": 62,
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

_source line 27 · 2026-05-22T17:46:15.827Z_

<details><summary>↩ Tool result · `toolu_018tWFQfDG2c7SbfyExDarcY`</summary>

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
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "ac12258d-25a9-4496-b654-c4a243c9a14e",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 28_

数据结构清楚了，开始写脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "0d9fdffc-5950-48af-b3bb-61f004ffbf6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EY4yrq3e8EkNrRfjDiQxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 138,
      "cache_read_input_tokens": 28640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 138
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

_source line 29_

<details open><summary>🔧 Tool call — Write · `toolu_01J1c1TBWBSFZ66aCJsCtSND`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "content": "#!/usr/bin/env python3\n\"\"\"R18: Base vs Instruct MH-DIF separation experiment.\"\"\"\n\nimport re\nimport sys\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r18_base_vs_instruct_dif\"\n\nN_STRATA = 5\nN_BOOT = 1000\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n# ── Part 1: Model classification ─────────────────────────────────────────\n\nINSTRUCT_SUFFIXES = re.compile(\n    r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)\"\n    r\"([-_\\.]|$)\",\n    re.IGNORECASE,\n)\n\nQUANT_SUFFIXES = re.compile(\n    r\"[-_\\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])\",\n    re.IGNORECASE,\n)\n\nFAMILY_PREFIX_EXCLUDE = re.compile(\n    r\"^(openchat|chatglm|chatml)\",\n    re.IGNORECASE,\n)\n\n\ndef classify_model(name: str) -> str:\n    short = name.split(\"/\")[-1] if \"/\" in name else name\n    stripped = QUANT_SUFFIXES.sub(\"\", short)\n\n    if stripped.lower().endswith(\"-it\"):\n        return \"instruct\"\n\n    if INSTRUCT_SUFFIXES.search(stripped):\n        prefix_part = stripped.split(\"-\")[0].split(\"_\")[0]\n        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):\n            rest = stripped[len(prefix_part):]\n            if not INSTRUCT_SUFFIXES.search(rest):\n                return \"base\"\n        return \"instruct\"\n\n    return \"base\"\n\n\n# ── Part 2: MH-DIF (extended) ────────────────────────────────────────────\n\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\n\n    Returns (c_pct, delta_mh, pval, is_c).\n    \"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = k_ref == k\n        mf = k_foc == k\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()\n        if mf.any():\n            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)\n    c_pct = is_c.sum() / J * 100\n\n    return c_pct, delta_j, pval_j, is_c\n\n\ndef ets_class(delta):\n    a = abs(delta)\n    if a < 1.0:\n        return \"A\"\n    elif a < 1.5:\n        return \"B\"\n    else:\n        return \"C\"\n\n\n# ── Main ──────────────────────────────────────────────────────────────────\n\ndef main():\n    print(\"Loading data...\")\n    meta = pd.read_csv(f\"{ROOT}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n    rm = np.load(f\"{ROOT}/response_matrix.npz\")\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]), shape=tuple(rm[\"shape\"]))\n    idx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n\n    # Build model name → row index lookup\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Classify models\n    meta = meta[meta[\"cohort_temporal\"].isin([\"2023\", \"2024\"])].copy()\n    meta[\"model_type\"] = meta[\"model_name\"].apply(classify_model)\n\n    # Save classification\n    class_df = meta[[\"model_name\", \"model_type\", \"cohort_temporal\", \"family\"]].copy()\n    class_df.to_csv(f\"{OUT}/model_classification.csv\", index=False)\n\n    # Map to response matrix rows\n    meta[\"rm_idx\"] = meta[\"model_name\"].map(name2row)\n    meta = meta.dropna(subset=[\"rm_idx\"])\n    meta[\"rm_idx\"] = meta[\"rm_idx\"].astype(int)\n\n    # Group counts\n    groups = {}\n    for mtype in [\"base\", \"instruct\"]:\n        ref_mask = (meta[\"model_type\"] == mtype) & (meta[\"cohort_temporal\"] == \"2023\")\n        foc_mask = (meta[\"model_type\"] == mtype) & (meta[\"cohort_temporal\"] == \"2024\")\n        groups[mtype] = {\n            \"ref_idx\": meta.loc[ref_mask, \"rm_idx\"].values,\n            \"foc_idx\": meta.loc[foc_mask, \"rm_idx\"].values,\n        }\n\n    print(\"\\n=== Part 4: Sample sizes ===\")\n    for mtype in [\"base\", \"instruct\"]:\n        n_ref = len(groups[mtype][\"ref_idx\"])\n        n_foc = len(groups[mtype][\"foc_idx\"])\n        flag = \" ⚠ UNDERPOWERED\" if min(n_ref, n_foc) < 80 else \"\"\n        print(f\"  {mtype:>10s}: ref(2023)={n_ref}, foc(2024)={n_foc}{flag}\")\n    print(f\"  {'full':>10s}: ref(2023)=1080, foc(2024)=807  (reported baseline)\")\n\n    # Run MH-DIF per group\n    results = {}\n    for mtype in [\"base\", \"instruct\"]:\n        ri, fi = groups[mtype][\"ref_idx\"], groups[mtype][\"foc_idx\"]\n        print(f\"\\nRunning MH-DIF for {mtype} ({len(ri)} ref, {len(fi)} foc)...\")\n        X_ref = X[ri]\n        X_foc = X[fi]\n        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)\n        results[mtype] = {\"c_pct\": c_pct, \"delta\": delta, \"pval\": pval, \"is_c\": is_c}\n        print(f\"  C% = {c_pct:.1f}%  ({is_c.sum()}/{len(is_c)} items)\")\n\n    # ── Part 3a: Bootstrap CI for C% difference ──────────────────────────\n    print(\"\\n=== Part 3a: Bootstrap C% difference ===\")\n    rng = np.random.default_rng(42)\n    boot_diff = np.zeros(N_BOOT)\n\n    for b in range(N_BOOT):\n        if (b + 1) % 200 == 0:\n            print(f\"  bootstrap {b+1}/{N_BOOT}...\")\n        cpcts = {}\n        for mtype in [\"base\", \"instruct\"]:\n            ri, fi = groups[mtype][\"ref_idx\"], groups[mtype][\"foc_idx\"]\n            ri_b = rng.choice(ri, size=len(ri), replace=True)\n            fi_b = rng.choice(fi, size=len(fi), replace=True)\n            c, _, _, _ = mh_dif_full(X[ri_b], X[fi_b])\n            cpcts[mtype] = c\n        boot_diff[b] = cpcts[\"base\"] - cpcts[\"instruct\"]\n\n    ci_lo, ci_hi = np.percentile(boot_diff, [2.5, 97.5])\n    mean_diff = boot_diff.mean()\n    print(f\"  C%_base - C%_instruct = {results['base']['c_pct']:.1f} - {results['instruct']['c_pct']:.1f} = {results['base']['c_pct'] - results['instruct']['c_pct']:.1f}\")\n    print(f\"  Bootstrap 95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]\")\n\n    # ── Part 3b: Difficulty-direction gradient ────────────────────────────\n    print(\"\\n=== Part 3b: Difficulty-direction gradient ===\")\n    all_2023_idx = meta.loc[meta[\"cohort_temporal\"] == \"2023\", \"rm_idx\"].values\n    X_2023 = X[all_2023_idx]\n    item_diff = np.asarray(X_2023.mean(axis=0), dtype=np.float64).ravel()\n\n    for mtype in [\"base\", \"instruct\"]:\n        c_mask = results[mtype][\"is_c\"]\n        if c_mask.sum() < 3:\n            print(f\"  {mtype}: too few C items ({c_mask.sum()}) for correlation\")\n            continue\n        rho, p = spearmanr(item_diff[c_mask], results[mtype][\"delta\"][c_mask])\n        print(f\"  {mtype}: ρ(difficulty, Δ_MH) = {rho:.3f}  (p={p:.2e}, n={c_mask.sum()})\")\n\n    # ── Part 3c: DIF item overlap ─────────────────────────────────────────\n    print(\"\\n=== Part 3c: DIF item overlap ===\")\n    c_base = set(np.where(results[\"base\"][\"is_c\"])[0])\n    c_inst = set(np.where(results[\"instruct\"][\"is_c\"])[0])\n    inter = c_base & c_inst\n    union = c_base | c_inst\n    jaccard = len(inter) / len(union) if union else 0\n\n    p_b = len(c_base) / len(item_ids)\n    p_i = len(c_inst) / len(item_ids)\n    expected_jaccard = (p_b * p_i) / (p_b + p_i - p_b * p_i) if (p_b + p_i - p_b * p_i) > 0 else 0\n\n    only_base = len(c_base - c_inst)\n    only_inst = len(c_inst - c_base)\n    both = len(inter)\n    print(f\"  |C_base|={len(c_base)}, |C_instruct|={len(c_inst)}\")\n    print(f\"  Only base: {only_base}, Only instruct: {only_inst}, Both: {both}\")\n    print(f\"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})\")\n\n    # ── Part 3d: Direction distribution ───────────────────────────────────\n    print(\"\\n=== Part 3d: DIF direction distribution ===\")\n    dir_table = {}\n    for mtype in [\"base\", \"instruct\"]:\n        d = results[mtype][\"delta\"][results[mtype][\"is_c\"]]\n        n_foc_fav = (d > 0).sum()\n        n_ref_fav = (d < 0).sum()\n        dir_table[mtype] = (int(n_foc_fav), int(n_ref_fav))\n        total = n_foc_fav + n_ref_fav\n        print(f\"  {mtype}: focal-favoring={n_foc_fav} ({n_foc_fav/total*100:.1f}%), ref-favoring={n_ref_fav} ({n_ref_fav/total*100:.1f}%)\")\n\n    ct = np.array([[dir_table[\"base\"][0], dir_table[\"base\"][1]],\n                    [dir_table[\"instruct\"][0], dir_table[\"instruct\"][1]]])\n    if ct.min() > 0:\n        chi2_val, p_dir, _, _ = chi2_contingency(ct)\n        print(f\"  χ²={chi2_val:.2f}, p={p_dir:.3e}\")\n    else:\n        p_dir = np.nan\n        print(\"  χ² test not possible (zero cell)\")\n\n    # ── Save per-item CSV ─────────────────────────────────────────────────\n    print(\"\\nSaving per-item results...\")\n\n    # Extract subject from item_id (format: subject_qXXXX or similar)\n    def get_subject(iid):\n        parts = iid.rsplit(\"_\", 1)\n        return parts[0] if len(parts) > 1 else iid\n\n    item_df = pd.DataFrame({\n        \"item_id\": item_ids,\n        \"subject\": [get_subject(str(i)) for i in item_ids],\n        \"difficulty\": item_diff,\n        \"delta_mh_base\": results[\"base\"][\"delta\"],\n        \"p_base\": results[\"base\"][\"pval\"],\n        \"ets_base\": [ets_class(d) for d in results[\"base\"][\"delta\"]],\n        \"is_c_base\": results[\"base\"][\"is_c\"],\n        \"delta_mh_instruct\": results[\"instruct\"][\"delta\"],\n        \"p_instruct\": results[\"instruct\"][\"pval\"],\n        \"ets_instruct\": [ets_class(d) for d in results[\"instruct\"][\"delta\"]],\n        \"is_c_instruct\": results[\"instruct\"][\"is_c\"],\n    })\n    item_df.to_csv(f\"{OUT}/base_instruct_item_results.csv\", index=False)\n\n    # ── Generate report ───────────────────────────────────────────────────\n    print(\"Writing report...\")\n\n    n_base_ref = len(groups[\"base\"][\"ref_idx\"])\n    n_base_foc = len(groups[\"base\"][\"foc_idx\"])\n    n_inst_ref = len(groups[\"instruct\"][\"ref_idx\"])\n    n_inst_foc = len(groups[\"instruct\"][\"foc_idx\"])\n\n    report = f\"\"\"# R18: Base vs Instruct DIF Separation Experiment\n\n## Sample Sizes\n\n| Group | Ref (2023) | Foc (2024) | Total |\n|-------|-----------|-----------|-------|\n| Base | {n_base_ref} | {n_base_foc} | {n_base_ref + n_base_foc} |\n| Instruct | {n_inst_ref} | {n_inst_foc} | {n_inst_ref + n_inst_foc} |\n| Full (reported) | 1,080 | 807 | 1,887 |\n\n{\"**⚠ Warning:** Some subgroups have N < 80; interpret with caution.\" if min(n_base_ref, n_base_foc, n_inst_ref, n_inst_foc) < 80 else \"All subgroups have N ≥ 80; adequate power.\"}\n\n## C% Comparison\n\n| Group | C% | DIF-C items |\n|-------|-----|------------|\n| Base | {results['base']['c_pct']:.1f}% | {results['base']['is_c'].sum()}/{len(item_ids)} |\n| Instruct | {results['instruct']['c_pct']:.1f}% | {results['instruct']['is_c'].sum()}/{len(item_ids)} |\n| Full (reported) | 31.3% | — |\n\n**Difference (base − instruct):** {results['base']['c_pct'] - results['instruct']['c_pct']:.1f} pp\n**Bootstrap 95% CI:** [{ci_lo:.1f}, {ci_hi:.1f}] (N={N_BOOT})\n\n## Difficulty–Direction Gradient\n\nSpearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:\n\n\"\"\"\n\n    for mtype in [\"base\", \"instruct\"]:\n        c_mask = results[mtype][\"is_c\"]\n        if c_mask.sum() >= 3:\n            rho, p = spearmanr(item_diff[c_mask], results[mtype][\"delta\"][c_mask])\n            report += f\"- **{mtype.capitalize()}:** ρ = {rho:.3f} (p = {p:.2e}, n = {c_mask.sum()})\\n\"\n        else:\n            report += f\"- **{mtype.capitalize()}:** too few C items ({c_mask.sum()}) for correlation\\n\"\n\n    report += f\"\"\"\n## DIF Item Overlap\n\n| Metric | Value |\n|--------|-------|\n| C_base only | {only_base} |\n| C_instruct only | {only_inst} |\n| Both | {both} |\n| Jaccard index | {jaccard:.3f} |\n| Expected Jaccard (independence) | {expected_jaccard:.3f} |\n| Jaccard / Expected ratio | {jaccard / expected_jaccard:.1f}× |\n\n## DIF Direction Distribution\n\n| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |\n|-------|----------------------|---------------------|\n| Base | {dir_table['base'][0]} ({dir_table['base'][0]/(sum(dir_table['base']))*100:.1f}%) | {dir_table['base'][1]} ({dir_table['base'][1]/(sum(dir_table['base']))*100:.1f}%) |\n| Instruct | {dir_table['instruct'][0]} ({dir_table['instruct'][0]/(sum(dir_table['instruct']))*100:.1f}%) | {dir_table['instruct'][1]} ({dir_table['instruct'][1]/(sum(dir_table['instruct']))*100:.1f}%) |\n\nχ² = {chi2_val:.2f}, p = {p_dir:.3e}\n\n## Output Files\n\n- `model_classification.csv` — {len(class_df)} models classified\n- `base_instruct_item_results.csv` — {len(item_ids)} items with per-group DIF statistics\n\"\"\"\n\n    with open(f\"{OUT}/base_instruct_dif_report.md\", \"w\") as f:\n        f.write(report)\n\n    print(f\"\\nDone. Results in {OUT}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "98d068cb-9f99-413e-b290-7cce58ba9dfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EY4yrq3e8EkNrRfjDiQxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 138,
      "cache_read_input_tokens": 28640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 138
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

_source line 30 · 2026-05-22T17:47:40.410Z_

<details><summary>↩ Tool result · `toolu_01J1c1TBWBSFZ66aCJsCtSND`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "ef7f5610-c14f-4586-b209-6cfb63988113",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
    "content": "#!/usr/bin/env python3\n\"\"\"R18: Base vs Instruct MH-DIF separation experiment.\"\"\"\n\nimport re\nimport sys\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r18_base_vs_instruct_dif\"\n\nN_STRATA = 5\nN_BOOT = 1000\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n# ── Part 1: Model classification ─────────────────────────────────────────\n\nINSTRUCT_SUFFIXES = re.compile(\n    r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)\"\n    r\"([-_\\.]|$)\",\n    re.IGNORECASE,\n)\n\nQUANT_SUFFIXES = re.compile(\n    r\"[-_\\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])\",\n    re.IGNORECASE,\n)\n\nFAMILY_PREFIX_EXCLUDE = re.compile(\n    r\"^(openchat|chatglm|chatml)\",\n    re.IGNORECASE,\n)\n\n\ndef classify_model(name: str) -> str:\n    short = name.split(\"/\")[-1] if \"/\" in name else name\n    stripped = QUANT_SUFFIXES.sub(\"\", short)\n\n    if stripped.lower().endswith(\"-it\"):\n        return \"instruct\"\n\n    if INSTRUCT_SUFFIXES.search(stripped):\n        prefix_part = stripped.split(\"-\")[0].split(\"_\")[0]\n        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):\n            rest = stripped[len(prefix_part):]\n            if not INSTRUCT_SUFFIXES.search(rest):\n                return \"base\"\n        return \"instruct\"\n\n    return \"base\"\n\n\n# ── Part 2: MH-DIF (extended) ────────────────────────────────────────────\n\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\n\n    Returns (c_pct, delta_mh, pval, is_c).\n    \"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = k_ref == k\n        mf = k_foc == k\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()\n        if mf.any():\n            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)\n    c_pct = is_c.sum() / J * 100\n\n    return c_pct, delta_j, pval_j, is_c\n\n\ndef ets_class(delta):\n    a = abs(delta)\n    if a < 1.0:\n        return \"A\"\n    elif a < 1.5:\n        return \"B\"\n    else:\n        return \"C\"\n\n\n# ── Main ──────────────────────────────────────────────────────────────────\n\ndef main():\n    print(\"Loading data...\")\n    meta = pd.read_csv(f\"{ROOT}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n    rm = np.load(f\"{ROOT}/response_matrix.npz\")\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]), shape=tuple(rm[\"shape\"]))\n    idx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n\n    # Build model name → row index lookup\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Classify models\n    meta = meta[meta[\"cohort_temporal\"].isin([\"2023\", \"2024\"])].copy()\n    meta[\"model_type\"] = meta[\"model_name\"].apply(classify_model)\n\n    # Save classification\n    class_df = meta[[\"model_name\", \"model_type\", \"cohort_temporal\", \"family\"]].copy()\n    class_df.to_csv(f\"{OUT}/model_classification.csv\", index=False)\n\n    # Map to response matrix rows\n    meta[\"rm_idx\"] = meta[\"model_name\"].map(name2row)\n    meta = meta.dropna(subset=[\"rm_idx\"])\n    meta[\"rm_idx\"] = meta[\"rm_idx\"].astype(int)\n\n    # Group counts\n    groups = {}\n    for mtype in [\"base\", \"instruct\"]:\n        ref_mask = (meta[\"model_type\"] == mtype) & (meta[\"cohort_temporal\"] == \"2023\")\n        foc_mask = (meta[\"model_type\"] == mtype) & (meta[\"cohort_temporal\"] == \"2024\")\n        groups[mtype] = {\n            \"ref_idx\": meta.loc[ref_mask, \"rm_idx\"].values,\n            \"foc_idx\": meta.loc[foc_mask, \"rm_idx\"].values,\n        }\n\n    print(\"\\n=== Part 4: Sample sizes ===\")\n    for mtype in [\"base\", \"instruct\"]:\n        n_ref = len(groups[mtype][\"ref_idx\"])\n        n_foc = len(groups[mtype][\"foc_idx\"])\n        flag = \" ⚠ UNDERPOWERED\" if min(n_ref, n_foc) < 80 else \"\"\n        print(f\"  {mtype:>10s}: ref(2023)={n_ref}, foc(2024)={n_foc}{flag}\")\n    print(f\"  {'full':>10s}: ref(2023)=1080, foc(2024)=807  (reported baseline)\")\n\n    # Run MH-DIF per group\n    results = {}\n    for mtype in [\"base\", \"instruct\"]:\n        ri, fi = groups[mtype][\"ref_idx\"], groups[mtype][\"foc_idx\"]\n        print(f\"\\nRunning MH-DIF for {mtype} ({len(ri)} ref, {len(fi)} foc)...\")\n        X_ref = X[ri]\n        X_foc = X[fi]\n        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)\n        results[mtype] = {\"c_pct\": c_pct, \"delta\": delta, \"pval\": pval, \"is_c\": is_c}\n        print(f\"  C% = {c_pct:.1f}%  ({is_c.sum()}/{len(is_c)} items)\")\n\n    # ── Part 3a: Bootstrap CI for C% difference ──────────────────────────\n    print(\"\\n=== Part 3a: Bootstrap C% difference ===\")\n    rng = np.random.default_rng(42)\n    boot_diff = np.zeros(N_BOOT)\n\n    for b in range(N_BOOT):\n        if (b + 1) % 200 == 0:\n            print(f\"  bootstrap {b+1}/{N_BOOT}...\")\n        cpcts = {}\n        for mtype in [\"base\", \"instruct\"]:\n            ri, fi = groups[mtype][\"ref_idx\"], groups[mtype][\"foc_idx\"]\n            ri_b = rng.choice(ri, size=len(ri), replace=True)\n            fi_b = rng.choice(fi, size=len(fi), replace=True)\n            c, _, _, _ = mh_dif_full(X[ri_b], X[fi_b])\n            cpcts[mtype] = c\n        boot_diff[b] = cpcts[\"base\"] - cpcts[\"instruct\"]\n\n    ci_lo, ci_hi = np.percentile(boot_diff, [2.5, 97.5])\n    mean_diff = boot_diff.mean()\n    print(f\"  C%_base - C%_instruct = {results['base']['c_pct']:.1f} - {results['instruct']['c_pct']:.1f} = {results['base']['c_pct'] - results['instruct']['c_pct']:.1f}\")\n    print(f\"  Bootstrap 95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]\")\n\n    # ── Part 3b: Difficulty-direction gradient ────────────────────────────\n    print(\"\\n=== Part 3b: Difficulty-direction gradient ===\")\n    all_2023_idx = meta.loc[meta[\"cohort_temporal\"] == \"2023\", \"rm_idx\"].values\n    X_2023 = X[all_2023_idx]\n    item_diff = np.asarray(X_2023.mean(axis=0), dtype=np.float64).ravel()\n\n    for mtype in [\"base\", \"instruct\"]:\n        c_mask = results[mtype][\"is_c\"]\n        if c_mask.sum() < 3:\n            print(f\"  {mtype}: too few C items ({c_mask.sum()}) for correlation\")\n            continue\n        rho, p = spearmanr(item_diff[c_mask], results[mtype][\"delta\"][c_mask])\n        print(f\"  {mtype}: ρ(difficulty, Δ_MH) = {rho:.3f}  (p={p:.2e}, n={c_mask.sum()})\")\n\n    # ── Part 3c: DIF item overlap ─────────────────────────────────────────\n    print(\"\\n=== Part 3c: DIF item overlap ===\")\n    c_base = set(np.where(results[\"base\"][\"is_c\"])[0])\n    c_inst = set(np.where(results[\"instruct\"][\"is_c\"])[0])\n    inter = c_base & c_inst\n    union = c_base | c_inst\n    jaccard = len(inter) / len(union) if union else 0\n\n    p_b = len(c_base) / len(item_ids)\n    p_i = len(c_inst) / len(item_ids)\n    expected_jaccard = (p_b * p_i) / (p_b + p_i - p_b * p_i) if (p_b + p_i - p_b * p_i) > 0 else 0\n\n    only_base = len(c_base - c_inst)\n    only_inst = len(c_inst - c_base)\n    both = len(inter)\n    print(f\"  |C_base|={len(c_base)}, |C_instruct|={len(c_inst)}\")\n    print(f\"  Only base: {only_base}, Only instruct: {only_inst}, Both: {both}\")\n    print(f\"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})\")\n\n    # ── Part 3d: Direction distribution ───────────────────────────────────\n    print(\"\\n=== Part 3d: DIF direction distribution ===\")\n    dir_table = {}\n    for mtype in [\"base\", \"instruct\"]:\n        d = results[mtype][\"delta\"][results[mtype][\"is_c\"]]\n        n_foc_fav = (d > 0).sum()\n        n_ref_fav = (d < 0).sum()\n        dir_table[mtype] = (int(n_foc_fav), int(n_ref_fav))\n        total = n_foc_fav + n_ref_fav\n        print(f\"  {mtype}: focal-favoring={n_foc_fav} ({n_foc_fav/total*100:.1f}%), ref-favoring={n_ref_fav} ({n_ref_fav/total*100:.1f}%)\")\n\n    ct = np.array([[dir_table[\"base\"][0], dir_table[\"base\"][1]],\n                    [dir_table[\"instruct\"][0], dir_table[\"instruct\"][1]]])\n    if ct.min() > 0:\n        chi2_val, p_dir, _, _ = chi2_contingency(ct)\n        print(f\"  χ²={chi2_val:.2f}, p={p_dir:.3e}\")\n    else:\n        p_dir = np.nan\n        print(\"  χ² test not possible (zero cell)\")\n\n    # ── Save per-item CSV ─────────────────────────────────────────────────\n    print(\"\\nSaving per-item results...\")\n\n    # Extract subject from item_id (format: subject_qXXXX or similar)\n    def get_subject(iid):\n        parts = iid.rsplit(\"_\", 1)\n        return parts[0] if len(parts) > 1 else iid\n\n    item_df = pd.DataFrame({\n        \"item_id\": item_ids,\n        \"subject\": [get_subject(str(i)) for i in item_ids],\n        \"difficulty\": item_diff,\n        \"delta_mh_base\": results[\"base\"][\"delta\"],\n        \"p_base\": results[\"base\"][\"pval\"],\n        \"ets_base\": [ets_class(d) for d in results[\"base\"][\"delta\"]],\n        \"is_c_base\": results[\"base\"][\"is_c\"],\n        \"delta_mh_instruct\": results[\"instruct\"][\"delta\"],\n        \"p_instruct\": results[\"instruct\"][\"pval\"],\n        \"ets_instruct\": [ets_class(d) for d in results[\"instruct\"][\"delta\"]],\n        \"is_c_instruct\": results[\"instruct\"][\"is_c\"],\n    })\n    item_df.to_csv(f\"{OUT}/base_instruct_item_results.csv\", index=False)\n\n    # ── Generate report ───────────────────────────────────────────────────\n    print(\"Writing report...\")\n\n    n_base_ref = len(groups[\"base\"][\"ref_idx\"])\n    n_base_foc = len(groups[\"base\"][\"foc_idx\"])\n    n_inst_ref = len(groups[\"instruct\"][\"ref_idx\"])\n    n_inst_foc = len(groups[\"instruct\"][\"foc_idx\"])\n\n    report = f\"\"\"# R18: Base vs Instruct DIF Separation Experiment\n\n## Sample Sizes\n\n| Group | Ref (2023) | Foc (2024) | Total |\n|-------|-----------|-----------|-------|\n| Base | {n_base_ref} | {n_base_foc} | {n_base_ref + n_base_foc} |\n| Instruct | {n_inst_ref} | {n_inst_foc} | {n_inst_ref + n_inst_foc} |\n| Full (reported) | 1,080 | 807 | 1,887 |\n\n{\"**⚠ Warning:** Some subgroups have N < 80; interpret with caution.\" if min(n_base_ref, n_base_foc, n_inst_ref, n_inst_foc) < 80 else \"All subgroups have N ≥ 80; adequate power.\"}\n\n## C% Comparison\n\n| Group | C% | DIF-C items |\n|-------|-----|------------|\n| Base | {results['base']['c_pct']:.1f}% | {results['base']['is_c'].sum()}/{len(item_ids)} |\n| Instruct | {results['instruct']['c_pct']:.1f}% | {results['instruct']['is_c'].sum()}/{len(item_ids)} |\n| Full (reported) | 31.3% | — |\n\n**Difference (base − instruct):** {results['base']['c_pct'] - results['instruct']['c_pct']:.1f} pp\n**Bootstrap 95% CI:** [{ci_lo:.1f}, {ci_hi:.1f}] (N={N_BOOT})\n\n## Difficulty–Direction Gradient\n\nSpearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:\n\n\"\"\"\n\n    for mtype in [\"base\", \"instruct\"]:\n        c_mask = results[mtype][\"is_c\"]\n        if c_mask.sum() >= 3:\n            rho, p = spearmanr(item_diff[c_mask], results[mtype][\"delta\"][c_mask])\n            report += f\"- **{mtype.capitalize()}:** ρ = {rho:.3f} (p = {p:.2e}, n = {c_mask.sum()})\\n\"\n        else:\n            report += f\"- **{mtype.capitalize()}:** too few C items ({c_mask.sum()}) for correlation\\n\"\n\n    report += f\"\"\"\n## DIF Item Overlap\n\n| Metric | Value |\n|--------|-------|\n| C_base only | {only_base} |\n| C_instruct only | {only_inst} |\n| Both | {both} |\n| Jaccard index | {jaccard:.3f} |\n| Expected Jaccard (independence) | {expected_jaccard:.3f} |\n| Jaccard / Expected ratio | {jaccard / expected_jaccard:.1f}× |\n\n## DIF Direction Distribution\n\n| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |\n|-------|----------------------|---------------------|\n| Base | {dir_table['base'][0]} ({dir_table['base'][0]/(sum(dir_table['base']))*100:.1f}%) | {dir_table['base'][1]} ({dir_table['base'][1]/(sum(dir_table['base']))*100:.1f}%) |\n| Instruct | {dir_table['instruct'][0]} ({dir_table['instruct'][0]/(sum(dir_table['instruct']))*100:.1f}%) | {dir_table['instruct'][1]} ({dir_table['instruct'][1]/(sum(dir_table['instruct']))*100:.1f}%) |\n\nχ² = {chi2_val:.2f}, p = {p_dir:.3e}\n\n## Output Files\n\n- `model_classification.csv` — {len(class_df)} models classified\n- `base_instruct_item_results.csv` — {len(item_ids)} items with per-group DIF statistics\n\"\"\"\n\n    with open(f\"{OUT}/base_instruct_dif_report.md\", \"w\") as f:\n        f.write(report)\n\n    print(f\"\\nDone. Results in {OUT}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 31_

运行脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "d16a313e-cdf8-4725-86ef-be0e6a8fa9ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9ZUdkXTVUfjRSV5N4nZVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5847,
      "cache_read_input_tokens": 28778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5847
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01WfZH1LrnwFFMtJAV7yWyFt`</summary>

```json
{
  "command": "python3 artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "description": "Run base vs instruct DIF analysis",
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
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "7156e7ce-d98d-43ff-9e4d-5a93f90afb4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9ZUdkXTVUfjRSV5N4nZVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5847,
      "cache_read_input_tokens": 28778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5847
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

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bq5qxyz67",
  "tool_use_id": "toolu_01WfZH1LrnwFFMtJAV7yWyFt",
  "description": "Run base vs instruct DIF analysis",
  "task_type": "local_bash",
  "uuid": "d01b1407-7909-4826-97d7-93d5d10ee62d",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bq5qxyz67",
  "tool_use_id": "toolu_01WfZH1LrnwFFMtJAV7yWyFt",
  "status": "completed",
  "output_file": "",
  "summary": "Run base vs instruct DIF analysis",
  "uuid": "ef9daf6e-2a78-4769-bd6b-bcbd8fd84b7e",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813"
}
```

---

### Tool result

_source line 35 · 2026-05-22T17:51:37.815Z_

<details><summary>↩ Tool result · `toolu_01WfZH1LrnwFFMtJAV7yWyFt`</summary>

```text
Loading data...

=== Part 4: Sample sizes ===
        base: ref(2023)=861, foc(2024)=548
    instruct: ref(2023)=219, foc(2024)=259
        full: ref(2023)=1080, foc(2024)=807  (reported baseline)

Running MH-DIF for base (861 ref, 548 foc)...
  C% = 32.1%  (4018/12508 items)

Running MH-DIF for instruct (219 ref, 259 foc)...
  C% = 36.5%  (4567/12508 items)

=== Part 3a: Bootstrap C% difference ===
  bootstrap 200/1000...
  bootstrap 400/1000...
  bootstrap 600/1000...
  bootstrap 800/1000...
  bootstrap 1000/1000...
  C%_base - C%_instruct = 32.1 - 36.5 = -4.4
  Bootstrap 95% CI: [-13.4, 4.3]

=== Part 3b: Difficulty-direction gradient ===
  base: ρ(difficulty, Δ_MH) = -0.570  (p=0.00e+00, n=4018)
  instruct: ρ(difficulty, Δ_MH) = -0.079  (p=1.02e-07, n=4567)

=== Part 3c: DIF item overlap ===
  |C_base|=4018, |C_instruct|=4567
  Only base: 1965, Only instruct: 2514, Both: 2053
  Jaccard = 0.314  (expected under independence: 0.206)

=== Part 3d: DIF direction distribution ===
  base: focal-favoring=1605 (39.9%), ref-favoring=2413 (60.1%)
  instruct: focal-favoring=2994 (65.6%), ref-favoring=1573 (34.4%)
  χ²=562.70, p=2.178e-124

Saving per-item results...
Writing report...

Done. Results in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "347bbe82-6b6a-4321-8040-6f21da21beda",
  "tool_use_result": {
    "stdout": "Loading data...\n\n=== Part 4: Sample sizes ===\n        base: ref(2023)=861, foc(2024)=548\n    instruct: ref(2023)=219, foc(2024)=259\n        full: ref(2023)=1080, foc(2024)=807  (reported baseline)\n\nRunning MH-DIF for base (861 ref, 548 foc)...\n  C% = 32.1%  (4018/12508 items)\n\nRunning MH-DIF for instruct (219 ref, 259 foc)...\n  C% = 36.5%  (4567/12508 items)\n\n=== Part 3a: Bootstrap C% difference ===\n  bootstrap 200/1000...\n  bootstrap 400/1000...\n  bootstrap 600/1000...\n  bootstrap 800/1000...\n  bootstrap 1000/1000...\n  C%_base - C%_instruct = 32.1 - 36.5 = -4.4\n  Bootstrap 95% CI: [-13.4, 4.3]\n\n=== Part 3b: Difficulty-direction gradient ===\n  base: ρ(difficulty, Δ_MH) = -0.570  (p=0.00e+00, n=4018)\n  instruct: ρ(difficulty, Δ_MH) = -0.079  (p=1.02e-07, n=4567)\n\n=== Part 3c: DIF item overlap ===\n  |C_base|=4018, |C_instruct|=4567\n  Only base: 1965, Only instruct: 2514, Both: 2053\n  Jaccard = 0.314  (expected under independence: 0.206)\n\n=== Part 3d: DIF direction distribution ===\n  base: focal-favoring=1605 (39.9%), ref-favoring=2413 (60.1%)\n  instruct: focal-favoring=2994 (65.6%), ref-favoring=1573 (34.4%)\n  χ²=562.70, p=2.178e-124\n\nSaving per-item results...\nWriting report...\n\nDone. Results in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/",
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

_source line 36_

运行完成。检查产出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "4c2f1633-1e53-4317-94e3-878fba75d94e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DShEWfVsyywp73xHgrkUKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 34625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 737
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01RwnqocFMfAdC5Tj9bUoHao`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "d11b6c81-e35d-4b66-9cd8-8ca6e1597df1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DShEWfVsyywp73xHgrkUKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 34625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 737
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

_source line 38 · 2026-05-22T17:51:41.071Z_

<details><summary>↩ Tool result · `toolu_01RwnqocFMfAdC5Tj9bUoHao`</summary>

```text
1	# R18: Base vs Instruct DIF Separation Experiment
2	
3	## Sample Sizes
4	
5	| Group | Ref (2023) | Foc (2024) | Total |
6	|-------|-----------|-----------|-------|
7	| Base | 861 | 548 | 1409 |
8	| Instruct | 219 | 259 | 478 |
9	| Full (reported) | 1,080 | 807 | 1,887 |
10	
11	All subgroups have N ≥ 80; adequate power.
12	
13	## C% Comparison
14	
15	| Group | C% | DIF-C items |
16	|-------|-----|------------|
17	| Base | 32.1% | 4018/12508 |
18	| Instruct | 36.5% | 4567/12508 |
19	| Full (reported) | 31.3% | — |
20	
21	**Difference (base − instruct):** -4.4 pp
22	**Bootstrap 95% CI:** [-13.4, 4.3] (N=1000)
23	
24	## Difficulty–Direction Gradient
25	
26	Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:
27	
28	- **Base:** ρ = -0.570 (p = 0.00e+00, n = 4018)
29	- **Instruct:** ρ = -0.079 (p = 1.02e-07, n = 4567)
30	
31	## DIF Item Overlap
32	
33	| Metric | Value |
34	|--------|-------|
35	| C_base only | 1965 |
36	| C_instruct only | 2514 |
37	| Both | 2053 |
38	| Jaccard index | 0.314 |
39	| Expected Jaccard (independence) | 0.206 |
40	| Jaccard / Expected ratio | 1.5× |
41	
42	## DIF Direction Distribution
43	
44	| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
45	|-------|----------------------|---------------------|
46	| Base | 1605 (39.9%) | 2413 (60.1%) |
47	| Instruct | 2994 (65.6%) | 1573 (34.4%) |
48	
49	χ² = 562.70, p = 2.178e-124
50	
51	## Output Files
52	
53	- `model_classification.csv` — 1887 models classified
54	- `base_instruct_item_results.csv` — 12508 items with per-group DIF statistics
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "a4f60e42-4164-4b76-9872-7092b28e133d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md",
      "content": "# R18: Base vs Instruct DIF Separation Experiment\n\n## Sample Sizes\n\n| Group | Ref (2023) | Foc (2024) | Total |\n|-------|-----------|-----------|-------|\n| Base | 861 | 548 | 1409 |\n| Instruct | 219 | 259 | 478 |\n| Full (reported) | 1,080 | 807 | 1,887 |\n\nAll subgroups have N ≥ 80; adequate power.\n\n## C% Comparison\n\n| Group | C% | DIF-C items |\n|-------|-----|------------|\n| Base | 32.1% | 4018/12508 |\n| Instruct | 36.5% | 4567/12508 |\n| Full (reported) | 31.3% | — |\n\n**Difference (base − instruct):** -4.4 pp\n**Bootstrap 95% CI:** [-13.4, 4.3] (N=1000)\n\n## Difficulty–Direction Gradient\n\nSpearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:\n\n- **Base:** ρ = -0.570 (p = 0.00e+00, n = 4018)\n- **Instruct:** ρ = -0.079 (p = 1.02e-07, n = 4567)\n\n## DIF Item Overlap\n\n| Metric | Value |\n|--------|-------|\n| C_base only | 1965 |\n| C_instruct only | 2514 |\n| Both | 2053 |\n| Jaccard index | 0.314 |\n| Expected Jaccard (independence) | 0.206 |\n| Jaccard / Expected ratio | 1.5× |\n\n## DIF Direction Distribution\n\n| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |\n|-------|----------------------|---------------------|\n| Base | 1605 (39.9%) | 2413 (60.1%) |\n| Instruct | 2994 (65.6%) | 1573 (34.4%) |\n\nχ² = 562.70, p = 2.178e-124\n\n## Output Files\n\n- `model_classification.csv` — 1887 models classified\n- `base_instruct_item_results.csv` — 12508 items with per-group DIF statistics\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01QaiqvmmaS5tNyAxByJ27Vz`</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv && echo \"---\" && head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv",
  "description": "Check CSV outputs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "b1ce0ac8-6669-4c53-840b-1e9f69a52dbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQYCwpx8vKp85iiNJXqEVV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 35362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 868
      },
      "output_tokens": 56,
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

_source line 40 · 2026-05-22T17:51:44.134Z_

<details><summary>↩ Tool result · `toolu_01QaiqvmmaS5tNyAxByJ27Vz`</summary>

```text
model_name,model_type,cohort_temporal,family
01-ai/Yi-1.5-34B,base,2024,yi-1.5
01-ai/Yi-1.5-34B-32K,base,2024,yi-1.5
01-ai/Yi-1.5-34B-Chat,instruct,2024,yi-1.5
01-ai/Yi-1.5-34B-Chat-16K,instruct,2024,yi-1.5
---
item_id,subject,difficulty,delta_mh_base,p_base,ets_base,is_c_base,delta_mh_instruct,p_instruct,ets_instruct,is_c_instruct
abstract_algebra.1,abstract,0.22037037037036922,0.5164981792551308,0.15231987161258398,A,False,-0.06348637436343886,1.0,A,False
abstract_algebra.10,abstract,0.07962962962962972,1.0738643316687086,0.01021045061688619,B,False,5.129733084585753,1.3209308746708892e-05,C,True
abstract_algebra.100,abstract,0.05370370370370375,1.743154620463568,0.0002863222906126506,C,True,5.480152433415236,0.0013550047192921744,C,True
abstract_algebra.11,abstract,0.6472222222222184,0.7522047960198835,0.010164602175935289,A,False,0.593784770139804,0.29792734454822223,A,False
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "f3865627-f91b-4bc3-9067-019a6b641298",
  "tool_use_result": {
    "stdout": "model_name,model_type,cohort_temporal,family\n01-ai/Yi-1.5-34B,base,2024,yi-1.5\n01-ai/Yi-1.5-34B-32K,base,2024,yi-1.5\n01-ai/Yi-1.5-34B-Chat,instruct,2024,yi-1.5\n01-ai/Yi-1.5-34B-Chat-16K,instruct,2024,yi-1.5\n---\nitem_id,subject,difficulty,delta_mh_base,p_base,ets_base,is_c_base,delta_mh_instruct,p_instruct,ets_instruct,is_c_instruct\nabstract_algebra.1,abstract,0.22037037037036922,0.5164981792551308,0.15231987161258398,A,False,-0.06348637436343886,1.0,A,False\nabstract_algebra.10,abstract,0.07962962962962972,1.0738643316687086,0.01021045061688619,B,False,5.129733084585753,1.3209308746708892e-05,C,True\nabstract_algebra.100,abstract,0.05370370370370375,1.743154620463568,0.0002863222906126506,C,True,5.480152433415236,0.0013550047192921744,C,True\nabstract_algebra.11,abstract,0.6472222222222184,0.7522047960198835,0.010164602175935289,A,False,0.593784770139804,0.29792734454822223,A,False",
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

_source line 41_

全部完成。三个产出文件均已生成。

**核心发现：**

| 指标 | Base | Instruct |
|------|------|----------|
| 样本量 | 861+548=1409 | 219+259=478 |
| C% | 32.1% | 36.5% |
| ρ(difficulty, Δ_MH) | **−0.570** | −0.079 |
| DIF 方向 | 60.1% ref-favoring | 65.6% focal-favoring |

关键解读：
1. **C% 差异不显著**（−4.4 pp, 95% CI [−13.4, 4.3] 包含 0），instruct 稍高但 bootstrap CI 宽
2. **Difficulty gradient 差异极大**：base 组 ρ=−0.57（容易题 DIF 大），instruct 组几乎无梯度（ρ=−0.08）——说明 base 和 instruct 的 DIF 机制不同
3. **方向完全相反**：base 组以 ref-favoring（2023↑）为主，instruct 组以 focal-favoring（2024↑）为主，χ²=562.7, p<10⁻¹²⁴
4. **Overlap 中等** (Jaccard=0.314, 1.5× 独立基线)：约一半 DIF items 是 group-specific 的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "uuid": "5127e42b-3af1-4671-8384-4ff1f1e37cdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtJrXkopS3V11ms5zNsBJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 36230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

_source line 42_

全部完成。三个产出文件均已生成。

**核心发现：**

| 指标 | Base | Instruct |
|------|------|----------|
| 样本量 | 861+548=1409 | 219+259=478 |
| C% | 32.1% | 36.5% |
| ρ(difficulty, Δ_MH) | **−0.570** | −0.079 |
| DIF 方向 | 60.1% ref-favoring | 65.6% focal-favoring |

关键解读：
1. **C% 差异不显著**（−4.4 pp, 95% CI [−13.4, 4.3] 包含 0），instruct 稍高但 bootstrap CI 宽
2. **Difficulty gradient 差异极大**：base 组 ρ=−0.57（容易题 DIF 大），instruct 组几乎无梯度（ρ=−0.08）——说明 base 和 instruct 的 DIF 机制不同
3. **方向完全相反**：base 组以 ref-favoring（2023↑）为主，instruct 组以 focal-favoring（2024↑）为主，χ²=562.7, p<10⁻¹²⁴
4. **Overlap 中等** (Jaccard=0.314, 1.5× 独立基线)：约一半 DIF items 是 group-specific 的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 383184,
  "duration_api_ms": 148156,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "62e91bce-ecc8-42ef-bf44-a280a64e3813",
  "total_cost_usd": 0.49386470000000005,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 25119,
    "cache_read_input_tokens": 201408,
    "output_tokens": 7240,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25119,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 401,
        "cache_read_input_tokens": 36230,
        "cache_creation_input_tokens": 730,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 730
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2279,
      "outputTokens": 3147,
      "cacheReadInputTokens": 63492,
      "cacheCreationInputTokens": 24607,
      "webSearchRequests": 0,
      "costUSD": 0.05512195,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 7240,
      "cacheReadInputTokens": 201408,
      "cacheCreationInputTokens": 25119,
      "webSearchRequests": 0,
      "costUSD": 0.43874275,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "97b18dd5-c369-4b2c-9264-5528355ddb9e"
}
```

</details>

---
