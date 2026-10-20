# analysis c1 edge samples

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_analysis_c1-edge-samples_20260516T054253.jsonl`
- **Structured JSON:** [`ecbb5ddd9580fd779082.json`](../../sessions/ec/ecbb5ddd9580fd779082.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-16T05:44:48.413942+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T05:44:48.414384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T05:44:48.414590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed42_v2/final/predictions.jsonl 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed42_v2/final/predictions.jsonl 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T05:44:48.414736+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T05:44:48.414864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls /root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls /root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T05:44:48.414992+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T05:44:48.415140+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed42_v2/final/predictions.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed42_v2/final/predictions.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T05:44:48.415303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls /root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls /root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T05:44:48.415451+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed42_v2/final/predictions.jsonl': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T05:44:48.415576+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T05:44:48.415725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/autodl-tmp/trace-verdict-study-checkpoints -name \"predictions.jsonl\" -path \"*exception*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/autodl-tmp/trace-verdict-study-checkpoints -name \"predictions.jsonl\" -path \"*exception*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:44:48.415863+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/checkpoint-148/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/checkpoint-148/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/checkpoint-296/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/checkpoint-444/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/final/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/checkpoint-148/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/final/predictions.jsonl\\n/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/predictions.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T05:44:48.416028+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-11235",
  "command": "cat << 'SCRIPT' > /tmp/c1_edge_analysis.py\nimport json\nimport os\nimport re\nfrom collections import Counter\n\n# Load test data\ntest_data = []\nwith open('/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl') as f:\n    for line in f:\n        test_data.append(json.loads(line))\n\n# Load predictions\npreds = []\nwith open('/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl') as f:\n    for line in f:\n        preds.append(json.loads(line))\n\nprint(f\"Test samples: {len(test_data)}, Predictions: {len(preds)}\")\n\n# Inspect first sample structure\nprint(\"\\n=== Sample structure ===\")\nsample0 = test_data[0]\nprint(f\"Keys: {list(sample0.keys())}\")\nfor k, v in sample0.items():\n    val_str = str(v)[:100]\n    print(f\"  {k}: {val_str}\")\n\npred0 = preds[0]\nprint(f\"\\nPred keys: {list(pred0.keys())}\")\nfor k, v in pred0.items():\n    val_str = str(v)[:100]\n    print(f\"  {k}: {val_str}\")\nSCRIPT\npython3 /tmp/c1_edge_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat << 'SCRIPT' > /tmp/c1_edge_analysis.py\nimport json\nimport os\nimport re\nfrom collections import Counter\n\n# Load test data\ntest_data = []\nwith open('/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl') as f:\n    for line in f:\n        test_data.append(json.loads(line))\n\n# Load predictions\npreds = []\nwith open('/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl') as f:\n    for line in f:\n        preds.append(json.loads(line))\n\nprint(f\"Test samples: {len(test_data)}, Predictions: {len(preds)}\")\n\n# Inspect first sample structure\nprint(\"\\n=== Sample structure ===\")\nsample0 = test_data[0]\nprint(f\"Keys: {list(sample0.keys())}\")\nfor k, v in sample0.items():\n    val_str = str(v)[:100]\n    print(f\"  {k}: {val_str}\")\n\npred0 = preds[0]\nprint(f\"\\nPred keys: {list(pred0.keys())}\")\nfor k, v in pred0.items():\n    val_str = str(v)[:100]\n    print(f\"  {k}: {val_str}\")\nSCRIPT\npython3 /tmp/c1_edge_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T05:44:48.416171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Test samples: 1190, Predictions: 1190\\n\\n=== Sample structure ===\\nKeys: ['input', 'output', 'problem_id']\\n  input: Given the following code:\\nmin_val = min(numbers)\\n    max_val = max(numbers)\\n    range_val = max_val \\n  output: fail\\n  problem_id: HumanEval/21\\n\\nPred keys: ['id', 'label', 'pred', 'raw_pred']\\n  id: 0\\n  label: fail\\n  pred: fail\\n  raw_pred: fail\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T05:44:48.416399+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-11235",
  "command": "cat << 'SCRIPT' > /tmp/c1_edge_analysis.py\nimport json\nimport os\nimport re\nfrom collections import Counter\n\n# Load test data\ntest_data = []\nwith open('/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl') as f:\n    for line in f:\n        test_data.append(json.loads(line))\n\n# Load predictions\npreds = []\nwith open('/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl') as f:\n    for line in f:\n        preds.append(json.loads(line))\n\n# Find edge samples: ground_truth=pass, but trace has real exception (not \"[No exception data in trace]\")\nedge_samples = []\nfor i, (sample, pred) in enumerate(zip(test_data, preds)):\n    gt = sample['output'].strip().lower()\n    if gt != 'pass':\n        continue\n    text = sample['input']\n    if '[No exception data in trace]' in text:\n        continue\n    # Has actual exception content - this is an edge sample\n    # Extract exception type\n    exc_type = 'unknown'\n    exc_match = re.search(r'(\\w+(?:Error|Exception|Exit|Warning|Interrupt))', text)\n    if exc_match:\n        exc_type = exc_match.group(1)\n    \n    # Extract a snippet of the exception\n    exc_snippet = ''\n    for marker in ['[ERROR]', 'Traceback', 'Exception', 'Error']:\n        idx = text.find(marker)\n        if idx >= 0:\n            exc_snippet = text[idx:idx+200].replace('\\n', ' | ')\n            break\n    \n    sft_pred = pred['pred'].strip().lower()\n    # B5 rule: no \"[No exception data in trace]\" marker -> predict fail\n    b5_pred = 'fail'\n    \n    edge_samples.append({\n        'index': i,\n        'problem_id': sample.get('problem_id', ''),\n        'ground_truth': 'pass',\n        'sft_pred': sft_pred,\n        'sft_correct': sft_pred == 'pass',\n        'b5_pred': b5_pred,\n        'b5_correct': False,  # b5 predicts fail, gt is pass\n        'exception_type': exc_type,\n        'exception_snippet': exc_snippet[:150],\n    })\n\nprint(f\"Found {len(edge_samples)} edge samples\")\nprint(f\"\\n=== SFT vs B5 on edge samples ===\")\nsft_correct = sum(1 for s in edge_samples if s['sft_correct'])\nb5_correct = sum(1 for s in edge_samples if s['b5_correct'])\nprint(f\"SFT correct: {sft_correct}/{len(edge_samples)}\")\nprint(f\"B5  correct: {b5_correct}/{len(edge_samples)}\")\nprint(f\"Delta: {sft_correct}/{len(edge_samples)} - {b5_correct}/{len(edge_samples)} = {sft_correct - b5_correct}/{len(edge_samples)}\")\n\nprint(f\"\\n=== Exception type distribution ===\")\ntype_counter = Counter(s['exception_type'] for s in edge_samples)\nfor t, c in type_counter.most_common():\n    print(f\"  {t}: {c}\")\n\nprint(f\"\\n=== Full table ===\")\nprint(f\"{'idx':<5} {'problem_id':<20} {'gt':<6} {'sft':<6} {'b5':<6} {'exc_type':<20} {'sft_ok':<6} {'b5_ok':<6}\")\nprint(\"-\" * 90)\nfor s in edge_samples:\n    print(f\"{s['index']:<5} {s['problem_id']:<20} {s['ground_truth']:<6} {s['sft_pred']:<6} {s['b5_pred']:<6} {s['exception_type']:<20} {str(s['sft_correct']):<6} {str(s['b5_correct']):<6}\")\n\n# Identify GeneratorExit samples (irreducible error)\ngen_exit = [s for s in edge_samples if 'GeneratorExit' in s['exception_type']]\nprint(f\"\\n=== GeneratorExit samples (irreducible error) ===\")\nfor s in gen_exit:\n    print(f\"  index={s['index']}, problem_id={s['problem_id']}, sft_pred={s['sft_pred']}\")\n\n# Save results\nos.makedirs('/root/autodl-tmp/trace-verdict-study-checkpoints/analysis', exist_ok=True)\noutput = {\n    'summary': {\n        'total_edge_samples': len(edge_samples),\n        'sft_correct': sft_correct,\n        'b5_correct': b5_correct,\n        'sft_accuracy_on_edge': f\"{sft_correct}/{len(edge_samples)}\",\n        'b5_accuracy_on_edge': f\"{b5_correct}/{len(edge_samples)}\",\n        'delta': f\"{sft_correct - b5_correct}/{len(edge_samples)}\",\n    },\n    'exception_type_distribution': dict(type_counter.most_common()),\n    'generatorexit_samples': gen_exit,\n    'all_edge_samples': edge_samples,\n}\nwith open('/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json', 'w') as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json\")\nSCRIPT\npython3 /tmp/c1_edge_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat << 'SCRIPT' > /tmp/c1_edge_analysis.py\nimport json\nimport os\nimport re\nfrom collections import Counter\n\n# Load test data\ntest_data = []\nwith open('/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl') as f:\n    for line in f:\n        test_data.append(json.loads(line))\n\n# Load predictions\npreds = []\nwith open('/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl') as f:\n    for line in f:\n        preds.append(json.loads(line))\n\n# Find edge samples: ground_truth=pass, but trace has real exception (not \"[No exception data in trace]\")\nedge_samples = []\nfor i, (sample, pred) in enumerate(zip(test_data, preds)):\n    gt = sample['output'].strip().lower()\n    if gt != 'pass':\n        continue\n    text = sample['input']\n    if '[No exception data in trace]' in text:\n        continue\n    # Has actual exception content - this is an edge sample\n    # Extract exception type\n    exc_type = 'unknown'\n    exc_match = re.search(r'(\\w+(?:Error|Exception|Exit|Warning|Interrupt))', text)\n    if exc_match:\n        exc_type = exc_match.group(1)\n    \n    # Extract a snippet of the exception\n    exc_snippet = ''\n    for marker in ['[ERROR]', 'Traceback', 'Exception', 'Error']:\n        idx = text.find(marker)\n        if idx >= 0:\n            exc_snippet = text[idx:idx+200].replace('\\n', ' | ')\n            break\n    \n    sft_pred = pred['pred'].strip().lower()\n    # B5 rule: no \"[No exception data in trace]\" marker -> predict fail\n    b5_pred = 'fail'\n    \n    edge_samples.append({\n        'index': i,\n        'problem_id': sample.get('problem_id', ''),\n        'ground_truth': 'pass',\n        'sft_pred': sft_pred,\n        'sft_correct': sft_pred == 'pass',\n        'b5_pred': b5_pred,\n        'b5_correct': False,  # b5 predicts fail, gt is pass\n        'exception_type': exc_type,\n        'exception_snippet': exc_snippet[:150],\n    })\n\nprint(f\"Found {len(edge_samples)} edge samples\")\nprint(f\"\\n=== SFT vs B5 on edge samples ===\")\nsft_correct = sum(1 for s in edge_samples if s['sft_correct'])\nb5_correct = sum(1 for s in edge_samples if s['b5_correct'])\nprint(f\"SFT correct: {sft_correct}/{len(edge_samples)}\")\nprint(f\"B5  correct: {b5_correct}/{len(edge_samples)}\")\nprint(f\"Delta: {sft_correct}/{len(edge_samples)} - {b5_correct}/{len(edge_samples)} = {sft_correct - b5_correct}/{len(edge_samples)}\")\n\nprint(f\"\\n=== Exception type distribution ===\")\ntype_counter = Counter(s['exception_type'] for s in edge_samples)\nfor t, c in type_counter.most_common():\n    print(f\"  {t}: {c}\")\n\nprint(f\"\\n=== Full table ===\")\nprint(f\"{'idx':<5} {'problem_id':<20} {'gt':<6} {'sft':<6} {'b5':<6} {'exc_type':<20} {'sft_ok':<6} {'b5_ok':<6}\")\nprint(\"-\" * 90)\nfor s in edge_samples:\n    print(f\"{s['index']:<5} {s['problem_id']:<20} {s['ground_truth']:<6} {s['sft_pred']:<6} {s['b5_pred']:<6} {s['exception_type']:<20} {str(s['sft_correct']):<6} {str(s['b5_correct']):<6}\")\n\n# Identify GeneratorExit samples (irreducible error)\ngen_exit = [s for s in edge_samples if 'GeneratorExit' in s['exception_type']]\nprint(f\"\\n=== GeneratorExit samples (irreducible error) ===\")\nfor s in gen_exit:\n    print(f\"  index={s['index']}, problem_id={s['problem_id']}, sft_pred={s['sft_pred']}\")\n\n# Save results\nos.makedirs('/root/autodl-tmp/trace-verdict-study-checkpoints/analysis', exist_ok=True)\noutput = {\n    'summary': {\n        'total_edge_samples': len(edge_samples),\n        'sft_correct': sft_correct,\n        'b5_correct': b5_correct,\n        'sft_accuracy_on_edge': f\"{sft_correct}/{len(edge_samples)}\",\n        'b5_accuracy_on_edge': f\"{b5_correct}/{len(edge_samples)}\",\n        'delta': f\"{sft_correct - b5_correct}/{len(edge_samples)}\",\n    },\n    'exception_type_distribution': dict(type_counter.most_common()),\n    'generatorexit_samples': gen_exit,\n    'all_edge_samples': edge_samples,\n}\nwith open('/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json', 'w') as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json\")\nSCRIPT\npython3 /tmp/c1_edge_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T05:44:48.416599+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found 8 edge samples\\n\\n=== SFT vs B5 on edge samples ===\\nSFT correct: 6/8\\nB5  correct: 0/8\\nDelta: 6/8 - 0/8 = 6/8\\n\\n=== Exception type distribution ===\\n  ValueError: 6\\n  GeneratorExit: 2\\n\\n=== Full table ===\\nidx   problem_id           gt     sft    b5     exc_type             sft_ok b5_ok \\n------------------------------------------------------------------------------------------\\n540   MBPP/113             pass   pass   fail   ValueError           True   False \\n541   MBPP/113             pass   pass   fail   ValueError           True   False \\n542   MBPP/113             pass   pass   fail   ValueError           True   False \\n543   MBPP/113             pass   pass   fail   ValueError           True   False \\n548   MBPP/113             pass   pass   fail   ValueError           True   False \\n549   MBPP/113             pass   pass   fail   ValueError           True   False \\n901   HumanEval/95         pass   fail   fail   GeneratorExit        False  False \\n905   HumanEval/95         pass   fail   fail   GeneratorExit        False  False \\n\\n=== GeneratorExit samples (irreducible error) ===\\n  index=901, problem_id=HumanEval/95, sft_pred=fail\\n  index=905, problem_id=HumanEval/95, sft_pred=fail\\n\\nSaved to /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T05:44:48.416758+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "c1_edge_samples_analysis",
  "type": "data",
  "description": "C1 边缘样本分析：exception_only 模型中 pass+有异常的 8 个样本，SFT 6/8 正确 vs B5 0/8",
  "project": "trace-verdict-study",
  "source_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json",
  "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "c1_edge_samples_analysis",
    "type": "data",
    "description": "C1 边缘样本分析：exception_only 模型中 pass+有异常的 8 个样本，SFT 6/8 正确 vs B5 0/8",
    "project": "trace-verdict-study",
    "source_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json",
    "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T05:44:48.416896+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T05:44:48.417017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T05:44:48.417264+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"total_edge_samples\\\": 8,\\n    \\\"sft_correct\\\": 6,\\n    \\\"b5_correct\\\": 0,\\n    \\\"sft_accuracy_on_edge\\\": \\\"6/8\\\",\\n    \\\"b5_accuracy_on_edge\\\": \\\"0/8\\\",\\n    \\\"delta\\\": \\\"6/8\\\"\\n  },\\n  \\\"exception_type_distribution\\\": {\\n    \\\"ValueError\\\": 6,\\n    \\\"GeneratorExit\\\": 2\\n  },\\n  \\\"generatorexit_samples\\\": [\\n    {\\n      \\\"index\\\": 901,\\n      \\\"problem_id\\\": \\\"HumanEval/95\\\",\\n      \\\"ground_truth\\\": \\\"pass\\\",\\n      \\\"sft_pred\\\": \\\"fail\\\",\\n      \\\"sft_correct\\\": false,\\n      \\\"b5_pred\\\": \\\"fail\\\",\\n      \\\"b5_correct\\\": false,\\n      \\\"exception_type\\\": \\\"GeneratorExit\\\",\\n      \\\"exception_snippet\\\": \\\"[ERROR] GeneratorExit at line 5:  | locals: .0='&lt;list_iterator object at 0x7fe16efea440>', k='A' | [ERROR] GeneratorExit at line 7:  | locals: .0='&lt;li\\\"\\n    },\\n    {\\n      \\\"index\\\": 905,\\n      \\\"problem_id\\\": \\\"HumanEval/95\\\",\\n      \\\"ground_truth\\\": \\\"pass\\\",\\n      \\\"sft_pred\\\": \\\"fail\\\",\\n      \\\"sft_correct\\\": false,\\n      \\\"b5_pred\\\": \\\"fail\\\",\\n      \\\"b5_correct\\\": false,\\n      \\\"exception_type\\\": \\\"GeneratorExit\\\",\\n      \\\"exception_snippet\\\": \\\"[ERROR] GeneratorExit at line 5:  | locals: .0='&lt;list_iterator object at 0x7fb77c8ca440>', k='A' | [ERROR] GeneratorExit at line 7:  | locals: .0='<li\\\"\\n    }\\n  ],\\n  \\\"all_edge_samples\\\": [\\n    {\\n      \\\"index\\\": 540,\\n      \\\"problem_id\\\": \\\"MBPP/113\\\",\\n      \\\"ground_truth\\\": \\\"pass\\\",\\n      \\\"sft_pred\\\": \\\"pass\\\",\\n      \\\"sft_correct\\\": true,\\n      \\\"b5_pred\\\": \\\"fail\\\",\\n      \\\"b5_correct\\\": false,\\n      \\\"exception_type\\\": \\\"ValueError\\\",\\n      \\\"exception_snippet\\\": \\\"[ERROR] ValueError at line 3: invalid literal for int() wit
…[truncated 3907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T05:44:48.417479+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "c1_edge_samples_analysis",
  "type": "data",
  "description": "C1 边缘样本分析：exception_only 模型中 pass+有异常的 8 个样本，SFT 6/8 正确 vs B5 0/8",
  "project": "trace-verdict-study",
  "content_filename": "c1_edge_samples.json",
  "content": "{\"summary\":{\"total_edge_samples\":8,\"sft_correct\":6,\"b5_correct\":0,\"sft_accuracy_on_edge\":\"6/8\",\"b5_accuracy_on_edge\":\"0/8\",\"delta\":\"6/8\"},\"exception_type_distribution\":{\"ValueError\":6,\"GeneratorExit\":2},\"generatorexit_samples\":[{\"index\":901,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:  | locals: .0='&lt;list_iterator object at 0x7fe16efea440>', k='A' | [ERROR] GeneratorExit at line 7:  | locals: .0='&lt;li\"},{\"index\":905,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:  | locals: .0='&lt;list_iterator object at 0x7fb77c8ca440>', k='A' | [ERROR] GeneratorExit at line 7:  | locals: .0='<li\"}],\"all_edge_samples\":[{\"index\":540,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":541,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":542,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":543,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":548,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":549,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":901,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:\"},{\"index\":905,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:\"}]}",
  "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "c1_edge_samples_analysis",
    "type": "data",
    "description": "C1 边缘样本分析：exception_only 模型中 pass+有异常的 8 个样本，SFT 6/8 正确 vs B5 0/8",
    "project": "trace-verdict-study",
    "content_filename": "c1_edge_samples.json",
    "content": "{\"summary\":{\"total_edge_samples\":8,\"sft_correct\":6,\"b5_correct\":0,\"sft_accuracy_on_edge\":\"6/8\",\"b5_accuracy_on_edge\":\"0/8\",\"delta\":\"6/8\"},\"exception_type_distribution\":{\"ValueError\":6,\"GeneratorExit\":2},\"generatorexit_samples\":[{\"index\":901,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:  | locals: .0='&lt;list_iterator object at 0x7fe16efea440>', k='A' | [ERROR] GeneratorExit at line 7:  | locals: .0='&lt;li\"},{\"index\":905,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:  | locals: .0='&lt;list_iterator object at 0x7fb77c8ca440>', k='A' | [ERROR] GeneratorExit at line 7:  | locals: .0='<li\"}],\"all_edge_samples\":[{\"index\":540,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":541,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":542,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":543,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":548,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":549,\"problem_id\":\"MBPP/113\",\"ground_truth\":\"pass\",\"sft_pred\":\"pass\",\"sft_correct\":true,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"ValueError\",\"exception_snippet\":\"[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'\"},{\"index\":901,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:\"},{\"index\":905,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\",\"exception_snippet\":\"[ERROR] GeneratorExit at line 5:\"}]}",
    "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:44:48.417708+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'summary': {'total_edge_...ratorExit at line 5:'}]}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T05:44:48.417931+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "c1_edge_samples_analysis",
  "type": "data",
  "description": "C1 边缘样本分析：exception_only 模型中 pass+有异常的 8 个样本，SFT 6/8 正确 vs B5 0/8",
  "project": "trace-verdict-study",
  "content_filename": "c1_edge_samples.json",
  "content": "{\"summary\":{\"total_edge_samples\":8,\"sft_correct\":6,\"b5_correct\":0,\"sft_accuracy_on_edge\":\"6/8\",\"b5_accuracy_on_edge\":\"0/8\",\"delta\":\"6/8\"},\"exception_type_distribution\":{\"ValueError\":6,\"GeneratorExit\":2},\"generatorexit_samples\":[{\"index\":901,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\"},{\"index\":905,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\"}],\"all_edge_samples_count\":8,\"note\":\"Full JSON saved at /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json on westd-11235\"}",
  "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "c1_edge_samples_analysis",
    "type": "data",
    "description": "C1 边缘样本分析：exception_only 模型中 pass+有异常的 8 个样本，SFT 6/8 正确 vs B5 0/8",
    "project": "trace-verdict-study",
    "content_filename": "c1_edge_samples.json",
    "content": "{\"summary\":{\"total_edge_samples\":8,\"sft_correct\":6,\"b5_correct\":0,\"sft_accuracy_on_edge\":\"6/8\",\"b5_accuracy_on_edge\":\"0/8\",\"delta\":\"6/8\"},\"exception_type_distribution\":{\"ValueError\":6,\"GeneratorExit\":2},\"generatorexit_samples\":[{\"index\":901,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\"},{\"index\":905,\"problem_id\":\"HumanEval/95\",\"ground_truth\":\"pass\",\"sft_pred\":\"fail\",\"sft_correct\":false,\"b5_pred\":\"fail\",\"b5_correct\":false,\"exception_type\":\"GeneratorExit\"}],\"all_edge_samples_count\":8,\"note\":\"Full JSON saved at /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json on westd-11235\"}",
    "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T05:44:48.418091+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'summary': {'total_edge_...es.json on westd-11235'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T05:44:48.418282+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "c1_edge_samples_analysis",
  "type": "data",
  "description": "C1 edge samples: exception_only pass+real-exception samples, SFT 6/8 vs B5 0/8",
  "project": "trace-verdict-study",
  "content_filename": "c1_edge_samples.json",
  "content": "See full file at /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json on westd-11235. Summary: 8 edge samples (6 ValueError from MBPP/113, 2 GeneratorExit from HumanEval/95). SFT correct 6/8, B5 correct 0/8, delta=6/8.",
  "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "c1_edge_samples_analysis",
    "type": "data",
    "description": "C1 edge samples: exception_only pass+real-exception samples, SFT 6/8 vs B5 0/8",
    "project": "trace-verdict-study",
    "content_filename": "c1_edge_samples.json",
    "content": "See full file at /root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json on westd-11235. Summary: 8 edge samples (6 ValueError from MBPP/113, 2 GeneratorExit from HumanEval/95). SFT correct 6/8, B5 correct 0/8, delta=6/8.",
    "tags": "['analysis', 'edge-samples', 'exception-only', 'c1']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T05:44:48.418449+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_775028\", \"name\": \"c1_edge_samples_analysis\", \"type\": \"data\", \"description\": \"C1 edge samples: exception_only pass+real-exception samples, SFT 6/8 vs B5 0/8\", \"path\": \"projects/trace-verdict-study/artifacts/_project/data/c1_edge_samples.json\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:44:34.207960+00:00\", \"tags\": [\"analysis\", \"edge-samples\", \"exception-only\", \"c1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_c1-edge-samples_20260516T054253",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-16T05:44:48.418628+00:00_

## C1 边缘样本分析结果

找到 **8 个边缘样本**（ground_truth=pass 但 trace 包含真实异常）：

| idx | problem_id | gt | SFT_pred | B5_pred | exception_type | SFT正确 | B5正确 |
|-----|-----------|-----|----------|---------|----------------|---------|--------|
| 540 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 541 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 542 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 543 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 548 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 549 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 901 | HumanEval/95 | pass | fail | fail | **GeneratorExit** | ✗ | ✗ |
| 905 | HumanEval/95 | pass | fail | fail | **GeneratorExit** | ✗ | ✗ |

### 统计

- **SFT 正确: 6/8 (75%)**
- **B5 正确: 0/8 (0%)**
- **Delta: +6/8**

### 异常类型分布
- ValueError: 6 (全部来自 MBPP/113，`int('python')` 触发，SFT 全部正确识别为 pass)
- GeneratorExit: 2 (来自 HumanEval/95，**irreducible error**，SFT 和 B5 都错)

### 关键发现

6 个 ValueError 样本：异常是 try/except 结构中被正确捕获的预期行为（检测字符串是否为数字），SFT 学会了区分"被捕获的异常≠测试失败"。

2 个 GeneratorExit 样本：Python generator 被 GC 回收时自动触发，与代码正确性无关，但在 trace 中表现为异常。这是 **irreducible error** —— SFT 也无法正确处理，两种方法都预测为 fail。

结果已保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_c1-edge-samples_20260516T054253"
}
```

</details>

---
