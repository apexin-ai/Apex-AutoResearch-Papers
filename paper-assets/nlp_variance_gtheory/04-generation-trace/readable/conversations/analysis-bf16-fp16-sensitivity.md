# analysis bf16 fp16 sensitivity

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_bf16_fp16_sensitivity_20260521T074400.jsonl`
- **Structured JSON:** [`8fa9cb17b5f5925c6634.json`](../../sessions/8f/8fa9cb17b5f5925c6634.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-21T07:46:17.614419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T07:46:17.614803+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T07:46:17.614963+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls results/exp001_llama/shard_*.jsonl results/exp001_mistral/shard_*.jsonl results/exp001_qwen/shard_*.jsonl results/exp001_gemma/shard_*.jsonl results/exp001_gemma_fp32/shard_*.jsonl 2>&1 | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls results/exp001_llama/shard_*.jsonl results/exp001_mistral/shard_*.jsonl results/exp001_qwen/shard_*.jsonl results/exp001_gemma/shard_*.jsonl results/exp001_gemma_fp32/shard_*.jsonl 2>&1 | head -30"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T07:46:17.615104+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:46:17.615234+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory/results -name \"shard_*.jsonl\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory/results -name \"shard_*.jsonl\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T07:46:17.615377+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/results/exp001_gemma/shard_0.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma/shard_1.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma/shard_2.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma/shard_3.jsonl\\n/root/nlp_variance_gtheory/results/exp001_mistral/shard_2.jsonl\\n/root/nlp_variance_gtheory/results/exp001_mistral/shard_1.jsonl\\n/root/nlp_variance_gtheory/results/exp001_mistral/shard_3.jsonl\\n/root/nlp_variance_gtheory/results/exp001_mistral/shard_0.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma_fp32/shard_0.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma_fp32/shard_2.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma_fp32/shard_3.jsonl\\n/root/nlp_variance_gtheory/results/exp001_gemma_fp32/shard_1.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_1.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_2.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_0.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_3_resume.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_3_original.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_3_merged_with_dup.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_3_patch.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_3_before_patch.jsonl\\n/root/nlp_variance_gtheory/results/exp001_qwen/shard_3.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:46:17.615592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory/results/exp001_llama -name \"shard_*.jsonl\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory/results/exp001_llama -name \"shard_*.jsonl\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T07:46:17.615736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -1 /root/nlp_variance_gtheory/results/exp001_mistral/shard_0.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -1 /root/nlp_variance_gtheory/results/exp001_mistral/shard_0.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T07:46:17.615867+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T07:46:17.616008+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"condition_id\\\": 4487, \\\"item_id\\\": \\\"abstract_algebra_81\\\", \\\"subject\\\": \\\"abstract_algebra\\\", \\\"model\\\": \\\"mistralai/Mistral-7B-Instruct-v0.3\\\", \\\"precision\\\": \\\"bfloat16\\\", \\\"temperature\\\": 0.3, \\\"top_p\\\": 0.9, \\\"prompt_template\\\": 1, \\\"seed\\\": 2048, \\\"ordering\\\": 3, \\\"generated_text\\\": \\\"A\\\\n\\\\nLet G be a group with |G| = 15\\\", \\\"predicted_answer\\\": \\\"A\\\", \\\"gold_answer\\\": \\\"D\\\", \\\"correct\\\": 0, \\\"latency_ms\\\": 28.05, \\\"answer_logprob\\\": 0.0, \\\"top_logprobs\\\": {\\\" A\\\": 0.0, \\\"\\\": -Infinity, \\\"[INST]\\\": -Infinity}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T07:46:17.616138+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T07:46:17.616275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"binary_data_limitation.json\\nbootstrap_vs_jackknife.json\\ncross_model_2way_precision.csv\\ncross_model_2way_precision_meta.json\\ncross_model_3way_bf16.csv\\ncross_model_3way_bf16_meta.json\\ncross_model_4way_bf16.csv\\ncross_model_balanced.csv\\ncross_model_balanced.jsonl\\ncross_model_balanced_meta.json\\ncross_model_bootstrap.json\\ncross_model_g_coefficients.json\\ncross_model_gstudy.json\\ncross_model_llama_gemma.csv\\ncross_model_llama_gemma.jsonl\\ncross_model_reml.json\\ncross_model_reml_500iter.json\\ndataset_a4_gstudy.json\\ndataset_a_gstudy.json\\ndataset_b_gstudy.json\\nfixed_vs_random_sensitivity.json\\nirt_vs_gtheory.json\\nllama_full.csv\\nllama_precision_balanced.csv\\nllama_precision_balanced_meta.json\\nllama_single_model_gstudy.json\\ntemperature_stratified_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T07:46:17.616464+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory/results -name \"*.jsonl\" -path \"*llama*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory/results -name \"*.jsonl\" -path \"*llama*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T07:46:17.616612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/exp001_llama/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/exp001_llama/"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T07:46:17.616752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/results/exp001_llama/llama_shard_0.jsonl\\n/root/nlp_variance_gtheory/results/exp001_llama/llama_shard_2.jsonl\\n/root/nlp_variance_gtheory/results/exp001_llama/llama_shard_1.jsonl\\n/root/nlp_variance_gtheory/results/exp001_llama/llama_shard_3.jsonl\\n/root/nlp_variance_gtheory/results/analysis/cross_model_llama_gemma.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T07:46:17.616883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"llama_shard_0.jsonl\\nllama_shard_1.jsonl\\nllama_shard_2.jsonl\\nllama_shard_3.jsonl\\nshards\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T07:46:17.617071+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cat > /root/nlp_variance_gtheory/scripts/bf16_fp16_sensitivity.py << 'PYEOF'\nimport pandas as pd\nimport numpy as np\nimport json\nimport glob\nimport os\n\nos.chdir('/root/nlp_variance_gtheory')\n\n# === Load data for 3 models (Llama, Mistral, Qwen) ===\nrecords = []\n\n# Llama: llama_shard_*.jsonl\nfor f in sorted(glob.glob('results/exp001_llama/llama_shard_*.jsonl')):\n    with open(f) as fh:\n        for line in fh:\n            records.append(json.loads(line))\n\n# Mistral & Qwen: shard_*.jsonl (exclude special files)\nfor model_dir in ['exp001_mistral', 'exp001_qwen']:\n    for f in sorted(glob.glob(f'results/{model_dir}/shard_[0-3].jsonl')):\n        with open(f) as fh:\n            for line in fh:\n                records.append(json.loads(line))\n\ndf = pd.DataFrame(records)\n\n# Normalize correct field\nif 'binary_correct' not in df.columns and 'correct' in df.columns:\n    df['binary_correct'] = df['correct']\n\n# Shorten model names\nmodel_map = {}\nfor m in df['model'].unique():\n    short = m.split('/')[-1] if '/' in m else m\n    model_map[m] = short\ndf['model'] = df['model'].map(model_map)\n\nprint(f\"Total records loaded: {len(df)}\")\nprint(f\"Models: {sorted(df['model'].unique())}\")\nprint(f\"Precisions: {sorted(df['precision'].unique())}\")\nprint(f\"By model×precision:\")\nprint(df.groupby(['model','precision']).size().unstack(fill_value=0))\nprint()\n\n# === Helper: variance decomposition ===\ndef variance_decomposition(data, label=\"\"):\n    grand_mean = data['binary_correct'].mean()\n    N = len(data)\n    total_var = data['binary_correct'].var()\n    ss_total = total_var * (N - 1)\n\n    facets = ['model', 'precision', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']\n    # Only use facets present in data with >1 level\n    facets = [f for f in facets if f in data.columns and data[f].nunique() > 1]\n\n    results = {}\n    for facet in facets:\n        group_means = data.groupby(facet)['binary_correct'].mean()\n        n_levels = len(group_means)\n        n_per_level = N / n_levels\n        ss = n_per_level * ((group_means - grand_mean) ** 2).sum()\n        results[facet] = {\n            'n_levels': int(n_levels),\n            'ss': float(ss),\n            'mean_range': [float(group_means.min()), float(group_means.max())]\n        }\n\n    interactions = [\n        ('model', 'item_id'), ('model', 'precision'), ('model', 'temperature'),\n        ('precision', 'item_id'), ('precision', 'temperature'),\n        ('temperature', 'item_id'), ('prompt_template', 'item_id'),\n        ('seed', 'item_id'), ('ordering', 'item_id'),\n    ]\n\n    for f1, f2 in interactions:\n        if f1 not in facets or f2 not in facets:\n            continue\n        cell_means = data.groupby([f1, f2])['binary_correct'].mean()\n        marginal_A = data.groupby(f1)['binary_correct'].mean()\n        marginal_B = data.groupby(f2)['binary_correct'].mean()\n        n_a = data[f1].nunique()\n        n_b = data[f2].nunique()\n        n_per_cell = N / (n_a * n_b)\n\n        interaction_ss = 0\n        for (a, b), cell_mean in cell_means.items():\n            expected = grand_mean + (marginal_A[a] - grand_mean) + (marginal_B[b] - grand_mean)\n            interaction_ss += (cell_mean - expected) ** 2\n        interaction_ss *= n_per_cell\n\n        results[f'{f1}:{f2}'] = {\n            'n_levels': int(n_a * n_b),\n            'ss': float(interaction_ss)\n        }\n\n    all_ss = {k: v['ss'] for k, v in results.items()}\n    ss_residual = ss_total - sum(all_ss.values())\n    all_ss['residual'] = max(0, ss_residual)\n    total_ss_sum = sum(all_ss.values())\n    variance_pct = {k: v / total_ss_sum * 100 for k, v in all_ss.items()}\n\n    print(f\"\\n=== {label} Variance Components ===\")\n    print(f\"N={N}, grand_mean={grand_mean:.4f}, total_var={total_var:.6f}\")\n    for k, v in sorted(variance_pct.items(), key=lambda x: -x[1]):\n        if v > 0.01:\n            print(f\"  {k}: {v:.4f}%\")\n\n    return results, variance_pct, {'N': N, 'grand_mean': float(grand_mean), 'total_var': float(total_var)}\n\n# === Analysis 1: BF16+FP16 only (3 models) ===\ndf_bf16_fp16 = df[df['precision'].isin(['bfloat16', 'float16'])].copy()\nprint(f\"\\n--- BF16+FP16 Dataset ---\")\nprint(f\"Records: {len(df_bf16_fp16)}\")\nprint(f\"By model: {df_bf16_fp16.groupby('model').size().to_dict()}\")\nprint(f\"By precision: {df_bf16_fp16.groupby('precision').size().to_dict()}\")\nprint(f\"Mean accuracy by precision:\")\nprint(df_bf16_fp16.groupby('precision')['binary_correct'].mean())\nprint(f\"Mean accuracy by model×precision:\")\nprint(df_bf16_fp16.groupby(['model','precision'])['binary_correct'].mean().unstack())\n\nres_bf16fp16, pct_bf16fp16, stats_bf16fp16 = variance_decomposition(df_bf16_fp16, \"BF16+FP16 Only (3 models)\")\n\n# === Analysis 2: All 3 precisions (same 3 models) ===\nprint(f\"\\n--- All 3 Precisions Dataset ---\")\nprint(f\"Records: {len(df)}\")\nprint(f\"By precision: {df.groupby('precision').size().to_dict()}\")\nprint(f\"Mean accuracy by precision:\")\nprint(df.groupby('precision')['binary_correct'].mean())\n\nres_3prec, pct_3prec, stats_3prec = variance_decomposition(df, \"All 3 Precisions (3 models)\")\n\n# === Comparison table ===\nprint(\"\\n\\n========== COMPARISON TABLE ==========\")\nprint(f\"{'Component':<25} {'3-Prec (%)':<15} {'BF16+FP16 (%)':<15} {'Delta':<10}\")\nprint(\"-\" * 65)\nall_keys = sorted(set(list(pct_3prec.keys()) + list(pct_bf16fp16.keys())),\n                  key=lambda x: -max(pct_3prec.get(x, 0), pct_bf16fp16.get(x, 0)))\nfor k in all_keys:\n    v3 = pct_3prec.get(k, 0)\n    v2 = pct_bf16fp16.get(k, 0)\n    delta = v2 - v3\n    if max(v3, v2) > 0.01:\n        print(f\"  {k:<23} {v3:>10.4f}     {v2:>10.4f}     {delta:>+8.4f}\")\n\n# === Save ===\nos.makedirs('results/analysis', exist_ok=True)\n\noutput = {\n    'analysis': 'BF16 vs FP16 sensitivity — FP32 confound check',\n    'date': '2026-05-21',\n    'motivation': 'Reviewer concern: FP32 dominates precision facet. Check if precision variance ~0 when FP32 excluded.',\n    'bf16_fp16_only': {\n        'n_records': int(len(df_bf16_fp16)),\n        'n_models': 3,\n        'models': sorted(df_bf16_fp16['model'].unique().tolist()),\n        'precisions': ['bfloat16', 'float16'],\n        'grand_mean': stats_bf16fp16['grand_mean'],\n        'variance_components_pct': {k: round(v, 4) for k, v in pct_bf16fp16.items()},\n        'precision_pct': round(pct_bf16fp16.get('precision', 0), 4),\n        'precision_item_pct': round(pct_bf16fp16.get('precision:item_id', 0), 4),\n        'accuracy_by_precision': df_bf16_fp16.groupby('precision')['binary_correct'].mean().to_dict(),\n    },\n    'all_3_precisions': {\n        'n_records': int(len(df)),\n        'n_models': 3,\n        'models': sorted(df['model'].unique().tolist()),\n        'precisions': sorted(df['precision'].unique().tolist()),\n        'grand_mean': stats_3prec['grand_mean'],\n        'variance_components_pct': {k: round(v, 4) for k, v in pct_3prec.items()},\n        'precision_pct': round(pct_3prec.get('precision', 0), 4),\n        'precision_item_pct': round(pct_3prec.get('precision:item_id', 0), 4),\n        'accuracy_by_precision': df.groupby('precision')['binary_correct'].mean().to_dict(),\n    },\n    'conclusion': '',\n}\n\n# Set conclusion based on results\nprec_bf16fp16 = pct_bf16fp16.get('precision', 0)\nprec_item_bf16fp16 = pct_bf16fp16.get('precision:item_id', 0)\nprec_3prec = pct_3prec.get('precision', 0)\nprec_item_3prec = pct_3prec.get('precision:item_id', 0)\noutput['conclusion'] = (\n    f\"With FP32 excluded: precision={prec_bf16fp16:.4f}%, precision×item={prec_item_bf16fp16:.4f}%. \"\n    f\"With FP32 included: precision={prec_3prec:.4f}%, precision×item={prec_item_3prec:.4f}%. \"\n    f\"FP32 removal {'confirms' if prec_bf16fp16 < 1.0 else 'does not confirm'} that \"\n    f\"precision variance is driven by FP32, not BF16-vs-FP16 differences.\"\n)\n\nwith open('results/analysis/bf16_fp16_only_gstudy.json', 'w') as f:\n    json.dump(output, f, indent=2, default=str)\n\nprint(f\"\\nSaved to results/analysis/bf16_fp16_only_gstudy.json\")\nprint(f\"\\n=== CONCLUSION ===\")\nprint(output['conclusion'])\nPYEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat > /root/nlp_variance_gtheory/scripts/bf16_fp16_sensitivity.py << 'PYEOF'\nimport pandas as pd\nimport numpy as np\nimport json\nimport glob\nimport os\n\nos.chdir('/root/nlp_variance_gtheory')\n\n# === Load data for 3 models (Llama, Mistral, Qwen) ===\nrecords = []\n\n# Llama: llama_shard_*.jsonl\nfor f in sorted(glob.glob('results/exp001_llama/llama_shard_*.jsonl')):\n    with open(f) as fh:\n        for line in fh:\n            records.append(json.loads(line))\n\n# Mistral & Qwen: shard_*.jsonl (exclude special files)\nfor model_dir in ['exp001_mistral', 'exp001_qwen']:\n    for f in sorted(glob.glob(f'results/{model_dir}/shard_[0-3].jsonl')):\n        with open(f) as fh:\n            for line in fh:\n                records.append(json.loads(line))\n\ndf = pd.DataFrame(records)\n\n# Normalize correct field\nif 'binary_correct' not in df.columns and 'correct' in df.columns:\n    df['binary_correct'] = df['correct']\n\n# Shorten model names\nmodel_map = {}\nfor m in df['model'].unique():\n    short = m.split('/')[-1] if '/' in m else m\n    model_map[m] = short\ndf['model'] = df['model'].map(model_map)\n\nprint(f\"Total records loaded: {len(df)}\")\nprint(f\"Models: {sorted(df['model'].unique())}\")\nprint(f\"Precisions: {sorted(df['precision'].unique())}\")\nprint(f\"By model×precision:\")\nprint(df.groupby(['model','precision']).size().unstack(fill_value=0))\nprint()\n\n# === Helper: variance decomposition ===\ndef variance_decomposition(data, label=\"\"):\n    grand_mean = data['binary_correct'].mean()\n    N = len(data)\n    total_var = data['binary_correct'].var()\n    ss_total = total_var * (N - 1)\n\n    facets = ['model', 'precision', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']\n    # Only use facets present in data with >1 level\n    facets = [f for f in facets if f in data.columns and data[f].nunique() > 1]\n\n    results = {}\n    for facet in facets:\n        group_means = data.groupby(facet)['binary_correct'].mean()\n        n_levels = len(group_means)\n        n_per_level = N / n_levels\n        ss = n_per_level * ((group_means - grand_mean) ** 2).sum()\n        results[facet] = {\n            'n_levels': int(n_levels),\n            'ss': float(ss),\n            'mean_range': [float(group_means.min()), float(group_means.max())]\n        }\n\n    interactions = [\n        ('model', 'item_id'), ('model', 'precision'), ('model', 'temperature'),\n        ('precision', 'item_id'), ('precision', 'temperature'),\n        ('temperature', 'item_id'), ('prompt_template', 'item_id'),\n        ('seed', 'item_id'), ('ordering', 'item_id'),\n    ]\n\n    for f1, f2 in interactions:\n        if f1 not in facets or f2 not in facets:\n            continue\n        cell_means = data.groupby([f1, f2])['binary_correct'].mean()\n        marginal_A = data.groupby(f1)['binary_correct'].mean()\n        marginal_B = data.groupby(f2)['binary_correct'].mean()\n        n_a = data[f1].nunique()\n        n_b = data[f2].nunique()\n        n_per_cell = N / (n_a * n_b)\n\n        interaction_ss = 0\n        for (a, b), cell_mean in cell_means.items():\n            expected = grand_mean + (marginal_A[a] - grand_mean) + (marginal_B[b] - grand_mean)\n            interaction_ss += (cell_mean - expected) ** 2\n        interaction_ss *= n_per_cell\n\n        results[f'{f1}:{f2}'] = {\n            'n_levels': int(n_a * n_b),\n            'ss': float(interaction_ss)\n        }\n\n    all_ss = {k: v['ss'] for k, v in results.items()}\n    ss_residual = ss_total - sum(all_ss.values())\n    all_ss['residual'] = max(0, ss_residual)\n    total_ss_sum = sum(all_ss.values())\n    variance_pct = {k: v / total_ss_sum * 100 for k, v in all_ss.items()}\n\n    print(f\"\\n=== {label} Variance Components ===\")\n    print(f\"N={N}, grand_mean={grand_mean:.4f}, total_var={total_var:.6f}\")\n    for k, v in sorted(variance_pct.items(), key=lambda x: -x[1]):\n        if v > 0.01:\n            print(f\"  {k}: {v:.4f}%\")\n\n    return results, variance_pct, {'N': N, 'grand_mean': float(grand_mean), 'total_var': float(total_var)}\n\n# === Analysis 1: BF16+FP16 only (3 models) ===\ndf_bf16_fp16 = df[df['precision'].isin(['bfloat16', 'float16'])].copy()\nprint(f\"\\n--- BF16+FP16 Dataset ---\")\nprint(f\"Records: {len(df_bf16_fp16)}\")\nprint(f\"By model: {df_bf16_fp16.groupby('model').size().to_dict()}\")\nprint(f\"By precision: {df_bf16_fp16.groupby('precision').size().to_dict()}\")\nprint(f\"Mean accuracy by precision:\")\nprint(df_bf16_fp16.groupby('precision')['binary_correct'].mean())\nprint(f\"Mean accuracy by model×precision:\")\nprint(df_bf16_fp16.groupby(['model','precision'])['binary_correct'].mean().unstack())\n\nres_bf16fp16, pct_bf16fp16, stats_bf16fp16 = variance_decomposition(df_bf16_fp16, \"BF16+FP16 Only (3 models)\")\n\n# === Analysis 2: All 3 precisions (same 3 models) ===\nprint(f\"\\n--- All 3 Precisions Dataset ---\")\nprint(f\"Records: {len(df)}\")\nprint(f\"By precision: {df.groupby('precision').size().to_dict()}\")\nprint(f\"Mean accuracy by precision:\")\nprint(df.groupby('precision')['binary_correct'].mean())\n\nres_3prec, pct_3prec, stats_3prec = variance_decomposition(df, \"All 3 Precisions (3 models)\")\n\n# === Comparison table ===\nprint(\"\\n\\n========== COMPARISON TABLE ==========\")\nprint(f\"{'Component':<25} {'3-Prec (%)':<15} {'BF16+FP16 (%)':<15} {'Delta':<10}\")\nprint(\"-\" * 65)\nall_keys = sorted(set(list(pct_3prec.keys()) + list(pct_bf16fp16.keys())),\n                  key=lambda x: -max(pct_3prec.get(x, 0), pct_bf16fp16.get(x, 0)))\nfor k in all_keys:\n    v3 = pct_3prec.get(k, 0)\n    v2 = pct_bf16fp16.get(k, 0)\n    delta = v2 - v3\n    if max(v3, v2) > 0.01:\n        print(f\"  {k:<23} {v3:>10.4f}     {v2:>10.4f}     {delta:>+8.4f}\")\n\n# === Save ===\nos.makedirs('results/analysis', exist_ok=True)\n\noutput = {\n    'analysis': 'BF16 vs FP16 sensitivity — FP32 confound check',\n    'date': '2026-05-21',\n    'motivation': 'Reviewer concern: FP32 dominates precision facet. Check if precision variance ~0 when FP32 excluded.',\n    'bf16_fp16_only': {\n        'n_records': int(len(df_bf16_fp16)),\n        'n_models': 3,\n        'models': sorted(df_bf16_fp16['model'].unique().tolist()),\n        'precisions': ['bfloat16', 'float16'],\n        'grand_mean': stats_bf16fp16['grand_mean'],\n        'variance_components_pct': {k: round(v, 4) for k, v in pct_bf16fp16.items()},\n        'precision_pct': round(pct_bf16fp16.get('precision', 0), 4),\n        'precision_item_pct': round(pct_bf16fp16.get('precision:item_id', 0), 4),\n        'accuracy_by_precision': df_bf16_fp16.groupby('precision')['binary_correct'].mean().to_dict(),\n    },\n    'all_3_precisions': {\n        'n_records': int(len(df)),\n        'n_models': 3,\n        'models': sorted(df['model'].unique().tolist()),\n        'precisions': sorted(df['precision'].unique().tolist()),\n        'grand_mean': stats_3prec['grand_mean'],\n        'variance_components_pct': {k: round(v, 4) for k, v in pct_3prec.items()},\n        'precision_pct': round(pct_3prec.get('precision', 0), 4),\n        'precision_item_pct': round(pct_3prec.get('precision:item_id', 0), 4),\n        'accuracy_by_precision': df.groupby('precision')['binary_correct'].mean().to_dict(),\n    },\n    'conclusion': '',\n}\n\n# Set conclusion based on results\nprec_bf16fp16 = pct_bf16fp16.get('precision', 0)\nprec_item_bf16fp16 = pct_bf16fp16.get('precision:item_id', 0)\nprec_3prec = pct_3prec.get('precision', 0)\nprec_item_3prec = pct_3prec.get('precision:item_id', 0)\noutput['conclusion'] = (\n    f\"With FP32 excluded: precision={prec_bf16fp16:.4f}%, precision×item={prec_item_bf16fp16:.4f}%. \"\n    f\"With FP32 included: precision={prec_3prec:.4f}%, precision×item={prec_item_3prec:.4f}%. \"\n    f\"FP32 removal {'confirms' if prec_bf16fp16 < 1.0 else 'does not confirm'} that \"\n    f\"precision variance is driven by FP32, not BF16-vs-FP16 differences.\"\n)\n\nwith open('results/analysis/bf16_fp16_only_gstudy.json', 'w') as f:\n    json.dump(output, f, indent=2, default=str)\n\nprint(f\"\\nSaved to results/analysis/bf16_fp16_only_gstudy.json\")\nprint(f\"\\n=== CONCLUSION ===\")\nprint(output['conclusion'])\nPYEOF\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T07:46:17.617334+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T07:46:17.617517+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/bf16_fp16_sensitivity.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/bf16_fp16_sensitivity.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T07:46:17.617704+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total records loaded: 757600\\nModels: ['Meta-Llama-3___1-8B-Instruct', 'Mistral-7B-Instruct-v0.3', 'Qwen3-8B']\\nPrecisions: ['bfloat16', 'float16', 'float32']\\nBy model×precision:\\nprecision                     bfloat16  float16  float32\\nmodel                                                   \\nMeta-Llama-3___1-8B-Instruct     86400    86400    66400\\nMistral-7B-Instruct-v0.3         86400    86400    86400\\nQwen3-8B                        100200    79600    79400\\n\\n\\n--- BF16+FP16 Dataset ---\\nRecords: 525400\\nBy model: {'Meta-Llama-3___1-8B-Instruct': 172800, 'Mistral-7B-Instruct-v0.3': 172800, 'Qwen3-8B': 179800}\\nBy precision: {'bfloat16': 273000, 'float16': 252400}\\nMean accuracy by precision:\\nprecision\\nbfloat16    0.693231\\nfloat16     0.690884\\nName: binary_correct, dtype: float64\\nMean accuracy by model×precision:\\nprecision                     bfloat16   float16\\nmodel                                           \\nMeta-Llama-3___1-8B-Instruct  0.710833  0.711447\\nMistral-7B-Instruct-v0.3      0.637581  0.638206\\nQwen3-8B                      0.726038  0.725741\\n\\n=== BF16+FP16 Only (3 models) Variance Components ===\\nN=525400, grand_mean=0.6921, total_var=0.213097\\n  item_id: 52.8718%\\n  model:item_id: 22.5072%\\n  residual: 19.4251%\\n  prompt_template:item_id: 1.7544%\\n  seed:item_id: 1.5591%\\n  model: 0.6951%\\n  temperature:item_id: 0.5583%\\n  ordering:item_id: 0.5551%\\n  precision:item_id: 0.0412%\\n  model:temperature: 0.0115%\\n  prompt_template: 0.0109%\\n\\n--- All 3 Precisions Dataset ---\\nRecords: 757600\\nBy precision: {'bfloat16': 273000, 'float16': 252400, 'float32': 232200}\\nMean accuracy by precision:\\nprecision\\nbfloat16    0.693231\\nfloat16     0.690884\\nfloat32     0.628984\\nName: binary_correct, dtype: float64\\n\\n=== All 3 Precisions (3 models) Variance Components ===\\nN=757600, grand_mean=0.6728, total_var=0.220155\\n  item_id: 46.4064%
…[truncated 1988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T07:46:17.617906+00:00_

分析完成。结果非常清晰，完全符合预期：

## 结果

### Precision 相关方差分量对比

| Component | 3-Precision (%) | BF16+FP16 (%) | Delta |
|---|---|---|---|
| **precision** | 0.4033 | **0.0006** | -0.4027 |
| **precision×item** | 1.3036 | **0.0412** | -1.2623 |
| **model×precision** | 0.1995 | **0.0009** | -0.1986 |

### 关键发现

1. **precision 主效应**：排除 FP32 后从 0.40% 降至 **0.0006%**（几乎为零）。BF16 和 FP16 的平均准确率差异仅 0.23pp（69.32% vs 69.09%），三个模型上方向不一致（Llama/Mistral FP16 略高，Qwen BF16 略高）。

2. **precision×item 交互**：从 1.30% 降至 **0.04%**（降幅 97%）。FP32 几乎是 precision×item 交互的唯一来源。

3. **其他分量稳定**：item_id（46.4→52.9%）、model×item（18.2→22.5%）占比上升是因为 precision 相关分量释放的空间被重新分配，绝对结构未变。

4. **数据覆盖**：525,400 条记录，3 个模型（Llama-3.1-8B、Mistral-7B、Qwen3-8B），BF16 273K + FP16 252K。

### 回应 Reviewer

FP32 与 BF16/FP16 有 ~6pp accuracy gap（62.9% vs 69.1%），是 precision facet 方差的主要来源。排除 FP32 后，precision 及其交互项均降至 ≈0%，证实 BF16≈FP16 在评估方差上无实质差异。Reviewer 关于 FP32 confound 的担忧是合理的——precision facet 的方差确实由 FP32 驱动，而非数值精度的渐进差异。

结果已保存至 `results/analysis/bf16_fp16_only_gstudy.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bf16_fp16_sensitivity_20260521T074400"
}
```

</details>

---
