# analysis supplementary completeness

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_analysis_supplementary-completeness_20260521T075031.jsonl`
- **Structured JSON:** [`2c627a5c5b2c2a832321.json`](../../sessions/2c/2c627a5c5b2c2a832321.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-21T08:02:19.980435+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T08:02:19.980830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T08:02:19.981038+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "filters": "{'conclusion': 'success'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "filters": "{'conclusion': 'success'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T08:02:19.981181+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T08:02:19.982253+00:00_

Error: result (230,118 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T08:02:19.982468+00:00_

docs/paper/main.tex
docs/paper/appendix.tex
docs/paper/checklist.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Glob",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T08:02:19.982637+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\nprint(f'Total experiments: {len(exps)}')\nprint(f'Type: {type(exps)}')\nif len(exps) > 0:\n    print(f'Keys: {list(exps[0].keys()) if isinstance(exps[0], dict) else \\\"not dict\\\"}')\n    # Show first experiment\n    print(json.dumps(exps[0], indent=2)[:2000])\n\"\n",
  "description": "Parse registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\nprint(f'Total experiments: {len(exps)}')\nprint(f'Type: {type(exps)}')\nif len(exps) > 0:\n    print(f'Keys: {list(exps[0].keys()) if isinstance(exps[0], dict) else \\\"not dict\\\"}')\n    # Show first experiment\n    print(json.dumps(exps[0], indent=2)[:2000])\n\"\n",
    "description": "Parse registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T08:02:19.982774+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    print(f'Keys: {list(exps[0].keys()) if isinstance(exps[0], dict) else "not dict"}')
                                                      ~~~~^^^
KeyError: 0
Total experiments: 4
Type: &lt;class 'dict'>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T08:02:19.982943+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\n\n# Extract summary: exp_id, metrics, hypothesis, tags\nsummary = []\nfor e in exps:\n    exp_id = e.get('exp_id', 'N/A')\n    metrics = e.get('metrics', {})\n    hypothesis = e.get('hypothesis', '')\n    tags = e.get('tags', [])\n    conclusion = e.get('conclusion', '')\n    status = e.get('status', '')\n    notes = e.get('notes', '')\n    summary.append({\n        'exp_id': exp_id,\n        'metrics': metrics,\n        'hypothesis': hypothesis[:200] if hypothesis else '',\n        'tags': tags,\n        'conclusion': conclusion,\n        'notes': notes[:200] if notes else ''\n    })\n\nprint(json.dumps(summary, indent=2))\n\" > /tmp/registry_success_summary.json 2>&1\nwc -l /tmp/registry_success_summary.json\necho \"---\"\nhead -100 /tmp/registry_success_summary.json\n",
  "description": "Extract success experiments summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\n\n# Extract summary: exp_id, metrics, hypothesis, tags\nsummary = []\nfor e in exps:\n    exp_id = e.get('exp_id', 'N/A')\n    metrics = e.get('metrics', {})\n    hypothesis = e.get('hypothesis', '')\n    tags = e.get('tags', [])\n    conclusion = e.get('conclusion', '')\n    status = e.get('status', '')\n    notes = e.get('notes', '')\n    summary.append({\n        'exp_id': exp_id,\n        'metrics': metrics,\n        'hypothesis': hypothesis[:200] if hypothesis else '',\n        'tags': tags,\n        'conclusion': conclusion,\n        'notes': notes[:200] if notes else ''\n    })\n\nprint(json.dumps(summary, indent=2))\n\" > /tmp/registry_success_summary.json 2>&1\nwc -l /tmp/registry_success_summary.json\necho \"---\"\nhead -100 /tmp/registry_success_summary.json\n",
    "description": "Extract success experiments summary"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T08:02:19.983081+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-1/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T08:02:19.983221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nif isinstance(result, dict):\n    print('Top-level keys:', list(result.keys()))\n    for k,v in result.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with {len(v)} keys')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:100]}')\n\"\n",
  "description": "Explore registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nif isinstance(result, dict):\n    print('Top-level keys:', list(result.keys()))\n    for k,v in result.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with {len(v)} keys')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:100]}')\n\"\n",
    "description": "Explore registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T08:02:19.983371+00:00_

Top-level keys: ['success', 'data', 'error', 'metadata']
  success: bool = True
  data: dict with 4 keys
  error: NoneType = None
  metadata: dict with 1 keys

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T08:02:19.983512+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nd = result['data']\nprint('data keys:', list(d.keys()))\nfor k,v in d.items():\n    if isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if len(v) > 0:\n            print(f'    first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n    elif isinstance(v, dict):\n        print(f'  {k}: dict with keys {list(v.keys())[:10]}')\n    else:\n        print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\nprint('metadata:', result.get('metadata'))\n\"\n",
  "description": "Explore registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nd = result['data']\nprint('data keys:', list(d.keys()))\nfor k,v in d.items():\n    if isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if len(v) > 0:\n            print(f'    first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n    elif isinstance(v, dict):\n        print(f'  {k}: dict with keys {list(v.keys())[:10]}')\n    else:\n        print(f'  {k}: {type(v).__name__} = {str(v)[:200]}')\nprint('metadata:', result.get('metadata'))\n\"\n",
    "description": "Explore registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T08:02:19.983655+00:00_

data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: dict with keys ['deepseek-cwm-repo-s123-eval-1epoch', 'deepseek-cwm-repo-s42-seq4096-eval', 'deepseek-cls-repo-s456-eval-v2', 'cls8b-repo-s456-eval-v2', 'qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval', 'cls8b-s42-ckpt-ablation', 'qwen3-8b-traj-repo-s456', 'qwen3-8b-traj-repo-s123', 'exp-downsample-cls-func-v3-eval', 'exp-downsample-cls-func-v3']
  count: int = 132
  total: int = 132
  baseline: NoneType = None
metadata: {'elapsed_seconds': 0.8113}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T08:02:19.983783+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n\n# Extract all experiments with key info\nsummary = []\nfor exp_id, e in exps.items():\n    metrics = e.get('metrics', {})\n    hypothesis = e.get('hypothesis', '')\n    tags = e.get('tags', [])\n    conclusion = e.get('conclusion', '')\n    notes = e.get('notes', '')\n    summary.append({\n        'exp_id': exp_id,\n        'metrics': metrics,\n        'hypothesis': hypothesis[:300] if hypothesis else '',\n        'tags': tags if tags else [],\n        'conclusion': conclusion,\n        'notes': notes[:300] if notes else ''\n    })\n\n# Sort by exp_id\nsummary.sort(key=lambda x: x['exp_id'])\nprint(json.dumps(summary, indent=2, ensure_ascii=False))\n\" > /tmp/registry_success_summary.json 2>&1\nwc -l /tmp/registry_success_summary.json\n",
  "description": "Extract all success experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n\n# Extract all experiments with key info\nsummary = []\nfor exp_id, e in exps.items():\n    metrics = e.get('metrics', {})\n    hypothesis = e.get('hypothesis', '')\n    tags = e.get('tags', [])\n    conclusion = e.get('conclusion', '')\n    notes = e.get('notes', '')\n    summary.append({\n        'exp_id': exp_id,\n        'metrics': metrics,\n        'hypothesis': hypothesis[:300] if hypothesis else '',\n        'tags': tags if tags else [],\n        'conclusion': conclusion,\n        'notes': notes[:300] if notes else ''\n    })\n\n# Sort by exp_id\nsummary.sort(key=lambda x: x['exp_id'])\nprint(json.dumps(summary, indent=2, ensure_ascii=False))\n\" > /tmp/registry_success_summary.json 2>&1\nwc -l /tmp/registry_success_summary.json\n",
    "description": "Extract all success experiments"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T08:02:19.983931+00:00_

2888 /tmp/registry_success_summary.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T08:02:19.984047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -80 /tmp/registry_success_summary.json",
  "description": "Preview registry summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "head -80 /tmp/registry_success_summary.json",
    "description": "Preview registry summary"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T08:02:19.984209+00:00_

Total experiments: 132

[
  {
    "exp_id": "5-paired-clustered-bootstrap",
    "metrics": {
      "pooled_gap_pp": -0.45,
      "pooled_ci_lower": -1.71,
      "pooled_ci_upper": 0.84,
      "pooled_p_value": 0.499,
      "tost_p_value": 0.0071,
      "tost_margin_pp": 2,
      "seed_level_paired_t_p": 0.425,
      "seed_level_mean_gap": -0.48,
      "n_variants_pooled": 523,
      "n_clusters": 114,
      "per_seed_gaps": {
        "seed42": -0.97,
        "seed123": 1.45,
        "seed456": -1.84,
        "seed789": -0.78,
        "seed0": -0.29
      }
    },
    "hypothesis": "5-seed paired variant-level clustered bootstrap CI + TOST 等价检验，验证 CLS 和 TRAJ 在 variant 级别是否等价（扩展之前 3-paired 分析）",
    "tags": [],
    "conclusion": "success",
    "notes": "5-paired 扩展了之前 3-paired 分析。核心发现：CLS 和 TRAJ 在 variant 级别统计等价（TOST p=0.0071, margin ±2pp），无显著差异（gap=-0.45pp, p=0.499）。确认 D018：per-test CLS 聚合到 variant 级别后与 TRAJ 表现一致。注意：seed 789/0 使用 4-bit 量化推理（低于 bf16 ~2-3pp），但 paired 比较内部一致。结果保存在 home:/home/sonny/exec-sim-repair-verifier/clustered_bootstrap_5paired."
  },
  {
    "exp_id": "block-corr-empirical",
    "metrics": {
      "icc": 0.1909,
      "icc_p_value": 0,
      "design_effect": 3.9676,
      "overall_error_rate": 0.1249,
      "all_correct_observed": 46,
      "all_correct_expected_iid": 16.35,
      "all_correct_ratio": 2.81,
      "error_std_observed": 0.1531,
      "error_std_expected_iid": 0.0811,
      "error_std_ratio": 1.89,
      "n_samples": 1890,
      "n_problems": 114,
      "inference_precision": "bfloat16",
      "version": "v2_corrected"
    },
    "hypothesis": "训练好的 per-test 分类器的预测误差在同一 problem_id 内是 block-correlated 而非 i.i.d.，验证 oracle 模拟的 block-correlation 假设",
    "tags": [],
    "conclusion": "success",
    "notes": "v2 修正版：用 bfloat16 推理替代 v1 的 4-bit 量化。accuracy 偏差已消除 (87.51% = 主评估)。ICC 从 0.233 降至 0.191（4-bit 量化误差本身也是 block-correlated 的），但结论不变：block-correlation 显著存在 (p<0.0001)，DEFF=3.97。"
  },
  {
    "exp_id": "cls-seed0",
    "metrics": {
     
…[truncated 969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T08:02:19.984399+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract all registry experiments",
  "prompt": "Read the file `/tmp/registry_success_summary.json` which contains 132 success experiments from a registry. Extract a compact table of ALL experiments with:\n- exp_id\n- key metric (accuracy or the most important metric)\n- brief hypothesis/purpose (one line)\n- tags\n\nOutput this as a clean markdown table sorted by exp_id. Write the result to `/tmp/all_success_experiments.md`.\n\nAlso, separately extract a JSON file `/tmp/exp_metrics_lookup.json` that maps exp_id to their key numeric metrics (especially accuracy values, F1, etc.) — we need to match these numbers against what appears in the paper. Format: {\"exp_id\": {\"accuracy\": X, \"other_metric\": Y, ...}, ...}\n\nAlso read the registry for negative/failure experiments. The full registry file is at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt`\nBut that only has conclusion=success. So also check the project's registry.yaml at `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml` for experiments with conclusion \"negative\" or \"failure\". Extract those to `/tmp/negative_experiments.md`.\n",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract all registry experiments",
    "prompt": "Read the file `/tmp/registry_success_summary.json` which contains 132 success experiments from a registry. Extract a compact table of ALL experiments with:\n- exp_id\n- key metric (accuracy or the most important metric)\n- brief hypothesis/purpose (one line)\n- tags\n\nOutput this as a clean markdown table sorted by exp_id. Write the result to `/tmp/all_success_experiments.md`.\n\nAlso, separately extract a JSON file `/tmp/exp_metrics_lookup.json` that maps exp_id to their key numeric metrics (especially accuracy values, F1, etc.) — we need to match these numbers against what appears in the paper. Format: {\"exp_id\": {\"accuracy\": X, \"other_metric\": Y, ...}, ...}\n\nAlso read the registry for negative/failure experiments. The full registry file is at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tool-results/mcp-agent-ml-research-read_registry-1779349847649.txt`\nBut that only has conclusion=success. So also check the project's registry.yaml at `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml` for experiments with conclusion \"negative\" or \"failure\". Extract those to `/tmp/negative_experiments.md`.\n",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T08:02:19.984564+00:00_

Async agent launched successfully.
agentId: ab53d0cbe29ef7ab9 (internal ID - do not mention to user. Use SendMessage with to: 'ab53d0cbe29ef7ab9' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tasks/ab53d0cbe29ef7ab9.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T08:02:19.984731+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Scan paper for referenced data",
  "prompt": "You are auditing an academic paper to find which experimental data/numbers are cited. The paper tex files are in `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`.\n\nRead ALL of these files completely:\n1. `experiments.tex` — contains Table 1, Table 3, and experimental results\n2. `appendix.tex` — contains appendix tables and analysis\n3. `analysis.tex` — analysis section (if exists)\n4. `method.tex` — may contain pilot data\n5. `abstract.tex` — may cite key numbers\n6. `introduction.tex` — may cite key numbers\n\nFor each file, extract:\n1. ALL numeric values that appear to be experimental results (accuracy percentages, F1 scores, p-values, ICC values, etc.)\n2. ALL table data — reproduce each table's content showing the metric values\n3. ANY experiment IDs or run names mentioned\n4. ANY references to specific seeds, checkpoints, or configurations\n\nWrite a comprehensive report to `/tmp/paper_referenced_data.md` with:\n- Section-by-section breakdown of what numbers appear\n- Complete reproduction of all tables with their numeric values\n- List of all unique accuracy/metric values found in the paper\n\nBe thorough — we need to match these against 132 experiments to find which ones are cited and which are missing.\n",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Agent",
  "tool_args": {
    "description": "Scan paper for referenced data",
    "prompt": "You are auditing an academic paper to find which experimental data/numbers are cited. The paper tex files are in `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`.\n\nRead ALL of these files completely:\n1. `experiments.tex` — contains Table 1, Table 3, and experimental results\n2. `appendix.tex` — contains appendix tables and analysis\n3. `analysis.tex` — analysis section (if exists)\n4. `method.tex` — may contain pilot data\n5. `abstract.tex` — may cite key numbers\n6. `introduction.tex` — may cite key numbers\n\nFor each file, extract:\n1. ALL numeric values that appear to be experimental results (accuracy percentages, F1 scores, p-values, ICC values, etc.)\n2. ALL table data — reproduce each table's content showing the metric values\n3. ANY experiment IDs or run names mentioned\n4. ANY references to specific seeds, checkpoints, or configurations\n\nWrite a comprehensive report to `/tmp/paper_referenced_data.md` with:\n- Section-by-section breakdown of what numbers appear\n- Complete reproduction of all tables with their numeric values\n- List of all unique accuracy/metric values found in the paper\n\nBe thorough — we need to match these against 132 experiments to find which ones are cited and which are missing.\n",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T08:02:19.984918+00:00_

Async agent launched successfully.
agentId: a6a7e9e0c43b6d074 (internal ID - do not mention to user. Use SendMessage with to: 'a6a7e9e0c43b6d074' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/214e1416-6a36-4ad4-8f28-4356406d36e3/tasks/a6a7e9e0c43b6d074.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T08:02:19.985108+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T08:02:19.985231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T08:02:19.985375+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'in_progress', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'in_progress', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'pending', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'pending', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'pending', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'in_progress', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'in_progress', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'pending', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'pending', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'pending', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T08:02:19.985525+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T08:02:19.985791+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'in_progress', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'pending', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'pending', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'in_progress', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'pending', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'pending', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T08:02:19.985972+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T08:02:19.986096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/paper_referenced_data.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/paper_referenced_data.md"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T08:02:19.986387+00:00_

1	# Paper Referenced Data: Complete Numeric Audit
2	
3	## 1. abstract.tex
4	
5	### Key Numbers
6	- z = -23.7 (formulation x complexity interaction)
7	- CLS--CWM gap: 19--26pp (repo-level, single-seed variant-level)
8	- TOST: 5 seeds
9	- Two model families: Qwen3, DeepSeek-Coder
10	- <=8B LoRA fine-tuning
11	
12	---
13	
14	## 2. introduction.tex
15	
16	### Key Numbers
17	- z = -23.7, n = 56,480 (interaction test)
18	- Formulation gap at function level: <=1.3pp
19	- Formulation gap at repo level: 19--26pp
20	- Oracle function-level: 90.63% (single-seed)
21	- Oracle repo-level variant: 95.83% (+14.58pp, single-seed)
22	- 0-shot -> fine-tuned gains: 35--36pp at repo level
23	- DeepSeek-Coder CLS--TRAJ gap: 2.69pp
24	- CLS throughput: 217x over CWM (token ratio)
25	- Four targeted interventions all fail (Appendix (g))
26	
27	---
28	
29	## 3. method.tex
30	
31	### Key Numbers
32	- No specific experimental results (theoretical framework only)
33	- ICC rho referenced conceptually
34	- FP bias: 56.5% (CLS, function-level, cited in failure mode discussion)
35	
36	---
37	
38	## 4. experiments.tex
39	
40	### Table 1 (tab:main_results) — Function-Level Per-Test Accuracy on HumanEval+MBPP (n=1,890)
41	
42	| Method | Model | Seeds | Accuracy (%) |
43	|--------|-------|-------|-------------|
44	| **Qwen3 (primary)** | | | |
45	| CLS (fine-tuned) | 4B | 5 | **88.43 +/- 0.78** |
46	| CWM (fine-tuned) | 4B | 5 | 87.19 +/- 0.37 |
47	| TRAJ (fine-tuned) | 4B | 5 | 86.30 +/- 0.97 |
48	| **DeepSeek-Coder (cross-model)** | | | |
49	| CLS (fine-tuned) | 6.7B | 2 | **86.85 +/- 0.11** |
50	| CWM (fine-tuned) | 6.7B | 2 | 86.83 +/- 1.49 |
51	| TRAJ (fine-tuned) | 6.7B | 2 | 84.16 +/- 1.30 |
52	| **Prompting baselines** | | | |
53	| 0-shot | 8B (Qwen3) | 1 | 68.70 |
54	| 0-shot | 6.7B (DeepSeek) | 1 | 63.00 |
55	| ZS LLM-as-judge | 8B (Qwen3) | 1 | 64.40 |
56	| ZS LLM-as-judge | 6.7B (DeepSeek) | 1 | 56.56 |
57	| ZS LLM-as-judge | 32B (NF4) | 1 | 71.69 |
58	| 3-shot ICL | 8B (Qwen3) | 1 | 68.78
…[truncated 26278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T08:02:19.986562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/all_success_experiments.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/all_success_experiments.md"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T08:02:19.986773+00:00_

1	# All Success Experiments (132)
2	
3	| # | exp_id | key_metric | value | hypothesis | tags |
4	|---|--------|-----------|-------|-----------|------|
5	| 1 | 5-paired-clustered-bootstrap | pooled_gap_pp | -0.45 | 5-seed paired variant-level clustered bootstrap CI + TOST 等价检验，验证 CLS 和 TRAJ 在 variant ... | — |
6	| 2 | block-corr-empirical | icc | 0.19 | 训练好的 per-test 分类器的预测误差在同一 problem_id 内是 block-correlated 而非 i.i.d.，验证 oracle 模拟的 block-... | — |
7	| 3 | cls-seed0 | accuracy | 87.94 | 补充 cls seed=0 用于 5-paired comparison (cls vs traj 各 5 seeds)，确认 per-test classification... | — |
8	| 4 | cls-seed789 | accuracy | 89 | 补充 cls seed=789 用于 5-paired comparison (cls vs traj 各 5 seeds)，确认 per-test classificati... | — |
9	| 5 | cls4b-ckpt4600-test-mutation-pr | accuracy | 83.63 | 4B CLS ckpt-4600 test mutation-type precision/recall breakdown，论文 Table 数据 | — |
10	| 6 | cls4b-seed123-ckpt800-val5120-eval | accuracy | 87.92 | D063 val@5120: 4B CLS seed123 ckpt-800 在 val set 上评估 | — |
11	| 7 | cls4b-v5-ckpt4000-val5120-eval | accuracy | 89.84 | 4B v5 ckpt-4000 val@5120 eval (supplementary data, D088) | — |
12	| 8 | cls4b-v5-ckpt4400-test5120-eval | accuracy | 83.24 | 4B test sweep 补点: ckpt-4400 test@5120。Supplementary val+test 双线图数据。 | — |
13	| 9 | cls4b-v5-ckpt4600-test-eval | accuracy | 83.63 | 4B v5 val-best (ckpt-4600, val=90.07%) 的 test eval。D088 要求 val-best 必须有对应 test 数字。 | — |
14	| 10 | cls4b-v5-ckpt600-test5120-eval | accuracy | 77.74 | 4B s42 test sweep 补点: ckpt-600 test@5120。与 val curve 对齐，supplementary val+test 双线图。 | — |
15	| 11 | cls4b-v5-ckpt600-val5120-eval | accuracy | 82.82 | Evaluate repo-level classification v5 checkpoint-600 on val split with max_seq_length=5120 | — |
16	| 12 | cls4b-v5-val-sweep-ckpt4200 | accuracy | 89.06 | 4B v5 ckpt-4200 val@5120 评估，checkpoint selection sweep 数据点 | — |
17	| 13 | cls4b-v5-val-sweep-ckpt4400-v3 | accuracy | 89.96 | v1/v2 因 RTX 5090 间歇性 CUDA hang 卡死（详见 4b_eval_hang_analysis.md）。v3 未修改 watchdog，验证是否为低概率... | — |
18	| 14 | c
…[truncated 17369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T08:02:19.986955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/negative_experiments.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/negative_experiments.md"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T08:02:19.987141+00:00_

1	# Negative/Failed Experiments
2	
3	Total: 72 experiments
4	
5	| # | exp_id | conclusion | hypothesis | key_metric | notes |
6	|---|--------|-----------|-----------|-----------|-------|
7	| 1 | D124-cwm-s42-epoch2-eval | failed | — | — | — |
8	| 2 | D131-cwm-s42-epoch3-seq2048 | failed | — | — | — |
9	| 3 | D133-cwm-s42-e2-seq2048-home | failed | — | — | 2026-05-18 13:52 UTC: Resumed after stuck kill. PID=4187955 (sonny@tmux:D133-resume). Resumed fro... |
10	| 4 | cls4b-seed123-ckpt800-test5120-eval | failed | CLS 4B seed123 val-best (ckpt-800, val=87.92%) test@5120。补充 4B multi-seed rep... | — | v1 失败：home 版 eval_repo_cls.py 不支持 --max_new_tokens 参数 |
11	| 5 | cls4b-seed123-ckpt800-test5120-eval-v2 | negative | CLS 4B seed123 val-best (ckpt-800) test@5120。v1 因 --max_new_tokens 参数不兼容失败，v2... | accuracy=75.33 | test acc=75.33%, 远低于 s42 的 83.63%。seed123 val-best (ckpt-800) 在 test 上仅比 majority baseline (73%) ... |
12	| 6 | cls4b-v5-ckpt4000-test5120-eval | failed | 4B s42 test sweep 补点: ckpt-4000 test@5120。Supplementary val+test 双线图。 | — | 服务器 home-1x5090 离线导致失败。SSH 连接超时，cron 5次检查均失败。实验运行约46分钟后断连，可能已完成但无法确认。需服务器恢复后检查日志。 |
13	| 7 | cls4b-v5-val5120-sweep-home | failed | D063 val sweep: 4B CLS v5 (s42) val@5120 sweep (ckpt-600/4000/4200/4400/4600) | — | — |
14	| 8 | cls8b-repo-s456-eval | failed | Qwen3-8B CLS repo-level s456 eval: 用 val-best checkpoint 评估 test set accuracy... | — | 失败原因: argparse error — --output_dir 不是 eval_repo_cls.py 的合法参数，正确参数是 --output | 建议: 改 --output_dir... |
15	| 9 | cls8b-repo-s456-train | failed | Qwen3-8B CLS repo-level s456: 第3个seed，与s42(84.48%)和s123(85.6%)组成3-seed covera... | — | Crashed at step 200/552. Root cause: swebench_full/swebench_pilot_data.jsonl was overwritten at M... |
16	| 10 | cls8b-repo-s456-train-v2 | failed | Qwen3-8B CLS repo-level s456: 第3个seed，与s42(84.48%)和s123(85.6%)组成3-seed covera... | — | 失败原因: timeout_hours 过短 (8h)，训练在 step 2320/6633 (35%, epoch ~1.04) 被 kill。训练本身正常 (loss=0.4199, gra... |
17	| 11 | cls8b-s42-ckpt1200-
…[truncated 10875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T08:02:19.987456+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\begin\\\\{figure|\\\\\\\\includegraphics|Figure~|Fig\\\\.|figure2|plot_",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\begin\\\\{figure|\\\\\\\\includegraphics|Figure~|Fig\\\\.|figure2|plot_",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T08:02:19.987615+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T08:02:19.987743+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/registry_success_summary.json | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\n# Count unique experiments\nprint(f'Total experiments: {len(data)}')\n# List all exp_ids\nfor e in data:\n    print(e['exp_id'])\n\" | wc -l\n",
  "description": "Count experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/registry_success_summary.json | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\n# Count unique experiments\nprint(f'Total experiments: {len(data)}')\n# List all exp_ids\nfor e in data:\n    print(e['exp_id'])\n\" | wc -l\n",
    "description": "Count experiments"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T08:02:19.987900+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 3, in &lt;module>
    data = json.load(sys.stdin)
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T08:02:19.988037+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\begin.figure|\\\\\\\\includegraphics|Figure|\\\\\\\\label.fig",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\begin.figure|\\\\\\\\includegraphics|Figure|\\\\\\\\label.fig",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T08:02:19.988168+00:00_

docs/paper/experiments.tex:90:\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +1.70\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
docs/paper/experiments.tex:135:\paragraph{Formulation divergence (single-seed).} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 19.31\pp{} at 8B (84.48\% vs.\ 65.17\%). \cwm{} falls below majority baseline at both scales. These gaps suggest complexity-dependent formulation effectiveness, though single-seed design and multiple confounds (\S\ref{sec:threats}) preclude definitive causal attribution.
docs/paper/appendix.tex:36:[Omitted long matching line]
docs/paper/introduction.tex:8:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T08:02:19.988309+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fig:scaling_gap|includegraphics|begin.figure",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fig:scaling_gap|includegraphics|begin.figure",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T08:02:19.988467+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-87-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-88-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-89-
docs/paper/experiments.tex:90:\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +1.70\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-91-
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-92-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-93-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-132-
docs/paper/experiments.tex-133-Zero-shot prompting collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex-134-
docs/paper/experiments.tex:135:\paragraph{Formulation divergence (single-seed).} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 19.31\pp{} at 8B (84.48\% vs.\ 65.17\%). \cwm{} falls below majorit
…[truncated 5540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T08:02:19.988653+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'completed', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'completed', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'in_progress', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'completed', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'completed', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'in_progress', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T08:02:19.988824+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T08:02:19.988952+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T08:02:19.989100+00:00_

4b_8b_cls_cwm_paired_bootstrap_corrected.json
4b_eval_hang_analysis.md
D132-cwm-s123-e2-seq2048
D133_diagnosis.md
D138_data_investigation.md
_project
all_experiments_parsed.json
analysis_5paired_bootstrap.py
bf16_only_tost.json
bibliography_audit_report.json
bibliography_candidates.yaml
block-corr-empirical
block_correlation_analysis.py
ckpt6315_eval_analysis.md
cls4b-v5-ckpt4400-val5120-eval
cls8b-block-correlation-empirical
cls8b-s42-resume-ckpt3600-mutation
cls8b_s42_ckpt3600_per_mutation_pr.json
cls8b_s42_ckpt3600_per_test_pr_bucketed.json
cls8b_seed123_ckpt3000_val_eval_pending.md
cls_multiseed_summary.json
cls_multiseed_table.md
cls_v4_s123_config_comparison.md
cls_v5_cwm_epoch2_launch_config.md
comprehensive_results_summary.md
comprehensive_test_results.md
cwm-rank32-ablation-v2
cwm-rank32-alpha64-ablation
cwm4b_mutation_breakdown.json
cwm8b_seed123_analysis.txt
cwm8b_shard_progress.md
cwm_error_mode_analysis.md
cwm_overfitting_analysis.md
cwm_rank32_eval_command.sh
cwm_rank64_train_command.sh
cwm_v6_diagnosis.md
cwm_v6_health_check.md
d008_eval_commands.md
d076_val_unparseable_root_cause.md
d077_fix_report.md
deepseek-cls-repo-v5-ckpt2105-eval-analysis.md
deepseek-cwm-repo-s123-train
deepseek-cwm-repo-s456-train
deepseek-traj-func
deepseek-traj-func-v2
deepseek_func_icc_result.md
deepseek_func_summary.json
deepseek_training_analysis.md
deepseek_traj_per_seed_analysis.md
deepseek_zero_shot.json
diag_cls_v4.md
diag_cwm_v10.md
diag_server_failures_20260516.md
diagnose_deepseek_cwm_s123.md
diagnose_exp-downsample-cls-func-v3-eval.md
diagnosis_cwm_v12_cls_8b.md
dream_reports
efficiency_benchmark.json
error_analysis_data.md
error_complementarity_deepseek.json
error_overlap_matched_seed.json
eval_pipeline_prep.md
eval_readiness_report.md
eval_repo_cls.py
eval_repo_cls_v2.py
eval_status_check_20260514.md
experiment_status_check_loop19.md
extract_predictions_generic.py
f1-macro-audit.md
f1_macro_summary.json
few_shot_baseline.json
fig1_reformulation.pdf
fig1_reformul
…[truncated 2215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T08:02:19.989290+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/supplementary_completeness_audit.md",
  "content": "# Supplementary Completeness Audit\n\n## Summary\n\n| Category | Count |\n|----------|-------|\n| Total success experiments | 132 |\n| Referenced in paper (Tables/Sections/Appendix) | 88 |\n| Potentially valuable omissions | 28 |\n| Not applicable (training runs / intermediate / superseded) | 16 |\n\n---\n\n## Referenced Experiments\n\n### Table 1 — Function-Level Per-Test Accuracy (n=1,890)\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| multi-seed-core | CLS 4B 3-seed (s42/123/456) | Table 1 (5-seed mean 88.43±0.78) |\n| cls-seed789 | acc=89.00 | Table 1 (contributes to 5-seed mean) |\n| cls-seed0 | acc=87.94 | Table 1 (contributes to 5-seed mean) |\n| per-test-precision-recall | CWM 4B s42=87.51 | Table 1 (5-seed mean 87.19±0.37) |\n| cwm-seed123 | acc=87.20 | Table 1 |\n| cwm-seed456 | acc=86.98 | Table 1 |\n| cwm-seed789 | acc=86.67 | Table 1 |\n| cwm-seed0 | acc=87.57 | Table 1 |\n| traj-level-finetuned | acc=85.66 | Table 1 (TRAJ 4B 5-seed mean 86.30±0.97) |\n| traj-level-seed123 | acc=85.47 | Table 1 |\n| traj-level-seed456 | acc=87.40 | Table 1 |\n| traj-level-seed789 | acc=87.31 | Table 1 |\n| traj-level-seed0 | acc=85.66 | Table 1 |\n| deepseek-cls-func | CLS DeepSeek s42 | Table 1 (2-seed mean 86.85±0.11) |\n| deepseek-cls-func-s123 | CLS DeepSeek s123 | Table 1 |\n| deepseek-cwm-func | CWM DeepSeek s42 | Table 1 (2-seed mean 86.83±1.49) |\n| deepseek-cwm-func-s123 | CWM DeepSeek s123 | Table 1 |\n| deepseek-traj-func-v2 | TRAJ DeepSeek s42 | Table 1 (2-seed mean 84.16±1.30) |\n| deepseek-traj-func-v2-s123 | TRAJ DeepSeek s123 | Table 1 |\n| qwen3-0shot-func-baseline | acc=68.70 | Table 1 (0-shot Qwen3-8B) |\n| deepseek-0shot-func-baseline | acc=63.00 | Table 1 (0-shot DeepSeek) |\n| llm-judge-8b-zeroshot | acc=64.40 | Table 1 (ZS LLM-as-judge 8B) |\n| llm-judge-32b-zeroshot | acc=71.69 | Table 1 (ZS LLM-as-judge 32B NF4) |\n| exp-e-qwen3-3shot-baseline | 3-shot Qwen3 | Table 1 (3-shot ICL 68.78) |\n\n### Table 2 — Model-Size Scaling (Qwen3, seeds 42/123, bf16)\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| model-size-scaling-cls8b | CLS 8B s42=90.48 | Table 2 |\n| cls8b-seed123 | CLS 8B s123=89.40 | Table 2 |\n| model-size-scaling-cwm8b | CWM 8B s42=87.67 | Table 2 |\n| cwm8b-seed123 | CWM 8B s123=86.98 | Table 2 |\n| qwen3-8b-traj-func-s42 | TRAJ 8B s42 | Table 2 (TRAJ 8B s42=87.60) |\n| qwen3-8b-traj-func-s123 | TRAJ 8B s123 | Table 2 (TRAJ 8B s123=87.79) |\n| cls8b-seed456 | CLS 8B s456=88.31 | §5.2 (3-seed clustered bootstrap p=0.0066) |\n| cwm8b-seed456 | CWM 8B s456=86.24 | §5.2 (3-seed clustered bootstrap) |\n\n### Table 3 — Repo-Level Cross-Formulation\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| cls4b-v5-ckpt4600-test-eval | CLS 4B s42=83.63 | Table 3 |\n| cls8b-s42-resume-ckpt3600-test-v2 | CLS 8B s42=84.48 | Table 3 |\n| cls8b-seed123-ckpt3000-test8192-eval | CLS 8B s123=85.60 | Table 3 |\n| cls8b-repo-s456-eval-v2 | CLS 8B s456=84.40 | Table 3 (mean 84.83±0.67) |\n| deepseek-cls-repo-v5-ckpt2105-eval | DeepSeek CLS s42 e1=82.61 | Table 3 |\n| deepseek-cls-repo-v5-ckpt6315-eval | DeepSeek CLS s42 e3=82.51 | App: variant-level table |\n| deepseek-cls-repo-s123 | DeepSeek CLS s123=74.93 | Table 3 |\n| deepseek-cls-repo-s456-eval-v2 | DeepSeek CLS s456=86.15 | Table 3 (2-seed mean 84.38±2.50) |\n| cwm4b-s42-mutation-breakdown | CWM 4B=58.04 | Table 3 |\n| qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | CWM 8B seq4096=64.36 | App: threats/seq-length |\n| deepseek-cwm-repo-s42-seq4096-eval | DeepSeek CWM=61.49 | Table 3 |\n| qwen3-4b-traj-repo-s42-eval | TRAJ 4B=72.92 | Table 3 |\n| qwen3-8b-traj-repo-s42-ckpt98-eval | TRAJ 8B epoch 2=72.92 | Table 3 / App: threats |\n| qwen3-8b-traj-repo-s42-best-eval | TRAJ 8B epoch 3=70.83 | App: threats (TRAJ epoch comparison) |\n| qwen3-8b-traj-repo-s123 | TRAJ 8B s123=77.08 | Table 3 (3-seed mean 72.91±3.61) |\n| qwen3-8b-traj-repo-s456 | TRAJ 8B s456=70.83 | Table 3 |\n| deepseek-traj-repo | DeepSeek TRAJ s42 | Table 3 |\n| deepseek-traj-repo-8k | DeepSeek TRAJ 8k s42=81.25 | Table 3 |\n| deepseek-traj-repo-8k-s123 | variant=75.00 | Table 3 (3-seed mean 77.08±3.61) |\n| deepseek-traj-repo-8k-s456 | variant=75.00 | Table 3 |\n| deepseek-traj-repo-s123 | variant=77.08 | Table 3 |\n| deepseek-traj-repo-8k-s0 | variant=75.00 | App: 6-seed TRAJ (mean 75.35±5.00) |\n| deepseek-traj-repo-8k-s789 | variant=66.67 | App: 6-seed TRAJ |\n| deepseek-traj-repo-8k-s999 | variant=79.17 | App: 6-seed TRAJ |\n| repo-level-0shot-baseline | 0-shot Qwen=49.90 | Table 3 |\n| deepseek-0shot-repo-baseline | 0-shot DeepSeek=48.50 | Table 3 |\n\n### Statistical Analysis (§5.2, §5.3, Appendix)\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| 5-paired-clustered-bootstrap | gap=-0.45pp, TOST p=0.007 | §5.2 equivalence, App: TOST/Holm |\n| block-corr-empirical | ICC=0.191, DEFF=3.97 | §5.3, App (f) |\n| oracle-f2p-stratified | block_adv=10.93pp | §5.3, App oracle table + Figure 3 |\n| mvp-a-oracle-sim | oracle routing | §5.3 (oracle concept) |\n| exp-a-routing | oracle routing=100% | §5.3 (oracle CLS-CWM routing) |\n| exp-b-complexity-bin | complexity analysis | §5 analysis (T-based binning) |\n\n### Appendix — Ablation / Control Experiments\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| cwm-rank32-ablation-v2 | acc=87.00 | App: LoRA rank ablation table |\n| cwm-rank32-alpha64-ablation | acc=87.04 | App: LoRA rank ablation table |\n| cls8b-s42-ckpt3600-seq2048-ablation | acc=83.04 | App: seq-length ablation |\n| cls8b-s42-ckpt-ablation | ckpt-2200=85.34, ckpt-6633=85.29 | App: threats (checkpoint selection <1pp) |\n| exp-downsample-cls-func-v3-eval | acc=80.74 | App: downsample control |\n| exp-downsample-cls-func-v3 | training run | App: downsample (produces model) |\n| exp-d-constrained-decoding | CWM constrained | App (b) unparseable analysis |\n| repo-level-3shot-baseline | per_test=46.28 | App: few-shot table |\n| cls4b-ckpt4600-test-mutation-pr | CLS 4B mutation data | App: per-mutation table |\n| cls8b-s42-resume-ckpt3600-mutation | CLS 8B s42 mutation data | App: per-mutation table |\n| cls8b-seed123-ckpt3000-mutation | CLS 8B s123 mutation data | App: per-mutation table |\n\n---\n\n## Potentially Valuable Omissions\n\n### Priority 1: Checkpoint Val/Test Sweep Curves (28 experiments)\n\n**These ~28 experiments form complete val+test training curves for CLS 4B and 8B across seeds 42/123. The paper mentions \"checkpoint selection: <1pp\" and references 3 specific checkpoints in Threats, but does NOT include a supplementary figure showing the full training dynamics.**\n\nA checkpoint sweep figure would:\n- Visually demonstrate the <1pp checkpoint selection claim\n- Show val-test correlation (or lack thereof)\n- Strengthen the \"no cherry-picking\" argument\n- Provide diagnostic value for reproducibility\n\n**Suggested: Appendix supplementary figure with val/test curves**\n\n#### 4B Seed 42 Val Sweep (6 experiments)\n| exp_id | checkpoint | val acc (%) |\n|--------|-----------|-------------|\n| cls4b-v5-ckpt600-val5120-eval | ckpt-600 | 82.82 |\n| cls4b-v5-ckpt4000-val5120-eval | ckpt-4000 | 89.84 |\n| cls4b-v5-val-sweep-ckpt4200 | ckpt-4200 | 89.06 |\n| cls4b-v5-val-sweep-ckpt4400-v3 | ckpt-4400 | 89.96 |\n| cls4b-v5-val-sweep-ckpt4600 | ckpt-4600 | 90.07 |\n| cls4b-seed123-ckpt800-val5120-eval | s123 ckpt-800 | 87.92 |\n\n#### 4B Seed 42 Test Sweep (2 experiments)\n| exp_id | checkpoint | test acc (%) |\n|--------|-----------|-------------|\n| cls4b-v5-ckpt600-test5120-eval | ckpt-600 | 77.74 |\n| cls4b-v5-ckpt4400-test5120-eval | ckpt-4400 | 83.24 |\n\n#### 8B Seed 42 Val Sweep (7 experiments)\n| exp_id | checkpoint | val acc (%) |\n|--------|-----------|-------------|\n| cls8b-s42-ckpt200-val8192-eval-v2 | ckpt-200 | 63.52 |\n| cls8b-s42-ckpt800-val8192-eval | ckpt-800 | 84.50 |\n| cls8b-s42-ckpt1000-val8192-eval | ckpt-1000 | 88.23 |\n| cls8b-s42-ckpt1200-val8192-v3 | ckpt-1200 | 87.76 |\n| cls8b-s42-ckpt1400-val8192-eval | ckpt-1400 | 85.97 |\n| cls8b-s42-ckpt1600-val8192-v2 | ckpt-1600 | 86.75 |\n| cls8b-s42-resume-val-sweep-seq8192-v2 | 21 ckpts (1800-5800) | sweep data |\n\n#### 8B Seed 42 Test Sweep (8 experiments)\n| exp_id | checkpoint | test acc (%) |\n|--------|-----------|-------------|\n| cls8b-s42-ckpt200-test8192-eval | ckpt-200 | 70.07 |\n| cls8b-s42-ckpt400-test8192-eval | ckpt-400 | 84.79 |\n| cls8b-s42-ckpt600-test8192-eval | ckpt-600 | 79.05 |\n| cls8b-s42-ckpt800-test8192-eval | ckpt-800 | 83.53 |\n| cls8b-s42-ckpt1000-test8192-eval | ckpt-1000 | 83.52 |\n| cls8b-s42-ckpt1200-test8192-eval | ckpt-1200 | 83.84 |\n| cls8b-s42-ckpt1400-test8192-eval | ckpt-1400 | 85.47 |\n| cls8b-s42-ckpt1600-test8192-eval | ckpt-1600 | 84.99 |\n\n#### 8B Seed 123 Val Sweep (5 experiments)\n| exp_id | checkpoint | val acc (%) |\n|--------|-----------|-------------|\n| cls8b-seed123-ckpt3000-val8192-eval | ckpt-3000 | 88.69 |\n| cls8b-seed123-ckpt6200-val8192-eval | ckpt-6200 | 87.52 |\n| cls8b-seed123-ckpt6400-val8192-eval | ckpt-6400 | 87.48 |\n| cls8b-seed123-ckpt6600-val8192-eval | ckpt-6600 | 87.23 |\n| cls8b-seed123-ckpt6633-val8192-eval | ckpt-6633 | 87.10 |\n\n#### 8B Seed 123 Test Sweep (5 experiments)\n| exp_id | checkpoint | test acc (%) |\n|--------|-----------|-------------|\n| cls8b-seed123-ckpt200-test-eval | ckpt-200 | 72.55 |\n| cls8b-seed123-ckpt6200-test-eval-v2 | ckpt-6200 | 84.70 |\n| cls8b-seed123-ckpt6400-test-eval-v2 | ckpt-6400 | 85.08 |\n| cls8b-seed123-ckpt6600-test-eval | ckpt-6600 | 84.90 |\n| cls8b-seed123-ckpt6633-test-eval | ckpt-6633 | 84.89 |\n\n### Priority 2: Additional Seq-Length Ablation Data Point\n\n| exp_id | metric | why valuable | suggested location |\n|--------|--------|--------------|--------------------|\n| cls8b-s42-ckpt1000-test-seq2048-ablation | acc=82.83 | Second data point for seq-length ablation (ckpt-1000@2048 vs ckpt-3600@2048=83.04). Shows <1pp consistency across checkpoints at short context. | App: threats, alongside existing 83.04% |\n\n### Priority 3: DeepSeek CWM s123 1-Epoch\n\n| exp_id | metric | why valuable | suggested location |\n|--------|--------|--------------|--------------------|\n| deepseek-cwm-repo-s123-eval-1epoch | acc=75.45 | DeepSeek CWM s123 at 1-epoch checkpoint. Paper cites DeepSeek CWM val-selected (56.70%) and epoch-3 (61.49%) for s42, but s123 1-epoch data (75.45) is unreported. Could strengthen or complicate the CWM epoch analysis. | App: threats (epoch selection) |\n\n---\n\n## Not Applicable (Training Runs / Intermediate / Superseded)\n\nThese experiments don't require paper citation — they are infrastructure (model training), intermediate artifacts (prediction JSONs), superseded versions, or partial evaluations.\n\n| exp_id | reason |\n|--------|--------|\n| deepseek-cls-repo-v5 | Training run — produces model evaluated in Table 3 |\n| deepseek-cwm-repo | Training run |\n| deepseek-traj-func | v1, superseded by v2 |\n| exp-downsample-cls-func-v3 | Training run (eval in exp-downsample-cls-func-v3-eval) |\n| qwen3-4b-traj-repo-s42 | Training run |\n| qwen3-8b-traj-repo-s42-v2 | Training run |\n| repo-level-cls-8b-conda | Training run |\n| repo-level-cls-8b-s42-resume | Training run (resume continuation) |\n| repo-level-cls-8b-seed123-conda-v3 | Training run |\n| repo-level-cls-seed123-home | Training run |\n| repo-level-cls-v4 | Early iteration, superseded by v5 |\n| repo-level-cls-v5 | Training run (produces CLS 4B model) |\n| repo-level-cls-v5-conda | Training variant (conda env replication) |\n| repo-level-cwm-v10 | Training run |\n| cls8b-eval-seed42 | Intermediate — generates prediction JSONs for error analysis |\n| cls8b-eval-seed123 | Intermediate — generates prediction JSONs |\n| matched-seed-8b-predictions | Intermediate — generates prediction JSONs for overlap analysis |\n| cls8b-s42-resume-ckpt3600-test | Superseded by v2 (data issue) |\n| cwm8b-ckpt400-test-eval-shard2 | Shard of CWM 8B eval (partial) |\n| cwm8b-ckpt400-test-eval-shard4 | Shard of CWM 8B eval (partial) |\n| mvp-b-data-prep | Data preparation — foundational, no results |\n| mvp-b-train | Initial pilot training — foundational |\n\n---\n\n## Negative Results Worth Discussing\n\n72 experiments have conclusion=failed or negative. Of these, ~67 are infrastructure failures (OOM, SSH timeout, argparse errors, GPU conflicts). 5-6 are genuine negative results:\n\n### Already Referenced in Paper\n\n| exp_id | conclusion | finding | where cited |\n|--------|-----------|---------|-------------|\n| p2p-regression-rate | negative | P2P rate 1.04% mean, 0% median | App (a): P2P regression rate |\n| cwm-baseline | negative | CWM tied CLS at 87.51% (hypothesis: CWM < CLS) | Table 1 (CWM 4B s42=87.51) |\n| per-test-majority-voting | negative | K=3 hurt accuracy by -0.68pp | App (g): failed interventions |\n| re-repair-phase0 | negative | Oracle diagnostics no effect | §5.3 re-repair pilot |\n| re-repair-docker-eval | negative | A1=52.3%, p=0.42, effect ~0 | §5.3 re-repair pilot |\n| cls4b-seed123-ckpt800-test5120-eval-v2 | negative | 4B s123 test=75.33%, far below s42=83.63 | App: limitations (seed instability caveat) |\n\n### Not Referenced But Worth Considering\n\n| exp_id | conclusion | finding | assessment |\n|--------|-----------|---------|------------|\n| repo-level-cwm-8b-conda-v5 | negative | 8B CWM training killed at 93.4% (step 6198/6633) | Infrastructure failure, not a scientific negative. Irrelevant for paper. |\n\n**Verdict: All scientifically meaningful negative results are already covered in the paper.** The remaining failed experiments are infrastructure issues that don't warrant paper discussion.\n\n---\n\n## Recommendations (Priority-Ordered)\n\n### 1. [HIGH] Add Checkpoint Sweep Figure to Appendix\n\n**28 experiments** of val/test sweep data are unreferenced. A dual-panel figure (4B + 8B, val + test curves) would:\n- Visually confirm the \"<1pp checkpoint selection noise\" claim (currently text-only)\n- Demonstrate val-test monotonicity (or lack thereof)\n- Show training dynamics differ across seeds\n- Use existing data — no new experiments needed\n\n**Suggested: App Figure \"Checkpoint Selection Sensitivity\" with 4 subplots (4B-val, 4B-test, 8B-val, 8B-test), each showing training step vs accuracy.**\n\nData available: 6 val + 2 test checkpoints for 4B-s42; 7 val + 8 test for 8B-s42; 5 val + 5 test for 8B-s123.\n\n### 2. [LOW] Mention Seq-Length Consistency Across Checkpoints\n\ncls8b-s42-ckpt1000-test-seq2048-ablation (82.83%) is within <1pp of cls8b-s42-ckpt3600-seq2048-ablation (83.04%). A one-sentence note in the seq-length ablation paragraph would strengthen the robustness claim.\n\n### 3. [LOW] DeepSeek CWM s123 Epoch Comparison\n\ndeepseek-cwm-repo-s123-eval-1epoch (75.45%) provides a cross-seed data point for CWM epoch selection. The paper discusses CWM epoch selection for s42 only (val-selected 56.70% vs epoch-3 61.49%). Adding the s123 1-epoch data could either corroborate or complicate this analysis. Evaluate before including.\n\n---\n\n## Coverage Statistics\n\n| Paper Section | Experiments Referenced | % of Total |\n|--------------|----------------------|------------|\n| Table 1 (func-level) | 24 | 18.2% |\n| Table 2 (scaling) | 8 | 6.1% |\n| Table 3 (repo-level) | 26 | 19.7% |\n| Table 4 (taxonomy) | (derived from above) | — |\n| §5.2 equivalence | 3 | 2.3% |\n| §5.3 analysis | 4 | 3.0% |\n| App: ablation/control | 11 | 8.3% |\n| App: per-mutation | 3 | 2.3% |\n| App: TRAJ DeepSeek 6-seed | 3 | 2.3% |\n| App: threats | 3 | 2.3% |\n| App: few-shot | 1 | 0.8% |\n| **Subtotal referenced** | **88** | **66.7%** |\n| Val/test sweep (unused) | 28 | 21.2% |\n| Training/intermediate | 16 | 12.1% |\n\n**Conclusion: The paper already references 88/132 (67%) of success experiments. The remaining 33% are split between val/test sweep data (useful for a supplementary figure) and training infrastructure (not citable). All negative results with scientific value are already discussed.**\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/supplementary_completeness_audit.md",
    "content": "# Supplementary Completeness Audit\n\n## Summary\n\n| Category | Count |\n|----------|-------|\n| Total success experiments | 132 |\n| Referenced in paper (Tables/Sections/Appendix) | 88 |\n| Potentially valuable omissions | 28 |\n| Not applicable (training runs / intermediate / superseded) | 16 |\n\n---\n\n## Referenced Experiments\n\n### Table 1 — Function-Level Per-Test Accuracy (n=1,890)\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| multi-seed-core | CLS 4B 3-seed (s42/123/456) | Table 1 (5-seed mean 88.43±0.78) |\n| cls-seed789 | acc=89.00 | Table 1 (contributes to 5-seed mean) |\n| cls-seed0 | acc=87.94 | Table 1 (contributes to 5-seed mean) |\n| per-test-precision-recall | CWM 4B s42=87.51 | Table 1 (5-seed mean 87.19±0.37) |\n| cwm-seed123 | acc=87.20 | Table 1 |\n| cwm-seed456 | acc=86.98 | Table 1 |\n| cwm-seed789 | acc=86.67 | Table 1 |\n| cwm-seed0 | acc=87.57 | Table 1 |\n| traj-level-finetuned | acc=85.66 | Table 1 (TRAJ 4B 5-seed mean 86.30±0.97) |\n| traj-level-seed123 | acc=85.47 | Table 1 |\n| traj-level-seed456 | acc=87.40 | Table 1 |\n| traj-level-seed789 | acc=87.31 | Table 1 |\n| traj-level-seed0 | acc=85.66 | Table 1 |\n| deepseek-cls-func | CLS DeepSeek s42 | Table 1 (2-seed mean 86.85±0.11) |\n| deepseek-cls-func-s123 | CLS DeepSeek s123 | Table 1 |\n| deepseek-cwm-func | CWM DeepSeek s42 | Table 1 (2-seed mean 86.83±1.49) |\n| deepseek-cwm-func-s123 | CWM DeepSeek s123 | Table 1 |\n| deepseek-traj-func-v2 | TRAJ DeepSeek s42 | Table 1 (2-seed mean 84.16±1.30) |\n| deepseek-traj-func-v2-s123 | TRAJ DeepSeek s123 | Table 1 |\n| qwen3-0shot-func-baseline | acc=68.70 | Table 1 (0-shot Qwen3-8B) |\n| deepseek-0shot-func-baseline | acc=63.00 | Table 1 (0-shot DeepSeek) |\n| llm-judge-8b-zeroshot | acc=64.40 | Table 1 (ZS LLM-as-judge 8B) |\n| llm-judge-32b-zeroshot | acc=71.69 | Table 1 (ZS LLM-as-judge 32B NF4) |\n| exp-e-qwen3-3shot-baseline | 3-shot Qwen3 | Table 1 (3-shot ICL 68.78) |\n\n### Table 2 — Model-Size Scaling (Qwen3, seeds 42/123, bf16)\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| model-size-scaling-cls8b | CLS 8B s42=90.48 | Table 2 |\n| cls8b-seed123 | CLS 8B s123=89.40 | Table 2 |\n| model-size-scaling-cwm8b | CWM 8B s42=87.67 | Table 2 |\n| cwm8b-seed123 | CWM 8B s123=86.98 | Table 2 |\n| qwen3-8b-traj-func-s42 | TRAJ 8B s42 | Table 2 (TRAJ 8B s42=87.60) |\n| qwen3-8b-traj-func-s123 | TRAJ 8B s123 | Table 2 (TRAJ 8B s123=87.79) |\n| cls8b-seed456 | CLS 8B s456=88.31 | §5.2 (3-seed clustered bootstrap p=0.0066) |\n| cwm8b-seed456 | CWM 8B s456=86.24 | §5.2 (3-seed clustered bootstrap) |\n\n### Table 3 — Repo-Level Cross-Formulation\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| cls4b-v5-ckpt4600-test-eval | CLS 4B s42=83.63 | Table 3 |\n| cls8b-s42-resume-ckpt3600-test-v2 | CLS 8B s42=84.48 | Table 3 |\n| cls8b-seed123-ckpt3000-test8192-eval | CLS 8B s123=85.60 | Table 3 |\n| cls8b-repo-s456-eval-v2 | CLS 8B s456=84.40 | Table 3 (mean 84.83±0.67) |\n| deepseek-cls-repo-v5-ckpt2105-eval | DeepSeek CLS s42 e1=82.61 | Table 3 |\n| deepseek-cls-repo-v5-ckpt6315-eval | DeepSeek CLS s42 e3=82.51 | App: variant-level table |\n| deepseek-cls-repo-s123 | DeepSeek CLS s123=74.93 | Table 3 |\n| deepseek-cls-repo-s456-eval-v2 | DeepSeek CLS s456=86.15 | Table 3 (2-seed mean 84.38±2.50) |\n| cwm4b-s42-mutation-breakdown | CWM 4B=58.04 | Table 3 |\n| qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | CWM 8B seq4096=64.36 | App: threats/seq-length |\n| deepseek-cwm-repo-s42-seq4096-eval | DeepSeek CWM=61.49 | Table 3 |\n| qwen3-4b-traj-repo-s42-eval | TRAJ 4B=72.92 | Table 3 |\n| qwen3-8b-traj-repo-s42-ckpt98-eval | TRAJ 8B epoch 2=72.92 | Table 3 / App: threats |\n| qwen3-8b-traj-repo-s42-best-eval | TRAJ 8B epoch 3=70.83 | App: threats (TRAJ epoch comparison) |\n| qwen3-8b-traj-repo-s123 | TRAJ 8B s123=77.08 | Table 3 (3-seed mean 72.91±3.61) |\n| qwen3-8b-traj-repo-s456 | TRAJ 8B s456=70.83 | Table 3 |\n| deepseek-traj-repo | DeepSeek TRAJ s42 | Table 3 |\n| deepseek-traj-repo-8k | DeepSeek TRAJ 8k s42=81.25 | Table 3 |\n| deepseek-traj-repo-8k-s123 | variant=75.00 | Table 3 (3-seed mean 77.08±3.61) |\n| deepseek-traj-repo-8k-s456 | variant=75.00 | Table 3 |\n| deepseek-traj-repo-s123 | variant=77.08 | Table 3 |\n| deepseek-traj-repo-8k-s0 | variant=75.00 | App: 6-seed TRAJ (mean 75.35±5.00) |\n| deepseek-traj-repo-8k-s789 | variant=66.67 | App: 6-seed TRAJ |\n| deepseek-traj-repo-8k-s999 | variant=79.17 | App: 6-seed TRAJ |\n| repo-level-0shot-baseline | 0-shot Qwen=49.90 | Table 3 |\n| deepseek-0shot-repo-baseline | 0-shot DeepSeek=48.50 | Table 3 |\n\n### Statistical Analysis (§5.2, §5.3, Appendix)\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| 5-paired-clustered-bootstrap | gap=-0.45pp, TOST p=0.007 | §5.2 equivalence, App: TOST/Holm |\n| block-corr-empirical | ICC=0.191, DEFF=3.97 | §5.3, App (f) |\n| oracle-f2p-stratified | block_adv=10.93pp | §5.3, App oracle table + Figure 3 |\n| mvp-a-oracle-sim | oracle routing | §5.3 (oracle concept) |\n| exp-a-routing | oracle routing=100% | §5.3 (oracle CLS-CWM routing) |\n| exp-b-complexity-bin | complexity analysis | §5 analysis (T-based binning) |\n\n### Appendix — Ablation / Control Experiments\n\n| exp_id | metric | where cited |\n|--------|--------|-------------|\n| cwm-rank32-ablation-v2 | acc=87.00 | App: LoRA rank ablation table |\n| cwm-rank32-alpha64-ablation | acc=87.04 | App: LoRA rank ablation table |\n| cls8b-s42-ckpt3600-seq2048-ablation | acc=83.04 | App: seq-length ablation |\n| cls8b-s42-ckpt-ablation | ckpt-2200=85.34, ckpt-6633=85.29 | App: threats (checkpoint selection <1pp) |\n| exp-downsample-cls-func-v3-eval | acc=80.74 | App: downsample control |\n| exp-downsample-cls-func-v3 | training run | App: downsample (produces model) |\n| exp-d-constrained-decoding | CWM constrained | App (b) unparseable analysis |\n| repo-level-3shot-baseline | per_test=46.28 | App: few-shot table |\n| cls4b-ckpt4600-test-mutation-pr | CLS 4B mutation data | App: per-mutation table |\n| cls8b-s42-resume-ckpt3600-mutation | CLS 8B s42 mutation data | App: per-mutation table |\n| cls8b-seed123-ckpt3000-mutation | CLS 8B s123 mutation data | App: per-mutation table |\n\n---\n\n## Potentially Valuable Omissions\n\n### Priority 1: Checkpoint Val/Test Sweep Curves (28 experiments)\n\n**These ~28 experiments form complete val+test training curves for CLS 4B and 8B across seeds 42/123. The paper mentions \"checkpoint selection: <1pp\" and references 3 specific checkpoints in Threats, but does NOT include a supplementary figure showing the full training dynamics.**\n\nA checkpoint sweep figure would:\n- Visually demonstrate the <1pp checkpoint selection claim\n- Show val-test correlation (or lack thereof)\n- Strengthen the \"no cherry-picking\" argument\n- Provide diagnostic value for reproducibility\n\n**Suggested: Appendix supplementary figure with val/test curves**\n\n#### 4B Seed 42 Val Sweep (6 experiments)\n| exp_id | checkpoint | val acc (%) |\n|--------|-----------|-------------|\n| cls4b-v5-ckpt600-val5120-eval | ckpt-600 | 82.82 |\n| cls4b-v5-ckpt4000-val5120-eval | ckpt-4000 | 89.84 |\n| cls4b-v5-val-sweep-ckpt4200 | ckpt-4200 | 89.06 |\n| cls4b-v5-val-sweep-ckpt4400-v3 | ckpt-4400 | 89.96 |\n| cls4b-v5-val-sweep-ckpt4600 | ckpt-4600 | 90.07 |\n| cls4b-seed123-ckpt800-val5120-eval | s123 ckpt-800 | 87.92 |\n\n#### 4B Seed 42 Test Sweep (2 experiments)\n| exp_id | checkpoint | test acc (%) |\n|--------|-----------|-------------|\n| cls4b-v5-ckpt600-test5120-eval | ckpt-600 | 77.74 |\n| cls4b-v5-ckpt4400-test5120-eval | ckpt-4400 | 83.24 |\n\n#### 8B Seed 42 Val Sweep (7 experiments)\n| exp_id | checkpoint | val acc (%) |\n|--------|-----------|-------------|\n| cls8b-s42-ckpt200-val8192-eval-v2 | ckpt-200 | 63.52 |\n| cls8b-s42-ckpt800-val8192-eval | ckpt-800 | 84.50 |\n| cls8b-s42-ckpt1000-val8192-eval | ckpt-1000 | 88.23 |\n| cls8b-s42-ckpt1200-val8192-v3 | ckpt-1200 | 87.76 |\n| cls8b-s42-ckpt1400-val8192-eval | ckpt-1400 | 85.97 |\n| cls8b-s42-ckpt1600-val8192-v2 | ckpt-1600 | 86.75 |\n| cls8b-s42-resume-val-sweep-seq8192-v2 | 21 ckpts (1800-5800) | sweep data |\n\n#### 8B Seed 42 Test Sweep (8 experiments)\n| exp_id | checkpoint | test acc (%) |\n|--------|-----------|-------------|\n| cls8b-s42-ckpt200-test8192-eval | ckpt-200 | 70.07 |\n| cls8b-s42-ckpt400-test8192-eval | ckpt-400 | 84.79 |\n| cls8b-s42-ckpt600-test8192-eval | ckpt-600 | 79.05 |\n| cls8b-s42-ckpt800-test8192-eval | ckpt-800 | 83.53 |\n| cls8b-s42-ckpt1000-test8192-eval | ckpt-1000 | 83.52 |\n| cls8b-s42-ckpt1200-test8192-eval | ckpt-1200 | 83.84 |\n| cls8b-s42-ckpt1400-test8192-eval | ckpt-1400 | 85.47 |\n| cls8b-s42-ckpt1600-test8192-eval | ckpt-1600 | 84.99 |\n\n#### 8B Seed 123 Val Sweep (5 experiments)\n| exp_id | checkpoint | val acc (%) |\n|--------|-----------|-------------|\n| cls8b-seed123-ckpt3000-val8192-eval | ckpt-3000 | 88.69 |\n| cls8b-seed123-ckpt6200-val8192-eval | ckpt-6200 | 87.52 |\n| cls8b-seed123-ckpt6400-val8192-eval | ckpt-6400 | 87.48 |\n| cls8b-seed123-ckpt6600-val8192-eval | ckpt-6600 | 87.23 |\n| cls8b-seed123-ckpt6633-val8192-eval | ckpt-6633 | 87.10 |\n\n#### 8B Seed 123 Test Sweep (5 experiments)\n| exp_id | checkpoint | test acc (%) |\n|--------|-----------|-------------|\n| cls8b-seed123-ckpt200-test-eval | ckpt-200 | 72.55 |\n| cls8b-seed123-ckpt6200-test-eval-v2 | ckpt-6200 | 84.70 |\n| cls8b-seed123-ckpt6400-test-eval-v2 | ckpt-6400 | 85.08 |\n| cls8b-seed123-ckpt6600-test-eval | ckpt-6600 | 84.90 |\n| cls8b-seed123-ckpt6633-test-eval | ckpt-6633 | 84.89 |\n\n### Priority 2: Additional Seq-Length Ablation Data Point\n\n| exp_id | metric | why valuable | suggested location |\n|--------|--------|--------------|--------------------|\n| cls8b-s42-ckpt1000-test-seq2048-ablation | acc=82.83 | Second data point for seq-length ablation (ckpt-1000@2048 vs ckpt-3600@2048=83.04). Shows <1pp consistency across checkpoints at short context. | App: threats, alongside existing 83.04% |\n\n### Priority 3: DeepSeek CWM s123 1-Epoch\n\n| exp_id | metric | why valuable | suggested location |\n|--------|--------|--------------|--------------------|\n| deepseek-cwm-repo-s123-eval-1epoch | acc=75.45 | DeepSeek CWM s123 at 1-epoch checkpoint. Paper cites DeepSeek CWM val-selected (56.70%) and epoch-3 (61.49%) for s42, but s123 1-epoch data (75.45) is unreported. Could strengthen or complicate the CWM epoch analysis. | App: threats (epoch selection) |\n\n---\n\n## Not Applicable (Training Runs / Intermediate / Superseded)\n\nThese experiments don't require paper citation — they are infrastructure (model training), intermediate artifacts (prediction JSONs), superseded versions, or partial evaluations.\n\n| exp_id | reason |\n|--------|--------|\n| deepseek-cls-repo-v5 | Training run — produces model evaluated in Table 3 |\n| deepseek-cwm-repo | Training run |\n| deepseek-traj-func | v1, superseded by v2 |\n| exp-downsample-cls-func-v3 | Training run (eval in exp-downsample-cls-func-v3-eval) |\n| qwen3-4b-traj-repo-s42 | Training run |\n| qwen3-8b-traj-repo-s42-v2 | Training run |\n| repo-level-cls-8b-conda | Training run |\n| repo-level-cls-8b-s42-resume | Training run (resume continuation) |\n| repo-level-cls-8b-seed123-conda-v3 | Training run |\n| repo-level-cls-seed123-home | Training run |\n| repo-level-cls-v4 | Early iteration, superseded by v5 |\n| repo-level-cls-v5 | Training run (produces CLS 4B model) |\n| repo-level-cls-v5-conda | Training variant (conda env replication) |\n| repo-level-cwm-v10 | Training run |\n| cls8b-eval-seed42 | Intermediate — generates prediction JSONs for error analysis |\n| cls8b-eval-seed123 | Intermediate — generates prediction JSONs |\n| matched-seed-8b-predictions | Intermediate — generates prediction JSONs for overlap analysis |\n| cls8b-s42-resume-ckpt3600-test | Superseded by v2 (data issue) |\n| cwm8b-ckpt400-test-eval-shard2 | Shard of CWM 8B eval (partial) |\n| cwm8b-ckpt400-test-eval-shard4 | Shard of CWM 8B eval (partial) |\n| mvp-b-data-prep | Data preparation — foundational, no results |\n| mvp-b-train | Initial pilot training — foundational |\n\n---\n\n## Negative Results Worth Discussing\n\n72 experiments have conclusion=failed or negative. Of these, ~67 are infrastructure failures (OOM, SSH timeout, argparse errors, GPU conflicts). 5-6 are genuine negative results:\n\n### Already Referenced in Paper\n\n| exp_id | conclusion | finding | where cited |\n|--------|-----------|---------|-------------|\n| p2p-regression-rate | negative | P2P rate 1.04% mean, 0% median | App (a): P2P regression rate |\n| cwm-baseline | negative | CWM tied CLS at 87.51% (hypothesis: CWM < CLS) | Table 1 (CWM 4B s42=87.51) |\n| per-test-majority-voting | negative | K=3 hurt accuracy by -0.68pp | App (g): failed interventions |\n| re-repair-phase0 | negative | Oracle diagnostics no effect | §5.3 re-repair pilot |\n| re-repair-docker-eval | negative | A1=52.3%, p=0.42, effect ~0 | §5.3 re-repair pilot |\n| cls4b-seed123-ckpt800-test5120-eval-v2 | negative | 4B s123 test=75.33%, far below s42=83.63 | App: limitations (seed instability caveat) |\n\n### Not Referenced But Worth Considering\n\n| exp_id | conclusion | finding | assessment |\n|--------|-----------|---------|------------|\n| repo-level-cwm-8b-conda-v5 | negative | 8B CWM training killed at 93.4% (step 6198/6633) | Infrastructure failure, not a scientific negative. Irrelevant for paper. |\n\n**Verdict: All scientifically meaningful negative results are already covered in the paper.** The remaining failed experiments are infrastructure issues that don't warrant paper discussion.\n\n---\n\n## Recommendations (Priority-Ordered)\n\n### 1. [HIGH] Add Checkpoint Sweep Figure to Appendix\n\n**28 experiments** of val/test sweep data are unreferenced. A dual-panel figure (4B + 8B, val + test curves) would:\n- Visually confirm the \"<1pp checkpoint selection noise\" claim (currently text-only)\n- Demonstrate val-test monotonicity (or lack thereof)\n- Show training dynamics differ across seeds\n- Use existing data — no new experiments needed\n\n**Suggested: App Figure \"Checkpoint Selection Sensitivity\" with 4 subplots (4B-val, 4B-test, 8B-val, 8B-test), each showing training step vs accuracy.**\n\nData available: 6 val + 2 test checkpoints for 4B-s42; 7 val + 8 test for 8B-s42; 5 val + 5 test for 8B-s123.\n\n### 2. [LOW] Mention Seq-Length Consistency Across Checkpoints\n\ncls8b-s42-ckpt1000-test-seq2048-ablation (82.83%) is within <1pp of cls8b-s42-ckpt3600-seq2048-ablation (83.04%). A one-sentence note in the seq-length ablation paragraph would strengthen the robustness claim.\n\n### 3. [LOW] DeepSeek CWM s123 Epoch Comparison\n\ndeepseek-cwm-repo-s123-eval-1epoch (75.45%) provides a cross-seed data point for CWM epoch selection. The paper discusses CWM epoch selection for s42 only (val-selected 56.70% vs epoch-3 61.49%). Adding the s123 1-epoch data could either corroborate or complicate this analysis. Evaluate before including.\n\n---\n\n## Coverage Statistics\n\n| Paper Section | Experiments Referenced | % of Total |\n|--------------|----------------------|------------|\n| Table 1 (func-level) | 24 | 18.2% |\n| Table 2 (scaling) | 8 | 6.1% |\n| Table 3 (repo-level) | 26 | 19.7% |\n| Table 4 (taxonomy) | (derived from above) | — |\n| §5.2 equivalence | 3 | 2.3% |\n| §5.3 analysis | 4 | 3.0% |\n| App: ablation/control | 11 | 8.3% |\n| App: per-mutation | 3 | 2.3% |\n| App: TRAJ DeepSeek 6-seed | 3 | 2.3% |\n| App: threats | 3 | 2.3% |\n| App: few-shot | 1 | 0.8% |\n| **Subtotal referenced** | **88** | **66.7%** |\n| Val/test sweep (unused) | 28 | 21.2% |\n| Training/intermediate | 16 | 12.1% |\n\n**Conclusion: The paper already references 88/132 (67%) of success experiments. The remaining 33% are split between val/test sweep data (useful for a supplementary figure) and training infrastructure (not citable). All negative results with scientific value are already discussed.**\n"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T08:02:19.989622+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/supplementary_completeness_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T08:02:19.989776+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'completed', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'completed', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'in_progress', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'completed', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'completed', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'in_progress', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T08:02:19.989954+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T08:02:19.990079+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "supplementary_completeness_audit",
  "type": "report",
  "description": "Audit of 132 success experiments vs paper citations: 88 referenced, 28 val/test sweep data points as potential supplementary figure, 16 training/intermediate. All negative results already covered. Main recommendation: checkpoint sweep figure for appendix.",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/supplementary_completeness_audit.md",
  "tags": "['paper', 'audit', 'supplementary', 'completeness']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "supplementary_completeness_audit",
    "type": "report",
    "description": "Audit of 132 success experiments vs paper citations: 88 referenced, 28 val/test sweep data points as potential supplementary figure, 16 training/intermediate. All negative results already covered. Main recommendation: checkpoint sweep figure for appendix.",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/supplementary_completeness_audit.md",
    "tags": "['paper', 'audit', 'supplementary', 'completeness']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T08:02:19.990224+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_7ea081\", \"name\": \"supplementary_completeness_audit\", \"type\": \"report\", \"description\": \"Audit of 132 success experiments vs paper citations: 88 referenced, 28 val/test sweep data points as potential supplementary figure, 16 training/intermediate. All negative results already covered. Main recommendation: checkpoint sweep figure for appendix.\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/supplementary_completeness_audit.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T08:02:08.058899+00:00\", \"tags\": [\"paper\", \"audit\", \"supplementary\", \"completeness\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T08:02:19.990354+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'completed', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'completed', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'completed', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Extract all 132 success experiments from registry', 'status': 'completed', 'activeForm': 'Extracting registry experiments (agent running)'}, {'content': 'Scan paper tex files for referenced data/numbers', 'status': 'completed', 'activeForm': 'Scanning paper files (agent running)'}, {'content': 'Cross-reference experiments vs paper citations', 'status': 'completed', 'activeForm': 'Cross-referencing experiments with paper'}, {'content': 'Review 7 negative experiments for paper value', 'status': 'completed', 'activeForm': 'Reviewing negative experiments'}, {'content': 'Write supplementary_completeness_audit.md', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'completed', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T08:02:19.990504+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_supplementary-completeness_20260521T075031",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-21T08:02:19.990665+00:00_

审计完成。`artifacts/supplementary_completeness_audit.md` 已注册。

核心发现：

- **88/132 (67%)** 实验已在论文中引用
- **28 个 val/test sweep 实验**是主要遗漏——可做一张 appendix checkpoint sweep 图，视觉化支撑 "<1pp checkpoint selection noise" 的声明
- **16 个**是训练/中间产物，无需引用
- **所有有科学价值的 negative 结果**已在论文中覆盖（P2P regression、majority voting 失败、re-repair 失败、4B seed123 不稳定）

唯一的 HIGH 优先级建议：用现有的 28 个 sweep 数据点画一张 checkpoint selection sensitivity 图加入 appendix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_supplementary-completeness_20260521T075031"
}
```

</details>

---
