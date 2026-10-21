# code d141 conditional decomp span fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_code_d141_conditional_decomp_span_fix_20260518T141657.jsonl`
- **Structured JSON:** [`012b330cd5c7f369fb45.json`](../../sessions/01/012b330cd5c7f369fb45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-18T14:18:20.156887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T14:18:20.157250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T14:18:20.157450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/analysis_d141_conditional_decomp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/analysis_d141_conditional_decomp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T14:18:20.157780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"D141 Task 2: Conditional Success Decomposition\\nDecomposes LP selection effectiveness into 4 buckets based on:\\n- Condition 1 (Non-degenerate): at least 2 samples have different entity F1\\n- Condition 2 (LP discriminative): within-instance LP range > median LP range\\n\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nimport os\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nOUT_DIR = os.path.join(BASE, \\\"output/d141_conditional_decomp\\\")\\nos.makedirs(OUT_DIR, exist_ok=True)\\n\\nDATASETS = {\\n    \\\"SciERC\\\": os.path.join(BASE, \\\"output/exp_012_rerun_1024/samples.jsonl\\\"),\\n    \\\"CoNLL\\\": os.path.join(BASE, \\\"output/exp_002_conll_n16_r1024/samples.jsonl\\\"),\\n    \\\"FewNERD\\\": os.path.join(BASE, \\\"output/exp_027_fewnerd_n16/samples.jsonl\\\"),\\n}\\n\\n\\ndef entity_f1(pred_entities, gold_entities):\\n    pred_set = {(e[\\\"text\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"text\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    tp = len(pred_set & gold_set)\\n    fp = len(pred_set - gold_set)\\n    fn = len(gold_set - pred_set)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / (tp + fp)\\n    r = tp / (tp + fn)\\n    return 2 * p * r / (p + r)\\n\\n\\ndef load_instances(path):\\n    instances = []\\n    with open(path) as f:\\n        for line in f:\\n            inst = json.loads(line)\\n            gold_ents = inst[\\\"gold\\\"].get(\\\"entities\\\", [])\\n            if len(gold_ents) == 0:\\n                continue\\n\\n            samples = inst[\\\"samples\\\"][:8]\\n            greedy = inst.get(\\\"greedy\\\")\\n            logprobs = inst.get(\\\"logprobs\\\", [])[:8]\\n\\n            sample_f1s = [entity_f1(s.get(\\\"entities\\\", []), gold_ents) for s in samples]\\n            greedy_f1 = entity_f1(greedy.get(\\\"entities\\\", []), gold_ents) if greedy else 0.0\\n\\n            lp_ran
…[truncated 7407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T14:18:20.157994+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && sed -i 's/(e\\[\"text\"\\], e\\[\"type\"\\])/(e[\"start\"], e[\"end\"], e[\"type\"])/g' analysis_d141_conditional_decomp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && sed -i 's/(e\\[\"text\"\\], e\\[\"type\"\\])/(e[\"start\"], e[\"end\"], e[\"type\"])/g' analysis_d141_conditional_decomp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T14:18:20.158155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T14:18:20.158296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -35 /root/autodl-tmp/struct_self_consist_ie/analysis_d141_conditional_decomp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -35 /root/autodl-tmp/struct_self_consist_ie/analysis_d141_conditional_decomp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T14:18:20.158447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"D141 Task 2: Conditional Success Decomposition\\nDecomposes LP selection effectiveness into 4 buckets based on:\\n- Condition 1 (Non-degenerate): at least 2 samples have different entity F1\\n- Condition 2 (LP discriminative): within-instance LP range > median LP range\\n\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nimport os\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nOUT_DIR = os.path.join(BASE, \\\"output/d141_conditional_decomp\\\")\\nos.makedirs(OUT_DIR, exist_ok=True)\\n\\nDATASETS = {\\n    \\\"SciERC\\\": os.path.join(BASE, \\\"output/exp_012_rerun_1024/samples.jsonl\\\"),\\n    \\\"CoNLL\\\": os.path.join(BASE, \\\"output/exp_002_conll_n16_r1024/samples.jsonl\\\"),\\n    \\\"FewNERD\\\": os.path.join(BASE, \\\"output/exp_027_fewnerd_n16/samples.jsonl\\\"),\\n}\\n\\n\\ndef entity_f1(pred_entities, gold_entities):\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    tp = len(pred_set & gold_set)\\n    fp = len(pred_set - gold_set)\\n    fn = len(gold_set - pred_set)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / (tp + fp)\\n    r = tp / (tp + fn)\\n    return 2 * p * r / (p + r)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T14:18:20.158594+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie/ && python analysis_d141_conditional_decomp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie/ && python analysis_d141_conditional_decomp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T14:18:20.158742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading SciERC from /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl...\\n  529 instances (after gold-empty filter)\\n  Median LP range: 0.040121\\nLoading CoNLL from /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl...\\n  2756 instances (after gold-empty filter)\\n  Median LP range: 0.062012\\nLoading FewNERD from /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl...\\n  4351 instances (after gold-empty filter)\\n  Median LP range: 0.066996\\n\\nResults saved to /root/autodl-tmp/struct_self_consist_ie/output/d141_conditional_decomp/\\n\\n=== TABLES ===\\n\\n--- SciERC (N=529, median LP range=0.040121) ---\\nBucket               N      %   Greedy   LP_sel    Delta                 95% CI\\nFavorable          227  42.9%   0.6333   0.6585  +0.0252       [0.0034, 0.0476]\\nCond1-only         208  39.3%   0.6632   0.6546  -0.0086      [-0.0330, 0.0162]\\nCond2-only          37   7.0%   0.4434   0.4254  -0.0180      [-0.0541, 0.0000]\\nUnfavorable         57  10.8%   0.7461   0.7461  +0.0000       [0.0000, 0.0000]\\n\\n--- CoNLL (N=2756, median LP range=0.062012) ---\\nBucket               N      %   Greedy   LP_sel    Delta                 95% CI\\nFavorable          841  30.5%   0.8679   0.8491  -0.0188     [-0.0293, -0.0085]\\nCond1-only         318  11.5%   0.8441   0.8239  -0.0202      [-0.0431, 0.0017]\\nCond2-only         537  19.5%   0.8887   0.8887  +0.0000       [0.0000, 0.0000]\\nUnfavorable       1060  38.5%   0.9661   0.9661  +0.0000       [0.0000, 0.0000]\\n\\n--- FewNERD (N=4351, median LP range=0.066996) ---\\nBucket               N      %   Greedy   LP_sel    Delta                 95% CI\\nFavorable         2064  47.4%   0.7829   0.7898  +0.0069       [0.0005, 0.0135]\\nCond1-only        1659  38.1%   0.7548   0.7821  +0.0274       [0.0182, 0.0371]\\nCond2-only         111   2.5%   0.1171   0.1141  -0.003
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T14:18:20.158906+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d141_v2_fix",
  "description": "Create output directory for results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d141_v2_fix",
    "description": "Create output directory for results"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T14:18:20.159028+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T14:18:20.159176+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d141_v2_fix/d141_conditional_decomp_span_matching_results.md",
  "content": "# D141 Conditional Success Decomposition — Span Matching (Fixed)\n\n**Date**: 2026-05-18\n**Fix**: Restored `entity_f1` to span matching `(start, end, type)` — previously incorrectly changed to text matching `(text, type)`.\n\n## Methodology\n\nFor each test instance with N=8 samples:\n- **Condition 1 (Non-degenerate)**: at least 2 samples have different entity-level F1\n- **Condition 2 (LP discriminative)**: within-instance LP range > median LP range\n\nFour buckets: Favorable (C1+C2), Cond1-only (C1 only), Cond2-only (C2 only), Unfavorable (neither).\n\nAll F1 values are macro-averaged (mean of per-instance F1). Delta = LP_sel - Greedy.\n\nEvaluation: **strict span matching** `(start, end, type)` — consistent with main table and entity_merge analysis.\n\n## SciERC (N=529, median LP range=0.040121)\n\n| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |\n|--------|--------|---|-----------|-------|-------|--------|\n| Favorable | 227 | 42.9 | 0.6333 | 0.6585 | +0.0252 | [0.0034, 0.0476] |\n| Cond1-only | 208 | 39.3 | 0.6632 | 0.6546 | -0.0086 | [-0.0330, 0.0162] |\n| Cond2-only | 37 | 7.0 | 0.4434 | 0.4254 | -0.0180 | [-0.0541, 0.0000] |\n| Unfavorable | 57 | 10.8 | 0.7461 | 0.7461 | +0.0000 | [0.0000, 0.0000] |\n\n## CoNLL (N=2756, median LP range=0.062012)\n\n| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |\n|--------|--------|---|-----------|-------|-------|--------|\n| Favorable | 841 | 30.5 | 0.8679 | 0.8491 | -0.0188 | [-0.0293, -0.0085] |\n| Cond1-only | 318 | 11.5 | 0.8441 | 0.8239 | -0.0202 | [-0.0431, 0.0017] |\n| Cond2-only | 537 | 19.5 | 0.8887 | 0.8887 | +0.0000 | [0.0000, 0.0000] |\n| Unfavorable | 1060 | 38.5 | 0.9661 | 0.9661 | +0.0000 | [0.0000, 0.0000] |\n\n## FewNERD (N=4351, median LP range=0.066996)\n\n| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |\n|--------|--------|---|-----------|-------|-------|--------|\n| Favorable | 2064 | 47.4 | 0.7829 | 0.7898 | +0.0069 | [0.0005, 0.0135] |\n| Cond1-only | 1659 | 38.1 | 0.7548 | 0.7821 | +0.0274 | [0.0182, 0.0371] |\n| Cond2-only | 111 | 2.5 | 0.1171 | 0.1141 | -0.0030 | [-0.0090, 0.0000] |\n| Unfavorable | 517 | 11.9 | 0.7206 | 0.7171 | -0.0035 | [-0.0089, 0.0000] |\n\n## Summary\n\n**SciERC**:\n- Favorable: Delta=+0.0252 CI=[0.0034, 0.0476] (42.9%) — significant positive gain\n- Cond1-only: Delta=-0.0086 (39.3%)\n- Cond2-only: Delta=-0.0180 (7.0%)\n- Unfavorable: Delta=+0.0000 (10.8%)\n\n**CoNLL**:\n- Favorable: Delta=-0.0188 CI=[-0.0293, -0.0085] (30.5%) — LP selection hurts\n- Cond1-only: Delta=-0.0202 (11.5%)\n- Cond2-only: Delta=+0.0000 (19.5%)\n- Unfavorable: Delta=+0.0000 (38.5%)\n\n**FewNERD**:\n- Favorable: Delta=+0.0069 CI=[0.0005, 0.0135] (47.4%) — significant positive gain\n- Cond1-only: Delta=+0.0274 CI=[0.0182, 0.0371] (38.1%) — strong gain even without LP discriminativeness\n- Cond2-only: Delta=-0.0030 (2.5%)\n- Unfavorable: Delta=-0.0035 (11.9%)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d141_v2_fix/d141_conditional_decomp_span_matching_results.md",
    "content": "# D141 Conditional Success Decomposition — Span Matching (Fixed)\n\n**Date**: 2026-05-18\n**Fix**: Restored `entity_f1` to span matching `(start, end, type)` — previously incorrectly changed to text matching `(text, type)`.\n\n## Methodology\n\nFor each test instance with N=8 samples:\n- **Condition 1 (Non-degenerate)**: at least 2 samples have different entity-level F1\n- **Condition 2 (LP discriminative)**: within-instance LP range > median LP range\n\nFour buckets: Favorable (C1+C2), Cond1-only (C1 only), Cond2-only (C2 only), Unfavorable (neither).\n\nAll F1 values are macro-averaged (mean of per-instance F1). Delta = LP_sel - Greedy.\n\nEvaluation: **strict span matching** `(start, end, type)` — consistent with main table and entity_merge analysis.\n\n## SciERC (N=529, median LP range=0.040121)\n\n| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |\n|--------|--------|---|-----------|-------|-------|--------|\n| Favorable | 227 | 42.9 | 0.6333 | 0.6585 | +0.0252 | [0.0034, 0.0476] |\n| Cond1-only | 208 | 39.3 | 0.6632 | 0.6546 | -0.0086 | [-0.0330, 0.0162] |\n| Cond2-only | 37 | 7.0 | 0.4434 | 0.4254 | -0.0180 | [-0.0541, 0.0000] |\n| Unfavorable | 57 | 10.8 | 0.7461 | 0.7461 | +0.0000 | [0.0000, 0.0000] |\n\n## CoNLL (N=2756, median LP range=0.062012)\n\n| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |\n|--------|--------|---|-----------|-------|-------|--------|\n| Favorable | 841 | 30.5 | 0.8679 | 0.8491 | -0.0188 | [-0.0293, -0.0085] |\n| Cond1-only | 318 | 11.5 | 0.8441 | 0.8239 | -0.0202 | [-0.0431, 0.0017] |\n| Cond2-only | 537 | 19.5 | 0.8887 | 0.8887 | +0.0000 | [0.0000, 0.0000] |\n| Unfavorable | 1060 | 38.5 | 0.9661 | 0.9661 | +0.0000 | [0.0000, 0.0000] |\n\n## FewNERD (N=4351, median LP range=0.066996)\n\n| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta | 95% CI |\n|--------|--------|---|-----------|-------|-------|--------|\n| Favorable | 2064 | 47.4 | 0.7829 | 0.7898 | +0.0069 | [0.0005, 0.0135] |\n| Cond1-only | 1659 | 38.1 | 0.7548 | 0.7821 | +0.0274 | [0.0182, 0.0371] |\n| Cond2-only | 111 | 2.5 | 0.1171 | 0.1141 | -0.0030 | [-0.0090, 0.0000] |\n| Unfavorable | 517 | 11.9 | 0.7206 | 0.7171 | -0.0035 | [-0.0089, 0.0000] |\n\n## Summary\n\n**SciERC**:\n- Favorable: Delta=+0.0252 CI=[0.0034, 0.0476] (42.9%) — significant positive gain\n- Cond1-only: Delta=-0.0086 (39.3%)\n- Cond2-only: Delta=-0.0180 (7.0%)\n- Unfavorable: Delta=+0.0000 (10.8%)\n\n**CoNLL**:\n- Favorable: Delta=-0.0188 CI=[-0.0293, -0.0085] (30.5%) — LP selection hurts\n- Cond1-only: Delta=-0.0202 (11.5%)\n- Cond2-only: Delta=+0.0000 (19.5%)\n- Unfavorable: Delta=+0.0000 (38.5%)\n\n**FewNERD**:\n- Favorable: Delta=+0.0069 CI=[0.0005, 0.0135] (47.4%) — significant positive gain\n- Cond1-only: Delta=+0.0274 CI=[0.0182, 0.0371] (38.1%) — strong gain even without LP discriminativeness\n- Cond2-only: Delta=-0.0030 (2.5%)\n- Unfavorable: Delta=-0.0035 (11.9%)\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T14:18:20.159350+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d141_v2_fix/d141_conditional_decomp_span_matching_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T14:18:20.159508+00:00_

完成。修复内容和结果：

**修复**: `entity_f1` 从 `(text, type)` 改回 `(start, end, type)` span matching，其他部分（数据源、N=8 截断、gold filter）未改动。

**Span matching 结果要点**:

| Dataset | Favorable Delta | Favorable % | 趋势 |
|---------|----------------|-------------|------|
| SciERC | +0.0252 [0.0034, 0.0476] | 42.9% | LP selection 显著正向 |
| CoNLL | -0.0188 [-0.0293, -0.0085] | 30.5% | LP selection 显著负向 |
| FewNERD | +0.0069 [0.0005, 0.0135] | 47.4% | LP selection 显著正向 |

CoNLL 的 Favorable bucket 在 span matching 下 delta 为负，与 text matching 时表现不同。FewNERD Cond1-only bucket 出现 +0.0274 的强正向增益。

结果已写入 `artifacts/d141_v2_fix/d141_conditional_decomp_span_matching_results.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_d141_conditional_decomp_span_fix_20260518T141657"
}
```

</details>

---
