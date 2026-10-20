# analysis option c degen vs headroom

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_option_c_degen_vs_headroom_20260517T085228.jsonl`
- **Structured JSON:** [`17def1ce2e1225f5792e.json`](../../sessions/17/17def1ce2e1225f5792e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T08:53:53.630707+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T08:53:53.631024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T08:53:53.631224+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/sampled_results.jsonl | python3 -m json.tool | head -60",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/sampled_results.jsonl | python3 -m json.tool | head -60",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T08:53:53.631379+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\nhead: cannot open '/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/sampled_results.jsonl' for reading: No such file or directory\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T08:53:53.631510+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && ls /root/autodl-tmp/struct_self_consist_ie/output/ | grep exp_021",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && ls /root/autodl-tmp/struct_self_consist_ie/output/ | grep exp_021",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T08:53:53.631642+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp_021_fewnerd_full\\nexp_021_inference\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T08:53:53.631765+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && ls /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && ls /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T08:53:53.631892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_log.txt\\nexp021_full_analysis.json\\nfull_analysis_log.txt\\nper_type_lp_analysis.csv\\nper_type_lp_table.tex\\nresults.json\\nsamples.jsonl\\nshard_0\\nshard_1\\nshard_2\\nshard_3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T08:53:53.632025+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl | python -m json.tool | head -80",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl | python -m json.tool | head -80",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T08:53:53.632220+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n    \\\"id\\\": \\\"fewnerd_test_00000\\\",\\n    \\\"text\\\": \\\"In the early 1930s the band moved to the Grill Room of the Taft Hotel in New York ; the band was renamed `` George Hall and His Hotel Taft Orchestra `` .\\\",\\n    \\\"gold\\\": {\\n        \\\"entities\\\": [\\n            {\\n                \\\"text\\\": \\\"Grill Room\\\",\\n                \\\"type\\\": \\\"building\\\",\\n                \\\"start\\\": 41,\\n                \\\"end\\\": 51\\n            },\\n            {\\n                \\\"text\\\": \\\"Taft Hotel\\\",\\n                \\\"type\\\": \\\"building\\\",\\n                \\\"start\\\": 59,\\n                \\\"end\\\": 69\\n            },\\n            {\\n                \\\"text\\\": \\\"New York\\\",\\n                \\\"type\\\": \\\"location\\\",\\n                \\\"start\\\": 73,\\n                \\\"end\\\": 81\\n            },\\n            {\\n                \\\"text\\\": \\\"George Hall and His Hotel Taft Orchestra\\\",\\n                \\\"type\\\": \\\"organization\\\",\\n                \\\"start\\\": 108,\\n                \\\"end\\\": 148\\n            }\\n        ],\\n        \\\"relations\\\": [],\\n        \\\"events\\\": []\\n    },\\n    \\\"samples\\\": [\\n        {\\n            \\\"entities\\\": [\\n                {\\n                    \\\"text\\\": \\\"Grill Room\\\",\\n                    \\\"type\\\": \\\"building\\\",\\n                    \\\"start\\\": 41,\\n                    \\\"end\\\": 51\\n                },\\n                {\\n                    \\\"text\\\": \\\"Taft Hotel\\\",\\n                    \\\"type\\\": \\\"building\\\",\\n                    \\\"start\\\": 59,\\n                    \\\"end\\\": 69\\n                },\\n                {\\n                    \\\"text\\\": \\\"New York\\\",\\n                    \\\"type\\\": \\\"location\\\",\\n                    \\\"start\\\": 73,\\n                  
…[truncated 1106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T08:53:53.632393+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl | python -c \"import json,sys; d=json.loads(sys.stdin.readline()); print(list(d.keys())); print('n_samples:', len(d['samples'])); s=d['samples'][0]; print('sample keys:', [k for k in s.keys() if k != 'token_logprobs'])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl | python -c \"import json,sys; d=json.loads(sys.stdin.readline()); print(list(d.keys())); print('n_samples:', len(d['samples'])); s=d['samples'][0]; print('sample keys:', [k for k in s.keys() if k != 'token_logprobs'])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T08:53:53.632528+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"['id', 'text', 'gold', 'samples', 'greedy', 'logprobs']\\nn_samples: 8\\nsample keys: ['entities', 'relations', 'events', 'cumulative_logprob', 'n_tokens', 'mean_logprob', 'token_texts']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T08:53:53.632652+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl | python -c \"\nimport json,sys\nd=json.loads(sys.stdin.readline())\nprint('greedy keys:', list(d['greedy'].keys()))\nprint('greedy entities:', d['greedy']['entities'][:2])\nprint('logprobs keys:', list(d['logprobs'].keys()) if isinstance(d['logprobs'], dict) else type(d['logprobs']))\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl | python -c \"\nimport json,sys\nd=json.loads(sys.stdin.readline())\nprint('greedy keys:', list(d['greedy'].keys()))\nprint('greedy entities:', d['greedy']['entities'][:2])\nprint('logprobs keys:', list(d['logprobs'].keys()) if isinstance(d['logprobs'], dict) else type(d['logprobs']))\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T08:53:53.632785+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"greedy keys: ['entities', 'relations', 'events', 'cumulative_logprob', 'n_tokens', 'mean_logprob', 'token_logprobs', 'token_texts']\\ngreedy entities: [{'text': 'Grill Room of the Taft Hotel', 'type': 'building', 'start': 41, 'end': 69}, {'text': 'New York', 'type': 'location', 'start': 73, 'end': 81}]\\nlogprobs keys: &lt;class 'list'>\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T08:53:53.632944+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && python << 'PYEOF'\nimport json, numpy as np\nfrom collections import Counter, defaultdict\nfrom scipy.stats import spearmanr\n\ndef entities_to_set(entities):\n    \"\"\"Convert entity list to set of (text, type, start, end) tuples for exact match.\"\"\"\n    return set((e['text'], e['type'], e['start'], e['end']) for e in entities)\n\ndef compute_f1(pred_entities, gold_entities):\n    \"\"\"Compute entity-level F1 between pred and gold.\"\"\"\n    pred_set = entities_to_set(pred_entities)\n    gold_set = entities_to_set(gold_entities)\n    if not pred_set and not gold_set:\n        return 1.0\n    if not pred_set or not gold_set:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    precision = tp / len(pred_set) if pred_set else 0.0\n    recall = tp / len(gold_set) if gold_set else 0.0\n    if precision + recall == 0:\n        return 0.0\n    return 2 * precision * recall / (precision + recall)\n\n# Load data\ndata = []\nwith open('/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl') as f:\n    for line in f:\n        data.append(json.loads(line))\n\nprint(f\"Total instances: {len(data)}\")\n\n# Per-type oracle headroom\ntype_greedy_f1s = defaultdict(list)\ntype_oracle_f1s = defaultdict(list)\n\nfor inst in data:\n    gold_entities = inst['gold']['entities']\n    if not gold_entities:  # gold-filtered: skip instances with no gold entities\n        continue\n    \n    # Determine dominant entity type\n    types = [e['type'] for e in gold_entities]\n    dominant_type = Counter(types).most_common(1)[0][0]\n    \n    # Greedy F1\n    greedy_entities = inst['greedy']['entities']\n    greedy_f1 = compute_f1(greedy_entities, gold_entities)\n    \n    # Oracle F1 = max F1 across all samples\n    sample_f1s = []\n    for s in inst['samples']:\n        sf1 = compute_f1(s['entities'], gold_entities)\n        sample_f1s.append(sf1)\n    \n    if sample_f1s:\n        oracle_f1 = max(sample_f1s)\n        type_greedy_f1s[dominant_type].append(greedy_f1)\n        type_oracle_f1s[dominant_type].append(oracle_f1)\n\n# Known degeneracy values\ndegen = {\n    'event': 12.71, 'other': 11.13, 'organization': 10.89, \n    'building': 12.35, 'product': 14.32, 'location': 14.08, \n    'person': 15.28, 'art': 25.84\n}\n\n# Compute and print table\nprint(\"\\n=== Option C: Constant F1 Degen vs Oracle Headroom ===\\n\")\nprint(f\"{'Type':<15} | {'Degen% (CF1)':>12} | {'Greedy F1':>10} | {'Oracle F1':>10} | {'Headroom (pp)':>13} | {'n':>6}\")\nprint(\"-\" * 80)\n\nheadroom_dict = {}\nfor t in sorted(degen.keys()):\n    if t in type_greedy_f1s:\n        mean_greedy = np.mean(type_greedy_f1s[t])\n        mean_oracle = np.mean(type_oracle_f1s[t])\n        headroom = (mean_oracle - mean_greedy) * 100\n        n = len(type_greedy_f1s[t])\n        headroom_dict[t] = headroom\n        print(f\"{t:<15} | {degen[t]:>11.2f}% | {mean_greedy:>10.4f} | {mean_oracle:>10.4f} | {headroom:>12.2f}pp | {n:>6}\")\n    else:\n        print(f\"{t:<15} | {degen[t]:>11.2f}% | {'N/A':>10} | {'N/A':>10} | {'N/A':>13} | {'N/A':>6}\")\n\n# Spearman correlation\ntypes_ordered = sorted([t for t in degen.keys() if t in headroom_dict])\nx = [degen[t] for t in types_ordered]\ny = [headroom_dict[t] for t in types_ordered]\n\nrho, p = spearmanr(x, y)\nprint(f\"\\nSpearman rho(Constant_F1_degen, oracle_headroom) = {rho:.3f}, p = {p:.4f}, n={len(types_ordered)}\")\nprint(f\"{'Significant (p < 0.05): Option C works' if p < 0.05 else 'Not significant (p >= 0.05)'}\")\n\n# Also print raw vectors for verification\nprint(f\"\\nDegen values:    {x}\")\nprint(f\"Headroom values: {[f'{v:.2f}' for v in y]}\")\nPYEOF",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && python << 'PYEOF'\nimport json, numpy as np\nfrom collections import Counter, defaultdict\nfrom scipy.stats import spearmanr\n\ndef entities_to_set(entities):\n    \"\"\"Convert entity list to set of (text, type, start, end) tuples for exact match.\"\"\"\n    return set((e['text'], e['type'], e['start'], e['end']) for e in entities)\n\ndef compute_f1(pred_entities, gold_entities):\n    \"\"\"Compute entity-level F1 between pred and gold.\"\"\"\n    pred_set = entities_to_set(pred_entities)\n    gold_set = entities_to_set(gold_entities)\n    if not pred_set and not gold_set:\n        return 1.0\n    if not pred_set or not gold_set:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    precision = tp / len(pred_set) if pred_set else 0.0\n    recall = tp / len(gold_set) if gold_set else 0.0\n    if precision + recall == 0:\n        return 0.0\n    return 2 * precision * recall / (precision + recall)\n\n# Load data\ndata = []\nwith open('/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl') as f:\n    for line in f:\n        data.append(json.loads(line))\n\nprint(f\"Total instances: {len(data)}\")\n\n# Per-type oracle headroom\ntype_greedy_f1s = defaultdict(list)\ntype_oracle_f1s = defaultdict(list)\n\nfor inst in data:\n    gold_entities = inst['gold']['entities']\n    if not gold_entities:  # gold-filtered: skip instances with no gold entities\n        continue\n    \n    # Determine dominant entity type\n    types = [e['type'] for e in gold_entities]\n    dominant_type = Counter(types).most_common(1)[0][0]\n    \n    # Greedy F1\n    greedy_entities = inst['greedy']['entities']\n    greedy_f1 = compute_f1(greedy_entities, gold_entities)\n    \n    # Oracle F1 = max F1 across all samples\n    sample_f1s = []\n    for s in inst['samples']:\n        sf1 = compute_f1(s['entities'], gold_entities)\n        sample_f1s.append(sf1)\n    \n    if sample_f1s:\n        oracle_f1 = max(sample_f1s)\n        type_greedy_f1s[dominant_type].append(greedy_f1)\n        type_oracle_f1s[dominant_type].append(oracle_f1)\n\n# Known degeneracy values\ndegen = {\n    'event': 12.71, 'other': 11.13, 'organization': 10.89, \n    'building': 12.35, 'product': 14.32, 'location': 14.08, \n    'person': 15.28, 'art': 25.84\n}\n\n# Compute and print table\nprint(\"\\n=== Option C: Constant F1 Degen vs Oracle Headroom ===\\n\")\nprint(f\"{'Type':<15} | {'Degen% (CF1)':>12} | {'Greedy F1':>10} | {'Oracle F1':>10} | {'Headroom (pp)':>13} | {'n':>6}\")\nprint(\"-\" * 80)\n\nheadroom_dict = {}\nfor t in sorted(degen.keys()):\n    if t in type_greedy_f1s:\n        mean_greedy = np.mean(type_greedy_f1s[t])\n        mean_oracle = np.mean(type_oracle_f1s[t])\n        headroom = (mean_oracle - mean_greedy) * 100\n        n = len(type_greedy_f1s[t])\n        headroom_dict[t] = headroom\n        print(f\"{t:<15} | {degen[t]:>11.2f}% | {mean_greedy:>10.4f} | {mean_oracle:>10.4f} | {headroom:>12.2f}pp | {n:>6}\")\n    else:\n        print(f\"{t:<15} | {degen[t]:>11.2f}% | {'N/A':>10} | {'N/A':>10} | {'N/A':>13} | {'N/A':>6}\")\n\n# Spearman correlation\ntypes_ordered = sorted([t for t in degen.keys() if t in headroom_dict])\nx = [degen[t] for t in types_ordered]\ny = [headroom_dict[t] for t in types_ordered]\n\nrho, p = spearmanr(x, y)\nprint(f\"\\nSpearman rho(Constant_F1_degen, oracle_headroom) = {rho:.3f}, p = {p:.4f}, n={len(types_ordered)}\")\nprint(f\"{'Significant (p < 0.05): Option C works' if p < 0.05 else 'Not significant (p >= 0.05)'}\")\n\n# Also print raw vectors for verification\nprint(f\"\\nDegen values:    {x}\")\nprint(f\"Headroom values: {[f'{v:.2f}' for v in y]}\")\nPYEOF",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T08:53:53.633146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total instances: 37648\\n\\n=== Option C: Constant F1 Degen vs Oracle Headroom ===\\n\\nType            | Degen% (CF1) |  Greedy F1 |  Oracle F1 | Headroom (pp) |      n\\n--------------------------------------------------------------------------------\\nart             |       25.84% |     0.7557 |     0.8477 |         9.21pp |   1277\\nbuilding        |       12.35% |     0.7024 |     0.8514 |        14.90pp |   1587\\nevent           |       12.71% |     0.6548 |     0.8162 |        16.14pp |   1306\\nlocation        |       14.08% |     0.7924 |     0.8951 |        10.27pp |   8023\\norganization    |       10.89% |     0.7202 |     0.8535 |        13.33pp |   6647\\nother           |       11.13% |     0.6373 |     0.8312 |        19.39pp |   3433\\nperson          |       15.28% |     0.8220 |     0.9141 |         9.21pp |   8016\\nproduct         |       14.32% |     0.6563 |     0.8140 |        15.78pp |   2276\\n\\nSpearman rho(Constant_F1_degen, oracle_headroom) = -0.619, p = 0.1017, n=8\\nNot significant (p >= 0.05)\\n\\nDegen values:    [25.84, 12.35, 12.71, 14.08, 10.89, 11.13, 15.28, 14.32]\\nHeadroom values: ['9.21', '14.90', '16.14', '10.27', '13.33', '19.39', '9.21', '15.78']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 19.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T08:53:53.633335+00:00_

结果：

```
=== Option C: Constant F1 Degen vs Oracle Headroom ===

Type            | Degen% (CF1) |  Greedy F1 |  Oracle F1 | Headroom (pp) |      n
--------------------------------------------------------------------------------
art             |       25.84% |     0.7557 |     0.8477 |         9.21pp |   1277
building        |       12.35% |     0.7024 |     0.8514 |        14.90pp |   1587
event           |       12.71% |     0.6548 |     0.8162 |        16.14pp |   1306
location        |       14.08% |     0.7924 |     0.8951 |        10.27pp |   8023
organization    |       10.89% |     0.7202 |     0.8535 |        13.33pp |   6647
other           |       11.13% |     0.6373 |     0.8312 |        19.39pp |   3433
person          |       15.28% |     0.8220 |     0.9141 |         9.21pp |   8016
product         |       14.32% |     0.6563 |     0.8140 |        15.78pp |   2276

Spearman ρ(Constant_F1_degen, oracle_headroom) = -0.619, p = 0.1017, n=8
Not significant (p >= 0.05)
```

**结论：** Spearman ρ = **-0.619**，p = 0.1017，n=8 下不显著。

方向是负相关：degeneracy 越高的 type（如 art 25.84%），oracle headroom 反而越小（9.21pp）。这与预期相反——高 degeneracy 本应意味着更多"有用的多样性"从而带来更大 oracle headroom，但实际上高 degeneracy 的 type（art）greedy 本身就较强（0.756），oracle 提升空间有限；而低 degeneracy 的 type（other 11.13%）greedy 很弱（0.637），oracle headroom 反而最大（19.39pp）。

Option C 在 n=8 的粒度下未通过显著性检验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_option_c_degen_vs_headroom_20260517T085228"
}
```

</details>

---
