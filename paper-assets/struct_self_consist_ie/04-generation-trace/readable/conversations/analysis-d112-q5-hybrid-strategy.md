# analysis d112 q5 hybrid strategy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_analysis_d112_q5_hybrid_strategy_20260516T092356.jsonl`
- **Structured JSON:** [`dfce04e3b80896123943.json`](../../sessions/df/dfce04e3b80896123943.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-16T09:28:08.791744+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T09:28:08.792095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:28:08.792324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T09:28:08.792469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T09:28:08.792609+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_within_rho.py\\nresults.json\\nsummary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:28:08.792749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_signals_5signal.json\\nauroc_5signal.json\\ncomparison.json\\nreliability_data_1024.json\\nreport.json\\nrun.log\\nsamples.jsonl\\nsamples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:28:08.792877+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:28:08.793063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"SciERC_NER_N8_T1.0\\\": {\\n    \\\"dataset\\\": \\\"SciERC_NER_N8_T1.0\\\",\\n    \\\"n_instances\\\": 551,\\n    \\\"n_samples_per_instance\\\": 8,\\n    \\\"within_instance_rho\\\": {\\n      \\\"SJ_all\\\": {\\n        \\\"metric\\\": \\\"SJ_all\\\",\\n        \\\"n_valid\\\": 427,\\n        \\\"median\\\": 0.5238,\\n        \\\"mean\\\": 0.3139,\\n        \\\"std\\\": 0.6949,\\n        \\\"q25\\\": -0.2,\\n        \\\"q75\\\": 0.9759,\\n        \\\"iqr\\\": 1.1759,\\n        \\\"n_positive\\\": 299,\\n        \\\"pct_positive\\\": 70.0,\\n        \\\"n_gt_0.3\\\": 255,\\n        \\\"pct_gt_0.3\\\": 59.7,\\n        \\\"n_gt_0.5\\\": 219,\\n        \\\"pct_gt_0.5\\\": 51.3,\\n        \\\"min\\\": -1.0,\\n        \\\"max\\\": 1.0\\n      },\\n      \\\"EM_all\\\": {\\n        \\\"metric\\\": \\\"EM_all\\\",\\n        \\\"n_valid\\\": 409,\\n        \\\"median\\\": 0.3974,\\n        \\\"mean\\\": 0.2722,\\n        \\\"std\\\": 0.7143,\\n        \\\"q25\\\": -0.2981,\\n        \\\"q75\\\": 0.9897,\\n        \\\"iqr\\\": 1.2879,\\n        \\\"n_positive\\\": 258,\\n        \\\"pct_positive\\\": 63.1,\\n        \\\"n_gt_0.3\\\": 230,\\n        \\\"pct_gt_0.3\\\": 56.2,\\n        \\\"n_gt_0.5\\\": 190,\\n        \\\"pct_gt_0.5\\\": 46.5,\\n        \\\"min\\\": -1.0,\\n        \\\"max\\\": 1.0\\n      },\\n      \\\"SJ_rich\\\": {\\n        \\\"metric\\\": \\\"SJ_rich_>=3uniq\\\",\\n        \\\"n_valid\\\": 251,\\n        \\\"median\\\": 0.4714,\\n        \\\"mean\\\": 0.3469,\\n        \\\"std\\\": 0.5734,\\n        \\\"q25\\\": 0.0065,\\n        \\\"q75\\\": 0.8407,\\n        \\\"iqr\\\": 0.8342,\\n        \\\"n_positive\\\": 188,\\n        \\\"pct_positive\\\": 74.9,\\n        \\\"n_gt_0.3\\\": 151,\\n        \\\"pct_gt_0.3\\\": 60.2,\\n        \\\"n_gt_0.5\\\": 119,\\n        \\\"pct_gt_0.5\\\": 47.4,\\n        \\\"min\\\": -1.0,\\n        \\\"max\\\": 1.0\\n      },\\n      \\\"EM_rich\\\": {\\n     
…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T09:28:08.793304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:28:08.793700+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 9068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:28:08.793901+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/analyze_within_rho.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/analyze_within_rho.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:28:08.794557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute within-instance MBR utility-F1 Spearman rho with diagnostics.\\\"\\\"\\\"\\nimport json\\nimport os\\nimport numpy as np\\nfrom itertools import combinations\\nfrom scipy.stats import spearmanr\\nfrom scipy.optimize import linear_sum_assignment\\n\\ndef entity_strict_f1(pred_entities, gold_entities):\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    tp = len(pred_set & gold_set)\\n    fp = len(pred_set - gold_set)\\n    fn = len(gold_set - pred_set)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / (tp + fp)\\n    r = tp / (tp + fn)\\n    return 2 * p * r / (p + r)\\n\\ndef span_overlap(s1_start, s1_end, s2_start, s2_end):\\n    inter = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))\\n    union = max(s1_end, s2_end) - min(s1_start, s2_start)\\n    return inter / union if union > 0 else 0.0\\n\\ndef ner_soft_jaccard_pair(ents_a, ents_b):\\n    if not ents_a and not ents_b:\\n        return 1.0\\n    if not ents_a or not ents_b:\\n        return 0.0\\n    n_a, n_b = len(ents_a), len(ents_b)\\n    size = max(n_a, n_b)\\n    cost = np.zeros((size, size))\\n    for i in range(n_a):\\n        for j in range(n_b):\\n            if ents_a[i][\\\"type\\\"] == ents_b[j][\\\"type\\\"]:\\n                cost[i, j] = span_overlap(\\n                    ents_a[i][\\\"start\\\"], ents_a[i][\\\"end\\\"],\\n                    ents_b[j][\\\"start\\\"], ents_b[j][\\\"end\\\"],\\n                )\\n    row_ind, col_ind = linear_sum_assignment(cost, maximize=True)\\n    matched_sum = cost[row_ind, col_ind].sum()\\n    denom = n_a + n_b - matched_sum\\n    return matched_sum / denom if denom > 0 else 1.0\\n\\ndef entity_set_key(entities):\\n    return frozenset((e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in entities)\\n\\ndef fleiss_kappa_ner(s
…[truncated 7120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T09:28:08.794771+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"samples_with_logprobs.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"samples_with_logprobs.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:28:08.794948+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T09:28:08.795214+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:28:08.795401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nrun.log\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T09:28:08.795534+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"samples.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"samples.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:28:08.795702+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/gate0_ft002v2_ckpt400/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2_r1024/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_200only_backup/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_200only/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_200only/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed456_t10_full/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_pilot/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_dryrun/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_dryrun/samples.jsonl\\n/root/autodl-tmp/struct_self_con
…[truncated 4351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T09:28:08.795871+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -2 /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -2 /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T09:28:08.796306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns in Japanese text\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis in Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns in Japanese t
…[truncated 9081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T09:28:08.796501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=open('/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl').readline(); inst=json.loads(d); print('n_samples:', len(inst['samples'])); print('has_greedy:', 'greedy' in inst); print('keys:', list(inst.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=open('/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl').readline(); inst=json.loads(d); print('n_samples:', len(inst['samples'])); print('has_greedy:', 'greedy' in inst); print('keys:', list(inst.keys()))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T09:28:08.796639+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T09:28:08.796815+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl').readline()); print('n_samples:', len(d['samples'])); print('has_greedy:', 'greedy' in d); print('has_logprobs:', 'logprobs' in d)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl').readline()); print('n_samples:', len(d['samples'])); print('has_greedy:', 'greedy' in d); print('has_logprobs:', 'logprobs' in d)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T09:28:08.797234+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T09:28:08.797411+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl').readline()); print('n_samples:', len(d['samples'])); print('has_greedy:', 'greedy' in d); print('has_logprobs:', 'logprobs' in d)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl').readline()); print('n_samples:', len(d['samples'])); print('has_greedy:', 'greedy' in d); print('has_logprobs:', 'logprobs' in d)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:28:08.797572+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T09:28:08.797737+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -c \"greedy\" /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -c \"greedy\" /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T09:28:08.797887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T09:28:08.798027+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -c \"greedy\" /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -c \"greedy\" /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T09:28:08.798327+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3453\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T09:28:08.798515+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T09:28:08.798665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T09:28:08.798795+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:28:08.798923+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3453 /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T09:28:08.799266+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy && cat > /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/compute_hybrid.py << 'SCRIPT'\n\"\"\"Compute hybrid strategy expected F1: greedy for degenerate, MBR for non-degenerate.\"\"\"\nimport json\nimport os\nimport numpy as np\nfrom itertools import combinations\nfrom scipy.optimize import linear_sum_assignment\n\ndef entity_strict_f1(pred_entities, gold_entities):\n    pred_set = {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in pred_entities}\n    gold_set = {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in gold_entities}\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    if tp == 0:\n        return 0.0\n    p = tp / (tp + fp)\n    r = tp / (tp + fn)\n    return 2 * p * r / (p + r)\n\ndef relation_strict_f1(pred_rels, gold_rels):\n    pred_set = {(r[\"head_start\"], r[\"head_end\"], r[\"tail_start\"], r[\"tail_end\"], r[\"type\"]) for r in pred_rels}\n    gold_set = {(r[\"head_start\"], r[\"head_end\"], r[\"tail_start\"], r[\"tail_end\"], r[\"type\"]) for r in gold_rels}\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    if tp == 0:\n        return 0.0\n    p = tp / (tp + fp)\n    r = tp / (tp + fn)\n    return 2 * p * r / (p + r)\n\ndef span_overlap(s1_start, s1_end, s2_start, s2_end):\n    inter = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))\n    union = max(s1_end, s2_end) - min(s1_start, s2_start)\n    return inter / union if union > 0 else 0.0\n\ndef ner_soft_jaccard_pair(ents_a, ents_b):\n    if not ents_a and not ents_b:\n        return 1.0\n    if not ents_a or not ents_b:\n        return 0.0\n    n_a, n_b = len(ents_a), len(ents_b)\n    size = max(n_a, n_b)\n    cost = np.zeros((size, size))\n    for i in range(n_a):\n        for j in range(n_b):\n            if ents_a[i][\"type\"] == ents_b[j][\"type\"]:\n                cost[i, j] = span_overlap(\n                    ents_a[i][\"start\"], ents_a[i][\"end\"],\n                    ents_b[j][\"start\"], ents_b[j][\"end\"],\n                )\n    row_ind, col_ind = linear_sum_assignment(cost, maximize=True)\n    matched_sum = cost[row_ind, col_ind].sum()\n    denom = n_a + n_b - matched_sum\n    return matched_sum / denom if denom > 0 else 1.0\n\ndef rel_soft_jaccard_pair(rels_a, rels_b):\n    if not rels_a and not rels_b:\n        return 1.0\n    if not rels_a or not rels_b:\n        return 0.0\n    n_a, n_b = len(rels_a), len(rels_b)\n    size = max(n_a, n_b)\n    cost = np.zeros((size, size))\n    for i in range(n_a):\n        for j in range(n_b):\n            if rels_a[i][\"type\"] == rels_b[j][\"type\"]:\n                head_ov = span_overlap(\n                    rels_a[i][\"head_start\"], rels_a[i][\"head_end\"],\n                    rels_b[j][\"head_start\"], rels_b[j][\"head_end\"],\n                )\n                tail_ov = span_overlap(\n                    rels_a[i][\"tail_start\"], rels_a[i][\"tail_end\"],\n                    rels_b[j][\"tail_start\"], rels_b[j][\"tail_end\"],\n                )\n                cost[i, j] = (head_ov + tail_ov) / 2.0\n    row_ind, col_ind = linear_sum_assignment(cost, maximize=True)\n    matched_sum = cost[row_ind, col_ind].sum()\n    denom = n_a + n_b - matched_sum\n    return matched_sum / denom if denom > 0 else 1.0\n\ndef compute_hybrid(jsonl_path, dataset_name, task_type=\"ner\"):\n    with open(jsonl_path) as f:\n        instances = [json.loads(line) for line in f if line.strip()]\n    \n    n_instances = len(instances)\n    n_samples = len(instances[0][\"samples\"])\n    \n    greedy_f1s = []\n    random_f1s = []\n    mbr_sj_f1s = []\n    oracle_f1s = []\n    hybrid_f1s = []\n    \n    n_degenerate = 0\n    n_non_degenerate = 0\n    \n    for inst in instances:\n        gold = inst[\"gold\"]\n        samples = inst[\"samples\"]\n        N = len(samples)\n        \n        # Compute F1 for each sample\n        if task_type == \"ner\":\n            f1s = np.array([entity_strict_f1(s.get(\"entities\", []), gold.get(\"entities\", [])) for s in samples])\n            greedy_f1 = entity_strict_f1(inst[\"greedy\"].get(\"entities\", []), gold.get(\"entities\", []))\n        else:  # RE\n            f1s = np.array([relation_strict_f1(s.get(\"relations\", []), gold.get(\"relations\", [])) for s in samples])\n            greedy_f1 = relation_strict_f1(inst[\"greedy\"].get(\"relations\", []), gold.get(\"relations\", []))\n        \n        # Compute SJ utility for each sample (average pairwise SJ with all others)\n        if task_type == \"ner\":\n            sj_matrix = np.zeros((N, N))\n            for i, j in combinations(range(N), 2):\n                v = ner_soft_jaccard_pair(\n                    samples[i].get(\"entities\", []),\n                    samples[j].get(\"entities\", [])\n                )\n                sj_matrix[i, j] = v\n                sj_matrix[j, i] = v\n            np.fill_diagonal(sj_matrix, 1.0)\n        else:  # RE\n            sj_matrix = np.zeros((N, N))\n            for i, j in combinations(range(N), 2):\n                v = rel_soft_jaccard_pair(\n                    samples[i].get(\"relations\", []),\n                    samples[j].get(\"relations\", [])\n                )\n                sj_matrix[i, j] = v\n                sj_matrix[j, i] = v\n            np.fill_diagonal(sj_matrix, 1.0)\n        \n        # SJ utility = mean pairwise SJ (excluding self)\n        sj_utilities = (sj_matrix.sum(axis=1) - 1.0) / (N - 1)\n        \n        # Identify degenerate: all F1s are the same\n        is_degenerate = np.var(f1s) < 1e-10\n        \n        # Baselines\n        greedy_f1s.append(greedy_f1)\n        random_f1s.append(float(np.mean(f1s)))\n        \n        # MBR (SJ-selected): always pick highest SJ utility sample\n        mbr_idx = int(np.argmax(sj_utilities))\n        mbr_sj_f1s.append(float(f1s[mbr_idx]))\n        \n        # Oracle: best F1 sample\n        oracle_f1s.append(float(np.max(f1s)))\n        \n        # Hybrid: degenerate -> greedy, non-degenerate -> MBR\n        if is_degenerate:\n            n_degenerate += 1\n            hybrid_f1s.append(greedy_f1)\n        else:\n            n_non_degenerate += 1\n            hybrid_f1s.append(float(f1s[mbr_idx]))\n    \n    results = {\n        \"dataset\": dataset_name,\n        \"task_type\": task_type,\n        \"n_instances\": n_instances,\n        \"n_samples_per_instance\": n_samples,\n        \"n_degenerate\": n_degenerate,\n        \"n_non_degenerate\": n_non_degenerate,\n        \"pct_degenerate\": round(100 * n_degenerate / n_instances, 1),\n        \"greedy_f1\": round(float(np.mean(greedy_f1s)), 4),\n        \"random_f1\": round(float(np.mean(random_f1s)), 4),\n        \"mbr_sj_f1\": round(float(np.mean(mbr_sj_f1s)), 4),\n        \"oracle_f1\": round(float(np.mean(oracle_f1s)), 4),\n        \"hybrid_f1\": round(float(np.mean(hybrid_f1s)), 4),\n        \"hybrid_gain_over_greedy\": round(float(np.mean(hybrid_f1s)) - float(np.mean(greedy_f1s)), 4),\n        \"hybrid_gain_over_random\": round(float(np.mean(hybrid_f1s)) - float(np.mean(random_f1s)), 4),\n        \"mbr_gain_over_greedy\": round(float(np.mean(mbr_sj_f1s)) - float(np.mean(greedy_f1s)), 4),\n        \"mbr_gain_over_random\": round(float(np.mean(mbr_sj_f1s)) - float(np.mean(random_f1s)), 4),\n    }\n    \n    # Compute oracle gap closed\n    oracle_gap = float(np.mean(oracle_f1s)) - float(np.mean(random_f1s))\n    if oracle_gap > 1e-10:\n        results[\"hybrid_pct_oracle_gap\"] = round(100 * (float(np.mean(hybrid_f1s)) - float(np.mean(random_f1s))) / oracle_gap, 1)\n        results[\"mbr_pct_oracle_gap\"] = round(100 * (float(np.mean(mbr_sj_f1s)) - float(np.mean(random_f1s))) / oracle_gap, 1)\n    \n    return results\n\nif __name__ == \"__main__\":\n    outdir = \"/root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy\"\n    os.makedirs(outdir, exist_ok=True)\n    \n    datasets = {\n        \"SciERC_NER_Qwen8B_N8\": {\n            \"path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\",\n            \"task\": \"ner\"\n        },\n        \"CoNLL_NER_Qwen8B_N16\": {\n            \"path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl\",\n            \"task\": \"ner\"\n        },\n        \"SciERC_RE_Qwen8B_N16\": {\n            \"path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl\",\n            \"task\": \"re\"\n        },\n    }\n    \n    all_results = {}\n    for name, cfg in datasets.items():\n        print(f\"Processing {name}...\")\n        if not os.path.exists(cfg[\"path\"]):\n            print(f\"  SKIP: {cfg['path']} not found\")\n            continue\n        all_results[name] = compute_hybrid(cfg[\"path\"], name, cfg[\"task\"])\n        r = all_results[name]\n        print(f\"  n={r['n_instances']}, N={r['n_samples_per_instance']}\")\n        print(f\"  degenerate: {r['n_degenerate']} ({r['pct_degenerate']}%)\")\n        print(f\"  greedy={r['greedy_f1']:.4f}, random={r['random_f1']:.4f}, MBR={r['mbr_sj_f1']:.4f}, hybrid={r['hybrid_f1']:.4f}, oracle={r['oracle_f1']:.4f}\")\n        print(f\"  hybrid gain over greedy: {r['hybrid_gain_over_greedy']:+.4f}\")\n        print(f\"  hybrid gain over random: {r['hybrid_gain_over_random']:+.4f}\")\n        print()\n    \n    # Save results\n    with open(os.path.join(outdir, \"results.json\"), \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    \n    # Generate summary\n    lines = [\"# Hybrid Strategy: Expected F1 Gain\", \"\"]\n    lines.append(\"**Strategy**: Use greedy for degenerate instances (constant F1 across all samples),\")\n    lines.append(\"MBR selection (highest SJ utility) for non-degenerate instances.\")\n    lines.append(\"\")\n    lines.append(\"| Dataset | N | #Inst | %Degen | Greedy | Random | MBR-SJ | **Hybrid** | Oracle | Hybrid Δ(greedy) |\")\n    lines.append(\"|---------|---|-------|--------|--------|--------|--------|------------|--------|------------------|\")\n    for name, r in all_results.items():\n        lines.append(f\"| {name} | {r['n_samples_per_instance']} | {r['n_instances']} | {r['pct_degenerate']}% | {r['greedy_f1']:.4f} | {r['random_f1']:.4f} | {r['mbr_sj_f1']:.4f} | **{r['hybrid_f1']:.4f}** | {r['oracle_f1']:.4f} | {r['hybrid_gain_over_greedy']:+.4f} |\")\n    lines.append(\"\")\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n    for name, r in all_results.items():\n        lines.append(f\"### {name}\")\n        lines.append(f\"- Degenerate instances: {r['n_degenerate']}/{r['n_instances']} ({r['pct_degenerate']}%)\")\n        lines.append(f\"- Non-degenerate instances: {r['n_non_degenerate']}/{r['n_instances']} ({100-r['pct_degenerate']:.1f}%)\")\n        lines.append(f\"- Hybrid F1 = {r['hybrid_f1']:.4f} (gain over greedy: {r['hybrid_gain_over_greedy']:+.4f})\")\n        lines.append(f\"- Pure MBR F1 = {r['mbr_sj_f1']:.4f} (gain over greedy: {r['mbr_gain_over_greedy']:+.4f})\")\n        if \"hybrid_pct_oracle_gap\" in r:\n            lines.append(f\"- Hybrid closes {r['hybrid_pct_oracle_gap']:.1f}% of oracle gap (vs {r['mbr_pct_oracle_gap']:.1f}% for pure MBR)\")\n        lines.append(\"\")\n    \n    summary = \"\\n\".join(lines)\n    with open(os.path.join(outdir, \"summary.md\"), \"w\") as f:\n        f.write(summary)\n    \n    print(\"Done. Results saved to\", outdir)\nSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy && cat > /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/compute_hybrid.py << 'SCRIPT'\n\"\"\"Compute hybrid strategy expected F1: greedy for degenerate, MBR for non-degenerate.\"\"\"\nimport json\nimport os\nimport numpy as np\nfrom itertools import combinations\nfrom scipy.optimize import linear_sum_assignment\n\ndef entity_strict_f1(pred_entities, gold_entities):\n    pred_set = {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in pred_entities}\n    gold_set = {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in gold_entities}\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    if tp == 0:\n        return 0.0\n    p = tp / (tp + fp)\n    r = tp / (tp + fn)\n    return 2 * p * r / (p + r)\n\ndef relation_strict_f1(pred_rels, gold_rels):\n    pred_set = {(r[\"head_start\"], r[\"head_end\"], r[\"tail_start\"], r[\"tail_end\"], r[\"type\"]) for r in pred_rels}\n    gold_set = {(r[\"head_start\"], r[\"head_end\"], r[\"tail_start\"], r[\"tail_end\"], r[\"type\"]) for r in gold_rels}\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    if tp == 0:\n        return 0.0\n    p = tp / (tp + fp)\n    r = tp / (tp + fn)\n    return 2 * p * r / (p + r)\n\ndef span_overlap(s1_start, s1_end, s2_start, s2_end):\n    inter = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))\n    union = max(s1_end, s2_end) - min(s1_start, s2_start)\n    return inter / union if union > 0 else 0.0\n\ndef ner_soft_jaccard_pair(ents_a, ents_b):\n    if not ents_a and not ents_b:\n        return 1.0\n    if not ents_a or not ents_b:\n        return 0.0\n    n_a, n_b = len(ents_a), len(ents_b)\n    size = max(n_a, n_b)\n    cost = np.zeros((size, size))\n    for i in range(n_a):\n        for j in range(n_b):\n            if ents_a[i][\"type\"] == ents_b[j][\"type\"]:\n                cost[i, j] = span_overlap(\n                    ents_a[i][\"start\"], ents_a[i][\"end\"],\n                    ents_b[j][\"start\"], ents_b[j][\"end\"],\n                )\n    row_ind, col_ind = linear_sum_assignment(cost, maximize=True)\n    matched_sum = cost[row_ind, col_ind].sum()\n    denom = n_a + n_b - matched_sum\n    return matched_sum / denom if denom > 0 else 1.0\n\ndef rel_soft_jaccard_pair(rels_a, rels_b):\n    if not rels_a and not rels_b:\n        return 1.0\n    if not rels_a or not rels_b:\n        return 0.0\n    n_a, n_b = len(rels_a), len(rels_b)\n    size = max(n_a, n_b)\n    cost = np.zeros((size, size))\n    for i in range(n_a):\n        for j in range(n_b):\n            if rels_a[i][\"type\"] == rels_b[j][\"type\"]:\n                head_ov = span_overlap(\n                    rels_a[i][\"head_start\"], rels_a[i][\"head_end\"],\n                    rels_b[j][\"head_start\"], rels_b[j][\"head_end\"],\n                )\n                tail_ov = span_overlap(\n                    rels_a[i][\"tail_start\"], rels_a[i][\"tail_end\"],\n                    rels_b[j][\"tail_start\"], rels_b[j][\"tail_end\"],\n                )\n                cost[i, j] = (head_ov + tail_ov) / 2.0\n    row_ind, col_ind = linear_sum_assignment(cost, maximize=True)\n    matched_sum = cost[row_ind, col_ind].sum()\n    denom = n_a + n_b - matched_sum\n    return matched_sum / denom if denom > 0 else 1.0\n\ndef compute_hybrid(jsonl_path, dataset_name, task_type=\"ner\"):\n    with open(jsonl_path) as f:\n        instances = [json.loads(line) for line in f if line.strip()]\n    \n    n_instances = len(instances)\n    n_samples = len(instances[0][\"samples\"])\n    \n    greedy_f1s = []\n    random_f1s = []\n    mbr_sj_f1s = []\n    oracle_f1s = []\n    hybrid_f1s = []\n    \n    n_degenerate = 0\n    n_non_degenerate = 0\n    \n    for inst in instances:\n        gold = inst[\"gold\"]\n        samples = inst[\"samples\"]\n        N = len(samples)\n        \n        # Compute F1 for each sample\n        if task_type == \"ner\":\n            f1s = np.array([entity_strict_f1(s.get(\"entities\", []), gold.get(\"entities\", [])) for s in samples])\n            greedy_f1 = entity_strict_f1(inst[\"greedy\"].get(\"entities\", []), gold.get(\"entities\", []))\n        else:  # RE\n            f1s = np.array([relation_strict_f1(s.get(\"relations\", []), gold.get(\"relations\", [])) for s in samples])\n            greedy_f1 = relation_strict_f1(inst[\"greedy\"].get(\"relations\", []), gold.get(\"relations\", []))\n        \n        # Compute SJ utility for each sample (average pairwise SJ with all others)\n        if task_type == \"ner\":\n            sj_matrix = np.zeros((N, N))\n            for i, j in combinations(range(N), 2):\n                v = ner_soft_jaccard_pair(\n                    samples[i].get(\"entities\", []),\n                    samples[j].get(\"entities\", [])\n                )\n                sj_matrix[i, j] = v\n                sj_matrix[j, i] = v\n            np.fill_diagonal(sj_matrix, 1.0)\n        else:  # RE\n            sj_matrix = np.zeros((N, N))\n            for i, j in combinations(range(N), 2):\n                v = rel_soft_jaccard_pair(\n                    samples[i].get(\"relations\", []),\n                    samples[j].get(\"relations\", [])\n                )\n                sj_matrix[i, j] = v\n                sj_matrix[j, i] = v\n            np.fill_diagonal(sj_matrix, 1.0)\n        \n        # SJ utility = mean pairwise SJ (excluding self)\n        sj_utilities = (sj_matrix.sum(axis=1) - 1.0) / (N - 1)\n        \n        # Identify degenerate: all F1s are the same\n        is_degenerate = np.var(f1s) < 1e-10\n        \n        # Baselines\n        greedy_f1s.append(greedy_f1)\n        random_f1s.append(float(np.mean(f1s)))\n        \n        # MBR (SJ-selected): always pick highest SJ utility sample\n        mbr_idx = int(np.argmax(sj_utilities))\n        mbr_sj_f1s.append(float(f1s[mbr_idx]))\n        \n        # Oracle: best F1 sample\n        oracle_f1s.append(float(np.max(f1s)))\n        \n        # Hybrid: degenerate -> greedy, non-degenerate -> MBR\n        if is_degenerate:\n            n_degenerate += 1\n            hybrid_f1s.append(greedy_f1)\n        else:\n            n_non_degenerate += 1\n            hybrid_f1s.append(float(f1s[mbr_idx]))\n    \n    results = {\n        \"dataset\": dataset_name,\n        \"task_type\": task_type,\n        \"n_instances\": n_instances,\n        \"n_samples_per_instance\": n_samples,\n        \"n_degenerate\": n_degenerate,\n        \"n_non_degenerate\": n_non_degenerate,\n        \"pct_degenerate\": round(100 * n_degenerate / n_instances, 1),\n        \"greedy_f1\": round(float(np.mean(greedy_f1s)), 4),\n        \"random_f1\": round(float(np.mean(random_f1s)), 4),\n        \"mbr_sj_f1\": round(float(np.mean(mbr_sj_f1s)), 4),\n        \"oracle_f1\": round(float(np.mean(oracle_f1s)), 4),\n        \"hybrid_f1\": round(float(np.mean(hybrid_f1s)), 4),\n        \"hybrid_gain_over_greedy\": round(float(np.mean(hybrid_f1s)) - float(np.mean(greedy_f1s)), 4),\n        \"hybrid_gain_over_random\": round(float(np.mean(hybrid_f1s)) - float(np.mean(random_f1s)), 4),\n        \"mbr_gain_over_greedy\": round(float(np.mean(mbr_sj_f1s)) - float(np.mean(greedy_f1s)), 4),\n        \"mbr_gain_over_random\": round(float(np.mean(mbr_sj_f1s)) - float(np.mean(random_f1s)), 4),\n    }\n    \n    # Compute oracle gap closed\n    oracle_gap = float(np.mean(oracle_f1s)) - float(np.mean(random_f1s))\n    if oracle_gap > 1e-10:\n        results[\"hybrid_pct_oracle_gap\"] = round(100 * (float(np.mean(hybrid_f1s)) - float(np.mean(random_f1s))) / oracle_gap, 1)\n        results[\"mbr_pct_oracle_gap\"] = round(100 * (float(np.mean(mbr_sj_f1s)) - float(np.mean(random_f1s))) / oracle_gap, 1)\n    \n    return results\n\nif __name__ == \"__main__\":\n    outdir = \"/root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy\"\n    os.makedirs(outdir, exist_ok=True)\n    \n    datasets = {\n        \"SciERC_NER_Qwen8B_N8\": {\n            \"path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\",\n            \"task\": \"ner\"\n        },\n        \"CoNLL_NER_Qwen8B_N16\": {\n            \"path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl\",\n            \"task\": \"ner\"\n        },\n        \"SciERC_RE_Qwen8B_N16\": {\n            \"path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2/samples.jsonl\",\n            \"task\": \"re\"\n        },\n    }\n    \n    all_results = {}\n    for name, cfg in datasets.items():\n        print(f\"Processing {name}...\")\n        if not os.path.exists(cfg[\"path\"]):\n            print(f\"  SKIP: {cfg['path']} not found\")\n            continue\n        all_results[name] = compute_hybrid(cfg[\"path\"], name, cfg[\"task\"])\n        r = all_results[name]\n        print(f\"  n={r['n_instances']}, N={r['n_samples_per_instance']}\")\n        print(f\"  degenerate: {r['n_degenerate']} ({r['pct_degenerate']}%)\")\n        print(f\"  greedy={r['greedy_f1']:.4f}, random={r['random_f1']:.4f}, MBR={r['mbr_sj_f1']:.4f}, hybrid={r['hybrid_f1']:.4f}, oracle={r['oracle_f1']:.4f}\")\n        print(f\"  hybrid gain over greedy: {r['hybrid_gain_over_greedy']:+.4f}\")\n        print(f\"  hybrid gain over random: {r['hybrid_gain_over_random']:+.4f}\")\n        print()\n    \n    # Save results\n    with open(os.path.join(outdir, \"results.json\"), \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    \n    # Generate summary\n    lines = [\"# Hybrid Strategy: Expected F1 Gain\", \"\"]\n    lines.append(\"**Strategy**: Use greedy for degenerate instances (constant F1 across all samples),\")\n    lines.append(\"MBR selection (highest SJ utility) for non-degenerate instances.\")\n    lines.append(\"\")\n    lines.append(\"| Dataset | N | #Inst | %Degen | Greedy | Random | MBR-SJ | **Hybrid** | Oracle | Hybrid Δ(greedy) |\")\n    lines.append(\"|---------|---|-------|--------|--------|--------|--------|------------|--------|------------------|\")\n    for name, r in all_results.items():\n        lines.append(f\"| {name} | {r['n_samples_per_instance']} | {r['n_instances']} | {r['pct_degenerate']}% | {r['greedy_f1']:.4f} | {r['random_f1']:.4f} | {r['mbr_sj_f1']:.4f} | **{r['hybrid_f1']:.4f}** | {r['oracle_f1']:.4f} | {r['hybrid_gain_over_greedy']:+.4f} |\")\n    lines.append(\"\")\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n    for name, r in all_results.items():\n        lines.append(f\"### {name}\")\n        lines.append(f\"- Degenerate instances: {r['n_degenerate']}/{r['n_instances']} ({r['pct_degenerate']}%)\")\n        lines.append(f\"- Non-degenerate instances: {r['n_non_degenerate']}/{r['n_instances']} ({100-r['pct_degenerate']:.1f}%)\")\n        lines.append(f\"- Hybrid F1 = {r['hybrid_f1']:.4f} (gain over greedy: {r['hybrid_gain_over_greedy']:+.4f})\")\n        lines.append(f\"- Pure MBR F1 = {r['mbr_sj_f1']:.4f} (gain over greedy: {r['mbr_gain_over_greedy']:+.4f})\")\n        if \"hybrid_pct_oracle_gap\" in r:\n            lines.append(f\"- Hybrid closes {r['hybrid_pct_oracle_gap']:.1f}% of oracle gap (vs {r['mbr_pct_oracle_gap']:.1f}% for pure MBR)\")\n        lines.append(\"\")\n    \n    summary = \"\\n\".join(lines)\n    with open(os.path.join(outdir, \"summary.md\"), \"w\") as f:\n        f.write(summary)\n    \n    print(\"Done. Results saved to\", outdir)\nSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T09:28:08.799570+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T09:28:08.799709+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy && python compute_hybrid.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy && python compute_hybrid.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T09:28:08.799853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Processing SciERC_NER_Qwen8B_N8...\\n  n=551, N=8\\n  degenerate: 116 (21.1%)\\n  greedy=0.6182, random=0.5835, MBR=0.6188, hybrid=0.6200, oracle=0.7448\\n  hybrid gain over greedy: +0.0018\\n  hybrid gain over random: +0.0365\\n\\nProcessing CoNLL_NER_Qwen8B_N16...\\n  n=3453, N=16\\n  degenerate: 2002 (58.0%)\\n  greedy=0.7239, random=0.6919, MBR=0.7215, hybrid=0.7215, oracle=0.7639\\n  hybrid gain over greedy: -0.0024\\n  hybrid gain over random: +0.0295\\n\\nProcessing SciERC_RE_Qwen8B_N16...\\n  n=551, N=16\\n  degenerate: 252 (45.7%)\\n  greedy=0.2904, random=0.2612, MBR=0.2847, hybrid=0.2847, oracle=0.4544\\n  hybrid gain over greedy: -0.0057\\n  hybrid gain over random: +0.0235\\n\\nDone. Results saved to /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T09:28:08.800033+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/summary.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/summary.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T09:28:08.800207+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Hybrid Strategy: Expected F1 Gain\\n\\n**Strategy**: Use greedy for degenerate instances (constant F1 across all samples),\\nMBR selection (highest SJ utility) for non-degenerate instances.\\n\\n| Dataset | N | #Inst | %Degen | Greedy | Random | MBR-SJ | **Hybrid** | Oracle | Hybrid Δ(greedy) |\\n|---------|---|-------|--------|--------|--------|--------|------------|--------|------------------|\\n| SciERC_NER_Qwen8B_N8 | 8 | 551 | 21.1% | 0.6182 | 0.5835 | 0.6188 | **0.6200** | 0.7448 | +0.0018 |\\n| CoNLL_NER_Qwen8B_N16 | 16 | 3453 | 58.0% | 0.7239 | 0.6919 | 0.7215 | **0.7215** | 0.7639 | -0.0024 |\\n| SciERC_RE_Qwen8B_N16 | 16 | 551 | 45.7% | 0.2904 | 0.2612 | 0.2847 | **0.2847** | 0.4544 | -0.0057 |\\n\\n## Key Findings\\n\\n### SciERC_NER_Qwen8B_N8\\n- Degenerate instances: 116/551 (21.1%)\\n- Non-degenerate instances: 435/551 (78.9%)\\n- Hybrid F1 = 0.6200 (gain over greedy: +0.0018)\\n- Pure MBR F1 = 0.6188 (gain over greedy: +0.0005)\\n- Hybrid closes 22.6% of oracle gap (vs 21.9% for pure MBR)\\n\\n### CoNLL_NER_Qwen8B_N16\\n- Degenerate instances: 2002/3453 (58.0%)\\n- Non-degenerate instances: 1451/3453 (42.0%)\\n- Hybrid F1 = 0.7215 (gain over greedy: -0.0024)\\n- Pure MBR F1 = 0.7215 (gain over greedy: -0.0024)\\n- Hybrid closes 41.0% of oracle gap (vs 41.0% for pure MBR)\\n\\n### SciERC_RE_Qwen8B_N16\\n- Degenerate instances: 252/551 (45.7%)\\n- Non-degenerate instances: 299/551 (54.3%)\\n- Hybrid F1 = 0.2847 (gain over greedy: -0.0057)\\n- Pure MBR F1 = 0.2847 (gain over greedy: -0.0057)\\n- Hybrid closes 12.2% of oracle gap (vs 12.2% for pure MBR)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T09:28:08.800387+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T09:28:08.800562+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"SciERC_NER_Qwen8B_N8\\\": {\\n    \\\"dataset\\\": \\\"SciERC_NER_Qwen8B_N8\\\",\\n    \\\"task_type\\\": \\\"ner\\\",\\n    \\\"n_instances\\\": 551,\\n    \\\"n_samples_per_instance\\\": 8,\\n    \\\"n_degenerate\\\": 116,\\n    \\\"n_non_degenerate\\\": 435,\\n    \\\"pct_degenerate\\\": 21.1,\\n    \\\"greedy_f1\\\": 0.6182,\\n    \\\"random_f1\\\": 0.5835,\\n    \\\"mbr_sj_f1\\\": 0.6188,\\n    \\\"oracle_f1\\\": 0.7448,\\n    \\\"hybrid_f1\\\": 0.62,\\n    \\\"hybrid_gain_over_greedy\\\": 0.0018,\\n    \\\"hybrid_gain_over_random\\\": 0.0365,\\n    \\\"mbr_gain_over_greedy\\\": 0.0005,\\n    \\\"mbr_gain_over_random\\\": 0.0353,\\n    \\\"hybrid_pct_oracle_gap\\\": 22.6,\\n    \\\"mbr_pct_oracle_gap\\\": 21.9\\n  },\\n  \\\"CoNLL_NER_Qwen8B_N16\\\": {\\n    \\\"dataset\\\": \\\"CoNLL_NER_Qwen8B_N16\\\",\\n    \\\"task_type\\\": \\\"ner\\\",\\n    \\\"n_instances\\\": 3453,\\n    \\\"n_samples_per_instance\\\": 16,\\n    \\\"n_degenerate\\\": 2002,\\n    \\\"n_non_degenerate\\\": 1451,\\n    \\\"pct_degenerate\\\": 58.0,\\n    \\\"greedy_f1\\\": 0.7239,\\n    \\\"random_f1\\\": 0.6919,\\n    \\\"mbr_sj_f1\\\": 0.7215,\\n    \\\"oracle_f1\\\": 0.7639,\\n    \\\"hybrid_f1\\\": 0.7215,\\n    \\\"hybrid_gain_over_greedy\\\": -0.0024,\\n    \\\"hybrid_gain_over_random\\\": 0.0295,\\n    \\\"mbr_gain_over_greedy\\\": -0.0024,\\n    \\\"mbr_gain_over_random\\\": 0.0295,\\n    \\\"hybrid_pct_oracle_gap\\\": 41.0,\\n    \\\"mbr_pct_oracle_gap\\\": 41.0\\n  },\\n  \\\"SciERC_RE_Qwen8B_N16\\\": {\\n    \\\"dataset\\\": \\\"SciERC_RE_Qwen8B_N16\\\",\\n    \\\"task_type\\\": \\\"re\\\",\\n    \\\"n_instances\\\": 551,\\n    \\\"n_samples_per_instance\\\": 16,\\n    \\\"n_degenerate\\\": 252,\\n    \\\"n_non_degenerate\\\": 299,\\n    \\\"pct_degenerate\\\": 45.7,\\n    \\\"greedy_f1\\\": 0.2904,\\n    \\\"random_f1\\\": 0.2612,\\n    \\\"mbr_sj_f1\\\": 0.2847,\\n    \\\"oracle_f1\\\": 0.4544,\\n    \\\"hybrid
…[truncated 396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T09:28:08.800732+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "d112_hybrid_strategy",
  "type": "data",
  "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. Results across SciERC NER/RE and CoNLL NER.",
  "project": "struct_self_consist_ie",
  "exp_id": "d112",
  "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/results.json",
  "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "d112_hybrid_strategy",
    "type": "data",
    "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. Results across SciERC NER/RE and CoNLL NER.",
    "project": "struct_self_consist_ie",
    "exp_id": "d112",
    "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/results.json",
    "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T09:28:08.800874+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/results.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T09:28:08.801031+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "d112_hybrid_strategy",
  "type": "data",
  "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. Results across SciERC NER/RE and CoNLL NER.",
  "project": "struct_self_consist_ie",
  "exp_id": "d112",
  "content": "{\n  \"SciERC_NER_Qwen8B_N8\": {\n    \"dataset\": \"SciERC_NER_Qwen8B_N8\",\n    \"task_type\": \"ner\",\n    \"n_instances\": 551,\n    \"n_samples_per_instance\": 8,\n    \"n_degenerate\": 116,\n    \"n_non_degenerate\": 435,\n    \"pct_degenerate\": 21.1,\n    \"greedy_f1\": 0.6182,\n    \"random_f1\": 0.5835,\n    \"mbr_sj_f1\": 0.6188,\n    \"oracle_f1\": 0.7448,\n    \"hybrid_f1\": 0.62,\n    \"hybrid_gain_over_greedy\": 0.0018,\n    \"hybrid_gain_over_random\": 0.0365,\n    \"mbr_gain_over_greedy\": 0.0005,\n    \"mbr_gain_over_random\": 0.0353,\n    \"hybrid_pct_oracle_gap\": 22.6,\n    \"mbr_pct_oracle_gap\": 21.9\n  },\n  \"CoNLL_NER_Qwen8B_N16\": {\n    \"dataset\": \"CoNLL_NER_Qwen8B_N16\",\n    \"task_type\": \"ner\",\n    \"n_instances\": 3453,\n    \"n_samples_per_instance\": 16,\n    \"n_degenerate\": 2002,\n    \"n_non_degenerate\": 1451,\n    \"pct_degenerate\": 58.0,\n    \"greedy_f1\": 0.7239,\n    \"random_f1\": 0.6919,\n    \"mbr_sj_f1\": 0.7215,\n    \"oracle_f1\": 0.7639,\n    \"hybrid_f1\": 0.7215,\n    \"hybrid_gain_over_greedy\": -0.0024,\n    \"hybrid_gain_over_random\": 0.0295,\n    \"mbr_gain_over_greedy\": -0.0024,\n    \"mbr_gain_over_random\": 0.0295,\n    \"hybrid_pct_oracle_gap\": 41.0,\n    \"mbr_pct_oracle_gap\": 41.0\n  },\n  \"SciERC_RE_Qwen8B_N16\": {\n    \"dataset\": \"SciERC_RE_Qwen8B_N16\",\n    \"task_type\": \"re\",\n    \"n_instances\": 551,\n    \"n_samples_per_instance\": 16,\n    \"n_degenerate\": 252,\n    \"n_non_degenerate\": 299,\n    \"pct_degenerate\": 45.7,\n    \"greedy_f1\": 0.2904,\n    \"random_f1\": 0.2612,\n    \"mbr_sj_f1\": 0.2847,\n    \"oracle_f1\": 0.4544,\n    \"hybrid_f1\": 0.2847,\n    \"hybrid_gain_over_greedy\": -0.0057,\n    \"hybrid_gain_over_random\": 0.0235,\n    \"mbr_gain_over_greedy\": -0.0057,\n    \"mbr_gain_over_random\": 0.0235,\n    \"hybrid_pct_oracle_gap\": 12.2,\n    \"mbr_pct_oracle_gap\": 12.2\n  }\n}",
  "content_filename": "results.json",
  "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "d112_hybrid_strategy",
    "type": "data",
    "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. Results across SciERC NER/RE and CoNLL NER.",
    "project": "struct_self_consist_ie",
    "exp_id": "d112",
    "content": "{\n  \"SciERC_NER_Qwen8B_N8\": {\n    \"dataset\": \"SciERC_NER_Qwen8B_N8\",\n    \"task_type\": \"ner\",\n    \"n_instances\": 551,\n    \"n_samples_per_instance\": 8,\n    \"n_degenerate\": 116,\n    \"n_non_degenerate\": 435,\n    \"pct_degenerate\": 21.1,\n    \"greedy_f1\": 0.6182,\n    \"random_f1\": 0.5835,\n    \"mbr_sj_f1\": 0.6188,\n    \"oracle_f1\": 0.7448,\n    \"hybrid_f1\": 0.62,\n    \"hybrid_gain_over_greedy\": 0.0018,\n    \"hybrid_gain_over_random\": 0.0365,\n    \"mbr_gain_over_greedy\": 0.0005,\n    \"mbr_gain_over_random\": 0.0353,\n    \"hybrid_pct_oracle_gap\": 22.6,\n    \"mbr_pct_oracle_gap\": 21.9\n  },\n  \"CoNLL_NER_Qwen8B_N16\": {\n    \"dataset\": \"CoNLL_NER_Qwen8B_N16\",\n    \"task_type\": \"ner\",\n    \"n_instances\": 3453,\n    \"n_samples_per_instance\": 16,\n    \"n_degenerate\": 2002,\n    \"n_non_degenerate\": 1451,\n    \"pct_degenerate\": 58.0,\n    \"greedy_f1\": 0.7239,\n    \"random_f1\": 0.6919,\n    \"mbr_sj_f1\": 0.7215,\n    \"oracle_f1\": 0.7639,\n    \"hybrid_f1\": 0.7215,\n    \"hybrid_gain_over_greedy\": -0.0024,\n    \"hybrid_gain_over_random\": 0.0295,\n    \"mbr_gain_over_greedy\": -0.0024,\n    \"mbr_gain_over_random\": 0.0295,\n    \"hybrid_pct_oracle_gap\": 41.0,\n    \"mbr_pct_oracle_gap\": 41.0\n  },\n  \"SciERC_RE_Qwen8B_N16\": {\n    \"dataset\": \"SciERC_RE_Qwen8B_N16\",\n    \"task_type\": \"re\",\n    \"n_instances\": 551,\n    \"n_samples_per_instance\": 16,\n    \"n_degenerate\": 252,\n    \"n_non_degenerate\": 299,\n    \"pct_degenerate\": 45.7,\n    \"greedy_f1\": 0.2904,\n    \"random_f1\": 0.2612,\n    \"mbr_sj_f1\": 0.2847,\n    \"oracle_f1\": 0.4544,\n    \"hybrid_f1\": 0.2847,\n    \"hybrid_gain_over_greedy\": -0.0057,\n    \"hybrid_gain_over_random\": 0.0235,\n    \"mbr_gain_over_greedy\": -0.0057,\n    \"mbr_gain_over_random\": 0.0235,\n    \"hybrid_pct_oracle_gap\": 12.2,\n    \"mbr_pct_oracle_gap\": 12.2\n  }\n}",
    "content_filename": "results.json",
    "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T09:28:08.801203+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'SciERC_NER_Qwen8B_N8': ..._pct_oracle_gap': 12.2}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T09:28:08.801349+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "d112_hybrid_strategy",
  "type": "data",
  "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. SciERC NER hybrid=0.6200 (+0.0018 over greedy), CoNLL NER hybrid=0.7215 (-0.0024), SciERC RE hybrid=0.2847 (-0.0057).",
  "project": "struct_self_consist_ie",
  "exp_id": "d112",
  "content": "{\"SciERC_NER_Qwen8B_N8\":{\"n_instances\":551,\"n_samples_per_instance\":8,\"n_degenerate\":116,\"pct_degenerate\":21.1,\"greedy_f1\":0.6182,\"random_f1\":0.5835,\"mbr_sj_f1\":0.6188,\"oracle_f1\":0.7448,\"hybrid_f1\":0.62,\"hybrid_gain_over_greedy\":0.0018,\"hybrid_pct_oracle_gap\":22.6},\"CoNLL_NER_Qwen8B_N16\":{\"n_instances\":3453,\"n_samples_per_instance\":16,\"n_degenerate\":2002,\"pct_degenerate\":58.0,\"greedy_f1\":0.7239,\"random_f1\":0.6919,\"mbr_sj_f1\":0.7215,\"oracle_f1\":0.7639,\"hybrid_f1\":0.7215,\"hybrid_gain_over_greedy\":-0.0024,\"hybrid_pct_oracle_gap\":41.0},\"SciERC_RE_Qwen8B_N16\":{\"n_instances\":551,\"n_samples_per_instance\":16,\"n_degenerate\":252,\"pct_degenerate\":45.7,\"greedy_f1\":0.2904,\"random_f1\":0.2612,\"mbr_sj_f1\":0.2847,\"oracle_f1\":0.4544,\"hybrid_f1\":0.2847,\"hybrid_gain_over_greedy\":-0.0057,\"hybrid_pct_oracle_gap\":12.2}}",
  "content_filename": "results.json",
  "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "d112_hybrid_strategy",
    "type": "data",
    "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. SciERC NER hybrid=0.6200 (+0.0018 over greedy), CoNLL NER hybrid=0.7215 (-0.0024), SciERC RE hybrid=0.2847 (-0.0057).",
    "project": "struct_self_consist_ie",
    "exp_id": "d112",
    "content": "{\"SciERC_NER_Qwen8B_N8\":{\"n_instances\":551,\"n_samples_per_instance\":8,\"n_degenerate\":116,\"pct_degenerate\":21.1,\"greedy_f1\":0.6182,\"random_f1\":0.5835,\"mbr_sj_f1\":0.6188,\"oracle_f1\":0.7448,\"hybrid_f1\":0.62,\"hybrid_gain_over_greedy\":0.0018,\"hybrid_pct_oracle_gap\":22.6},\"CoNLL_NER_Qwen8B_N16\":{\"n_instances\":3453,\"n_samples_per_instance\":16,\"n_degenerate\":2002,\"pct_degenerate\":58.0,\"greedy_f1\":0.7239,\"random_f1\":0.6919,\"mbr_sj_f1\":0.7215,\"oracle_f1\":0.7639,\"hybrid_f1\":0.7215,\"hybrid_gain_over_greedy\":-0.0024,\"hybrid_pct_oracle_gap\":41.0},\"SciERC_RE_Qwen8B_N16\":{\"n_instances\":551,\"n_samples_per_instance\":16,\"n_degenerate\":252,\"pct_degenerate\":45.7,\"greedy_f1\":0.2904,\"random_f1\":0.2612,\"mbr_sj_f1\":0.2847,\"oracle_f1\":0.4544,\"hybrid_f1\":0.2847,\"hybrid_gain_over_greedy\":-0.0057,\"hybrid_pct_oracle_gap\":12.2}}",
    "content_filename": "results.json",
    "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T09:28:08.801488+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'SciERC_NER_Qwen8B_N8': ..._pct_oracle_gap': 12.2}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T09:28:08.801641+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "d112_hybrid_strategy",
  "type": "data",
  "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. SciERC NER hybrid=0.6200 (+0.0018 over greedy), CoNLL NER hybrid=0.7215 (-0.0024), SciERC RE hybrid=0.2847 (-0.0057).",
  "project": "struct_self_consist_ie",
  "exp_id": "d112",
  "content": "# Hybrid Strategy: Expected F1 Gain\n\nStrategy: Use greedy for degenerate instances (constant F1 across all samples), MBR selection (highest SJ utility) for non-degenerate instances.\n\n| Dataset | N | #Inst | %Degen | Greedy | Random | MBR-SJ | Hybrid | Oracle | Hybrid-Greedy |\n|---------|---|-------|--------|--------|--------|--------|--------|--------|---------------|\n| SciERC NER | 8 | 551 | 21.1% | 0.6182 | 0.5835 | 0.6188 | 0.6200 | 0.7448 | +0.0018 |\n| CoNLL NER | 16 | 3453 | 58.0% | 0.7239 | 0.6919 | 0.7215 | 0.7215 | 0.7639 | -0.0024 |\n| SciERC RE | 16 | 551 | 45.7% | 0.2904 | 0.2612 | 0.2847 | 0.2847 | 0.4544 | -0.0057 |\n\nKey: Hybrid marginally helps SciERC NER (+0.18pp) but does not beat greedy on CoNLL/RE where degenerate proportion is high. On non-degenerate instances, MBR selection underperforms greedy for CoNLL/RE tasks.\n\nOutput: /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/",
  "content_filename": "summary.md",
  "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "d112_hybrid_strategy",
    "type": "data",
    "description": "Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. SciERC NER hybrid=0.6200 (+0.0018 over greedy), CoNLL NER hybrid=0.7215 (-0.0024), SciERC RE hybrid=0.2847 (-0.0057).",
    "project": "struct_self_consist_ie",
    "exp_id": "d112",
    "content": "# Hybrid Strategy: Expected F1 Gain\n\nStrategy: Use greedy for degenerate instances (constant F1 across all samples), MBR selection (highest SJ utility) for non-degenerate instances.\n\n| Dataset | N | #Inst | %Degen | Greedy | Random | MBR-SJ | Hybrid | Oracle | Hybrid-Greedy |\n|---------|---|-------|--------|--------|--------|--------|--------|--------|---------------|\n| SciERC NER | 8 | 551 | 21.1% | 0.6182 | 0.5835 | 0.6188 | 0.6200 | 0.7448 | +0.0018 |\n| CoNLL NER | 16 | 3453 | 58.0% | 0.7239 | 0.6919 | 0.7215 | 0.7215 | 0.7639 | -0.0024 |\n| SciERC RE | 16 | 551 | 45.7% | 0.2904 | 0.2612 | 0.2847 | 0.2847 | 0.4544 | -0.0057 |\n\nKey: Hybrid marginally helps SciERC NER (+0.18pp) but does not beat greedy on CoNLL/RE where degenerate proportion is high. On non-degenerate instances, MBR selection underperforms greedy for CoNLL/RE tasks.\n\nOutput: /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/",
    "content_filename": "summary.md",
    "tags": "['hybrid', 'mbr', 'greedy', 'degenerate', 'q5', 'rebuttal']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T09:28:08.801807+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_421a8c\", \"name\": \"d112_hybrid_strategy\", \"type\": \"data\", \"description\": \"Hybrid strategy expected F1: greedy for degenerate instances + MBR-SJ for non-degenerate. SciERC NER hybrid=0.6200 (+0.0018 over greedy), CoNLL NER hybrid=0.7215 (-0.0024), SciERC RE hybrid=0.2847 (-0.0057).\", \"path\": \"projects/struct_self_consist_ie/artifacts/d112/data/summary.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"d112\", \"skill\": \"\", \"created_at\": \"2026-05-16T09:28:00.767701+00:00\", \"tags\": [\"hybrid\", \"mbr\", \"greedy\", \"degenerate\", \"q5\", \"rebuttal\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-16T09:28:08.801977+00:00_

完成。结果保存于 `/root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/`。

**核心结论：**

| Dataset | %Degen | Greedy | MBR-SJ | **Hybrid** | Hybrid Δ(greedy) |
|---------|--------|--------|--------|------------|------------------|
| SciERC NER (N=8) | 21.1% | 0.6182 | 0.6188 | **0.6200** | **+0.0018** |
| CoNLL NER (N=16) | 58.0% | 0.7239 | 0.7215 | 0.7215 | -0.0024 |
| SciERC RE (N=16) | 45.7% | 0.2904 | 0.2847 | 0.2847 | -0.0057 |

Hybrid 策略（degenerate 用 greedy，non-degenerate 用 MBR-SJ）仅在 SciERC NER 上微弱优于 greedy (+0.18pp)。CoNLL/RE 的 degenerate 比例高（58%/46%），且在 non-degenerate instances 上 MBR 选择并未超过 greedy，导致 hybrid 反而略低于 greedy。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d112_q5_hybrid_strategy_20260516T092356"
}
```

</details>

---
