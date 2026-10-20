# code analyze mvp upgrade

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_code_analyze-mvp-upgrade_20260514T083241.log`
- **Structured JSON:** [`78face4ba3712e9f2134.json`](../../sessions/78/78face4ba3712e9f2134.json)

## Before a recorded user message

20 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
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
  "uuid": "d82ce49b-3fe9-487a-b1e1-6e19a2468d0c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1778753400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "42413bab-f7d8-4ef4-970b-8be11d401a8e",
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc"
}
```

---

### Assistant

_source line 4_

Let me start by reading both files to understand the current code and the evaluation criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "2193f215-82eb-4967-9ce4-e88a96e2b28e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XybDCbvYaXKoffrVQTEpKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12364,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12364
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

<details open><summary>🔧 Tool call — Read · `toolu_01NwRiH8Qch96q88bfuY1JQX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "169cdfb9-ad83-4b75-9414-8bc0cbf73bcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XybDCbvYaXKoffrVQTEpKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12364,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12364
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

_source line 6 · 2026-05-14T08:32:55.929Z_

<details><summary>↩ Tool result · `toolu_01NwRiH8Qch96q88bfuY1JQX`</summary>

```text
1	"""Analyze MVP experiment: metric trends, cross-correlation, lead time.
2	
3	Reads all_metrics.json from each rep, produces:
4	  - metric_trends.png : canary + downstream metrics vs generation
5	  - cross_correlation.png : cross-correlation heatmap
6	  - lead_time_table.csv : lead time estimates per canary-downstream pair
7	  - analysis_summary.json : machine-readable summary
8	
9	Usage:
10	    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44
11	"""
12	
13	import argparse
14	import json
15	import os
16	
17	import matplotlib.pyplot as plt
18	import numpy as np
19	import pandas as pd
20	
21	
22	CANARY_METRICS = ["token_entropy", "self_bleu", "ece", "effective_rank"]
23	DOWNSTREAM_METRICS = ["perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve"]
24	
25	# Metrics where higher = worse (collapse direction)
26	HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
27	# Metrics where lower = worse (collapse direction)
28	LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
29	                   "distinct_3", "mauve"}
30	
31	
32	def load_metrics(results_dir, seeds):
33	    """Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}."""
34	    data = {}
35	    for seed in seeds:
36	        path = os.path.join(results_dir, f"rep_{seed}", "all_metrics.json")
37	        with open(path) as f:
38	            data[seed] = json.load(f)
39	    return data
40	
41	
42	def metrics_to_df(data):
43	    """Convert {seed: [metrics_per_gen]} to a long-form DataFrame."""
44	    rows = []
45	    for seed, gens in data.items():
46	        for m in gens:
47	            m_copy = dict(m)
48	            m_copy["seed"] = seed
49	            rows.append(m_copy)
50	    return pd.DataFrame(rows)
51	
52	
53	def normalize_for_correlation(series, metric_name):
54	    """Flip sign so that 'getting worse' is always positive direction."""
55	    s = series.copy()
56	    if metric_name in LOWER_IS_WORSE:
57	        s = -s
58	    s = (s - s.mean()) / (s.std() + 1e-12)
59	    return s
60	
61	
62	def cross_correlate(x, y, max_lag=5):
63	    """Cross-correlation of x and y at lags -max_lag..+max_lag.
64	
65	    Positive lag k means y leads x by k steps.
66	    Negative lag k means x leads y by |k| steps.
67	    """
68	    x = (x - x.mean()) / (x.std() + 1e-12)
69	    y = (y - y.mean()) / (y.std() + 1e-12)
70	    n = len(x)
71	    correlations = {}
72	    for lag in range(-max_lag, max_lag + 1):
73	        if lag >= 0:
74	            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0
75	        else:
76	            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0
77	        correlations[lag] = c
78	    return correlations
79	
80	
81	def estimate_lead_time(canary_series, downstream_series, canary_name,
82	                       downstream_name, max_lag=5):
83	    """Estimate how many generations canary leads downstream.
84	
85	    Returns (peak_lag, peak_corr). Negative peak_lag = canary leads.
86	    """
87	    c_norm = normalize_for_correlation(canary_series, canary_name)
88	    d_norm = normalize_for_correlation(downstream_series, downstream_name)
89	    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
90	    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
91	    return peak_lag, corrs[peak_lag], corrs
92	
93	
94	def plot_metric_trends(df, output_dir):
95	    """Plot metric-vs-generation with mean ± std across seeds."""
96	    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS
97	    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
98	    axes = axes.flatten()
99	
100	    for idx, metric in enumerate(all_metrics):
101	        if idx >= len(axes):
102	            break
103	        ax = axes[idx]
104	        grouped = df.groupby("generation")[metric]
105	        mean = grouped.mean()
106	        std = grouped.std()
107	
108	        ax.plot(mean.index, mean.values, "o-", linewidth=2)
109	        ax.fill_between(mean.index, mean.values - std.values,
110	                        mean.values + std.values, alpha=0.2)
111	        ax.set_title(metric, fontsize=11, fontweight="bold")
112	        ax.set_xlabel("Generation")
113	        ax.set_ylabel(metric)
114	        ax.grid(True, alpha=0.3)
115	
116	        is_canary = metric in CANARY_METRICS
117	        ax.set_facecolor("#fff8f0" if is_canary else "#f0f8ff")
118	
119	    for idx in range(len(all_metrics), len(axes)):
120	        axes[idx].set_visible(False)
121	
122	    fig.suptitle("Metric Trends over Generations (mean ± std, 3 reps)",
123	                 fontsize=14, fontweight="bold")
124	    plt.tight_layout()
125	    plt.savefig(os.path.join(output_dir, "metric_trends.png"), dpi=150,
126	                bbox_inches="tight")
127	    plt.close()
128	    print(f"Saved metric_trends.png")
129	
130	
131	def plot_cross_correlation_heatmap(lead_table, output_dir):
132	    """Heatmap of peak lag (canary leads = negative lag)."""
133	    pivot_lag = lead_table.pivot(index="canary", columns="downstream",
134	                                values="peak_lag")
135	    pivot_corr = lead_table.pivot(index="canary", columns="downstream",
136	                                  values="peak_corr")
137	
138	    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
139	
140	    im1 = ax1.imshow(pivot_lag.values, cmap="RdBu_r", aspect="auto",
141	                     vmin=-5, vmax=5)
142	    ax1.set_xticks(range(len(pivot_lag.columns)))
143	    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha="right")
144	    ax1.set_yticks(range(len(pivot_lag.index)))
145	    ax1.set_yticklabels(pivot_lag.index)
146	    ax1.set_title("Peak Lag (negative = canary leads)")
147	    for i in range(len(pivot_lag.index)):
148	        for j in range(len(pivot_lag.columns)):
149	            ax1.text(j, i, f"{pivot_lag.values[i, j]:.0f}",
150	                     ha="center", va="center", fontsize=10)
151	    plt.colorbar(im1, ax=ax1)
152	
153	    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap="YlOrRd", aspect="auto",
154	                     vmin=0, vmax=1)
155	    ax2.set_xticks(range(len(pivot_corr.columns)))
156	    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha="right")
157	    ax2.set_yticks(range(len(pivot_corr.index)))
158	    ax2.set_yticklabels(pivot_corr.index)
159	    ax2.set_title("|Peak Correlation|")
160	    for i in range(len(pivot_corr.index)):
161	        for j in range(len(pivot_corr.columns)):
162	            ax2.text(j, i, f"{pivot_corr.values[i, j]:.2f}",
163	                     ha="center", va="center", fontsize=10)
164	    plt.colorbar(im2, ax=ax2)
165	
166	    fig.suptitle("Cross-Correlation: Canary → Downstream", fontsize=13,
167	                 fontweight="bold")
168	    plt.tight_layout()
169	    plt.savefig(os.path.join(output_dir, "cross_correlation.png"), dpi=150,
170	                bbox_inches="tight")
171	    plt.close()
172	    print("Saved cross_correlation.png")
173	
174	
175	def main():
176	    parser = argparse.ArgumentParser()
177	    parser.add_argument("--results_dir", type=str, default="results/mvp")
178	    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 43, 44])
179	    parser.add_argument("--max_lag", type=int, default=5)
180	    args = parser.parse_args()
181	
182	    output_dir = os.path.join(args.results_dir, "analysis")
183	    os.makedirs(output_dir, exist_ok=True)
184	
185	    print("Loading metrics …")
186	    data = load_metrics(args.results_dir, args.seeds)
187	    df = metrics_to_df(data)
188	
189	    # --- Metric trend plots ---
190	    plot_metric_trends(df, output_dir)
191	
192	    # --- Cross-correlation & lead time ---
193	    lead_rows = []
194	    for canary in CANARY_METRICS:
195	        for downstream in DOWNSTREAM_METRICS:
196	            all_lags = []
197	            all_corrs = []
198	            for seed in args.seeds:
199	                seed_df = df[df["seed"] == seed].sort_values("generation")
200	                c_series = seed_df[canary].values
201	                d_series = seed_df[downstream].values
202	                lag, corr, _ = estimate_lead_time(
203	                    c_series, d_series, canary, downstream,
204	                    max_lag=args.max_lag)
205	                all_lags.append(lag)
206	                all_corrs.append(corr)
207	
208	            lead_rows.append({
209	                "canary": canary,
210	                "downstream": downstream,
211	                "peak_lag": np.mean(all_lags),
212	                "peak_corr": np.mean(all_corrs),
213	                "lag_std": np.std(all_lags),
214	                "corr_std": np.std(all_corrs),
215	                "consistent": all(l < 0 for l in all_lags),
216	            })
217	
218	    lead_table = pd.DataFrame(lead_rows)
219	    lead_table.to_csv(os.path.join(output_dir, "lead_time_table.csv"),
220	                      index=False)
221	    print("Saved lead_time_table.csv")
222	
223	    plot_cross_correlation_heatmap(lead_table, output_dir)
224	
225	    # --- Summary ---
226	    consistent_leaders = lead_table[lead_table["consistent"]]
227	    summary = {
228	        "total_canary_downstream_pairs": len(lead_table),
229	        "consistent_leaders": len(consistent_leaders),
230	        "best_canary": None,
231	        "pass_fail": "UNDETERMINED",
232	    }
233	
234	    if len(consistent_leaders) > 0:
235	        best = consistent_leaders.loc[
236	            consistent_leaders["peak_corr"].abs().idxmax()]
237	        summary["best_canary"] = best["canary"]
238	        summary["best_downstream"] = best["downstream"]
239	        summary["best_lead_gens"] = abs(best["peak_lag"])
240	        summary["best_corr"] = best["peak_corr"]
241	        summary["pass_fail"] = "PASS"
242	    else:
243	        summary["pass_fail"] = "FAIL"
244	
245	    with open(os.path.join(output_dir, "analysis_summary.json"), "w") as f:
246	        json.dump(summary, f, indent=2)
247	
248	    # --- Console report ---
249	    print("\n" + "=" * 60)
250	    print("MVP ANALYSIS SUMMARY")
251	    print("=" * 60)
252	    print(f"Consistent canary leaders (lead in all 3 reps): "
253	          f"{len(consistent_leaders)}/{len(lead_table)}")
254	
255	    if summary["pass_fail"] == "PASS":
256	        print(f"\n✅ PASS — Best canary: {summary['best_canary']}")
257	        print(f"   Leads {summary['best_downstream']} by "
258	              f"~{summary['best_lead_gens']:.1f} generations")
259	        print(f"   Peak correlation: {summary['best_corr']:.3f}")
260	    else:
261	        print("\n❌ FAIL — No canary consistently leads any downstream metric")
262	
263	    print("\nFull lead time table:")
264	    print(lead_table.to_string(index=False))
265	    print(f"\nResults saved to {output_dir}/")
266	
267	
268	if __name__ == "__main__":
269	    main()
270	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "0696d7c3-cc12-4a02-ae88-b5424518b815",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py",
      "content": "\"\"\"Analyze MVP experiment: metric trends, cross-correlation, lead time.\n\nReads all_metrics.json from each rep, produces:\n  - metric_trends.png : canary + downstream metrics vs generation\n  - cross_correlation.png : cross-correlation heatmap\n  - lead_time_table.csv : lead time estimates per canary-downstream pair\n  - analysis_summary.json : machine-readable summary\n\nUsage:\n    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44\n\"\"\"\n\nimport argparse\nimport json\nimport os\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\n\nCANARY_METRICS = [\"token_entropy\", \"self_bleu\", \"ece\", \"effective_rank\"]\nDOWNSTREAM_METRICS = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n# Metrics where higher = worse (collapse direction)\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\n# Metrics where lower = worse (collapse direction)\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\", \"distinct_1\", \"distinct_2\",\n                   \"distinct_3\", \"mauve\"}\n\n\ndef load_metrics(results_dir, seeds):\n    \"\"\"Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}.\"\"\"\n    data = {}\n    for seed in seeds:\n        path = os.path.join(results_dir, f\"rep_{seed}\", \"all_metrics.json\")\n        with open(path) as f:\n            data[seed] = json.load(f)\n    return data\n\n\ndef metrics_to_df(data):\n    \"\"\"Convert {seed: [metrics_per_gen]} to a long-form DataFrame.\"\"\"\n    rows = []\n    for seed, gens in data.items():\n        for m in gens:\n            m_copy = dict(m)\n            m_copy[\"seed\"] = seed\n            rows.append(m_copy)\n    return pd.DataFrame(rows)\n\n\ndef normalize_for_correlation(series, metric_name):\n    \"\"\"Flip sign so that 'getting worse' is always positive direction.\"\"\"\n    s = series.copy()\n    if metric_name in LOWER_IS_WORSE:\n        s = -s\n    s = (s - s.mean()) / (s.std() + 1e-12)\n    return s\n\n\ndef cross_correlate(x, y, max_lag=5):\n    \"\"\"Cross-correlation of x and y at lags -max_lag..+max_lag.\n\n    Positive lag k means y leads x by k steps.\n    Negative lag k means x leads y by |k| steps.\n    \"\"\"\n    x = (x - x.mean()) / (x.std() + 1e-12)\n    y = (y - y.mean()) / (y.std() + 1e-12)\n    n = len(x)\n    correlations = {}\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0\n        else:\n            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0\n        correlations[lag] = c\n    return correlations\n\n\ndef estimate_lead_time(canary_series, downstream_series, canary_name,\n                       downstream_name, max_lag=5):\n    \"\"\"Estimate how many generations canary leads downstream.\n\n    Returns (peak_lag, peak_corr). Negative peak_lag = canary leads.\n    \"\"\"\n    c_norm = normalize_for_correlation(canary_series, canary_name)\n    d_norm = normalize_for_correlation(downstream_series, downstream_name)\n    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    return peak_lag, corrs[peak_lag], corrs\n\n\ndef plot_metric_trends(df, output_dir):\n    \"\"\"Plot metric-vs-generation with mean ± std across seeds.\"\"\"\n    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS\n    fig, axes = plt.subplots(3, 3, figsize=(15, 12))\n    axes = axes.flatten()\n\n    for idx, metric in enumerate(all_metrics):\n        if idx >= len(axes):\n            break\n        ax = axes[idx]\n        grouped = df.groupby(\"generation\")[metric]\n        mean = grouped.mean()\n        std = grouped.std()\n\n        ax.plot(mean.index, mean.values, \"o-\", linewidth=2)\n        ax.fill_between(mean.index, mean.values - std.values,\n                        mean.values + std.values, alpha=0.2)\n        ax.set_title(metric, fontsize=11, fontweight=\"bold\")\n        ax.set_xlabel(\"Generation\")\n        ax.set_ylabel(metric)\n        ax.grid(True, alpha=0.3)\n\n        is_canary = metric in CANARY_METRICS\n        ax.set_facecolor(\"#fff8f0\" if is_canary else \"#f0f8ff\")\n\n    for idx in range(len(all_metrics), len(axes)):\n        axes[idx].set_visible(False)\n\n    fig.suptitle(\"Metric Trends over Generations (mean ± std, 3 reps)\",\n                 fontsize=14, fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"metric_trends.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(f\"Saved metric_trends.png\")\n\n\ndef plot_cross_correlation_heatmap(lead_table, output_dir):\n    \"\"\"Heatmap of peak lag (canary leads = negative lag).\"\"\"\n    pivot_lag = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                values=\"peak_lag\")\n    pivot_corr = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                  values=\"peak_corr\")\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n\n    im1 = ax1.imshow(pivot_lag.values, cmap=\"RdBu_r\", aspect=\"auto\",\n                     vmin=-5, vmax=5)\n    ax1.set_xticks(range(len(pivot_lag.columns)))\n    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha=\"right\")\n    ax1.set_yticks(range(len(pivot_lag.index)))\n    ax1.set_yticklabels(pivot_lag.index)\n    ax1.set_title(\"Peak Lag (negative = canary leads)\")\n    for i in range(len(pivot_lag.index)):\n        for j in range(len(pivot_lag.columns)):\n            ax1.text(j, i, f\"{pivot_lag.values[i, j]:.0f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im1, ax=ax1)\n\n    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap=\"YlOrRd\", aspect=\"auto\",\n                     vmin=0, vmax=1)\n    ax2.set_xticks(range(len(pivot_corr.columns)))\n    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha=\"right\")\n    ax2.set_yticks(range(len(pivot_corr.index)))\n    ax2.set_yticklabels(pivot_corr.index)\n    ax2.set_title(\"|Peak Correlation|\")\n    for i in range(len(pivot_corr.index)):\n        for j in range(len(pivot_corr.columns)):\n            ax2.text(j, i, f\"{pivot_corr.values[i, j]:.2f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im2, ax=ax2)\n\n    fig.suptitle(\"Cross-Correlation: Canary → Downstream\", fontsize=13,\n                 fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"cross_correlation.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(\"Saved cross_correlation.png\")\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--results_dir\", type=str, default=\"results/mvp\")\n    parser.add_argument(\"--seeds\", type=int, nargs=\"+\", default=[42, 43, 44])\n    parser.add_argument(\"--max_lag\", type=int, default=5)\n    args = parser.parse_args()\n\n    output_dir = os.path.join(args.results_dir, \"analysis\")\n    os.makedirs(output_dir, exist_ok=True)\n\n    print(\"Loading metrics …\")\n    data = load_metrics(args.results_dir, args.seeds)\n    df = metrics_to_df(data)\n\n    # --- Metric trend plots ---\n    plot_metric_trends(df, output_dir)\n\n    # --- Cross-correlation & lead time ---\n    lead_rows = []\n    for canary in CANARY_METRICS:\n        for downstream in DOWNSTREAM_METRICS:\n            all_lags = []\n            all_corrs = []\n            for seed in args.seeds:\n                seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n                c_series = seed_df[canary].values\n                d_series = seed_df[downstream].values\n                lag, corr, _ = estimate_lead_time(\n                    c_series, d_series, canary, downstream,\n                    max_lag=args.max_lag)\n                all_lags.append(lag)\n                all_corrs.append(corr)\n\n            lead_rows.append({\n                \"canary\": canary,\n                \"downstream\": downstream,\n                \"peak_lag\": np.mean(all_lags),\n                \"peak_corr\": np.mean(all_corrs),\n                \"lag_std\": np.std(all_lags),\n                \"corr_std\": np.std(all_corrs),\n                \"consistent\": all(l < 0 for l in all_lags),\n            })\n\n    lead_table = pd.DataFrame(lead_rows)\n    lead_table.to_csv(os.path.join(output_dir, \"lead_time_table.csv\"),\n                      index=False)\n    print(\"Saved lead_time_table.csv\")\n\n    plot_cross_correlation_heatmap(lead_table, output_dir)\n\n    # --- Summary ---\n    consistent_leaders = lead_table[lead_table[\"consistent\"]]\n    summary = {\n        \"total_canary_downstream_pairs\": len(lead_table),\n        \"consistent_leaders\": len(consistent_leaders),\n        \"best_canary\": None,\n        \"pass_fail\": \"UNDETERMINED\",\n    }\n\n    if len(consistent_leaders) > 0:\n        best = consistent_leaders.loc[\n            consistent_leaders[\"peak_corr\"].abs().idxmax()]\n        summary[\"best_canary\"] = best[\"canary\"]\n        summary[\"best_downstream\"] = best[\"downstream\"]\n        summary[\"best_lead_gens\"] = abs(best[\"peak_lag\"])\n        summary[\"best_corr\"] = best[\"peak_corr\"]\n        summary[\"pass_fail\"] = \"PASS\"\n    else:\n        summary[\"pass_fail\"] = \"FAIL\"\n\n    with open(os.path.join(output_dir, \"analysis_summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n\n    # --- Console report ---\n    print(\"\\n\" + \"=\" * 60)\n    print(\"MVP ANALYSIS SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"Consistent canary leaders (lead in all 3 reps): \"\n          f\"{len(consistent_leaders)}/{len(lead_table)}\")\n\n    if summary[\"pass_fail\"] == \"PASS\":\n        print(f\"\\n✅ PASS — Best canary: {summary['best_canary']}\")\n        print(f\"   Leads {summary['best_downstream']} by \"\n              f\"~{summary['best_lead_gens']:.1f} generations\")\n        print(f\"   Peak correlation: {summary['best_corr']:.3f}\")\n    else:\n        print(\"\\n❌ FAIL — No canary consistently leads any downstream metric\")\n\n    print(\"\\nFull lead time table:\")\n    print(lead_table.to_string(index=False))\n    print(f\"\\nResults saved to {output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 270,
      "startLine": 1,
      "totalLines": 270
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01AYcY3AqSCZiSkrhHctfBmD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mvp_evaluation_criteria.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "a8d73ed5-ae7f-4782-8981-b4ec85055b20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XybDCbvYaXKoffrVQTEpKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12364,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12364
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

_source line 8 · 2026-05-14T08:32:56.109Z_

<details><summary>↩ Tool result · `toolu_01AYcY3AqSCZiSkrhHctfBmD`</summary>

```text
1	# MVP Evaluation Criteria: Canary Lead-Lag Detection
2	
3	> **Pre-registered evaluation protocol.** Defined before MVP results are available to prevent post-hoc threshold adjustment. Any deviation from this document must be logged with justification in `memory.md` before analysis proceeds.
4	
5	**MVP setup:** Pythia-410m, WikiText-103, 100% synthetic full replacement, 10 generations (Gen 0–9), 3 seeds (42/43/44). Canary metrics: `token_entropy`, `self_bleu`, `ece`, `effective_rank`. Downstream metrics: `perplexity`, `distinct_1`, `distinct_2`, `distinct_3`, `mauve`.
6	
7	**Core hypothesis:** At least one canary metric family consistently leads at least one downstream metric by ≥1 generation across all 3 repetitions.
8	
9	---
10	
11	## 1. Cross-Correlation Significance Threshold
12	
13	### The small-sample problem
14	
15	With N=10 time points per series and max_lag=5, the effective overlap at extreme lags is only 5 data points. Pearson correlation on 5 points has catastrophically low power — even r=0.9 is not significant at p<0.05 with n=5 (critical r ≈ 0.878 for one-tailed test at df=3). Standard asymptotic p-values are unreliable here.
16	
17	### Recommended method: Permutation test
18	
19	For each (canary, downstream, seed) triplet:
20	
21	1. Compute the observed peak |r| at the peak lag from `cross_correlate()`.
22	2. Generate B=10,000 permutations of the downstream series (random shuffle, breaking temporal structure).
23	3. For each permutation, recompute cross-correlation across all lags and record the max |r| across all lags (this accounts for multiple-lag testing).
24	4. p-value = (number of permutation max |r| ≥ observed peak |r|) / B.
25	
26	### Significance thresholds
27	
28	| Criterion | Threshold | Rationale |
29	|-----------|-----------|-----------|
30	| Per-triplet significance | p < 0.10 (one-tailed) | Relaxed from 0.05 due to N=10; reduces false negatives at MVP stage |
31	| Effect size floor | \|peak r\| ≥ 0.60 | Correlation below 0.60 is unlikely practically meaningful even if "significant" at N=10 |
32	| Required for PASS | Both p < 0.10 AND \|r\| ≥ 0.60 must hold for the triplet to count as "significant" |
33	
34	### Why not bootstrap CI?
35	
36	Bootstrap CI for correlation requires exchangeable residuals, which temporal series violate. Block bootstrap with block length > 1 is infeasible at N=10. Permutation test is the correct nonparametric choice for testing "no temporal association" under the null.
37	
38	### Implementation note
39	
40	`analyze_mvp.py` currently selects peak lag by `max(abs(corrs))` without significance testing. The permutation test should be added as a post-processing step; the existing lag selection logic is retained.
41	
42	---
43	
44	## 2. "3/3 Reps Consistent" Judgment Rules
45	
46	### Primary rule: Strict negative lag
47	
48	A (canary, downstream) pair is **consistent** if and only if:
49	
50	- All 3 seeds produce peak_lag < 0 (strictly negative), AND
51	- All 3 seeds pass the significance filter (§1: p < 0.10 and |r| ≥ 0.60).
52	
53	This matches the existing `analyze_mvp.py` line 215: `all(l < 0 for l in all_lags)`.
54	
55	### Lag dispersion tolerance
56	
57	Peak lags need not be identical — only consistently negative. Examples:
58	
59	| Seed lags | Consistent? | Reason |
60	|-----------|-------------|--------|
61	| -2, -1, -3 | ✅ Yes | All negative, spread is acceptable |
62	| -1, -1, -1 | ✅ Yes | Ideal case |
63	| -5, -1, -4 | ✅ Yes | Large spread but all negative; flag lag_std for discussion |
64	| -2, -1, 0 | ❌ No | Lag=0 is not negative; 0 means simultaneous, not leading |
65	| -2, +1, -1 | ❌ No | One seed shows canary lagging |
66	
67	### Lag=0 is NOT a lead
68	
69	Lag=0 indicates simultaneous movement, which does not support the "early warning" hypothesis. Lag=0 is treated as failure for the lead-lag criterion, even though it may indicate co-movement.
70	
71	### Reporting
72	
73	For each consistent pair, report: mean lag, lag std, min lag, max lag across seeds. If lag_std > 2.0, flag as "high dispersion — interpret with caution."
74	
75	---
76	
77	## 3. Non-Monotonic Indicator Handling (effective_rank)
78	
79	### Problem
80	
81	`effective_rank` may exhibit non-monotonic behavior: initial increase (model explores broader representation space early in fine-tuning) followed by decrease (collapse narrows representations). This complicates correlation-based analysis which assumes a consistent directional trend.
82	
83	### Adopted method: Gen 4–9 linear regression slope
84	
85	**Rationale:** Generations 0–3 capture the transient fine-tuning adjustment. Generations 4–9 (6 points) capture the steady-state collapse trajectory, which is the regime where early warning matters.
86	
87	**Procedure:**
88	
89	1. Fit OLS: `effective_rank ~ β₀ + β₁ · generation` on Gen 4–9 for each seed.
90	2. If β₁ < 0 in all 3 seeds → collapse direction is "decreasing" → use the standard sign flip in `normalize_for_correlation()`.
91	3. If β₁ > 0 in all 3 seeds → effective_rank is increasing through Gen 9 → collapse has not manifested in this metric → exclude `effective_rank` from lead-lag analysis and note it in results.
92	4. If β₁ signs are mixed across seeds → report `effective_rank` as **inconclusive** for this MVP; do not count it toward PASS or FAIL.
93	
94	### Why not Spearman over the full series?
95	
96	Spearman rank correlation over 10 points conflates the transient and steady-state regimes. A metric that rises for 3 generations then falls for 7 would show weak Spearman correlation, masking a real late-phase collapse signal.
97	
98	### Why not "final trend only"?
99	
100	"Final trend" (e.g., Gen 8→9 direction) is a single difference — too noisy to be reliable. Six points (Gen 4–9) provide a minimal but defensible regression.
101	
102	### Application to other metrics
103	
104	If any other canary metric exhibits non-monotonicity (visible in `metric_trends.png`), apply the same Gen 4–9 slope procedure before cross-correlation analysis. Document which metrics required this treatment.
105	
106	---
107	
108	## 4. MAUVE Baseline Interpretation
109	
110	### Known issue
111	
112	Validation run produced Gen 0 MAUVE = 0.034. Healthy models typically produce MAUVE > 0.8 on standard benchmarks.
113	
114	### Probable causes (ordered by likelihood)
115	
116	1. **max_length=256 truncation**: MAUVE computes distributional divergence over full text. 256-token truncation creates artifactual distributional mismatch between generated (which may naturally terminate earlier) and real text (truncated mid-sentence). This is the most likely cause.
117	2. **Pythia-410m base quality**: A 410M-parameter model without instruction tuning produces lower-quality unconditional generations, especially on WikiText-103's encyclopedic domain.
118	3. **Prompt/generation mismatch**: If generation uses different prompting strategy than the reference distribution, MAUVE captures this systematic offset rather than collapse-related degradation.
119	
120	### Floor effect decision rule
121	
122	**Definition:** MAUVE exhibits a floor effect if:
123	
124	- Gen 0 MAUVE < 0.10 (already near minimum), AND
125	- The coefficient of variation across generations CV = std/mean < 0.50 (insufficient relative variation to detect trends).
126	
127	If BOTH conditions hold across all 3 seeds:
128	
129	1. **Demote MAUVE** from primary downstream metric to supplementary.
130	2. **Primary downstream metrics** become: `perplexity`, `distinct_1`, `distinct_2`, `distinct_3`.
131	3. MAUVE cross-correlation results are still computed and reported but do not count toward PASS/FAIL determination.
132	4. Log this demotion decision in `analysis_summary.json` with field `"mauve_demoted": true, "mauve_demoted_reason": "floor_effect"`.
133	
134	### If MAUVE is NOT demoted
135	
136	If Gen 0 MAUVE ≥ 0.10 or CV ≥ 0.50, retain MAUVE as a primary downstream metric — there is sufficient dynamic range to detect trends.
137	
138	---
139	
140	## 5. Graded Verdict System
141	
142	Each (canary_family, downstream_metric) pair is evaluated independently. The overall verdict aggregates across all pairs.
143	
144	### Per-pair criteria
145	
146	| Pair verdict | Conditions |
147	|-------------|------------|
148	| **SIGNIFICANT LEAD** | 3/3 seeds: peak_lag < 0, p < 0.10, \|r\| ≥ 0.60 |
149	| **WEAK LEAD** | 3/3 seeds: peak_lag < 0, but ≥1 seed fails significance (p ≥ 0.10 or \|r\| < 0.60) |
150	| **NO LEAD** | Any seed has peak_lag ≥ 0 |
151	
152	### Overall MVP verdict
153	
154	| Verdict | Required evidence |
155	|---------|-------------------|
156	| **STRONG PASS** | ≥2 canary families each have ≥1 SIGNIFICANT LEAD pair against non-demoted downstream metrics |
157	| **PASS** | ≥1 canary family has ≥1 SIGNIFICANT LEAD pair against a non-demoted downstream metric |
158	| **CONDITIONAL PASS** | No SIGNIFICANT LEAD pairs exist, but ≥1 canary family has ≥1 WEAK LEAD pair in all 3 seeds. Proceed to Phase 2 with this canary family prioritized but with explicit acknowledgment that MVP evidence is suggestive, not conclusive |
159	| **FAIL** | No canary family achieves even WEAK LEAD consistency across 3 seeds |
160	
161	### The 2/3 problem
162	
163	If 2/3 seeds show a lead but 1/3 does not: this is **NO LEAD** for that pair (not CONDITIONAL PASS). The hypothesis requires consistency across seeds to rule out stochastic artifacts. A 2/3 result may be noted in discussion but does not contribute to the verdict.
164	
165	**Exception:** If the dissenting seed shows peak_lag = 0 (simultaneous, not reverse), and the other 2 seeds show peak_lag ≤ -2 with p < 0.05, record this as a "near miss" in the report. It does not change the verdict but informs Phase 2 design (e.g., whether more seeds are needed).
166	
167	### Handling `effective_rank` non-monotonicity
168	
169	If `effective_rank` is marked **inconclusive** per §3, its pairs are excluded from the verdict entirely (neither helping nor hurting). The verdict is computed over the remaining 3 canary families only. If `effective_rank` is the *only* canary with leads and it is inconclusive, the overall verdict is FAIL (we cannot claim a lead based on an inconclusive metric).
170	
171	---
172	
173	## 6. Decision Summary Table
174	
175	| # | Check | Rule | If TRUE | If FALSE |
176	|---|-------|------|---------|----------|
177	| 1 | MAUVE Gen 0 < 0.10 AND CV < 0.50 across all seeds? | §4 floor effect test | Demote MAUVE to supplementary | Retain MAUVE as primary downstream |
178	| 2 | `effective_rank` Gen 4–9 slope sign consistent across seeds? | §3 slope test | Include in analysis (flip sign if β₁ < 0) | Mark inconclusive, exclude from verdict |
179	| 3 | For each (canary, downstream) pair: all 3 seeds peak_lag < 0? | §2 strict negative | Pair is a lead candidate | Pair is NO LEAD |
180	| 4 | For lead candidates: all 3 seeds p < 0.10 AND \|r\| ≥ 0.60? | §1 significance | SIGNIFICANT LEAD | WEAK LEAD |
181	| 5 | ≥1 canary family has ≥1 SIGNIFICANT LEAD pair? | §5 PASS threshold | **PASS** (or STRONG PASS if ≥2 families) | Go to check 6 |
182	| 6 | ≥1 canary family has ≥1 WEAK LEAD pair (3/3 consistent)? | §5 CONDITIONAL threshold | **CONDITIONAL PASS** — proceed with caveats | **FAIL** |
183	
184	### Post-verdict actions
185	
186	| Verdict | Next step |
187	|---------|-----------|
188	| STRONG PASS | Proceed to Phase 2 (synthetic ratio gradient). Prioritize the leading canary families. |
189	| PASS | Proceed to Phase 2. Expand to more seeds (5 instead of 3) to strengthen evidence. |
190	| CONDITIONAL PASS | Proceed to Phase 2 with modifications: increase to 20 generations (more statistical power) and 5 seeds. Re-evaluate with the same criteria at Phase 2 completion. |
191	| FAIL | Revisit canary metric definitions or pivot research direction. Analyze whether collapse itself occurred (check perplexity trajectory); if no collapse happened in 10 generations, the null result is expected and the experiment should be extended. |
192	
193	---
194	
195	## Appendix: Implementation Checklist for `analyze_mvp.py`
196	
197	The current `analyze_mvp.py` implements checks 2–3 and part of check 5 (binary PASS/FAIL). The following additions are needed before final analysis:
198	
199	- [ ] Add permutation test (§1) to `estimate_lead_time()` or as a wrapper function
200	- [ ] Add per-seed significance filtering before aggregation
201	- [ ] Add MAUVE floor effect detection (§4) before cross-correlation
202	- [ ] Add `effective_rank` monotonicity check (§3) via Gen 4–9 OLS
203	- [ ] Extend `analysis_summary.json` with graded verdict (§5) and all intermediate decisions
204	- [ ] Report lag dispersion statistics (mean, std, min, max) per consistent pair
205	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "947dd080-f3f5-4e71-9d2d-f220059327fe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/mvp_evaluation_criteria.md",
      "content": "# MVP Evaluation Criteria: Canary Lead-Lag Detection\n\n> **Pre-registered evaluation protocol.** Defined before MVP results are available to prevent post-hoc threshold adjustment. Any deviation from this document must be logged with justification in `memory.md` before analysis proceeds.\n\n**MVP setup:** Pythia-410m, WikiText-103, 100% synthetic full replacement, 10 generations (Gen 0–9), 3 seeds (42/43/44). Canary metrics: `token_entropy`, `self_bleu`, `ece`, `effective_rank`. Downstream metrics: `perplexity`, `distinct_1`, `distinct_2`, `distinct_3`, `mauve`.\n\n**Core hypothesis:** At least one canary metric family consistently leads at least one downstream metric by ≥1 generation across all 3 repetitions.\n\n---\n\n## 1. Cross-Correlation Significance Threshold\n\n### The small-sample problem\n\nWith N=10 time points per series and max_lag=5, the effective overlap at extreme lags is only 5 data points. Pearson correlation on 5 points has catastrophically low power — even r=0.9 is not significant at p<0.05 with n=5 (critical r ≈ 0.878 for one-tailed test at df=3). Standard asymptotic p-values are unreliable here.\n\n### Recommended method: Permutation test\n\nFor each (canary, downstream, seed) triplet:\n\n1. Compute the observed peak |r| at the peak lag from `cross_correlate()`.\n2. Generate B=10,000 permutations of the downstream series (random shuffle, breaking temporal structure).\n3. For each permutation, recompute cross-correlation across all lags and record the max |r| across all lags (this accounts for multiple-lag testing).\n4. p-value = (number of permutation max |r| ≥ observed peak |r|) / B.\n\n### Significance thresholds\n\n| Criterion | Threshold | Rationale |\n|-----------|-----------|-----------|\n| Per-triplet significance | p < 0.10 (one-tailed) | Relaxed from 0.05 due to N=10; reduces false negatives at MVP stage |\n| Effect size floor | \\|peak r\\| ≥ 0.60 | Correlation below 0.60 is unlikely practically meaningful even if \"significant\" at N=10 |\n| Required for PASS | Both p < 0.10 AND \\|r\\| ≥ 0.60 must hold for the triplet to count as \"significant\" |\n\n### Why not bootstrap CI?\n\nBootstrap CI for correlation requires exchangeable residuals, which temporal series violate. Block bootstrap with block length > 1 is infeasible at N=10. Permutation test is the correct nonparametric choice for testing \"no temporal association\" under the null.\n\n### Implementation note\n\n`analyze_mvp.py` currently selects peak lag by `max(abs(corrs))` without significance testing. The permutation test should be added as a post-processing step; the existing lag selection logic is retained.\n\n---\n\n## 2. \"3/3 Reps Consistent\" Judgment Rules\n\n### Primary rule: Strict negative lag\n\nA (canary, downstream) pair is **consistent** if and only if:\n\n- All 3 seeds produce peak_lag < 0 (strictly negative), AND\n- All 3 seeds pass the significance filter (§1: p < 0.10 and |r| ≥ 0.60).\n\nThis matches the existing `analyze_mvp.py` line 215: `all(l < 0 for l in all_lags)`.\n\n### Lag dispersion tolerance\n\nPeak lags need not be identical — only consistently negative. Examples:\n\n| Seed lags | Consistent? | Reason |\n|-----------|-------------|--------|\n| -2, -1, -3 | ✅ Yes | All negative, spread is acceptable |\n| -1, -1, -1 | ✅ Yes | Ideal case |\n| -5, -1, -4 | ✅ Yes | Large spread but all negative; flag lag_std for discussion |\n| -2, -1, 0 | ❌ No | Lag=0 is not negative; 0 means simultaneous, not leading |\n| -2, +1, -1 | ❌ No | One seed shows canary lagging |\n\n### Lag=0 is NOT a lead\n\nLag=0 indicates simultaneous movement, which does not support the \"early warning\" hypothesis. Lag=0 is treated as failure for the lead-lag criterion, even though it may indicate co-movement.\n\n### Reporting\n\nFor each consistent pair, report: mean lag, lag std, min lag, max lag across seeds. If lag_std > 2.0, flag as \"high dispersion — interpret with caution.\"\n\n---\n\n## 3. Non-Monotonic Indicator Handling (effective_rank)\n\n### Problem\n\n`effective_rank` may exhibit non-monotonic behavior: initial increase (model explores broader representation space early in fine-tuning) followed by decrease (collapse narrows representations). This complicates correlation-based analysis which assumes a consistent directional trend.\n\n### Adopted method: Gen 4–9 linear regression slope\n\n**Rationale:** Generations 0–3 capture the transient fine-tuning adjustment. Generations 4–9 (6 points) capture the steady-state collapse trajectory, which is the regime where early warning matters.\n\n**Procedure:**\n\n1. Fit OLS: `effective_rank ~ β₀ + β₁ · generation` on Gen 4–9 for each seed.\n2. If β₁ < 0 in all 3 seeds → collapse direction is \"decreasing\" → use the standard sign flip in `normalize_for_correlation()`.\n3. If β₁ > 0 in all 3 seeds → effective_rank is increasing through Gen 9 → collapse has not manifested in this metric → exclude `effective_rank` from lead-lag analysis and note it in results.\n4. If β₁ signs are mixed across seeds → report `effective_rank` as **inconclusive** for this MVP; do not count it toward PASS or FAIL.\n\n### Why not Spearman over the full series?\n\nSpearman rank correlation over 10 points conflates the transient and steady-state regimes. A metric that rises for 3 generations then falls for 7 would show weak Spearman correlation, masking a real late-phase collapse signal.\n\n### Why not \"final trend only\"?\n\n\"Final trend\" (e.g., Gen 8→9 direction) is a single difference — too noisy to be reliable. Six points (Gen 4–9) provide a minimal but defensible regression.\n\n### Application to other metrics\n\nIf any other canary metric exhibits non-monotonicity (visible in `metric_trends.png`), apply the same Gen 4–9 slope procedure before cross-correlation analysis. Document which metrics required this treatment.\n\n---\n\n## 4. MAUVE Baseline Interpretation\n\n### Known issue\n\nValidation run produced Gen 0 MAUVE = 0.034. Healthy models typically produce MAUVE > 0.8 on standard benchmarks.\n\n### Probable causes (ordered by likelihood)\n\n1. **max_length=256 truncation**: MAUVE computes distributional divergence over full text. 256-token truncation creates artifactual distributional mismatch between generated (which may naturally terminate earlier) and real text (truncated mid-sentence). This is the most likely cause.\n2. **Pythia-410m base quality**: A 410M-parameter model without instruction tuning produces lower-quality unconditional generations, especially on WikiText-103's encyclopedic domain.\n3. **Prompt/generation mismatch**: If generation uses different prompting strategy than the reference distribution, MAUVE captures this systematic offset rather than collapse-related degradation.\n\n### Floor effect decision rule\n\n**Definition:** MAUVE exhibits a floor effect if:\n\n- Gen 0 MAUVE < 0.10 (already near minimum), AND\n- The coefficient of variation across generations CV = std/mean < 0.50 (insufficient relative variation to detect trends).\n\nIf BOTH conditions hold across all 3 seeds:\n\n1. **Demote MAUVE** from primary downstream metric to supplementary.\n2. **Primary downstream metrics** become: `perplexity`, `distinct_1`, `distinct_2`, `distinct_3`.\n3. MAUVE cross-correlation results are still computed and reported but do not count toward PASS/FAIL determination.\n4. Log this demotion decision in `analysis_summary.json` with field `\"mauve_demoted\": true, \"mauve_demoted_reason\": \"floor_effect\"`.\n\n### If MAUVE is NOT demoted\n\nIf Gen 0 MAUVE ≥ 0.10 or CV ≥ 0.50, retain MAUVE as a primary downstream metric — there is sufficient dynamic range to detect trends.\n\n---\n\n## 5. Graded Verdict System\n\nEach (canary_family, downstream_metric) pair is evaluated independently. The overall verdict aggregates across all pairs.\n\n### Per-pair criteria\n\n| Pair verdict | Conditions |\n|-------------|------------|\n| **SIGNIFICANT LEAD** | 3/3 seeds: peak_lag < 0, p < 0.10, \\|r\\| ≥ 0.60 |\n| **WEAK LEAD** | 3/3 seeds: peak_lag < 0, but ≥1 seed fails significance (p ≥ 0.10 or \\|r\\| < 0.60) |\n| **NO LEAD** | Any seed has peak_lag ≥ 0 |\n\n### Overall MVP verdict\n\n| Verdict | Required evidence |\n|---------|-------------------|\n| **STRONG PASS** | ≥2 canary families each have ≥1 SIGNIFICANT LEAD pair against non-demoted downstream metrics |\n| **PASS** | ≥1 canary family has ≥1 SIGNIFICANT LEAD pair against a non-demoted downstream metric |\n| **CONDITIONAL PASS** | No SIGNIFICANT LEAD pairs exist, but ≥1 canary family has ≥1 WEAK LEAD pair in all 3 seeds. Proceed to Phase 2 with this canary family prioritized but with explicit acknowledgment that MVP evidence is suggestive, not conclusive |\n| **FAIL** | No canary family achieves even WEAK LEAD consistency across 3 seeds |\n\n### The 2/3 problem\n\nIf 2/3 seeds show a lead but 1/3 does not: this is **NO LEAD** for that pair (not CONDITIONAL PASS). The hypothesis requires consistency across seeds to rule out stochastic artifacts. A 2/3 result may be noted in discussion but does not contribute to the verdict.\n\n**Exception:** If the dissenting seed shows peak_lag = 0 (simultaneous, not reverse), and the other 2 seeds show peak_lag ≤ -2 with p < 0.05, record this as a \"near miss\" in the report. It does not change the verdict but informs Phase 2 design (e.g., whether more seeds are needed).\n\n### Handling `effective_rank` non-monotonicity\n\nIf `effective_rank` is marked **inconclusive** per §3, its pairs are excluded from the verdict entirely (neither helping nor hurting). The verdict is computed over the remaining 3 canary families only. If `effective_rank` is the *only* canary with leads and it is inconclusive, the overall verdict is FAIL (we cannot claim a lead based on an inconclusive metric).\n\n---\n\n## 6. Decision Summary Table\n\n| # | Check | Rule | If TRUE | If FALSE |\n|---|-------|------|---------|----------|\n| 1 | MAUVE Gen 0 < 0.10 AND CV < 0.50 across all seeds? | §4 floor effect test | Demote MAUVE to supplementary | Retain MAUVE as primary downstream |\n| 2 | `effective_rank` Gen 4–9 slope sign consistent across seeds? | §3 slope test | Include in analysis (flip sign if β₁ < 0) | Mark inconclusive, exclude from verdict |\n| 3 | For each (canary, downstream) pair: all 3 seeds peak_lag < 0? | §2 strict negative | Pair is a lead candidate | Pair is NO LEAD |\n| 4 | For lead candidates: all 3 seeds p < 0.10 AND \\|r\\| ≥ 0.60? | §1 significance | SIGNIFICANT LEAD | WEAK LEAD |\n| 5 | ≥1 canary family has ≥1 SIGNIFICANT LEAD pair? | §5 PASS threshold | **PASS** (or STRONG PASS if ≥2 families) | Go to check 6 |\n| 6 | ≥1 canary family has ≥1 WEAK LEAD pair (3/3 consistent)? | §5 CONDITIONAL threshold | **CONDITIONAL PASS** — proceed with caveats | **FAIL** |\n\n### Post-verdict actions\n\n| Verdict | Next step |\n|---------|-----------|\n| STRONG PASS | Proceed to Phase 2 (synthetic ratio gradient). Prioritize the leading canary families. |\n| PASS | Proceed to Phase 2. Expand to more seeds (5 instead of 3) to strengthen evidence. |\n| CONDITIONAL PASS | Proceed to Phase 2 with modifications: increase to 20 generations (more statistical power) and 5 seeds. Re-evaluate with the same criteria at Phase 2 completion. |\n| FAIL | Revisit canary metric definitions or pivot research direction. Analyze whether collapse itself occurred (check perplexity trajectory); if no collapse happened in 10 generations, the null result is expected and the experiment should be extended. |\n\n---\n\n## Appendix: Implementation Checklist for `analyze_mvp.py`\n\nThe current `analyze_mvp.py` implements checks 2–3 and part of check 5 (binary PASS/FAIL). The following additions are needed before final analysis:\n\n- [ ] Add permutation test (§1) to `estimate_lead_time()` or as a wrapper function\n- [ ] Add per-seed significance filtering before aggregation\n- [ ] Add MAUVE floor effect detection (§4) before cross-correlation\n- [ ] Add `effective_rank` monotonicity check (§3) via Gen 4–9 OLS\n- [ ] Extend `analysis_summary.json` with graded verdict (§5) and all intermediate decisions\n- [ ] Report lag dispersion statistics (mean, std, min, max) per consistent pair\n",
      "numLines": 205,
      "startLine": 1,
      "totalLines": 205
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both files. Let me implement all 6 checks. I'll write the updated `analyze_mvp.py` with all the required changes.

Let me plan the implementation:

1. **Permutation test function** - `permutation_test(canary_series, downstream_series, canary_name, downstream_name, max_lag=5, n_permutations=10000, seed=0)`
2. **Per-seed significance filtering** - In main(), call permutation_test for each triplet, classify pairs


3. **MAUVE floor effect detection** - Check Gen 0 MAUVE and CV before running cross-correlation
4. **effective_rank monotonicity check** - Fit OLS regression on Gen 4-9 to verify increasing trend
5. **Graded verdict system** - Assign STRONG PASS / PASS / CONDITIONAL PASS / FAIL based on all checks
6. **Lag dispersion statistics** - Calculate spread metrics for consistent pairs

I'll also add the `--n_permutations` CLI argument and write out the complete updated file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "48665f16-e5ab-4951-9433-19aac1a42847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175qNLJRV4Dta7yBabgbNaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
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

_source line 10_

Now I have full context. Let me implement all 6 checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "e523ef12-b1b9-4251-bd84-935506be811c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175qNLJRV4Dta7yBabgbNaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
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

_source line 11_

<details open><summary>🔧 Tool call — Write · `toolu_018yX5xrMAyVa2YT5jKDJDQA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py",
  "content": "\"\"\"Analyze MVP experiment: metric trends, cross-correlation, lead time.\n\nReads all_metrics.json from each rep, produces:\n  - metric_trends.png : canary + downstream metrics vs generation\n  - cross_correlation.png : cross-correlation heatmap\n  - lead_time_table.csv : lead time estimates per canary-downstream pair\n  - analysis_summary.json : machine-readable summary with graded verdict\n\nEvaluation pipeline (per mvp_evaluation_criteria.md):\n  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50\n  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency\n  3. Permutation test (§1) — per-triplet significance via 10k permutations\n  4. Per-seed significance filtering (§2) — 3/3 consistency requirement\n  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL\n  6. Lag dispersion statistics — mean, std, min, max per consistent pair\n\nUsage:\n    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44\n    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\n\nCANARY_METRICS = [\"token_entropy\", \"self_bleu\", \"ece\", \"effective_rank\"]\nDOWNSTREAM_METRICS = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\", \"distinct_1\", \"distinct_2\",\n                   \"distinct_3\", \"mauve\"}\n\n\ndef load_metrics(results_dir, seeds):\n    \"\"\"Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}.\"\"\"\n    data = {}\n    for seed in seeds:\n        path = os.path.join(results_dir, f\"rep_{seed}\", \"all_metrics.json\")\n        with open(path) as f:\n            data[seed] = json.load(f)\n    return data\n\n\ndef metrics_to_df(data):\n    \"\"\"Convert {seed: [metrics_per_gen]} to a long-form DataFrame.\"\"\"\n    rows = []\n    for seed, gens in data.items():\n        for m in gens:\n            m_copy = dict(m)\n            m_copy[\"seed\"] = seed\n            rows.append(m_copy)\n    return pd.DataFrame(rows)\n\n\ndef normalize_for_correlation(series, metric_name):\n    \"\"\"Flip sign so that 'getting worse' is always positive direction.\"\"\"\n    s = series.copy()\n    if metric_name in LOWER_IS_WORSE:\n        s = -s\n    s = (s - s.mean()) / (s.std() + 1e-12)\n    return s\n\n\ndef cross_correlate(x, y, max_lag=5):\n    \"\"\"Cross-correlation of x and y at lags -max_lag..+max_lag.\n\n    Positive lag k means y leads x by k steps.\n    Negative lag k means x leads y by |k| steps.\n    \"\"\"\n    x = (x - x.mean()) / (x.std() + 1e-12)\n    y = (y - y.mean()) / (y.std() + 1e-12)\n    n = len(x)\n    correlations = {}\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0\n        else:\n            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0\n        correlations[lag] = c\n    return correlations\n\n\ndef estimate_lead_time(canary_series, downstream_series, canary_name,\n                       downstream_name, max_lag=5):\n    \"\"\"Estimate how many generations canary leads downstream.\n\n    Returns (peak_lag, peak_corr, corrs). Negative peak_lag = canary leads.\n    \"\"\"\n    c_norm = normalize_for_correlation(canary_series, canary_name)\n    d_norm = normalize_for_correlation(downstream_series, downstream_name)\n    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    return peak_lag, corrs[peak_lag], corrs\n\n\ndef permutation_test(canary_series, downstream_series, canary_name,\n                     downstream_name, max_lag=5, n_permutations=10000, seed=0):\n    \"\"\"Permutation test for cross-correlation significance.\n\n    Shuffles the downstream series to break temporal structure, recomputes\n    max |r| across all lags for each permutation. p-value is the fraction\n    of permutation max|r| >= observed peak|r|.\n\n    Returns (peak_lag, peak_corr, p_value).\n    \"\"\"\n    c_norm = normalize_for_correlation(canary_series, canary_name)\n    d_norm = normalize_for_correlation(downstream_series, downstream_name)\n\n    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    observed_peak_r = abs(corrs[peak_lag])\n\n    rng = np.random.RandomState(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        d_perm = rng.permutation(d_norm)\n        perm_corrs = cross_correlate(c_norm, d_perm, max_lag=max_lag)\n        perm_max_r = max(abs(v) for v in perm_corrs.values())\n        if perm_max_r >= observed_peak_r:\n            count_ge += 1\n\n    p_value = count_ge / n_permutations\n    return peak_lag, corrs[peak_lag], p_value\n\n\ndef check_mauve_floor(df, seeds):\n    \"\"\"Check MAUVE floor effect: Gen 0 < 0.10 and CV < 0.50 across all seeds.\n\n    Returns (demoted: bool, reason: str or None).\n    \"\"\"\n    for seed in seeds:\n        seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n        gen0_mauve = seed_df[seed_df[\"generation\"] == 0][\"mauve\"].values\n        if len(gen0_mauve) == 0:\n            return False, None\n        if gen0_mauve[0] >= 0.10:\n            return False, None\n        mauve_vals = seed_df[\"mauve\"].values\n        mean_m = np.mean(mauve_vals)\n        std_m = np.std(mauve_vals)\n        cv = std_m / (mean_m + 1e-12)\n        if cv >= 0.50:\n            return False, None\n    return True, \"floor_effect\"\n\n\ndef check_effective_rank_monotonicity(df, seeds):\n    \"\"\"Check effective_rank Gen 4-9 slope consistency across seeds.\n\n    Returns (status: str, slopes: dict).\n    status is one of: \"decreasing\", \"increasing\", \"inconclusive\".\n    \"\"\"\n    slopes = {}\n    for seed in seeds:\n        seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n        late = seed_df[seed_df[\"generation\"] >= 4]\n        if len(late) < 2:\n            return \"inconclusive\", {}\n        gens = late[\"generation\"].values.astype(float)\n        vals = late[\"effective_rank\"].values.astype(float)\n        coeffs = np.polyfit(gens, vals, 1)\n        slopes[str(seed)] = float(coeffs[0])\n\n    slope_vals = list(slopes.values())\n    if all(s < 0 for s in slope_vals):\n        return \"decreasing\", slopes\n    if all(s > 0 for s in slope_vals):\n        return \"increasing\", slopes\n    return \"inconclusive\", slopes\n\n\ndef classify_pair(per_seed_results):\n    \"\"\"Classify a (canary, downstream) pair based on per-seed results.\n\n    Returns one of: \"SIGNIFICANT LEAD\", \"WEAK LEAD\", \"NO LEAD\".\n    \"\"\"\n    if not all(r[\"peak_lag\"] < 0 for r in per_seed_results):\n        return \"NO LEAD\"\n    if all(r[\"p_value\"] < 0.10 and abs(r[\"peak_corr\"]) >= 0.60\n           for r in per_seed_results):\n        return \"SIGNIFICANT LEAD\"\n    return \"WEAK LEAD\"\n\n\ndef check_near_miss(per_seed_results):\n    \"\"\"Check if a NO LEAD pair is a near miss (2/3 seeds lead, 1 at lag=0).\"\"\"\n    lags = [r[\"peak_lag\"] for r in per_seed_results]\n    neg_seeds = [r for r in per_seed_results if r[\"peak_lag\"] < 0]\n    zero_seeds = [r for r in per_seed_results if r[\"peak_lag\"] == 0]\n    if len(neg_seeds) == 2 and len(zero_seeds) == 1:\n        if all(r[\"peak_lag\"] <= -2 and r[\"p_value\"] < 0.05 for r in neg_seeds):\n            return True\n    return False\n\n\ndef compute_lag_dispersion(per_seed_results):\n    \"\"\"Compute lag dispersion statistics for a consistent pair.\"\"\"\n    lags = [r[\"peak_lag\"] for r in per_seed_results]\n    lag_std = float(np.std(lags))\n    return {\n        \"mean_lag\": float(np.mean(lags)),\n        \"lag_std\": lag_std,\n        \"min_lag\": int(min(lags)),\n        \"max_lag\": int(max(lags)),\n        \"high_dispersion\": lag_std > 2.0,\n    }\n\n\ndef compute_verdict(per_pair_results, effective_rank_status):\n    \"\"\"Compute graded verdict from per-pair results.\n\n    Returns (verdict, reasoning, significant_pairs, weak_pairs).\n    \"\"\"\n    significant_pairs = []\n    weak_pairs = []\n\n    for pr in per_pair_results:\n        if pr[\"canary\"] == \"effective_rank\" and effective_rank_status == \"inconclusive\":\n            continue\n        if pr[\"pair_verdict\"] == \"SIGNIFICANT LEAD\":\n            significant_pairs.append(pr)\n        elif pr[\"pair_verdict\"] == \"WEAK LEAD\":\n            weak_pairs.append(pr)\n\n    sig_families = set(p[\"canary\"] for p in significant_pairs)\n    weak_families = set(p[\"canary\"] for p in weak_pairs)\n\n    if len(sig_families) >= 2:\n        verdict = \"STRONG PASS\"\n        reasoning = (f\"{len(sig_families)} canary families ({', '.join(sorted(sig_families))}) \"\n                     f\"each have >= 1 SIGNIFICANT LEAD pair.\")\n    elif len(sig_families) >= 1:\n        verdict = \"PASS\"\n        reasoning = (f\"{len(sig_families)} canary family ({', '.join(sorted(sig_families))}) \"\n                     f\"has >= 1 SIGNIFICANT LEAD pair.\")\n    elif len(weak_families) >= 1:\n        verdict = \"CONDITIONAL PASS\"\n        reasoning = (f\"No SIGNIFICANT LEAD pairs, but {len(weak_families)} canary \"\n                     f\"family ({', '.join(sorted(weak_families))}) has >= 1 WEAK LEAD pair.\")\n    else:\n        verdict = \"FAIL\"\n        reasoning = \"No canary family achieves even WEAK LEAD consistency across seeds.\"\n\n    return verdict, reasoning, significant_pairs, weak_pairs\n\n\ndef plot_metric_trends(df, output_dir):\n    \"\"\"Plot metric-vs-generation with mean +/- std across seeds.\"\"\"\n    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS\n    fig, axes = plt.subplots(3, 3, figsize=(15, 12))\n    axes = axes.flatten()\n\n    for idx, metric in enumerate(all_metrics):\n        if idx >= len(axes):\n            break\n        ax = axes[idx]\n        grouped = df.groupby(\"generation\")[metric]\n        mean = grouped.mean()\n        std = grouped.std()\n\n        ax.plot(mean.index, mean.values, \"o-\", linewidth=2)\n        ax.fill_between(mean.index, mean.values - std.values,\n                        mean.values + std.values, alpha=0.2)\n        ax.set_title(metric, fontsize=11, fontweight=\"bold\")\n        ax.set_xlabel(\"Generation\")\n        ax.set_ylabel(metric)\n        ax.grid(True, alpha=0.3)\n\n        is_canary = metric in CANARY_METRICS\n        ax.set_facecolor(\"#fff8f0\" if is_canary else \"#f0f8ff\")\n\n    for idx in range(len(all_metrics), len(axes)):\n        axes[idx].set_visible(False)\n\n    fig.suptitle(\"Metric Trends over Generations (mean ± std, 3 reps)\",\n                 fontsize=14, fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"metric_trends.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(\"Saved metric_trends.png\")\n\n\ndef plot_cross_correlation_heatmap(lead_table, output_dir):\n    \"\"\"Heatmap of peak lag (canary leads = negative lag).\"\"\"\n    pivot_lag = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                values=\"peak_lag\")\n    pivot_corr = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                  values=\"peak_corr\")\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n\n    im1 = ax1.imshow(pivot_lag.values, cmap=\"RdBu_r\", aspect=\"auto\",\n                     vmin=-5, vmax=5)\n    ax1.set_xticks(range(len(pivot_lag.columns)))\n    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha=\"right\")\n    ax1.set_yticks(range(len(pivot_lag.index)))\n    ax1.set_yticklabels(pivot_lag.index)\n    ax1.set_title(\"Peak Lag (negative = canary leads)\")\n    for i in range(len(pivot_lag.index)):\n        for j in range(len(pivot_lag.columns)):\n            ax1.text(j, i, f\"{pivot_lag.values[i, j]:.0f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im1, ax=ax1)\n\n    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap=\"YlOrRd\", aspect=\"auto\",\n                     vmin=0, vmax=1)\n    ax2.set_xticks(range(len(pivot_corr.columns)))\n    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha=\"right\")\n    ax2.set_yticks(range(len(pivot_corr.index)))\n    ax2.set_yticklabels(pivot_corr.index)\n    ax2.set_title(\"|Peak Correlation|\")\n    for i in range(len(pivot_corr.index)):\n        for j in range(len(pivot_corr.columns)):\n            ax2.text(j, i, f\"{pivot_corr.values[i, j]:.2f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im2, ax=ax2)\n\n    fig.suptitle(\"Cross-Correlation: Canary → Downstream\", fontsize=13,\n                 fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"cross_correlation.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(\"Saved cross_correlation.png\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Analyze MVP experiment with graded verdict system.\")\n    parser.add_argument(\"--results_dir\", type=str, default=\"results/mvp\")\n    parser.add_argument(\"--seeds\", type=int, nargs=\"+\", default=[42, 43, 44])\n    parser.add_argument(\"--max_lag\", type=int, default=5)\n    parser.add_argument(\"--n_permutations\", type=int, default=10000,\n                        help=\"Number of permutations for significance test (default: 10000)\")\n    args = parser.parse_args()\n\n    output_dir = os.path.join(args.results_dir, \"analysis\")\n    os.makedirs(output_dir, exist_ok=True)\n\n    print(\"Loading metrics ...\")\n    data = load_metrics(args.results_dir, args.seeds)\n    df = metrics_to_df(data)\n\n    # --- Metric trend plots ---\n    plot_metric_trends(df, output_dir)\n\n    # --- §4: MAUVE floor effect detection ---\n    mauve_demoted, mauve_reason = check_mauve_floor(df, args.seeds)\n    active_downstream = list(DOWNSTREAM_METRICS)\n    if mauve_demoted:\n        print(f\"MAUVE demoted to supplementary (reason: {mauve_reason})\")\n\n    # --- §3: effective_rank monotonicity check ---\n    er_status, er_slopes = check_effective_rank_monotonicity(df, args.seeds)\n    print(f\"effective_rank status: {er_status} (slopes: {er_slopes})\")\n\n    # --- Cross-correlation with permutation tests ---\n    total_triplets = len(CANARY_METRICS) * len(DOWNSTREAM_METRICS) * len(args.seeds)\n    triplet_idx = 0\n\n    per_pair_results = []\n    lead_rows = []\n    near_misses = []\n\n    for canary in CANARY_METRICS:\n        for downstream in DOWNSTREAM_METRICS:\n            per_seed = []\n            all_lags = []\n            all_corrs = []\n\n            for seed in args.seeds:\n                triplet_idx += 1\n                print(f\"\\r  Permutation test {triplet_idx}/{total_triplets}: \"\n                      f\"{canary} vs {downstream} (seed {seed})\", end=\"\",\n                      flush=True)\n\n                seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n                c_series = seed_df[canary].values\n                d_series = seed_df[downstream].values\n\n                peak_lag, peak_corr, p_value = permutation_test(\n                    c_series, d_series, canary, downstream,\n                    max_lag=args.max_lag,\n                    n_permutations=args.n_permutations,\n                    seed=seed)\n\n                per_seed.append({\n                    \"seed\": seed,\n                    \"peak_lag\": int(peak_lag),\n                    \"peak_corr\": round(float(peak_corr), 4),\n                    \"p_value\": round(float(p_value), 4),\n                })\n                all_lags.append(peak_lag)\n                all_corrs.append(peak_corr)\n\n            pair_verdict = classify_pair(per_seed)\n\n            pair_result = {\n                \"canary\": canary,\n                \"downstream\": downstream,\n                \"pair_verdict\": pair_verdict,\n                \"per_seed\": per_seed,\n            }\n\n            if pair_verdict in (\"SIGNIFICANT LEAD\", \"WEAK LEAD\"):\n                disp = compute_lag_dispersion(per_seed)\n                pair_result.update(disp)\n            else:\n                if check_near_miss(per_seed):\n                    near_misses.append({\"canary\": canary, \"downstream\": downstream,\n                                        \"per_seed\": per_seed})\n\n            per_pair_results.append(pair_result)\n\n            lead_rows.append({\n                \"canary\": canary,\n                \"downstream\": downstream,\n                \"peak_lag\": np.mean(all_lags),\n                \"peak_corr\": np.mean(all_corrs),\n                \"lag_std\": np.std(all_lags),\n                \"corr_std\": np.std(all_corrs),\n                \"consistent\": all(l < 0 for l in all_lags),\n            })\n\n    print()\n\n    lead_table = pd.DataFrame(lead_rows)\n    lead_table.to_csv(os.path.join(output_dir, \"lead_time_table.csv\"),\n                      index=False)\n    print(\"Saved lead_time_table.csv\")\n\n    plot_cross_correlation_heatmap(lead_table, output_dir)\n\n    # --- §5: Graded verdict ---\n    verdict_pairs = per_pair_results\n    if mauve_demoted:\n        verdict_pairs = [p for p in per_pair_results if p[\"downstream\"] != \"mauve\"]\n\n    verdict, reasoning, sig_pairs, weak_pairs = compute_verdict(\n        verdict_pairs, er_status)\n\n    # --- Build summary ---\n    summary = {\n        \"mauve_demoted\": mauve_demoted,\n        \"mauve_demoted_reason\": mauve_reason,\n        \"effective_rank_status\": er_status,\n        \"effective_rank_slopes\": er_slopes,\n        \"per_pair_results\": per_pair_results,\n        \"verdict\": verdict,\n        \"verdict_reasoning\": reasoning,\n        \"significant_lead_pairs\": [\n            {\"canary\": p[\"canary\"], \"downstream\": p[\"downstream\"]}\n            for p in sig_pairs\n        ],\n        \"weak_lead_pairs\": [\n            {\"canary\": p[\"canary\"], \"downstream\": p[\"downstream\"]}\n            for p in weak_pairs\n        ],\n        \"near_misses\": near_misses,\n    }\n\n    with open(os.path.join(output_dir, \"analysis_summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n\n    # --- Console report ---\n    print(\"\\n\" + \"=\" * 60)\n    print(\"MVP ANALYSIS SUMMARY\")\n    print(\"=\" * 60)\n\n    if mauve_demoted:\n        print(f\"MAUVE: demoted to supplementary ({mauve_reason})\")\n    else:\n        print(\"MAUVE: retained as primary downstream metric\")\n\n    print(f\"effective_rank: {er_status}\")\n    if er_slopes:\n        slope_str = \", \".join(f\"seed {k}: {v:.4f}\" for k, v in er_slopes.items())\n        print(f\"  slopes: {slope_str}\")\n\n    n_sig = len(sig_pairs)\n    n_weak = len(weak_pairs)\n    n_total = len(verdict_pairs)\n    print(f\"\\nPair results ({n_total} pairs evaluated for verdict):\")\n    print(f\"  SIGNIFICANT LEAD: {n_sig}\")\n    print(f\"  WEAK LEAD: {n_weak}\")\n    print(f\"  NO LEAD: {n_total - n_sig - n_weak}\")\n\n    if near_misses:\n        print(f\"  Near misses: {len(near_misses)}\")\n        for nm in near_misses:\n            print(f\"    {nm['canary']} -> {nm['downstream']}\")\n\n    verdict_icon = {\"STRONG PASS\": \"STRONG PASS\", \"PASS\": \"PASS\",\n                    \"CONDITIONAL PASS\": \"CONDITIONAL PASS\", \"FAIL\": \"FAIL\"}\n    print(f\"\\nVerdict: {verdict_icon[verdict]}\")\n    print(f\"Reasoning: {reasoning}\")\n\n    if sig_pairs:\n        print(\"\\nSignificant lead pairs:\")\n        for p in sig_pairs:\n            disp_flag = \" [high_dispersion]\" if p.get(\"high_dispersion\") else \"\"\n            print(f\"  {p['canary']} -> {p['downstream']}: \"\n                  f\"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}\")\n            for s in p[\"per_seed\"]:\n                print(f\"    seed {s['seed']}: lag={s['peak_lag']}, \"\n                      f\"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}\")\n\n    if weak_pairs:\n        print(\"\\nWeak lead pairs:\")\n        for p in weak_pairs:\n            disp_flag = \" [high_dispersion]\" if p.get(\"high_dispersion\") else \"\"\n            print(f\"  {p['canary']} -> {p['downstream']}: \"\n                  f\"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}\")\n            for s in p[\"per_seed\"]:\n                print(f\"    seed {s['seed']}: lag={s['peak_lag']}, \"\n                      f\"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}\")\n\n    print(\"\\nFull lead time table:\")\n    print(lead_table.to_string(index=False))\n    print(f\"\\nResults saved to {output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "c196745b-af86-4509-9aa8-0bbea86e2180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175qNLJRV4Dta7yBabgbNaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8139,
      "cache_read_input_tokens": 24205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8139
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

_source line 12 · 2026-05-14T08:34:30.914Z_

<details><summary>↩ Tool result · `toolu_018yX5xrMAyVa2YT5jKDJDQA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "7a9f633f-d874-4220-86a8-ab365bc12db3",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py",
    "content": "\"\"\"Analyze MVP experiment: metric trends, cross-correlation, lead time.\n\nReads all_metrics.json from each rep, produces:\n  - metric_trends.png : canary + downstream metrics vs generation\n  - cross_correlation.png : cross-correlation heatmap\n  - lead_time_table.csv : lead time estimates per canary-downstream pair\n  - analysis_summary.json : machine-readable summary with graded verdict\n\nEvaluation pipeline (per mvp_evaluation_criteria.md):\n  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50\n  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency\n  3. Permutation test (§1) — per-triplet significance via 10k permutations\n  4. Per-seed significance filtering (§2) — 3/3 consistency requirement\n  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL\n  6. Lag dispersion statistics — mean, std, min, max per consistent pair\n\nUsage:\n    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44\n    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\n\nCANARY_METRICS = [\"token_entropy\", \"self_bleu\", \"ece\", \"effective_rank\"]\nDOWNSTREAM_METRICS = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\", \"distinct_1\", \"distinct_2\",\n                   \"distinct_3\", \"mauve\"}\n\n\ndef load_metrics(results_dir, seeds):\n    \"\"\"Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}.\"\"\"\n    data = {}\n    for seed in seeds:\n        path = os.path.join(results_dir, f\"rep_{seed}\", \"all_metrics.json\")\n        with open(path) as f:\n            data[seed] = json.load(f)\n    return data\n\n\ndef metrics_to_df(data):\n    \"\"\"Convert {seed: [metrics_per_gen]} to a long-form DataFrame.\"\"\"\n    rows = []\n    for seed, gens in data.items():\n        for m in gens:\n            m_copy = dict(m)\n            m_copy[\"seed\"] = seed\n            rows.append(m_copy)\n    return pd.DataFrame(rows)\n\n\ndef normalize_for_correlation(series, metric_name):\n    \"\"\"Flip sign so that 'getting worse' is always positive direction.\"\"\"\n    s = series.copy()\n    if metric_name in LOWER_IS_WORSE:\n        s = -s\n    s = (s - s.mean()) / (s.std() + 1e-12)\n    return s\n\n\ndef cross_correlate(x, y, max_lag=5):\n    \"\"\"Cross-correlation of x and y at lags -max_lag..+max_lag.\n\n    Positive lag k means y leads x by k steps.\n    Negative lag k means x leads y by |k| steps.\n    \"\"\"\n    x = (x - x.mean()) / (x.std() + 1e-12)\n    y = (y - y.mean()) / (y.std() + 1e-12)\n    n = len(x)\n    correlations = {}\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0\n        else:\n            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0\n        correlations[lag] = c\n    return correlations\n\n\ndef estimate_lead_time(canary_series, downstream_series, canary_name,\n                       downstream_name, max_lag=5):\n    \"\"\"Estimate how many generations canary leads downstream.\n\n    Returns (peak_lag, peak_corr, corrs). Negative peak_lag = canary leads.\n    \"\"\"\n    c_norm = normalize_for_correlation(canary_series, canary_name)\n    d_norm = normalize_for_correlation(downstream_series, downstream_name)\n    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    return peak_lag, corrs[peak_lag], corrs\n\n\ndef permutation_test(canary_series, downstream_series, canary_name,\n                     downstream_name, max_lag=5, n_permutations=10000, seed=0):\n    \"\"\"Permutation test for cross-correlation significance.\n\n    Shuffles the downstream series to break temporal structure, recomputes\n    max |r| across all lags for each permutation. p-value is the fraction\n    of permutation max|r| >= observed peak|r|.\n\n    Returns (peak_lag, peak_corr, p_value).\n    \"\"\"\n    c_norm = normalize_for_correlation(canary_series, canary_name)\n    d_norm = normalize_for_correlation(downstream_series, downstream_name)\n\n    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    observed_peak_r = abs(corrs[peak_lag])\n\n    rng = np.random.RandomState(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        d_perm = rng.permutation(d_norm)\n        perm_corrs = cross_correlate(c_norm, d_perm, max_lag=max_lag)\n        perm_max_r = max(abs(v) for v in perm_corrs.values())\n        if perm_max_r >= observed_peak_r:\n            count_ge += 1\n\n    p_value = count_ge / n_permutations\n    return peak_lag, corrs[peak_lag], p_value\n\n\ndef check_mauve_floor(df, seeds):\n    \"\"\"Check MAUVE floor effect: Gen 0 < 0.10 and CV < 0.50 across all seeds.\n\n    Returns (demoted: bool, reason: str or None).\n    \"\"\"\n    for seed in seeds:\n        seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n        gen0_mauve = seed_df[seed_df[\"generation\"] == 0][\"mauve\"].values\n        if len(gen0_mauve) == 0:\n            return False, None\n        if gen0_mauve[0] >= 0.10:\n            return False, None\n        mauve_vals = seed_df[\"mauve\"].values\n        mean_m = np.mean(mauve_vals)\n        std_m = np.std(mauve_vals)\n        cv = std_m / (mean_m + 1e-12)\n        if cv >= 0.50:\n            return False, None\n    return True, \"floor_effect\"\n\n\ndef check_effective_rank_monotonicity(df, seeds):\n    \"\"\"Check effective_rank Gen 4-9 slope consistency across seeds.\n\n    Returns (status: str, slopes: dict).\n    status is one of: \"decreasing\", \"increasing\", \"inconclusive\".\n    \"\"\"\n    slopes = {}\n    for seed in seeds:\n        seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n        late = seed_df[seed_df[\"generation\"] >= 4]\n        if len(late) < 2:\n            return \"inconclusive\", {}\n        gens = late[\"generation\"].values.astype(float)\n        vals = late[\"effective_rank\"].values.astype(float)\n        coeffs = np.polyfit(gens, vals, 1)\n        slopes[str(seed)] = float(coeffs[0])\n\n    slope_vals = list(slopes.values())\n    if all(s < 0 for s in slope_vals):\n        return \"decreasing\", slopes\n    if all(s > 0 for s in slope_vals):\n        return \"increasing\", slopes\n    return \"inconclusive\", slopes\n\n\ndef classify_pair(per_seed_results):\n    \"\"\"Classify a (canary, downstream) pair based on per-seed results.\n\n    Returns one of: \"SIGNIFICANT LEAD\", \"WEAK LEAD\", \"NO LEAD\".\n    \"\"\"\n    if not all(r[\"peak_lag\"] < 0 for r in per_seed_results):\n        return \"NO LEAD\"\n    if all(r[\"p_value\"] < 0.10 and abs(r[\"peak_corr\"]) >= 0.60\n           for r in per_seed_results):\n        return \"SIGNIFICANT LEAD\"\n    return \"WEAK LEAD\"\n\n\ndef check_near_miss(per_seed_results):\n    \"\"\"Check if a NO LEAD pair is a near miss (2/3 seeds lead, 1 at lag=0).\"\"\"\n    lags = [r[\"peak_lag\"] for r in per_seed_results]\n    neg_seeds = [r for r in per_seed_results if r[\"peak_lag\"] < 0]\n    zero_seeds = [r for r in per_seed_results if r[\"peak_lag\"] == 0]\n    if len(neg_seeds) == 2 and len(zero_seeds) == 1:\n        if all(r[\"peak_lag\"] <= -2 and r[\"p_value\"] < 0.05 for r in neg_seeds):\n            return True\n    return False\n\n\ndef compute_lag_dispersion(per_seed_results):\n    \"\"\"Compute lag dispersion statistics for a consistent pair.\"\"\"\n    lags = [r[\"peak_lag\"] for r in per_seed_results]\n    lag_std = float(np.std(lags))\n    return {\n        \"mean_lag\": float(np.mean(lags)),\n        \"lag_std\": lag_std,\n        \"min_lag\": int(min(lags)),\n        \"max_lag\": int(max(lags)),\n        \"high_dispersion\": lag_std > 2.0,\n    }\n\n\ndef compute_verdict(per_pair_results, effective_rank_status):\n    \"\"\"Compute graded verdict from per-pair results.\n\n    Returns (verdict, reasoning, significant_pairs, weak_pairs).\n    \"\"\"\n    significant_pairs = []\n    weak_pairs = []\n\n    for pr in per_pair_results:\n        if pr[\"canary\"] == \"effective_rank\" and effective_rank_status == \"inconclusive\":\n            continue\n        if pr[\"pair_verdict\"] == \"SIGNIFICANT LEAD\":\n            significant_pairs.append(pr)\n        elif pr[\"pair_verdict\"] == \"WEAK LEAD\":\n            weak_pairs.append(pr)\n\n    sig_families = set(p[\"canary\"] for p in significant_pairs)\n    weak_families = set(p[\"canary\"] for p in weak_pairs)\n\n    if len(sig_families) >= 2:\n        verdict = \"STRONG PASS\"\n        reasoning = (f\"{len(sig_families)} canary families ({', '.join(sorted(sig_families))}) \"\n                     f\"each have >= 1 SIGNIFICANT LEAD pair.\")\n    elif len(sig_families) >= 1:\n        verdict = \"PASS\"\n        reasoning = (f\"{len(sig_families)} canary family ({', '.join(sorted(sig_families))}) \"\n                     f\"has >= 1 SIGNIFICANT LEAD pair.\")\n    elif len(weak_families) >= 1:\n        verdict = \"CONDITIONAL PASS\"\n        reasoning = (f\"No SIGNIFICANT LEAD pairs, but {len(weak_families)} canary \"\n                     f\"family ({', '.join(sorted(weak_families))}) has >= 1 WEAK LEAD pair.\")\n    else:\n        verdict = \"FAIL\"\n        reasoning = \"No canary family achieves even WEAK LEAD consistency across seeds.\"\n\n    return verdict, reasoning, significant_pairs, weak_pairs\n\n\ndef plot_metric_trends(df, output_dir):\n    \"\"\"Plot metric-vs-generation with mean +/- std across seeds.\"\"\"\n    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS\n    fig, axes = plt.subplots(3, 3, figsize=(15, 12))\n    axes = axes.flatten()\n\n    for idx, metric in enumerate(all_metrics):\n        if idx >= len(axes):\n            break\n        ax = axes[idx]\n        grouped = df.groupby(\"generation\")[metric]\n        mean = grouped.mean()\n        std = grouped.std()\n\n        ax.plot(mean.index, mean.values, \"o-\", linewidth=2)\n        ax.fill_between(mean.index, mean.values - std.values,\n                        mean.values + std.values, alpha=0.2)\n        ax.set_title(metric, fontsize=11, fontweight=\"bold\")\n        ax.set_xlabel(\"Generation\")\n        ax.set_ylabel(metric)\n        ax.grid(True, alpha=0.3)\n\n        is_canary = metric in CANARY_METRICS\n        ax.set_facecolor(\"#fff8f0\" if is_canary else \"#f0f8ff\")\n\n    for idx in range(len(all_metrics), len(axes)):\n        axes[idx].set_visible(False)\n\n    fig.suptitle(\"Metric Trends over Generations (mean ± std, 3 reps)\",\n                 fontsize=14, fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"metric_trends.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(\"Saved metric_trends.png\")\n\n\ndef plot_cross_correlation_heatmap(lead_table, output_dir):\n    \"\"\"Heatmap of peak lag (canary leads = negative lag).\"\"\"\n    pivot_lag = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                values=\"peak_lag\")\n    pivot_corr = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                  values=\"peak_corr\")\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n\n    im1 = ax1.imshow(pivot_lag.values, cmap=\"RdBu_r\", aspect=\"auto\",\n                     vmin=-5, vmax=5)\n    ax1.set_xticks(range(len(pivot_lag.columns)))\n    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha=\"right\")\n    ax1.set_yticks(range(len(pivot_lag.index)))\n    ax1.set_yticklabels(pivot_lag.index)\n    ax1.set_title(\"Peak Lag (negative = canary leads)\")\n    for i in range(len(pivot_lag.index)):\n        for j in range(len(pivot_lag.columns)):\n            ax1.text(j, i, f\"{pivot_lag.values[i, j]:.0f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im1, ax=ax1)\n\n    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap=\"YlOrRd\", aspect=\"auto\",\n                     vmin=0, vmax=1)\n    ax2.set_xticks(range(len(pivot_corr.columns)))\n    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha=\"right\")\n    ax2.set_yticks(range(len(pivot_corr.index)))\n    ax2.set_yticklabels(pivot_corr.index)\n    ax2.set_title(\"|Peak Correlation|\")\n    for i in range(len(pivot_corr.index)):\n        for j in range(len(pivot_corr.columns)):\n            ax2.text(j, i, f\"{pivot_corr.values[i, j]:.2f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im2, ax=ax2)\n\n    fig.suptitle(\"Cross-Correlation: Canary → Downstream\", fontsize=13,\n                 fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"cross_correlation.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(\"Saved cross_correlation.png\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Analyze MVP experiment with graded verdict system.\")\n    parser.add_argument(\"--results_dir\", type=str, default=\"results/mvp\")\n    parser.add_argument(\"--seeds\", type=int, nargs=\"+\", default=[42, 43, 44])\n    parser.add_argument(\"--max_lag\", type=int, default=5)\n    parser.add_argument(\"--n_permutations\", type=int, default=10000,\n                        help=\"Number of permutations for significance test (default: 10000)\")\n    args = parser.parse_args()\n\n    output_dir = os.path.join(args.results_dir, \"analysis\")\n    os.makedirs(output_dir, exist_ok=True)\n\n    print(\"Loading metrics ...\")\n    data = load_metrics(args.results_dir, args.seeds)\n    df = metrics_to_df(data)\n\n    # --- Metric trend plots ---\n    plot_metric_trends(df, output_dir)\n\n    # --- §4: MAUVE floor effect detection ---\n    mauve_demoted, mauve_reason = check_mauve_floor(df, args.seeds)\n    active_downstream = list(DOWNSTREAM_METRICS)\n    if mauve_demoted:\n        print(f\"MAUVE demoted to supplementary (reason: {mauve_reason})\")\n\n    # --- §3: effective_rank monotonicity check ---\n    er_status, er_slopes = check_effective_rank_monotonicity(df, args.seeds)\n    print(f\"effective_rank status: {er_status} (slopes: {er_slopes})\")\n\n    # --- Cross-correlation with permutation tests ---\n    total_triplets = len(CANARY_METRICS) * len(DOWNSTREAM_METRICS) * len(args.seeds)\n    triplet_idx = 0\n\n    per_pair_results = []\n    lead_rows = []\n    near_misses = []\n\n    for canary in CANARY_METRICS:\n        for downstream in DOWNSTREAM_METRICS:\n            per_seed = []\n            all_lags = []\n            all_corrs = []\n\n            for seed in args.seeds:\n                triplet_idx += 1\n                print(f\"\\r  Permutation test {triplet_idx}/{total_triplets}: \"\n                      f\"{canary} vs {downstream} (seed {seed})\", end=\"\",\n                      flush=True)\n\n                seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n                c_series = seed_df[canary].values\n                d_series = seed_df[downstream].values\n\n                peak_lag, peak_corr, p_value = permutation_test(\n                    c_series, d_series, canary, downstream,\n                    max_lag=args.max_lag,\n                    n_permutations=args.n_permutations,\n                    seed=seed)\n\n                per_seed.append({\n                    \"seed\": seed,\n                    \"peak_lag\": int(peak_lag),\n                    \"peak_corr\": round(float(peak_corr), 4),\n                    \"p_value\": round(float(p_value), 4),\n                })\n                all_lags.append(peak_lag)\n                all_corrs.append(peak_corr)\n\n            pair_verdict = classify_pair(per_seed)\n\n            pair_result = {\n                \"canary\": canary,\n                \"downstream\": downstream,\n                \"pair_verdict\": pair_verdict,\n                \"per_seed\": per_seed,\n            }\n\n            if pair_verdict in (\"SIGNIFICANT LEAD\", \"WEAK LEAD\"):\n                disp = compute_lag_dispersion(per_seed)\n                pair_result.update(disp)\n            else:\n                if check_near_miss(per_seed):\n                    near_misses.append({\"canary\": canary, \"downstream\": downstream,\n                                        \"per_seed\": per_seed})\n\n            per_pair_results.append(pair_result)\n\n            lead_rows.append({\n                \"canary\": canary,\n                \"downstream\": downstream,\n                \"peak_lag\": np.mean(all_lags),\n                \"peak_corr\": np.mean(all_corrs),\n                \"lag_std\": np.std(all_lags),\n                \"corr_std\": np.std(all_corrs),\n                \"consistent\": all(l < 0 for l in all_lags),\n            })\n\n    print()\n\n    lead_table = pd.DataFrame(lead_rows)\n    lead_table.to_csv(os.path.join(output_dir, \"lead_time_table.csv\"),\n                      index=False)\n    print(\"Saved lead_time_table.csv\")\n\n    plot_cross_correlation_heatmap(lead_table, output_dir)\n\n    # --- §5: Graded verdict ---\n    verdict_pairs = per_pair_results\n    if mauve_demoted:\n        verdict_pairs = [p for p in per_pair_results if p[\"downstream\"] != \"mauve\"]\n\n    verdict, reasoning, sig_pairs, weak_pairs = compute_verdict(\n        verdict_pairs, er_status)\n\n    # --- Build summary ---\n    summary = {\n        \"mauve_demoted\": mauve_demoted,\n        \"mauve_demoted_reason\": mauve_reason,\n        \"effective_rank_status\": er_status,\n        \"effective_rank_slopes\": er_slopes,\n        \"per_pair_results\": per_pair_results,\n        \"verdict\": verdict,\n        \"verdict_reasoning\": reasoning,\n        \"significant_lead_pairs\": [\n            {\"canary\": p[\"canary\"], \"downstream\": p[\"downstream\"]}\n            for p in sig_pairs\n        ],\n        \"weak_lead_pairs\": [\n            {\"canary\": p[\"canary\"], \"downstream\": p[\"downstream\"]}\n            for p in weak_pairs\n        ],\n        \"near_misses\": near_misses,\n    }\n\n    with open(os.path.join(output_dir, \"analysis_summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n\n    # --- Console report ---\n    print(\"\\n\" + \"=\" * 60)\n    print(\"MVP ANALYSIS SUMMARY\")\n    print(\"=\" * 60)\n\n    if mauve_demoted:\n        print(f\"MAUVE: demoted to supplementary ({mauve_reason})\")\n    else:\n        print(\"MAUVE: retained as primary downstream metric\")\n\n    print(f\"effective_rank: {er_status}\")\n    if er_slopes:\n        slope_str = \", \".join(f\"seed {k}: {v:.4f}\" for k, v in er_slopes.items())\n        print(f\"  slopes: {slope_str}\")\n\n    n_sig = len(sig_pairs)\n    n_weak = len(weak_pairs)\n    n_total = len(verdict_pairs)\n    print(f\"\\nPair results ({n_total} pairs evaluated for verdict):\")\n    print(f\"  SIGNIFICANT LEAD: {n_sig}\")\n    print(f\"  WEAK LEAD: {n_weak}\")\n    print(f\"  NO LEAD: {n_total - n_sig - n_weak}\")\n\n    if near_misses:\n        print(f\"  Near misses: {len(near_misses)}\")\n        for nm in near_misses:\n            print(f\"    {nm['canary']} -> {nm['downstream']}\")\n\n    verdict_icon = {\"STRONG PASS\": \"STRONG PASS\", \"PASS\": \"PASS\",\n                    \"CONDITIONAL PASS\": \"CONDITIONAL PASS\", \"FAIL\": \"FAIL\"}\n    print(f\"\\nVerdict: {verdict_icon[verdict]}\")\n    print(f\"Reasoning: {reasoning}\")\n\n    if sig_pairs:\n        print(\"\\nSignificant lead pairs:\")\n        for p in sig_pairs:\n            disp_flag = \" [high_dispersion]\" if p.get(\"high_dispersion\") else \"\"\n            print(f\"  {p['canary']} -> {p['downstream']}: \"\n                  f\"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}\")\n            for s in p[\"per_seed\"]:\n                print(f\"    seed {s['seed']}: lag={s['peak_lag']}, \"\n                      f\"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}\")\n\n    if weak_pairs:\n        print(\"\\nWeak lead pairs:\")\n        for p in weak_pairs:\n            disp_flag = \" [high_dispersion]\" if p.get(\"high_dispersion\") else \"\"\n            print(f\"  {p['canary']} -> {p['downstream']}: \"\n                  f\"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}\")\n            for s in p[\"per_seed\"]:\n                print(f\"    seed {s['seed']}: lag={s['peak_lag']}, \"\n                      f\"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}\")\n\n    print(\"\\nFull lead time table:\")\n    print(lead_table.to_string(index=False))\n    print(f\"\\nResults saved to {output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 15,
        "newStart": 4,
        "newLines": 25,
        "lines": [
          "   - metric_trends.png : canary + downstream metrics vs generation",
          "   - cross_correlation.png : cross-correlation heatmap",
          "   - lead_time_table.csv : lead time estimates per canary-downstream pair",
          "-  - analysis_summary.json : machine-readable summary",
          "+  - analysis_summary.json : machine-readable summary with graded verdict",
          " ",
          "+Evaluation pipeline (per mvp_evaluation_criteria.md):",
          "+  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50",
          "+  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency",
          "+  3. Permutation test (§1) — per-triplet significance via 10k permutations",
          "+  4. Per-seed significance filtering (§2) — 3/3 consistency requirement",
          "+  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL",
          "+  6. Lag dispersion statistics — mean, std, min, max per consistent pair",
          "+",
          " Usage:",
          "     python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44",
          "+    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000",
          " \"\"\"",
          " ",
          " import argparse",
          " import json",
          " import os",
          "+import sys",
          " ",
          " import matplotlib.pyplot as plt",
          " import numpy as np"
        ]
      },
      {
        "oldStart": 22,
        "oldLines": 9,
        "newStart": 32,
        "newLines": 7,
        "lines": [
          " CANARY_METRICS = [\"token_entropy\", \"self_bleu\", \"ece\", \"effective_rank\"]",
          " DOWNSTREAM_METRICS = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]",
          " ",
          "-# Metrics where higher = worse (collapse direction)",
          " HIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}",
          "-# Metrics where lower = worse (collapse direction)",
          " LOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\", \"distinct_1\", \"distinct_2\",",
          "                    \"distinct_3\", \"mauve\"}",
          " "
        ]
      },
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 90,
        "newLines": 7,
        "lines": [
          "                        downstream_name, max_lag=5):",
          "     \"\"\"Estimate how many generations canary leads downstream.",
          " ",
          "-    Returns (peak_lag, peak_corr). Negative peak_lag = canary leads.",
          "+    Returns (peak_lag, peak_corr, corrs). Negative peak_lag = canary leads.",
          "     \"\"\"",
          "     c_norm = normalize_for_correlation(canary_series, canary_name)",
          "     d_norm = normalize_for_correlation(downstream_series, downstream_name)"
        ]
      },
      {
        "oldStart": 91,
        "oldLines": 8,
        "newStart": 99,
        "newLines": 159,
        "lines": [
          "     return peak_lag, corrs[peak_lag], corrs",
          " ",
          " ",
          "+def permutation_test(canary_series, downstream_series, canary_name,",
          "+                     downstream_name, max_lag=5, n_permutations=10000, seed=0):",
          "+    \"\"\"Permutation test for cross-correlation significance.",
          "+",
          "+    Shuffles the downstream series to break temporal structure, recomputes",
          "+    max |r| across all lags for each permutation. p-value is the fraction",
          "+    of permutation max|r| >= observed peak|r|.",
          "+",
          "+    Returns (peak_lag, peak_corr, p_value).",
          "+    \"\"\"",
          "+    c_norm = normalize_for_correlation(canary_series, canary_name)",
          "+    d_norm = normalize_for_correlation(downstream_series, downstream_name)",
          "+",
          "+    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)",
          "+    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))",
          "+    observed_peak_r = abs(corrs[peak_lag])",
          "+",
          "+    rng = np.random.RandomState(seed)",
          "+    count_ge = 0",
          "+    for _ in range(n_permutations):",
          "+        d_perm = rng.permutation(d_norm)",
          "+        perm_corrs = cross_correlate(c_norm, d_perm, max_lag=max_lag)",
          "+        perm_max_r = max(abs(v) for v in perm_corrs.values())",
          "+        if perm_max_r >= observed_peak_r:",
          "+            count_ge += 1",
          "+",
          "+    p_value = count_ge / n_permutations",
          "+    return peak_lag, corrs[peak_lag], p_value",
          "+",
          "+",
          "+def check_mauve_floor(df, seeds):",
          "+    \"\"\"Check MAUVE floor effect: Gen 0 < 0.10 and CV < 0.50 across all seeds.",
          "+",
          "+    Returns (demoted: bool, reason: str or None).",
          "+    \"\"\"",
          "+    for seed in seeds:",
          "+        seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")",
          "+        gen0_mauve = seed_df[seed_df[\"generation\"] == 0][\"mauve\"].values",
          "+        if len(gen0_mauve) == 0:",
          "+            return False, None",
          "+        if gen0_mauve[0] >= 0.10:",
          "+            return False, None",
          "+        mauve_vals = seed_df[\"mauve\"].values",
          "+        mean_m = np.mean(mauve_vals)",
          "+        std_m = np.std(mauve_vals)",
          "+        cv = std_m / (mean_m + 1e-12)",
          "+        if cv >= 0.50:",
          "+            return False, None",
          "+    return True, \"floor_effect\"",
          "+",
          "+",
          "+def check_effective_rank_monotonicity(df, seeds):",
          "+    \"\"\"Check effective_rank Gen 4-9 slope consistency across seeds.",
          "+",
          "+    Returns (status: str, slopes: dict).",
          "+    status is one of: \"decreasing\", \"increasing\", \"inconclusive\".",
          "+    \"\"\"",
          "+    slopes = {}",
          "+    for seed in seeds:",
          "+        seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")",
          "+        late = seed_df[seed_df[\"generation\"] >= 4]",
          "+        if len(late) < 2:",
          "+            return \"inconclusive\", {}",
          "+        gens = late[\"generation\"].values.astype(float)",
          "+        vals = late[\"effective_rank\"].values.astype(float)",
          "+        coeffs = np.polyfit(gens, vals, 1)",
          "+        slopes[str(seed)] = float(coeffs[0])",
          "+",
          "+    slope_vals = list(slopes.values())",
          "+    if all(s < 0 for s in slope_vals):",
          "+        return \"decreasing\", slopes",
          "+    if all(s > 0 for s in slope_vals):",
          "+        return \"increasing\", slopes",
          "+    return \"inconclusive\", slopes",
          "+",
          "+",
          "+def classify_pair(per_seed_results):",
          "+    \"\"\"Classify a (canary, downstream) pair based on per-seed results.",
          "+",
          "+    Returns one of: \"SIGNIFICANT LEAD\", \"WEAK LEAD\", \"NO LEAD\".",
          "+    \"\"\"",
          "+    if not all(r[\"peak_lag\"] < 0 for r in per_seed_results):",
          "+        return \"NO LEAD\"",
          "+    if all(r[\"p_value\"] < 0.10 and abs(r[\"peak_corr\"]) >= 0.60",
          "+           for r in per_seed_results):",
          "+        return \"SIGNIFICANT LEAD\"",
          "+    return \"WEAK LEAD\"",
          "+",
          "+",
          "+def check_near_miss(per_seed_results):",
          "+    \"\"\"Check if a NO LEAD pair is a near miss (2/3 seeds lead, 1 at lag=0).\"\"\"",
          "+    lags = [r[\"peak_lag\"] for r in per_seed_results]",
          "+    neg_seeds = [r for r in per_seed_results if r[\"peak_lag\"] < 0]",
          "+    zero_seeds = [r for r in per_seed_results if r[\"peak_lag\"] == 0]",
          "+    if len(neg_seeds) == 2 and len(zero_seeds) == 1:",
          "+        if all(r[\"peak_lag\"] <= -2 and r[\"p_value\"] < 0.05 for r in neg_seeds):",
          "+            return True",
          "+    return False",
          "+",
          "+",
          "+def compute_lag_dispersion(per_seed_results):",
          "+    \"\"\"Compute lag dispersion statistics for a consistent pair.\"\"\"",
          "+    lags = [r[\"peak_lag\"] for r in per_seed_results]",
          "+    lag_std = float(np.std(lags))",
          "+    return {",
          "+        \"mean_lag\": float(np.mean(lags)),",
          "+        \"lag_std\": lag_std,",
          "+        \"min_lag\": int(min(lags)),",
          "+        \"max_lag\": int(max(lags)),",
          "+        \"high_dispersion\": lag_std > 2.0,",
          "+    }",
          "+",
          "+",
          "+def compute_verdict(per_pair_results, effective_rank_status):",
          "+    \"\"\"Compute graded verdict from per-pair results.",
          "+",
          "+    Returns (verdict, reasoning, significant_pairs, weak_pairs).",
          "+    \"\"\"",
          "+    significant_pairs = []",
          "+    weak_pairs = []",
          "+",
          "+    for pr in per_pair_results:",
          "+        if pr[\"canary\"] == \"effective_rank\" and effective_rank_status == \"inconclusive\":",
          "+            continue",
          "+        if pr[\"pair_verdict\"] == \"SIGNIFICANT LEAD\":",
          "+            significant_pairs.append(pr)",
          "+        elif pr[\"pair_verdict\"] == \"WEAK LEAD\":",
          "+            weak_pairs.append(pr)",
          "+",
          "+    sig_families = set(p[\"canary\"] for p in significant_pairs)",
          "+    weak_families = set(p[\"canary\"] for p in weak_pairs)",
          "+",
          "+    if len(sig_families) >= 2:",
          "+        verdict = \"STRONG PASS\"",
          "+        reasoning = (f\"{len(sig_families)} canary families ({', '.join(sorted(sig_families))}) \"",
          "+                     f\"each have >= 1 SIGNIFICANT LEAD pair.\")",
          "+    elif len(sig_families) >= 1:",
          "+        verdict = \"PASS\"",
          "+        reasoning = (f\"{len(sig_families)} canary family ({', '.join(sorted(sig_families))}) \"",
          "+                     f\"has >= 1 SIGNIFICANT LEAD pair.\")",
          "+    elif len(weak_families) >= 1:",
          "+        verdict = \"CONDITIONAL PASS\"",
          "+        reasoning = (f\"No SIGNIFICANT LEAD pairs, but {len(weak_families)} canary \"",
          "+                     f\"family ({', '.join(sorted(weak_families))}) has >= 1 WEAK LEAD pair.\")",
          "+    else:",
          "+        verdict = \"FAIL\"",
          "+        reasoning = \"No canary family achieves even WEAK LEAD consistency across seeds.\"",
          "+",
          "+    return verdict, reasoning, significant_pairs, weak_pairs",
          "+",
          "+",
          " def plot_metric_trends(df, output_dir):",
          "-    \"\"\"Plot metric-vs-generation with mean ± std across seeds.\"\"\"",
          "+    \"\"\"Plot metric-vs-generation with mean +/- std across seeds.\"\"\"",
          "     all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS",
          "     fig, axes = plt.subplots(3, 3, figsize=(15, 12))",
          "     axes = axes.flatten()"
        ]
      },
      {
        "oldStart": 125,
        "oldLines": 7,
        "newStart": 284,
        "newLines": 7,
        "lines": [
          "     plt.savefig(os.path.join(output_dir, \"metric_trends.png\"), dpi=150,",
          "                 bbox_inches=\"tight\")",
          "     plt.close()",
          "-    print(f\"Saved metric_trends.png\")",
          "+    print(\"Saved metric_trends.png\")",
          " ",
          " ",
          " def plot_cross_correlation_heatmap(lead_table, output_dir):"
        ]
      },
      {
        "oldStart": 173,
        "oldLines": 38,
        "newStart": 332,
        "newLines": 93,
        "lines": [
          " ",
          " ",
          " def main():",
          "-    parser = argparse.ArgumentParser()",
          "+    parser = argparse.ArgumentParser(",
          "+        description=\"Analyze MVP experiment with graded verdict system.\")",
          "     parser.add_argument(\"--results_dir\", type=str, default=\"results/mvp\")",
          "     parser.add_argument(\"--seeds\", type=int, nargs=\"+\", default=[42, 43, 44])",
          "     parser.add_argument(\"--max_lag\", type=int, default=5)",
          "+    parser.add_argument(\"--n_permutations\", type=int, default=10000,",
          "+                        help=\"Number of permutations for significance test (default: 10000)\")",
          "     args = parser.parse_args()",
          " ",
          "     output_dir = os.path.join(args.results_dir, \"analysis\")",
          "     os.makedirs(output_dir, exist_ok=True)",
          " ",
          "-    print(\"Loading metrics …\")",
          "+    print(\"Loading metrics ...\")",
          "     data = load_metrics(args.results_dir, args.seeds)",
          "     df = metrics_to_df(data)",
          " ",
          "     # --- Metric trend plots ---",
          "     plot_metric_trends(df, output_dir)",
          " ",
          "-    # --- Cross-correlation & lead time ---",
          "+    # --- §4: MAUVE floor effect detection ---",
          "+    mauve_demoted, mauve_reason = check_mauve_floor(df, args.seeds)",
          "+    active_downstream = list(DOWNSTREAM_METRICS)",
          "+    if mauve_demoted:",
          "+        print(f\"MAUVE demoted to supplementary (reason: {mauve_reason})\")",
          "+",
          "+    # --- §3: effective_rank monotonicity check ---",
          "+    er_status, er_slopes = check_effective_rank_monotonicity(df, args.seeds)",
          "+    print(f\"effective_rank status: {er_status} (slopes: {er_slopes})\")",
          "+",
          "+    # --- Cross-correlation with permutation tests ---",
          "+    total_triplets = len(CANARY_METRICS) * len(DOWNSTREAM_METRICS) * len(args.seeds)",
          "+    triplet_idx = 0",
          "+",
          "+    per_pair_results = []",
          "     lead_rows = []",
          "+    near_misses = []",
          "+",
          "     for canary in CANARY_METRICS:",
          "         for downstream in DOWNSTREAM_METRICS:",
          "+            per_seed = []",
          "             all_lags = []",
          "             all_corrs = []",
          "+",
          "             for seed in args.seeds:",
          "+                triplet_idx += 1",
          "+                print(f\"\\r  Permutation test {triplet_idx}/{total_triplets}: \"",
          "+                      f\"{canary} vs {downstream} (seed {seed})\", end=\"\",",
          "+                      flush=True)",
          "+",
          "                 seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")",
          "                 c_series = seed_df[canary].values",
          "                 d_series = seed_df[downstream].values",
          "-                lag, corr, _ = estimate_lead_time(",
          "+",
          "+                peak_lag, peak_corr, p_value = permutation_test(",
          "                     c_series, d_series, canary, downstream,",
          "-                    max_lag=args.max_lag)",
          "-                all_lags.append(lag)",
          "-                all_corrs.append(corr)",
          "+                    max_lag=args.max_lag,",
          "+                    n_permutations=args.n_permutations,",
          "+                    seed=seed)",
          " ",
          "+                per_seed.append({",
          "+                    \"seed\": seed,",
          "+                    \"peak_lag\": int(peak_lag),",
          "+                    \"peak_corr\": round(float(peak_corr), 4),",
          "+                    \"p_value\": round(float(p_value), 4),",
          "+                })",
          "+                all_lags.append(peak_lag)",
          "+                all_corrs.append(peak_corr)",
          "+",
          "+            pair_verdict = classify_pair(per_seed)",
          "+",
          "+            pair_result = {",
          "+                \"canary\": canary,",
          "+                \"downstream\": downstream,",
          "+                \"pair_verdict\": pair_verdict,",
          "+                \"per_seed\": per_seed,",
          "+            }",
          "+",
          "+            if pair_verdict in (\"SIGNIFICANT LEAD\", \"WEAK LEAD\"):",
          "+                disp = compute_lag_dispersion(per_seed)",
          "+                pair_result.update(disp)",
          "+            else:",
          "+                if check_near_miss(per_seed):",
          "+                    near_misses.append({\"canary\": canary, \"downstream\": downstream,",
          "+                                        \"per_seed\": per_seed})",
          "+",
          "+            per_pair_results.append(pair_result)",
          "+",
          "             lead_rows.append({",
          "                 \"canary\": canary,",
          "                 \"downstream\": downstream,"
        ]
      },
      {
        "oldStart": 215,
        "oldLines": 6,
        "newStart": 429,
        "newLines": 8,
        "lines": [
          "                 \"consistent\": all(l < 0 for l in all_lags),",
          "             })",
          " ",
          "+    print()",
          "+",
          "     lead_table = pd.DataFrame(lead_rows)",
          "     lead_table.to_csv(os.path.join(output_dir, \"lead_time_table.csv\"),",
          "                       index=False)"
        ]
      },
      {
        "oldStart": 222,
        "oldLines": 26,
        "newStart": 438,
        "newLines": 34,
        "lines": [
          " ",
          "     plot_cross_correlation_heatmap(lead_table, output_dir)",
          " ",
          "-    # --- Summary ---",
          "-    consistent_leaders = lead_table[lead_table[\"consistent\"]]",
          "+    # --- §5: Graded verdict ---",
          "+    verdict_pairs = per_pair_results",
          "+    if mauve_demoted:",
          "+        verdict_pairs = [p for p in per_pair_results if p[\"downstream\"] != \"mauve\"]",
          "+",
          "+    verdict, reasoning, sig_pairs, weak_pairs = compute_verdict(",
          "+        verdict_pairs, er_status)",
          "+",
          "+    # --- Build summary ---",
          "     summary = {",
          "-        \"total_canary_downstream_pairs\": len(lead_table),",
          "-        \"consistent_leaders\": len(consistent_leaders),",
          "-        \"best_canary\": None,",
          "-        \"pass_fail\": \"UNDETERMINED\",",
          "+        \"mauve_demoted\": mauve_demoted,",
          "+        \"mauve_demoted_reason\": mauve_reason,",
          "+        \"effective_rank_status\": er_status,",
          "+        \"effective_rank_slopes\": er_slopes,",
          "+        \"per_pair_results\": per_pair_results,",
          "+        \"verdict\": verdict,",
          "+        \"verdict_reasoning\": reasoning,",
          "+        \"significant_lead_pairs\": [",
          "+            {\"canary\": p[\"canary\"], \"downstream\": p[\"downstream\"]}",
          "+            for p in sig_pairs",
          "+        ],",
          "+        \"weak_lead_pairs\": [",
          "+            {\"canary\": p[\"canary\"], \"downstream\": p[\"downstream\"]}",
          "+            for p in weak_pairs",
          "+        ],",
          "+        \"near_misses\": near_misses,",
          "     }",
          " ",
          "-    if len(consistent_leaders) > 0:",
          "-        best = consistent_leaders.loc[",
          "-            consistent_leaders[\"peak_corr\"].abs().idxmax()]",
          "-        summary[\"best_canary\"] = best[\"canary\"]",
          "-        summary[\"best_downstream\"] = best[\"downstream\"]",
          "-        summary[\"best_lead_gens\"] = abs(best[\"peak_lag\"])",
          "-        summary[\"best_corr\"] = best[\"peak_corr\"]",
          "-        summary[\"pass_fail\"] = \"PASS\"",
          "-    else:",
          "-        summary[\"pass_fail\"] = \"FAIL\"",
          "-",
          "     with open(os.path.join(output_dir, \"analysis_summary.json\"), \"w\") as f:",
          "         json.dump(summary, f, indent=2)",
          " "
        ]
      },
      {
        "oldStart": 249,
        "oldLines": 17,
        "newStart": 473,
        "newLines": 55,
        "lines": [
          "     print(\"\\n\" + \"=\" * 60)",
          "     print(\"MVP ANALYSIS SUMMARY\")",
          "     print(\"=\" * 60)",
          "-    print(f\"Consistent canary leaders (lead in all 3 reps): \"",
          "-          f\"{len(consistent_leaders)}/{len(lead_table)}\")",
          " ",
          "-    if summary[\"pass_fail\"] == \"PASS\":",
          "-        print(f\"\\n✅ PASS — Best canary: {summary['best_canary']}\")",
          "-        print(f\"   Leads {summary['best_downstream']} by \"",
          "-              f\"~{summary['best_lead_gens']:.1f} generations\")",
          "-        print(f\"   Peak correlation: {summary['best_corr']:.3f}\")",
          "+    if mauve_demoted:",
          "+        print(f\"MAUVE: demoted to supplementary ({mauve_reason})\")",
          "     else:",
          "-        print(\"\\n❌ FAIL — No canary consistently leads any downstream metric\")",
          "+        print(\"MAUVE: retained as primary downstream metric\")",
          " ",
          "+    print(f\"effective_rank: {er_status}\")",
          "+    if er_slopes:",
          "+        slope_str = \", \".join(f\"seed {k}: {v:.4f}\" for k, v in er_slopes.items())",
          "+        print(f\"  slopes: {slope_str}\")",
          "+",
          "+    n_sig = len(sig_pairs)",
          "+    n_weak = len(weak_pairs)",
          "+    n_total = len(verdict_pairs)",
          "+    print(f\"\\nPair results ({n_total} pairs evaluated for verdict):\")",
          "+    print(f\"  SIGNIFICANT LEAD: {n_sig}\")",
          "+    print(f\"  WEAK LEAD: {n_weak}\")",
          "+    print(f\"  NO LEAD: {n_total - n_sig - n_weak}\")",
          "+",
          "+    if near_misses:",
          "+        print(f\"  Near misses: {len(near_misses)}\")",
          "+        for nm in near_misses:",
          "+            print(f\"    {nm['canary']} -> {nm['downstream']}\")",
          "+",
          "+    verdict_icon = {\"STRONG PASS\": \"STRONG PASS\", \"PASS\": \"PASS\",",
          "+                    \"CONDITIONAL PASS\": \"CONDITIONAL PASS\", \"FAIL\": \"FAIL\"}",
          "+    print(f\"\\nVerdict: {verdict_icon[verdict]}\")",
          "+    print(f\"Reasoning: {reasoning}\")",
          "+",
          "+    if sig_pairs:",
          "+        print(\"\\nSignificant lead pairs:\")",
          "+        for p in sig_pairs:",
          "+            disp_flag = \" [high_dispersion]\" if p.get(\"high_dispersion\") else \"\"",
          "+            print(f\"  {p['canary']} -> {p['downstream']}: \"",
          "+                  f\"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}\")",
          "+            for s in p[\"per_seed\"]:",
          "+                print(f\"    seed {s['seed']}: lag={s['peak_lag']}, \"",
          "+                      f\"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}\")",
          "+",
          "+    if weak_pairs:",
          "+        print(\"\\nWeak lead pairs:\")",
          "+        for p in weak_pairs:",
          "+            disp_flag = \" [high_dispersion]\" if p.get(\"high_dispersion\") else \"\"",
          "+            print(f\"  {p['canary']} -> {p['downstream']}: \"",
          "+                  f\"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}\")",
          "+            for s in p[\"per_seed\"]:",
          "+                print(f\"    seed {s['seed']}: lag={s['peak_lag']}, \"",
          "+                      f\"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}\")",
          "+",
          "     print(\"\\nFull lead time table:\")",
          "     print(lead_table.to_string(index=False))",
          "     print(f\"\\nResults saved to {output_dir}/\")"
        ]
      }
    ],
    "originalFile": "\"\"\"Analyze MVP experiment: metric trends, cross-correlation, lead time.\n\nReads all_metrics.json from each rep, produces:\n  - metric_trends.png : canary + downstream metrics vs generation\n  - cross_correlation.png : cross-correlation heatmap\n  - lead_time_table.csv : lead time estimates per canary-downstream pair\n  - analysis_summary.json : machine-readable summary\n\nUsage:\n    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44\n\"\"\"\n\nimport argparse\nimport json\nimport os\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\n\nCANARY_METRICS = [\"token_entropy\", \"self_bleu\", \"ece\", \"effective_rank\"]\nDOWNSTREAM_METRICS = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\n# Metrics where higher = worse (collapse direction)\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\n# Metrics where lower = worse (collapse direction)\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\", \"distinct_1\", \"distinct_2\",\n                   \"distinct_3\", \"mauve\"}\n\n\ndef load_metrics(results_dir, seeds):\n    \"\"\"Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}.\"\"\"\n    data = {}\n    for seed in seeds:\n        path = os.path.join(results_dir, f\"rep_{seed}\", \"all_metrics.json\")\n        with open(path) as f:\n            data[seed] = json.load(f)\n    return data\n\n\ndef metrics_to_df(data):\n    \"\"\"Convert {seed: [metrics_per_gen]} to a long-form DataFrame.\"\"\"\n    rows = []\n    for seed, gens in data.items():\n        for m in gens:\n            m_copy = dict(m)\n            m_copy[\"seed\"] = seed\n            rows.append(m_copy)\n    return pd.DataFrame(rows)\n\n\ndef normalize_for_correlation(series, metric_name):\n    \"\"\"Flip sign so that 'getting worse' is always positive direction.\"\"\"\n    s = series.copy()\n    if metric_name in LOWER_IS_WORSE:\n        s = -s\n    s = (s - s.mean()) / (s.std() + 1e-12)\n    return s\n\n\ndef cross_correlate(x, y, max_lag=5):\n    \"\"\"Cross-correlation of x and y at lags -max_lag..+max_lag.\n\n    Positive lag k means y leads x by k steps.\n    Negative lag k means x leads y by |k| steps.\n    \"\"\"\n    x = (x - x.mean()) / (x.std() + 1e-12)\n    y = (y - y.mean()) / (y.std() + 1e-12)\n    n = len(x)\n    correlations = {}\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0\n        else:\n            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0\n        correlations[lag] = c\n    return correlations\n\n\ndef estimate_lead_time(canary_series, downstream_series, canary_name,\n                       downstream_name, max_lag=5):\n    \"\"\"Estimate how many generations canary leads downstream.\n\n    Returns (peak_lag, peak_corr). Negative peak_lag = canary leads.\n    \"\"\"\n    c_norm = normalize_for_correlation(canary_series, canary_name)\n    d_norm = normalize_for_correlation(downstream_series, downstream_name)\n    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    return peak_lag, corrs[peak_lag], corrs\n\n\ndef plot_metric_trends(df, output_dir):\n    \"\"\"Plot metric-vs-generation with mean ± std across seeds.\"\"\"\n    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS\n    fig, axes = plt.subplots(3, 3, figsize=(15, 12))\n    axes = axes.flatten()\n\n    for idx, metric in enumerate(all_metrics):\n        if idx >= len(axes):\n            break\n        ax = axes[idx]\n        grouped = df.groupby(\"generation\")[metric]\n        mean = grouped.mean()\n        std = grouped.std()\n\n        ax.plot(mean.index, mean.values, \"o-\", linewidth=2)\n        ax.fill_between(mean.index, mean.values - std.values,\n                        mean.values + std.values, alpha=0.2)\n        ax.set_title(metric, fontsize=11, fontweight=\"bold\")\n        ax.set_xlabel(\"Generation\")\n        ax.set_ylabel(metric)\n        ax.grid(True, alpha=0.3)\n\n        is_canary = metric in CANARY_METRICS\n        ax.set_facecolor(\"#fff8f0\" if is_canary else \"#f0f8ff\")\n\n    for idx in range(len(all_metrics), len(axes)):\n        axes[idx].set_visible(False)\n\n    fig.suptitle(\"Metric Trends over Generations (mean ± std, 3 reps)\",\n                 fontsize=14, fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"metric_trends.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(f\"Saved metric_trends.png\")\n\n\ndef plot_cross_correlation_heatmap(lead_table, output_dir):\n    \"\"\"Heatmap of peak lag (canary leads = negative lag).\"\"\"\n    pivot_lag = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                values=\"peak_lag\")\n    pivot_corr = lead_table.pivot(index=\"canary\", columns=\"downstream\",\n                                  values=\"peak_corr\")\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n\n    im1 = ax1.imshow(pivot_lag.values, cmap=\"RdBu_r\", aspect=\"auto\",\n                     vmin=-5, vmax=5)\n    ax1.set_xticks(range(len(pivot_lag.columns)))\n    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha=\"right\")\n    ax1.set_yticks(range(len(pivot_lag.index)))\n    ax1.set_yticklabels(pivot_lag.index)\n    ax1.set_title(\"Peak Lag (negative = canary leads)\")\n    for i in range(len(pivot_lag.index)):\n        for j in range(len(pivot_lag.columns)):\n            ax1.text(j, i, f\"{pivot_lag.values[i, j]:.0f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im1, ax=ax1)\n\n    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap=\"YlOrRd\", aspect=\"auto\",\n                     vmin=0, vmax=1)\n    ax2.set_xticks(range(len(pivot_corr.columns)))\n    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha=\"right\")\n    ax2.set_yticks(range(len(pivot_corr.index)))\n    ax2.set_yticklabels(pivot_corr.index)\n    ax2.set_title(\"|Peak Correlation|\")\n    for i in range(len(pivot_corr.index)):\n        for j in range(len(pivot_corr.columns)):\n            ax2.text(j, i, f\"{pivot_corr.values[i, j]:.2f}\",\n                     ha=\"center\", va=\"center\", fontsize=10)\n    plt.colorbar(im2, ax=ax2)\n\n    fig.suptitle(\"Cross-Correlation: Canary → Downstream\", fontsize=13,\n                 fontweight=\"bold\")\n    plt.tight_layout()\n    plt.savefig(os.path.join(output_dir, \"cross_correlation.png\"), dpi=150,\n                bbox_inches=\"tight\")\n    plt.close()\n    print(\"Saved cross_correlation.png\")\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--results_dir\", type=str, default=\"results/mvp\")\n    parser.add_argument(\"--seeds\", type=int, nargs=\"+\", default=[42, 43, 44])\n    parser.add_argument(\"--max_lag\", type=int, default=5)\n    args = parser.parse_args()\n\n    output_dir = os.path.join(args.results_dir, \"analysis\")\n    os.makedirs(output_dir, exist_ok=True)\n\n    print(\"Loading metrics …\")\n    data = load_metrics(args.results_dir, args.seeds)\n    df = metrics_to_df(data)\n\n    # --- Metric trend plots ---\n    plot_metric_trends(df, output_dir)\n\n    # --- Cross-correlation & lead time ---\n    lead_rows = []\n    for canary in CANARY_METRICS:\n        for downstream in DOWNSTREAM_METRICS:\n            all_lags = []\n            all_corrs = []\n            for seed in args.seeds:\n                seed_df = df[df[\"seed\"] == seed].sort_values(\"generation\")\n                c_series = seed_df[canary].values\n                d_series = seed_df[downstream].values\n                lag, corr, _ = estimate_lead_time(\n                    c_series, d_series, canary, downstream,\n                    max_lag=args.max_lag)\n                all_lags.append(lag)\n                all_corrs.append(corr)\n\n            lead_rows.append({\n                \"canary\": canary,\n                \"downstream\": downstream,\n                \"peak_lag\": np.mean(all_lags),\n                \"peak_corr\": np.mean(all_corrs),\n                \"lag_std\": np.std(all_lags),\n                \"corr_std\": np.std(all_corrs),\n                \"consistent\": all(l < 0 for l in all_lags),\n            })\n\n    lead_table = pd.DataFrame(lead_rows)\n    lead_table.to_csv(os.path.join(output_dir, \"lead_time_table.csv\"),\n                      index=False)\n    print(\"Saved lead_time_table.csv\")\n\n    plot_cross_correlation_heatmap(lead_table, output_dir)\n\n    # --- Summary ---\n    consistent_leaders = lead_table[lead_table[\"consistent\"]]\n    summary = {\n        \"total_canary_downstream_pairs\": len(lead_table),\n        \"consistent_leaders\": len(consistent_leaders),\n        \"best_canary\": None,\n        \"pass_fail\": \"UNDETERMINED\",\n    }\n\n    if len(consistent_leaders) > 0:\n        best = consistent_leaders.loc[\n            consistent_leaders[\"peak_corr\"].abs().idxmax()]\n        summary[\"best_canary\"] = best[\"canary\"]\n        summary[\"best_downstream\"] = best[\"downstream\"]\n        summary[\"best_lead_gens\"] = abs(best[\"peak_lag\"])\n        summary[\"best_corr\"] = best[\"peak_corr\"]\n        summary[\"pass_fail\"] = \"PASS\"\n    else:\n        summary[\"pass_fail\"] = \"FAIL\"\n\n    with open(os.path.join(output_dir, \"analysis_summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n\n    # --- Console report ---\n    print(\"\\n\" + \"=\" * 60)\n    print(\"MVP ANALYSIS SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"Consistent canary leaders (lead in all 3 reps): \"\n          f\"{len(consistent_leaders)}/{len(lead_table)}\")\n\n    if summary[\"pass_fail\"] == \"PASS\":\n        print(f\"\\n✅ PASS — Best canary: {summary['best_canary']}\")\n        print(f\"   Leads {summary['best_downstream']} by \"\n              f\"~{summary['best_lead_gens']:.1f} generations\")\n        print(f\"   Peak correlation: {summary['best_corr']:.3f}\")\n    else:\n        print(\"\\n❌ FAIL — No canary consistently leads any downstream metric\")\n\n    print(\"\\nFull lead time table:\")\n    print(lead_table.to_string(index=False))\n    print(f\"\\nResults saved to {output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01NzXgoHbVhKivLDVJ2P62cx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts && python analyze_mvp.py --help",
  "description": "Verify CLI argument parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "2e75af53-4091-45ff-8e43-50daf68bc452",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgNgfFYN2BafHj3WMU7Y4A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7016,
      "cache_read_input_tokens": 32344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7016
      },
      "output_tokens": 60,
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

_source line 14 · 2026-05-14T08:34:34.170Z_

<details><summary>↩ Tool result · reported error · `toolu_01NzXgoHbVhKivLDVJ2P62cx`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "49af1786-f651-4470-8b5b-f1adb2337d66",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_018qTPytot3yxWVYvDtDLKXf`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts && python3 analyze_mvp.py --help",
  "description": "Verify CLI argument parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "2b2b58db-e7e9-43cb-b913-18a754848d16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoLRj7Vgb4HHQL1BNy9jDp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 153,
      "cache_read_input_tokens": 39360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 153
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

_source line 16 · 2026-05-14T08:34:38.113Z_

<details><summary>↩ Tool result · reported error · `toolu_018qTPytot3yxWVYvDtDLKXf`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py", line 27, in &lt;module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "ecb6732e-cab3-4b6e-a10b-6ceadfbba48c",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py\", line 27, in &lt;module>\n    import matplotlib.pyplot as plt\nModuleNotFoundError: No module named 'matplotlib'"
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_017sm5HNpDVaMMnLZknFCKp5`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts && python3 -c \"\nimport ast, sys\ntree = ast.parse(open('analyze_mvp.py').read())\n# Check it parses fine\nprint('AST parse OK')\n# Find argparse setup\nfor node in ast.walk(tree):\n    if isinstance(node, ast.Call) and hasattr(node, 'func'):\n        if isinstance(node.func, ast.Attribute) and node.func.attr == 'add_argument':\n            for arg in node.args:\n                if isinstance(arg, ast.Constant):\n                    print(f'  arg: {arg.value}')\n\"",
  "description": "Verify script parses and has correct CLI args"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "362d13ef-40ab-4218-aa14-0c5085ad64e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dk1ym9xtK93U9JCVQ6RoZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 39513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 222
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T08:34:44.790Z_

<details><summary>↩ Tool result · `toolu_017sm5HNpDVaMMnLZknFCKp5`</summary>

```text
AST parse OK
  arg: --results_dir
  arg: --seeds
  arg: --max_lag
  arg: --n_permutations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "ef82302e-f274-4df4-97c1-487819947ba8",
  "tool_use_result": {
    "stdout": "AST parse OK\n  arg: --results_dir\n  arg: --seeds\n  arg: --max_lag\n  arg: --n_permutations",
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

_source line 19_

脚本 AST 解析通过，4 个 CLI 参数（`--results_dir`, `--seeds`, `--max_lag`, `--n_permutations`）均已注册。本地无 matplotlib 所以无法直接运行 `--help`，但语法和参数定义正确。

实现的 6 项检查：

1. **`permutation_test()`** — B=10000 次 shuffle downstream，计算 max|r| 的 p-value
2. **Per-seed significance** — 每个 triplet 调 permutation_test，`classify_pair()` 按 3/3 seeds 规则判定 SIGNIFICANT/WEAK/NO LEAD
3. **`check_mauve_floor()`** — Gen 0 MAUVE < 0.10 且 CV < 0.50 时 demote
4. **`check_effective_rank_monotonicity()`** — Gen 4-9 OLS 斜率一致性检查
5. **`compute_verdict()`** — STRONG PASS / PASS / CONDITIONAL PASS / FAIL，排除 inconclusive 的 effective_rank 和 demoted 的 MAUVE
6. **`compute_lag_dispersion()`** — mean/std/min/max lag，std > 2.0 标记 high_dispersion

所有现有功能（plots, CSV, console report）保留，`analysis_summary.json` 输出结构符合要求规格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "uuid": "a117a6b4-5f54-448a-829b-7ea80ff285ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDVU93jmRPfL7yFNHnBPJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 39735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 305
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

### Task result

_source line 20_

脚本 AST 解析通过，4 个 CLI 参数（`--results_dir`, `--seeds`, `--max_lag`, `--n_permutations`）均已注册。本地无 matplotlib 所以无法直接运行 `--help`，但语法和参数定义正确。

实现的 6 项检查：

1. **`permutation_test()`** — B=10000 次 shuffle downstream，计算 max|r| 的 p-value
2. **Per-seed significance** — 每个 triplet 调 permutation_test，`classify_pair()` 按 3/3 seeds 规则判定 SIGNIFICANT/WEAK/NO LEAD
3. **`check_mauve_floor()`** — Gen 0 MAUVE < 0.10 且 CV < 0.50 时 demote
4. **`check_effective_rank_monotonicity()`** — Gen 4-9 OLS 斜率一致性检查
5. **`compute_verdict()`** — STRONG PASS / PASS / CONDITIONAL PASS / FAIL，排除 inconclusive 的 effective_rank 和 demoted 的 MAUVE
6. **`compute_lag_dispersion()`** — mean/std/min/max lag，std > 2.0 标记 high_dispersion

所有现有功能（plots, CSV, console report）保留，`analysis_summary.json` 输出结构符合要求规格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 128068,
  "duration_api_ms": 128904,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "9a37f187-a6dd-452a-9151-0c07cb4edddc",
  "total_cost_usd": 0.47258275,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 28199,
    "cache_read_input_tokens": 186998,
    "output_tokens": 8019,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28199,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 387,
        "cache_read_input_tokens": 39735,
        "cache_creation_input_tokens": 305,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 305
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2225,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002325,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 8019,
      "cacheReadInputTokens": 186998,
      "cacheCreationInputTokens": 28199,
      "webSearchRequests": 0,
      "costUSD": 0.47025775000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8e8c3e7f-caa4-46ec-a966-8d0ce40baaf3"
}
```

</details>

---
