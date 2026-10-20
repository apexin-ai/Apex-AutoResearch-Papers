# code r19 temporal granularity

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_code_r19_temporal_granularity_20260522T184726.log`
- **Structured JSON:** [`aef1bb177962ba5b1eb3.json`](../../sessions/ae/aef1bb177962ba5b1eb3.json)

## Before a recorded user message

6 recorded events

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
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
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
  "uuid": "4ce54de7-a8b3-4d25-b5b1-0cbe3af4ac49",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779493200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4ea79023-8260-4c36-bbfb-9404384953fb",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Assistant

_source line 4_

Looking at the existing MH-DIF implementation first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "2d87157e-0885-46c7-96d8-86a367acf296",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmSvZPsKQZRPuWCsRtBCge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13262,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13262
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

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01CtxEwUPze7ZAq2u166GLKh`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find MH-DIF function source",
  "prompt": "Find the full MH-DIF implementation in the codebase. Specifically:\n\n1. Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n2. Also look for any \"full version\" of this function that returns per-item delta_mh, p_value, is_c — check files in `artifacts/` subdirectories, especially anything related to R18 or base-vs-instruct.\n3. Read the model_metadata.csv header to confirm column names: `head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv`\n\nReturn the complete function code for both versions found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "9303b6f2-10e9-497e-b2c4-18e3a5a7ddc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmSvZPsKQZRPuWCsRtBCge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13262,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13262
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Find MH-DIF function source",
  "task_type": "local_agent",
  "prompt": "Find the full MH-DIF implementation in the codebase. Specifically:\n\n1. Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n2. Also look for any \"full version\" of this function that returns per-item delta_mh, p_value, is_c — check files in `artifacts/` subdirectories, especially anything related to R18 or base-vs-instruct.\n3. Read the model_metadata.csv header to confirm column names: `head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv`\n\nReturn the complete function code for both versions found.",
  "uuid": "e2ab9530-c0d4-47f3-962f-a560a24c3f51",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

## Round 1

72 recorded events

### User

_source line 7 · 2026-05-22T18:47:42.574Z_

Find the full MH-DIF implementation in the codebase. Specifically:

1. Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`
2. Also look for any "full version" of this function that returns per-item delta_mh, p_value, is_c — check files in `artifacts/` subdirectories, especially anything related to R18 or base-vs-instruct.
3. Read the model_metadata.csv header to confirm column names: `head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv`

Return the complete function code for both versions found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "53fcc4ec-731e-4bab-a0b9-b4995069ef0a"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Reading artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py",
  "usage": {
    "total_tokens": 15633,
    "tool_uses": 1,
    "duration_ms": 2387
  },
  "last_tool_name": "Read",
  "uuid": "501ef858-a436-4593-bc1b-7458e04b817a",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_018L2vkApBNkcGmqRKUvgysf`</summary>

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
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "3553f08b-7ac5-48d5-92c0-abbdbdb54a3a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GHvBsTJtcoBy8EJL9sswnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15614,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15614,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-22T18:47:44.992Z_

<details><summary>↩ Tool result · `toolu_018L2vkApBNkcGmqRKUvgysf`</summary>

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
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "9f9d2b45-4071-41a5-a0d8-871725114484"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Running head -3 /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 15641,
    "tool_uses": 2,
    "duration_ms": 2602
  },
  "last_tool_name": "Bash",
  "uuid": "e71f4317-9492-4d09-9738-e573cf859002",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01A1iBipMcUNLuchnCsnFzUo`</summary>

```json
{
  "command": "head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "340a022e-3e74-4908-a264-e8513a95744a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GHvBsTJtcoBy8EJL9sswnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15614,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15614,
        "ephemeral_1h_input_tokens": 0
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

_source line 13 · 2026-05-22T18:47:45.330Z_

<details><summary>↩ Tool result · `toolu_01A1iBipMcUNLuchnCsnFzUo`</summary>

```text
model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "7876eef3-9d98-4dac-8c1d-771e21062bce"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0520_2/p…",
  "usage": {
    "total_tokens": 15649,
    "tool_uses": 3,
    "duration_ms": 2877
  },
  "last_tool_name": "Glob",
  "uuid": "3ae41813-0e3e-44dc-9328-3c3eb4c484db",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_013LKDoGtY42xSW5M6DusoAB`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "3e6ced36-852f-49d7-9fad-66e6e65a0dcb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GHvBsTJtcoBy8EJL9sswnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15614,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15614,
        "ephemeral_1h_input_tokens": 0
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

_source line 16 · 2026-05-22T18:47:45.473Z_

<details><summary>↩ Tool result · `toolu_013LKDoGtY42xSW5M6DusoAB`</summary>

```text
artifacts/_project/intermediate/dif_power_simulation.py
artifacts/dif_power_simulation.py
artifacts/dif_diagnostic.py
artifacts/_project/intermediate/dif_phase2_simulation.py
artifacts/dif_phase2_simulation.py
artifacts/_project/intermediate/metabench_explore.py
artifacts/_project/intermediate/metabench_explore_0bd873.py
artifacts/metabench_explore.py
artifacts/build_response_matrix.py
artifacts/plan_001/plan_001_analysis.py
artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py
artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py
artifacts/plan_001b/plan_001b_analysis.py
artifacts/plan_001b/data/plan_001b_analysis.py
artifacts/plan_011/plan_011_analysis.py
artifacts/plan_011_semi_synthetic_validation/intermediate/plan_011_analysis_67f432.py
artifacts/plan_011_semi_synthetic_validation/intermediate/plan_011_analysis.py
artifacts/_project/intermediate/plan_012_irt_theta_analysis.py
artifacts/plan_012_irt_theta_conditioning/intermediate/plan_012_irt_theta_analysis.py
artifacts/plan_012/plan_012_irt_theta_analysis.py
artifacts/_project/intermediate/plan_014_within_subject_dif.py
artifacts/plan_014/plan_014_within_subject_dif.py
artifacts/_project/intermediate/plan_013_q3_analysis.py
artifacts/plan_013/plan_013_q3_analysis.py
artifacts/plan_015/plan_015_bifactor_analysis.py
artifacts/_project/intermediate/plan_016_within_subject_injection.py
artifacts/plan_016/plan_016_within_subject_injection.py
artifacts/plan_017/plan_017_downstream_impact.py
artifacts/plan_017/intermediate/plan_017_downstream_impact.py
artifacts/_project/data/plan_004_step1_gsm8k_temporal_dif.py
artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py
artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py
artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py
artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
artifacts/plan_004/plan_004_step3_gsm1k_dif_correlation.py
artifacts/plan_018/plan_018_threshold_sensitivity.py
artifacts/plan_018/intermediate/plan_018_threshold_sensitivity.py
artifacts/_project/data/plan_020_circularity_ablation.py
artifacts/plan_020/plan_020_circularity_ablation.py
artifacts/plan_019/plan_019_instability_decomposition.py
artifacts/plan_019/intermediate/plan_019_instability_decomposition.py
artifacts/plan_004/intermediate/plan_004_bootstrap_ci.py
artifacts/plan_010/plan_010_arch_stratified_dif.py
artifacts/plan_004/intermediate/plan_004_bootstrap_ci_fa8ab5.py
artifacts/plan_004/plan_004_bootstrap_ci.py
artifacts/_project/intermediate/plan_021_nonuniform_dif.py
artifacts/plan_021/plan_021_nonuniform_dif.py
artifacts/plan_023/intermediate/plan_023_item_characterization.py
artifacts/plan_023/plan_023_item_characterization.py
artifacts/plan_022/plan_022_model_independence.py
artifacts/plan_022/intermediate/plan_022_model_independence.py
artifacts/_project/intermediate/plan_024_within_family.py
artifacts/plan_024/plan_024_within_family.py
artifacts/_project/intermediate/bootstrap_dfpr.py
artifacts/plan_016_supplement/bootstrap_dfpr.py
artifacts/_project/intermediate/rank_shift_analysis.py
artifacts/plan_017_supplement/rank_shift_analysis.py
artifacts/plan_013_supplement/ld_dif_cross_analysis.py
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py
artifacts/plan_026/plan_026_constat_dif_comparison.py
artifacts/plan_027_temporal_overlap/plan_027_temporal_overlap.py
artifacts/plan_030_odds_ratio/intermediate/plan_030_odds_ratio.py
artifacts/plan_030_odds_ratio/plan_030_odds_ratio.py
artifacts/plan_029_permutation_null/plan_029_permutation_null.py
artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py
artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py
artifacts/plan_031_temporal_granularity/intermediate/plan_031_temporal_granularity.py
artifacts/plan_031_temporal_granularity/plan_031_temporal_granularity.py
artifacts/plan_028_bootstrap_ci/bootstrap_ci.py
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py
artifacts/plan_033_subject_dif_concentration/plan_033_subject_dif_concentration.py
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py
artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py
artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py
artifacts/plan_034/intermediate/plan_034_multi_subject_injection.py
artifacts/_project/intermediate/plan_035_q3_inflation_sim.py
artifacts/plan_035_q3_inflation_sim/plan_035_q3_inflation_sim.py
artifacts/sf8_power_sensitivity/sf8_power_sensitivity.py
artifacts/mf2_practical_significance/compute_mf2.py
artifacts/mf2_practical_significance/compute_one.py
artifacts/mf2_practical_significance/combine_results.py
artifacts/sf1_cluster_bootstrap/run_bootstrap.py
artifacts/mf2_rho_degradation/run_simulation.py
artifacts/_project/intermediate/lofo_robustness.py
artifacts/lofo_robustness/lofo_robustness.py
artifacts/predictive_model/phase2_train.py
artifacts/_project/data/mf1_lofo_power_calibration.py
artifacts/mf1_lofo_power_calibration/mf1_lofo_power_calibration.py
artifacts/_project/intermediate/mf2_deff_estimation.py
artifacts/mf2_deff_estimation/mf2_deff_estimation.py
artifacts/mf2_deff_estimation/mf2_deff_estimation_v3.py
artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py
artifacts/r15_subject_level_rho/subject_level_rho_analysis.py
artifacts/r15_random_split_control/random_split_analysis.py
artifacts/r17_k_sensitivity/k_sensitivity_analysis.py
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py
artifacts/r17_gsm1k_jaccard_permutation/gsm1k_jaccard_permutation.py
artifacts/r18_rank_bucket_reversal/rank_reversal_analysis.py
artifacts/r18_dedup_k_curve/dedup_k_analysis.py
artifacts/r18_icc_by_family_size/icc_family_analysis.py
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "2c9d9647-b89a-43e3-85f0-138b54d03578"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Searching for def.*mh_dif.*delta.*pval",
  "usage": {
    "total_tokens": 24871,
    "tool_uses": 4,
    "duration_ms": 6202
  },
  "last_tool_name": "Grep",
  "uuid": "6020ffb8-aae9-41c8-9e58-a3b43379e1ef",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01U6QX8KgAKEtcp8q1fPCdcK`</summary>

```json
{
  "pattern": "def.*mh_dif.*delta.*pval",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "cdac1566-cf62-4e72-a8f1-e0af0dfeb1a8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F348zQsCcqwE6cBNN9ntHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9216,
      "cache_read_input_tokens": 15614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9216,
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

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0520_2/p…",
  "usage": {
    "total_tokens": 24872,
    "tool_uses": 5,
    "duration_ms": 6416
  },
  "last_tool_name": "Glob",
  "uuid": "a6c57c6b-5ade-4138-8a37-e5f69ebf0a8b",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_018arbPE26o6qAJTLkHbFvmw`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18*/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "39c60b21-5b13-425e-bb48-007da7a4ba0d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F348zQsCcqwE6cBNN9ntHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9216,
      "cache_read_input_tokens": 15614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9216,
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

_source line 21 · 2026-05-22T18:47:49.041Z_

<details><summary>↩ Tool result · `toolu_018arbPE26o6qAJTLkHbFvmw`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "77ec60f2-2c85-40fe-88d6-d4c1594826cf"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0520_2/p…",
  "usage": {
    "total_tokens": 24873,
    "tool_uses": 6,
    "duration_ms": 6588
  },
  "last_tool_name": "Glob",
  "uuid": "cee0a204-6740-4b04-8209-b573f9fceb7e",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Glob · `toolu_019HXxAxTFCErdW3Htryej97`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/*bootstrap*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "9b9eef55-b0d2-4dcb-ab01-182e3a83270b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F348zQsCcqwE6cBNN9ntHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9216,
      "cache_read_input_tokens": 15614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9216,
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

_source line 24 · 2026-05-22T18:47:49.239Z_

<details><summary>↩ Tool result · `toolu_019HXxAxTFCErdW3Htryej97`</summary>

```text
artifacts/plan_004/intermediate/plan_004_bootstrap_ci.py
artifacts/plan_004/intermediate/plan_004_bootstrap_ci_fa8ab5.py
artifacts/plan_004/plan_004_bootstrap_ci.py
artifacts/_project/intermediate/bootstrap_dfpr.py
artifacts/plan_016_supplement/bootstrap_dfpr.py
artifacts/plan_028_bootstrap_ci/bootstrap_ci.py
artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py
artifacts/sf1_cluster_bootstrap/run_bootstrap.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "84d0d440-c879-41bc-8587-52de2b81e78d"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T18:48:08.802Z_

<details><summary>↩ Tool result · reported error · `toolu_01U6QX8KgAKEtcp8q1fPCdcK`</summary>

```text
Ripgrep search timed out after 20 seconds. The search may have matched files but did not complete in time. Try searching a more specific path or pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "d1e84d6e-e100-42ff-b66c-2059e919a746",
  "tool_use_result": "Error: Ripgrep search timed out after 20 seconds. The search may have matched files but did not complete in time. Try searching a more specific path or pattern."
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Reading artifacts/plan_028_bootstrap_ci/bootstrap_ci.py",
  "usage": {
    "total_tokens": 25414,
    "tool_uses": 7,
    "duration_ms": 28416
  },
  "last_tool_name": "Read",
  "uuid": "42ccee33-2a34-40fc-b605-53bb45a59567",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01HBp6b9W5CicobZHiryTrBs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "0a7c9449-e9c3-4d0c-a20e-248672c3fa59",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MyyCvTLoPAE7XDKctPSWch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 192,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 24830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 354,
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

_source line 28 · 2026-05-22T18:48:11.001Z_

<details><summary>↩ Tool result · `toolu_01HBp6b9W5CicobZHiryTrBs`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	bootstrap_ci.py — Bootstrap 95% CI for MH-DIF C% across all 6 benchmarks.
4	
5	Resamples *models* (not items) with replacement from each cohort,
6	re-runs MH-DIF on each bootstrap sample, records C%.
7	
8	Outputs:
9	  bootstrap_ci_results.csv       — per-benchmark C%, CI_lower, CI_upper
10	  bootstrap_distributions.csv    — per-bootstrap C% for distribution plots
11	  bootstrap_ci_report.md         — human-readable report
12	"""
13	
14	import numpy as np
15	import pandas as pd
16	from scipy.stats import chi2 as chi2_dist
17	from pathlib import Path
18	import time
19	import warnings
20	import gc
21	warnings.filterwarnings("ignore", category=RuntimeWarning)
22	
23	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
24	DATA = BASE / "metabench_data" / "benchmark-data"
25	OUT = BASE / "plan_028_bootstrap_ci"
26	OUT.mkdir(exist_ok=True)
27	
28	N_BOOTSTRAP = 1000
29	SEED = 42
30	
31	
32	# ════════════════════════════════════════════════════════════════════════════
33	#  MH-DIF CORE (from plan_028, with inf-delta fix)
34	# ════════════════════════════════════════════════════════════════════════════
35	def _nan_row(j):
36	    return dict(col_idx=j, ets_class="A")
37	
38	
39	def mh_dif_c_pct(X_ref, X_foc, n_strata=5):
40	    """
41	    Purified MH-DIF → returns only C%.
42	    Stripped version that skips storing full per-item stats for speed.
43	    """
44	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
45	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
46	    J = X_ref.shape[1]
47	    n_c = 0
48	
49	    for j in range(J):
50	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
51	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
52	
53	        s_all = np.concatenate([s_ref, s_foc])
54	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
55	        if len(edges) < 2:
56	            continue
57	        n_bins = len(edges) - 1
58	        k_ref = np.digitize(s_ref, edges[1:-1])
59	        k_foc = np.digitize(s_foc, edges[1:-1])
60	
61	        R = S = 0.0
62	        sum_diff = sum_var = 0.0
63	        n_ok = 0
64	
65	        for k in range(n_bins):
66	            mr = (k_ref == k)
67	            mf = (k_foc == k)
68	            n1 = int(mr.sum())
69	            n0 = int(mf.sum())
70	            if n1 == 0 or n0 == 0:
71	                continue
72	
73	            A = float(X_ref[mr, j].sum())
74	            B = float(n1 - A)
75	            C = float(X_foc[mf, j].sum())
76	            D = float(n0 - C)
77	            Nk = float(n1 + n0)
78	            m1 = A + C
79	            m0 = B + D
80	
81	            if m1 == 0 or m0 == 0 or Nk <= 1:
82	                continue
83	            n_ok += 1
84	
85	            Rk = A * D / Nk
86	            Sk = B * C / Nk
87	            R += Rk
88	            S += Sk
89	
90	            EA = n1 * m1 / Nk
91	            sum_diff += A - EA
92	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
93	
94	        if n_ok == 0 or (R == 0 and S == 0):
95	            continue
96	
97	        if S == 0:
98	            delta = -np.inf
99	        elif R == 0:
100	            delta = np.inf
101	        else:
102	            alpha = R / S
103	            delta = -2.35 * np.log(alpha)
104	
105	        if sum_var > 0:
106	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
107	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
108	        else:
109	            pval = np.nan
110	
111	        if not np.isfinite(delta):
112	            ets = "A"
113	        elif abs(delta) >= 1.5 and pval < 0.05:
114	            ets = "C"
115	        elif abs(delta) >= 1.0:
116	            ets = "B"
117	        else:
118	            ets = "A"
119	
120	        if ets == "C":
121	            n_c += 1
122	
123	    return n_c / J * 100
124	
125	
126	# ════════════════════════════════════════════════════════════════════════════
127	#  DATA LOADING
128	# ════════════════════════════════════════════════════════════════════════════
129	def load_response_matrix(benchmark_name):
130	    """Load CSV → (response_matrix, model_names, item_ids)."""
131	    path = DATA / f"{benchmark_name}.csv"
132	    print(f"  Loading {path.name}...")
133	
134	    file_size_mb = path.stat().st_size / 1024 / 1024
135	    print(f"  File size: {file_size_mb:.0f} MB")
136	
137	    if file_size_mb > 500:
138	        print("  Using chunked loading (large file)...")
139	        sources_set, items_set = set(), set()
140	        for chunk in pd.read_csv(path, chunksize=2_000_000, usecols=["source", "item"]):
141	            sources_set.update(chunk["source"].unique())
142	            items_set.update(chunk["item"].unique())
143	
144	        sources = sorted(sources_set)
145	        items = sorted(items_set)
146	        src2idx = {s: i for i, s in enumerate(sources)}
147	        itm2idx = {t: i for i, t in enumerate(items)}
148	        print(f"  Discovered {len(sources)} sources × {len(items)} items")
149	
150	        X = np.full((len(sources), len(items)), -1, dtype=np.int8)
151	        for chunk in pd.read_csv(path, chunksize=2_000_000):
152	            if chunk["correct"].dtype == object:
153	                vals = chunk["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).values
154	            else:
155	                vals = chunk["correct"].astype(np.int8).values
156	            si = chunk["source"].map(src2idx).values
157	            ii = chunk["item"].map(itm2idx).values
158	            X[si, ii] = vals
159	        del chunk
160	
161	        complete_mask = np.all(X >= 0, axis=1)
162	        X = X[complete_mask]
163	        model_names = np.array(sources)[complete_mask]
164	        item_ids = np.array(items)
165	    else:
166	        df = pd.read_csv(path)
167	        if df["correct"].dtype == object:
168	            df["correct"] = df["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).astype(int)
169	        else:
170	            df["correct"] = df["correct"].astype(int)
171	
172	        pivot = df.pivot(index="source", columns="item", values="correct")
173	        pivot = pivot.dropna(axis=0)
174	        model_names = pivot.index.values
175	        item_ids = pivot.columns.values
176	        X = pivot.values.astype(np.int8)
177	        del df, pivot
178	
179	    print(f"  Matrix: {X.shape[0]} models × {X.shape[1]} items")
180	    return X, model_names, item_ids
181	
182	
183	def load_mmlu_from_npz():
184	    """Load pre-built MMLU sparse matrix (matches plan_001 exactly)."""
185	    from scipy.sparse import load_npz
186	    print("  Loading MMLU from response_matrix.npz...")
187	    t0 = time.time()
188	
189	    mat = load_npz(BASE / "response_matrix.npz")
190	    X = mat.toarray().astype(np.int8)
191	    del mat
192	
193	    idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
194	    model_names = idx["model_names"]
195	    item_ids = idx["item_ids"]
196	
197	    print(f"  MMLU matrix: {X.shape[0]} models × {X.shape[1]} items ({time.time()-t0:.0f}s)")
198	    return X, model_names, item_ids
199	
200	
201	# ════════════════════════════════════════════════════════════════════════════
202	#  BOOTSTRAP
203	# ════════════════════════════════════════════════════════════════════════════
204	def run_bootstrap(X, ref_idx, foc_idx, n_bootstrap, rng, bench_name):
205	    """Bootstrap resample models, compute C% each time."""
206	    n_ref = len(ref_idx)
207	    n_foc = len(foc_idx)
208	
209	    # Original C%
210	    print(f"  Computing original C%...")
211	    t0 = time.time()
212	    original_c = mh_dif_c_pct(X[ref_idx], X[foc_idx])
213	    print(f"  Original C% = {original_c:.2f}% ({time.time()-t0:.1f}s)")
214	
215	    per_iter_est = time.time() - t0
216	    total_est = per_iter_est * n_bootstrap
217	    print(f"  Estimated total: {total_est/60:.0f} min for {n_bootstrap} bootstraps")
218	
219	    boot_cs = np.zeros(n_bootstrap)
220	    t_start = time.time()
221	
222	    for b in range(n_bootstrap):
223	        # Resample models with replacement within each group
224	        boot_ref = ref_idx[rng.randint(0, n_ref, size=n_ref)]
225	        boot_foc = foc_idx[rng.randint(0, n_foc, size=n_foc)]
226	
227	        boot_cs[b] = mh_dif_c_pct(X[boot_ref], X[boot_foc])
228	
229	        if (b + 1) % 100 == 0 or b == 0:
230	            elapsed = time.time() - t_start
231	            rate = (b + 1) / elapsed
232	            eta = (n_bootstrap - b - 1) / rate / 60
233	            print(f"    [{bench_name}] bootstrap {b+1}/{n_bootstrap}  "
234	                  f"C%={boot_cs[b]:.2f}%  mean={boot_cs[:b+1].mean():.2f}%  "
235	                  f"({elapsed:.0f}s elapsed, ETA {eta:.0f}min)")
236	
237	    ci_lower = np.percentile(boot_cs, 2.5)
238	    ci_upper = np.percentile(boot_cs, 97.5)
239	    boot_mean = boot_cs.mean()
240	    boot_std = boot_cs.std()
241	
242	    print(f"  {bench_name}: C% = {original_c:.2f}% [{ci_lower:.2f}%, {ci_upper:.2f}%]")
243	    print(f"  Bootstrap mean = {boot_mean:.2f}% (bias = {boot_mean - original_c:+.2f}pp)")
244	
245	    return dict(
246	        benchmark=bench_name,
247	        original_c_pct=original_c,
248	        ci_lower=ci_lower,
249	        ci_upper=ci_upper,
250	        boot_mean=boot_mean,
251	        boot_std=boot_std,
252	        n_bootstrap=n_bootstrap,
253	        n_ref=n_ref,
254	        n_foc=n_foc,
255	        n_items=X.shape[1],
256	    ), boot_cs
257	
258	
259	# ════════════════════════════════════════════════════════════════════════════
260	#  MAIN
261	# ════════════════════════════════════════════════════════════════════════════
262	def main():
263	    import argparse
264	    parser = argparse.ArgumentParser()
265	    parser.add_argument("--n-bootstrap", type=int, default=N_BOOTSTRAP)
266	    parser.add_argument("--benchmarks", nargs="*", default=None,
267	                        help="Subset of benchmarks to run (default: all 6)")
268	    args = parser.parse_args()
269	
270	    n_boot = args.n_bootstrap
271	    print(f"Bootstrap CI analysis — N={n_boot}, seed={SEED}")
272	    print(f"Output: {OUT}\n")
273	
274	    model_meta = pd.read_csv(BASE / "model_metadata.csv")
275	    cohort_map = dict(zip(model_meta["model_name"], model_meta["cohort_temporal"]))
276	
277	    ALL_BENCHMARKS = ["mmlu", "arc", "hellaswag", "winogrande", "truthfulqa", "gsm8k"]
278	    benchmarks = args.benchmarks if args.benchmarks else ALL_BENCHMARKS
279	
280	    # Per-benchmark seeds for reproducibility regardless of batch ordering
281	    BENCH_SEEDS = {b: SEED + i for i, b in enumerate(ALL_BENCHMARKS)}
282	
283	    all_summaries = []
284	    all_distributions = []
285	
286	    for bench in benchmarks:
287	        print(f"\n{'='*60}")
288	        print(f"  BENCHMARK: {bench.upper()}")
289	        print(f"{'='*60}")
290	
291	        # Load data
292	        if bench == "mmlu":
293	            X, model_names, item_ids = load_mmlu_from_npz()
294	        else:
295	            X, model_names, item_ids = load_response_matrix(bench)
296	
297	        name2row = {n: i for i, n in enumerate(model_names)}
298	
299	        ref_idx = np.array([name2row[n] for n in model_names
300	                            if cohort_map.get(n) == "2023"])
301	        foc_idx = np.array([name2row[n] for n in model_names
302	                            if cohort_map.get(n) == "2024"])
303	        print(f"  Cohort split: ref(2023)={len(ref_idx)}, foc(2024)={len(foc_idx)}")
304	
305	        if len(ref_idx) < 50 or len(foc_idx) < 50:
306	            print(f"  SKIP: insufficient models (<50 per cohort)")
307	            continue
308	
309	        rng = np.random.RandomState(BENCH_SEEDS[bench])
310	        summary, boot_cs = run_bootstrap(X, ref_idx, foc_idx, n_boot, rng, bench)
311	        all_summaries.append(summary)
312	
313	        boot_dist = pd.DataFrame({"bootstrap_id": range(len(boot_cs)), "c_pct": boot_cs})
314	        boot_dist["benchmark"] = bench
315	
316	        # Save per-benchmark files (safe for parallel runs)
317	        pd.DataFrame([summary]).to_csv(OUT / f"bootstrap_{bench}_summary.csv", index=False)
318	        boot_dist.to_csv(OUT / f"bootstrap_{bench}_dist.csv", index=False)
319	        print(f"  Saved: bootstrap_{bench}_summary.csv, bootstrap_{bench}_dist.csv")
320	
321	        for b, c in enumerate(boot_cs):
322	            all_distributions.append(dict(benchmark=bench, bootstrap_id=b, c_pct=c))
323	
324	        del X
325	        gc.collect()
326	
327	    # ── Merge all per-benchmark files into combined outputs ──
328	    _merge_results()
329	
330	    # ── Final summary ──
331	    results_df = pd.DataFrame(all_summaries)
332	    print(f"\n{'='*60}")
333	    print("BOOTSTRAP CI SUMMARY")
334	    print(f"{'='*60}")
335	    for _, r in results_df.iterrows():
336	        print(f"  {r.benchmark.upper():12s}  C% = {r.original_c_pct:5.1f}%  "
337	              f"[{r.ci_lower:5.1f}%, {r.ci_upper:5.1f}%]  "
338	              f"(boot mean={r.boot_mean:.1f}%, std={r.boot_std:.1f}%)")
339	
340	
341	def _merge_results():
342	    """Merge all per-benchmark files into combined outputs."""
343	    import glob as globmod
344	    summary_files = sorted(globmod.glob(str(OUT / "bootstrap_*_summary.csv")))
345	    dist_files = sorted(globmod.glob(str(OUT / "bootstrap_*_dist.csv")))
346	
347	    if summary_files:
348	        results_df = pd.concat([pd.read_csv(f) for f in summary_files], ignore_index=True)
349	        results_df.to_csv(OUT / "bootstrap_ci_results.csv", index=False)
350	        print(f"\nMerged {len(summary_files)} benchmarks → bootstrap_ci_results.csv")
351	
352	        _write_report(results_df)
353	        print("Saved: bootstrap_ci_report.md")
354	
355	    if dist_files:
356	        dist_df = pd.concat([pd.read_csv(f) for f in dist_files], ignore_index=True)
357	        dist_df.to_csv(OUT / "bootstrap_distributions.csv", index=False)
358	        print(f"Merged {len(dist_files)} benchmarks → bootstrap_distributions.csv")
359	
360	
361	def _write_report(results_df):
362	    L = []
363	    def w(s=""):
364	        L.append(s)
365	
366	    w("# Bootstrap 95% CI for MH-DIF C%")
367	    w()
368	    w("## Method")
369	    w()
370	    w(f"- Bootstrap resampling of **models** (not items), {int(results_df.iloc[0].n_bootstrap)} iterations")
371	    w("- Within each bootstrap: resample N_ref models with replacement from 2023 cohort,")
372	    w("  resample N_foc models with replacement from 2024 cohort")
373	    w("- Re-run purified MH-DIF (5 strata) on resampled groups")
374	    w("- 95% CI = [2.5th, 97.5th] percentile of bootstrap C% distribution")
375	    w(f"- Random seed = {SEED}")
376	    w()
377	
378	    w("## Results")
379	    w()
380	    w("| Benchmark | Items | N_ref | N_foc | C% | 95% CI | Boot Mean | Boot SD |")
381	    w("|-----------|-------|-------|-------|----|--------|-----------|---------|")
382	    for _, r in results_df.iterrows():
383	        w(f"| {r.benchmark.upper()} | {int(r.n_items)} | {int(r.n_ref)} | {int(r.n_foc)} | "
384	          f"{r.original_c_pct:.1f}% | [{r.ci_lower:.1f}%, {r.ci_upper:.1f}%] | "
385	          f"{r.boot_mean:.1f}% | {r.boot_std:.1f}% |")
386	    w()
387	
388	    w("## Validation")
389	    w()
390	    for _, r in results_df.iterrows():
391	        bias = r.boot_mean - r.original_c_pct
392	        ci_width = r.ci_upper - r.ci_lower
393	        w(f"- **{r.benchmark.upper()}**: bias = {bias:+.2f}pp, CI width = {ci_width:.1f}pp")
394	    w()
395	
396	    (OUT / "bootstrap_ci_report.md").write_text("\n".join(L) + "\n")
397	
398	
399	if __name__ == "__main__":
400	    main()
401	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "b454f29d-ce14-493c-bfe2-95d7aaeb96b6"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Reading artifacts/plan_004/plan_004_bootstrap_ci.py",
  "usage": {
    "total_tokens": 25415,
    "tool_uses": 8,
    "duration_ms": 28762
  },
  "last_tool_name": "Read",
  "uuid": "657f354d-51b5-4a2d-8a85-a7e667ce0122",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01UJ9uC15r1use6ViB8BaU9q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "b57b5a77-6110-422c-ba66-ed94c6d02df5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MyyCvTLoPAE7XDKctPSWch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 192,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 24830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 354,
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

_source line 31 · 2026-05-22T18:48:11.344Z_

<details><summary>↩ Tool result · `toolu_01UJ9uC15r1use6ViB8BaU9q`</summary>

```text
1	"""BCa bootstrap confidence intervals for GSM1K contamination gap correlations."""
2	
3	import numpy as np
4	import pandas as pd
5	from scipy import stats
6	from pathlib import Path
7	
8	BASE = Path(__file__).parent
9	DATA_PATH = BASE / "gsm1k_dif_correlation.csv"
10	DOMAIN_PATH = BASE.parent / "plan_001" / "domain_specificity.csv"
11	OUTPUT_PATH = BASE / "bootstrap_ci_report.md"
12	N_BOOT = 10_000
13	ALPHA = 0.05
14	SEED = 42
15	
16	
17	def bca_bootstrap_ci(arrays, stat_func, n_boot=N_BOOT, alpha=ALPHA, seed=SEED):
18	    """BCa bootstrap CI for a statistic computed from multiple aligned arrays."""
19	    rng = np.random.RandomState(seed)
20	    n = len(arrays[0])
21	
22	    theta_hat = stat_func(*arrays)
23	
24	    theta_boot = np.empty(n_boot)
25	    for i in range(n_boot):
26	        idx = rng.choice(n, size=n, replace=True)
27	        theta_boot[i] = stat_func(*(a[idx] for a in arrays))
28	
29	    z0 = stats.norm.ppf(np.mean(theta_boot < theta_hat))
30	
31	    theta_jack = np.empty(n)
32	    for i in range(n):
33	        idx = np.concatenate([np.arange(i), np.arange(i + 1, n)])
34	        theta_jack[i] = stat_func(*(a[idx] for a in arrays))
35	
36	    theta_dot = np.mean(theta_jack)
37	    diff = theta_dot - theta_jack
38	    a_hat = np.sum(diff ** 3) / (6.0 * np.sum(diff ** 2) ** 1.5 + 1e-15)
39	
40	    z_lo = stats.norm.ppf(alpha / 2)
41	    z_hi = stats.norm.ppf(1 - alpha / 2)
42	
43	    def adj(z_a):
44	        num = z0 + z_a
45	        return stats.norm.cdf(z0 + num / (1 - a_hat * num))
46	
47	    p_lo = np.clip(adj(z_lo), 0.5 / n_boot, 1 - 0.5 / n_boot)
48	    p_hi = np.clip(adj(z_hi), 0.5 / n_boot, 1 - 0.5 / n_boot)
49	
50	    ci_lo = np.percentile(theta_boot, 100 * p_lo)
51	    ci_hi = np.percentile(theta_boot, 100 * p_hi)
52	    boot_se = np.std(theta_boot, ddof=1)
53	
54	    return theta_hat, ci_lo, ci_hi, boot_se
55	
56	
57	def pearson_r(x, y):
58	    return stats.pearsonr(x, y)[0]
59	
60	
61	def spearman_rho(x, y):
62	    return stats.spearmanr(x, y)[0]
63	
64	
65	def partial_pearson_r(x, y, z):
66	    def _resid(a, b):
67	        slope, intercept = np.polyfit(b, a, 1)
68	        return a - (slope * b + intercept)
69	    return stats.pearsonr(_resid(x, z), _resid(y, z))[0]
70	
71	
72	def main():
73	    df = pd.read_csv(DATA_PATH).dropna(subset=["gap", "dif_advantage"])
74	    print(f"GSM1K data: {len(df)} models")
75	
76	    gap = df["gap"].values
77	    dif_adv = df["dif_advantage"].values
78	    gsm8k_acc = df["gsm8k_acc"].values
79	
80	    results = []
81	
82	    # 1) Pearson r
83	    est, lo, hi, se = bca_bootstrap_ci((gap, dif_adv), pearson_r)
84	    p = stats.pearsonr(gap, dif_adv)[1]
85	    results.append(("Pearson *r* (gap vs DIF advantage)", len(df), est, lo, hi, se, p))
86	    print(f"Pearson r = {est:.3f} [{lo:.3f}, {hi:.3f}], SE={se:.3f}, p={p:.4f}")
87	
88	    # 2) Spearman ρ
89	    est, lo, hi, se = bca_bootstrap_ci((gap, dif_adv), spearman_rho)
90	    p = stats.spearmanr(gap, dif_adv)[1]
91	    results.append(("Spearman *ρ* (gap vs DIF advantage)", len(df), est, lo, hi, se, p))
92	    print(f"Spearman ρ = {est:.3f} [{lo:.3f}, {hi:.3f}], SE={se:.3f}, p={p:.4f}")
93	
94	    # 3) Partial r | GSM8K accuracy
95	    est, lo, hi, se = bca_bootstrap_ci((gap, dif_adv, gsm8k_acc), partial_pearson_r)
96	    n = len(df)
97	    t = est * np.sqrt((n - 3) / (1 - est ** 2))
98	    p = 2 * stats.t.sf(abs(t), df=n - 3)
99	    results.append(("Partial *r* (gap vs DIF adv | GSM8K acc)", len(df), est, lo, hi, se, p))
100	    print(f"Partial r = {est:.3f} [{lo:.3f}, {hi:.3f}], SE={se:.3f}, p={p:.4f}")
101	
102	    # 4) Domain Spearman ρ (plan_001, 57 MMLU subjects)
103	    domain_done = False
104	    if DOMAIN_PATH.exists():
105	        dd = pd.read_csv(DOMAIN_PATH).dropna(subset=["pct_c"])
106	        pct_c = dd["pct_c"].values
107	        # Find which column gives ρ ≈ 0.307
108	        for col in ["acc_change", "acc_2024", "acc_2023"]:
109	            rho_check = stats.spearmanr(pct_c, dd[col].values)[0]
110	            print(f"  ρ(pct_c, {col}) = {rho_check:.3f}")
111	            if abs(rho_check - 0.307) < 0.05:
112	                y = dd[col].values
113	                est, lo, hi, se = bca_bootstrap_ci((pct_c, y), spearman_rho)
114	                p = stats.spearmanr(pct_c, y)[1]
115	                results.append((
116	                    f"Domain Spearman *ρ* (C% vs {col})", len(dd), est, lo, hi, se, p
117	                ))
118	                print(f"Domain ρ = {est:.3f} [{lo:.3f}, {hi:.3f}], SE={se:.3f}, p={p:.4f}")
119	                domain_done = True
120	                break
121	        if not domain_done:
122	            print("  No pairing close to ρ=0.307; skipping domain bootstrap.")
123	
124	    # --- Report ---
125	    lines = [
126	        "# Bootstrap Confidence Intervals Report",
127	        "",
128	        "## Method",
129	        "",
130	        "Bias-corrected and accelerated (BCa) bootstrap, 10,000 resamples, seed = 42.",
131	        "BCa adjusts for bias and skewness in the bootstrap distribution via",
132	        "bias-correction factor *z*₀ and jackknife acceleration factor *â*.",
133	        "For partial correlation, each resample re-computes OLS residuals and",
134	        "correlates them, preserving the conditioning structure.",
135	        "",
136	        "## Results",
137	        "",
138	        "| Statistic | *n* | Estimate | 95% CI | Boot. SE | *p* |",
139	        "|-----------|-----|----------|--------|----------|-----|",
140	    ]
141	    for name, n_obs, est, lo, hi, se, p in results:
142	        lines.append(
143	            f"| {name} | {n_obs} | {est:.3f} | [{lo:.3f}, {hi:.3f}] | {se:.3f} | {p:.4f} |"
144	        )
145	
146	    lines += [
147	        "",
148	        "## Verification",
149	        "",
150	        f"- Pearson *r* point estimate ({results[0][2]:.3f}) matches reported −0.478.",
151	        f"- Spearman *ρ* point estimate ({results[1][2]:.3f}) matches reported −0.403.",
152	        f"- Partial *r* point estimate ({results[2][2]:.3f}) matches reported −0.385.",
153	    ]
154	
155	    any_cross = any(lo <= 0 <= hi for _, _, _, lo, hi, _, _ in results)
156	    if any_cross:
157	        lines.append("- **Note**: At least one CI includes zero.")
158	    else:
159	        lines.append("- All CIs exclude zero, consistent with reported *p*-values.")
160	
161	    lines += [
162	        "",
163	        "## Interpretation",
164	        "",
165	        "The negative correlations between GSM8K→GSM1K gap and DIF advantage",
166	        "are robust: models with larger contamination-driven accuracy drops",
167	        "show systematically lower performance advantage on DIF-flagged items.",
168	        "This relationship holds after controlling for overall model ability",
169	        "(partial *r*), ruling out a simple ability confound.",
170	    ]
171	
172	    if domain_done:
173	        dr = [r for r in results if "Domain" in r[0]][0]
174	        lines += [
175	            "",
176	            f"The domain-level Spearman *ρ* = {dr[2]:.3f} [{dr[3]:.3f}, {dr[4]:.3f}]",
177	            f"indicates that MMLU subjects with higher contamination rates (C%)",
178	            f"tend to show {'larger' if dr[2] > 0 else 'smaller'} accuracy changes",
179	            f"across model generations, {'though the CI includes zero' if dr[3] <= 0 else 'with the CI excluding zero'}.",
180	        ]
181	
182	    lines.append("")
183	    OUTPUT_PATH.write_text("\n".join(lines))
184	    print(f"\nReport → {OUTPUT_PATH}")
185	
186	
187	if __name__ == "__main__":
188	    main()
189	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "d87c2df7-9e1a-4e67-8292-b5ef479f1bdd"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 34662,
    "tool_uses": 9,
    "duration_ms": 32259
  },
  "last_tool_name": "Bash",
  "uuid": "8498b073-5fd5-4a40-b5db-50201b7fd886",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_015ivvKKcbMnytywHMrWeZ3b`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*r18*\" -o -name \"*R18*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "ecef8044-b019-48f1-80ef-e07b69bb8127",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MhWgcquxnFfD1PL9CAtKCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9430,
      "cache_read_input_tokens": 25184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9430,
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

_source line 34 · 2026-05-22T18:48:14.952Z_

<details><summary>↩ Tool result · `toolu_015ivvKKcbMnytywHMrWeZ3b`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_restricted_range_rho
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_icc_by_family_size
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_dedup_k_curve
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "a18b6f3c-b10b-4ad3-bcef-df853c34ef18"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Searching for return.*delta.*pval|return.*\\(delta|def.*dif.*full",
  "usage": {
    "total_tokens": 34663,
    "tool_uses": 10,
    "duration_ms": 32952
  },
  "last_tool_name": "Grep",
  "uuid": "79d348c7-9ef5-484a-9e51-39bf48e72b4a",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_01QU7EeavqdD5jhRhXybSpbP`</summary>

```json
{
  "pattern": "return.*delta.*pval|return.*\\(delta|def.*dif.*full",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "a1e6958b-ce7c-46ae-9082-73d7f429c2fc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MhWgcquxnFfD1PL9CAtKCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9430,
      "cache_read_input_tokens": 25184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9430,
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

_source line 37 · 2026-05-22T18:48:15.557Z_

<details><summary>↩ Tool result · `toolu_01QU7EeavqdD5jhRhXybSpbP`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "479ae929-1d9e-408e-a419-4b53829a9012"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0520_2/p…",
  "usage": {
    "total_tokens": 35287,
    "tool_uses": 11,
    "duration_ms": 34912
  },
  "last_tool_name": "Glob",
  "uuid": "392e6072-bd2a-4943-9070-6fb8538579fd",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Glob · `toolu_01CTGhQMWofPKGWE7VpAWXkZ`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "6e6a2a66-5701-43e6-a5e8-bf0486d8957a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P5R6NWMUntUnaEVprxs7Uo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 34614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 622,
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

_source line 40 · 2026-05-22T18:48:17.503Z_

<details><summary>↩ Tool result · `toolu_01CTGhQMWofPKGWE7VpAWXkZ`</summary>

```text
artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "5de607f7-7b79-4fb9-9ba4-2a6f9406c0c3"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Reading artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "usage": {
    "total_tokens": 35448,
    "tool_uses": 12,
    "duration_ms": 36834
  },
  "last_tool_name": "Read",
  "uuid": "4a9f1ca0-dc00-436f-ba45-20cf82cf0c78",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_011QRniHisMAXtNGUuWiJcsf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "ca48ba2f-7eaf-4bf3-a345-5035d346b461",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Na8n8Y7BzLrSe7PHVtdv5V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 35236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 160,
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

_source line 43 · 2026-05-22T18:48:19.418Z_

<details><summary>↩ Tool result · `toolu_011QRniHisMAXtNGUuWiJcsf`</summary>

```text
1	#!/usr/bin/env python3
2	"""R18: Base vs Instruct MH-DIF separation experiment."""
3	
4	import re
5	import sys
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse
9	from scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency
10	
11	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
12	OUT = f"{ROOT}/r18_base_vs_instruct_dif"
13	
14	N_STRATA = 5
15	N_BOOT = 1000
16	ALPHA = 0.05
17	DELTA_THRESH = 1.5
18	
19	# ── Part 1: Model classification ─────────────────────────────────────────
20	
21	INSTRUCT_SUFFIXES = re.compile(
22	    r"[-_\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)"
23	    r"([-_\.]|$)",
24	    re.IGNORECASE,
25	)
26	
27	QUANT_SUFFIXES = re.compile(
28	    r"[-_\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])",
29	    re.IGNORECASE,
30	)
31	
32	FAMILY_PREFIX_EXCLUDE = re.compile(
33	    r"^(openchat|chatglm|chatml)",
34	    re.IGNORECASE,
35	)
36	
37	
38	def classify_model(name: str) -> str:
39	    short = name.split("/")[-1] if "/" in name else name
40	    stripped = QUANT_SUFFIXES.sub("", short)
41	
42	    if stripped.lower().endswith("-it"):
43	        return "instruct"
44	
45	    if INSTRUCT_SUFFIXES.search(stripped):
46	        prefix_part = stripped.split("-")[0].split("_")[0]
47	        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):
48	            rest = stripped[len(prefix_part):]
49	            if not INSTRUCT_SUFFIXES.search(rest):
50	                return "base"
51	        return "instruct"
52	
53	    return "base"
54	
55	
56	# ── Part 2: MH-DIF (extended) ────────────────────────────────────────────
57	
58	def mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):
59	    """Vectorized MH-DIF returning per-item details.
60	
61	    Returns (c_pct, delta_mh, pval, is_c).
62	    """
63	    n_ref, J = X_ref.shape
64	    n_foc = X_foc.shape[0]
65	
66	    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()
67	    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()
68	    s_all = np.concatenate([tot_ref, tot_foc])
69	
70	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
71	    n_bins = len(edges) - 1
72	    if n_bins < 1:
73	        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)
74	
75	    k_ref = np.digitize(tot_ref, edges[1:-1])
76	    k_foc = np.digitize(tot_foc, edges[1:-1])
77	
78	    n1 = np.zeros(n_bins, dtype=np.float64)
79	    n0 = np.zeros(n_bins, dtype=np.float64)
80	    A = np.zeros((n_bins, J), dtype=np.float64)
81	    C = np.zeros((n_bins, J), dtype=np.float64)
82	
83	    for k in range(n_bins):
84	        mr = k_ref == k
85	        mf = k_foc == k
86	        n1[k] = mr.sum()
87	        n0[k] = mf.sum()
88	        if mr.any():
89	            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()
90	        if mf.any():
91	            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()
92	
93	    B = n1[:, None] - A
94	    D = n0[:, None] - C
95	    Nk = (n1 + n0)[:, None]
96	    m1 = A + C
97	    m0 = B + D
98	
99	    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)
100	
101	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
102	    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)
103	
104	    finite_mask = (Rj > 0) & (Sj > 0)
105	    with np.errstate(divide="ignore", invalid="ignore"):
106	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
107	
108	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
109	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
110	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
111	    sum_var = np.where(
112	        valid,
113	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),
114	        0,
115	    ).sum(axis=0)
116	
117	    chi2_j = np.where(
118	        sum_var > 0,
119	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
120	        0,
121	    )
122	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
123	
124	    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)
125	    c_pct = is_c.sum() / J * 100
126	
127	    return c_pct, delta_j, pval_j, is_c
128	
129	
130	def ets_class(delta):
131	    a = abs(delta)
132	    if a < 1.0:
133	        return "A"
134	    elif a < 1.5:
135	        return "B"
136	    else:
137	        return "C"
138	
139	
140	# ── Main ──────────────────────────────────────────────────────────────────
141	
142	def main():
143	    print("Loading data...")
144	    meta = pd.read_csv(f"{ROOT}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv")
145	    rm = np.load(f"{ROOT}/response_matrix.npz")
146	    X = sparse.csr_matrix((rm["data"], rm["indices"], rm["indptr"]), shape=tuple(rm["shape"]))
147	    idx = np.load(f"{ROOT}/response_matrix_index.npz", allow_pickle=True)
148	    model_names = idx["model_names"]
149	    item_ids = idx["item_ids"]
150	
151	    # Build model name → row index lookup
152	    name2row = {n: i for i, n in enumerate(model_names)}
153	
154	    # Classify models
155	    meta = meta[meta["cohort_temporal"].isin(["2023", "2024"])].copy()
156	    meta["model_type"] = meta["model_name"].apply(classify_model)
157	
158	    # Save classification
159	    class_df = meta[["model_name", "model_type", "cohort_temporal", "family"]].copy()
160	    class_df.to_csv(f"{OUT}/model_classification.csv", index=False)
161	
162	    # Map to response matrix rows
163	    meta["rm_idx"] = meta["model_name"].map(name2row)
164	    meta = meta.dropna(subset=["rm_idx"])
165	    meta["rm_idx"] = meta["rm_idx"].astype(int)
166	
167	    # Group counts
168	    groups = {}
169	    for mtype in ["base", "instruct"]:
170	        ref_mask = (meta["model_type"] == mtype) & (meta["cohort_temporal"] == "2023")
171	        foc_mask = (meta["model_type"] == mtype) & (meta["cohort_temporal"] == "2024")
172	        groups[mtype] = {
173	            "ref_idx": meta.loc[ref_mask, "rm_idx"].values,
174	            "foc_idx": meta.loc[foc_mask, "rm_idx"].values,
175	        }
176	
177	    print("\n=== Part 4: Sample sizes ===")
178	    for mtype in ["base", "instruct"]:
179	        n_ref = len(groups[mtype]["ref_idx"])
180	        n_foc = len(groups[mtype]["foc_idx"])
181	        flag = " ⚠ UNDERPOWERED" if min(n_ref, n_foc) < 80 else ""
182	        print(f"  {mtype:>10s}: ref(2023)={n_ref}, foc(2024)={n_foc}{flag}")
183	    print(f"  {'full':>10s}: ref(2023)=1080, foc(2024)=807  (reported baseline)")
184	
185	    # Run MH-DIF per group
186	    results = {}
187	    for mtype in ["base", "instruct"]:
188	        ri, fi = groups[mtype]["ref_idx"], groups[mtype]["foc_idx"]
189	        print(f"\nRunning MH-DIF for {mtype} ({len(ri)} ref, {len(fi)} foc)...")
190	        X_ref = X[ri]
191	        X_foc = X[fi]
192	        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)
193	        results[mtype] = {"c_pct": c_pct, "delta": delta, "pval": pval, "is_c": is_c}
194	        print(f"  C% = {c_pct:.1f}%  ({is_c.sum()}/{len(is_c)} items)")
195	
196	    # ── Part 3a: Bootstrap CI for C% difference ──────────────────────────
197	    print("\n=== Part 3a: Bootstrap C% difference ===")
198	    rng = np.random.default_rng(42)
199	    boot_diff = np.zeros(N_BOOT)
200	
201	    for b in range(N_BOOT):
202	        if (b + 1) % 200 == 0:
203	            print(f"  bootstrap {b+1}/{N_BOOT}...")
204	        cpcts = {}
205	        for mtype in ["base", "instruct"]:
206	            ri, fi = groups[mtype]["ref_idx"], groups[mtype]["foc_idx"]
207	            ri_b = rng.choice(ri, size=len(ri), replace=True)
208	            fi_b = rng.choice(fi, size=len(fi), replace=True)
209	            c, _, _, _ = mh_dif_full(X[ri_b], X[fi_b])
210	            cpcts[mtype] = c
211	        boot_diff[b] = cpcts["base"] - cpcts["instruct"]
212	
213	    ci_lo, ci_hi = np.percentile(boot_diff, [2.5, 97.5])
214	    mean_diff = boot_diff.mean()
215	    print(f"  C%_base - C%_instruct = {results['base']['c_pct']:.1f} - {results['instruct']['c_pct']:.1f} = {results['base']['c_pct'] - results['instruct']['c_pct']:.1f}")
216	    print(f"  Bootstrap 95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]")
217	
218	    # ── Part 3b: Difficulty-direction gradient ────────────────────────────
219	    print("\n=== Part 3b: Difficulty-direction gradient ===")
220	    all_2023_idx = meta.loc[meta["cohort_temporal"] == "2023", "rm_idx"].values
221	    X_2023 = X[all_2023_idx]
222	    item_diff = np.asarray(X_2023.mean(axis=0), dtype=np.float64).ravel()
223	
224	    for mtype in ["base", "instruct"]:
225	        c_mask = results[mtype]["is_c"]
226	        if c_mask.sum() < 3:
227	            print(f"  {mtype}: too few C items ({c_mask.sum()}) for correlation")
228	            continue
229	        rho, p = spearmanr(item_diff[c_mask], results[mtype]["delta"][c_mask])
230	        print(f"  {mtype}: ρ(difficulty, Δ_MH) = {rho:.3f}  (p={p:.2e}, n={c_mask.sum()})")
231	
232	    # ── Part 3c: DIF item overlap ─────────────────────────────────────────
233	    print("\n=== Part 3c: DIF item overlap ===")
234	    c_base = set(np.where(results["base"]["is_c"])[0])
235	    c_inst = set(np.where(results["instruct"]["is_c"])[0])
236	    inter = c_base & c_inst
237	    union = c_base | c_inst
238	    jaccard = len(inter) / len(union) if union else 0
239	
240	    p_b = len(c_base) / len(item_ids)
241	    p_i = len(c_inst) / len(item_ids)
242	    expected_jaccard = (p_b * p_i) / (p_b + p_i - p_b * p_i) if (p_b + p_i - p_b * p_i) > 0 else 0
243	
244	    only_base = len(c_base - c_inst)
245	    only_inst = len(c_inst - c_base)
246	    both = len(inter)
247	    print(f"  |C_base|={len(c_base)}, |C_instruct|={len(c_inst)}")
248	    print(f"  Only base: {only_base}, Only instruct: {only_inst}, Both: {both}")
249	    print(f"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})")
250	
251	    # ── Part 3d: Direction distribution ───────────────────────────────────
252	    print("\n=== Part 3d: DIF direction distribution ===")
253	    dir_table = {}
254	    for mtype in ["base", "instruct"]:
255	        d = results[mtype]["delta"][results[mtype]["is_c"]]
256	        n_foc_fav = (d > 0).sum()
257	        n_ref_fav = (d < 0).sum()
258	        dir_table[mtype] = (int(n_foc_fav), int(n_ref_fav))
259	        total = n_foc_fav + n_ref_fav
260	        print(f"  {mtype}: focal-favoring={n_foc_fav} ({n_foc_fav/total*100:.1f}%), ref-favoring={n_ref_fav} ({n_ref_fav/total*100:.1f}%)")
261	
262	    ct = np.array([[dir_table["base"][0], dir_table["base"][1]],
263	                    [dir_table["instruct"][0], dir_table["instruct"][1]]])
264	    if ct.min() > 0:
265	        chi2_val, p_dir, _, _ = chi2_contingency(ct)
266	        print(f"  χ²={chi2_val:.2f}, p={p_dir:.3e}")
267	    else:
268	        p_dir = np.nan
269	        print("  χ² test not possible (zero cell)")
270	
271	    # ── Save per-item CSV ─────────────────────────────────────────────────
272	    print("\nSaving per-item results...")
273	
274	    # Extract subject from item_id (format: subject_qXXXX or similar)
275	    def get_subject(iid):
276	        parts = iid.rsplit("_", 1)
277	        return parts[0] if len(parts) > 1 else iid
278	
279	    item_df = pd.DataFrame({
280	        "item_id": item_ids,
281	        "subject": [get_subject(str(i)) for i in item_ids],
282	        "difficulty": item_diff,
283	        "delta_mh_base": results["base"]["delta"],
284	        "p_base": results["base"]["pval"],
285	        "ets_base": [ets_class(d) for d in results["base"]["delta"]],
286	        "is_c_base": results["base"]["is_c"],
287	        "delta_mh_instruct": results["instruct"]["delta"],
288	        "p_instruct": results["instruct"]["pval"],
289	        "ets_instruct": [ets_class(d) for d in results["instruct"]["delta"]],
290	        "is_c_instruct": results["instruct"]["is_c"],
291	    })
292	    item_df.to_csv(f"{OUT}/base_instruct_item_results.csv", index=False)
293	
294	    # ── Generate report ───────────────────────────────────────────────────
295	    print("Writing report...")
296	
297	    n_base_ref = len(groups["base"]["ref_idx"])
298	    n_base_foc = len(groups["base"]["foc_idx"])
299	    n_inst_ref = len(groups["instruct"]["ref_idx"])
300	    n_inst_foc = len(groups["instruct"]["foc_idx"])
301	
302	    report = f"""# R18: Base vs Instruct DIF Separation Experiment
303	
304	## Sample Sizes
305	
306	| Group | Ref (2023) | Foc (2024) | Total |
307	|-------|-----------|-----------|-------|
308	| Base | {n_base_ref} | {n_base_foc} | {n_base_ref + n_base_foc} |
309	| Instruct | {n_inst_ref} | {n_inst_foc} | {n_inst_ref + n_inst_foc} |
310	| Full (reported) | 1,080 | 807 | 1,887 |
311	
312	{"**⚠ Warning:** Some subgroups have N < 80; interpret with caution." if min(n_base_ref, n_base_foc, n_inst_ref, n_inst_foc) < 80 else "All subgroups have N ≥ 80; adequate power."}
313	
314	## C% Comparison
315	
316	| Group | C% | DIF-C items |
317	|-------|-----|------------|
318	| Base | {results['base']['c_pct']:.1f}% | {results['base']['is_c'].sum()}/{len(item_ids)} |
319	| Instruct | {results['instruct']['c_pct']:.1f}% | {results['instruct']['is_c'].sum()}/{len(item_ids)} |
320	| Full (reported) | 31.3% | — |
321	
322	**Difference (base − instruct):** {results['base']['c_pct'] - results['instruct']['c_pct']:.1f} pp
323	**Bootstrap 95% CI:** [{ci_lo:.1f}, {ci_hi:.1f}] (N={N_BOOT})
324	
325	## Difficulty–Direction Gradient
326	
327	Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:
328	
329	"""
330	
331	    for mtype in ["base", "instruct"]:
332	        c_mask = results[mtype]["is_c"]
333	        if c_mask.sum() >= 3:
334	            rho, p = spearmanr(item_diff[c_mask], results[mtype]["delta"][c_mask])
335	            report += f"- **{mtype.capitalize()}:** ρ = {rho:.3f} (p = {p:.2e}, n = {c_mask.sum()})\n"
336	        else:
337	            report += f"- **{mtype.capitalize()}:** too few C items ({c_mask.sum()}) for correlation\n"
338	
339	    report += f"""
340	## DIF Item Overlap
341	
342	| Metric | Value |
343	|--------|-------|
344	| C_base only | {only_base} |
345	| C_instruct only | {only_inst} |
346	| Both | {both} |
347	| Jaccard index | {jaccard:.3f} |
348	| Expected Jaccard (independence) | {expected_jaccard:.3f} |
349	| Jaccard / Expected ratio | {jaccard / expected_jaccard:.1f}× |
350	
351	## DIF Direction Distribution
352	
353	| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
354	|-------|----------------------|---------------------|
355	| Base | {dir_table['base'][0]} ({dir_table['base'][0]/(sum(dir_table['base']))*100:.1f}%) | {dir_table['base'][1]} ({dir_table['base'][1]/(sum(dir_table['base']))*100:.1f}%) |
356	| Instruct | {dir_table['instruct'][0]} ({dir_table['instruct'][0]/(sum(dir_table['instruct']))*100:.1f}%) | {dir_table['instruct'][1]} ({dir_table['instruct'][1]/(sum(dir_table['instruct']))*100:.1f}%) |
357	
358	χ² = {chi2_val:.2f}, p = {p_dir:.3e}
359	
360	## Output Files
361	
362	- `model_classification.csv` — {len(class_df)} models classified
363	- `base_instruct_item_results.csv` — {len(item_ids)} items with per-group DIF statistics
364	"""
365	
366	    with open(f"{OUT}/base_instruct_dif_report.md", "w") as f:
367	        f.write(report)
368	
369	    print(f"\nDone. Results in {OUT}/")
370	
371	
372	if __name__ == "__main__":
373	    main()
374	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "7d9e89bd-0407-4980-8d8c-0377b575cd37"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "description": "Running head -1 /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 42037,
    "tool_uses": 13,
    "duration_ms": 39824
  },
  "last_tool_name": "Bash",
  "uuid": "4e0d036b-e8dc-4d1e-98b8-8c98e5f09f75",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01WxddkwEKXAw63XWwcaA1HU`</summary>

```json
{
  "command": "head -1 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv | tr ',' '\\n' | nl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "e07bbf2e-bcea-4620-8531-8421a8fbd5c1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PwHcwXrLJUxkADAGh5GmVb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6587,
      "cache_read_input_tokens": 35396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6587,
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

_source line 46 · 2026-05-22T18:48:22.474Z_

<details><summary>↩ Tool result · `toolu_01WxddkwEKXAw63XWwcaA1HU`</summary>

```text
     1	model_name
     2	family
     3	release_year
     4	release_half
     5	training_method
     6	accuracy
     7	cohort_temporal
     8	cohort_accuracy_quintile
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "e2ba2526-95a4-42f1-b108-58281c965954"
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a48e368fd2be8645c",
  "tool_use_id": "toolu_01CtxEwUPze7ZAq2u166GLKh",
  "status": "completed",
  "output_file": "",
  "summary": "Find MH-DIF function source",
  "usage": {
    "total_tokens": 42228,
    "tool_uses": 13,
    "duration_ms": 57783
  },
  "uuid": "5d6c05f8-969a-43ae-88f0-daa7231b5207",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool result

_source line 48 · 2026-05-22T18:48:40.361Z_

<details><summary>↩ Tool result · `toolu_01CtxEwUPze7ZAq2u166GLKh`</summary>

````text
Perfect! Now I have all the information needed. Let me compile the complete findings.

## Summary

I've found the complete MH-DIF implementation in your codebase. Here are the two key versions:

### 1. **Vectorized Total-Score Version (C% only)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`

**Function `mh_dif_c_pct_vec()` (lines 34-101):**
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

**Returns:** Scalar C% (percentage of DIF-flagged items)

---

### 2. **Full Per-Item Version (delta_mh, p_value, is_c)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py`

**Function `mh_dif_full()` (lines 58-127):**
```python
def mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):
    """Vectorized MH-DIF returning per-item details.

    Returns (c_pct, delta_mh, pval, is_c).
    """
    n_ref, J = X_ref.shape
    n_foc = X_foc.shape[0]

    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()
    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()
    s_all = np.concatenate([tot_ref, tot_foc])

    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
    n_bins = len(edges) - 1
    if n_bins < 1:
        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)

    k_ref = np.digitize(tot_ref, edges[1:-1])
    k_foc = np.digitize(tot_foc, edges[1:-1])

    n1 = np.zeros(n_bins, dtype=np.float64)
    n0 = np.zeros(n_bins, dtype=np.float64)
    A = np.zeros((n_bins, J), dtype=np.float64)
    C = np.zeros((n_bins, J), dtype=np.float64)

    for k in range(n_bins):
        mr = k_ref == k
        mf = k_foc == k
        n1[k] = mr.sum()
        n0[k] = mf.sum()
        if mr.any():
            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()
        if mf.any():
            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()

    B = n1[:, None] - A
    D = n0[:, None] - C
    Nk = (n1 + n0)[:, None]
    m1 = A + C
    m0 = B + D

    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)

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
        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),
        0,
    ).sum(axis=0)

    chi2_j = np.where(
        sum_var > 0,
        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
        0,
    )
    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)

    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)
    c_pct = is_c.sum() / J * 100

    return c_pct, delta_j, pval_j, is_c
```

**Returns:** Tuple of (c_pct, delta_mh_array, pval_array, is_c_bool_array)

---

### Key Differences:

1. **v1 (mmlu_bootstrap_ci.py):** Returns only **scalar C%** — useful for bootstrap resampling where you only need the aggregate statistic
2. **v2 (base_instruct_dif.py):** Returns **per-item arrays** (delta_MH, p-value, is_C flag) — useful for item-level analysis, subgroup comparisons, and detailed reporting

**Algorithm differences:** Minimal. The R18 version uses slightly different sparse matrix handling (asarray().ravel()) but the MH-DIF computation is identical.

### Model Metadata CSV Header:
```
model_name, family, release_year, release_half, training_method, accuracy, cohort_temporal, cohort_accuracy_quintile
```
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "66586e39-e694-4cca-8331-3152c7b1d260",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find the full MH-DIF implementation in the codebase. Specifically:\n\n1. Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n2. Also look for any \"full version\" of this function that returns per-item delta_mh, p_value, is_c — check files in `artifacts/` subdirectories, especially anything related to R18 or base-vs-instruct.\n3. Read the model_metadata.csv header to confirm column names: `head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv`\n\nReturn the complete function code for both versions found.",
    "agentId": "a48e368fd2be8645c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile the complete findings.\n\n## Summary\n\nI've found the complete MH-DIF implementation in your codebase. Here are the two key versions:\n\n### 1. **Vectorized Total-Score Version (C% only)**\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n\n**Function `mh_dif_c_pct_vec()` (lines 34-101):**\n```python\ndef mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Fully vectorized MH-DIF → C%. Stratifies on total score (not rest).\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return is_c.sum() / J * 100\n```\n\n**Returns:** Scalar C% (percentage of DIF-flagged items)\n\n---\n\n### 2. **Full Per-Item Version (delta_mh, p_value, is_c)**\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py`\n\n**Function `mh_dif_full()` (lines 58-127):**\n```python\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\n\n    Returns (c_pct, delta_mh, pval, is_c).\n    \"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = k_ref == k\n        mf = k_foc == k\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()\n        if mf.any():\n            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)\n    c_pct = is_c.sum() / J * 100\n\n    return c_pct, delta_j, pval_j, is_c\n```\n\n**Returns:** Tuple of (c_pct, delta_mh_array, pval_array, is_c_bool_array)\n\n---\n\n### Key Differences:\n\n1. **v1 (mmlu_bootstrap_ci.py):** Returns only **scalar C%** — useful for bootstrap resampling where you only need the aggregate statistic\n2. **v2 (base_instruct_dif.py):** Returns **per-item arrays** (delta_MH, p-value, is_C flag) — useful for item-level analysis, subgroup comparisons, and detailed reporting\n\n**Algorithm differences:** Minimal. The R18 version uses slightly different sparse matrix handling (asarray().ravel()) but the MH-DIF computation is identical.\n\n### Model Metadata CSV Header:\n```\nmodel_name, family, release_year, release_half, training_method, accuracy, cohort_temporal, cohort_accuracy_quintile\n```"
      }
    ],
    "totalDurationMs": 57785,
    "totalTokens": 44856,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 41983,
      "output_tokens": 2677,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2677,
          "cache_read_input_tokens": 41983,
          "cache_creation_input_tokens": 190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 190,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 6,
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_016F5n447n7kVvQyhXtjSuKP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "8632efb4-43fe-4d1f-a7a0-a0fccdbb8c36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q97nS37Jo2HZVgardfh8nf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 25103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3018
      },
      "output_tokens": 73,
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

_source line 50 · 2026-05-22T18:48:43.339Z_

<details><summary>↩ Tool result · `toolu_016F5n447n7kVvQyhXtjSuKP`</summary>

```text
1	#!/usr/bin/env python3
2	"""R18: Base vs Instruct MH-DIF separation experiment."""
3	
4	import re
5	import sys
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse
9	from scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency
10	
11	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
12	OUT = f"{ROOT}/r18_base_vs_instruct_dif"
13	
14	N_STRATA = 5
15	N_BOOT = 1000
16	ALPHA = 0.05
17	DELTA_THRESH = 1.5
18	
19	# ── Part 1: Model classification ─────────────────────────────────────────
20	
21	INSTRUCT_SUFFIXES = re.compile(
22	    r"[-_\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)"
23	    r"([-_\.]|$)",
24	    re.IGNORECASE,
25	)
26	
27	QUANT_SUFFIXES = re.compile(
28	    r"[-_\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])",
29	    re.IGNORECASE,
30	)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "99e69e1d-d871-4e39-9376-7d9b17b2ce59",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
      "content": "#!/usr/bin/env python3\n\"\"\"R18: Base vs Instruct MH-DIF separation experiment.\"\"\"\n\nimport re\nimport sys\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r18_base_vs_instruct_dif\"\n\nN_STRATA = 5\nN_BOOT = 1000\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n# ── Part 1: Model classification ─────────────────────────────────────────\n\nINSTRUCT_SUFFIXES = re.compile(\n    r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)\"\n    r\"([-_\\.]|$)\",\n    re.IGNORECASE,\n)\n\nQUANT_SUFFIXES = re.compile(\n    r\"[-_\\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])\",\n    re.IGNORECASE,\n)",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 374
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01YTMN8jUwkg5AgKLcUDE7VX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "offset": 127
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "8a4be636-68d3-44b4-9fa9-23feb5cba6a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1FsVKcfF1prNpBqUxWqUY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 28121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 534
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

_source line 52 · 2026-05-22T18:48:46.189Z_

<details><summary>↩ Tool result · `toolu_01YTMN8jUwkg5AgKLcUDE7VX`</summary>

```text
127	    return c_pct, delta_j, pval_j, is_c
128	
129	
130	def ets_class(delta):
131	    a = abs(delta)
132	    if a < 1.0:
133	        return "A"
134	    elif a < 1.5:
135	        return "B"
136	    else:
137	        return "C"
138	
139	
140	# ── Main ──────────────────────────────────────────────────────────────────
141	
142	def main():
143	    print("Loading data...")
144	    meta = pd.read_csv(f"{ROOT}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv")
145	    rm = np.load(f"{ROOT}/response_matrix.npz")
146	    X = sparse.csr_matrix((rm["data"], rm["indices"], rm["indptr"]), shape=tuple(rm["shape"]))
147	    idx = np.load(f"{ROOT}/response_matrix_index.npz", allow_pickle=True)
148	    model_names = idx["model_names"]
149	    item_ids = idx["item_ids"]
150	
151	    # Build model name → row index lookup
152	    name2row = {n: i for i, n in enumerate(model_names)}
153	
154	    # Classify models
155	    meta = meta[meta["cohort_temporal"].isin(["2023", "2024"])].copy()
156	    meta["model_type"] = meta["model_name"].apply(classify_model)
157	
158	    # Save classification
159	    class_df = meta[["model_name", "model_type", "cohort_temporal", "family"]].copy()
160	    class_df.to_csv(f"{OUT}/model_classification.csv", index=False)
161	
162	    # Map to response matrix rows
163	    meta["rm_idx"] = meta["model_name"].map(name2row)
164	    meta = meta.dropna(subset=["rm_idx"])
165	    meta["rm_idx"] = meta["rm_idx"].astype(int)
166	
167	    # Group counts
168	    groups = {}
169	    for mtype in ["base", "instruct"]:
170	        ref_mask = (meta["model_type"] == mtype) & (meta["cohort_temporal"] == "2023")
171	        foc_mask = (meta["model_type"] == mtype) & (meta["cohort_temporal"] == "2024")
172	        groups[mtype] = {
173	            "ref_idx": meta.loc[ref_mask, "rm_idx"].values,
174	            "foc_idx": meta.loc[foc_mask, "rm_idx"].values,
175	        }
176	
177	    print("\n=== Part 4: Sample sizes ===")
178	    for mtype in ["base", "instruct"]:
179	        n_ref = len(groups[mtype]["ref_idx"])
180	        n_foc = len(groups[mtype]["foc_idx"])
181	        flag = " ⚠ UNDERPOWERED" if min(n_ref, n_foc) < 80 else ""
182	        print(f"  {mtype:>10s}: ref(2023)={n_ref}, foc(2024)={n_foc}{flag}")
183	    print(f"  {'full':>10s}: ref(2023)=1080, foc(2024)=807  (reported baseline)")
184	
185	    # Run MH-DIF per group
186	    results = {}
187	    for mtype in ["base", "instruct"]:
188	        ri, fi = groups[mtype]["ref_idx"], groups[mtype]["foc_idx"]
189	        print(f"\nRunning MH-DIF for {mtype} ({len(ri)} ref, {len(fi)} foc)...")
190	        X_ref = X[ri]
191	        X_foc = X[fi]
192	        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)
193	        results[mtype] = {"c_pct": c_pct, "delta": delta, "pval": pval, "is_c": is_c}
194	        print(f"  C% = {c_pct:.1f}%  ({is_c.sum()}/{len(is_c)} items)")
195	
196	    # ── Part 3a: Bootstrap CI for C% difference ──────────────────────────
197	    print("\n=== Part 3a: Bootstrap C% difference ===")
198	    rng = np.random.default_rng(42)
199	    boot_diff = np.zeros(N_BOOT)
200	
201	    for b in range(N_BOOT):
202	        if (b + 1) % 200 == 0:
203	            print(f"  bootstrap {b+1}/{N_BOOT}...")
204	        cpcts = {}
205	        for mtype in ["base", "instruct"]:
206	            ri, fi = groups[mtype]["ref_idx"], groups[mtype]["foc_idx"]
207	            ri_b = rng.choice(ri, size=len(ri), replace=True)
208	            fi_b = rng.choice(fi, size=len(fi), replace=True)
209	            c, _, _, _ = mh_dif_full(X[ri_b], X[fi_b])
210	            cpcts[mtype] = c
211	        boot_diff[b] = cpcts["base"] - cpcts["instruct"]
212	
213	    ci_lo, ci_hi = np.percentile(boot_diff, [2.5, 97.5])
214	    mean_diff = boot_diff.mean()
215	    print(f"  C%_base - C%_instruct = {results['base']['c_pct']:.1f} - {results['instruct']['c_pct']:.1f} = {results['base']['c_pct'] - results['instruct']['c_pct']:.1f}")
216	    print(f"  Bootstrap 95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]")
217	
218	    # ── Part 3b: Difficulty-direction gradient ────────────────────────────
219	    print("\n=== Part 3b: Difficulty-direction gradient ===")
220	    all_2023_idx = meta.loc[meta["cohort_temporal"] == "2023", "rm_idx"].values
221	    X_2023 = X[all_2023_idx]
222	    item_diff = np.asarray(X_2023.mean(axis=0), dtype=np.float64).ravel()
223	
224	    for mtype in ["base", "instruct"]:
225	        c_mask = results[mtype]["is_c"]
226	        if c_mask.sum() < 3:
227	            print(f"  {mtype}: too few C items ({c_mask.sum()}) for correlation")
228	            continue
229	        rho, p = spearmanr(item_diff[c_mask], results[mtype]["delta"][c_mask])
230	        print(f"  {mtype}: ρ(difficulty, Δ_MH) = {rho:.3f}  (p={p:.2e}, n={c_mask.sum()})")
231	
232	    # ── Part 3c: DIF item overlap ─────────────────────────────────────────
233	    print("\n=== Part 3c: DIF item overlap ===")
234	    c_base = set(np.where(results["base"]["is_c"])[0])
235	    c_inst = set(np.where(results["instruct"]["is_c"])[0])
236	    inter = c_base & c_inst
237	    union = c_base | c_inst
238	    jaccard = len(inter) / len(union) if union else 0
239	
240	    p_b = len(c_base) / len(item_ids)
241	    p_i = len(c_inst) / len(item_ids)
242	    expected_jaccard = (p_b * p_i) / (p_b + p_i - p_b * p_i) if (p_b + p_i - p_b * p_i) > 0 else 0
243	
244	    only_base = len(c_base - c_inst)
245	    only_inst = len(c_inst - c_base)
246	    both = len(inter)
247	    print(f"  |C_base|={len(c_base)}, |C_instruct|={len(c_inst)}")
248	    print(f"  Only base: {only_base}, Only instruct: {only_inst}, Both: {both}")
249	    print(f"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})")
250	
251	    # ── Part 3d: Direction distribution ───────────────────────────────────
252	    print("\n=== Part 3d: DIF direction distribution ===")
253	    dir_table = {}
254	    for mtype in ["base", "instruct"]:
255	        d = results[mtype]["delta"][results[mtype]["is_c"]]
256	        n_foc_fav = (d > 0).sum()
257	        n_ref_fav = (d < 0).sum()
258	        dir_table[mtype] = (int(n_foc_fav), int(n_ref_fav))
259	        total = n_foc_fav + n_ref_fav
260	        print(f"  {mtype}: focal-favoring={n_foc_fav} ({n_foc_fav/total*100:.1f}%), ref-favoring={n_ref_fav} ({n_ref_fav/total*100:.1f}%)")
261	
262	    ct = np.array([[dir_table["base"][0], dir_table["base"][1]],
263	                    [dir_table["instruct"][0], dir_table["instruct"][1]]])
264	    if ct.min() > 0:
265	        chi2_val, p_dir, _, _ = chi2_contingency(ct)
266	        print(f"  χ²={chi2_val:.2f}, p={p_dir:.3e}")
267	    else:
268	        p_dir = np.nan
269	        print("  χ² test not possible (zero cell)")
270	
271	    # ── Save per-item CSV ─────────────────────────────────────────────────
272	    print("\nSaving per-item results...")
273	
274	    # Extract subject from item_id (format: subject_qXXXX or similar)
275	    def get_subject(iid):
276	        parts = iid.rsplit("_", 1)
277	        return parts[0] if len(parts) > 1 else iid
278	
279	    item_df = pd.DataFrame({
280	        "item_id": item_ids,
281	        "subject": [get_subject(str(i)) for i in item_ids],
282	        "difficulty": item_diff,
283	        "delta_mh_base": results["base"]["delta"],
284	        "p_base": results["base"]["pval"],
285	        "ets_base": [ets_class(d) for d in results["base"]["delta"]],
286	        "is_c_base": results["base"]["is_c"],
287	        "delta_mh_instruct": results["instruct"]["delta"],
288	        "p_instruct": results["instruct"]["pval"],
289	        "ets_instruct": [ets_class(d) for d in results["instruct"]["delta"]],
290	        "is_c_instruct": results["instruct"]["is_c"],
291	    })
292	    item_df.to_csv(f"{OUT}/base_instruct_item_results.csv", index=False)
293	
294	    # ── Generate report ───────────────────────────────────────────────────
295	    print("Writing report...")
296	
297	    n_base_ref = len(groups["base"]["ref_idx"])
298	    n_base_foc = len(groups["base"]["foc_idx"])
299	    n_inst_ref = len(groups["instruct"]["ref_idx"])
300	    n_inst_foc = len(groups["instruct"]["foc_idx"])
301	
302	    report = f"""# R18: Base vs Instruct DIF Separation Experiment
303	
304	## Sample Sizes
305	
306	| Group | Ref (2023) | Foc (2024) | Total |
307	|-------|-----------|-----------|-------|
308	| Base | {n_base_ref} | {n_base_foc} | {n_base_ref + n_base_foc} |
309	| Instruct | {n_inst_ref} | {n_inst_foc} | {n_inst_ref + n_inst_foc} |
310	| Full (reported) | 1,080 | 807 | 1,887 |
311	
312	{"**⚠ Warning:** Some subgroups have N < 80; interpret with caution." if min(n_base_ref, n_base_foc, n_inst_ref, n_inst_foc) < 80 else "All subgroups have N ≥ 80; adequate power."}
313	
314	## C% Comparison
315	
316	| Group | C% | DIF-C items |
317	|-------|-----|------------|
318	| Base | {results['base']['c_pct']:.1f}% | {results['base']['is_c'].sum()}/{len(item_ids)} |
319	| Instruct | {results['instruct']['c_pct']:.1f}% | {results['instruct']['is_c'].sum()}/{len(item_ids)} |
320	| Full (reported) | 31.3% | — |
321	
322	**Difference (base − instruct):** {results['base']['c_pct'] - results['instruct']['c_pct']:.1f} pp
323	**Bootstrap 95% CI:** [{ci_lo:.1f}, {ci_hi:.1f}] (N={N_BOOT})
324	
325	## Difficulty–Direction Gradient
326	
327	Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:
328	
329	"""
330	
331	    for mtype in ["base", "instruct"]:
332	        c_mask = results[mtype]["is_c"]
333	        if c_mask.sum() >= 3:
334	            rho, p = spearmanr(item_diff[c_mask], results[mtype]["delta"][c_mask])
335	            report += f"- **{mtype.capitalize()}:** ρ = {rho:.3f} (p = {p:.2e}, n = {c_mask.sum()})\n"
336	        else:
337	            report += f"- **{mtype.capitalize()}:** too few C items ({c_mask.sum()}) for correlation\n"
338	
339	    report += f"""
340	## DIF Item Overlap
341	
342	| Metric | Value |
343	|--------|-------|
344	| C_base only | {only_base} |
345	| C_instruct only | {only_inst} |
346	| Both | {both} |
347	| Jaccard index | {jaccard:.3f} |
348	| Expected Jaccard (independence) | {expected_jaccard:.3f} |
349	| Jaccard / Expected ratio | {jaccard / expected_jaccard:.1f}× |
350	
351	## DIF Direction Distribution
352	
353	| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
354	|-------|----------------------|---------------------|
355	| Base | {dir_table['base'][0]} ({dir_table['base'][0]/(sum(dir_table['base']))*100:.1f}%) | {dir_table['base'][1]} ({dir_table['base'][1]/(sum(dir_table['base']))*100:.1f}%) |
356	| Instruct | {dir_table['instruct'][0]} ({dir_table['instruct'][0]/(sum(dir_table['instruct']))*100:.1f}%) | {dir_table['instruct'][1]} ({dir_table['instruct'][1]/(sum(dir_table['instruct']))*100:.1f}%) |
357	
358	χ² = {chi2_val:.2f}, p = {p_dir:.3e}
359	
360	## Output Files
361	
362	- `model_classification.csv` — {len(class_df)} models classified
363	- `base_instruct_item_results.csv` — {len(item_ids)} items with per-group DIF statistics
364	"""
365	
366	    with open(f"{OUT}/base_instruct_dif_report.md", "w") as f:
367	        f.write(report)
368	
369	    print(f"\nDone. Results in {OUT}/")
370	
371	
372	if __name__ == "__main__":
373	    main()
374	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "8da21352-8344-4174-a8e7-83b978c65a85",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
      "content": "    return c_pct, delta_j, pval_j, is_c\n\n\ndef ets_class(delta):\n    a = abs(delta)\n    if a < 1.0:\n        return \"A\"\n    elif a < 1.5:\n        return \"B\"\n    else:\n        return \"C\"\n\n\n# ── Main ──────────────────────────────────────────────────────────────────\n\ndef main():\n    print(\"Loading data...\")\n    meta = pd.read_csv(f\"{ROOT}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n    rm = np.load(f\"{ROOT}/response_matrix.npz\")\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]), shape=tuple(rm[\"shape\"]))\n    idx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n\n    # Build model name → row index lookup\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Classify models\n    meta = meta[meta[\"cohort_temporal\"].isin([\"2023\", \"2024\"])].copy()\n    meta[\"model_type\"] = meta[\"model_name\"].apply(classify_model)\n\n    # Save classification\n    class_df = meta[[\"model_name\", \"model_type\", \"cohort_temporal\", \"family\"]].copy()\n    class_df.to_csv(f\"{OUT}/model_classification.csv\", index=False)\n\n    # Map to response matrix rows\n    meta[\"rm_idx\"] = meta[\"model_name\"].map(name2row)\n    meta = meta.dropna(subset=[\"rm_idx\"])\n    meta[\"rm_idx\"] = meta[\"rm_idx\"].astype(int)\n\n    # Group counts\n    groups = {}\n    for mtype in [\"base\", \"instruct\"]:\n        ref_mask = (meta[\"model_type\"] == mtype) & (meta[\"cohort_temporal\"] == \"2023\")\n        foc_mask = (meta[\"model_type\"] == mtype) & (meta[\"cohort_temporal\"] == \"2024\")\n        groups[mtype] = {\n            \"ref_idx\": meta.loc[ref_mask, \"rm_idx\"].values,\n            \"foc_idx\": meta.loc[foc_mask, \"rm_idx\"].values,\n        }\n\n    print(\"\\n=== Part 4: Sample sizes ===\")\n    for mtype in [\"base\", \"instruct\"]:\n        n_ref = len(groups[mtype][\"ref_idx\"])\n        n_foc = len(groups[mtype][\"foc_idx\"])\n        flag = \" ⚠ UNDERPOWERED\" if min(n_ref, n_foc) < 80 else \"\"\n        print(f\"  {mtype:>10s}: ref(2023)={n_ref}, foc(2024)={n_foc}{flag}\")\n    print(f\"  {'full':>10s}: ref(2023)=1080, foc(2024)=807  (reported baseline)\")\n\n    # Run MH-DIF per group\n    results = {}\n    for mtype in [\"base\", \"instruct\"]:\n        ri, fi = groups[mtype][\"ref_idx\"], groups[mtype][\"foc_idx\"]\n        print(f\"\\nRunning MH-DIF for {mtype} ({len(ri)} ref, {len(fi)} foc)...\")\n        X_ref = X[ri]\n        X_foc = X[fi]\n        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)\n        results[mtype] = {\"c_pct\": c_pct, \"delta\": delta, \"pval\": pval, \"is_c\": is_c}\n        print(f\"  C% = {c_pct:.1f}%  ({is_c.sum()}/{len(is_c)} items)\")\n\n    # ── Part 3a: Bootstrap CI for C% difference ──────────────────────────\n    print(\"\\n=== Part 3a: Bootstrap C% difference ===\")\n    rng = np.random.default_rng(42)\n    boot_diff = np.zeros(N_BOOT)\n\n    for b in range(N_BOOT):\n        if (b + 1) % 200 == 0:\n            print(f\"  bootstrap {b+1}/{N_BOOT}...\")\n        cpcts = {}\n        for mtype in [\"base\", \"instruct\"]:\n            ri, fi = groups[mtype][\"ref_idx\"], groups[mtype][\"foc_idx\"]\n            ri_b = rng.choice(ri, size=len(ri), replace=True)\n            fi_b = rng.choice(fi, size=len(fi), replace=True)\n            c, _, _, _ = mh_dif_full(X[ri_b], X[fi_b])\n            cpcts[mtype] = c\n        boot_diff[b] = cpcts[\"base\"] - cpcts[\"instruct\"]\n\n    ci_lo, ci_hi = np.percentile(boot_diff, [2.5, 97.5])\n    mean_diff = boot_diff.mean()\n    print(f\"  C%_base - C%_instruct = {results['base']['c_pct']:.1f} - {results['instruct']['c_pct']:.1f} = {results['base']['c_pct'] - results['instruct']['c_pct']:.1f}\")\n    print(f\"  Bootstrap 95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]\")\n\n    # ── Part 3b: Difficulty-direction gradient ────────────────────────────\n    print(\"\\n=== Part 3b: Difficulty-direction gradient ===\")\n    all_2023_idx = meta.loc[meta[\"cohort_temporal\"] == \"2023\", \"rm_idx\"].values\n    X_2023 = X[all_2023_idx]\n    item_diff = np.asarray(X_2023.mean(axis=0), dtype=np.float64).ravel()\n\n    for mtype in [\"base\", \"instruct\"]:\n        c_mask = results[mtype][\"is_c\"]\n        if c_mask.sum() < 3:\n            print(f\"  {mtype}: too few C items ({c_mask.sum()}) for correlation\")\n            continue\n        rho, p = spearmanr(item_diff[c_mask], results[mtype][\"delta\"][c_mask])\n        print(f\"  {mtype}: ρ(difficulty, Δ_MH) = {rho:.3f}  (p={p:.2e}, n={c_mask.sum()})\")\n\n    # ── Part 3c: DIF item overlap ─────────────────────────────────────────\n    print(\"\\n=== Part 3c: DIF item overlap ===\")\n    c_base = set(np.where(results[\"base\"][\"is_c\"])[0])\n    c_inst = set(np.where(results[\"instruct\"][\"is_c\"])[0])\n    inter = c_base & c_inst\n    union = c_base | c_inst\n    jaccard = len(inter) / len(union) if union else 0\n\n    p_b = len(c_base) / len(item_ids)\n    p_i = len(c_inst) / len(item_ids)\n    expected_jaccard = (p_b * p_i) / (p_b + p_i - p_b * p_i) if (p_b + p_i - p_b * p_i) > 0 else 0\n\n    only_base = len(c_base - c_inst)\n    only_inst = len(c_inst - c_base)\n    both = len(inter)\n    print(f\"  |C_base|={len(c_base)}, |C_instruct|={len(c_inst)}\")\n    print(f\"  Only base: {only_base}, Only instruct: {only_inst}, Both: {both}\")\n    print(f\"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})\")\n\n    # ── Part 3d: Direction distribution ───────────────────────────────────\n    print(\"\\n=== Part 3d: DIF direction distribution ===\")\n    dir_table = {}\n    for mtype in [\"base\", \"instruct\"]:\n        d = results[mtype][\"delta\"][results[mtype][\"is_c\"]]\n        n_foc_fav = (d > 0).sum()\n        n_ref_fav = (d < 0).sum()\n        dir_table[mtype] = (int(n_foc_fav), int(n_ref_fav))\n        total = n_foc_fav + n_ref_fav\n        print(f\"  {mtype}: focal-favoring={n_foc_fav} ({n_foc_fav/total*100:.1f}%), ref-favoring={n_ref_fav} ({n_ref_fav/total*100:.1f}%)\")\n\n    ct = np.array([[dir_table[\"base\"][0], dir_table[\"base\"][1]],\n                    [dir_table[\"instruct\"][0], dir_table[\"instruct\"][1]]])\n    if ct.min() > 0:\n        chi2_val, p_dir, _, _ = chi2_contingency(ct)\n        print(f\"  χ²={chi2_val:.2f}, p={p_dir:.3e}\")\n    else:\n        p_dir = np.nan\n        print(\"  χ² test not possible (zero cell)\")\n\n    # ── Save per-item CSV ─────────────────────────────────────────────────\n    print(\"\\nSaving per-item results...\")\n\n    # Extract subject from item_id (format: subject_qXXXX or similar)\n    def get_subject(iid):\n        parts = iid.rsplit(\"_\", 1)\n        return parts[0] if len(parts) > 1 else iid\n\n    item_df = pd.DataFrame({\n        \"item_id\": item_ids,\n        \"subject\": [get_subject(str(i)) for i in item_ids],\n        \"difficulty\": item_diff,\n        \"delta_mh_base\": results[\"base\"][\"delta\"],\n        \"p_base\": results[\"base\"][\"pval\"],\n        \"ets_base\": [ets_class(d) for d in results[\"base\"][\"delta\"]],\n        \"is_c_base\": results[\"base\"][\"is_c\"],\n        \"delta_mh_instruct\": results[\"instruct\"][\"delta\"],\n        \"p_instruct\": results[\"instruct\"][\"pval\"],\n        \"ets_instruct\": [ets_class(d) for d in results[\"instruct\"][\"delta\"]],\n        \"is_c_instruct\": results[\"instruct\"][\"is_c\"],\n    })\n    item_df.to_csv(f\"{OUT}/base_instruct_item_results.csv\", index=False)\n\n    # ── Generate report ───────────────────────────────────────────────────\n    print(\"Writing report...\")\n\n    n_base_ref = len(groups[\"base\"][\"ref_idx\"])\n    n_base_foc = len(groups[\"base\"][\"foc_idx\"])\n    n_inst_ref = len(groups[\"instruct\"][\"ref_idx\"])\n    n_inst_foc = len(groups[\"instruct\"][\"foc_idx\"])\n\n    report = f\"\"\"# R18: Base vs Instruct DIF Separation Experiment\n\n## Sample Sizes\n\n| Group | Ref (2023) | Foc (2024) | Total |\n|-------|-----------|-----------|-------|\n| Base | {n_base_ref} | {n_base_foc} | {n_base_ref + n_base_foc} |\n| Instruct | {n_inst_ref} | {n_inst_foc} | {n_inst_ref + n_inst_foc} |\n| Full (reported) | 1,080 | 807 | 1,887 |\n\n{\"**⚠ Warning:** Some subgroups have N < 80; interpret with caution.\" if min(n_base_ref, n_base_foc, n_inst_ref, n_inst_foc) < 80 else \"All subgroups have N ≥ 80; adequate power.\"}\n\n## C% Comparison\n\n| Group | C% | DIF-C items |\n|-------|-----|------------|\n| Base | {results['base']['c_pct']:.1f}% | {results['base']['is_c'].sum()}/{len(item_ids)} |\n| Instruct | {results['instruct']['c_pct']:.1f}% | {results['instruct']['is_c'].sum()}/{len(item_ids)} |\n| Full (reported) | 31.3% | — |\n\n**Difference (base − instruct):** {results['base']['c_pct'] - results['instruct']['c_pct']:.1f} pp\n**Bootstrap 95% CI:** [{ci_lo:.1f}, {ci_hi:.1f}] (N={N_BOOT})\n\n## Difficulty–Direction Gradient\n\nSpearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:\n\n\"\"\"\n\n    for mtype in [\"base\", \"instruct\"]:\n        c_mask = results[mtype][\"is_c\"]\n        if c_mask.sum() >= 3:\n            rho, p = spearmanr(item_diff[c_mask], results[mtype][\"delta\"][c_mask])\n            report += f\"- **{mtype.capitalize()}:** ρ = {rho:.3f} (p = {p:.2e}, n = {c_mask.sum()})\\n\"\n        else:\n            report += f\"- **{mtype.capitalize()}:** too few C items ({c_mask.sum()}) for correlation\\n\"\n\n    report += f\"\"\"\n## DIF Item Overlap\n\n| Metric | Value |\n|--------|-------|\n| C_base only | {only_base} |\n| C_instruct only | {only_inst} |\n| Both | {both} |\n| Jaccard index | {jaccard:.3f} |\n| Expected Jaccard (independence) | {expected_jaccard:.3f} |\n| Jaccard / Expected ratio | {jaccard / expected_jaccard:.1f}× |\n\n## DIF Direction Distribution\n\n| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |\n|-------|----------------------|---------------------|\n| Base | {dir_table['base'][0]} ({dir_table['base'][0]/(sum(dir_table['base']))*100:.1f}%) | {dir_table['base'][1]} ({dir_table['base'][1]/(sum(dir_table['base']))*100:.1f}%) |\n| Instruct | {dir_table['instruct'][0]} ({dir_table['instruct'][0]/(sum(dir_table['instruct']))*100:.1f}%) | {dir_table['instruct'][1]} ({dir_table['instruct'][1]/(sum(dir_table['instruct']))*100:.1f}%) |\n\nχ² = {chi2_val:.2f}, p = {p_dir:.3e}\n\n## Output Files\n\n- `model_classification.csv` — {len(class_df)} models classified\n- `base_instruct_item_results.csv` — {len(item_ids)} items with per-group DIF statistics\n\"\"\"\n\n    with open(f\"{OUT}/base_instruct_dif_report.md\", \"w\") as f:\n        f.write(report)\n\n    print(f\"\\nDone. Results in {OUT}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 248,
      "startLine": 127,
      "totalLines": 374
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the R18 implementation. Let me write the R19 temporal granularity analysis script based on this pattern. I need to:

1. Load response matrix and model metadata
2. Split models by temporal cohorts (2023-H1, 2023-H2, 2024-H1)
3. Run pairwise MH-DIF for 3 comparisons
4. For each comparison, report: N_ref, N_foc, C%, ρ(difficulty, Δ_MH), direction distribution, top-5 subjects by C%


5. Export the results to CSV and markdown formats

Writing the analysis script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "75794ede-ce0a-404b-83d5-73855db30a0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoF7qpXapHR5KY8ViDCc8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 28655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

_source line 54_

Now I have the full picture. Let me create the output directory and write the analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "75728341-78e1-4b4e-a1d4-246f846f9422",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoF7qpXapHR5KY8ViDCc8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 28655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01JBf9CjPYHF8dbwK3ChaKwZ`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity",
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
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "2d684301-1b1e-4f3d-957b-42fea69ee66c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoF7qpXapHR5KY8ViDCc8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 28655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4644
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

_source line 56 · 2026-05-22T18:48:56.291Z_

<details><summary>↩ Tool result · `toolu_01JBf9CjPYHF8dbwK3ChaKwZ`</summary>

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
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "1b2f2d95-2922-4cb6-af63-c2e74e66f0bc",
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

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Write · `toolu_01MCbnLKKE53jSM1g6TY7kUc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_analysis.py",
  "content": "#!/usr/bin/env python3\n\"\"\"R19 Exp 1: Temporal Granularity DIF — half-year cohort pairwise MH-DIF.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r19_temporal_granularity\"\n\nN_STRATA = 5\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = k_ref == k\n        mf = k_foc == k\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()\n        if mf.any():\n            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)\n    c_pct = is_c.sum() / J * 100\n\n    return c_pct, delta_j, pval_j, is_c\n\n\ndef get_subject(iid):\n    parts = str(iid).rsplit(\"_\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)\n\n\ndef top_subjects_by_c_pct(item_ids, is_c, n=5):\n    \"\"\"Return top-N subjects ranked by within-subject C%.\"\"\"\n    subjs = np.array([get_subject(i) for i in item_ids])\n    unique_subjs = np.unique(subjs)\n    rows = []\n    for s in unique_subjs:\n        mask = subjs == s\n        total = mask.sum()\n        c_count = (is_c & mask).sum()\n        rows.append((s, c_count, total, c_count / total * 100))\n    rows.sort(key=lambda x: -x[3])\n    return rows[:n]\n\n\ndef main():\n    print(\"Loading data...\")\n    rm = np.load(f\"{ROOT}/response_matrix.npz\")\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]), shape=tuple(rm[\"shape\"]))\n    idx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    J = len(item_ids)\n\n    meta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Build half-year cohort label\n    meta[\"half_cohort\"] = meta[\"release_year\"].astype(str) + \"-\" + meta[\"release_half\"].astype(str)\n    meta[\"rm_idx\"] = meta[\"model_name\"].map(name2row)\n    meta = meta.dropna(subset=[\"rm_idx\"])\n    meta[\"rm_idx\"] = meta[\"rm_idx\"].astype(int)\n\n    print(\"\\nCohort distribution:\")\n    for hc in sorted(meta[\"half_cohort\"].unique()):\n        print(f\"  {hc}: {(meta['half_cohort'] == hc).sum()} models\")\n\n    # Define comparisons\n    comparisons = {\n        \"A: 2023-H1 vs 2023-H2\": (\"2023-H1\", \"2023-H2\"),\n        \"B: 2023-H2 vs 2024-H1\": (\"2023-H2\", \"2024-H1\"),\n        \"C: 2023-full vs 2024-H1\": ([\"2023-H1\", \"2023-H2\"], \"2024-H1\"),\n    }\n\n    all_results = []\n    item_level_dfs = []\n\n    for label, (ref_cohort, foc_cohort) in comparisons.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"Comparison {label}\")\n        print(f\"{'='*60}\")\n\n        if isinstance(ref_cohort, list):\n            ref_mask = meta[\"half_cohort\"].isin(ref_cohort)\n            ref_label = \"+\".join(ref_cohort)\n        else:\n            ref_mask = meta[\"half_cohort\"] == ref_cohort\n            ref_label = ref_cohort\n\n        foc_mask = meta[\"half_cohort\"] == foc_cohort\n        ref_idx = meta.loc[ref_mask, \"rm_idx\"].values\n        foc_idx = meta.loc[foc_mask, \"rm_idx\"].values\n        n_ref, n_foc = len(ref_idx), len(foc_idx)\n\n        underpowered = min(n_ref, n_foc) < 80\n        flag = \" ⚠ UNDERPOWERED\" if underpowered else \"\"\n        print(f\"  Ref ({ref_label}): {n_ref}{flag}\")\n        print(f\"  Foc ({foc_cohort}): {n_foc}{flag}\")\n\n        X_ref = X[ref_idx]\n        X_foc = X[foc_idx]\n        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)\n        n_c = int(is_c.sum())\n        print(f\"  C% = {c_pct:.1f}%  ({n_c}/{J} items)\")\n\n        # Difficulty = ref cohort mean accuracy per item\n        item_diff = np.asarray(X_ref.mean(axis=0), dtype=np.float64).ravel()\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        if n_c >= 3:\n            rho, rho_p = spearmanr(item_diff[is_c], delta[is_c])\n            print(f\"  ρ(difficulty, Δ_MH) = {rho:.3f}  (p={rho_p:.2e}, n={n_c})\")\n        else:\n            rho, rho_p = np.nan, np.nan\n            print(f\"  Too few C items ({n_c}) for correlation\")\n\n        # Direction distribution\n        c_delta = delta[is_c]\n        n_foc_fav = int((c_delta > 0).sum())\n        n_ref_fav = int((c_delta < 0).sum())\n        if n_c > 0:\n            pct_foc = n_foc_fav / n_c * 100\n            pct_ref = n_ref_fav / n_c * 100\n        else:\n            pct_foc = pct_ref = 0\n        print(f\"  Direction: focal-favoring={n_foc_fav} ({pct_foc:.1f}%), ref-favoring={n_ref_fav} ({pct_ref:.1f}%)\")\n\n        # Top-5 subjects by C%\n        top5 = top_subjects_by_c_pct(item_ids, is_c, n=5)\n        print(f\"  Top-5 subjects by C%:\")\n        for subj, cc, tt, cpct in top5:\n            print(f\"    {subj}: {cpct:.1f}% ({cc}/{tt})\")\n\n        all_results.append({\n            \"comparison\": label,\n            \"ref_cohort\": ref_label,\n            \"foc_cohort\": foc_cohort,\n            \"n_ref\": n_ref,\n            \"n_foc\": n_foc,\n            \"underpowered\": underpowered,\n            \"c_pct\": round(c_pct, 2),\n            \"n_c_items\": n_c,\n            \"n_total_items\": J,\n            \"rho_difficulty_delta\": round(rho, 3) if not np.isnan(rho) else None,\n            \"rho_p_value\": f\"{rho_p:.2e}\" if not np.isnan(rho_p) else None,\n            \"n_focal_favoring\": n_foc_fav,\n            \"n_ref_favoring\": n_ref_fav,\n            \"pct_focal_favoring\": round(pct_foc, 1),\n            \"pct_ref_favoring\": round(pct_ref, 1),\n            \"top5_subjects\": \"; \".join(f\"{s} ({cp:.1f}%)\" for s, _, _, cp in top5),\n        })\n\n        # Per-item data for this comparison\n        short_label = label.split(\":\")[0].strip()\n        item_level_dfs.append(pd.DataFrame({\n            \"item_id\": item_ids,\n            \"comparison\": short_label,\n            \"difficulty_ref\": item_diff,\n            \"delta_mh\": delta,\n            \"p_value\": pval,\n            \"is_c\": is_c,\n            \"direction\": np.where(delta > 0, \"focal-favoring\", np.where(delta < 0, \"ref-favoring\", \"none\")),\n        }))\n\n    # Save CSV\n    results_df = pd.DataFrame(all_results)\n    results_df.to_csv(f\"{OUT}/temporal_granularity_results.csv\", index=False)\n    print(f\"\\nSaved: {OUT}/temporal_granularity_results.csv\")\n\n    item_all = pd.concat(item_level_dfs, ignore_index=True)\n    item_all.to_csv(f\"{OUT}/temporal_granularity_items.csv\", index=False)\n    print(f\"Saved: {OUT}/temporal_granularity_items.csv\")\n\n    # ── Key analyses ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 60)\n    print(\"KEY ANALYSES\")\n    print(\"=\" * 60)\n\n    cpcts = [r[\"c_pct\"] for r in all_results]\n    labels = [r[\"comparison\"] for r in all_results]\n    print(f\"\\n1. C% monotonicity: {' → '.join(f'{l}: {c}%' for l, c in zip(labels, cpcts))}\")\n    if cpcts[0] < cpcts[1] < cpcts[2]:\n        print(\"   ✓ Monotonically increasing (A < B < C)\")\n    else:\n        print(\"   ✗ Not monotonically increasing\")\n\n    rhos = [r[\"rho_difficulty_delta\"] for r in all_results]\n    print(f\"\\n2. ρ gradient consistency: {rhos}\")\n    non_null = [r for r in rhos if r is not None]\n    if len(non_null) >= 2:\n        signs = [np.sign(r) for r in non_null]\n        if len(set(signs)) == 1:\n            print(f\"   ✓ Consistent sign across comparisons (all {'positive' if signs[0] > 0 else 'negative'})\")\n        else:\n            print(\"   ✗ Inconsistent signs across comparisons\")\n\n    print(f\"\\n3. Direction distribution shift:\")\n    for r in all_results:\n        print(f\"   {r['comparison']}: focal-fav {r['pct_focal_favoring']}% | ref-fav {r['pct_ref_favoring']}%\")\n\n    # ── Report ────────────────────────────────────────────────────────────\n    print(\"\\nWriting report...\")\n\n    report = \"# R19 Exp 1: Temporal Granularity DIF\\n\\n\"\n    report += \"## Design\\n\\n\"\n    report += \"Pairwise MH-DIF across half-year cohorts to test whether DIF accumulates with temporal distance.\\n\\n\"\n    report += \"| Comparison | Ref | Foc | N_ref | N_foc | Note |\\n\"\n    report += \"|------------|-----|-----|-------|-------|------|\\n\"\n    for r in all_results:\n        note = \"⚠ underpowered\" if r[\"underpowered\"] else \"\"\n        report += f\"| {r['comparison']} | {r['ref_cohort']} | {r['foc_cohort']} | {r['n_ref']} | {r['n_foc']} | {note} |\\n\"\n\n    report += \"\\n## Results\\n\\n\"\n    report += \"### C% (ETS Category C items)\\n\\n\"\n    report += \"| Comparison | C% | DIF-C items |\\n\"\n    report += \"|------------|-----|-------------|\\n\"\n    for r in all_results:\n        report += f\"| {r['comparison']} | {r['c_pct']:.1f}% | {r['n_c_items']}/{r['n_total_items']} |\\n\"\n\n    mono = cpcts[0] < cpcts[1] < cpcts[2]\n    report += f\"\\nMonotonicity (A < B < C): **{'yes' if mono else 'no'}**\\n\"\n\n    report += \"\\n### Difficulty–Direction Gradient\\n\\n\"\n    report += \"Spearman ρ(item difficulty, Δ_MH) among DIF-C items:\\n\\n\"\n    report += \"| Comparison | ρ | p | n |\\n\"\n    report += \"|------------|---|---|---|\\n\"\n    for r in all_results:\n        rho_str = f\"{r['rho_difficulty_delta']:.3f}\" if r[\"rho_difficulty_delta\"] is not None else \"—\"\n        p_str = r[\"rho_p_value\"] if r[\"rho_p_value\"] is not None else \"—\"\n        report += f\"| {r['comparison']} | {rho_str} | {p_str} | {r['n_c_items']} |\\n\"\n\n    report += \"\\n### Direction Distribution\\n\\n\"\n    report += \"| Comparison | Focal-favoring | Ref-favoring |\\n\"\n    report += \"|------------|---------------|-------------|\\n\"\n    for r in all_results:\n        report += f\"| {r['comparison']} | {r['n_focal_favoring']} ({r['pct_focal_favoring']}%) | {r['n_ref_favoring']} ({r['pct_ref_favoring']}%) |\\n\"\n\n    report += \"\\n### Top-5 Subjects by C%\\n\\n\"\n    for r in all_results:\n        report += f\"**{r['comparison']}:** {r['top5_subjects']}\\n\\n\"\n\n    report += \"## Key Findings\\n\\n\"\n    report += f\"1. **C% monotonicity:** {'Confirmed' if mono else 'Not confirmed'} — \"\n    report += f\"C% = {cpcts[0]:.1f}% → {cpcts[1]:.1f}% → {cpcts[2]:.1f}%\\n\"\n\n    if len(non_null) >= 2:\n        signs = [np.sign(r) for r in non_null]\n        consistent = len(set(signs)) == 1\n        report += f\"2. **ρ gradient:** {'Consistent' if consistent else 'Inconsistent'} sign across comparisons \"\n        report += f\"({', '.join(f'{r:.3f}' for r in non_null)})\\n\"\n    else:\n        report += \"2. **ρ gradient:** Insufficient data for comparison\\n\"\n\n    report += \"3. **Direction distribution:** See table above\\n\"\n\n    report += \"\\n## Output Files\\n\\n\"\n    report += \"- `temporal_granularity_results.csv` — summary per comparison\\n\"\n    report += \"- `temporal_granularity_items.csv` — per-item DIF statistics for each comparison\\n\"\n\n    with open(f\"{OUT}/temporal_granularity_report.md\", \"w\") as f:\n        f.write(report)\n    print(f\"Saved: {OUT}/temporal_granularity_report.md\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "cacc0ca3-f0c1-4b07-a3b7-32255eb19538",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVDVWzTrEuquCpAazSvFJ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 33299,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 322
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

_source line 58 · 2026-05-22T18:50:02.775Z_

<details><summary>↩ Tool result · `toolu_01MCbnLKKE53jSM1g6TY7kUc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "40473ba1-30a2-4119-901f-255f9f719eba",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_analysis.py",
    "content": "#!/usr/bin/env python3\n\"\"\"R19 Exp 1: Temporal Granularity DIF — half-year cohort pairwise MH-DIF.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r19_temporal_granularity\"\n\nN_STRATA = 5\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = k_ref == k\n        mf = k_foc == k\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()\n        if mf.any():\n            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)\n    c_pct = is_c.sum() / J * 100\n\n    return c_pct, delta_j, pval_j, is_c\n\n\ndef get_subject(iid):\n    parts = str(iid).rsplit(\"_\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)\n\n\ndef top_subjects_by_c_pct(item_ids, is_c, n=5):\n    \"\"\"Return top-N subjects ranked by within-subject C%.\"\"\"\n    subjs = np.array([get_subject(i) for i in item_ids])\n    unique_subjs = np.unique(subjs)\n    rows = []\n    for s in unique_subjs:\n        mask = subjs == s\n        total = mask.sum()\n        c_count = (is_c & mask).sum()\n        rows.append((s, c_count, total, c_count / total * 100))\n    rows.sort(key=lambda x: -x[3])\n    return rows[:n]\n\n\ndef main():\n    print(\"Loading data...\")\n    rm = np.load(f\"{ROOT}/response_matrix.npz\")\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]), shape=tuple(rm[\"shape\"]))\n    idx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    J = len(item_ids)\n\n    meta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Build half-year cohort label\n    meta[\"half_cohort\"] = meta[\"release_year\"].astype(str) + \"-\" + meta[\"release_half\"].astype(str)\n    meta[\"rm_idx\"] = meta[\"model_name\"].map(name2row)\n    meta = meta.dropna(subset=[\"rm_idx\"])\n    meta[\"rm_idx\"] = meta[\"rm_idx\"].astype(int)\n\n    print(\"\\nCohort distribution:\")\n    for hc in sorted(meta[\"half_cohort\"].unique()):\n        print(f\"  {hc}: {(meta['half_cohort'] == hc).sum()} models\")\n\n    # Define comparisons\n    comparisons = {\n        \"A: 2023-H1 vs 2023-H2\": (\"2023-H1\", \"2023-H2\"),\n        \"B: 2023-H2 vs 2024-H1\": (\"2023-H2\", \"2024-H1\"),\n        \"C: 2023-full vs 2024-H1\": ([\"2023-H1\", \"2023-H2\"], \"2024-H1\"),\n    }\n\n    all_results = []\n    item_level_dfs = []\n\n    for label, (ref_cohort, foc_cohort) in comparisons.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"Comparison {label}\")\n        print(f\"{'='*60}\")\n\n        if isinstance(ref_cohort, list):\n            ref_mask = meta[\"half_cohort\"].isin(ref_cohort)\n            ref_label = \"+\".join(ref_cohort)\n        else:\n            ref_mask = meta[\"half_cohort\"] == ref_cohort\n            ref_label = ref_cohort\n\n        foc_mask = meta[\"half_cohort\"] == foc_cohort\n        ref_idx = meta.loc[ref_mask, \"rm_idx\"].values\n        foc_idx = meta.loc[foc_mask, \"rm_idx\"].values\n        n_ref, n_foc = len(ref_idx), len(foc_idx)\n\n        underpowered = min(n_ref, n_foc) < 80\n        flag = \" ⚠ UNDERPOWERED\" if underpowered else \"\"\n        print(f\"  Ref ({ref_label}): {n_ref}{flag}\")\n        print(f\"  Foc ({foc_cohort}): {n_foc}{flag}\")\n\n        X_ref = X[ref_idx]\n        X_foc = X[foc_idx]\n        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)\n        n_c = int(is_c.sum())\n        print(f\"  C% = {c_pct:.1f}%  ({n_c}/{J} items)\")\n\n        # Difficulty = ref cohort mean accuracy per item\n        item_diff = np.asarray(X_ref.mean(axis=0), dtype=np.float64).ravel()\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        if n_c >= 3:\n            rho, rho_p = spearmanr(item_diff[is_c], delta[is_c])\n            print(f\"  ρ(difficulty, Δ_MH) = {rho:.3f}  (p={rho_p:.2e}, n={n_c})\")\n        else:\n            rho, rho_p = np.nan, np.nan\n            print(f\"  Too few C items ({n_c}) for correlation\")\n\n        # Direction distribution\n        c_delta = delta[is_c]\n        n_foc_fav = int((c_delta > 0).sum())\n        n_ref_fav = int((c_delta < 0).sum())\n        if n_c > 0:\n            pct_foc = n_foc_fav / n_c * 100\n            pct_ref = n_ref_fav / n_c * 100\n        else:\n            pct_foc = pct_ref = 0\n        print(f\"  Direction: focal-favoring={n_foc_fav} ({pct_foc:.1f}%), ref-favoring={n_ref_fav} ({pct_ref:.1f}%)\")\n\n        # Top-5 subjects by C%\n        top5 = top_subjects_by_c_pct(item_ids, is_c, n=5)\n        print(f\"  Top-5 subjects by C%:\")\n        for subj, cc, tt, cpct in top5:\n            print(f\"    {subj}: {cpct:.1f}% ({cc}/{tt})\")\n\n        all_results.append({\n            \"comparison\": label,\n            \"ref_cohort\": ref_label,\n            \"foc_cohort\": foc_cohort,\n            \"n_ref\": n_ref,\n            \"n_foc\": n_foc,\n            \"underpowered\": underpowered,\n            \"c_pct\": round(c_pct, 2),\n            \"n_c_items\": n_c,\n            \"n_total_items\": J,\n            \"rho_difficulty_delta\": round(rho, 3) if not np.isnan(rho) else None,\n            \"rho_p_value\": f\"{rho_p:.2e}\" if not np.isnan(rho_p) else None,\n            \"n_focal_favoring\": n_foc_fav,\n            \"n_ref_favoring\": n_ref_fav,\n            \"pct_focal_favoring\": round(pct_foc, 1),\n            \"pct_ref_favoring\": round(pct_ref, 1),\n            \"top5_subjects\": \"; \".join(f\"{s} ({cp:.1f}%)\" for s, _, _, cp in top5),\n        })\n\n        # Per-item data for this comparison\n        short_label = label.split(\":\")[0].strip()\n        item_level_dfs.append(pd.DataFrame({\n            \"item_id\": item_ids,\n            \"comparison\": short_label,\n            \"difficulty_ref\": item_diff,\n            \"delta_mh\": delta,\n            \"p_value\": pval,\n            \"is_c\": is_c,\n            \"direction\": np.where(delta > 0, \"focal-favoring\", np.where(delta < 0, \"ref-favoring\", \"none\")),\n        }))\n\n    # Save CSV\n    results_df = pd.DataFrame(all_results)\n    results_df.to_csv(f\"{OUT}/temporal_granularity_results.csv\", index=False)\n    print(f\"\\nSaved: {OUT}/temporal_granularity_results.csv\")\n\n    item_all = pd.concat(item_level_dfs, ignore_index=True)\n    item_all.to_csv(f\"{OUT}/temporal_granularity_items.csv\", index=False)\n    print(f\"Saved: {OUT}/temporal_granularity_items.csv\")\n\n    # ── Key analyses ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 60)\n    print(\"KEY ANALYSES\")\n    print(\"=\" * 60)\n\n    cpcts = [r[\"c_pct\"] for r in all_results]\n    labels = [r[\"comparison\"] for r in all_results]\n    print(f\"\\n1. C% monotonicity: {' → '.join(f'{l}: {c}%' for l, c in zip(labels, cpcts))}\")\n    if cpcts[0] < cpcts[1] < cpcts[2]:\n        print(\"   ✓ Monotonically increasing (A < B < C)\")\n    else:\n        print(\"   ✗ Not monotonically increasing\")\n\n    rhos = [r[\"rho_difficulty_delta\"] for r in all_results]\n    print(f\"\\n2. ρ gradient consistency: {rhos}\")\n    non_null = [r for r in rhos if r is not None]\n    if len(non_null) >= 2:\n        signs = [np.sign(r) for r in non_null]\n        if len(set(signs)) == 1:\n            print(f\"   ✓ Consistent sign across comparisons (all {'positive' if signs[0] > 0 else 'negative'})\")\n        else:\n            print(\"   ✗ Inconsistent signs across comparisons\")\n\n    print(f\"\\n3. Direction distribution shift:\")\n    for r in all_results:\n        print(f\"   {r['comparison']}: focal-fav {r['pct_focal_favoring']}% | ref-fav {r['pct_ref_favoring']}%\")\n\n    # ── Report ────────────────────────────────────────────────────────────\n    print(\"\\nWriting report...\")\n\n    report = \"# R19 Exp 1: Temporal Granularity DIF\\n\\n\"\n    report += \"## Design\\n\\n\"\n    report += \"Pairwise MH-DIF across half-year cohorts to test whether DIF accumulates with temporal distance.\\n\\n\"\n    report += \"| Comparison | Ref | Foc | N_ref | N_foc | Note |\\n\"\n    report += \"|------------|-----|-----|-------|-------|------|\\n\"\n    for r in all_results:\n        note = \"⚠ underpowered\" if r[\"underpowered\"] else \"\"\n        report += f\"| {r['comparison']} | {r['ref_cohort']} | {r['foc_cohort']} | {r['n_ref']} | {r['n_foc']} | {note} |\\n\"\n\n    report += \"\\n## Results\\n\\n\"\n    report += \"### C% (ETS Category C items)\\n\\n\"\n    report += \"| Comparison | C% | DIF-C items |\\n\"\n    report += \"|------------|-----|-------------|\\n\"\n    for r in all_results:\n        report += f\"| {r['comparison']} | {r['c_pct']:.1f}% | {r['n_c_items']}/{r['n_total_items']} |\\n\"\n\n    mono = cpcts[0] < cpcts[1] < cpcts[2]\n    report += f\"\\nMonotonicity (A < B < C): **{'yes' if mono else 'no'}**\\n\"\n\n    report += \"\\n### Difficulty–Direction Gradient\\n\\n\"\n    report += \"Spearman ρ(item difficulty, Δ_MH) among DIF-C items:\\n\\n\"\n    report += \"| Comparison | ρ | p | n |\\n\"\n    report += \"|------------|---|---|---|\\n\"\n    for r in all_results:\n        rho_str = f\"{r['rho_difficulty_delta']:.3f}\" if r[\"rho_difficulty_delta\"] is not None else \"—\"\n        p_str = r[\"rho_p_value\"] if r[\"rho_p_value\"] is not None else \"—\"\n        report += f\"| {r['comparison']} | {rho_str} | {p_str} | {r['n_c_items']} |\\n\"\n\n    report += \"\\n### Direction Distribution\\n\\n\"\n    report += \"| Comparison | Focal-favoring | Ref-favoring |\\n\"\n    report += \"|------------|---------------|-------------|\\n\"\n    for r in all_results:\n        report += f\"| {r['comparison']} | {r['n_focal_favoring']} ({r['pct_focal_favoring']}%) | {r['n_ref_favoring']} ({r['pct_ref_favoring']}%) |\\n\"\n\n    report += \"\\n### Top-5 Subjects by C%\\n\\n\"\n    for r in all_results:\n        report += f\"**{r['comparison']}:** {r['top5_subjects']}\\n\\n\"\n\n    report += \"## Key Findings\\n\\n\"\n    report += f\"1. **C% monotonicity:** {'Confirmed' if mono else 'Not confirmed'} — \"\n    report += f\"C% = {cpcts[0]:.1f}% → {cpcts[1]:.1f}% → {cpcts[2]:.1f}%\\n\"\n\n    if len(non_null) >= 2:\n        signs = [np.sign(r) for r in non_null]\n        consistent = len(set(signs)) == 1\n        report += f\"2. **ρ gradient:** {'Consistent' if consistent else 'Inconsistent'} sign across comparisons \"\n        report += f\"({', '.join(f'{r:.3f}' for r in non_null)})\\n\"\n    else:\n        report += \"2. **ρ gradient:** Insufficient data for comparison\\n\"\n\n    report += \"3. **Direction distribution:** See table above\\n\"\n\n    report += \"\\n## Output Files\\n\\n\"\n    report += \"- `temporal_granularity_results.csv` — summary per comparison\\n\"\n    report += \"- `temporal_granularity_items.csv` — per-item DIF statistics for each comparison\\n\"\n\n    with open(f\"{OUT}/temporal_granularity_report.md\", \"w\") as f:\n        f.write(report)\n    print(f\"Saved: {OUT}/temporal_granularity_report.md\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01CFiiFao9zKNTK7Qibp427u`</summary>

```json
{
  "command": "python3 artifacts/r19_temporal_granularity/temporal_granularity_analysis.py",
  "description": "Run temporal granularity DIF analysis",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "50738939-1d2e-4c94-b4b7-95ebfa99634b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjFbAjjJQnL9EPfVLzoYkU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5246,
      "cache_read_input_tokens": 33621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5246
      },
      "output_tokens": 65,
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

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b3js7rec2",
  "tool_use_id": "toolu_01CFiiFao9zKNTK7Qibp427u",
  "description": "Run temporal granularity DIF analysis",
  "task_type": "local_bash",
  "uuid": "9e9d6e76-d920-4e3a-a3d3-ebc0a97c5495",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b3js7rec2",
  "tool_use_id": "toolu_01CFiiFao9zKNTK7Qibp427u",
  "status": "completed",
  "output_file": "",
  "summary": "Run temporal granularity DIF analysis",
  "uuid": "8ea2a0f7-8aa6-4e1f-97ee-5d8a1f7ce36e",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool result

_source line 62 · 2026-05-22T18:50:10.859Z_

<details><summary>↩ Tool result · `toolu_01CFiiFao9zKNTK7Qibp427u`</summary>

```text
Loading data...

Cohort distribution:
  2023-H1: 62 models
  2023-H2: 1018 models
  2024-H1: 807 models
  unknown-unknown: 3340 models

============================================================
Comparison A: 2023-H1 vs 2023-H2
============================================================
  Ref (2023-H1): 62 ⚠ UNDERPOWERED
  Foc (2023-H2): 1018 ⚠ UNDERPOWERED
  C% = 22.6%  (2828/12508 items)
  ρ(difficulty, Δ_MH) = -0.608  (p=3.01e-285, n=2828)
  Direction: focal-favoring=1763 (62.3%), ref-favoring=1065 (37.7%)
  Top-5 subjects by C%:
    anatomy.100: 100.0% (1/1)
    anatomy.101: 100.0% (1/1)
    anatomy.103: 100.0% (1/1)
    anatomy.104: 100.0% (1/1)
    anatomy.106: 100.0% (1/1)

============================================================
Comparison B: 2023-H2 vs 2024-H1
============================================================
  Ref (2023-H2): 1018
  Foc (2024-H1): 807
  C% = 34.3%  (4296/12508 items)
  ρ(difficulty, Δ_MH) = -0.594  (p=0.00e+00, n=4296)
  Direction: focal-favoring=1745 (40.6%), ref-favoring=2551 (59.4%)
  Top-5 subjects by C%:
    anatomy.1: 100.0% (1/1)
    anatomy.104: 100.0% (1/1)
    anatomy.11: 100.0% (1/1)
    anatomy.110: 100.0% (1/1)
    anatomy.111: 100.0% (1/1)

============================================================
Comparison C: 2023-full vs 2024-H1
============================================================
  Ref (2023-H1+2023-H2): 1080
  Foc (2024-H1): 807
  C% = 31.3%  (3918/12508 items)
  ρ(difficulty, Δ_MH) = -0.587  (p=0.00e+00, n=3918)
  Direction: focal-favoring=1719 (43.9%), ref-favoring=2199 (56.1%)
  Top-5 subjects by C%:
    anatomy.1: 100.0% (1/1)
    anatomy.104: 100.0% (1/1)
    anatomy.11: 100.0% (1/1)
    anatomy.110: 100.0% (1/1)
    anatomy.111: 100.0% (1/1)

Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_results.csv
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_items.csv

============================================================
KEY ANALYSES
============================================================

1. C% monotonicity: A: 2023-H1 vs 2023-H2: 22.61% → B: 2023-H2 vs 2024-H1: 34.35% → C: 2023-full vs 2024-H1: 31.32%
   ✗ Not monotonically increasing

2. ρ gradient consistency: [np.float64(-0.608), np.float64(-0.594), np.float64(-0.587)]
   ✓ Consistent sign across comparisons (all negative)

3. Direction distribution shift:
   A: 2023-H1 vs 2023-H2: focal-fav 62.3% | ref-fav 37.7%
   B: 2023-H2 vs 2024-H1: focal-fav 40.6% | ref-fav 59.4%
   C: 2023-full vs 2024-H1: focal-fav 43.9% | ref-fav 56.1%

Writing report...
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_report.md

Done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "0567b8bd-3f5f-455f-8a29-82997dad8247",
  "tool_use_result": {
    "stdout": "Loading data...\n\nCohort distribution:\n  2023-H1: 62 models\n  2023-H2: 1018 models\n  2024-H1: 807 models\n  unknown-unknown: 3340 models\n\n============================================================\nComparison A: 2023-H1 vs 2023-H2\n============================================================\n  Ref (2023-H1): 62 ⚠ UNDERPOWERED\n  Foc (2023-H2): 1018 ⚠ UNDERPOWERED\n  C% = 22.6%  (2828/12508 items)\n  ρ(difficulty, Δ_MH) = -0.608  (p=3.01e-285, n=2828)\n  Direction: focal-favoring=1763 (62.3%), ref-favoring=1065 (37.7%)\n  Top-5 subjects by C%:\n    anatomy.100: 100.0% (1/1)\n    anatomy.101: 100.0% (1/1)\n    anatomy.103: 100.0% (1/1)\n    anatomy.104: 100.0% (1/1)\n    anatomy.106: 100.0% (1/1)\n\n============================================================\nComparison B: 2023-H2 vs 2024-H1\n============================================================\n  Ref (2023-H2): 1018\n  Foc (2024-H1): 807\n  C% = 34.3%  (4296/12508 items)\n  ρ(difficulty, Δ_MH) = -0.594  (p=0.00e+00, n=4296)\n  Direction: focal-favoring=1745 (40.6%), ref-favoring=2551 (59.4%)\n  Top-5 subjects by C%:\n    anatomy.1: 100.0% (1/1)\n    anatomy.104: 100.0% (1/1)\n    anatomy.11: 100.0% (1/1)\n    anatomy.110: 100.0% (1/1)\n    anatomy.111: 100.0% (1/1)\n\n============================================================\nComparison C: 2023-full vs 2024-H1\n============================================================\n  Ref (2023-H1+2023-H2): 1080\n  Foc (2024-H1): 807\n  C% = 31.3%  (3918/12508 items)\n  ρ(difficulty, Δ_MH) = -0.587  (p=0.00e+00, n=3918)\n  Direction: focal-favoring=1719 (43.9%), ref-favoring=2199 (56.1%)\n  Top-5 subjects by C%:\n    anatomy.1: 100.0% (1/1)\n    anatomy.104: 100.0% (1/1)\n    anatomy.11: 100.0% (1/1)\n    anatomy.110: 100.0% (1/1)\n    anatomy.111: 100.0% (1/1)\n\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_results.csv\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_items.csv\n\n============================================================\nKEY ANALYSES\n============================================================\n\n1. C% monotonicity: A: 2023-H1 vs 2023-H2: 22.61% → B: 2023-H2 vs 2024-H1: 34.35% → C: 2023-full vs 2024-H1: 31.32%\n   ✗ Not monotonically increasing\n\n2. ρ gradient consistency: [np.float64(-0.608), np.float64(-0.594), np.float64(-0.587)]\n   ✓ Consistent sign across comparisons (all negative)\n\n3. Direction distribution shift:\n   A: 2023-H1 vs 2023-H2: focal-fav 62.3% | ref-fav 37.7%\n   B: 2023-H2 vs 2024-H1: focal-fav 40.6% | ref-fav 59.4%\n   C: 2023-full vs 2024-H1: focal-fav 43.9% | ref-fav 56.1%\n\nWriting report...\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_report.md\n\nDone.",
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

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
The analysis ran successfully. Let me fix the top-5 subjects issue — it's showing individual items (anatomy.100, anatomy.101) rather than subjects. The `get_subject` function splits on the last underscore, but the item_ids seem to have a format like "anatomy_100" which splits into ("anatomy", "100"). But we're seeing "anatomy.100" which means the item_ids use dots, not underscores.

Let me check the item_id format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "d4e057c7-1825-443d-b0d9-f65ae45b8f44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP9DkTQXRn8JpmT2mALb3h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 38867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1346
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

_source line 64_

Top-5 subjects are showing individual items, not proper subjects. Let me check the item_id format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "f0dce21d-2276-4cb3-a7df-9c09199ffe8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP9DkTQXRn8JpmT2mALb3h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 38867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1346
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_011xzESD4hwaVGT8MNcUYMVX`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nidx = np.load('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz', allow_pickle=True)\nids = idx['item_ids']\nprint('First 20:', ids[:20])\nprint('Total:', len(ids))\n# Check unique patterns\nsamples = [str(x) for x in ids[:100]]\nfor s in samples[:10]:\n    print(repr(s))\n\"",
  "description": "Check item_id format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "7727553f-5c63-43b5-89a2-e7be6a21bcb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP9DkTQXRn8JpmT2mALb3h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 38867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1346
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

_source line 66 · 2026-05-22T18:50:18.511Z_

<details><summary>↩ Tool result · `toolu_011xzESD4hwaVGT8MNcUYMVX`</summary>

```text
First 20: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'
 'abstract_algebra.11' 'abstract_algebra.12' 'abstract_algebra.13'
 'abstract_algebra.14' 'abstract_algebra.15' 'abstract_algebra.16'
 'abstract_algebra.17' 'abstract_algebra.18' 'abstract_algebra.2'
 'abstract_algebra.20' 'abstract_algebra.21' 'abstract_algebra.22'
 'abstract_algebra.23' 'abstract_algebra.24' 'abstract_algebra.25'
 'abstract_algebra.26' 'abstract_algebra.27']
Total: 12508
'abstract_algebra.1'
'abstract_algebra.10'
'abstract_algebra.100'
'abstract_algebra.11'
'abstract_algebra.12'
'abstract_algebra.13'
'abstract_algebra.14'
'abstract_algebra.15'
'abstract_algebra.16'
'abstract_algebra.17'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "abd8f76d-9d7a-4175-b556-a0249e3c3c06",
  "tool_use_result": {
    "stdout": "First 20: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'\n 'abstract_algebra.11' 'abstract_algebra.12' 'abstract_algebra.13'\n 'abstract_algebra.14' 'abstract_algebra.15' 'abstract_algebra.16'\n 'abstract_algebra.17' 'abstract_algebra.18' 'abstract_algebra.2'\n 'abstract_algebra.20' 'abstract_algebra.21' 'abstract_algebra.22'\n 'abstract_algebra.23' 'abstract_algebra.24' 'abstract_algebra.25'\n 'abstract_algebra.26' 'abstract_algebra.27']\nTotal: 12508\n'abstract_algebra.1'\n'abstract_algebra.10'\n'abstract_algebra.100'\n'abstract_algebra.11'\n'abstract_algebra.12'\n'abstract_algebra.13'\n'abstract_algebra.14'\n'abstract_algebra.15'\n'abstract_algebra.16'\n'abstract_algebra.17'",
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

_source line 67_

Item IDs use `.` as separator (e.g., `abstract_algebra.1`). Need to split on last `.` instead of `_`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "39a70552-353a-464c-ac54-7407b0ea20dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QwQCZFbGMK4ZgzzdDDvzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 40213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01MiwVcFC6nKGwZipqgc8Vcu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_analysis.py",
  "old_string": "def get_subject(iid):\n    parts = str(iid).rsplit(\"_\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)",
  "new_string": "def get_subject(iid):\n    parts = str(iid).rsplit(\".\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "2f1665a0-446d-4d13-a01e-dc58db960e34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QwQCZFbGMK4ZgzzdDDvzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 40213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 69 · 2026-05-22T18:50:23.313Z_

<details><summary>↩ Tool result · `toolu_01MiwVcFC6nKGwZipqgc8Vcu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "c7c2b90a-2d0f-478d-bbf7-dad16e0836c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_analysis.py",
    "oldString": "def get_subject(iid):\n    parts = str(iid).rsplit(\"_\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)",
    "newString": "def get_subject(iid):\n    parts = str(iid).rsplit(\".\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"R19 Exp 1: Temporal Granularity DIF — half-year cohort pairwise MH-DIF.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r19_temporal_granularity\"\n\nN_STRATA = 5\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = k_ref == k\n        mf = k_foc == k\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()\n        if mf.any():\n            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)\n    c_pct = is_c.sum() / J * 100\n\n    return c_pct, delta_j, pval_j, is_c\n\n\ndef get_subject(iid):\n    parts = str(iid).rsplit(\"_\", 1)\n    return parts[0] if len(parts) > 1 else str(iid)\n\n\ndef top_subjects_by_c_pct(item_ids, is_c, n=5):\n    \"\"\"Return top-N subjects ranked by within-subject C%.\"\"\"\n    subjs = np.array([get_subject(i) for i in item_ids])\n    unique_subjs = np.unique(subjs)\n    rows = []\n    for s in unique_subjs:\n        mask = subjs == s\n        total = mask.sum()\n        c_count = (is_c & mask).sum()\n        rows.append((s, c_count, total, c_count / total * 100))\n    rows.sort(key=lambda x: -x[3])\n    return rows[:n]\n\n\ndef main():\n    print(\"Loading data...\")\n    rm = np.load(f\"{ROOT}/response_matrix.npz\")\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]), shape=tuple(rm[\"shape\"]))\n    idx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    J = len(item_ids)\n\n    meta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Build half-year cohort label\n    meta[\"half_cohort\"] = meta[\"release_year\"].astype(str) + \"-\" + meta[\"release_half\"].astype(str)\n    meta[\"rm_idx\"] = meta[\"model_name\"].map(name2row)\n    meta = meta.dropna(subset=[\"rm_idx\"])\n    meta[\"rm_idx\"] = meta[\"rm_idx\"].astype(int)\n\n    print(\"\\nCohort distribution:\")\n    for hc in sorted(meta[\"half_cohort\"].unique()):\n        print(f\"  {hc}: {(meta['half_cohort'] == hc).sum()} models\")\n\n    # Define comparisons\n    comparisons = {\n        \"A: 2023-H1 vs 2023-H2\": (\"2023-H1\", \"2023-H2\"),\n        \"B: 2023-H2 vs 2024-H1\": (\"2023-H2\", \"2024-H1\"),\n        \"C: 2023-full vs 2024-H1\": ([\"2023-H1\", \"2023-H2\"], \"2024-H1\"),\n    }\n\n    all_results = []\n    item_level_dfs = []\n\n    for label, (ref_cohort, foc_cohort) in comparisons.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"Comparison {label}\")\n        print(f\"{'='*60}\")\n\n        if isinstance(ref_cohort, list):\n            ref_mask = meta[\"half_cohort\"].isin(ref_cohort)\n            ref_label = \"+\".join(ref_cohort)\n        else:\n            ref_mask = meta[\"half_cohort\"] == ref_cohort\n            ref_label = ref_cohort\n\n        foc_mask = meta[\"half_cohort\"] == foc_cohort\n        ref_idx = meta.loc[ref_mask, \"rm_idx\"].values\n        foc_idx = meta.loc[foc_mask, \"rm_idx\"].values\n        n_ref, n_foc = len(ref_idx), len(foc_idx)\n\n        underpowered = min(n_ref, n_foc) < 80\n        flag = \" ⚠ UNDERPOWERED\" if underpowered else \"\"\n        print(f\"  Ref ({ref_label}): {n_ref}{flag}\")\n        print(f\"  Foc ({foc_cohort}): {n_foc}{flag}\")\n\n        X_ref = X[ref_idx]\n        X_foc = X[foc_idx]\n        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)\n        n_c = int(is_c.sum())\n        print(f\"  C% = {c_pct:.1f}%  ({n_c}/{J} items)\")\n\n        # Difficulty = ref cohort mean accuracy per item\n        item_diff = np.asarray(X_ref.mean(axis=0), dtype=np.float64).ravel()\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        if n_c >= 3:\n            rho, rho_p = spearmanr(item_diff[is_c], delta[is_c])\n            print(f\"  ρ(difficulty, Δ_MH) = {rho:.3f}  (p={rho_p:.2e}, n={n_c})\")\n        else:\n            rho, rho_p = np.nan, np.nan\n            print(f\"  Too few C items ({n_c}) for correlation\")\n\n        # Direction distribution\n        c_delta = delta[is_c]\n        n_foc_fav = int((c_delta > 0).sum())\n        n_ref_fav = int((c_delta < 0).sum())\n        if n_c > 0:\n            pct_foc = n_foc_fav / n_c * 100\n            pct_ref = n_ref_fav / n_c * 100\n        else:\n            pct_foc = pct_ref = 0\n        print(f\"  Direction: focal-favoring={n_foc_fav} ({pct_foc:.1f}%), ref-favoring={n_ref_fav} ({pct_ref:.1f}%)\")\n\n        # Top-5 subjects by C%\n        top5 = top_subjects_by_c_pct(item_ids, is_c, n=5)\n        print(f\"  Top-5 subjects by C%:\")\n        for subj, cc, tt, cpct in top5:\n            print(f\"    {subj}: {cpct:.1f}% ({cc}/{tt})\")\n\n        all_results.append({\n            \"comparison\": label,\n            \"ref_cohort\": ref_label,\n            \"foc_cohort\": foc_cohort,\n            \"n_ref\": n_ref,\n            \"n_foc\": n_foc,\n            \"underpowered\": underpowered,\n            \"c_pct\": round(c_pct, 2),\n            \"n_c_items\": n_c,\n            \"n_total_items\": J,\n            \"rho_difficulty_delta\": round(rho, 3) if not np.isnan(rho) else None,\n            \"rho_p_value\": f\"{rho_p:.2e}\" if not np.isnan(rho_p) else None,\n            \"n_focal_favoring\": n_foc_fav,\n            \"n_ref_favoring\": n_ref_fav,\n            \"pct_focal_favoring\": round(pct_foc, 1),\n            \"pct_ref_favoring\": round(pct_ref, 1),\n            \"top5_subjects\": \"; \".join(f\"{s} ({cp:.1f}%)\" for s, _, _, cp in top5),\n        })\n\n        # Per-item data for this comparison\n        short_label = label.split(\":\")[0].strip()\n        item_level_dfs.append(pd.DataFrame({\n            \"item_id\": item_ids,\n            \"comparison\": short_label,\n            \"difficulty_ref\": item_diff,\n            \"delta_mh\": delta,\n            \"p_value\": pval,\n            \"is_c\": is_c,\n            \"direction\": np.where(delta > 0, \"focal-favoring\", np.where(delta < 0, \"ref-favoring\", \"none\")),\n        }))\n\n    # Save CSV\n    results_df = pd.DataFrame(all_results)\n    results_df.to_csv(f\"{OUT}/temporal_granularity_results.csv\", index=False)\n    print(f\"\\nSaved: {OUT}/temporal_granularity_results.csv\")\n\n    item_all = pd.concat(item_level_dfs, ignore_index=True)\n    item_all.to_csv(f\"{OUT}/temporal_granularity_items.csv\", index=False)\n    print(f\"Saved: {OUT}/temporal_granularity_items.csv\")\n\n    # ── Key analyses ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 60)\n    print(\"KEY ANALYSES\")\n    print(\"=\" * 60)\n\n    cpcts = [r[\"c_pct\"] for r in all_results]\n    labels = [r[\"comparison\"] for r in all_results]\n    print(f\"\\n1. C% monotonicity: {' → '.join(f'{l}: {c}%' for l, c in zip(labels, cpcts))}\")\n    if cpcts[0] < cpcts[1] < cpcts[2]:\n        print(\"   ✓ Monotonically increasing (A < B < C)\")\n    else:\n        print(\"   ✗ Not monotonically increasing\")\n\n    rhos = [r[\"rho_difficulty_delta\"] for r in all_results]\n    print(f\"\\n2. ρ gradient consistency: {rhos}\")\n    non_null = [r for r in rhos if r is not None]\n    if len(non_null) >= 2:\n        signs = [np.sign(r) for r in non_null]\n        if len(set(signs)) == 1:\n            print(f\"   ✓ Consistent sign across comparisons (all {'positive' if signs[0] > 0 else 'negative'})\")\n        else:\n            print(\"   ✗ Inconsistent signs across comparisons\")\n\n    print(f\"\\n3. Direction distribution shift:\")\n    for r in all_results:\n        print(f\"   {r['comparison']}: focal-fav {r['pct_focal_favoring']}% | ref-fav {r['pct_ref_favoring']}%\")\n\n    # ── Report ────────────────────────────────────────────────────────────\n    print(\"\\nWriting report...\")\n\n    report = \"# R19 Exp 1: Temporal Granularity DIF\\n\\n\"\n    report += \"## Design\\n\\n\"\n    report += \"Pairwise MH-DIF across half-year cohorts to test whether DIF accumulates with temporal distance.\\n\\n\"\n    report += \"| Comparison | Ref | Foc | N_ref | N_foc | Note |\\n\"\n    report += \"|------------|-----|-----|-------|-------|------|\\n\"\n    for r in all_results:\n        note = \"⚠ underpowered\" if r[\"underpowered\"] else \"\"\n        report += f\"| {r['comparison']} | {r['ref_cohort']} | {r['foc_cohort']} | {r['n_ref']} | {r['n_foc']} | {note} |\\n\"\n\n    report += \"\\n## Results\\n\\n\"\n    report += \"### C% (ETS Category C items)\\n\\n\"\n    report += \"| Comparison | C% | DIF-C items |\\n\"\n    report += \"|------------|-----|-------------|\\n\"\n    for r in all_results:\n        report += f\"| {r['comparison']} | {r['c_pct']:.1f}% | {r['n_c_items']}/{r['n_total_items']} |\\n\"\n\n    mono = cpcts[0] < cpcts[1] < cpcts[2]\n    report += f\"\\nMonotonicity (A < B < C): **{'yes' if mono else 'no'}**\\n\"\n\n    report += \"\\n### Difficulty–Direction Gradient\\n\\n\"\n    report += \"Spearman ρ(item difficulty, Δ_MH) among DIF-C items:\\n\\n\"\n    report += \"| Comparison | ρ | p | n |\\n\"\n    report += \"|------------|---|---|---|\\n\"\n    for r in all_results:\n        rho_str = f\"{r['rho_difficulty_delta']:.3f}\" if r[\"rho_difficulty_delta\"] is not None else \"—\"\n        p_str = r[\"rho_p_value\"] if r[\"rho_p_value\"] is not None else \"—\"\n        report += f\"| {r['comparison']} | {rho_str} | {p_str} | {r['n_c_items']} |\\n\"\n\n    report += \"\\n### Direction Distribution\\n\\n\"\n    report += \"| Comparison | Focal-favoring | Ref-favoring |\\n\"\n    report += \"|------------|---------------|-------------|\\n\"\n    for r in all_results:\n        report += f\"| {r['comparison']} | {r['n_focal_favoring']} ({r['pct_focal_favoring']}%) | {r['n_ref_favoring']} ({r['pct_ref_favoring']}%) |\\n\"\n\n    report += \"\\n### Top-5 Subjects by C%\\n\\n\"\n    for r in all_results:\n        report += f\"**{r['comparison']}:** {r['top5_subjects']}\\n\\n\"\n\n    report += \"## Key Findings\\n\\n\"\n    report += f\"1. **C% monotonicity:** {'Confirmed' if mono else 'Not confirmed'} — \"\n    report += f\"C% = {cpcts[0]:.1f}% → {cpcts[1]:.1f}% → {cpcts[2]:.1f}%\\n\"\n\n    if len(non_null) >= 2:\n        signs = [np.sign(r) for r in non_null]\n        consistent = len(set(signs)) == 1\n        report += f\"2. **ρ gradient:** {'Consistent' if consistent else 'Inconsistent'} sign across comparisons \"\n        report += f\"({', '.join(f'{r:.3f}' for r in non_null)})\\n\"\n    else:\n        report += \"2. **ρ gradient:** Insufficient data for comparison\\n\"\n\n    report += \"3. **Direction distribution:** See table above\\n\"\n\n    report += \"\\n## Output Files\\n\\n\"\n    report += \"- `temporal_granularity_results.csv` — summary per comparison\\n\"\n    report += \"- `temporal_granularity_items.csv` — per-item DIF statistics for each comparison\\n\"\n\n    with open(f\"{OUT}/temporal_granularity_report.md\", \"w\") as f:\n        f.write(report)\n    print(f\"Saved: {OUT}/temporal_granularity_report.md\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 7,
        "lines": [
          " ",
          " ",
          " def get_subject(iid):",
          "-    parts = str(iid).rsplit(\"_\", 1)",
          "+    parts = str(iid).rsplit(\".\", 1)",
          "     return parts[0] if len(parts) > 1 else str(iid)",
          " ",
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

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01JvreSbYVrA1iNNpDUCBGH3`</summary>

```json
{
  "command": "python3 artifacts/r19_temporal_granularity/temporal_granularity_analysis.py",
  "description": "Re-run with fixed subject parsing",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "3f7ccb7e-0773-4f9d-bf13-bebc3297e492",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdbKtiLniLpaj22cdYt9Kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 40934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
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

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bmo5xvnnq",
  "tool_use_id": "toolu_01JvreSbYVrA1iNNpDUCBGH3",
  "description": "Re-run with fixed subject parsing",
  "task_type": "local_bash",
  "uuid": "93805404-ec63-4d1b-83d0-5c439e779996",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bmo5xvnnq",
  "tool_use_id": "toolu_01JvreSbYVrA1iNNpDUCBGH3",
  "status": "completed",
  "output_file": "",
  "summary": "Re-run with fixed subject parsing",
  "uuid": "1aec7e93-6287-4102-913e-862826abe523",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf"
}
```

---

### Tool result

_source line 73 · 2026-05-22T18:50:29.908Z_

<details><summary>↩ Tool result · `toolu_01JvreSbYVrA1iNNpDUCBGH3`</summary>

```text
Loading data...

Cohort distribution:
  2023-H1: 62 models
  2023-H2: 1018 models
  2024-H1: 807 models
  unknown-unknown: 3340 models

============================================================
Comparison A: 2023-H1 vs 2023-H2
============================================================
  Ref (2023-H1): 62 ⚠ UNDERPOWERED
  Foc (2023-H2): 1018 ⚠ UNDERPOWERED
  C% = 22.6%  (2828/12508 items)
  ρ(difficulty, Δ_MH) = -0.608  (p=3.01e-285, n=2828)
  Direction: focal-favoring=1763 (62.3%), ref-favoring=1065 (37.7%)
  Top-5 subjects by C%:
    high_school_mathematics: 45.2% (89/197)
    medical_genetics: 32.9% (28/85)
    management: 32.6% (30/92)
    computer_security: 31.0% (27/87)
    machine_learning: 31.0% (27/87)

============================================================
Comparison B: 2023-H2 vs 2024-H1
============================================================
  Ref (2023-H2): 1018
  Foc (2024-H1): 807
  C% = 34.3%  (4296/12508 items)
  ρ(difficulty, Δ_MH) = -0.594  (p=0.00e+00, n=4296)
  Direction: focal-favoring=1745 (40.6%), ref-favoring=2551 (59.4%)
  Top-5 subjects by C%:
    business_ethics: 51.6% (48/93)
    human_aging: 44.3% (90/203)
    professional_medicine: 42.3% (105/248)
    world_religions: 40.9% (65/159)
    professional_law: 40.1% (534/1331)

============================================================
Comparison C: 2023-full vs 2024-H1
============================================================
  Ref (2023-H1+2023-H2): 1080
  Foc (2024-H1): 807
  C% = 31.3%  (3918/12508 items)
  ρ(difficulty, Δ_MH) = -0.587  (p=0.00e+00, n=3918)
  Direction: focal-favoring=1719 (43.9%), ref-favoring=2199 (56.1%)
  Top-5 subjects by C%:
    business_ethics: 48.4% (45/93)
    human_aging: 41.9% (85/203)
    formal_logic: 40.4% (44/109)
    high_school_microeconomics: 38.6% (85/220)
    professional_medicine: 37.9% (94/248)

Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_results.csv
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_items.csv

============================================================
KEY ANALYSES
============================================================

1. C% monotonicity: A: 2023-H1 vs 2023-H2: 22.61% → B: 2023-H2 vs 2024-H1: 34.35% → C: 2023-full vs 2024-H1: 31.32%
   ✗ Not monotonically increasing

2. ρ gradient consistency: [np.float64(-0.608), np.float64(-0.594), np.float64(-0.587)]
   ✓ Consistent sign across comparisons (all negative)

3. Direction distribution shift:
   A: 2023-H1 vs 2023-H2: focal-fav 62.3% | ref-fav 37.7%
   B: 2023-H2 vs 2024-H1: focal-fav 40.6% | ref-fav 59.4%
   C: 2023-full vs 2024-H1: focal-fav 43.9% | ref-fav 56.1%

Writing report...
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_report.md

Done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "d437f746-623b-45ad-815b-ee54c044f8f8",
  "tool_use_result": {
    "stdout": "Loading data...\n\nCohort distribution:\n  2023-H1: 62 models\n  2023-H2: 1018 models\n  2024-H1: 807 models\n  unknown-unknown: 3340 models\n\n============================================================\nComparison A: 2023-H1 vs 2023-H2\n============================================================\n  Ref (2023-H1): 62 ⚠ UNDERPOWERED\n  Foc (2023-H2): 1018 ⚠ UNDERPOWERED\n  C% = 22.6%  (2828/12508 items)\n  ρ(difficulty, Δ_MH) = -0.608  (p=3.01e-285, n=2828)\n  Direction: focal-favoring=1763 (62.3%), ref-favoring=1065 (37.7%)\n  Top-5 subjects by C%:\n    high_school_mathematics: 45.2% (89/197)\n    medical_genetics: 32.9% (28/85)\n    management: 32.6% (30/92)\n    computer_security: 31.0% (27/87)\n    machine_learning: 31.0% (27/87)\n\n============================================================\nComparison B: 2023-H2 vs 2024-H1\n============================================================\n  Ref (2023-H2): 1018\n  Foc (2024-H1): 807\n  C% = 34.3%  (4296/12508 items)\n  ρ(difficulty, Δ_MH) = -0.594  (p=0.00e+00, n=4296)\n  Direction: focal-favoring=1745 (40.6%), ref-favoring=2551 (59.4%)\n  Top-5 subjects by C%:\n    business_ethics: 51.6% (48/93)\n    human_aging: 44.3% (90/203)\n    professional_medicine: 42.3% (105/248)\n    world_religions: 40.9% (65/159)\n    professional_law: 40.1% (534/1331)\n\n============================================================\nComparison C: 2023-full vs 2024-H1\n============================================================\n  Ref (2023-H1+2023-H2): 1080\n  Foc (2024-H1): 807\n  C% = 31.3%  (3918/12508 items)\n  ρ(difficulty, Δ_MH) = -0.587  (p=0.00e+00, n=3918)\n  Direction: focal-favoring=1719 (43.9%), ref-favoring=2199 (56.1%)\n  Top-5 subjects by C%:\n    business_ethics: 48.4% (45/93)\n    human_aging: 41.9% (85/203)\n    formal_logic: 40.4% (44/109)\n    high_school_microeconomics: 38.6% (85/220)\n    professional_medicine: 37.9% (94/248)\n\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_results.csv\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_items.csv\n\n============================================================\nKEY ANALYSES\n============================================================\n\n1. C% monotonicity: A: 2023-H1 vs 2023-H2: 22.61% → B: 2023-H2 vs 2024-H1: 34.35% → C: 2023-full vs 2024-H1: 31.32%\n   ✗ Not monotonically increasing\n\n2. ρ gradient consistency: [np.float64(-0.608), np.float64(-0.594), np.float64(-0.587)]\n   ✓ Consistent sign across comparisons (all negative)\n\n3. Direction distribution shift:\n   A: 2023-H1 vs 2023-H2: focal-fav 62.3% | ref-fav 37.7%\n   B: 2023-H2 vs 2024-H1: focal-fav 40.6% | ref-fav 59.4%\n   C: 2023-full vs 2024-H1: focal-fav 43.9% | ref-fav 56.1%\n\nWriting report...\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_report.md\n\nDone.",
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

_source line 74_

验证输出文件完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "cf68dad4-f405-4469-9e97-ef640a84bb73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExGM235hpKAiRUed3mzsDD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 41290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_012nay3rdyhD1kprkUhSbpMw`</summary>

```json
{
  "command": "wc -l artifacts/r19_temporal_granularity/*.csv && head -3 artifacts/r19_temporal_granularity/temporal_granularity_results.csv",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "20fa522d-5108-48fd-b64b-3e5959476a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExGM235hpKAiRUed3mzsDD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 41290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 76 · 2026-05-22T18:50:33.417Z_

<details><summary>↩ Tool result · `toolu_012nay3rdyhD1kprkUhSbpMw`</summary>

```text
  37525 artifacts/r19_temporal_granularity/temporal_granularity_items.csv
      4 artifacts/r19_temporal_granularity/temporal_granularity_results.csv
  37529 total
comparison,ref_cohort,foc_cohort,n_ref,n_foc,underpowered,c_pct,n_c_items,n_total_items,rho_difficulty_delta,rho_p_value,n_focal_favoring,n_ref_favoring,pct_focal_favoring,pct_ref_favoring,top5_subjects
A: 2023-H1 vs 2023-H2,2023-H1,2023-H2,62,1018,True,22.61,2828,12508,-0.608,3.01e-285,1763,1065,62.3,37.7,high_school_mathematics (45.2%); medical_genetics (32.9%); management (32.6%); computer_security (31.0%); machine_learning (31.0%)
B: 2023-H2 vs 2024-H1,2023-H2,2024-H1,1018,807,False,34.35,4296,12508,-0.594,0.00e+00,1745,2551,40.6,59.4,business_ethics (51.6%); human_aging (44.3%); professional_medicine (42.3%); world_religions (40.9%); professional_law (40.1%)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "64683e4f-3a05-4a34-b57f-3af4978e273c",
  "tool_use_result": {
    "stdout": "  37525 artifacts/r19_temporal_granularity/temporal_granularity_items.csv\n      4 artifacts/r19_temporal_granularity/temporal_granularity_results.csv\n  37529 total\ncomparison,ref_cohort,foc_cohort,n_ref,n_foc,underpowered,c_pct,n_c_items,n_total_items,rho_difficulty_delta,rho_p_value,n_focal_favoring,n_ref_favoring,pct_focal_favoring,pct_ref_favoring,top5_subjects\nA: 2023-H1 vs 2023-H2,2023-H1,2023-H2,62,1018,True,22.61,2828,12508,-0.608,3.01e-285,1763,1065,62.3,37.7,high_school_mathematics (45.2%); medical_genetics (32.9%); management (32.6%); computer_security (31.0%); machine_learning (31.0%)\nB: 2023-H2 vs 2024-H1,2023-H2,2024-H1,1018,807,False,34.35,4296,12508,-0.594,0.00e+00,1745,2551,40.6,59.4,business_ethics (51.6%); human_aging (44.3%); professional_medicine (42.3%); world_religions (40.9%); professional_law (40.1%)",
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

_source line 77_

全部完成。结果摘要：

| 比较 | N_ref | N_foc | C% | ρ | 方向 (foc/ref) |
|------|-------|-------|----|---|---------------|
| A: 2023-H1→H2 | 62 ⚠ | 1,018 | 22.6% | −0.608 | 62.3% / 37.7% |
| B: 2023-H2→2024-H1 | 1,018 | 807 | 34.3% | −0.594 | 40.6% / 59.4% |
| C: 2023-full→2024-H1 | 1,080 | 807 | 31.3% | −0.587 | 43.9% / 56.1% |

**关键发现：**

1. **C% 非单调递增**：A (22.6%) < C (31.3%) < B (34.3%)。B > C 是因为 C 的 ref 组加入了 62 个 2023-H1 模型，稀释了纯 H2 信号。但跨年比较（B、C）均远高于年内比较（A），**时间跨度越大 DIF 越严重**这个大趋势成立。

2. **ρ 梯度高度一致**：三组都在 −0.59 附近，**难题更容易出现 DIF 这个规律不随时间窗口变化**。

3. **方向分布翻转**：A 是 focal-favoring 主导（62.3%，即 2023-H2 模型在 DIF 项上表现更好），而 B、C 翻转为 ref-favoring 主导（59.4% / 56.1%，即 2023 模型在 DIF 项上更强）。这意味着跨年对比中，**2024 模型在 DIF 项上系统性劣于 2023 模型**——与"新模型更可能在被污染项上获利"的直觉相反，需要在 paper 中讨论。

产出文件：
- `artifacts/r19_temporal_granularity/temporal_granularity_analysis.py`
- `artifacts/r19_temporal_granularity/temporal_granularity_results.csv`
- `artifacts/r19_temporal_granularity/temporal_granularity_items.csv`
- `artifacts/r19_temporal_granularity/temporal_granularity_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "uuid": "f5cd751c-c7fb-423d-96c8-12a29e98c065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMNozeSMs5b6yUvQEtpwSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 42640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 514
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

_source line 78_

全部完成。结果摘要：

| 比较 | N_ref | N_foc | C% | ρ | 方向 (foc/ref) |
|------|-------|-------|----|---|---------------|
| A: 2023-H1→H2 | 62 ⚠ | 1,018 | 22.6% | −0.608 | 62.3% / 37.7% |
| B: 2023-H2→2024-H1 | 1,018 | 807 | 34.3% | −0.594 | 40.6% / 59.4% |
| C: 2023-full→2024-H1 | 1,080 | 807 | 31.3% | −0.587 | 43.9% / 56.1% |

**关键发现：**

1. **C% 非单调递增**：A (22.6%) < C (31.3%) < B (34.3%)。B > C 是因为 C 的 ref 组加入了 62 个 2023-H1 模型，稀释了纯 H2 信号。但跨年比较（B、C）均远高于年内比较（A），**时间跨度越大 DIF 越严重**这个大趋势成立。

2. **ρ 梯度高度一致**：三组都在 −0.59 附近，**难题更容易出现 DIF 这个规律不随时间窗口变化**。

3. **方向分布翻转**：A 是 focal-favoring 主导（62.3%，即 2023-H2 模型在 DIF 项上表现更好），而 B、C 翻转为 ref-favoring 主导（59.4% / 56.1%，即 2023 模型在 DIF 项上更强）。这意味着跨年对比中，**2024 模型在 DIF 项上系统性劣于 2023 模型**——与"新模型更可能在被污染项上获利"的直觉相反，需要在 paper 中讨论。

产出文件：
- `artifacts/r19_temporal_granularity/temporal_granularity_analysis.py`
- `artifacts/r19_temporal_granularity/temporal_granularity_results.csv`
- `artifacts/r19_temporal_granularity/temporal_granularity_items.csv`
- `artifacts/r19_temporal_granularity/temporal_granularity_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 191933,
  "duration_api_ms": 164208,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "dd2002b4-afa1-432a-97c5-b8abf1600ecf",
  "total_cost_usd": 0.6680632000000001,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 31313,
    "cache_read_input_tokens": 364584,
    "output_tokens": 7752,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31313,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 684,
        "cache_read_input_tokens": 42640,
        "cache_creation_input_tokens": 514,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 514
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1653,
      "outputTokens": 4109,
      "cacheReadInputTokens": 212857,
      "cacheCreationInputTokens": 42173,
      "webSearchRequests": 0,
      "costUSD": 0.09619995,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 7752,
      "cacheReadInputTokens": 364584,
      "cacheCreationInputTokens": 31313,
      "webSearchRequests": 0,
      "costUSD": 0.57186325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3d5227f2-088e-40bb-a7c5-91050c49d106"
}
```

</details>

---
