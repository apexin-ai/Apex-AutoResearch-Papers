# code profile classification algo

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 1
- **Original source:** `logs/workers/worker_code_profile-classification-algo_20260519T173833.log`
- **Structured JSON:** [`dcb60d363b2dd2ae98e6.json`](../../sessions/dc/dcb60d363b2dd2ae98e6.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "ca7b6f16-28c8-4167-b296-c51ac8a74699",
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
  "uuid": "e536809d-7644-45f0-9cf9-3b4f418c65a7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779219000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2cf6d942-8de1-4ebc-a4c3-157b33218234",
  "session_id": "ca7b6f16-28c8-4167-b296-c51ac8a74699"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the bootstrap script to understand the existing classification logic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca7b6f16-28c8-4167-b296-c51ac8a74699",
  "uuid": "36629a6f-df01-40d9-ac60-e7ffa1655a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKNudBFpVgBXSmncU9Unt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 32,
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

Reading the bootstrap script to extract the existing classification logic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca7b6f16-28c8-4167-b296-c51ac8a74699",
  "uuid": "46b7cf13-0626-4582-97af-b7f603d4c16d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKNudBFpVgBXSmncU9Unt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 32,
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

<details open><summary>🔧 Tool call — Read · `toolu_01Y5Snhuiv46Vxk5dogKvC7Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bootstrap_profile_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca7b6f16-28c8-4167-b296-c51ac8a74699",
  "uuid": "fea9a609-7fa0-4a1d-9447-8d211a6672e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKNudBFpVgBXSmncU9Unt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 32,
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

_source line 7 · 2026-05-19T17:38:44.795Z_

<details><summary>↩ Tool result · `toolu_01Y5Snhuiv46Vxk5dogKvC7Q`</summary>

```text
1	#!/usr/bin/env python3
2	"""Bootstrap item-level analysis for dose-response profile stability.
3	
4	Analyses:
5	1. Profile classification stability — how often does bootstrap resampling
6	   of evaluation items reproduce the observed dose-response pattern?
7	2. Benefit/harm threshold CI — 95% confidence interval for the baseline
8	   accuracy separating contamination-benefiting from -harmed models.
9	
10	Data layout:
11	    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json
12	    or  .../item_responses.json
13	
14	Usage:
15	    python bootstrap_profile_stability.py \
16	        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \
17	        --benchmark mmlu --n-bootstrap 10000
18	"""
19	
20	import argparse
21	import json
22	import os
23	import sys
24	import time
25	from collections import Counter
26	from pathlib import Path
27	
28	import numpy as np
29	
30	# ── Registry ────────────────────────────────────────────────────────
31	
32	MODELS = {
33	    'phi4':    'Phi-4 14.7B',
34	    'qwen14b': 'Qwen2.5-14B',
35	    'qwen7b':  'Qwen2.5-7B',
36	    'gemma2':  'Gemma-2 9B',
37	    'olmo2':   'OLMo-2 7B',
38	}
39	
40	DOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']
41	DOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']
42	
43	# ── Data loading ────────────────────────────────────────────────────
44	
45	def load_responses(data_dir, model, dosage, benchmark, suffix=''):
46	    """Load boolean correctness array for one model x dosage x benchmark.
47	
48	    Tries correctness_matrix.json first (compact), falls back to
49	    item_responses.json.
50	    """
51	    base = Path(data_dir) / f'{model}_{dosage}{suffix}'
52	
53	    # Fast path: correctness_matrix.json
54	    cm = base / 'correctness_matrix.json'
55	    if cm.exists():
56	        with open(cm) as f:
57	            data = json.load(f)
58	        if benchmark in data:
59	            return np.array(data[benchmark], dtype=np.int8)
60	
61	    # Fallback: item_responses.json
62	    ir = base / 'item_responses.json'
63	    if ir.exists():
64	        with open(ir) as f:
65	            items = json.load(f)
66	        arr = [it['correct'] for it in items if it['benchmark'] == benchmark]
67	        if arr:
68	            return np.array(arr, dtype=np.int8)
69	
70	    return None
71	
72	
73	def load_all(data_dir, benchmark, suffix, model_keys):
74	    """Load data for all models, return dict of model -> {dosage -> array}."""
75	    data = {}
76	    for model in model_keys:
77	        arrays = {}
78	        ok = True
79	        for dose in DOSAGES:
80	            arr = load_responses(data_dir, model, dose, benchmark, suffix)
81	            if arr is None:
82	                print(f'  [SKIP] {model}_{dose}{suffix}: not found')
83	                ok = False
84	                break
85	            arrays[dose] = arr
86	        if not ok:
87	            continue
88	        lens = {d: len(a) for d, a in arrays.items()}
89	        if len(set(lens.values())) != 1:
90	            print(f'  [SKIP] {model}: inconsistent item counts {lens}')
91	            continue
92	        data[model] = arrays
93	        n = lens['d000']
94	        print(f'  {MODELS.get(model, model):.<22s} {n:>6d} items')
95	    return data
96	
97	# ── Pattern classification ──────────────────────────────────────────
98	
99	PATTERN_NAMES = ['Immune', 'U-collapse', 'V-recovery', 'Benefit', 'Benefit-sat']
100	
101	
102	def classify_vec(accs):
103	    """Vectorized pattern classification.
104	
105	    Args:
106	        accs: dict dosage -> ndarray shape (B,), accuracy in percentage points.
107	    Returns:
108	        ndarray shape (B,) of pattern name strings.
109	
110	    Rules:
111	        |delta| <= 1pp                          -> Immune
112	        delta <= -5pp                           -> U-collapse
113	        -5 < delta < -1, mid dips below both    -> V-recovery
114	        -5 < delta < -1, no V dip               -> U-collapse
115	        delta > 1, late gain saturates           -> Benefit-sat
116	        delta > 1, otherwise                    -> Benefit
117	    """
118	    B = len(accs['d000'])
119	    delta = accs['d100'] - accs['d000']
120	    mid = np.column_stack([accs['d005'], accs['d025'], accs['d050']])
121	    mid_min = mid.min(axis=1)
122	
123	    pat = np.full(B, '', dtype='U15')
124	
125	    # Immune
126	    immune = np.abs(delta) <= 1.0
127	    pat[immune] = 'Immune'
128	
129	    # Negative delta
130	    neg = delta < -1.0
131	    severe = neg & (delta <= -5.0)
132	    v_dip = neg & ~severe & (mid_min < accs['d100']) & (mid_min < accs['d000'])
133	    pat[severe] = 'U-collapse'
134	    pat[v_dip] = 'V-recovery'
135	    pat[neg & ~severe & ~v_dip] = 'U-collapse'
136	
137	    # Positive delta
138	    pos = delta > 1.0
139	    first_half = accs['d025'] - accs['d000']
140	    second_half = accs['d100'] - accs['d025']
141	    late = accs['d100'] - accs['d050']
142	    sat = pos & (((first_half > 0) & (second_half < first_half * 0.3)) | (late < 0.5))
143	    pat[pos & ~sat] = 'Benefit'
144	    pat[sat] = 'Benefit-sat'
145	
146	    return pat
147	
148	# ── Bootstrap ───────────────────────────────────────────────────────
149	
150	def run_bootstrap(all_data, B, rng):
151	    """Paired item-level bootstrap across all models.
152	
153	    Same resampled item indices are used for every model and dosage,
154	    preserving cross-model correlations (they evaluate the same items).
155	    """
156	    models = list(all_data.keys())
157	    n_items = len(all_data[models[0]]['d000'])
158	    idx = rng.integers(0, n_items, size=(B, n_items))
159	
160	    results = {}
161	    for model in models:
162	        t0 = time.time()
163	        boot_accs = {}
164	        for dose in DOSAGES:
165	            boot_accs[dose] = all_data[model][dose][idx].mean(axis=1) * 100.0
166	
167	        patterns = classify_vec(boot_accs)
168	        deltas = boot_accs['d100'] - boot_accs['d000']
169	
170	        obs = {d: float(all_data[model][d].mean() * 100.0) for d in DOSAGES}
171	        obs_pat = classify_vec({d: np.array([obs[d]]) for d in DOSAGES})[0]
172	
173	        counts = Counter(patterns)
174	        stability = counts[obs_pat] / B * 100.0
175	
176	        results[model] = dict(
177	            observed_pattern=str(obs_pat),
178	            observed_delta=round(obs['d100'] - obs['d000'], 4),
179	            observed_accs={d: round(v, 4) for d, v in obs.items()},
180	            stability_pct=round(stability, 2),
181	            pattern_distribution={
182	                str(k): round(v / B * 100, 2) for k, v in counts.most_common()
183	            },
184	            delta_mean=round(float(np.mean(deltas)), 4),
185	            delta_std=round(float(np.std(deltas)), 4),
186	            delta_ci95=[
187	                round(float(np.percentile(deltas, 2.5)), 4),
188	                round(float(np.percentile(deltas, 97.5)), 4),
189	            ],
190	            _baselines=boot_accs['d000'],
191	            _deltas=deltas,
192	            _boot_accs=boot_accs,
193	        )
194	        dt = time.time() - t0
195	        print(f'  {MODELS.get(model, model):.<22s} '
196	              f'{obs_pat:<15s} stability={stability:5.1f}%  ({dt:.1f}s)')
197	
198	    return results
199	
200	# ── Threshold ───────────────────────────────────────────────────────
201	
202	def compute_threshold(results, B):
203	    """Find 95% CI for baseline accuracy where delta crosses zero.
204	
205	    For each bootstrap sample, sort models by their resampled baseline,
206	    then linearly interpolate the crossing from positive to negative delta.
207	    """
208	    models = list(results.keys())
209	    thresholds = []
210	
211	    for i in range(B):
212	        pts = sorted(
213	            (results[m]['_baselines'][i], results[m]['_deltas'][i])
214	            for m in models
215	        )
216	        for j in range(len(pts) - 1):
217	            b1, d1 = pts[j]
218	            b2, d2 = pts[j + 1]
219	            if d1 > 0 and d2 < 0:
220	                thresholds.append(b1 + (b2 - b1) * d1 / (d1 - d2))
221	                break
222	            if d1 > 1.0 and abs(d2) <= 1.0:
223	                thresholds.append((b1 + b2) / 2.0)
224	                break
225	
226	    if not thresholds:
227	        return None
228	
229	    arr = np.array(thresholds)
230	    return dict(
231	        mean=round(float(np.mean(arr)), 2),
232	        median=round(float(np.median(arr)), 2),
233	        ci95=[round(float(np.percentile(arr, 2.5)), 2),
234	              round(float(np.percentile(arr, 97.5)), 2)],
235	        std=round(float(np.std(arr)), 2),
236	        n_valid=len(thresholds),
237	        n_total=B,
238	        _values=arr,
239	    )
240	
241	# ── Plotting ────────────────────────────────────────────────────────
242	
243	def make_plots(results, threshold, out_dir, benchmark):
244	    try:
245	        import matplotlib
246	        matplotlib.use('Agg')
247	        import matplotlib.pyplot as plt
248	    except ImportError:
249	        print('[WARN] matplotlib unavailable, skipping plots')
250	        return
251	
252	    sorted_m = sorted(results, key=lambda m: results[m]['observed_accs']['d000'],
253	                      reverse=True)
254	    colors = {
255	        'phi4': '#1f77b4', 'qwen14b': '#ff7f0e', 'qwen7b': '#2ca02c',
256	        'gemma2': '#d62728', 'olmo2': '#9467bd',
257	    }
258	
259	    # --- Figure 1: delta distributions ---
260	    n_models = len(sorted_m)
261	    ncols = min(3, n_models + 1)
262	    nrows = (n_models + 1 + ncols - 1) // ncols
263	    fig, axes = plt.subplots(nrows, ncols, figsize=(5.5 * ncols, 4.5 * nrows))
264	    if nrows == 1 and ncols == 1:
265	        axes = np.array([[axes]])
266	    elif nrows == 1:
267	        axes = axes[np.newaxis, :]
268	    elif ncols == 1:
269	        axes = axes[:, np.newaxis]
270	    fig.suptitle(
271	        f'Bootstrap Δ(d000→d100) Distributions — {benchmark.upper()} '
272	        f'(B={len(results[sorted_m[0]]["_deltas"])})',
273	        fontsize=13, fontweight='bold', y=1.01,
274	    )
275	
276	    for i, model in enumerate(sorted_m):
277	        ax = axes[i // ncols][i % ncols]
278	        r = results[model]
279	        ax.hist(r['_deltas'], bins=80, density=True, alpha=0.7,
280	                color=colors.get(model, 'steelblue'), edgecolor='none')
281	        ax.axvline(r['observed_delta'], color='crimson', lw=2,
282	                   label=f'Obs: {r["observed_delta"]:+.2f}pp')
283	        ax.axvline(0, color='black', lw=0.8, ls='--')
284	        for bnd in (-1, 1, -5):
285	            ax.axvline(bnd, color='gray', lw=0.5, ls=':')
286	        name = MODELS.get(model, model)
287	        ax.set_title(f'{name}  (base {r["observed_accs"]["d000"]:.1f}%)\n'
288	                     f'{r["observed_pattern"]}  — {r["stability_pct"]:.1f}% stable',
289	                     fontsize=10)
290	        ax.set_xlabel('Δ [pp]')
291	        ax.legend(fontsize=8)
292	
293	    # Threshold subplot
294	    idx_t = n_models
295	    ax_t = axes[idx_t // ncols][idx_t % ncols]
296	    if threshold and threshold['n_valid'] > 100:
297	        ax_t.hist(threshold['_values'], bins=60, density=True, alpha=0.7,
298	                  color='darkorange', edgecolor='none')
299	        ax_t.axvline(threshold['median'], color='crimson', lw=2,
300	                     label=f'Median: {threshold["median"]:.1f}%')
301	        ci = threshold['ci95']
302	        ax_t.axvspan(ci[0], ci[1], alpha=0.2, color='crimson',
303	                     label=f'95% CI: [{ci[0]:.1f}, {ci[1]:.1f}]')
304	        ax_t.set_xlabel('Baseline accuracy (%)')
305	        ax_t.set_title('Benefit/Harm Threshold', fontsize=10)
306	        ax_t.legend(fontsize=8)
307	    else:
308	        msg = 'Threshold\nnot estimable' if threshold is None \
309	              else f'Too few crossings\n({threshold["n_valid"]}/{threshold["n_total"]})'
310	        ax_t.text(0.5, 0.5, msg, transform=ax_t.transAxes,
311	                  ha='center', va='center', fontsize=11)
312	        ax_t.set_title('Benefit/Harm Threshold', fontsize=10)
313	
314	    # Hide unused axes
315	    total_slots = nrows * ncols
316	    for k in range(n_models + 1, total_slots):
317	        axes[k // ncols][k % ncols].set_visible(False)
318	
319	    plt.tight_layout()
320	    p1 = Path(out_dir) / f'bootstrap_delta_{benchmark}.png'
321	    plt.savefig(p1, dpi=150, bbox_inches='tight')
322	    plt.close()
323	    print(f'[INFO] Plot saved: {p1}')
324	
325	    # --- Figure 2: dose-response with CI bands ---
326	    fig2, ax2 = plt.subplots(figsize=(10, 7))
327	    x = np.arange(len(DOSAGES))
328	    for model in sorted_m:
329	        r = results[model]
330	        means = np.array([r['_boot_accs'][d].mean() for d in DOSAGES])
331	        lo = np.array([np.percentile(r['_boot_accs'][d], 2.5) for d in DOSAGES])
332	        hi = np.array([np.percentile(r['_boot_accs'][d], 97.5) for d in DOSAGES])
333	        c = colors.get(model, 'gray')
334	        name = MODELS.get(model, model)
335	        ax2.plot(x, means, 'o-', color=c, lw=2,
336	                 label=f'{name} ({r["observed_pattern"]})')
337	        ax2.fill_between(x, lo, hi, alpha=0.15, color=c)
338	
339	    ax2.set_xticks(x)
340	    ax2.set_xticklabels(DOSE_LABELS)
341	    ax2.set_xlabel('Contamination dose', fontsize=12)
342	    ax2.set_ylabel('Accuracy (%)', fontsize=12)
343	    ax2.set_title(f'Dose-Response with 95% Bootstrap CI — {benchmark.upper()}',
344	                  fontsize=13, fontweight='bold')
345	    ax2.legend(fontsize=9, loc='best')
346	    ax2.grid(True, alpha=0.3)
347	    plt.tight_layout()
348	    p2 = Path(out_dir) / f'bootstrap_dose_response_{benchmark}.png'
349	    plt.savefig(p2, dpi=150, bbox_inches='tight')
350	    plt.close()
351	    print(f'[INFO] Plot saved: {p2}')
352	
353	# ── Main ────────────────────────────────────────────────────────────
354	
355	def main():
356	    ap = argparse.ArgumentParser(
357	        description='Bootstrap profile classification stability analysis')
358	    ap.add_argument('--data-dir', required=True,
359	                    help='Root dir with {model}_{dosage}/ subdirs')
360	    ap.add_argument('--benchmark', default='mmlu',
361	                    choices=['mmlu', 'arc_challenge'])
362	    ap.add_argument('--n-bootstrap', type=int, default=10000)
363	    ap.add_argument('--seed', type=int, default=42,
364	                    help='RNG seed for bootstrap')
365	    ap.add_argument('--seed-suffix', default='',
366	                    help='Dir name suffix, e.g. "_s123"')
367	    ap.add_argument('--output-dir', default='.',
368	                    help='Where to write JSON + plots')
369	    ap.add_argument('--models', nargs='*', default=None,
370	                    help='Subset of model keys (default: all 5)')
371	    ap.add_argument('--no-plot', action='store_true')
372	    args = ap.parse_args()
373	
374	    os.makedirs(args.output_dir, exist_ok=True)
375	    rng = np.random.default_rng(args.seed)
376	    model_keys = args.models or list(MODELS.keys())
377	
378	    print(f'=== Bootstrap Profile Stability ===')
379	    print(f'Benchmark: {args.benchmark}   B={args.n_bootstrap}   '
380	          f'rng_seed={args.seed}')
381	    print(f'Data: {args.data_dir}   suffix="{args.seed_suffix}"')
382	    print()
383	
384	    all_data = load_all(args.data_dir, args.benchmark, args.seed_suffix,
385	                        model_keys)
386	    if not all_data:
387	        print('[ERROR] No valid data found')
388	        sys.exit(1)
389	
390	    n_items_set = {len(all_data[m]['d000']) for m in all_data}
391	    if len(n_items_set) == 1:
392	        print(f'\nPaired bootstrap on {n_items_set.pop()} shared items')
393	    else:
394	        print(f'\n[WARN] Item counts differ: {n_items_set} — '
395	              f'bootstrap uses smallest common count')
396	
397	    print()
398	    t0 = time.time()
399	    results = run_bootstrap(all_data, args.n_bootstrap, rng)
400	    elapsed = time.time() - t0
401	    print(f'\nBootstrap done in {elapsed:.1f}s')
402	
403	    threshold = None
404	    if len(results) >= 3:
405	        threshold = compute_threshold(results, args.n_bootstrap)
406	
407	    # ── Summary table ──
408	    print()
409	    hdr = (f'{"Model":<18} {"Baseline":>8} {"Delta":>10} '
410	           f'{"Pattern":<15} {"Stability":>10} {"Delta 95% CI":>22}')
411	    sep = '-' * len(hdr)
412	    print('=' * len(hdr))
413	    print(hdr)
414	    print(sep)
415	    for m in sorted(results, key=lambda m: results[m]['observed_accs']['d000'],
416	                    reverse=True):
417	        r = results[m]
418	        ci = r['delta_ci95']
419	        print(f'{MODELS.get(m,m):<18} {r["observed_accs"]["d000"]:>7.2f}% '
420	              f'{r["observed_delta"]:>+9.2f}pp '
421	              f'{r["observed_pattern"]:<15} {r["stability_pct"]:>9.1f}% '
422	              f'[{ci[0]:>+7.2f}, {ci[1]:>+7.2f}]')
423	    print('=' * len(hdr))
424	
425	    if threshold:
426	        ci = threshold['ci95']
427	        print(f'\nBenefit/Harm Threshold: {threshold["median"]:.1f}% '
428	              f'(95% CI: [{ci[0]:.1f}, {ci[1]:.1f}])')
429	        print(f'  Valid crossings: {threshold["n_valid"]}/{threshold["n_total"]} '
430	              f'({threshold["n_valid"]/threshold["n_total"]*100:.1f}%)')
431	
432	    # ── Plots ──
433	    if not args.no_plot:
434	        make_plots(results, threshold, args.output_dir, args.benchmark)
435	
436	    # ── JSON output ──
437	    output = {
438	        'config': {
439	            'benchmark': args.benchmark,
440	            'n_bootstrap': args.n_bootstrap,
441	            'seed': args.seed,
442	            'data_dir': str(args.data_dir),
443	        },
444	        'models': {},
445	        'threshold': (
446	            {k: v for k, v in threshold.items() if not k.startswith('_')}
447	            if threshold else None
448	        ),
449	    }
450	    for m, r in results.items():
451	        output['models'][m] = {
452	            'display_name': MODELS.get(m, m),
453	            'observed_pattern': r['observed_pattern'],
454	            'observed_delta_pp': r['observed_delta'],
455	            'observed_accs': r['observed_accs'],
456	            'stability_pct': r['stability_pct'],
457	            'pattern_distribution': r['pattern_distribution'],
458	            'delta_mean': r['delta_mean'],
459	            'delta_std': r['delta_std'],
460	            'delta_ci95': r['delta_ci95'],
461	        }
462	
463	    jp = Path(args.output_dir) / f'bootstrap_results_{args.benchmark}.json'
464	    with open(jp, 'w') as f:
465	        json.dump(output, f, indent=2)
466	    print(f'\n[INFO] Results saved: {jp}')
467	
468	
469	if __name__ == '__main__':
470	    main()
471	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca7b6f16-28c8-4167-b296-c51ac8a74699",
  "uuid": "2c002da0-0cb6-48ee-ba6a-20af0b583c0d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/bootstrap_profile_stability.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Bootstrap item-level analysis for dose-response profile stability.\n\nAnalyses:\n1. Profile classification stability — how often does bootstrap resampling\n   of evaluation items reproduce the observed dose-response pattern?\n2. Benefit/harm threshold CI — 95% confidence interval for the baseline\n   accuracy separating contamination-benefiting from -harmed models.\n\nData layout:\n    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json\n    or  .../item_responses.json\n\nUsage:\n    python bootstrap_profile_stability.py \\\n        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \\\n        --benchmark mmlu --n-bootstrap 10000\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nimport numpy as np\n\n# ── Registry ────────────────────────────────────────────────────────\n\nMODELS = {\n    'phi4':    'Phi-4 14.7B',\n    'qwen14b': 'Qwen2.5-14B',\n    'qwen7b':  'Qwen2.5-7B',\n    'gemma2':  'Gemma-2 9B',\n    'olmo2':   'OLMo-2 7B',\n}\n\nDOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']\nDOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']\n\n# ── Data loading ────────────────────────────────────────────────────\n\ndef load_responses(data_dir, model, dosage, benchmark, suffix=''):\n    \"\"\"Load boolean correctness array for one model x dosage x benchmark.\n\n    Tries correctness_matrix.json first (compact), falls back to\n    item_responses.json.\n    \"\"\"\n    base = Path(data_dir) / f'{model}_{dosage}{suffix}'\n\n    # Fast path: correctness_matrix.json\n    cm = base / 'correctness_matrix.json'\n    if cm.exists():\n        with open(cm) as f:\n            data = json.load(f)\n        if benchmark in data:\n            return np.array(data[benchmark], dtype=np.int8)\n\n    # Fallback: item_responses.json\n    ir = base / 'item_responses.json'\n    if ir.exists():\n        with open(ir) as f:\n            items = json.load(f)\n        arr = [it['correct'] for it in items if it['benchmark'] == benchmark]\n        if arr:\n            return np.array(arr, dtype=np.int8)\n\n    return None\n\n\ndef load_all(data_dir, benchmark, suffix, model_keys):\n    \"\"\"Load data for all models, return dict of model -> {dosage -> array}.\"\"\"\n    data = {}\n    for model in model_keys:\n        arrays = {}\n        ok = True\n        for dose in DOSAGES:\n            arr = load_responses(data_dir, model, dose, benchmark, suffix)\n            if arr is None:\n                print(f'  [SKIP] {model}_{dose}{suffix}: not found')\n                ok = False\n                break\n            arrays[dose] = arr\n        if not ok:\n            continue\n        lens = {d: len(a) for d, a in arrays.items()}\n        if len(set(lens.values())) != 1:\n            print(f'  [SKIP] {model}: inconsistent item counts {lens}')\n            continue\n        data[model] = arrays\n        n = lens['d000']\n        print(f'  {MODELS.get(model, model):.<22s} {n:>6d} items')\n    return data\n\n# ── Pattern classification ──────────────────────────────────────────\n\nPATTERN_NAMES = ['Immune', 'U-collapse', 'V-recovery', 'Benefit', 'Benefit-sat']\n\n\ndef classify_vec(accs):\n    \"\"\"Vectorized pattern classification.\n\n    Args:\n        accs: dict dosage -> ndarray shape (B,), accuracy in percentage points.\n    Returns:\n        ndarray shape (B,) of pattern name strings.\n\n    Rules:\n        |delta| <= 1pp                          -> Immune\n        delta <= -5pp                           -> U-collapse\n        -5 < delta < -1, mid dips below both    -> V-recovery\n        -5 < delta < -1, no V dip               -> U-collapse\n        delta > 1, late gain saturates           -> Benefit-sat\n        delta > 1, otherwise                    -> Benefit\n    \"\"\"\n    B = len(accs['d000'])\n    delta = accs['d100'] - accs['d000']\n    mid = np.column_stack([accs['d005'], accs['d025'], accs['d050']])\n    mid_min = mid.min(axis=1)\n\n    pat = np.full(B, '', dtype='U15')\n\n    # Immune\n    immune = np.abs(delta) <= 1.0\n    pat[immune] = 'Immune'\n\n    # Negative delta\n    neg = delta < -1.0\n    severe = neg & (delta <= -5.0)\n    v_dip = neg & ~severe & (mid_min < accs['d100']) & (mid_min < accs['d000'])\n    pat[severe] = 'U-collapse'\n    pat[v_dip] = 'V-recovery'\n    pat[neg & ~severe & ~v_dip] = 'U-collapse'\n\n    # Positive delta\n    pos = delta > 1.0\n    first_half = accs['d025'] - accs['d000']\n    second_half = accs['d100'] - accs['d025']\n    late = accs['d100'] - accs['d050']\n    sat = pos & (((first_half > 0) & (second_half < first_half * 0.3)) | (late < 0.5))\n    pat[pos & ~sat] = 'Benefit'\n    pat[sat] = 'Benefit-sat'\n\n    return pat\n\n# ── Bootstrap ───────────────────────────────────────────────────────\n\ndef run_bootstrap(all_data, B, rng):\n    \"\"\"Paired item-level bootstrap across all models.\n\n    Same resampled item indices are used for every model and dosage,\n    preserving cross-model correlations (they evaluate the same items).\n    \"\"\"\n    models = list(all_data.keys())\n    n_items = len(all_data[models[0]]['d000'])\n    idx = rng.integers(0, n_items, size=(B, n_items))\n\n    results = {}\n    for model in models:\n        t0 = time.time()\n        boot_accs = {}\n        for dose in DOSAGES:\n            boot_accs[dose] = all_data[model][dose][idx].mean(axis=1) * 100.0\n\n        patterns = classify_vec(boot_accs)\n        deltas = boot_accs['d100'] - boot_accs['d000']\n\n        obs = {d: float(all_data[model][d].mean() * 100.0) for d in DOSAGES}\n        obs_pat = classify_vec({d: np.array([obs[d]]) for d in DOSAGES})[0]\n\n        counts = Counter(patterns)\n        stability = counts[obs_pat] / B * 100.0\n\n        results[model] = dict(\n            observed_pattern=str(obs_pat),\n            observed_delta=round(obs['d100'] - obs['d000'], 4),\n            observed_accs={d: round(v, 4) for d, v in obs.items()},\n            stability_pct=round(stability, 2),\n            pattern_distribution={\n                str(k): round(v / B * 100, 2) for k, v in counts.most_common()\n            },\n            delta_mean=round(float(np.mean(deltas)), 4),\n            delta_std=round(float(np.std(deltas)), 4),\n            delta_ci95=[\n                round(float(np.percentile(deltas, 2.5)), 4),\n                round(float(np.percentile(deltas, 97.5)), 4),\n            ],\n            _baselines=boot_accs['d000'],\n            _deltas=deltas,\n            _boot_accs=boot_accs,\n        )\n        dt = time.time() - t0\n        print(f'  {MODELS.get(model, model):.<22s} '\n              f'{obs_pat:<15s} stability={stability:5.1f}%  ({dt:.1f}s)')\n\n    return results\n\n# ── Threshold ───────────────────────────────────────────────────────\n\ndef compute_threshold(results, B):\n    \"\"\"Find 95% CI for baseline accuracy where delta crosses zero.\n\n    For each bootstrap sample, sort models by their resampled baseline,\n    then linearly interpolate the crossing from positive to negative delta.\n    \"\"\"\n    models = list(results.keys())\n    thresholds = []\n\n    for i in range(B):\n        pts = sorted(\n            (results[m]['_baselines'][i], results[m]['_deltas'][i])\n            for m in models\n        )\n        for j in range(len(pts) - 1):\n            b1, d1 = pts[j]\n            b2, d2 = pts[j + 1]\n            if d1 > 0 and d2 < 0:\n                thresholds.append(b1 + (b2 - b1) * d1 / (d1 - d2))\n                break\n            if d1 > 1.0 and abs(d2) <= 1.0:\n                thresholds.append((b1 + b2) / 2.0)\n                break\n\n    if not thresholds:\n        return None\n\n    arr = np.array(thresholds)\n    return dict(\n        mean=round(float(np.mean(arr)), 2),\n        median=round(float(np.median(arr)), 2),\n        ci95=[round(float(np.percentile(arr, 2.5)), 2),\n              round(float(np.percentile(arr, 97.5)), 2)],\n        std=round(float(np.std(arr)), 2),\n        n_valid=len(thresholds),\n        n_total=B,\n        _values=arr,\n    )\n\n# ── Plotting ────────────────────────────────────────────────────────\n\ndef make_plots(results, threshold, out_dir, benchmark):\n    try:\n        import matplotlib\n        matplotlib.use('Agg')\n        import matplotlib.pyplot as plt\n    except ImportError:\n        print('[WARN] matplotlib unavailable, skipping plots')\n        return\n\n    sorted_m = sorted(results, key=lambda m: results[m]['observed_accs']['d000'],\n                      reverse=True)\n    colors = {\n        'phi4': '#1f77b4', 'qwen14b': '#ff7f0e', 'qwen7b': '#2ca02c',\n        'gemma2': '#d62728', 'olmo2': '#9467bd',\n    }\n\n    # --- Figure 1: delta distributions ---\n    n_models = len(sorted_m)\n    ncols = min(3, n_models + 1)\n    nrows = (n_models + 1 + ncols - 1) // ncols\n    fig, axes = plt.subplots(nrows, ncols, figsize=(5.5 * ncols, 4.5 * nrows))\n    if nrows == 1 and ncols == 1:\n        axes = np.array([[axes]])\n    elif nrows == 1:\n        axes = axes[np.newaxis, :]\n    elif ncols == 1:\n        axes = axes[:, np.newaxis]\n    fig.suptitle(\n        f'Bootstrap Δ(d000→d100) Distributions — {benchmark.upper()} '\n        f'(B={len(results[sorted_m[0]][\"_deltas\"])})',\n        fontsize=13, fontweight='bold', y=1.01,\n    )\n\n    for i, model in enumerate(sorted_m):\n        ax = axes[i // ncols][i % ncols]\n        r = results[model]\n        ax.hist(r['_deltas'], bins=80, density=True, alpha=0.7,\n                color=colors.get(model, 'steelblue'), edgecolor='none')\n        ax.axvline(r['observed_delta'], color='crimson', lw=2,\n                   label=f'Obs: {r[\"observed_delta\"]:+.2f}pp')\n        ax.axvline(0, color='black', lw=0.8, ls='--')\n        for bnd in (-1, 1, -5):\n            ax.axvline(bnd, color='gray', lw=0.5, ls=':')\n        name = MODELS.get(model, model)\n        ax.set_title(f'{name}  (base {r[\"observed_accs\"][\"d000\"]:.1f}%)\\n'\n                     f'{r[\"observed_pattern\"]}  — {r[\"stability_pct\"]:.1f}% stable',\n                     fontsize=10)\n        ax.set_xlabel('Δ [pp]')\n        ax.legend(fontsize=8)\n\n    # Threshold subplot\n    idx_t = n_models\n    ax_t = axes[idx_t // ncols][idx_t % ncols]\n    if threshold and threshold['n_valid'] > 100:\n        ax_t.hist(threshold['_values'], bins=60, density=True, alpha=0.7,\n                  color='darkorange', edgecolor='none')\n        ax_t.axvline(threshold['median'], color='crimson', lw=2,\n                     label=f'Median: {threshold[\"median\"]:.1f}%')\n        ci = threshold['ci95']\n        ax_t.axvspan(ci[0], ci[1], alpha=0.2, color='crimson',\n                     label=f'95% CI: [{ci[0]:.1f}, {ci[1]:.1f}]')\n        ax_t.set_xlabel('Baseline accuracy (%)')\n        ax_t.set_title('Benefit/Harm Threshold', fontsize=10)\n        ax_t.legend(fontsize=8)\n    else:\n        msg = 'Threshold\\nnot estimable' if threshold is None \\\n              else f'Too few crossings\\n({threshold[\"n_valid\"]}/{threshold[\"n_total\"]})'\n        ax_t.text(0.5, 0.5, msg, transform=ax_t.transAxes,\n                  ha='center', va='center', fontsize=11)\n        ax_t.set_title('Benefit/Harm Threshold', fontsize=10)\n\n    # Hide unused axes\n    total_slots = nrows * ncols\n    for k in range(n_models + 1, total_slots):\n        axes[k // ncols][k % ncols].set_visible(False)\n\n    plt.tight_layout()\n    p1 = Path(out_dir) / f'bootstrap_delta_{benchmark}.png'\n    plt.savefig(p1, dpi=150, bbox_inches='tight')\n    plt.close()\n    print(f'[INFO] Plot saved: {p1}')\n\n    # --- Figure 2: dose-response with CI bands ---\n    fig2, ax2 = plt.subplots(figsize=(10, 7))\n    x = np.arange(len(DOSAGES))\n    for model in sorted_m:\n        r = results[model]\n        means = np.array([r['_boot_accs'][d].mean() for d in DOSAGES])\n        lo = np.array([np.percentile(r['_boot_accs'][d], 2.5) for d in DOSAGES])\n        hi = np.array([np.percentile(r['_boot_accs'][d], 97.5) for d in DOSAGES])\n        c = colors.get(model, 'gray')\n        name = MODELS.get(model, model)\n        ax2.plot(x, means, 'o-', color=c, lw=2,\n                 label=f'{name} ({r[\"observed_pattern\"]})')\n        ax2.fill_between(x, lo, hi, alpha=0.15, color=c)\n\n    ax2.set_xticks(x)\n    ax2.set_xticklabels(DOSE_LABELS)\n    ax2.set_xlabel('Contamination dose', fontsize=12)\n    ax2.set_ylabel('Accuracy (%)', fontsize=12)\n    ax2.set_title(f'Dose-Response with 95% Bootstrap CI — {benchmark.upper()}',\n                  fontsize=13, fontweight='bold')\n    ax2.legend(fontsize=9, loc='best')\n    ax2.grid(True, alpha=0.3)\n    plt.tight_layout()\n    p2 = Path(out_dir) / f'bootstrap_dose_response_{benchmark}.png'\n    plt.savefig(p2, dpi=150, bbox_inches='tight')\n    plt.close()\n    print(f'[INFO] Plot saved: {p2}')\n\n# ── Main ────────────────────────────────────────────────────────────\n\ndef main():\n    ap = argparse.ArgumentParser(\n        description='Bootstrap profile classification stability analysis')\n    ap.add_argument('--data-dir', required=True,\n                    help='Root dir with {model}_{dosage}/ subdirs')\n    ap.add_argument('--benchmark', default='mmlu',\n                    choices=['mmlu', 'arc_challenge'])\n    ap.add_argument('--n-bootstrap', type=int, default=10000)\n    ap.add_argument('--seed', type=int, default=42,\n                    help='RNG seed for bootstrap')\n    ap.add_argument('--seed-suffix', default='',\n                    help='Dir name suffix, e.g. \"_s123\"')\n    ap.add_argument('--output-dir', default='.',\n                    help='Where to write JSON + plots')\n    ap.add_argument('--models', nargs='*', default=None,\n                    help='Subset of model keys (default: all 5)')\n    ap.add_argument('--no-plot', action='store_true')\n    args = ap.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    rng = np.random.default_rng(args.seed)\n    model_keys = args.models or list(MODELS.keys())\n\n    print(f'=== Bootstrap Profile Stability ===')\n    print(f'Benchmark: {args.benchmark}   B={args.n_bootstrap}   '\n          f'rng_seed={args.seed}')\n    print(f'Data: {args.data_dir}   suffix=\"{args.seed_suffix}\"')\n    print()\n\n    all_data = load_all(args.data_dir, args.benchmark, args.seed_suffix,\n                        model_keys)\n    if not all_data:\n        print('[ERROR] No valid data found')\n        sys.exit(1)\n\n    n_items_set = {len(all_data[m]['d000']) for m in all_data}\n    if len(n_items_set) == 1:\n        print(f'\\nPaired bootstrap on {n_items_set.pop()} shared items')\n    else:\n        print(f'\\n[WARN] Item counts differ: {n_items_set} — '\n              f'bootstrap uses smallest common count')\n\n    print()\n    t0 = time.time()\n    results = run_bootstrap(all_data, args.n_bootstrap, rng)\n    elapsed = time.time() - t0\n    print(f'\\nBootstrap done in {elapsed:.1f}s')\n\n    threshold = None\n    if len(results) >= 3:\n        threshold = compute_threshold(results, args.n_bootstrap)\n\n    # ── Summary table ──\n    print()\n    hdr = (f'{\"Model\":<18} {\"Baseline\":>8} {\"Delta\":>10} '\n           f'{\"Pattern\":<15} {\"Stability\":>10} {\"Delta 95% CI\":>22}')\n    sep = '-' * len(hdr)\n    print('=' * len(hdr))\n    print(hdr)\n    print(sep)\n    for m in sorted(results, key=lambda m: results[m]['observed_accs']['d000'],\n                    reverse=True):\n        r = results[m]\n        ci = r['delta_ci95']\n        print(f'{MODELS.get(m,m):<18} {r[\"observed_accs\"][\"d000\"]:>7.2f}% '\n              f'{r[\"observed_delta\"]:>+9.2f}pp '\n              f'{r[\"observed_pattern\"]:<15} {r[\"stability_pct\"]:>9.1f}% '\n              f'[{ci[0]:>+7.2f}, {ci[1]:>+7.2f}]')\n    print('=' * len(hdr))\n\n    if threshold:\n        ci = threshold['ci95']\n        print(f'\\nBenefit/Harm Threshold: {threshold[\"median\"]:.1f}% '\n              f'(95% CI: [{ci[0]:.1f}, {ci[1]:.1f}])')\n        print(f'  Valid crossings: {threshold[\"n_valid\"]}/{threshold[\"n_total\"]} '\n              f'({threshold[\"n_valid\"]/threshold[\"n_total\"]*100:.1f}%)')\n\n    # ── Plots ──\n    if not args.no_plot:\n        make_plots(results, threshold, args.output_dir, args.benchmark)\n\n    # ── JSON output ──\n    output = {\n        'config': {\n            'benchmark': args.benchmark,\n            'n_bootstrap': args.n_bootstrap,\n            'seed': args.seed,\n            'data_dir': str(args.data_dir),\n        },\n        'models': {},\n        'threshold': (\n            {k: v for k, v in threshold.items() if not k.startswith('_')}\n            if threshold else None\n        ),\n    }\n    for m, r in results.items():\n        output['models'][m] = {\n            'display_name': MODELS.get(m, m),\n            'observed_pattern': r['observed_pattern'],\n            'observed_delta_pp': r['observed_delta'],\n            'observed_accs': r['observed_accs'],\n            'stability_pct': r['stability_pct'],\n            'pattern_distribution': r['pattern_distribution'],\n            'delta_mean': r['delta_mean'],\n            'delta_std': r['delta_std'],\n            'delta_ci95': r['delta_ci95'],\n        }\n\n    jp = Path(args.output_dir) / f'bootstrap_results_{args.benchmark}.json'\n    with open(jp, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f'\\n[INFO] Results saved: {jp}')\n\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 471,
      "startLine": 1,
      "totalLines": 471
    }
  }
}
```

</details>

---
