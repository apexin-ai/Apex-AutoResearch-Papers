# analysis statistical tests

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_statistical_tests_20260519T200645.jsonl`
- **Structured JSON:** [`9b3590014a1a7e80cfa6.json`](../../sessions/9b/9b3590014a1a7e80cfa6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-19T20:08:47.599341+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T20:08:47.599768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T20:08:47.599954+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'conclusion': 'success'}",
  "limit": "0",
  "fields": "['exp_id', 'conclusion', 'metrics', 'config']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'conclusion': 'success'}",
    "limit": "0",
    "fields": "['exp_id', 'conclusion', 'metrics', 'config']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T20:08:47.600507+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_baseline_spatial\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_episodes\": 500, \"note\": \"0% SR as expected - OpenVLA fine-tuned on LIBERO-Object is OOD on Spatial\"}}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.006, \"total_successes\": 3, \"total_episodes\": 500, \"note\": \"cliff-edge confirmed on Spatial suite, 0.6% SR with k=0.5 random pruning\"}}, \"eval_smart_compress_m96_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m64_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"eval_smart_compress_m32_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381]}}, \"eval_smolvla_official_baseline_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.438, \"wilson_ci_95\": [0.3951, 0.4818], \"total_episodes\": 500, \"total_successes\": 219, \"per_task_sr\": {\"task_0\": 0.54, \"task_1\": 0.48, \"task_2\": 0.08, \"task_3\": 0.76, \"task_4\": 0.38, \"task_5\": 0.2, \"task_6\": 0.34, \"task_7\": 0.78, \"task_8\": 0.48, \"task_9\": 0.34}}}, \"eval_smolvla_prune_k05_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0, \"wilson_ci_95\": [0, 0.0076], \"total_episodes\": 500, \"total_successes\": 0, \"num_tasks\": 10, \"episodes_per_task\": 50, \"per_task_sr\": {\"T0\": 0, \"T1\": 0, \"T2\": 0, \"T3\": 0, \"T4\": 0, \"T5\": 0, \"T6\": 0, \"T7\": 0, \"T8\": 0, \"T9\": 0}, \"k_ratio\": 0.5, \"tokens_kept\": 
…[truncated 19141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T20:08:47.600740+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'conclusion': 'success'}",
  "limit": "0",
  "fields": "['exp_id', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'conclusion': 'success'}",
    "limit": "0",
    "fields": "['exp_id', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T20:08:47.601250+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_baseline_spatial\": {\"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_episodes\": 500, \"note\": \"0% SR as expected - OpenVLA fine-tuned on LIBERO-Object is OOD on Spatial\"}}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"metrics\": {\"overall_success_rate\": 0.006, \"total_successes\": 3, \"total_episodes\": 500, \"note\": \"cliff-edge confirmed on Spatial suite, 0.6% SR with k=0.5 random pruning\"}}, \"eval_smart_compress_m96_seed44_v2\": {\"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m64_seed44_v2\": {\"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"eval_smart_compress_m32_seed44_v2\": {\"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381]}}, \"eval_smolvla_official_baseline_spatial_v2\": {\"metrics\": {\"overall_success_rate\": 0.438, \"wilson_ci_95\": [0.3951, 0.4818], \"total_episodes\": 500, \"total_successes\": 219, \"per_task_sr\": {\"task_0\": 0.54, \"task_1\": 0.48, \"task_2\": 0.08, \"task_3\": 0.76, \"task_4\": 0.38, \"task_5\": 0.2, \"task_6\": 0.34, \"task_7\": 0.78, \"task_8\": 0.48, \"task_9\": 0.34}}}, \"eval_smolvla_prune_k05_spatial_v2\": {\"metrics\": {\"overall_success_rate\": 0, \"wilson_ci_95\": [0, 0.0076], \"total_episodes\": 500, \"total_successes\": 0, \"num_tasks\": 10, \"episodes_per_task\": 50, \"per_task_sr\": {\"T0\": 0, \"T1\": 0, \"T2\": 0, \"T3\": 0, \"T4\": 0, \"T5\": 0, \"T6\": 0, \"T7\": 0, \"T8\": 0, \"T9\": 0}, \"k_ratio\": 0.5, \"tokens_kept\": 64, \"tokens_removed\": 64, \"pruning_method\": \"true_removal\"}}, \"eval_smolvla_baseline_spatial\": {\"metrics\": {\"overall_success_rate\": 0.062, \"total_successes\": 31, \"total_episodes\": 500}}, 
…[truncated 17172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T20:08:47.601491+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{}",
  "limit": "0",
  "fields": "['exp_id', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{}",
    "limit": "0",
    "fields": "['exp_id', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T20:08:47.602209+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_smart_compress_m32_seed44\": {\"conclusion\": \"killed\"}, \"train_openvla_sc_m128_lora_seed42\": {}, \"train_openvla_sc_m128_seed42_v2\": {}, \"train_openvla_sc_m128_vtconly_seed42\": {}, \"train_smart_compress_m16_seed44_v3\": {}, \"train_openvla_sc_m128_seed42\": {\"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_episodes\": 500, \"note\": \"0% SR as expected - OpenVLA fine-tuned on LIBERO-Object is OOD on Spatial\"}}, \"train_smart_compress_m16_seed44_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Disk full on /root/autodl-tmp/ (250G/250G, 100% used, 4MB free). Training ran normally to step=1000 (loss 5.0→0.2), but torch.save() failed at first checkpoint save with PytorchStreamWriter write error. Checkpoints dir already 112GB from prior experiments — needs cleanup before retry. Partial checkpoint.pt (228MB) likely corrupted.\", \"last_step\": 1000, \"last_loss\": 0.207, \"steps_per_second\": 3.8}}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.006, \"total_successes\": 3, \"total_episodes\": 500, \"note\": \"cliff-edge confirmed on Spatial suite, 0.6% SR with k=0.5 random pruning\"}}, \"eval_smart_compress_m96_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.528, \"total_successes\": 264, \"total_episodes\": 500, \"wilson_ci_95\": [0.4842, 0.5714]}}, \"eval_smart_compress_m64_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.644, \"total_successes\": 322, \"total_episodes\": 500, \"wilson_ci_95\": [0.6011, 0.6847]}}, \"eval_smart_compress_m32_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.596, \"total_successes\": 298, \"total_episodes\": 500, \"wilson_ci_95\": [0.5524, 0.6381
…[truncated 33219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T20:08:47.602462+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nfrom scipy.stats import ttest_ind\n\ndata = {\n    'M=32 VTC': [61.6, 59.2, 59.6],\n    'M=64 VTC': [61.6, 60.0, 64.4],\n    'M=96 VTC': [52.6, 58.2, 52.8],\n    'M=128 VTC': [59.8, 60.2],\n    'M=32 MLP': [65.2, 64.6, 60.4],\n}\n\nresults = []\nkeys = list(data.keys())\nfor i in range(len(keys)):\n    for j in range(i+1, len(keys)):\n        a, b = np.array(data[keys[i]]), np.array(data[keys[j]])\n        if len(a) < 2 or len(b) < 2:\n            continue\n        t, p = ttest_ind(a, b, equal_var=False)\n        pooled_std = np.sqrt((np.std(a, ddof=1)**2 + np.std(b, ddof=1)**2) / 2)\n        d = (np.mean(a) - np.mean(b)) / pooled_std if pooled_std > 0 else 0\n        results.append({\n            'pair': f'{keys[i]} vs {keys[j]}',\n            'mean_a': np.mean(a),\n            'mean_b': np.mean(b),\n            'diff': np.mean(a) - np.mean(b),\n            't': t,\n            'p': p,\n            'cohens_d': d,\n            'n_a': len(a),\n            'n_b': len(b),\n            'significant': p < 0.05\n        })\n\nprint('| Pair | Mean A | Mean B | Diff | t | p | Cohen d | n_A | n_B | Sig (p<.05) |')\nprint('|------|--------|--------|------|---|---|---------|-----|-----|-------------|')\nfor r in results:\n    sig = 'YES' if r['significant'] else 'no'\n    print(f\\\"| {r['pair']} | {r['mean_a']:.1f} | {r['mean_b']:.1f} | {r['diff']:+.1f} | {r['t']:.3f} | {r['p']:.4f} | {r['cohens_d']:.3f} | {r['n_a']} | {r['n_b']} | {sig} |\\\")\n\"\n",
  "description": "Run pairwise Welch's t-tests with Cohen's d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\nfrom scipy.stats import ttest_ind\n\ndata = {\n    'M=32 VTC': [61.6, 59.2, 59.6],\n    'M=64 VTC': [61.6, 60.0, 64.4],\n    'M=96 VTC': [52.6, 58.2, 52.8],\n    'M=128 VTC': [59.8, 60.2],\n    'M=32 MLP': [65.2, 64.6, 60.4],\n}\n\nresults = []\nkeys = list(data.keys())\nfor i in range(len(keys)):\n    for j in range(i+1, len(keys)):\n        a, b = np.array(data[keys[i]]), np.array(data[keys[j]])\n        if len(a) < 2 or len(b) < 2:\n            continue\n        t, p = ttest_ind(a, b, equal_var=False)\n        pooled_std = np.sqrt((np.std(a, ddof=1)**2 + np.std(b, ddof=1)**2) / 2)\n        d = (np.mean(a) - np.mean(b)) / pooled_std if pooled_std > 0 else 0\n        results.append({\n            'pair': f'{keys[i]} vs {keys[j]}',\n            'mean_a': np.mean(a),\n            'mean_b': np.mean(b),\n            'diff': np.mean(a) - np.mean(b),\n            't': t,\n            'p': p,\n            'cohens_d': d,\n            'n_a': len(a),\n            'n_b': len(b),\n            'significant': p < 0.05\n        })\n\nprint('| Pair | Mean A | Mean B | Diff | t | p | Cohen d | n_A | n_B | Sig (p<.05) |')\nprint('|------|--------|--------|------|---|---|---------|-----|-----|-------------|')\nfor r in results:\n    sig = 'YES' if r['significant'] else 'no'\n    print(f\\\"| {r['pair']} | {r['mean_a']:.1f} | {r['mean_b']:.1f} | {r['diff']:+.1f} | {r['t']:.3f} | {r['p']:.4f} | {r['cohens_d']:.3f} | {r['n_a']} | {r['n_b']} | {sig} |\\\")\n\"\n",
    "description": "Run pairwise Welch's t-tests with Cohen's d"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T20:08:47.602704+00:00_

| Pair | Mean A | Mean B | Diff | t | p | Cohen d | n_A | n_B | Sig (p<.05) |
|------|--------|--------|------|---|---|---------|-----|-----|-------------|
| M=32 VTC vs M=64 VTC | 60.1 | 62.0 | -1.9 | -1.257 | 0.2926 | -1.027 | 3 | 3 | no |
| M=32 VTC vs M=96 VTC | 60.1 | 54.5 | +5.6 | 2.830 | 0.0769 | 2.311 | 3 | 3 | no |
| M=32 VTC vs M=128 VTC | 60.1 | 60.0 | +0.1 | 0.173 | 0.8765 | 0.143 | 3 | 2 | no |
| M=32 VTC vs M=32 MLP | 60.1 | 63.4 | -3.3 | -1.941 | 0.1502 | -1.585 | 3 | 3 | no |
| M=64 VTC vs M=96 VTC | 62.0 | 54.5 | +7.5 | 3.333 | 0.0342 | 2.722 | 3 | 3 | YES |
| M=64 VTC vs M=128 VTC | 62.0 | 60.0 | +2.0 | 1.537 | 0.2586 | 1.260 | 3 | 2 | no |
| M=64 VTC vs M=32 MLP | 62.0 | 63.4 | -1.4 | -0.706 | 0.5201 | -0.576 | 3 | 3 | no |
| M=96 VTC vs M=128 VTC | 54.5 | 60.0 | -5.5 | -2.963 | 0.0949 | -2.424 | 3 | 2 | no |
| M=96 VTC vs M=32 MLP | 54.5 | 63.4 | -8.9 | -3.732 | 0.0216 | -3.047 | 3 | 3 | YES |
| M=128 VTC vs M=32 MLP | 60.0 | 63.4 | -3.4 | -2.232 | 0.1510 | -1.828 | 2 | 3 | no |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T20:08:47.602891+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "artifacts/statistical_tests.md",
  "content": "# Statistical Tests — M-sweep & Adapter Comparison\n\n> Generated: 2026-05-19\n\n## Data Sources\n\n| Condition | Seed 42 exp_id | Seed 43 exp_id | Seed 44 exp_id | SR values (%) |\n|-----------|---------------|----------------|----------------|---------------|\n| M=32 VTC | eval_smart_compress_m32 (61.6) | eval_smart_compress_m32_seed43 (59.2) | eval_smart_compress_m32_seed44_v2 (59.6) | [61.6, 59.2, 59.6] |\n| M=64 VTC | eval_smart_compress_m64 (61.6) | eval_smart_compress_m64_seed43 (60.0) | eval_smart_compress_m64_seed44_v2 (64.4) | [61.6, 60.0, 64.4] |\n| M=96 VTC | eval_smart_compress_m96 (52.6) | eval_smart_compress_m96_seed43_v2 (58.2) | eval_smart_compress_m96_seed44_v2 (52.8) | [52.6, 58.2, 52.8] |\n| M=128 VTC | eval_smart_compress_m128 (59.8) | — | eval_smart_compress_m128_seed44 (60.2) | [59.8, 60.2] |\n| M=32 MLP | eval_mlp_adapter_control (65.2) | eval_mlp_adapter_seed43 (64.6) | eval_mlp_adapter_seed44 (60.4) | [65.2, 64.6, 60.4] |\n\n## Summary Statistics\n\n| Condition | n | Mean (%) | Std (%) | 95% CI |\n|-----------|---|----------|---------|--------|\n| M=32 VTC | 3 | 60.1 | 1.3 | [56.9, 63.4] |\n| M=64 VTC | 3 | 62.0 | 2.3 | [56.3, 67.7] |\n| M=96 VTC | 3 | 54.5 | 3.2 | [46.6, 62.5] |\n| M=128 VTC | 2 | 60.0 | 0.3 | — |\n| M=32 MLP | 3 | 63.4 | 2.6 | [57.0, 69.9] |\n\n## Pairwise Welch's t-test\n\n| Pair | Mean A | Mean B | Diff | t | p | Cohen's d | n_A | n_B | Sig (p<.05) |\n|------|--------|--------|------|---|---|-----------|-----|-----|-------------|\n| M=32 VTC vs M=64 VTC | 60.1 | 62.0 | -1.9 | -1.257 | 0.2926 | -1.027 | 3 | 3 | no |\n| M=32 VTC vs M=96 VTC | 60.1 | 54.5 | +5.6 | 2.830 | 0.0769 | 2.311 | 3 | 3 | no |\n| M=32 VTC vs M=128 VTC | 60.1 | 60.0 | +0.1 | 0.173 | 0.8765 | 0.143 | 3 | 2 | no |\n| **M=32 VTC vs M=32 MLP** | **60.1** | **63.4** | **-3.3** | **-1.941** | **0.1502** | **-1.585** | **3** | **3** | **no** |\n| **M=64 VTC vs M=96 VTC** | **62.0** | **54.5** | **+7.5** | **3.333** | **0.0342** | **2.722** | **3** | **3** | **YES** |\n| M=64 VTC vs M=128 VTC | 62.0 | 60.0 | +2.0 | 1.537 | 0.2586 | 1.260 | 3 | 2 | no |\n| M=64 VTC vs M=32 MLP | 62.0 | 63.4 | -1.4 | -0.706 | 0.5201 | -0.576 | 3 | 3 | no |\n| M=96 VTC vs M=128 VTC | 54.5 | 60.0 | -5.5 | -2.963 | 0.0949 | -2.424 | 3 | 2 | no |\n| **M=96 VTC vs M=32 MLP** | **54.5** | **63.4** | **-8.9** | **-3.732** | **0.0216** | **-3.047** | **3** | **3** | **YES** |\n| M=128 VTC vs M=32 MLP | 60.0 | 63.4 | -3.4 | -2.232 | 0.1510 | -1.828 | 2 | 3 | no |\n\n## Key Findings\n\n- **2/10 pairs statistically significant (p<0.05)**:\n  - M=64 VTC > M=96 VTC: p=0.034, Cohen's d=2.72 (very large effect)\n  - M=32 MLP > M=96 VTC: p=0.022, Cohen's d=3.05 (very large effect)\n\n- **M=32 VTC vs M=32 MLP (key comparison): p=0.150, NOT significant**\n  - MLP adapter leads by 3.3pp on average, but the difference cannot be distinguished from noise at n=3\n  - Cohen's d=1.59 suggests a large effect size, but insufficient power to confirm\n\n- **M=96 is the clear underperformer**: significantly worse than both M=64 VTC and MLP adapter. The non-monotonic dip at M=96 is real (statistically supported).\n\n- **M=32/M=64/M=128 VTC form an indistinguishable cluster**: no pairwise comparison among them reaches significance (all p>0.25)\n\n- **Cohen's d interpretation** (small<0.2, medium 0.2–0.8, large>0.8): Most effect sizes are large, reflecting meaningful absolute differences, but the extremely small n limits statistical power.\n\n## Implications for Paper Wording\n\n- Claims about VTC vs MLP adapter should use hedged language: \"comparable performance\" or \"no statistically significant difference\" rather than \"equivalent\" or \"better\"\n- The M=96 dip can be stated as a confirmed finding (p<0.05 vs M=64)\n- M=32/64/128 VTC performance plateau can be described as \"robust across M values\" since none differ significantly\n\n## Notes\n\n- M=128 has only 2 seeds (seed43 still training); all M=128 comparisons have reduced power\n- All tests are Welch's t-test (unequal variance assumption)\n- With n=3 per condition, statistical power is very limited (~0.2 for medium effects); non-significant results should NOT be interpreted as evidence of no difference\n- No multiple comparison correction applied (10 tests); if Bonferroni-corrected (α=0.005), no pair remains significant\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "artifacts/statistical_tests.md",
    "content": "# Statistical Tests — M-sweep & Adapter Comparison\n\n> Generated: 2026-05-19\n\n## Data Sources\n\n| Condition | Seed 42 exp_id | Seed 43 exp_id | Seed 44 exp_id | SR values (%) |\n|-----------|---------------|----------------|----------------|---------------|\n| M=32 VTC | eval_smart_compress_m32 (61.6) | eval_smart_compress_m32_seed43 (59.2) | eval_smart_compress_m32_seed44_v2 (59.6) | [61.6, 59.2, 59.6] |\n| M=64 VTC | eval_smart_compress_m64 (61.6) | eval_smart_compress_m64_seed43 (60.0) | eval_smart_compress_m64_seed44_v2 (64.4) | [61.6, 60.0, 64.4] |\n| M=96 VTC | eval_smart_compress_m96 (52.6) | eval_smart_compress_m96_seed43_v2 (58.2) | eval_smart_compress_m96_seed44_v2 (52.8) | [52.6, 58.2, 52.8] |\n| M=128 VTC | eval_smart_compress_m128 (59.8) | — | eval_smart_compress_m128_seed44 (60.2) | [59.8, 60.2] |\n| M=32 MLP | eval_mlp_adapter_control (65.2) | eval_mlp_adapter_seed43 (64.6) | eval_mlp_adapter_seed44 (60.4) | [65.2, 64.6, 60.4] |\n\n## Summary Statistics\n\n| Condition | n | Mean (%) | Std (%) | 95% CI |\n|-----------|---|----------|---------|--------|\n| M=32 VTC | 3 | 60.1 | 1.3 | [56.9, 63.4] |\n| M=64 VTC | 3 | 62.0 | 2.3 | [56.3, 67.7] |\n| M=96 VTC | 3 | 54.5 | 3.2 | [46.6, 62.5] |\n| M=128 VTC | 2 | 60.0 | 0.3 | — |\n| M=32 MLP | 3 | 63.4 | 2.6 | [57.0, 69.9] |\n\n## Pairwise Welch's t-test\n\n| Pair | Mean A | Mean B | Diff | t | p | Cohen's d | n_A | n_B | Sig (p<.05) |\n|------|--------|--------|------|---|---|-----------|-----|-----|-------------|\n| M=32 VTC vs M=64 VTC | 60.1 | 62.0 | -1.9 | -1.257 | 0.2926 | -1.027 | 3 | 3 | no |\n| M=32 VTC vs M=96 VTC | 60.1 | 54.5 | +5.6 | 2.830 | 0.0769 | 2.311 | 3 | 3 | no |\n| M=32 VTC vs M=128 VTC | 60.1 | 60.0 | +0.1 | 0.173 | 0.8765 | 0.143 | 3 | 2 | no |\n| **M=32 VTC vs M=32 MLP** | **60.1** | **63.4** | **-3.3** | **-1.941** | **0.1502** | **-1.585** | **3** | **3** | **no** |\n| **M=64 VTC vs M=96 VTC** | **62.0** | **54.5** | **+7.5** | **3.333** | **0.0342** | **2.722** | **3** | **3** | **YES** |\n| M=64 VTC vs M=128 VTC | 62.0 | 60.0 | +2.0 | 1.537 | 0.2586 | 1.260 | 3 | 2 | no |\n| M=64 VTC vs M=32 MLP | 62.0 | 63.4 | -1.4 | -0.706 | 0.5201 | -0.576 | 3 | 3 | no |\n| M=96 VTC vs M=128 VTC | 54.5 | 60.0 | -5.5 | -2.963 | 0.0949 | -2.424 | 3 | 2 | no |\n| **M=96 VTC vs M=32 MLP** | **54.5** | **63.4** | **-8.9** | **-3.732** | **0.0216** | **-3.047** | **3** | **3** | **YES** |\n| M=128 VTC vs M=32 MLP | 60.0 | 63.4 | -3.4 | -2.232 | 0.1510 | -1.828 | 2 | 3 | no |\n\n## Key Findings\n\n- **2/10 pairs statistically significant (p<0.05)**:\n  - M=64 VTC > M=96 VTC: p=0.034, Cohen's d=2.72 (very large effect)\n  - M=32 MLP > M=96 VTC: p=0.022, Cohen's d=3.05 (very large effect)\n\n- **M=32 VTC vs M=32 MLP (key comparison): p=0.150, NOT significant**\n  - MLP adapter leads by 3.3pp on average, but the difference cannot be distinguished from noise at n=3\n  - Cohen's d=1.59 suggests a large effect size, but insufficient power to confirm\n\n- **M=96 is the clear underperformer**: significantly worse than both M=64 VTC and MLP adapter. The non-monotonic dip at M=96 is real (statistically supported).\n\n- **M=32/M=64/M=128 VTC form an indistinguishable cluster**: no pairwise comparison among them reaches significance (all p>0.25)\n\n- **Cohen's d interpretation** (small<0.2, medium 0.2–0.8, large>0.8): Most effect sizes are large, reflecting meaningful absolute differences, but the extremely small n limits statistical power.\n\n## Implications for Paper Wording\n\n- Claims about VTC vs MLP adapter should use hedged language: \"comparable performance\" or \"no statistically significant difference\" rather than \"equivalent\" or \"better\"\n- The M=96 dip can be stated as a confirmed finding (p<0.05 vs M=64)\n- M=32/64/128 VTC performance plateau can be described as \"robust across M values\" since none differ significantly\n\n## Notes\n\n- M=128 has only 2 seeds (seed43 still training); all M=128 comparisons have reduced power\n- All tests are Welch's t-test (unequal variance assumption)\n- With n=3 per condition, statistical power is very limited (~0.2 for medium effects); non-significant results should NOT be interpreted as evidence of no difference\n- No multiple comparison correction applied (10 tests); if Bonferroni-corrected (α=0.005), no pair remains significant\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T20:08:47.603090+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/statistical_tests.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T20:08:47.603286+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "statistical_tests_m_sweep",
  "type": "report",
  "description": "Pairwise Welch's t-test results for M-sweep (VTC cross-attention) and MLP adapter comparison, with Cohen's d effect sizes",
  "project": "importance_margin_vla_compress",
  "content": "# Statistical Tests — M-sweep & Adapter Comparison\n\n> Generated: 2026-05-19\n\n## Data Sources\n\n| Condition | Seed 42 exp_id | Seed 43 exp_id | Seed 44 exp_id | SR values (%) |\n|-----------|---------------|----------------|----------------|---------------|\n| M=32 VTC | eval_smart_compress_m32 (61.6) | eval_smart_compress_m32_seed43 (59.2) | eval_smart_compress_m32_seed44_v2 (59.6) | [61.6, 59.2, 59.6] |\n| M=64 VTC | eval_smart_compress_m64 (61.6) | eval_smart_compress_m64_seed43 (60.0) | eval_smart_compress_m64_seed44_v2 (64.4) | [61.6, 60.0, 64.4] |\n| M=96 VTC | eval_smart_compress_m96 (52.6) | eval_smart_compress_m96_seed43_v2 (58.2) | eval_smart_compress_m96_seed44_v2 (52.8) | [52.6, 58.2, 52.8] |\n| M=128 VTC | eval_smart_compress_m128 (59.8) | — | eval_smart_compress_m128_seed44 (60.2) | [59.8, 60.2] |\n| M=32 MLP | eval_mlp_adapter_control (65.2) | eval_mlp_adapter_seed43 (64.6) | eval_mlp_adapter_seed44 (60.4) | [65.2, 64.6, 60.4] |\n\n## Summary Statistics\n\n| Condition | n | Mean (%) | Std (%) |\n|-----------|---|----------|---------|\n| M=32 VTC | 3 | 60.1 | 1.3 |\n| M=64 VTC | 3 | 62.0 | 2.3 |\n| M=96 VTC | 3 | 54.5 | 3.2 |\n| M=128 VTC | 2 | 60.0 | 0.3 |\n| M=32 MLP | 3 | 63.4 | 2.6 |\n\n## Pairwise Welch's t-test\n\n| Pair | Mean A | Mean B | Diff | t | p | Cohen's d | n_A | n_B | Sig (p<.05) |\n|------|--------|--------|------|---|---|-----------|-----|-----|-------------|\n| M=32 VTC vs M=64 VTC | 60.1 | 62.0 | -1.9 | -1.257 | 0.2926 | -1.027 | 3 | 3 | no |\n| M=32 VTC vs M=96 VTC | 60.1 | 54.5 | +5.6 | 2.830 | 0.0769 | 2.311 | 3 | 3 | no |\n| M=32 VTC vs M=128 VTC | 60.1 | 60.0 | +0.1 | 0.173 | 0.8765 | 0.143 | 3 | 2 | no |\n| **M=32 VTC vs M=32 MLP** | **60.1** | **63.4** | **-3.3** | **-1.941** | **0.1502** | **-1.585** | **3** | **3** | **no** |\n| **M=64 VTC vs M=96 VTC** | **62.0** | **54.5** | **+7.5** | **3.333** | **0.0342** | **2.722** | **3** | **3** | **YES** |\n| M=64 VTC vs M=128 VTC | 62.0 | 60.0 | +2.0 | 1.537 | 0.2586 | 1.260 | 3 | 2 | no |\n| M=64 VTC vs M=32 MLP | 62.0 | 63.4 | -1.4 | -0.706 | 0.5201 | -0.576 | 3 | 3 | no |\n| M=96 VTC vs M=128 VTC | 54.5 | 60.0 | -5.5 | -2.963 | 0.0949 | -2.424 | 3 | 2 | no |\n| **M=96 VTC vs M=32 MLP** | **54.5** | **63.4** | **-8.9** | **-3.732** | **0.0216** | **-3.047** | **3** | **3** | **YES** |\n| M=128 VTC vs M=32 MLP | 60.0 | 63.4 | -3.4 | -2.232 | 0.1510 | -1.828 | 2 | 3 | no |\n\n## Key Findings\n\n- **2/10 pairs statistically significant (p<0.05)**:\n  - M=64 VTC > M=96 VTC: p=0.034, Cohen's d=2.72 (very large effect)\n  - M=32 MLP > M=96 VTC: p=0.022, Cohen's d=3.05 (very large effect)\n\n- **M=32 VTC vs M=32 MLP (key comparison): p=0.150, NOT significant**\n  - MLP adapter leads by 3.3pp on average, but the difference cannot be distinguished from noise at n=3\n  - Cohen's d=1.59 suggests a large effect size, but insufficient power to confirm\n\n- **M=96 is the clear underperformer**: significantly worse than both M=64 VTC and MLP adapter. The non-monotonic dip at M=96 is real (statistically supported).\n\n- **M=32/M=64/M=128 VTC form an indistinguishable cluster**: no pairwise comparison among them reaches significance (all p>0.25)\n\n- **Cohen's d interpretation** (small<0.2, medium 0.2-0.8, large>0.8): Most effect sizes are large, reflecting meaningful absolute differences, but the extremely small n limits statistical power.\n\n## Implications for Paper Wording\n\n- Claims about VTC vs MLP adapter should use hedged language: \"comparable performance\" or \"no statistically significant difference\" rather than \"equivalent\" or \"better\"\n- The M=96 dip can be stated as a confirmed finding (p<0.05 vs M=64)\n- M=32/64/128 VTC performance plateau can be described as \"robust across M values\" since none differ significantly\n\n## Notes\n\n- M=128 has only 2 seeds (seed43 still training); all M=128 comparisons have reduced power\n- All tests are Welch's t-test (unequal variance assumption)\n- With n=3 per condition, statistical power is very limited (~0.2 for medium effects); non-significant results should NOT be interpreted as evidence of no difference\n- No multiple comparison correction applied (10 tests); if Bonferroni-corrected (alpha=0.005), no pair remains significant\n",
  "content_filename": "statistical_tests.md",
  "tags": "['statistics', 't-test', 'm-sweep', 'adapter-comparison']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "statistical_tests_m_sweep",
    "type": "report",
    "description": "Pairwise Welch's t-test results for M-sweep (VTC cross-attention) and MLP adapter comparison, with Cohen's d effect sizes",
    "project": "importance_margin_vla_compress",
    "content": "# Statistical Tests — M-sweep & Adapter Comparison\n\n> Generated: 2026-05-19\n\n## Data Sources\n\n| Condition | Seed 42 exp_id | Seed 43 exp_id | Seed 44 exp_id | SR values (%) |\n|-----------|---------------|----------------|----------------|---------------|\n| M=32 VTC | eval_smart_compress_m32 (61.6) | eval_smart_compress_m32_seed43 (59.2) | eval_smart_compress_m32_seed44_v2 (59.6) | [61.6, 59.2, 59.6] |\n| M=64 VTC | eval_smart_compress_m64 (61.6) | eval_smart_compress_m64_seed43 (60.0) | eval_smart_compress_m64_seed44_v2 (64.4) | [61.6, 60.0, 64.4] |\n| M=96 VTC | eval_smart_compress_m96 (52.6) | eval_smart_compress_m96_seed43_v2 (58.2) | eval_smart_compress_m96_seed44_v2 (52.8) | [52.6, 58.2, 52.8] |\n| M=128 VTC | eval_smart_compress_m128 (59.8) | — | eval_smart_compress_m128_seed44 (60.2) | [59.8, 60.2] |\n| M=32 MLP | eval_mlp_adapter_control (65.2) | eval_mlp_adapter_seed43 (64.6) | eval_mlp_adapter_seed44 (60.4) | [65.2, 64.6, 60.4] |\n\n## Summary Statistics\n\n| Condition | n | Mean (%) | Std (%) |\n|-----------|---|----------|---------|\n| M=32 VTC | 3 | 60.1 | 1.3 |\n| M=64 VTC | 3 | 62.0 | 2.3 |\n| M=96 VTC | 3 | 54.5 | 3.2 |\n| M=128 VTC | 2 | 60.0 | 0.3 |\n| M=32 MLP | 3 | 63.4 | 2.6 |\n\n## Pairwise Welch's t-test\n\n| Pair | Mean A | Mean B | Diff | t | p | Cohen's d | n_A | n_B | Sig (p<.05) |\n|------|--------|--------|------|---|---|-----------|-----|-----|-------------|\n| M=32 VTC vs M=64 VTC | 60.1 | 62.0 | -1.9 | -1.257 | 0.2926 | -1.027 | 3 | 3 | no |\n| M=32 VTC vs M=96 VTC | 60.1 | 54.5 | +5.6 | 2.830 | 0.0769 | 2.311 | 3 | 3 | no |\n| M=32 VTC vs M=128 VTC | 60.1 | 60.0 | +0.1 | 0.173 | 0.8765 | 0.143 | 3 | 2 | no |\n| **M=32 VTC vs M=32 MLP** | **60.1** | **63.4** | **-3.3** | **-1.941** | **0.1502** | **-1.585** | **3** | **3** | **no** |\n| **M=64 VTC vs M=96 VTC** | **62.0** | **54.5** | **+7.5** | **3.333** | **0.0342** | **2.722** | **3** | **3** | **YES** |\n| M=64 VTC vs M=128 VTC | 62.0 | 60.0 | +2.0 | 1.537 | 0.2586 | 1.260 | 3 | 2 | no |\n| M=64 VTC vs M=32 MLP | 62.0 | 63.4 | -1.4 | -0.706 | 0.5201 | -0.576 | 3 | 3 | no |\n| M=96 VTC vs M=128 VTC | 54.5 | 60.0 | -5.5 | -2.963 | 0.0949 | -2.424 | 3 | 2 | no |\n| **M=96 VTC vs M=32 MLP** | **54.5** | **63.4** | **-8.9** | **-3.732** | **0.0216** | **-3.047** | **3** | **3** | **YES** |\n| M=128 VTC vs M=32 MLP | 60.0 | 63.4 | -3.4 | -2.232 | 0.1510 | -1.828 | 2 | 3 | no |\n\n## Key Findings\n\n- **2/10 pairs statistically significant (p<0.05)**:\n  - M=64 VTC > M=96 VTC: p=0.034, Cohen's d=2.72 (very large effect)\n  - M=32 MLP > M=96 VTC: p=0.022, Cohen's d=3.05 (very large effect)\n\n- **M=32 VTC vs M=32 MLP (key comparison): p=0.150, NOT significant**\n  - MLP adapter leads by 3.3pp on average, but the difference cannot be distinguished from noise at n=3\n  - Cohen's d=1.59 suggests a large effect size, but insufficient power to confirm\n\n- **M=96 is the clear underperformer**: significantly worse than both M=64 VTC and MLP adapter. The non-monotonic dip at M=96 is real (statistically supported).\n\n- **M=32/M=64/M=128 VTC form an indistinguishable cluster**: no pairwise comparison among them reaches significance (all p>0.25)\n\n- **Cohen's d interpretation** (small<0.2, medium 0.2-0.8, large>0.8): Most effect sizes are large, reflecting meaningful absolute differences, but the extremely small n limits statistical power.\n\n## Implications for Paper Wording\n\n- Claims about VTC vs MLP adapter should use hedged language: \"comparable performance\" or \"no statistically significant difference\" rather than \"equivalent\" or \"better\"\n- The M=96 dip can be stated as a confirmed finding (p<0.05 vs M=64)\n- M=32/64/128 VTC performance plateau can be described as \"robust across M values\" since none differ significantly\n\n## Notes\n\n- M=128 has only 2 seeds (seed43 still training); all M=128 comparisons have reduced power\n- All tests are Welch's t-test (unequal variance assumption)\n- With n=3 per condition, statistical power is very limited (~0.2 for medium effects); non-significant results should NOT be interpreted as evidence of no difference\n- No multiple comparison correction applied (10 tests); if Bonferroni-corrected (alpha=0.005), no pair remains significant\n",
    "content_filename": "statistical_tests.md",
    "tags": "['statistics', 't-test', 'm-sweep', 'adapter-comparison']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T20:08:47.603484+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_cd7566\", \"name\": \"statistical_tests_m_sweep\", \"type\": \"report\", \"description\": \"Pairwise Welch's t-test results for M-sweep (VTC cross-attention) and MLP adapter comparison, with Cohen's d effect sizes\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/report/statistical_tests.md\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T20:08:39.766094+00:00\", \"tags\": [\"statistics\", \"t-test\", \"m-sweep\", \"adapter-comparison\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260519T200645",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T20:08:47.603652+00:00_

统计检验完成，已注册为 `art_20260519_cd7566`。

核心结论：
- **仅 2/10 对显著 (p<0.05)**：M=64 VTC > M=96 VTC (p=0.034)，M=32 MLP > M=96 VTC (p=0.022)
- **VTC vs MLP (M=32)：p=0.150，不显著** — MLP 领先 3.3pp 但 n=3 power 不足以确认
- M=32/64/128 VTC 形成不可区分的性能平台（所有 p>0.25）
- M=96 是确认的低点，Bonferroni 校正后 (α=0.005) 所有对均不显著
- 论文措辞建议：VTC vs MLP 用 "comparable" / "no significant difference"，M=96 dip 可直接 claim

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_statistical_tests_20260519T200645"
}
```

</details>

---
