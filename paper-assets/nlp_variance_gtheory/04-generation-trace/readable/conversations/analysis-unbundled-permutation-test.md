# analysis unbundled permutation test

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_unbundled_permutation_test_20260522T101608.jsonl`
- **Structured JSON:** [`07ba2a482ad0d7755e29.json`](../../sessions/07/07ba2a482ad0d7755e29.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-22T10:17:07.393587+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for bench in mmlu arc hellaswag gsm8k math; do echo \"=== $bench ===\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/bootstrap_ci_${bench}.json 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); c=d['components']['item_id']; print(f\\\"point={c.get('point',c.get('variance_pct'))}, ci=[{c['ci_lower']}, {c['ci_upper']}]\\\")\" 2>&1; done",
  "description": "Read bootstrap CI files for item_id component"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608",
  "tool": "Bash",
  "tool_args": {
    "command": "for bench in mmlu arc hellaswag gsm8k math; do echo \"=== $bench ===\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/bootstrap_ci_${bench}.json 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); c=d['components']['item_id']; print(f\\\"point={c.get('point',c.get('variance_pct'))}, ci=[{c['ci_lower']}, {c['ci_upper']}]\\\")\" 2>&1; done",
    "description": "Read bootstrap CI files for item_id component"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T10:17:07.393877+00:00_

=== mmlu ===
point=None, ci=[33.0499, 42.4259]
=== arc ===
point=None, ci=[29.9028, 45.2689]
=== hellaswag ===
point=None, ci=[28.9599, 39.3605]
=== gsm8k ===
point=None, ci=[13.4919, 20.1842]
=== math ===
point=None, ci=[20.5617, 26.9761]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:17:07.394057+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat << 'PYEOF' | python3\nimport json\nimport numpy as np\nfrom itertools import combinations\n\n# Data\nbenchmarks = ['mmlu', 'arc', 'hellaswag', 'gsm8k', 'math']\nvalues = {'mmlu': 37.9, 'arc': 37.9, 'hellaswag': 34.3, 'gsm8k': 16.9, 'math': 24.0}\n\n# Exact bootstrap CIs from files\nci_bounds = {\n    'mmlu': (33.0499, 42.4259),\n    'arc': (29.9028, 45.2689),\n    'hellaswag': (28.9599, 39.3605),\n    'gsm8k': (13.4919, 20.1842),\n    'math': (20.5617, 26.9761),\n}\n\nmc = ['mmlu', 'arc', 'hellaswag']\nff = ['gsm8k', 'math']\n\nmc_vals = [values[b] for b in mc]\nff_vals = [values[b] for b in ff]\nmc_mean = np.mean(mc_vals)\nff_mean = np.mean(ff_vals)\nobserved_diff = abs(mc_mean - ff_mean)\n\n# === Exhaustive Permutation Test ===\nall_vals = [values[b] for b in benchmarks]\nall_diffs = []\nfor combo in combinations(range(5), 2):\n    group2 = [all_vals[i] for i in combo]\n    group1 = [all_vals[i] for i in range(5) if i not in combo]\n    diff = abs(np.mean(group1) - np.mean(group2))\n    all_diffs.append(round(diff, 4))\n\nn_extreme = sum(1 for d in all_diffs if d >= observed_diff - 1e-9)\np_value = n_extreme / len(all_diffs)\n\nprint(f\"Observed diff: {observed_diff:.4f}\")\nprint(f\"All diffs: {sorted(all_diffs, reverse=True)}\")\nprint(f\"n_extreme: {n_extreme}, p_value: {p_value:.2f}\")\n\n# === Cohen's d with item-level propagated CI ===\ns_pooled = np.sqrt((np.var(mc_vals, ddof=1) * (len(mc_vals)-1) + np.var(ff_vals, ddof=1) * (len(ff_vals)-1)) / (len(mc_vals) + len(ff_vals) - 2))\nd_point = (mc_mean - ff_mean) / s_pooled\n\nprint(f\"\\nCohen's d point: {d_point:.4f}, s_pooled: {s_pooled:.4f}\")\nprint(f\"MC mean: {mc_mean:.4f}, FF mean: {ff_mean:.4f}\")\n\n# Bootstrap CI\nnp.random.seed(42)\nn_boot = 10000\nse = {}\nfor b in benchmarks:\n    lo, hi = ci_bounds[b]\n    se[b] = (hi - lo) / (2 * 1.96)\n\nd_boots = []\nfor _ in range(n_boot):\n    sim = {b: np.random.normal(values[b], se[b]) for b in benchmarks}\n    mc_sim = [sim[b] for b in mc]\n    ff_sim = [sim[b] for b in ff]\n    mc_m = np.mean(mc_sim)\n    ff_m = np.mean(ff_sim)\n    sp = np.sqrt((np.var(mc_sim, ddof=1) * 2 + np.var(ff_sim, ddof=1) * 1) / 3)\n    if sp > 0.01:\n        d_boots.append((mc_m - ff_m) / sp)\n\nci_lo = np.percentile(d_boots, 2.5)\nci_hi = np.percentile(d_boots, 97.5)\nprint(f\"Bootstrap CI: [{ci_lo:.4f}, {ci_hi:.4f}] (n_valid={len(d_boots)})\")\n\n# === Save ===\nresult = {\n    \"unbundled_item_id_pct\": {b: values[b] for b in benchmarks},\n    \"permutation_test\": {\n        \"observed_diff\": round(observed_diff, 4),\n        \"n_permutations\": 10,\n        \"n_extreme\": n_extreme,\n        \"p_value\": round(p_value, 4),\n        \"all_permutation_diffs\": sorted(all_diffs, reverse=True)\n    },\n    \"cohens_d\": {\n        \"point\": round(d_point, 4),\n        \"ci_item_level\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"n_bootstrap\": 10000,\n        \"mc_mean\": round(mc_mean, 4),\n        \"ff_mean\": round(ff_mean, 4),\n        \"s_pooled\": round(s_pooled, 4)\n    }\n}\n\nout_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/unbundled_permutation_test.json\"\nwith open(out_path, 'w') as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF",
  "description": "Run permutation test and Cohen's d analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608",
  "tool": "Bash",
  "tool_args": {
    "command": "cat << 'PYEOF' | python3\nimport json\nimport numpy as np\nfrom itertools import combinations\n\n# Data\nbenchmarks = ['mmlu', 'arc', 'hellaswag', 'gsm8k', 'math']\nvalues = {'mmlu': 37.9, 'arc': 37.9, 'hellaswag': 34.3, 'gsm8k': 16.9, 'math': 24.0}\n\n# Exact bootstrap CIs from files\nci_bounds = {\n    'mmlu': (33.0499, 42.4259),\n    'arc': (29.9028, 45.2689),\n    'hellaswag': (28.9599, 39.3605),\n    'gsm8k': (13.4919, 20.1842),\n    'math': (20.5617, 26.9761),\n}\n\nmc = ['mmlu', 'arc', 'hellaswag']\nff = ['gsm8k', 'math']\n\nmc_vals = [values[b] for b in mc]\nff_vals = [values[b] for b in ff]\nmc_mean = np.mean(mc_vals)\nff_mean = np.mean(ff_vals)\nobserved_diff = abs(mc_mean - ff_mean)\n\n# === Exhaustive Permutation Test ===\nall_vals = [values[b] for b in benchmarks]\nall_diffs = []\nfor combo in combinations(range(5), 2):\n    group2 = [all_vals[i] for i in combo]\n    group1 = [all_vals[i] for i in range(5) if i not in combo]\n    diff = abs(np.mean(group1) - np.mean(group2))\n    all_diffs.append(round(diff, 4))\n\nn_extreme = sum(1 for d in all_diffs if d >= observed_diff - 1e-9)\np_value = n_extreme / len(all_diffs)\n\nprint(f\"Observed diff: {observed_diff:.4f}\")\nprint(f\"All diffs: {sorted(all_diffs, reverse=True)}\")\nprint(f\"n_extreme: {n_extreme}, p_value: {p_value:.2f}\")\n\n# === Cohen's d with item-level propagated CI ===\ns_pooled = np.sqrt((np.var(mc_vals, ddof=1) * (len(mc_vals)-1) + np.var(ff_vals, ddof=1) * (len(ff_vals)-1)) / (len(mc_vals) + len(ff_vals) - 2))\nd_point = (mc_mean - ff_mean) / s_pooled\n\nprint(f\"\\nCohen's d point: {d_point:.4f}, s_pooled: {s_pooled:.4f}\")\nprint(f\"MC mean: {mc_mean:.4f}, FF mean: {ff_mean:.4f}\")\n\n# Bootstrap CI\nnp.random.seed(42)\nn_boot = 10000\nse = {}\nfor b in benchmarks:\n    lo, hi = ci_bounds[b]\n    se[b] = (hi - lo) / (2 * 1.96)\n\nd_boots = []\nfor _ in range(n_boot):\n    sim = {b: np.random.normal(values[b], se[b]) for b in benchmarks}\n    mc_sim = [sim[b] for b in mc]\n    ff_sim = [sim[b] for b in ff]\n    mc_m = np.mean(mc_sim)\n    ff_m = np.mean(ff_sim)\n    sp = np.sqrt((np.var(mc_sim, ddof=1) * 2 + np.var(ff_sim, ddof=1) * 1) / 3)\n    if sp > 0.01:\n        d_boots.append((mc_m - ff_m) / sp)\n\nci_lo = np.percentile(d_boots, 2.5)\nci_hi = np.percentile(d_boots, 97.5)\nprint(f\"Bootstrap CI: [{ci_lo:.4f}, {ci_hi:.4f}] (n_valid={len(d_boots)})\")\n\n# === Save ===\nresult = {\n    \"unbundled_item_id_pct\": {b: values[b] for b in benchmarks},\n    \"permutation_test\": {\n        \"observed_diff\": round(observed_diff, 4),\n        \"n_permutations\": 10,\n        \"n_extreme\": n_extreme,\n        \"p_value\": round(p_value, 4),\n        \"all_permutation_diffs\": sorted(all_diffs, reverse=True)\n    },\n    \"cohens_d\": {\n        \"point\": round(d_point, 4),\n        \"ci_item_level\": [round(ci_lo, 4), round(ci_hi, 4)],\n        \"n_bootstrap\": 10000,\n        \"mc_mean\": round(mc_mean, 4),\n        \"ff_mean\": round(ff_mean, 4),\n        \"s_pooled\": round(s_pooled, 4)\n    }\n}\n\nout_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/unbundled_permutation_test.json\"\nwith open(out_path, 'w') as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF",
    "description": "Run permutation test and Cohen's d analysis"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T10:17:07.394230+00:00_

Observed diff: 16.2500
All diffs: [np.float64(16.25), np.float64(12.8333), np.float64(9.8333), np.float64(9.8333), np.float64(7.6667), np.float64(4.6667), np.float64(4.6667), np.float64(1.75), np.float64(1.25), np.float64(1.25)]
n_extreme: 1, p_value: 0.10

Cohen's d point: 4.8380, s_pooled: 3.3588
MC mean: 36.7000, FF mean: 20.4500
Bootstrap CI: [2.3211, 8.1949] (n_valid=10000)

Saved to /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/unbundled_permutation_test.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T10:17:07.394360+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/unbundled_permutation_test.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/unbundled_permutation_test.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T10:17:07.394544+00:00_

1	{
2	  "unbundled_item_id_pct": {
3	    "mmlu": 37.9,
4	    "arc": 37.9,
5	    "hellaswag": 34.3,
6	    "gsm8k": 16.9,
7	    "math": 24.0
8	  },
9	  "permutation_test": {
10	    "observed_diff": 16.25,
11	    "n_permutations": 10,
12	    "n_extreme": 1,
13	    "p_value": 0.1,
14	    "all_permutation_diffs": [
15	      16.25,
16	      12.8333,
17	      9.8333,
18	      9.8333,
19	      7.6667,
20	      4.6667,
21	      4.6667,
22	      1.75,
23	      1.25,
24	      1.25
25	    ]
26	  },
27	  "cohens_d": {
28	    "point": 4.838,
29	    "ci_item_level": [
30	      2.3211,
31	      8.1949
32	    ],
33	    "n_bootstrap": 10000,
34	    "mc_mean": 36.7,
35	    "ff_mean": 20.45,
36	    "s_pooled": 3.3588
37	  }
38	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-22T10:17:07.394709+00:00_

结果已保存。

- **Permutation test**: p = 0.10（观测差 16.25 是 10 种排列中最极端的，n=5 时理论最小 p 即为 0.10）
- **Cohen's d**: 4.84 [2.32, 8.19]，CI 完全在正区间，效应量极大——unbundled item_id% 在 MC 与 FF 之间的差异方向一致且稳健

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_unbundled_permutation_test_20260522T101608"
}
```

</details>

---
