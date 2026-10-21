# fix d134 analysis rankbiserial

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_fix_d134-analysis-rankbiserial_20260518T150748.log`
- **Structured JSON:** [`608bff4ce5c69c95e7df.json`](../../sessions/60/608bff4ce5c69c95e7df.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
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
  "uuid": "5c0813ec-9487-464d-a4a4-b10a9c8dd6ab",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1779126600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "99cea7ea-e094-4230-8329-a46ba557edfa",
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down:
1. Read the local script
2. SSH to remote server and write it (with shebang fix)
3. Run it and report results

Let me start by reading the local script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "ae4721b4-fd25-4c6a-be36-330ce22ff80e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WZJfwiQwxHjLzSZoza3nZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15123
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — Read · `toolu_0124LDC2bvrLPotSQqjawpsA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "a3f88523-9287-4dd2-b4bb-bd63ce299e4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WZJfwiQwxHjLzSZoza3nZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15123
      },
      "output_tokens": 27,
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

_source line 6 · 2026-05-18T15:08:01.948Z_

<details><summary>↩ Tool result · `toolu_0124LDC2bvrLPotSQqjawpsA`</summary>

```text
1	#!/usr/bin/env python3
2	"""D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.
3	Reads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.
4	Computes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),
5	and BCa bootstrap CIs. Outputs appendix-ready markdown.
6	"""
7	
8	import argparse
9	import json
10	import re
11	import sys
12	from pathlib import Path
13	
14	import numpy as np
15	import pandas as pd
16	from scipy import stats
17	from scipy.special import betaln
18	
19	CONDITION_MAP = [
20	    ("d134_4b_isr", "ISR"),
21	    ("d134_4b_random", "RANDOM"),
22	    ("plan002_additive", "ISR"),
23	    ("plan018_additive_random", "RANDOM"),
24	    ("plan018_random", "RANDOM"),
25	]
26	
27	MODE_PREFIXES = {
28	    "d134_only": ["d134_4b"],
29	    "all": ["d134_4b", "plan002_additive_b01", "plan018_additive_random_b01", "plan018_random"],
30	}
31	
32	
33	def parse_args():
34	    p = argparse.ArgumentParser(description="D134 multi-seed analysis and statistical tests")
35	    p.add_argument("--data_dir", type=str, default="/root/autodl-tmp/outputs",
36	                   help="Directory containing experiment outputs")
37	    p.add_argument("--mode", type=str, default="d134_only", choices=list(MODE_PREFIXES),
38	                   help="d134_only = matched 5+5 design (default); all = include original seeds")
39	    p.add_argument("--prefix", type=str, default=None,
40	                   help="(Legacy) Single prefix filter; overrides mode/prefixes")
41	    p.add_argument("--prefixes", type=str, default=None,
42	                   help="Comma-separated prefixes; overrides --mode")
43	    p.add_argument("--output", type=str, default=None,
44	                   help="Write markdown summary to this file")
45	    p.add_argument("--n_perm", type=int, default=10000,
46	                   help="Number of permutations for permutation test")
47	    p.add_argument("--n_boot", type=int, default=10000,
48	                   help="Number of bootstrap resamples for BCa CI")
49	    p.add_argument("--seed", type=int, default=42,
50	                   help="Random seed for permutation/bootstrap")
51	    return p.parse_args()
52	
53	
54	# --- Data loading ---
55	
56	def match_condition(name: str) -> str | None:
57	    best_prefix = ""
58	    best_cond = None
59	    for prefix, cond in CONDITION_MAP:
60	        if name.startswith(prefix) and len(prefix) > len(best_prefix):
61	            best_prefix = prefix
62	            best_cond = cond
63	    return best_cond
64	
65	
66	def extract_seed(name: str) -> int | None:
67	    m = re.search(r'_s(\d+)', name)
68	    return int(m.group(1)) if m else None
69	
70	
71	def load_eval_results(path: Path) -> dict | None:
72	    if not path.exists():
73	        return None
74	    with open(path) as f:
75	        data = json.load(f)
76	    if "eval_results" in data:
77	        return data["eval_results"]
78	    return data
79	
80	
81	def load_taxonomy_unified(path: Path) -> dict | None:
82	    with open(path) as f:
83	        raw = json.load(f)
84	    t = raw.get("taxonomy", {})
85	    proved = t.get("proved", 0)
86	    if proved == 0:
87	        return None
88	    h7 = t.get("H7", 0)
89	    h1 = t.get("H1_exact", 0)
90	    h8 = t.get("H8", 0)
91	    genuine = t.get("genuine", 0)
92	    return {
93	        "n_total": 100, "n_proved": proved,
94	        "h7_total_count": h7, "h7_total_rate": h7 / proved,
95	        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
96	        "genuine_count": genuine, "genuine_rate": genuine / proved,
97	        "content_independent_count": 0,
98	    }
99	
100	
101	def load_taxonomy_verification(path: Path) -> dict | None:
102	    with open(path) as f:
103	        raw = json.load(f)
104	    proved = raw.get("proved", 0)
105	    if proved == 0:
106	        return None
107	    tax = raw.get("taxonomy", {})
108	    h7 = tax.get("h7", {}).get("count", 0)
109	    h1 = tax.get("h1_exact", {}).get("count", 0)
110	    h8 = tax.get("h8", {}).get("count", 0)
111	    genuine = tax.get("genuine", {}).get("count", 0)
112	    return {
113	        "n_total": raw.get("total", 100), "n_proved": proved,
114	        "h7_total_count": h7, "h7_total_rate": h7 / proved,
115	        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
116	        "genuine_count": genuine, "genuine_rate": genuine / proved,
117	        "content_independent_count": 0,
118	    }
119	
120	
121	def discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:
122	    runs = []
123	    seen = set()
124	    for entry in sorted(data_dir.iterdir()):
125	        name = entry.name
126	        if not any(name.startswith(p) for p in prefixes):
127	            continue
128	        cond = match_condition(name)
129	        seed_val = extract_seed(name)
130	        if cond is None or seed_val is None:
131	            continue
132	        key = (cond, seed_val)
133	        if key in seen:
134	            continue
135	        data = None
136	        if entry.is_dir():
137	            for fname in ["classify.json", "taxonomy.json"]:
138	                data = load_eval_results(entry / fname)
139	                if data is not None:
140	                    break
141	            if data is None:
142	                continue
143	        elif entry.is_file():
144	            if name.endswith("_taxonomy_unified.json"):
145	                data = load_taxonomy_unified(entry)
146	            elif name.endswith("_taxonomy_verification.json"):
147	                data = load_taxonomy_verification(entry)
148	            if data is None:
149	                continue
150	        else:
151	            continue
152	        seen.add(key)
153	        runs.append({"dir_name": name, "seed": seed_val, "condition": cond, "data": data})
154	    return runs
155	
156	
157	def compute_row(run: dict) -> dict:
158	    d = run["data"]
159	    n_proved = d.get("n_proved", 0)
160	    n_total = d.get("n_total", 100)
161	    h7 = d.get("h7_total_count", 0)
162	    h7_rate = d.get("h7_total_rate", h7 / n_proved if n_proved > 0 else 0.0)
163	    h1 = d.get("h1_strict_count", 0)
164	    h8 = d.get("h8_conjunction_collapse_count", 0)
165	    genuine = d.get("genuine_count", 0)
166	    genuine_rate = d.get("genuine_rate", genuine / n_proved if n_proved > 0 else 0.0)
167	    ci = d.get("content_independent_count", 0)
168	    snh = max(genuine - ci, 0)
169	    snh_rate = snh / n_proved if n_proved > 0 else 0.0
170	    return {
171	        "seed": run["seed"], "condition": run["condition"], "n_total": n_total,
172	        "PR": n_proved, "H7_count": h7, "H7_rate": h7_rate,
173	        "H1_count": h1, "H8_count": h8,
174	        "genuine_count": genuine, "genuine_rate": genuine_rate,
175	        "CI_count": ci, "SNH_count": snh, "SNH_rate": snh_rate,
176	    }
177	
178	
179	def build_table(runs: list[dict]) -> pd.DataFrame:
180	    rows = [compute_row(r) for r in runs]
181	    df = pd.DataFrame(rows)
182	    df = df.sort_values(["condition", "seed"]).reset_index(drop=True)
183	    return df
184	
185	
186	# --- Statistical tests ---
187	
188	def fisher_h7_domination(df: pd.DataFrame) -> dict:
189	    results = {}
190	    for cond in ["ISR", "RANDOM"]:
191	        sub = df[df["condition"] == cond]
192	        results[cond] = {
193	            "n": len(sub),
194	            "h7_dom": int((sub["H7_rate"] >= 0.5).sum()),
195	            "not_h7_dom": int((sub["H7_rate"] < 0.5).sum()),
196	        }
197	    table = np.array([
198	        [results["ISR"]["h7_dom"], results["ISR"]["not_h7_dom"]],
199	        [results["RANDOM"]["h7_dom"], results["RANDOM"]["not_h7_dom"]],
200	    ])
201	    odds_ratio, p_value = stats.fisher_exact(table, alternative="greater")
202	
203	    # 95% exact CI via scipy.stats.contingency
204	    or_ci_lo, or_ci_hi = np.nan, np.nan
205	    try:
206	        ct = stats.contingency.odds_ratio(table)
207	        ci = ct.confidence_interval(confidence_level=0.95)
208	        or_ci_lo, or_ci_hi = ci.low, ci.high
209	    except Exception:
210	        pass
211	
212	    return {
213	        "table": table.tolist(),
214	        "ISR": results["ISR"],
215	        "RANDOM": results["RANDOM"],
216	        "odds_ratio": odds_ratio,
217	        "or_ci_lo": or_ci_lo,
218	        "or_ci_hi": or_ci_hi,
219	        "p_value": p_value,
220	    }
221	
222	
223	def permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,
224	                              rng_seed: int = 42) -> dict:
225	    isr = df[df["condition"] == "ISR"]["genuine_rate"].values
226	    rand = df[df["condition"] == "RANDOM"]["genuine_rate"].values
227	    observed = isr.mean() - rand.mean()
228	    pooled = np.concatenate([isr, rand])
229	    n_isr = len(isr)
230	    rng = np.random.default_rng(rng_seed)
231	    count = 0
232	    for _ in range(n_perm):
233	        perm = rng.permutation(pooled)
234	        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:
235	            count += 1
236	    return {
237	        "observed_diff": float(observed),
238	        "p_value": count / n_perm,
239	        "n_perm": n_perm,
240	        "isr_mean": float(isr.mean()),
241	        "random_mean": float(rand.mean()),
242	    }
243	
244	
245	def mannwhitney_h7(df: pd.DataFrame) -> dict:
246	    isr = df[df["condition"] == "ISR"]["H7_rate"].values
247	    rand = df[df["condition"] == "RANDOM"]["H7_rate"].values
248	    n1, n2 = len(isr), len(rand)
249	    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative="greater")
250	    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan
251	    return {
252	        "U": float(u_stat),
253	        "p_value": float(p_value),
254	        "r_rank_biserial": float(r_rb),
255	        "isr_median": float(np.median(isr)),
256	        "random_median": float(np.median(rand)),
257	    }
258	
259	
260	def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,
261	                      rng_seed: int = 42) -> dict:
262	    """BCa 95% CI for per-condition means of a metric."""
263	    result = {}
264	    for cond in ["ISR", "RANDOM"]:
265	        vals = df[df["condition"] == cond][metric].values
266	        if len(vals) < 2:
267	            result[cond] = {"mean": float(vals.mean()) if len(vals) else np.nan,
268	                            "ci_lo": np.nan, "ci_hi": np.nan}
269	            continue
270	        res = stats.bootstrap(
271	            (vals,), np.mean, n_resamples=n_boot,
272	            confidence_level=0.95, method="BCa",
273	            random_state=np.random.default_rng(rng_seed),
274	        )
275	        result[cond] = {
276	            "mean": float(vals.mean()),
277	            "ci_lo": float(res.confidence_interval.low),
278	            "ci_hi": float(res.confidence_interval.high),
279	        }
280	    return result
281	
282	
283	def bayes_factor_h7_domination(df: pd.DataFrame) -> dict:
284	    """BF10 for H7-domination rate difference (beta-binomial conjugate).
285	    H0: ISR and Random share same domination rate.
286	    H1: independent rates. Prior: Beta(1,1) on each.
287	    """
288	    isr_sub = df[df["condition"] == "ISR"]
289	    rand_sub = df[df["condition"] == "RANDOM"]
290	    k_isr = int((isr_sub["H7_rate"] >= 0.5).sum())
291	    n_isr = len(isr_sub)
292	    k_rand = int((rand_sub["H7_rate"] >= 0.5).sum())
293	    n_rand = len(rand_sub)
294	    k_total = k_isr + k_rand
295	    n_total = n_isr + n_rand
296	
297	    # log marginal under H0 (shared rate)
298	    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)
299	    # log marginal under H1 (independent rates)
300	    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)
301	                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))
302	    log_bf10 = log_m_h1 - log_m_h0
303	    bf10 = float(np.exp(log_bf10))
304	
305	    return {
306	        "k_isr": k_isr, "n_isr": n_isr,
307	        "k_rand": k_rand, "n_rand": n_rand,
308	        "bf10": bf10,
309	        "log_bf10": float(log_bf10),
310	        "interpretation": _interpret_bf(bf10),
311	    }
312	
313	
314	def _interpret_bf(bf: float) -> str:
315	    if bf > 100:
316	        return "extreme evidence for H1"
317	    if bf > 30:
318	        return "very strong evidence for H1"
319	    if bf > 10:
320	        return "strong evidence for H1"
321	    if bf > 3:
322	        return "moderate evidence for H1"
323	    if bf > 1:
324	        return "anecdotal evidence for H1"
325	    if bf > 1/3:
326	        return "anecdotal evidence (inconclusive)"
327	    if bf > 1/10:
328	        return "moderate evidence for H0"
329	    return "strong evidence for H0"
330	
331	
332	def condition_stats(df: pd.DataFrame) -> pd.DataFrame:
333	    metrics = ["PR", "H7_rate", "genuine_rate", "SNH_rate"]
334	    rows = []
335	    for cond in ["ISR", "RANDOM"]:
336	        sub = df[df["condition"] == cond]
337	        row = {"condition": cond, "n_seeds": len(sub)}
338	        for m in metrics:
339	            vals = sub[m].values
340	            row[f"{m}_mean"] = vals.mean()
341	            row[f"{m}_std"] = vals.std(ddof=1) if len(vals) > 1 else 0.0
342	        rows.append(row)
343	    return pd.DataFrame(rows)
344	
345	
346	# --- Formatting ---
347	
348	def fmt_pct(val: float) -> str:
349	    return f"{val*100:.1f}\\%"
350	
351	def fmt_or(val: float) -> str:
352	    return "$\\infty$" if np.isinf(val) else f"{val:.2f}"
353	
354	def fmt_ci(lo: float, hi: float) -> str:
355	    lo_s = f"{lo:.2f}" if not np.isnan(lo) else "0"
356	    hi_s = "$\\infty$" if np.isinf(hi) or np.isnan(hi) else f"{hi:.2f}"
357	    return f"[{lo_s}, {hi_s}]"
358	
359	def fmt_p(p: float) -> str:
360	    if p < 0.001:
361	        return "$<$0.001"
362	    return f"{p:.3f}"
363	
364	def fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:
365	    if pct:
366	        return f"{mean*100:.1f} $\\pm$ {std*100:.1f}\\%"
367	    return f"{mean:.1f} $\\pm$ {std:.1f}"
368	
369	def fmt_bca(bca: dict, pct: bool = False) -> str:
370	    m = bca["mean"]
371	    lo, hi = bca["ci_lo"], bca["ci_hi"]
372	    if pct:
373	        return f"{m*100:.1f}\\% [{lo*100:.1f}, {hi*100:.1f}]"
374	    return f"{m:.1f} [{lo:.1f}, {hi:.1f}]"
375	
376	
377	# --- Console output ---
378	
379	def print_per_seed_table(df: pd.DataFrame):
380	    print("\n" + "=" * 90)
381	    print("  PER-SEED RESULTS")
382	    print("=" * 90)
383	    cols = ["condition", "seed", "PR", "H7_count", "H7_rate", "H1_count",
384	            "H8_count", "genuine_count", "genuine_rate", "CI_count", "SNH_count", "SNH_rate"]
385	    fmt = df[cols].copy()
386	    for c in ["H7_rate", "genuine_rate", "SNH_rate"]:
387	        fmt[c] = fmt[c].apply(lambda v: f"{v*100:.1f}%")
388	    print(fmt.to_string(index=False))
389	
390	
391	def print_condition_stats(cond_df: pd.DataFrame):
392	    print("\n" + "=" * 90)
393	    print("  CONDITION-LEVEL STATISTICS (mean +/- SD)")
394	    print("=" * 90)
395	    for _, row in cond_df.iterrows():
396	        n = int(row['n_seeds'])
397	        print(f"\n  {row['condition']} (n={n} seeds):")
398	        print(f"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}")
399	        print(f"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%")
400	        print(f"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%")
401	        print(f"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%")
402	
403	
404	def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):
405	    print("\n" + "=" * 90)
406	    print("  STATISTICAL TESTS")
407	    print("=" * 90)
408	
409	    print("\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)")
410	    print(f"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds")
411	    print(f"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds")
412	    print(f"     Contingency: {fisher['table']}")
413	    or_str = "inf" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.4f}"
414	    print(f"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]"
415	          if not np.isnan(fisher['or_ci_lo']) else f"     OR = {or_str}, 95% CI = N/A")
416	    print(f"     p-value (one-sided, greater): {fisher['p_value']:.4f}")
417	
418	    print(f"\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})")
419	    print(f"     ISR mean:    {perm['isr_mean']*100:.2f}%")
420	    print(f"     RANDOM mean: {perm['random_mean']*100:.2f}%")
421	    print(f"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}")
422	
423	    print(f"\n  3. H7 Rate Mann-Whitney U Test")
424	    print(f"     ISR median:    {mw['isr_median']*100:.1f}%")
425	    print(f"     RANDOM median: {mw['random_median']*100:.1f}%")
426	    print(f"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}")
427	    print(f"     Rank-biserial r = {mw['r_rank_biserial']:.4f}")
428	
429	    print(f"\n  4. Bayes Factor (H7 Domination, Beta-Binomial)")
430	    print(f"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated")
431	    print(f"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated")
432	    print(f"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})")
433	
434	    print(f"\n  5. BCa Bootstrap 95% CI (n_boot resamples)")
435	    for label, bca in [("H7 rate", bca_h7), ("Genuine rate", bca_gen)]:
436	        print(f"     {label}:")
437	        for cond in ["ISR", "RANDOM"]:
438	            b = bca[cond]
439	            print(f"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]"
440	                  if not np.isnan(b['ci_lo']) else f"       {cond}: {b['mean']*100:.1f}% [N/A]")
441	
442	
443	# --- Markdown generation (appendix-ready) ---
444	
445	def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,
446	                      fisher: dict, perm: dict, mw: dict,
447	                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:
448	    L = []
449	    L.append("## D134: ISR vs Random Statistical Analysis\n")
450	
451	    # Per-seed table
452	    L.append("### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\n")
453	    L.append("| Condition | Seed | PR | H7 | H7\\% | H1 | H8 | Genuine | Gen\\% | CI | S-NH | S-NH\\% |")
454	    L.append("|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|")
455	    for _, r in df.iterrows():
456	        L.append(
457	            f"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | "
458	            f"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | "
459	            f"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | "
460	            f"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |"
461	        )
462	
463	    # Condition summary with BCa CI
464	    L.append("\n### Table A2: Condition-Level Summary\n")
465	    L.append("| Condition | $n$ | PR (mean$\\pm$SD) | H7\\% (mean$\\pm$SD) | H7\\% BCa 95\\% CI | Gen\\% (mean$\\pm$SD) | Gen\\% BCa 95\\% CI |")
466	    L.append("|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|")
467	    for _, r in cond_df.iterrows():
468	        cond = r["condition"]
469	        h7_bca = bca_h7.get(cond, {})
470	        gen_bca = bca_gen.get(cond, {})
471	        h7_ci = f"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else "N/A"
472	        gen_ci = f"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else "N/A"
473	        L.append(
474	            f"| {cond} | {int(r['n_seeds'])} | "
475	            f"{r['PR_mean']:.1f}$\\pm${r['PR_std']:.1f} | "
476	            f"{r['H7_rate_mean']*100:.1f}$\\pm${r['H7_rate_std']*100:.1f} | "
477	            f"{h7_ci} | "
478	            f"{r['genuine_rate_mean']*100:.1f}$\\pm${r['genuine_rate_std']*100:.1f} | "
479	            f"{gen_ci} |"
480	        )
481	
482	    # Statistical tests
483	    if fisher and perm and mw and bf:
484	        L.append("\n### Statistical Tests\n")
485	
486	        # Fisher
487	        or_str = "$\\infty$" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.2f}"
488	        ci_lo = f"{fisher['or_ci_lo']:.2f}" if not np.isnan(fisher['or_ci_lo']) else "0"
489	        ci_hi = "$\\infty$" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f"{fisher['or_ci_hi']:.2f}"
490	        L.append("**1. H7 Domination Fisher Exact Test** (threshold: H7$\\geq$50\\% of proved)")
491	        L.append(f"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; "
492	                 f"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}")
493	        L.append(f"- OR = {or_str}, 95\\% exact CI = [{ci_lo}, {ci_hi}], "
494	                 f"$p$ = {fmt_p(fisher['p_value'])}")
495	        L.append("")
496	
497	        # Permutation
498	        L.append(f"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)")
499	        L.append(f"- ISR mean: {perm['isr_mean']*100:.2f}\\%, Random mean: {perm['random_mean']*100:.2f}\\%")
500	        L.append(f"- $\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}")
501	        L.append("")
502	
503	        # Mann-Whitney
504	        L.append("**3. H7 Rate Mann-Whitney $U$ Test**")
505	        L.append(f"- ISR median: {mw['isr_median']*100:.1f}\\%, Random median: {mw['random_median']*100:.1f}\\%")
506	        L.append(f"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, "
507	                 f"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}")
508	        L.append("")
509	
510	        # Bayes Factor
511	        L.append("**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))")
512	        L.append(f"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})")
513	        L.append(f"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, "
514	                 f"Random: {bf['k_rand']}/{bf['n_rand']}")
515	
516	    return "\n".join(L) + "\n"
517	
518	
519	# --- Main ---
520	
521	def main():
522	    args = parse_args()
523	    data_dir = Path(args.data_dir)
524	
525	    if not data_dir.exists():
526	        print(f"ERROR: data directory {data_dir} does not exist", file=sys.stderr)
527	        sys.exit(1)
528	
529	    if args.prefix:
530	        prefixes = [args.prefix]
531	    elif args.prefixes:
532	        prefixes = [p.strip() for p in args.prefixes.split(",")]
533	    else:
534	        prefixes = MODE_PREFIXES[args.mode]
535	    print(f"Mode: {args.mode} | Prefixes: {prefixes}")
536	
537	    runs = discover_runs(data_dir, prefixes)
538	    if not runs:
539	        print(f"ERROR: no runs found in {data_dir} with prefixes {prefixes}", file=sys.stderr)
540	        sys.exit(1)
541	
542	    isr_count = sum(1 for r in runs if r["condition"] == "ISR")
543	    rand_count = sum(1 for r in runs if r["condition"] == "RANDOM")
544	    print(f"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM")
545	    for r in runs:
546	        print(f"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}")
547	
548	    df = build_table(runs)
549	    print_per_seed_table(df)
550	
551	    cond_df = condition_stats(df)
552	    print_condition_stats(cond_df)
553	
554	    if isr_count < 2 or rand_count < 2:
555	        print("\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.",
556	              file=sys.stderr)
557	        bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
558	        bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
559	        if args.output:
560	            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)
561	            Path(args.output).write_text(md)
562	            print(f"\nMarkdown written to {args.output}")
563	        return
564	
565	    fisher = fisher_h7_domination(df)
566	    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)
567	    mw = mannwhitney_h7(df)
568	    bf = bayes_factor_h7_domination(df)
569	    bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
570	    bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
571	
572	    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)
573	
574	    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)
575	    print("\n" + "=" * 90)
576	    print("  MARKDOWN OUTPUT (appendix-ready)")
577	    print("=" * 90)
578	    print(md)
579	
580	    if args.output:
581	        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
582	        Path(args.output).write_text(md)
583	        print(f"Markdown written to {args.output}")
584	
585	
586	if __name__ == "__main__":
587	    main()
588	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "ecd7c0b1-9f25-4f8d-b015-0f7bab4e355e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 588,
      "startLine": 1,
      "totalLines": 588
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I need to modify the shebang and write it to the remote server, then run the dry run. Let me first prepare the script content with the updated shebang, then use SSH to write and execute.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "2bdb4962-d2e0-4817-8971-7122facd4209",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhFtJr5jGbXqDmSdWhkz1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10032,
      "cache_read_input_tokens": 26964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10032
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015MrZWwoWuGqrvCMUig7bbp`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "8e874092-837f-4491-9706-2bfcf310992e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhFtJr5jGbXqDmSdWhkz1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10032,
      "cache_read_input_tokens": 26964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10032
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

_source line 9 · 2026-05-18T15:08:11.328Z_

<details><summary>↩ Tool result · `toolu_015MrZWwoWuGqrvCMUig7bbp`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "626e8317-a030-4f58-9b99-ebf1fbdf5c4f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
I need to write the script to the remote server with the shebang changed to `#!/root/miniconda3/bin/python`, then run the dry run. Let me use a heredoc approach via ssh_execute to write the file.

The script is quite long. Let me use a base64 approach or a Python-based write to avoid shell escaping issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "14d0b806-643d-4b26-a685-e5af02b3868a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4Sj1D7SuH7crxS6DCxUg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 36996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 21,
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

_source line 11_

Writing the script to the remote server and running the dry run.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "c53a2765-b2a6-4975-88c1-02fbc1baa9e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4Sj1D7SuH7crxS6DCxUg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 36996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 21,
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JaVtN6Hp14ZDQPUzz7SoTd`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "cat > /root/solver-trace-ablation/scripts/d134_analysis.py << 'HEREDOC_EOF'\n#!/root/miniconda3/bin/python\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC_EOF\necho \"EXIT_CODE=$?\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "b54fe895-9e55-4c2e-930a-449f91260a96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4Sj1D7SuH7crxS6DCxUg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 36996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 21,
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

_source line 13 · 2026-05-18T15:10:11.922Z_

<details><summary>↩ Tool result · `toolu_01JaVtN6Hp14ZDQPUzz7SoTd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "5f4e63cb-0a9e-4c93-ac73-c1ed5042f5a0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"EXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.21}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

文件已写入。运行 dry run。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "fc181329-b449-4771-8b0a-eb548e88ff3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLhShXM9XJpvDNe9C1ErH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8936,
      "cache_read_input_tokens": 37386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8936
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SgZBUzQbCKbXMh8mkYyKZY`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "cd /root/solver-trace-ablation && /root/miniconda3/bin/python scripts/d134_analysis.py --mode all --data_dir /root/autodl-tmp/outputs --n_boot 1000 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "6042b622-97be-4d1e-bd82-19813d0e6c86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLhShXM9XJpvDNe9C1ErH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8936,
      "cache_read_input_tokens": 37386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8936
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

_source line 16 · 2026-05-18T15:10:19.151Z_

<details><summary>↩ Tool result · `toolu_01SgZBUzQbCKbXMh8mkYyKZY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/scipy/stats/_resampling.py:155: RuntimeWarning: invalid value encountered in scalar divide\\n  a_hat = 1/6 * sum(nums) / sum(dens)**(3/2)\\n/root/miniconda3/lib/python3.12/site-packages/scipy/_lib/_util.py:365: DegenerateDataWarning: The BCa confidence interval cannot be calculated. This problem is known to occur when the distribution is degenerate or the statistic is np.min.\\n  return fun(*args, **kwargs)\\nMode: all | Prefixes: ['d134_4b', 'plan002_additive_b01', 'plan018_additive_random_b01', 'plan018_random']\\nFound 7 runs: 5 ISR, 2 RANDOM\\n  ISR    s47 <- d134_4b_isr_b01_s47\\n  ISR    s48 <- d134_4b_isr_b01_s48\\n  ISR    s49 <- d134_4b_isr_b01_s49\\n  ISR    s50 <- d134_4b_isr_b01_s50\\n  ISR    s42 <- plan002_additive_b01_s42_1000_taxonomy_unified.json\\n  RANDOM s44 <- plan018_additive_random_b01_s44_r2\\n  RANDOM s42 <- plan018_random_s42_taxonomy_verification.json\\n\\n==========================================================================================\\n  PER-SEED RESULTS\\n==========================================================================================\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate\\n      ISR    42  90        87   96.7%         0         2              1         1.1%         0          1     1.1%\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%\\n      ISR    50  98        84   85.7%         0         8              6         6.1%         2          4     4.1%\\n   RANDOM    42  79         0    0.0%        56         3             12        15.2%         0         12    15.2%\\n   RANDOM    44  89         0    0.0%        73        16              6         6.7%        18          0     0.0%\\n\\n==========================================================================================\\n  CONDITION-LEVEL STATISTICS (mean +/- SD)\\n==========================================================================================\\n\\n  ISR (n=5 seeds):\\n    PR:           87.4 +/- 13.0\\n    H7 rate:      90.6 +/- 7.2%\\n    Genuine rate: 2.3 +/- 2.4%\\n    S-NH rate:    1.3 +/- 1.7%\\n\\n  RANDOM (n=2 seeds):\\n    PR:           84.0 +/- 7.1\\n    H7 rate:      0.0 +/- 0.0%\\n    Genuine rate: 11.0 +/- 6.0%\\n    S-NH rate:    7.6 +/- 10.7%\\n\\n==========================================================================================\\n  STATISTICAL TESTS\\n==========================================================================================\\n\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\\n     ISR:    5 dominated / 5 seeds\\n     RANDOM: 0 dominated / 2 seeds\\n     Contingency: [[5, 0], [0, 2]]\\n     OR = inf, 95% CI = [0.6506, inf]\\n     p-value (one-sided, greater): 0.0476\\n\\n  2. Genuine Rate Permutation Test (n_perm=10000)\\n     ISR mean:    2.30%\\n     RANDOM mean: 10.96%\\n     Diff: -8.67 pp, p = 1.0000\\n\\n  3. H7 Rate Mann-Whitney U Test\\n     ISR median:    85.7%\\n     RANDOM median: 0.0%\\n     U = 10.0, p = 0.0393\\n     Rank-biserial r = 1.0000\\n\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\\n     ISR:    5/5 dominated\\n     RANDOM: 0/2 dominated\\n     BF10 = 9.3333 (moderate evidence for H1)\\n\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\\n     H7 rate:\\n       ISR: 90.6% [85.3, 96.4]\\n       RANDOM: 0.0% [N/A]\\n     Genuine rate:\\n       ISR: 2.3% [0.9, 5.1]\\n       RANDOM: 11.0% [6.7, 15.2]\\n\\n==========================================================================================\\n  MARKDOWN OUTPUT (appendix-ready)\\n==========================================================================================\\n## D134: ISR vs Random Statistical Analysis\\n\\n### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\\n| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\\n|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\\n| ISR | 42 | 90 | 87 | 96.7 | 0 | 2 | 1 | 1.1 | 0 | 1 | 1.1 |\\n| ISR | 47 | 97 | 83 | 85.6 | 1 | 10 | 3 | 3.1 | 8 | 0 | 0.0 |\\n| ISR | 48 | 66 | 66 | 100.0 | 0 | 0 | 0 | 0.0 | 2 | 0 | 0.0 |\\n| ISR | 49 | 86 | 73 | 84.9 | 6 | 6 | 1 | 1.2 | 0 | 1 | 1.2 |\\n| ISR | 50 | 98 | 84 | 85.7 | 0 | 8 | 6 | 6.1 | 2 | 4 | 4.1 |\\n| RANDOM | 42 | 79 | 0 | 0.0 | 56 | 3 | 12 | 15.2 | 0 | 12 | 15.2 |\\n| RANDOM | 44 | 89 | 0 | 0.0 | 73 | 16 | 6 | 6.7 | 18 | 0 | 0.0 |\\n\\n### Table A2: Condition-Level Summary\\n\\n| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\\n|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\\n| ISR | 5 | 87.4$\\\\pm$13.0 | 90.6$\\\\pm$7.2 | [85.3, 96.4] | 2.3$\\\\pm$2.4 | [0.9, 5.1] |\\n| RANDOM | 2 | 84.0$\\\\pm$7.1 | 0.0$\\\\pm$0.0 | N/A | 11.0$\\\\pm$6.0 | [6.7, 15.2] |\\n\\n### Statistical Tests\\n\\n**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\\n- ISR: 5/5 seeds H7-dominated; Random: 0/2\\n- OR = $\\\\infty$, 95\\\\% exact CI = [0.65, $\\\\infty$], $p$ = 0.048\\n\\n**2. Genuine Rate Permutation Test** ($n$ = 10,000 permutations)\\n- ISR mean: 2.30\\\\%, Random mean: 10.96\\\\%\\n- $\\\\Delta$ = -8.67 pp, $p$ = 1.000\\n\\n**3. H7 Rate Mann-Whitney $U$ Test**\\n- ISR median: 85.7\\\\%, Random median: 0.0\\\\%\\n- $U$ = 10.0, $p$ = 0.039, rank-biserial $r$ = 1.000\\n\\n**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\n- $BF_{10}$ = 9.33 (moderate evidence for H1)\\n- ISR: 5/5 H7-dominated, Random: 0/2\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "6808599c-e0a2-4c78-923b-173ae6a86173",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/lib/python3.12/site-packages/scipy/stats/_resampling.py:155: RuntimeWarning: invalid value encountered in scalar divide\\\\n  a_hat = 1/6 * sum(nums) / sum(dens)**(3/2)\\\\n/root/miniconda3/lib/python3.12/site-packages/scipy/_lib/_util.py:365: DegenerateDataWarning: The BCa confidence interval cannot be calculated. This problem is known to occur when the distribution is degenerate or the statistic is np.min.\\\\n  return fun(*args, **kwargs)\\\\nMode: all | Prefixes: ['d134_4b', 'plan002_additive_b01', 'plan018_additive_random_b01', 'plan018_random']\\\\nFound 7 runs: 5 ISR, 2 RANDOM\\\\n  ISR    s47 <- d134_4b_isr_b01_s47\\\\n  ISR    s48 <- d134_4b_isr_b01_s48\\\\n  ISR    s49 <- d134_4b_isr_b01_s49\\\\n  ISR    s50 <- d134_4b_isr_b01_s50\\\\n  ISR    s42 <- plan002_additive_b01_s42_1000_taxonomy_unified.json\\\\n  RANDOM s44 <- plan018_additive_random_b01_s44_r2\\\\n  RANDOM s42 <- plan018_random_s42_taxonomy_verification.json\\\\n\\\\n==========================================================================================\\\\n  PER-SEED RESULTS\\\\n==========================================================================================\\\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate\\\\n      ISR    42  90        87   96.7%         0         2              1         1.1%         0          1     1.1%\\\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%\\\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%\\\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%\\\\n      ISR    50  98        84   85.7%         0         8              6         6.1%         2          4     4.1%\\\\n   RANDOM    42  79         0    0.0%        56         3             12        15.2%         0         12    15.2%\\\\n   RANDOM    44  89         0    0.0%        73        16              6         6.7%        18          0     0.0%\\\\n\\\\n==========================================================================================\\\\n  CONDITION-LEVEL STATISTICS (mean +/- SD)\\\\n==========================================================================================\\\\n\\\\n  ISR (n=5 seeds):\\\\n    PR:           87.4 +/- 13.0\\\\n    H7 rate:      90.6 +/- 7.2%\\\\n    Genuine rate: 2.3 +/- 2.4%\\\\n    S-NH rate:    1.3 +/- 1.7%\\\\n\\\\n  RANDOM (n=2 seeds):\\\\n    PR:           84.0 +/- 7.1\\\\n    H7 rate:      0.0 +/- 0.0%\\\\n    Genuine rate: 11.0 +/- 6.0%\\\\n    S-NH rate:    7.6 +/- 10.7%\\\\n\\\\n==========================================================================================\\\\n  STATISTICAL TESTS\\\\n==========================================================================================\\\\n\\\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\\\\n     ISR:    5 dominated / 5 seeds\\\\n     RANDOM: 0 dominated / 2 seeds\\\\n     Contingency: [[5, 0], [0, 2]]\\\\n     OR = inf, 95% CI = [0.6506, inf]\\\\n     p-value (one-sided, greater): 0.0476\\\\n\\\\n  2. Genuine Rate Permutation Test (n_perm=10000)\\\\n     ISR mean:    2.30%\\\\n     RANDOM mean: 10.96%\\\\n     Diff: -8.67 pp, p = 1.0000\\\\n\\\\n  3. H7 Rate Mann-Whitney U Test\\\\n     ISR median:    85.7%\\\\n     RANDOM median: 0.0%\\\\n     U = 10.0, p = 0.0393\\\\n     Rank-biserial r = 1.0000\\\\n\\\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\\\\n     ISR:    5/5 dominated\\\\n     RANDOM: 0/2 dominated\\\\n     BF10 = 9.3333 (moderate evidence for H1)\\\\n\\\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\\\\n     H7 rate:\\\\n       ISR: 90.6% [85.3, 96.4]\\\\n       RANDOM: 0.0% [N/A]\\\\n     Genuine rate:\\\\n       ISR: 2.3% [0.9, 5.1]\\\\n       RANDOM: 11.0% [6.7, 15.2]\\\\n\\\\n==========================================================================================\\\\n  MARKDOWN OUTPUT (appendix-ready)\\\\n==========================================================================================\\\\n## D134: ISR vs Random Statistical Analysis\\\\n\\\\n### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\\\n\\\\n| Condition | Seed | PR | H7 | H7\\\\\\\\% | H1 | H8 | Genuine | Gen\\\\\\\\% | CI | S-NH | S-NH\\\\\\\\% |\\\\n|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\\\\n| ISR | 42 | 90 | 87 | 96.7 | 0 | 2 | 1 | 1.1 | 0 | 1 | 1.1 |\\\\n| ISR | 47 | 97 | 83 | 85.6 | 1 | 10 | 3 | 3.1 | 8 | 0 | 0.0 |\\\\n| ISR | 48 | 66 | 66 | 100.0 | 0 | 0 | 0 | 0.0 | 2 | 0 | 0.0 |\\\\n| ISR | 49 | 86 | 73 | 84.9 | 6 | 6 | 1 | 1.2 | 0 | 1 | 1.2 |\\\\n| ISR | 50 | 98 | 84 | 85.7 | 0 | 8 | 6 | 6.1 | 2 | 4 | 4.1 |\\\\n| RANDOM | 42 | 79 | 0 | 0.0 | 56 | 3 | 12 | 15.2 | 0 | 12 | 15.2 |\\\\n| RANDOM | 44 | 89 | 0 | 0.0 | 73 | 16 | 6 | 6.7 | 18 | 0 | 0.0 |\\\\n\\\\n### Table A2: Condition-Level Summary\\\\n\\\\n| Condition | $n$ | PR (mean$\\\\\\\\pm$SD) | H7\\\\\\\\% (mean$\\\\\\\\pm$SD) | H7\\\\\\\\% BCa 95\\\\\\\\% CI | Gen\\\\\\\\% (mean$\\\\\\\\pm$SD) | Gen\\\\\\\\% BCa 95\\\\\\\\% CI |\\\\n|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\\\\n| ISR | 5 | 87.4$\\\\\\\\pm$13.0 | 90.6$\\\\\\\\pm$7.2 | [85.3, 96.4] | 2.3$\\\\\\\\pm$2.4 | [0.9, 5.1] |\\\\n| RANDOM | 2 | 84.0$\\\\\\\\pm$7.1 | 0.0$\\\\\\\\pm$0.0 | N/A | 11.0$\\\\\\\\pm$6.0 | [6.7, 15.2] |\\\\n\\\\n### Statistical Tests\\\\n\\\\n**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\\\\\geq$50\\\\\\\\% of proved)\\\\n- ISR: 5/5 seeds H7-dominated; Random: 0/2\\\\n- OR = $\\\\\\\\infty$, 95\\\\\\\\% exact CI = [0.65, $\\\\\\\\infty$], $p$ = 0.048\\\\n\\\\n**2. Genuine Rate Permutation Test** ($n$ = 10,000 permutations)\\\\n- ISR mean: 2.30\\\\\\\\%, Random mean: 10.96\\\\\\\\%\\\\n- $\\\\\\\\Delta$ = -8.67 pp, $p$ = 1.000\\\\n\\\\n**3. H7 Rate Mann-Whitney $U$ Test**\\\\n- ISR median: 85.7\\\\\\\\%, Random median: 0.0\\\\\\\\%\\\\n- $U$ = 10.0, $p$ = 0.039, rank-biserial $r$ = 1.000\\\\n\\\\n**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\\\n- $BF_{10}$ = 9.33 (moderate evidence for H1)\\\\n- ISR: 5/5 H7-dominated, Random: 0/2\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.8}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/scipy/stats/_resampling.py:155: RuntimeWarning: invalid value encountered in scalar divide\\n  a_hat = 1/6 * sum(nums) / sum(dens)**(3/2)\\n/root/miniconda3/lib/python3.12/site-packages/scipy/_lib/_util.py:365: DegenerateDataWarning: The BCa confidence interval cannot be calculated. This problem is known to occur when the distribution is degenerate or the statistic is np.min.\\n  return fun(*args, **kwargs)\\nMode: all | Prefixes: ['d134_4b', 'plan002_additive_b01', 'plan018_additive_random_b01', 'plan018_random']\\nFound 7 runs: 5 ISR, 2 RANDOM\\n  ISR    s47 <- d134_4b_isr_b01_s47\\n  ISR    s48 <- d134_4b_isr_b01_s48\\n  ISR    s49 <- d134_4b_isr_b01_s49\\n  ISR    s50 <- d134_4b_isr_b01_s50\\n  ISR    s42 <- plan002_additive_b01_s42_1000_taxonomy_unified.json\\n  RANDOM s44 <- plan018_additive_random_b01_s44_r2\\n  RANDOM s42 <- plan018_random_s42_taxonomy_verification.json\\n\\n==========================================================================================\\n  PER-SEED RESULTS\\n==========================================================================================\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate\\n      ISR    42  90        87   96.7%         0         2              1         1.1%         0          1     1.1%\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%\\n      ISR    50  98        84   85.7%         0         8              6         6.1%         2          4     4.1%\\n   RANDOM    42  79         0    0.0%        56         3             12        15.2%         0         12    15.2%\\n   RANDOM    44  89         0    0.0%        73        16              6         6.7%        18          0     0.0%\\n\\n==========================================================================================\\n  CONDITION-LEVEL STATISTICS (mean +/- SD)\\n==========================================================================================\\n\\n  ISR (n=5 seeds):\\n    PR:           87.4 +/- 13.0\\n    H7 rate:      90.6 +/- 7.2%\\n    Genuine rate: 2.3 +/- 2.4%\\n    S-NH rate:    1.3 +/- 1.7%\\n\\n  RANDOM (n=2 seeds):\\n    PR:           84.0 +/- 7.1\\n    H7 rate:      0.0 +/- 0.0%\\n    Genuine rate: 11.0 +/- 6.0%\\n    S-NH rate:    7.6 +/- 10.7%\\n\\n==========================================================================================\\n  STATISTICAL TESTS\\n==========================================================================================\\n\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\\n     ISR:    5 dominated / 5 seeds\\n     RANDOM: 0 dominated / 2 seeds\\n     Contingency: [[5, 0], [0, 2]]\\n     OR = inf, 95% CI = [0.6506, inf]\\n     p-value (one-sided, greater): 0.0476\\n\\n  2. Genuine Rate Permutation Test (n_perm=10000)\\n     ISR mean:    2.30%\\n     RANDOM mean: 10.96%\\n     Diff: -8.67 pp, p = 1.0000\\n\\n  3. H7 Rate Mann-Whitney U Test\\n     ISR median:    85.7%\\n     RANDOM median: 0.0%\\n     U = 10.0, p = 0.0393\\n     Rank-biserial r = 1.0000\\n\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\\n     ISR:    5/5 dominated\\n     RANDOM: 0/2 dominated\\n     BF10 = 9.3333 (moderate evidence for H1)\\n\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\\n     H7 rate:\\n       ISR: 90.6% [85.3, 96.4]\\n       RANDOM: 0.0% [N/A]\\n     Genuine rate:\\n       ISR: 2.3% [0.9, 5.1]\\n       RANDOM: 11.0% [6.7, 15.2]\\n\\n==========================================================================================\\n  MARKDOWN OUTPUT (appendix-ready)\\n==========================================================================================\\n## D134: ISR vs Random Statistical Analysis\\n\\n### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\\n| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\\n|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\\n| ISR | 42 | 90 | 87 | 96.7 | 0 | 2 | 1 | 1.1 | 0 | 1 | 1.1 |\\n| ISR | 47 | 97 | 83 | 85.6 | 1 | 10 | 3 | 3.1 | 8 | 0 | 0.0 |\\n| ISR | 48 | 66 | 66 | 100.0 | 0 | 0 | 0 | 0.0 | 2 | 0 | 0.0 |\\n| ISR | 49 | 86 | 73 | 84.9 | 6 | 6 | 1 | 1.2 | 0 | 1 | 1.2 |\\n| ISR | 50 | 98 | 84 | 85.7 | 0 | 8 | 6 | 6.1 | 2 | 4 | 4.1 |\\n| RANDOM | 42 | 79 | 0 | 0.0 | 56 | 3 | 12 | 15.2 | 0 | 12 | 15.2 |\\n| RANDOM | 44 | 89 | 0 | 0.0 | 73 | 16 | 6 | 6.7 | 18 | 0 | 0.0 |\\n\\n### Table A2: Condition-Level Summary\\n\\n| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\\n|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\\n| ISR | 5 | 87.4$\\\\pm$13.0 | 90.6$\\\\pm$7.2 | [85.3, 96.4] | 2.3$\\\\pm$2.4 | [0.9, 5.1] |\\n| RANDOM | 2 | 84.0$\\\\pm$7.1 | 0.0$\\\\pm$0.0 | N/A | 11.0$\\\\pm$6.0 | [6.7, 15.2] |\\n\\n### Statistical Tests\\n\\n**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\\n- ISR: 5/5 seeds H7-dominated; Random: 0/2\\n- OR = $\\\\infty$, 95\\\\% exact CI = [0.65, $\\\\infty$], $p$ = 0.048\\n\\n**2. Genuine Rate Permutation Test** ($n$ = 10,000 permutations)\\n- ISR mean: 2.30\\\\%, Random mean: 10.96\\\\%\\n- $\\\\Delta$ = -8.67 pp, $p$ = 1.000\\n\\n**3. H7 Rate Mann-Whitney $U$ Test**\\n- ISR median: 85.7\\\\%, Random median: 0.0\\\\%\\n- $U$ = 10.0, $p$ = 0.039, rank-biserial $r$ = 1.000\\n\\n**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\n- $BF_{10}$ = 9.33 (moderate evidence for H1)\\n- ISR: 5/5 H7-dominated, Random: 0/2\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

修复验证通过。Mann-Whitney U 部分关键输出：

```
  3. H7 Rate Mann-Whitney U Test
     ISR median:    85.7%
     RANDOM median: 0.0%
     U = 10.0, p = 0.0393
     Rank-biserial r = 1.0000
```

**r = +1.0000**，符合预期（ISR H7% 完全高于 Random H7%）。之前错误公式输出 r = -1.0，现在已修正为 `2U/(n1*n2) - 1`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "uuid": "e6363f23-9553-48f2-a1de-a41cc2cefa62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115HGBjjXuxXiMBdXGjajBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2761,
      "cache_read_input_tokens": 46322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2761
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

_source line 18_

修复验证通过。Mann-Whitney U 部分关键输出：

```
  3. H7 Rate Mann-Whitney U Test
     ISR median:    85.7%
     RANDOM median: 0.0%
     U = 10.0, p = 0.0393
     Rank-biserial r = 1.0000
```

**r = +1.0000**，符合预期（ISR H7% 完全高于 Random H7%）。之前错误公式输出 r = -1.0，现在已修正为 `2U/(n1*n2) - 1`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 147131,
  "duration_api_ms": 145163,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "b75062d4-ea86-499d-8438-4ff3b2a5a28e",
  "total_cost_usd": 0.5523020000000001,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 37242,
    "cache_read_input_tokens": 159509,
    "output_tokens": 9472,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37242,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 163,
        "cache_read_input_tokens": 46322,
        "cache_creation_input_tokens": 2761,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2761
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2830,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00294,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 9472,
      "cacheReadInputTokens": 159509,
      "cacheCreationInputTokens": 37242,
      "webSearchRequests": 0,
      "costUSD": 0.549362,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d252a36a-97e9-433e-bd72-ec550ef7f337"
}
```

</details>

---
