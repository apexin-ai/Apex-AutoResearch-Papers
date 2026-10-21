# research paper materials

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_research_paper-materials_20260512T172304.jsonl`
- **Structured JSON:** [`8e14a5b3691b41e6e704.json`](../../sessions/8e/8e14a5b3691b41e6e704.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-12T17:32:27.176788+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T17:32:27.177168+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T17:32:27.177345+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T17:32:27.177740+00:00_

Error: result (69,548 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T17:32:27.177936+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T17:32:27.178130+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\", \"content\": \"# Paper Framing — exec-sim-repair-verifier\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)\\n- Deadline: ARR May 25, 2026 (14 days from project start)\\n\\n## Core Claims (3 conditions)\\n\\n1. **Complexity-Dependent Reformulation Advantage**: Binary pass/fail classification and execution output generation (CWM-style) achieve equivalent accuracy on simple function-level code (4B: F1 diff 0.9pp), but classification scales better with model size (8B 3-seed mean accuracy gap=2.43pp; seed42: 2.81pp, cls 90.48% vs cwm 87.67%) and to repo-level complexity where CWM failure modes—token-budget exhaustion and string-value prediction errors—dominate. Zero-shot LLM-as-judge baselines (8B: 64.4%, 32B NF4: 71.7%) are far below fine-tuned 4B (88.4%), confirming fine-tuning necessity. (Validated function-level near-null + 8B scaling evidence; repo-level SWE-bench experiments in progress. Fallback: if repo-level also null, reframe to efficiency-equivalent accuracy—same F1 with 1-token vs N-token inference.)\\n\\n2. **Diagnostic Granularity At Equivalent Accuracy**: Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence test p=0.007, ±2pp margin; 5-seed pooled gap -0.40pp, 95% CI [-1.32, +0.52]) while providing actionable diagnostic information (which specific tests a patch fails). The per-test formulation gains diagnostic granularity without sacrificing accuracy—potentially enabling targeted re-repair and oracle-based test selection. (Evidence: 5-paired clustered bootstrap CI, 114 clusters, 10000 resamples. Paper must justify ±2pp margin: in code verification, 2pp variant-level difference is negligible given ICC=0.191/DEFF=3.97. Seeds 789
…[truncated 5157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T17:32:27.178298+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T17:32:27.178505+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ROADMAP.md\", \"content\": \"# exec-sim-repair-verifier — Research Dashboard\\n\\n> 最后更新: 2026-05-12 17:09 UTC | 更新原因: Reviewer WARNING: 修正8B表格混用accuracy/fail_f1，更新GPU状态和已完成任务\\n\\n## 核心方向\\nTask reformulation: execution simulation 从 generation → classification。**函数级两者等价（F1 diff <0.5pp, TOST p=0.007），核心假说转为 complexity-dependent advantage——repo-level 是决胜战场。** 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP，repo-level 训练中 + 论文写作已启动）\\n- **Story pillars**:\\n  - Pillar 1 (Complexity-Dependent Advantage): ⏳ repo-level CLS 训练中，CWM 待确认状态；函数级 null result + 8B scaling gap=2.43pp 已确认\\n  - Pillar 2 (Function-level Equivalence): ✅ TOST 等价 (gap=-0.45pp, p=0.007, ±2pp margin)\\n  - Pillar 3 (Oracle Frontier): ✅ 模拟数据完成（MVP-A）+ block-corr-empirical 完成\\n  - Pillar 4 (Model-Size Scaling): ✅ 8B 3-seed 完成，accuracy gap=2.43pp mean\\n- **Paper Agent**: 已激活，Full Draft 模式，writing_plan.yaml 待审批\\n\\n## GPU 状态\\n\\n### seetacloud-westd-4x5090 (4× RTX 5090)\\n| GPU | 实验 | 状态 |\\n|-----|------|------|\\n| cuda:0 | 空闲（per-test-precision-recall 已完成） | ⚪ 待分配 |\\n| cuda:1 | 空闲（block-corr-empirical 已完成） | ⚪ 待分配 |\\n| cuda:2 | repo-level-cls-v3 (PID 69782) | 🟢 训练中 |\\n| cuda:3 | repo-level-cwm-v3 (?) | ⚠️ 待确认 |\\n\\n### home-1x5090 (1× RTX 5090)\\n| GPU | 实验 | 状态 |\\n|-----|------|------|\\n| cuda:0 | 空闲（per-test-majority-voting 已完成） | ⚪ 待分配 |\\n\\n## 已完成实验摘要\\n\\n### 4B Function-level (per-test)\\n| 实验 | Accuracy | Fail F1 | Seeds |\\n|------|----------|---------|-------|\\n| CLS (classification) | 87.5-88.1% | 87.6-89.1% | 5 seeds |\\n| CWM (generation) | 86.2-87.6% | 87.3-87.9% | 5 seeds |\\n| **Gap** | ~1.25pp | ~0.5-1.7pp | TOST equivalent |\\n\\n### 8B Scaling (accuracy, 已修正)\\n| 实验 | seed42 | seed123 | seed456 | Mean |\\n|------|--------|---------|---------|------|\\n| cls8b | 90.48% | 89.40% | 88.31% | 89.40% |\\n| cwm8b | 87.67% | 86.98%
…[truncated 3027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T17:32:27.178714+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract experiment metrics from registry",
  "prompt": "I need you to parse a large JSON registry file and extract structured experiment data.\n\nThe file is at: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nPlease:\n1. First probe the structure with bash (jq type, length, keys)\n2. Then extract ALL experiments that have status containing \"DONE\" (both DONE/success and DONE/negative)\n3. For each experiment, extract:\n   - exp_id\n   - title or description\n   - model (if available)\n   - seed\n   - status and conclusion\n   - ALL metrics (accuracy, fail_f1, pass_f1, precision, recall, training duration, any other metrics)\n   - tags or category info\n   - created_at / updated_at\n\nGroup them by category:\n- 4B function-level CLS experiments\n- 4B function-level CWM experiments  \n- 8B CLS experiments\n- 8B CWM experiments\n- Trajectory-level baseline\n- LLM-judge baseline\n- Oracle/statistical analysis\n- Per-test analysis (precision-recall, majority-voting, error-overlap)\n- Repo-level experiments\n- Any other experiments\n\nOutput the COMPLETE data for every experiment — do not summarize or abbreviate metrics. I need exact numbers. Format as structured text that I can use to build markdown tables.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract experiment metrics from registry",
    "prompt": "I need you to parse a large JSON registry file and extract structured experiment data.\n\nThe file is at: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nPlease:\n1. First probe the structure with bash (jq type, length, keys)\n2. Then extract ALL experiments that have status containing \"DONE\" (both DONE/success and DONE/negative)\n3. For each experiment, extract:\n   - exp_id\n   - title or description\n   - model (if available)\n   - seed\n   - status and conclusion\n   - ALL metrics (accuracy, fail_f1, pass_f1, precision, recall, training duration, any other metrics)\n   - tags or category info\n   - created_at / updated_at\n\nGroup them by category:\n- 4B function-level CLS experiments\n- 4B function-level CWM experiments  \n- 8B CLS experiments\n- 8B CWM experiments\n- Trajectory-level baseline\n- LLM-judge baseline\n- Oracle/statistical analysis\n- Per-test analysis (precision-recall, majority-voting, error-overlap)\n- Repo-level experiments\n- Any other experiments\n\nOutput the COMPLETE data for every experiment — do not summarize or abbreviate metrics. I need exact numbers. Format as structured text that I can use to build markdown tables.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T17:32:27.178930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt",
    "description": "Check file size"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T17:32:27.179065+00:00_

74168 /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T17:32:27.179224+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\nprint('Outer keys:', list(outer.keys()))\ninner = json.loads(outer['result'])\nprint('Inner type:', type(inner).__name__)\nif isinstance(inner, dict):\n    print('Inner keys:', list(inner.keys())[:20])\n    for k in list(inner.keys())[:3]:\n        print(f'  {k} type:', type(inner[k]).__name__)\nelif isinstance(inner, list):\n    print('Inner length:', len(inner))\n    if inner:\n        print('First item keys:', list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\n\"",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\nprint('Outer keys:', list(outer.keys()))\ninner = json.loads(outer['result'])\nprint('Inner type:', type(inner).__name__)\nif isinstance(inner, dict):\n    print('Inner keys:', list(inner.keys())[:20])\n    for k in list(inner.keys())[:3]:\n        print(f'  {k} type:', type(inner[k]).__name__)\nelif isinstance(inner, list):\n    print('Inner length:', len(inner))\n    if inner:\n        print('First item keys:', list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\n\"",
    "description": "Probe JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T17:32:27.179362+00:00_

Outer keys: ['result']
Inner type: dict
Inner keys: ['success', 'data', 'error', 'metadata']
  success type: bool
  data type: dict
  error type: NoneType

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T17:32:27.179501+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('data keys:', list(data.keys()))\nfor k in data:\n    v = data[k]\n    print(f'  {k}: type={type(v).__name__}', end='')\n    if isinstance(v, list):\n        print(f', len={len(v)}')\n    elif isinstance(v, dict):\n        print(f', keys={list(v.keys())[:5]}')\n    else:\n        print(f', value={v}')\n\"",
  "description": "Probe inner data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('data keys:', list(data.keys()))\nfor k in data:\n    v = data[k]\n    print(f'  {k}: type={type(v).__name__}', end='')\n    if isinstance(v, list):\n        print(f', len={len(v)}')\n    elif isinstance(v, dict):\n        print(f', keys={list(v.keys())[:5]}')\n    else:\n        print(f', value={v}')\n\"",
    "description": "Probe inner data structure"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T17:32:27.179627+00:00_

data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, keys=['repo-level-cwm-v3', 'repo-level-cls-v3', 'matched-seed-8b-predictions', 'cls8b-eval-seed123', 'cls8b-eval-seed42']
  count: type=int, value=42
  total: type=int, value=42
  baseline: type=NoneType, value=None

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T17:32:27.179754+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n# Show all experiment IDs and their status\nfor eid, exp in exps.items():\n    status = exp.get('status', 'N/A')\n    print(f'{eid}: status={status}')\n\"",
  "description": "List all experiments and their statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n# Show all experiment IDs and their status\nfor eid, exp in exps.items():\n    status = exp.get('status', 'N/A')\n    print(f'{eid}: status={status}')\n\"",
    "description": "List all experiments and their statuses"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T17:32:27.179904+00:00_

Total experiments: 42

repo-level-cwm-v3: status=DONE
repo-level-cls-v3: status=DONE
matched-seed-8b-predictions: status=PREPARING
cls8b-eval-seed123: status=PREPARING
cls8b-eval-seed42: status=PREPARING
repo-level-cls-v4: status=PREPARING
repo-level-cls-home: status=PREPARING
cwm-seed789: status=DONE
repo-level-cwm-v2: status=PREPARING
repo-level-cls-v2: status=PREPARING
cls8b-seed456: status=DONE
cwm8b-seed456: status=DONE
5-paired-clustered-bootstrap: status=DONE
repo-level-cwm: status=DONE
repo-level-cls: status=DONE
cwm-seed0: status=DONE
per-test-precision-recall: status=DONE
cwm-seed123: status=DONE
cwm-seed456: status=DONE
cls-seed0: status=DONE
cls-seed789: status=DONE
cls8b-seed123: status=DONE
cwm8b-seed123: status=DONE
traj-level-finetuned: status=DONE
traj-level-seed456: status=DONE
traj-level-seed789: status=DONE
traj-level-seed0: status=DONE
per-test-majority-voting: status=DONE
block-corr-empirical: status=DONE
model-size-scaling-cwm8b: status=DONE
model-size-scaling-cls8b: status=DONE
llm-judge-32b-zeroshot: status=DONE
llm-judge-8b-zeroshot: status=DONE
traj-level-seed123: status=DONE
oracle-f2p-stratified: status=DONE
trace-then-judge: status=DONE
mvp-b-train: status=DONE
multi-seed-core: status=DONE
cwm-baseline: status=DONE
mvp-a-oracle-sim: status=DONE
p2p-regression-rate: status=DONE
mvp-b-data-prep: status=DONE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T17:32:27.180053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# First, let's look at the full structure of one experiment to understand all fields\nfor eid, exp in list(exps.items())[:1]:\n    print(json.dumps(exp, indent=2))\n\" 2>&1 | head -80",
  "description": "Show full structure of one experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# First, let's look at the full structure of one experiment to understand all fields\nfor eid, exp in list(exps.items())[:1]:\n    print(json.dumps(exp, indent=2))\n\" 2>&1 | head -80",
    "description": "Show full structure of one experiment"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T17:32:27.180234+00:00_

{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-12T16:30:59.064Z",
  "updated_at": "2026-05-12T17:22:48.589Z",
  "hypothesis": "Repo-level CWM (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator \u4fee\u590d\u540e v3\u3002\u4e0e cls-v3 \u914d\u5bf9\u9a8c\u8bc1 complexity gap\u3002",
  "notes": "v3 \u6839\u56e0\u786e\u8ba4\uff1a\u6839\u5206\u533a\u78c1\u76d8\u6ee1(89%, 27G/30G)\u5bfc\u81f4 SIGKILL\uff0c\u975e RAM OOM\u3002\u7cfb\u7edf RAM 754G \u7a7a\u95f2 621G\u3002\u5df2\u4fee\u590d\uff1a/root/.cache \u79fb\u81f3\u6570\u636e\u76d8\uff0c\u6839\u5206\u533a\u964d\u81f3 64%\u3002\u8bad\u7ec3\u81f3 step 3/6633 \u540e\u88ab\u6740\u3002",
  "reproduce": {
    "finished_at": "2026-05-12T17:09:20.159Z"
  },
  "failure_reason": "EXIT_CODE=137 (SIGKILL \u2014 OOM killer or manual kill)",
  "completed_at": "2026-05-12T17:09:22.135Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-12T17:09:24.124724+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed",
      "notes": "v3 WeightedDataCollator \u4fee\u590d\u5df2\u751f\u6548\u3002PID 69888 \u5728 cuda:3 \u4e0a\u6b63\u5e38\u8bad\u7ec3\uff0cstep 3/6633 at ~10.7s/it\uff08\u622a\u81f3 17:03\uff09\u3002\u9884\u8ba1\u603b\u8bad\u7ec3\u65f6\u95f4 ~19.7h\u3002"
    }
  },
  "spec": {
    "command": "bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py'",
    "server": "westd-48478",
    "gpu_id": "cuda:3",
    "data_path": "/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/",
    "data_count": 70000,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 42,
    "notes": "Director \u786e\u8ba4\u6b63\u5e38\u8fd0\u884c, \u4e4b\u524d SIGKILL \u68c0\u6d4b\u4e3a\u8bef\u62a5\u3002\u9884\u8ba1 CWM ~12:40 UTC \u5b8c\u6210"
  },
  "conclusion": "failed"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-12T17:32:27.180383+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Print full JSON for ALL DONE experiments\nfor eid, exp in exps.items():\n    if 'DONE' in exp.get('status', ''):\n        print('='*80)\n        print(f'EXP_ID: {eid}')\n        print(json.dumps(exp, indent=2, ensure_ascii=False))\n        print()\n\" 2>&1",
  "description": "Extract all DONE experiments with full details",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Print full JSON for ALL DONE experiments\nfor eid, exp in exps.items():\n    if 'DONE' in exp.get('status', ''):\n        print('='*80)\n        print(f'EXP_ID: {eid}')\n        print(json.dumps(exp, indent=2, ensure_ascii=False))\n        print()\n\" 2>&1",
    "description": "Extract all DONE experiments with full details",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T17:32:27.180526+00:00_

&lt;persisted-output>
Output too large (73.6KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt

Preview (first 2KB):
================================================================================
EXP_ID: repo-level-cwm-v3
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-12T16:30:59.064Z",
  "updated_at": "2026-05-12T17:22:48.589Z",
  "hypothesis": "Repo-level CWM (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator 修复后 v3。与 cls-v3 配对验证 complexity gap。",
  "notes": "v3 根因确认：根分区磁盘满(89%, 27G/30G)导致 SIGKILL，非 RAM OOM。系统 RAM 754G 空闲 621G。已修复：/root/.cache 移至数据盘，根分区降至 64%。训练至 step 3/6633 后被杀。",
  "reproduce": {
    "finished_at": "2026-05-12T17:09:20.159Z"
  },
  "failure_reason": "EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)",
  "completed_at": "2026-05-12T17:09:22.135Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-12T17:09:24.124724+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed",
      "notes": "v3 WeightedDataCollator 修复已生效。PID 69888 在 cuda:3 上正常训练，step 3/6633 at ~10.7s/it（截至 17:03）。预计总训练时间 ~19.7h。"
    }
  },
  "spec": {
    "command": "bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py'",
    "server": "westd-48478",
    "gpu_id": "cuda:3",
    "data_path": "/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/",
    "data_count": 70000,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 42,
    "notes": "Director 确认正常运行, 之前 SIGKILL 检测为误报。预计 CWM ~12:40 UTC 完成"
  },
  "conclusion": "failed"
}

================================================================================
EXP_ID: repo-level-cls-v3
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-12T16:30:58
…[truncated 204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-12T17:32:27.180684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T17:32:27.180969+00:00_

1	================================================================================
2	EXP_ID: repo-level-cwm-v3
3	{
4	  "status": "DONE",
5	  "retry_count": 1,
6	  "created_at": "2026-05-12T16:30:59.064Z",
7	  "updated_at": "2026-05-12T17:22:48.589Z",
8	  "hypothesis": "Repo-level CWM (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator 修复后 v3。与 cls-v3 配对验证 complexity gap。",
9	  "notes": "v3 根因确认：根分区磁盘满(89%, 27G/30G)导致 SIGKILL，非 RAM OOM。系统 RAM 754G 空闲 621G。已修复：/root/.cache 移至数据盘，根分区降至 64%。训练至 step 3/6633 后被杀。",
10	  "reproduce": {
11	    "finished_at": "2026-05-12T17:09:20.159Z"
12	  },
13	  "failure_reason": "EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)",
14	  "completed_at": "2026-05-12T17:09:22.135Z",
15	  "extra": {
16	    "hook_events": [
17	      {
18	        "event": "on_failed",
19	        "action": "agent",
20	        "ts": "2026-05-12T17:09:24.124724+00:00"
21	      }
22	    ],
23	    "previous_failure": {
24	      "conclusion": "failed",
25	      "notes": "v3 WeightedDataCollator 修复已生效。PID 69888 在 cuda:3 上正常训练，step 3/6633 at ~10.7s/it（截至 17:03）。预计总训练时间 ~19.7h。"
26	    }
27	  },
28	  "spec": {
29	    "command": "bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py'",
30	    "server": "westd-48478",
31	    "gpu_id": "cuda:3",
32	    "data_path": "/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/",
33	    "data_count": 70000,
34	    "model_name": "Qwen/Qwen3-4B",
35	    "seed": 42,
36	    "notes": "Director 确认正常运行, 之前 SIGKILL 检测为误报。预计 CWM ~12:40 UTC 完成"
37	  },
38	  "conclusion": "failed"
39	}
40	
41	================================================================================
42	EXP_ID: repo-level-cls-v3
43	{
44	  "status": "DONE",
45	  "retry_count": 1,
46	  "created_at": "2026-05-12T16:30:58.016Z",
47	  "updated_at": "2026-05-12T17:22:47.581Z",
48	  "hypothesis": "Repo-level CLS (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator 修复后 v3。验证 complex
…[truncated 19892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-12T17:32:27.181174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T17:32:27.181416+00:00_

500	    "bucket_11plus_acc": 87.12
501	  },
502	  "notes": "扩展诊断分析完成 (eval_pertest_diagnostic.py)。新增发现：114 个 problems 中 48 个 (42.1%) 完美预测；median problem fail-F1=94.12%；return_value 最易 (F1=98.6%), off_by_one 最难 (F1=80.8%)；worst problems: MBPP/397 (40%), HumanEval/130 (46%)。脚本和结果保存在 home:/home/sonny/exec-sim-repair-verifier/eval_pertest_diag.json。"
503	}
504	
505	================================================================================
506	EXP_ID: cwm-seed123
507	{
508	  "status": "DONE",
509	  "retry_count": 0,
510	  "created_at": "2026-05-12T11:24:58.500Z",
511	  "updated_at": "2026-05-12T13:15:21.097Z",
512	  "hypothesis": "补充 4B CWM seed=123，与 cwm-baseline (seed=42, 87.51%) 对比确认 4B cls-cwm gap ~0.9pp 的稳定性，同时为 \"scaling widens gap\" 叙事提供更强 evidence",
513	  "spec": {
514	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --seed 123 --no_wandb --device cuda:0 && python3 eval_cwm_baseline.py --checkpoint_dir checkpoints_cwm_seed123/best --device cuda:0\"",
515	    "server": "seetacloud-westd-4x5090",
516	    "gpu": "cuda:2",
517	    "pid": 39006,
518	    "log_path": "~/runs/exec-sim-repair-verifier/cwm-seed123.log",
519	    "submitted_at": "2026-05-12T11:49:35.477Z",
520	    "submitted_via": "submit_training_job",
521	    "backend": "tmux",
522	    "account": "root",
523	    "data_path": "/home/sonny/exec-sim-repair-verifier/data/",
524	    "data_count": 15290,
525	    "model_name": "Qwen/Qwen3-4B",
526	    "seed": 123,
527	    "metrics": {
528	      "overall_accuracy": 87.2,
529	      "pass_f1": 86.95,
530	      "fail_f1": 87.44,
531	      "exact_match_rate": 84.44,
532	      "majority_baseline_accuracy": 51.75,
533	      "accuracy_vs_baseline_gap_pp": 35.45,
534	      "test_set_size": 1890,
535	      "unparseable_predictions": 0
536	    },
5
…[truncated 20372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-12T17:32:27.181583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
  "offset": "1000",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
    "offset": "1000",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T17:32:27.181872+00:00_

1000	    "eval_loss_epoch2": 0.0885,
1001	    "eval_loss_epoch3": 0.1011,
1002	    "train_runtime_sec": 4071.3
1003	  },
1004	  "conclusion": "success",
1005	  "completed_at": "2026-05-12T10:21:57.297Z"
1006	}
1007	
1008	================================================================================
1009	EXP_ID: per-test-majority-voting
1010	{
1011	  "status": "DONE",
1012	  "retry_count": 0,
1013	  "created_at": "2026-05-12T08:18:14.827Z",
1014	  "updated_at": "2026-05-12T10:06:09.994Z",
1015	  "spec": {
1016	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 eval_majority_voting.py --base_model_path /root/.cache/huggingface/hub/Qwen/Qwen3-4B --checkpoint_path checkpoints/best --data_dir data/ --output eval_majority_voting.json --K 3 --temperature 0.7 --gpu 0\"",
1017	    "server": "seetacloud-westd-4x5090",
1018	    "gpu": [
1019	      "cuda:2"
1020	    ],
1021	    "pid": "21710",
1022	    "log_path": "~/runs/exec-sim-repair-verifier/per-test-majority-voting.log",
1023	    "submitted_at": "2026-05-12T09:22:45.956Z",
1024	    "submitted_via": "submit_training_job",
1025	    "backend": "tmux",
1026	    "account": "root",
1027	    "data_path": "/home/sonny/exec-sim-repair-verifier/data/test.jsonl",
1028	    "data_count": 1890,
1029	    "model_name": "Qwen/Qwen3-4B + LoRA",
1030	    "seed": 42,
1031	    "checkpoint_source": "/home/sonny/exec-sim-repair-verifier/checkpoints/best/",
1032	    "checkpoint_path": "/home/sonny/exec-sim-repair-verifier/checkpoints/best/",
1033	    "wall_clock_seconds": 643.2,
1034	    "gpu_hours": 0.18
1035	  },
1036	  "hypothesis": "Per-test majority voting (K=3, temperature=0.7) with fine-tuned 4B classification model 能否通过 self-consistency 提升 single-pass 87.5% accuracy",
1037	  "reproduce": {
1038	    "finished_at": "2026-05-12T09:25:13.934Z"
1039	  },
1040	  "extra": {
1041	    "hook_events": [
1
…[truncated 20640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T17:32:27.182060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
  "offset": "1500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/bd2f2ueow.txt",
    "offset": "1500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T17:32:27.182252+00:00_

1500	    "command": "bash -c \"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints/best/ --output eval_results.json\"",
1501	    "server": "home-1x5090",
1502	    "gpu": [
1503	      "cuda:0"
1504	    ],
1505	    "pid": "2102798",
1506	    "log_path": "~/runs/exec-sim-repair-verifier/mvp-b-train.log",
1507	    "submitted_at": "2026-05-11T20:06:48.617Z",
1508	    "submitted_via": "submit_training_job",
1509	    "backend": "tmux",
1510	    "account": "sonny",
1511	    "wall_clock_seconds": 4384.0,
1512	    "gpu_hours": 1.22
1513	  },
1514	  "notes": "OOM at step 15 (2nd attempt). Root cause: cross_entropy logits fp32 = 9.4GB + model 26GB > 32GB VRAM. Fix: bs 8→2, grad_accum 4→16, effective bs unchanged at 32. Retry count: 2.",
1515	  "conclusion": "success",
1516	  "metrics": {
1517	    "overall_accuracy": 0.875,
1518	    "pass_f1": 0.871,
1519	    "fail_f1": 0.879,
1520	    "pass_precision": 0.9324,
1521	    "pass_recall": 0.818,
1522	    "fail_precision": 0.8275,
1523	    "fail_recall": 0.9364,
1524	    "majority_baseline": 0.52,
1525	    "accuracy_vs_majority_gap": 0.355
1526	  },
1527	  "checkpoint_path": "/home/sonny/exec-sim-repair-verifier/checkpoints/best/",
1528	  "completed_at": "2026-05-11T21:19:52.606Z"
1529	}
1530	
1531	================================================================================
1532	EXP_ID: multi-seed-core
1533	{
1534	  "status": "DONE",
1535	  "retry_count": 0,
1536	  "created_at": "2026-05-11T22:31:56.650Z",
1537	  "updated_at": "2026-05-12T04:44:24.731Z",
1538	  "hypothesis": "Classification verifier 在 3 seeds 下稳定达到 ~87% accuracy/F1，CWM ≈ classification 的 null result robust",
1539	  "spec": {
1540	    "command": "bash -c \"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model
…[truncated 9770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T17:32:27.182423+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Count DONE experiments and check for any non-DONE\ndone = [eid for eid, e in exps.items() if e.get('status') == 'DONE']\nnot_done = [eid for eid, e in exps.items() if e.get('status') != 'DONE']\nprint(f'DONE: {len(done)}')\nprint(f'Not DONE: {len(not_done)} -> {not_done}')\n\n# Count conclusions\nfrom collections import Counter\nconclusions = Counter(e.get('conclusion', 'N/A') for eid, e in exps.items() if e.get('status') == 'DONE')\nprint(f'Conclusions: {dict(conclusions)}')\n\"",
  "description": "Count DONE experiments and conclusions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/42bb523e-e25e-46a3-926d-a6758cf800fb/tool-results/mcp-agent-ml-research-read_registry-1778606598209.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Count DONE experiments and check for any non-DONE\ndone = [eid for eid, e in exps.items() if e.get('status') == 'DONE']\nnot_done = [eid for eid, e in exps.items() if e.get('status') != 'DONE']\nprint(f'DONE: {len(done)}')\nprint(f'Not DONE: {len(not_done)} -> {not_done}')\n\n# Count conclusions\nfrom collections import Counter\nconclusions = Counter(e.get('conclusion', 'N/A') for eid, e in exps.items() if e.get('status') == 'DONE')\nprint(f'Conclusions: {dict(conclusions)}')\n\"",
    "description": "Count DONE experiments and conclusions"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T17:32:27.182557+00:00_

DONE: 35
Not DONE: 7 -> ['matched-seed-8b-predictions', 'cls8b-eval-seed123', 'cls8b-eval-seed42', 'repo-level-cls-v4', 'repo-level-cls-home', 'repo-level-cwm-v2', 'repo-level-cls-v2']
Conclusions: {'failed': 5, 'success': 27, 'negative': 3}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T17:32:27.182916+00:00_

Now I have all the data. Let me compile the complete structured output.

Here is the complete extracted experiment data from all 35 DONE experiments, grouped by category:

---

## CATEGORY 1: 4B Function-Level CLS Experiments

### mvp-b-train (seed=42, initial pilot)
- **exp_id:** mvp-b-train
- **hypothesis:** Qwen3-4B LoRA on function-level (code, test) -> pass/fail, target per-class F1 >65%, accuracy > majority+10pp
- **model:** Qwen/Qwen3-4B
- **seed:** 42
- **status:** DONE | **conclusion:** success
- **created_at:** 2026-05-11T19:24:04.462Z | **updated_at:** 2026-05-12T04:44:41.807Z | **completed_at:** 2026-05-11T21:19:52.606Z
- **metrics:**
  - overall_accuracy: 0.875 (87.5%)
  - pass_f1: 0.871 (87.1%)
  - fail_f1: 0.879 (87.9%)
  - pass_precision: 0.9324 (93.24%)
  - pass_recall: 0.818 (81.8%)
  - fail_precision: 0.8275 (82.75%)
  - fail_recall: 0.9364 (93.64%)
  - majority_baseline: 0.52 (52%)
  - accuracy_vs_majority_gap: 0.355 (35.5pp)
- **wall_clock_seconds:** 4384.0 | **gpu_hours:** 1.22

### multi-seed-core (seeds=42,123,456)
- **exp_id:** multi-seed-core
- **hypothesis:** Classification verifier stable ~87% accuracy/F1 across 3 seeds, CWM approx classification null result robust
- **model:** Qwen/Qwen3-4B
- **seeds:** 42, 123, 456
- **status:** DONE | **conclusion:** success
- **created_at:** 2026-05-11T22:31:56.650Z | **updated_at:** 2026-05-12T04:44:24.731Z | **completed_at:** 2026-05-12T04:44:24.731Z
- **metrics:**
  - seed42: accuracy=87.83, pass_f1=88.06, fail_f1=87.59, pass_precision=89.45, pass_recall=86.71, fail_precision=86.20, fail_recall=89.04
  - seed123: accuracy=89.52, pass_f1=89.64, fail_f1=89.40, pass_precision=91.76, pass_recall=87.63, fail_precision=87.34, fail_recall=91.56
  - seed456: accuracy=87.88, pass_f1=87.53, fail_f1=88.21, pass_precision=93.60, pass_recall=82.21, fail_precision=83.12, fail_recall=93.97
  - mean: accuracy=88.41, pass_f1=88.41, fail_f1=88.40
  - std: accuracy=0.96, pass_f1=1.10, fail_f1=0.92
- **wall_clock_seco
…[truncated 24759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T17:32:27.183221+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_materials.md",
  "content": "# Paper Materials — exec-sim-repair-verifier\n\n> 生成时间: 2026-05-12 | 基于 registry 中 35 个 DONE 实验\n\n---\n\n## 1. 结构化指标表格\n\n### 1.1 4B Function-Level: CLS vs CWM (5 seeds each)\n\n**Classification (CLS) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | multi-seed-core | 87.83 | 87.59 | 88.06 | 86.20 | 89.04 | 89.45 | 86.71 | 17298s (3-seed batch) |\n| 123 | multi-seed-core | 89.52 | 89.40 | 89.64 | 87.34 | 91.56 | 91.76 | 87.63 | (same batch) |\n| 456 | multi-seed-core | 87.88 | 88.21 | 87.53 | 83.12 | 93.97 | 93.60 | 82.21 | (same batch) |\n| 789 | cls-seed789 | 89.00 | 89.10 | 88.90 | 85.20 | 93.40 | 93.30 | 84.90 | 3849s |\n| 0 | cls-seed0 | 87.94 | 88.08 | 87.79 | 84.20 | 92.32 | 92.13 | 83.84 | 4977s |\n| **Mean** | | **88.43** | **88.48** | **88.38** | **85.21** | **92.06** | **92.05** | **85.06** | |\n| **Std** | | **0.74** | **0.67** | **0.83** | | | | | |\n\n**Code World Model (CWM) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | cwm-baseline | 87.51 | 87.71 | 87.31 | 83.53 | 92.32 | 92.06 | 83.03 | 84.02 | 3439s |\n| 123 | cwm-seed123 | 87.20 | 87.44 | 86.95 | — | — | — | — | 84.44 | 5096s |\n| 456 | cwm-seed456 | 86.98 | 87.29 | 86.66 | 82.52 | 92.65 | 92.26 | 81.70 | 84.02 | 3440s |\n| 789 | cwm-seed789 | 86.67 | 86.60 | 86.74 | 84.09 | 89.25 | 89.37 | 84.25 | 83.97 | 5158s |\n| 0 | cwm-seed0 | 87.57 | 87.93 | 87.18 | 82.71 | 93.86 | 93.45 | 81.70 | 84.29 | 3586s |\n| **Mean** | | **87.19** | **87.39** | **86.97** | **83.21** | **92.02** | **91.79** | **82.67** | **84.15** | |\n| **Std** | | **0.38** | **0.52** | **0.27** | | | | | | |\n\n**4B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 87.83 | 87.51 | +0.32 |\n| 123 | 89.52 | 87.20 | +2.32 |\n| 456 | 87.88 | 86.98 | +0.90 |\n| 789 | 89.00 | 86.67 | +2.33 |\n| 0 | 87.94 | 87.57 | +0.37 |\n| **Mean** | **88.43** | **87.19** | **+1.25** |\n\n### 1.2 8B Function-Level: CLS vs CWM (3 seeds each)\n\n**Classification (CLS) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | model-size-scaling-cls8b | 90.48 | 90.06 | 90.86 | 90.76 | 89.36 | 90.22 | 91.51 | 5614s |\n| 123 | cls8b-seed123 | 89.40 | 89.20 | 89.50 | 87.50 | 90.90 | 91.20 | 87.90 | 5666s |\n| 456 | cls8b-seed456 | 88.31 | 88.41 | 88.20 | 84.72 | 92.43 | 92.29 | 84.46 | 5481s |\n| **Mean** | | **89.40** | **89.22** | **89.52** | **87.66** | **90.90** | **91.24** | **87.96** | |\n\n**Code World Model (CWM) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | model-size-scaling-cwm8b | 87.67 | 87.77 | 87.57 | 84.19 | 91.67 | 91.53 | 83.95 | 84.39 | 5570s |\n| 123 | cwm8b-seed123 | 86.98 | 87.13 | 86.83 | — | — | — | — | 84.13 | 5948s |\n| 456 | cwm8b-seed456 | 86.24 | 86.51 | 85.96 | 82.09 | 91.45 | 91.08 | 81.39 | 82.80 | 6071s |\n| **Mean** | | **86.96** | **87.14** | **86.79** | **83.14** | **91.56** | **91.31** | **82.67** | **83.77** | |\n\n**8B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 90.48 | 87.67 | +2.81 |\n| 123 | 89.40 | 86.98 | +2.42 |\n| 456 | 88.31 | 86.24 | +2.07 |\n| **Mean** | **89.40** | **86.96** | **+2.43** |\n\n**Scaling Summary: CLS-CWM Gap Widens with Model Size**\n\n| Model Size | CLS Mean Acc | CWM Mean Acc | Gap (pp) | Seeds |\n|------------|-------------|-------------|----------|-------|\n| 4B | 88.43 | 87.19 | +1.25 | 5 |\n| 8B | 89.40 | 86.96 | +2.43 | 3 |\n| Gap widening | | | +1.18 | |\n\n### 1.3 Trajectory-Level Baseline (5 seeds, Qwen3-4B)\n\n| Seed | Exp ID | Accuracy | Unresolved F1 | Resolved F1 | Consistency |\n|------|--------|----------|---------------|-------------|-------------|\n| 42 | traj-level-finetuned | 85.66 | 87.50 | 83.18 | 79.94% |\n| 123 | traj-level-seed123 | 85.47 | 87.00 | 83.52 | 78.59% |\n| 456 | traj-level-seed456 | 87.40 | 88.70 | 85.80 | 78.80% |\n| 789 | traj-level-seed789 | 87.31 | 88.27 | 86.17 | 76.74% |\n| 0 | traj-level-seed0 | 85.66 | 87.37 | 83.41 | 79.55% |\n| **Mean** | | **86.30** | **87.77** | **84.42** | **78.72%** |\n\n### 1.4 LLM-Judge Zero-Shot Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec |\n|-------|----------|---------|---------|-----------|----------|-----------|----------|\n| Qwen3-8B zero-shot | 64.40 | 72.20 | 50.50 | 57.90 | 95.80 | 90.00 | 35.10 |\n| Qwen3-32B NF4 zero-shot | 71.69 | 75.91 | 65.68 | 64.40 | 92.43 | 88.12 | 52.35 |\n| Fine-tuned 4B CLS (ref) | 88.43 | 88.48 | 88.38 | 85.21 | 92.06 | 92.05 | 85.06 |\n\nFine-tuning advantage: +24.0pp over 8B zero-shot, +16.7pp over 32B zero-shot.\n\n### 1.5 CLS vs Trajectory — Variant-Level Equivalence (5-Paired Clustered Bootstrap)\n\n| Metric | Value |\n|--------|-------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp |\n| 95% CI | [−1.71, +0.84] |\n| Pooled p-value (gap ≠ 0) | 0.499 |\n| TOST p-value (±2pp margin) | 0.0071 |\n| TOST conclusion | **Equivalent** |\n| ICC (intra-cluster correlation) | 0.191 |\n| Design effect (DEFF) | 3.97 |\n| n_variants | 523 |\n| n_clusters | 114 |\n\nPer-seed variant-level gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29\n\n### 1.6 Oracle / Statistical Analysis\n\n**Oracle F2P Stratification (oracle-f2p-stratified)**\n\n| T bucket | % of instances | Block-corr advantage (pp) | Contribution to overall |\n|----------|---------------|--------------------------|------------------------|\n| T=1 | 68.7% | −0.09 | negligible |\n| T=2 | 19.1% | 31.69 | 55.3% |\n| T=3–5 | 7.1% | 40.74 | — |\n| T≥6 | 5.1% | 40.06 | — |\n| **Overall** | 100% | **10.93** | |\n\n**P2P Regression Rate (p2p-regression-rate)**\n- Mean regression rate: 1.04%, median: 0%\n- 77% of incorrect patches break zero P2P tests\n- Falls in <5% zone → P2P signal weak for this dataset\n- Conclusion: NEGATIVE — P2P regression detection provides minimal value at current rates\n\n**Block Correlation (block-corr-empirical)**\n\n| Metric | Value |\n|--------|-------|\n| ICC | 0.191 |\n| ICC p-value | 0.000 |\n| Design effect | 3.97 |\n| Overall error rate | 12.49% |\n| All-correct problems (observed) | 46 |\n| All-correct problems (expected i.i.d.) | 16.35 |\n| Ratio (observed/expected) | 2.81× |\n| Error std observed | 0.153 |\n| Error std expected i.i.d. | 0.081 |\n\n**Matched-Seed Error Overlap (from paper_framing.md)**\n- CLS dominant error: miss bugs (FN) — 75.5% of CLS errors\n- CWM dominant error: false alarms (FP) — 83.1% of CWM errors\n- Oracle ensemble accuracy: 90.63%\n- Complementary error patterns → formulation diversity as verification strategy\n\n### 1.7 Per-Test Diagnostic Analysis\n\n**Precision-Recall by Mutation Type (per-test-precision-recall)**\n\n| Mutation Type | Accuracy | Notes |\n|---------------|----------|-------|\n| return_value | 97.26% | Easiest (F1=98.6%) |\n| operator_swap | — | — |\n| boundary_removal | — | — |\n| variable_swap | — | — |\n| off_by_one | 82.56% | Hardest (F1=80.8%) |\n\n- 114 problems, 48 (42.1%) perfect prediction\n- Median problem fail-F1: 94.12%\n- Worst problems: MBPP/397 (40%), HumanEval/130 (46%)\n- Bucket 6–10 tests: 96.3% accuracy; 11+ tests: 87.1%\n\n**Majority Voting K=3 (per-test-majority-voting) — NEGATIVE**\n\n| Metric | Greedy | Majority Vote K=3 | Delta |\n|--------|--------|-------------------|-------|\n| Accuracy | 87.51 | 86.83 | −0.69 |\n| Fail F1 | 87.86 | 87.29 | −0.57 |\n| Pass F1 | 87.15 | 86.33 | −0.82 |\n\n- Unanimous rate: 93.3%\n- Net flips: −13 (28 correct→wrong, 15 wrong→correct)\n- Conclusion: Self-consistency hurts; model is well-calibrated at greedy decoding\n\n### 1.8 Dataset Statistics (mvp-b-data-prep)\n\n| Metric | Value |\n|--------|-------|\n| Total samples | 19,076 |\n| HumanEval | 5,575 |\n| MBPP | 13,501 |\n| Class balance | pass 52.0% / fail 48.0% |\n| Train/Val/Test | 15,290 / 1,896 / 1,890 |\n| Majority baseline | 52.0% |\n| Label verification | All verified by execution (5s timeout) |\n\n### 1.9 Training Hyperparameters (representative)\n\n| Param | 4B CLS/CWM | 8B CLS/CWM |\n|-------|-----------|-----------|\n| Base model | Qwen/Qwen3-4B | Qwen/Qwen3-8B |\n| Method | LoRA | LoRA |\n| Batch size | 2 | 2 |\n| Grad accumulation | 16 | 16 |\n| Learning rate | 2e-4 | 2e-4 |\n| Epochs | 3 | 3 |\n| Trainable params | ~0.19% | ~0.19% (15.3M/8.2B) |\n| GPU hours per seed | ~1.0–1.5h | ~1.5–1.7h |\n\n---\n\n## 2. Paper Framing 证据审查\n\n### Claim 1: Complexity-Dependent Reformulation Advantage\n\n> CLS and CWM equivalent on simple function-level code; CLS scales better with model size and to repo-level complexity.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| 4B function-level CLS≈CWM | ✅ 充足 | 5 seeds each | Gap=+1.25pp mean, std overlap |\n| 8B scaling gap widens | ✅ 充足 | 3 seeds each | Gap=+2.43pp mean (2.07–2.81 range) |\n| LLM-judge far below fine-tuned | ✅ 充足 | 2 baselines | 8B: 64.4%, 32B: 71.7% vs fine-tuned 4B: 88.4% |\n| Repo-level CLS > CWM | ❌ 缺失 | repo-level-cls-v3/cwm-v3 均 SIGKILL | 训练中，预计 14–20h |\n| CWM failure modes (token exhaustion, string errors) | ⚠️ 间接 | EM rate ~84% | 需要 repo-level 数据直接展示 failure cases |\n\n**统计检验缺口：**\n- ❌ 4B CLS vs CWM 没有正式的 paired bootstrap 检验（只有 5-seed mean gap）\n- ❌ 8B CLS vs CWM 没有正式的 paired bootstrap 检验\n- ❌ 8B scaling gap widening 的显著性检验（4B gap vs 8B gap interaction test）\n- ⚠️ 需要 effect size (Cohen's d 或 similar) for CLS-CWM comparison\n\n**判定：** 函数级证据方向正确但统计力度不足（5 seeds 下 paired t-test power 低）。Repo-level 是此 claim 的 **关键缺失**，必须等训练完成。\n\n### Claim 2: Diagnostic Granularity At Equivalent Accuracy\n\n> Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring while providing diagnostic info.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| Variant-level equivalence | ✅ 充足 | 5-paired-clustered-bootstrap | TOST p=0.007, gap=−0.45pp, CI [−1.71, +0.84] |\n| Cluster structure accounted for | ✅ 充足 | block-corr-empirical | ICC=0.191, DEFF=3.97 |\n| Diagnostic granularity value | ✅ 部分 | per-test-precision-recall | Per-mutation, per-problem breakdown |\n| Downstream re-repair benefit | ❌ 缺失 | — | 未实验，需决策是否做 |\n\n**统计检验：** ✅ 完整 — TOST 正式等价检验 + clustered bootstrap + ICC/DEFF + 多 seed 验证。\n\n**注意事项：**\n- Seeds 789/0 使用 4-bit quantization，论文需说明\n- ±2pp TOST margin 的合理性论证需要（论文已规划用 ICC/DEFF justification）\n\n**判定：** 此 claim 证据最充分，可直接写入论文。\n\n### Claim 3: Accuracy-Utility Frontier Characterization\n\n> Per-test advantage depends on test distribution; concentrates in multi-F2P instances; P2P signal weak.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| T distribution sensitivity | ✅ 充足 | oracle-f2p-stratified | T=1 无优势, T≥2 优势 30–41pp |\n| P2P regression rare (<5%) | ✅ 充足 | p2p-regression-rate | 1.04% mean, negative finding |\n| Block correlation amplifies advantage | ✅ 充足 | block-corr-empirical | ICC=0.191, observed/expected ratio 2.81× |\n| Error complementarity | ✅ 充足 | matched-seed error overlap | CLS FN-heavy, CWM FP-heavy, oracle 90.63% |\n| Majority voting ineffective | ✅ 充足 | per-test-majority-voting | K=3 hurts by −0.69pp (negative) |\n| Oracle frontier full characterization | ✅ 部分 | mvp-a-oracle-sim | Simulated; needs real model verification |\n\n**统计检验：** ⚠️ 部分 — oracle 分析基于模拟数据（假设 precision/recall），非实际模型。Block-corr 用真实模型验证过。\n\n**判定：** 证据丰富，但 oracle frontier 是模拟而非实际模型验证——需在论文中明确说明。\n\n---\n\n## 3. 缺失清单\n\n### 3.1 缺失的实验/数据\n\n| 优先级 | 缺失项 | 依赖 | 备注 |\n|--------|--------|------|------|\n| **P0** | Repo-level CLS 训练结果 | v4 训练完成 (~14–20h) | Claim 1 核心依赖 |\n| **P0** | Repo-level CWM 训练结果 | v4 训练完成 | Claim 1 核心依赖 |\n| **P0** | Repo-level CLS vs CWM paired bootstrap | 两个训练都完成后 | 决定论文走 Main 还是 Plan B |\n| **P1** | 4B CLS vs CWM paired bootstrap (5 seeds) | 数据已有，需跑统计 | Claim 1 函数级统计完善 |\n| **P1** | 8B CLS vs CWM paired bootstrap (3 seeds) | 数据已有，需跑统计 | Claim 1 scaling 统计完善 |\n| **P1** | Scaling interaction test (4B gap vs 8B gap) | 数据已有，需跑统计 | Gap widening 显著性 |\n| **P2** | CLS vs CWM effect size (Cohen's d) | 数据已有 | 补充统计报告 |\n| **P2** | Diagnostic re-repair experiment | 需新实验或决策 future work | Claim 2 downstream |\n| **P3** | Oracle frontier with real model (not simulation) | per-test-precision-recall 数据可用 | Claim 3 加强 |\n\n### 3.2 缺失的图表\n\n| Figure | 描述 | 数据来源 | 优先级 |\n|--------|------|----------|--------|\n| Fig 1 | **方法概览图**：CLS vs CWM formulation 对比示意 | 手绘/设计 | P0 |\n| Fig 2 | **主结果柱状图**：4B/8B CLS vs CWM accuracy + error bars | 1.1 + 1.2 表格 | P0 |\n| Fig 3 | **Scaling plot**：Model size (4B→8B) × Formulation (CLS/CWM) accuracy 折线图 | 1.1 + 1.2 | P0 |\n| Fig 4 | **CLS vs TRAJ 等价性**：paired difference forest plot 或 TOST 可视化 | 1.5 | P0 |\n| Fig 5 | **LLM-judge baseline 对比**：bar chart (8B-zs, 32B-zs, 4B-ft, 8B-ft) | 1.4 | P1 |\n| Fig 6 | **Oracle frontier**：resolve rate vs precision curves for different T | 1.6 oracle-sim | P1 |\n| Fig 7 | **F2P 分层分析**：per-test advantage by T bucket bar chart | 1.6 stratified | P1 |\n| Fig 8 | **Error complementarity**：CLS vs CWM error Venn/confusion 对比 | matched-seed overlap | P1 |\n| Fig 9 | **Block correlation**：observed vs expected i.i.d. error distribution | 1.6 block-corr | P2 |\n| Fig 10 | **Per-test precision-recall by mutation**：bar chart or radar | 1.7 | P2 |\n| Fig 11 | **Repo-level 结果**（待训练完成） | — | P0 (待数据) |\n\n### 3.3 Repo-Level 完成后需要的后续分析\n\n1. **Repo-level eval**: 在 SWE-bench Verified 子集上评估 CLS 和 CWM 模型\n2. **Paired bootstrap**: repo-level CLS vs CWM paired bootstrap CI + significance test (n≥200)\n3. **Go/No-Go 决策**: 按 ROADMAP D008 标准判定 — ≥3pp 全力推 Main, 1–3pp 评估, <1pp kill C1\n4. **CWM failure mode 分析**: 定性分析 repo-level CWM 预测失败的具体 case（token exhaustion, string mismatch）\n5. **Repo-level oracle frontier**: 用真实模型 precision/recall 重跑 oracle 分析\n6. **Repo-level 结果整合**: 更新 Fig 3 scaling plot 加入 repo-level 数据点\n7. **End-to-end re-ranking demo**（stretch）: 用 per-test classifier 做 candidate re-ranking, 衡量 resolve rate\n\n### 3.4 可立即执行的 CPU 任务（不需要 GPU/训练完成）\n\n1. ✅ 整理本文档（已完成）\n2. **P1**: 跑 4B CLS vs CWM 5-seed paired bootstrap 统计检验\n3. **P1**: 跑 8B CLS vs CWM 3-seed paired bootstrap 统计检验\n4. **P1**: 计算 scaling interaction effect\n5. **P1**: 计算 CLS vs CWM effect sizes\n6. **P0**: 画 Fig 2–10（数据均已就绪）\n7. **P0**: Paper Agent 继续写已完成 pillars 的章节\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "paper_materials.md",
    "content": "# Paper Materials — exec-sim-repair-verifier\n\n> 生成时间: 2026-05-12 | 基于 registry 中 35 个 DONE 实验\n\n---\n\n## 1. 结构化指标表格\n\n### 1.1 4B Function-Level: CLS vs CWM (5 seeds each)\n\n**Classification (CLS) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | multi-seed-core | 87.83 | 87.59 | 88.06 | 86.20 | 89.04 | 89.45 | 86.71 | 17298s (3-seed batch) |\n| 123 | multi-seed-core | 89.52 | 89.40 | 89.64 | 87.34 | 91.56 | 91.76 | 87.63 | (same batch) |\n| 456 | multi-seed-core | 87.88 | 88.21 | 87.53 | 83.12 | 93.97 | 93.60 | 82.21 | (same batch) |\n| 789 | cls-seed789 | 89.00 | 89.10 | 88.90 | 85.20 | 93.40 | 93.30 | 84.90 | 3849s |\n| 0 | cls-seed0 | 87.94 | 88.08 | 87.79 | 84.20 | 92.32 | 92.13 | 83.84 | 4977s |\n| **Mean** | | **88.43** | **88.48** | **88.38** | **85.21** | **92.06** | **92.05** | **85.06** | |\n| **Std** | | **0.74** | **0.67** | **0.83** | | | | | |\n\n**Code World Model (CWM) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | cwm-baseline | 87.51 | 87.71 | 87.31 | 83.53 | 92.32 | 92.06 | 83.03 | 84.02 | 3439s |\n| 123 | cwm-seed123 | 87.20 | 87.44 | 86.95 | — | — | — | — | 84.44 | 5096s |\n| 456 | cwm-seed456 | 86.98 | 87.29 | 86.66 | 82.52 | 92.65 | 92.26 | 81.70 | 84.02 | 3440s |\n| 789 | cwm-seed789 | 86.67 | 86.60 | 86.74 | 84.09 | 89.25 | 89.37 | 84.25 | 83.97 | 5158s |\n| 0 | cwm-seed0 | 87.57 | 87.93 | 87.18 | 82.71 | 93.86 | 93.45 | 81.70 | 84.29 | 3586s |\n| **Mean** | | **87.19** | **87.39** | **86.97** | **83.21** | **92.02** | **91.79** | **82.67** | **84.15** | |\n| **Std** | | **0.38** | **0.52** | **0.27** | | | | | | |\n\n**4B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 87.83 | 87.51 | +0.32 |\n| 123 | 89.52 | 87.20 | +2.32 |\n| 456 | 87.88 | 86.98 | +0.90 |\n| 789 | 89.00 | 86.67 | +2.33 |\n| 0 | 87.94 | 87.57 | +0.37 |\n| **Mean** | **88.43** | **87.19** | **+1.25** |\n\n### 1.2 8B Function-Level: CLS vs CWM (3 seeds each)\n\n**Classification (CLS) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | model-size-scaling-cls8b | 90.48 | 90.06 | 90.86 | 90.76 | 89.36 | 90.22 | 91.51 | 5614s |\n| 123 | cls8b-seed123 | 89.40 | 89.20 | 89.50 | 87.50 | 90.90 | 91.20 | 87.90 | 5666s |\n| 456 | cls8b-seed456 | 88.31 | 88.41 | 88.20 | 84.72 | 92.43 | 92.29 | 84.46 | 5481s |\n| **Mean** | | **89.40** | **89.22** | **89.52** | **87.66** | **90.90** | **91.24** | **87.96** | |\n\n**Code World Model (CWM) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | model-size-scaling-cwm8b | 87.67 | 87.77 | 87.57 | 84.19 | 91.67 | 91.53 | 83.95 | 84.39 | 5570s |\n| 123 | cwm8b-seed123 | 86.98 | 87.13 | 86.83 | — | — | — | — | 84.13 | 5948s |\n| 456 | cwm8b-seed456 | 86.24 | 86.51 | 85.96 | 82.09 | 91.45 | 91.08 | 81.39 | 82.80 | 6071s |\n| **Mean** | | **86.96** | **87.14** | **86.79** | **83.14** | **91.56** | **91.31** | **82.67** | **83.77** | |\n\n**8B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 90.48 | 87.67 | +2.81 |\n| 123 | 89.40 | 86.98 | +2.42 |\n| 456 | 88.31 | 86.24 | +2.07 |\n| **Mean** | **89.40** | **86.96** | **+2.43** |\n\n**Scaling Summary: CLS-CWM Gap Widens with Model Size**\n\n| Model Size | CLS Mean Acc | CWM Mean Acc | Gap (pp) | Seeds |\n|------------|-------------|-------------|----------|-------|\n| 4B | 88.43 | 87.19 | +1.25 | 5 |\n| 8B | 89.40 | 86.96 | +2.43 | 3 |\n| Gap widening | | | +1.18 | |\n\n### 1.3 Trajectory-Level Baseline (5 seeds, Qwen3-4B)\n\n| Seed | Exp ID | Accuracy | Unresolved F1 | Resolved F1 | Consistency |\n|------|--------|----------|---------------|-------------|-------------|\n| 42 | traj-level-finetuned | 85.66 | 87.50 | 83.18 | 79.94% |\n| 123 | traj-level-seed123 | 85.47 | 87.00 | 83.52 | 78.59% |\n| 456 | traj-level-seed456 | 87.40 | 88.70 | 85.80 | 78.80% |\n| 789 | traj-level-seed789 | 87.31 | 88.27 | 86.17 | 76.74% |\n| 0 | traj-level-seed0 | 85.66 | 87.37 | 83.41 | 79.55% |\n| **Mean** | | **86.30** | **87.77** | **84.42** | **78.72%** |\n\n### 1.4 LLM-Judge Zero-Shot Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec |\n|-------|----------|---------|---------|-----------|----------|-----------|----------|\n| Qwen3-8B zero-shot | 64.40 | 72.20 | 50.50 | 57.90 | 95.80 | 90.00 | 35.10 |\n| Qwen3-32B NF4 zero-shot | 71.69 | 75.91 | 65.68 | 64.40 | 92.43 | 88.12 | 52.35 |\n| Fine-tuned 4B CLS (ref) | 88.43 | 88.48 | 88.38 | 85.21 | 92.06 | 92.05 | 85.06 |\n\nFine-tuning advantage: +24.0pp over 8B zero-shot, +16.7pp over 32B zero-shot.\n\n### 1.5 CLS vs Trajectory — Variant-Level Equivalence (5-Paired Clustered Bootstrap)\n\n| Metric | Value |\n|--------|-------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp |\n| 95% CI | [−1.71, +0.84] |\n| Pooled p-value (gap ≠ 0) | 0.499 |\n| TOST p-value (±2pp margin) | 0.0071 |\n| TOST conclusion | **Equivalent** |\n| ICC (intra-cluster correlation) | 0.191 |\n| Design effect (DEFF) | 3.97 |\n| n_variants | 523 |\n| n_clusters | 114 |\n\nPer-seed variant-level gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29\n\n### 1.6 Oracle / Statistical Analysis\n\n**Oracle F2P Stratification (oracle-f2p-stratified)**\n\n| T bucket | % of instances | Block-corr advantage (pp) | Contribution to overall |\n|----------|---------------|--------------------------|------------------------|\n| T=1 | 68.7% | −0.09 | negligible |\n| T=2 | 19.1% | 31.69 | 55.3% |\n| T=3–5 | 7.1% | 40.74 | — |\n| T≥6 | 5.1% | 40.06 | — |\n| **Overall** | 100% | **10.93** | |\n\n**P2P Regression Rate (p2p-regression-rate)**\n- Mean regression rate: 1.04%, median: 0%\n- 77% of incorrect patches break zero P2P tests\n- Falls in <5% zone → P2P signal weak for this dataset\n- Conclusion: NEGATIVE — P2P regression detection provides minimal value at current rates\n\n**Block Correlation (block-corr-empirical)**\n\n| Metric | Value |\n|--------|-------|\n| ICC | 0.191 |\n| ICC p-value | 0.000 |\n| Design effect | 3.97 |\n| Overall error rate | 12.49% |\n| All-correct problems (observed) | 46 |\n| All-correct problems (expected i.i.d.) | 16.35 |\n| Ratio (observed/expected) | 2.81× |\n| Error std observed | 0.153 |\n| Error std expected i.i.d. | 0.081 |\n\n**Matched-Seed Error Overlap (from paper_framing.md)**\n- CLS dominant error: miss bugs (FN) — 75.5% of CLS errors\n- CWM dominant error: false alarms (FP) — 83.1% of CWM errors\n- Oracle ensemble accuracy: 90.63%\n- Complementary error patterns → formulation diversity as verification strategy\n\n### 1.7 Per-Test Diagnostic Analysis\n\n**Precision-Recall by Mutation Type (per-test-precision-recall)**\n\n| Mutation Type | Accuracy | Notes |\n|---------------|----------|-------|\n| return_value | 97.26% | Easiest (F1=98.6%) |\n| operator_swap | — | — |\n| boundary_removal | — | — |\n| variable_swap | — | — |\n| off_by_one | 82.56% | Hardest (F1=80.8%) |\n\n- 114 problems, 48 (42.1%) perfect prediction\n- Median problem fail-F1: 94.12%\n- Worst problems: MBPP/397 (40%), HumanEval/130 (46%)\n- Bucket 6–10 tests: 96.3% accuracy; 11+ tests: 87.1%\n\n**Majority Voting K=3 (per-test-majority-voting) — NEGATIVE**\n\n| Metric | Greedy | Majority Vote K=3 | Delta |\n|--------|--------|-------------------|-------|\n| Accuracy | 87.51 | 86.83 | −0.69 |\n| Fail F1 | 87.86 | 87.29 | −0.57 |\n| Pass F1 | 87.15 | 86.33 | −0.82 |\n\n- Unanimous rate: 93.3%\n- Net flips: −13 (28 correct→wrong, 15 wrong→correct)\n- Conclusion: Self-consistency hurts; model is well-calibrated at greedy decoding\n\n### 1.8 Dataset Statistics (mvp-b-data-prep)\n\n| Metric | Value |\n|--------|-------|\n| Total samples | 19,076 |\n| HumanEval | 5,575 |\n| MBPP | 13,501 |\n| Class balance | pass 52.0% / fail 48.0% |\n| Train/Val/Test | 15,290 / 1,896 / 1,890 |\n| Majority baseline | 52.0% |\n| Label verification | All verified by execution (5s timeout) |\n\n### 1.9 Training Hyperparameters (representative)\n\n| Param | 4B CLS/CWM | 8B CLS/CWM |\n|-------|-----------|-----------|\n| Base model | Qwen/Qwen3-4B | Qwen/Qwen3-8B |\n| Method | LoRA | LoRA |\n| Batch size | 2 | 2 |\n| Grad accumulation | 16 | 16 |\n| Learning rate | 2e-4 | 2e-4 |\n| Epochs | 3 | 3 |\n| Trainable params | ~0.19% | ~0.19% (15.3M/8.2B) |\n| GPU hours per seed | ~1.0–1.5h | ~1.5–1.7h |\n\n---\n\n## 2. Paper Framing 证据审查\n\n### Claim 1: Complexity-Dependent Reformulation Advantage\n\n> CLS and CWM equivalent on simple function-level code; CLS scales better with model size and to repo-level complexity.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| 4B function-level CLS≈CWM | ✅ 充足 | 5 seeds each | Gap=+1.25pp mean, std overlap |\n| 8B scaling gap widens | ✅ 充足 | 3 seeds each | Gap=+2.43pp mean (2.07–2.81 range) |\n| LLM-judge far below fine-tuned | ✅ 充足 | 2 baselines | 8B: 64.4%, 32B: 71.7% vs fine-tuned 4B: 88.4% |\n| Repo-level CLS > CWM | ❌ 缺失 | repo-level-cls-v3/cwm-v3 均 SIGKILL | 训练中，预计 14–20h |\n| CWM failure modes (token exhaustion, string errors) | ⚠️ 间接 | EM rate ~84% | 需要 repo-level 数据直接展示 failure cases |\n\n**统计检验缺口：**\n- ❌ 4B CLS vs CWM 没有正式的 paired bootstrap 检验（只有 5-seed mean gap）\n- ❌ 8B CLS vs CWM 没有正式的 paired bootstrap 检验\n- ❌ 8B scaling gap widening 的显著性检验（4B gap vs 8B gap interaction test）\n- ⚠️ 需要 effect size (Cohen's d 或 similar) for CLS-CWM comparison\n\n**判定：** 函数级证据方向正确但统计力度不足（5 seeds 下 paired t-test power 低）。Repo-level 是此 claim 的 **关键缺失**，必须等训练完成。\n\n### Claim 2: Diagnostic Granularity At Equivalent Accuracy\n\n> Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring while providing diagnostic info.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| Variant-level equivalence | ✅ 充足 | 5-paired-clustered-bootstrap | TOST p=0.007, gap=−0.45pp, CI [−1.71, +0.84] |\n| Cluster structure accounted for | ✅ 充足 | block-corr-empirical | ICC=0.191, DEFF=3.97 |\n| Diagnostic granularity value | ✅ 部分 | per-test-precision-recall | Per-mutation, per-problem breakdown |\n| Downstream re-repair benefit | ❌ 缺失 | — | 未实验，需决策是否做 |\n\n**统计检验：** ✅ 完整 — TOST 正式等价检验 + clustered bootstrap + ICC/DEFF + 多 seed 验证。\n\n**注意事项：**\n- Seeds 789/0 使用 4-bit quantization，论文需说明\n- ±2pp TOST margin 的合理性论证需要（论文已规划用 ICC/DEFF justification）\n\n**判定：** 此 claim 证据最充分，可直接写入论文。\n\n### Claim 3: Accuracy-Utility Frontier Characterization\n\n> Per-test advantage depends on test distribution; concentrates in multi-F2P instances; P2P signal weak.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| T distribution sensitivity | ✅ 充足 | oracle-f2p-stratified | T=1 无优势, T≥2 优势 30–41pp |\n| P2P regression rare (<5%) | ✅ 充足 | p2p-regression-rate | 1.04% mean, negative finding |\n| Block correlation amplifies advantage | ✅ 充足 | block-corr-empirical | ICC=0.191, observed/expected ratio 2.81× |\n| Error complementarity | ✅ 充足 | matched-seed error overlap | CLS FN-heavy, CWM FP-heavy, oracle 90.63% |\n| Majority voting ineffective | ✅ 充足 | per-test-majority-voting | K=3 hurts by −0.69pp (negative) |\n| Oracle frontier full characterization | ✅ 部分 | mvp-a-oracle-sim | Simulated; needs real model verification |\n\n**统计检验：** ⚠️ 部分 — oracle 分析基于模拟数据（假设 precision/recall），非实际模型。Block-corr 用真实模型验证过。\n\n**判定：** 证据丰富，但 oracle frontier 是模拟而非实际模型验证——需在论文中明确说明。\n\n---\n\n## 3. 缺失清单\n\n### 3.1 缺失的实验/数据\n\n| 优先级 | 缺失项 | 依赖 | 备注 |\n|--------|--------|------|------|\n| **P0** | Repo-level CLS 训练结果 | v4 训练完成 (~14–20h) | Claim 1 核心依赖 |\n| **P0** | Repo-level CWM 训练结果 | v4 训练完成 | Claim 1 核心依赖 |\n| **P0** | Repo-level CLS vs CWM paired bootstrap | 两个训练都完成后 | 决定论文走 Main 还是 Plan B |\n| **P1** | 4B CLS vs CWM paired bootstrap (5 seeds) | 数据已有，需跑统计 | Claim 1 函数级统计完善 |\n| **P1** | 8B CLS vs CWM paired bootstrap (3 seeds) | 数据已有，需跑统计 | Claim 1 scaling 统计完善 |\n| **P1** | Scaling interaction test (4B gap vs 8B gap) | 数据已有，需跑统计 | Gap widening 显著性 |\n| **P2** | CLS vs CWM effect size (Cohen's d) | 数据已有 | 补充统计报告 |\n| **P2** | Diagnostic re-repair experiment | 需新实验或决策 future work | Claim 2 downstream |\n| **P3** | Oracle frontier with real model (not simulation) | per-test-precision-recall 数据可用 | Claim 3 加强 |\n\n### 3.2 缺失的图表\n\n| Figure | 描述 | 数据来源 | 优先级 |\n|--------|------|----------|--------|\n| Fig 1 | **方法概览图**：CLS vs CWM formulation 对比示意 | 手绘/设计 | P0 |\n| Fig 2 | **主结果柱状图**：4B/8B CLS vs CWM accuracy + error bars | 1.1 + 1.2 表格 | P0 |\n| Fig 3 | **Scaling plot**：Model size (4B→8B) × Formulation (CLS/CWM) accuracy 折线图 | 1.1 + 1.2 | P0 |\n| Fig 4 | **CLS vs TRAJ 等价性**：paired difference forest plot 或 TOST 可视化 | 1.5 | P0 |\n| Fig 5 | **LLM-judge baseline 对比**：bar chart (8B-zs, 32B-zs, 4B-ft, 8B-ft) | 1.4 | P1 |\n| Fig 6 | **Oracle frontier**：resolve rate vs precision curves for different T | 1.6 oracle-sim | P1 |\n| Fig 7 | **F2P 分层分析**：per-test advantage by T bucket bar chart | 1.6 stratified | P1 |\n| Fig 8 | **Error complementarity**：CLS vs CWM error Venn/confusion 对比 | matched-seed overlap | P1 |\n| Fig 9 | **Block correlation**：observed vs expected i.i.d. error distribution | 1.6 block-corr | P2 |\n| Fig 10 | **Per-test precision-recall by mutation**：bar chart or radar | 1.7 | P2 |\n| Fig 11 | **Repo-level 结果**（待训练完成） | — | P0 (待数据) |\n\n### 3.3 Repo-Level 完成后需要的后续分析\n\n1. **Repo-level eval**: 在 SWE-bench Verified 子集上评估 CLS 和 CWM 模型\n2. **Paired bootstrap**: repo-level CLS vs CWM paired bootstrap CI + significance test (n≥200)\n3. **Go/No-Go 决策**: 按 ROADMAP D008 标准判定 — ≥3pp 全力推 Main, 1–3pp 评估, <1pp kill C1\n4. **CWM failure mode 分析**: 定性分析 repo-level CWM 预测失败的具体 case（token exhaustion, string mismatch）\n5. **Repo-level oracle frontier**: 用真实模型 precision/recall 重跑 oracle 分析\n6. **Repo-level 结果整合**: 更新 Fig 3 scaling plot 加入 repo-level 数据点\n7. **End-to-end re-ranking demo**（stretch）: 用 per-test classifier 做 candidate re-ranking, 衡量 resolve rate\n\n### 3.4 可立即执行的 CPU 任务（不需要 GPU/训练完成）\n\n1. ✅ 整理本文档（已完成）\n2. **P1**: 跑 4B CLS vs CWM 5-seed paired bootstrap 统计检验\n3. **P1**: 跑 8B CLS vs CWM 3-seed paired bootstrap 统计检验\n4. **P1**: 计算 scaling interaction effect\n5. **P1**: 计算 CLS vs CWM effect sizes\n6. **P0**: 画 Fig 2–10（数据均已就绪）\n7. **P0**: Paper Agent 继续写已完成 pillars 的章节\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T17:32:27.183551+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'paper_materials.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T17:32:27.183721+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T17:32:27.183879+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
build_cwm_data.py
build_data.py
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
eval_cwm_baseline.py
eval_majority_voting.py
experiment_plan.lock
experiment_plan.yaml
llm_judge_zeroshot.py
logs
memory.md
mvp_a_total_sim.py
paper_framing.md
registry.lock
registry.yaml
report.md
study_status.lock
task_context
train_cwm_baseline.py
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-12T17:32:27.184013+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T17:32:27.184136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T17:32:27.184290+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/paper_materials.md",
  "content": "# Paper Materials — exec-sim-repair-verifier\n\n> 生成时间: 2026-05-12 | 基于 registry 中 35 个 DONE 实验\n\n---\n\n## 1. 结构化指标表格\n\n### 1.1 4B Function-Level: CLS vs CWM (5 seeds each)\n\n**Classification (CLS) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | multi-seed-core | 87.83 | 87.59 | 88.06 | 86.20 | 89.04 | 89.45 | 86.71 | 17298s (3-seed batch) |\n| 123 | multi-seed-core | 89.52 | 89.40 | 89.64 | 87.34 | 91.56 | 91.76 | 87.63 | (same batch) |\n| 456 | multi-seed-core | 87.88 | 88.21 | 87.53 | 83.12 | 93.97 | 93.60 | 82.21 | (same batch) |\n| 789 | cls-seed789 | 89.00 | 89.10 | 88.90 | 85.20 | 93.40 | 93.30 | 84.90 | 3849s |\n| 0 | cls-seed0 | 87.94 | 88.08 | 87.79 | 84.20 | 92.32 | 92.13 | 83.84 | 4977s |\n| **Mean** | | **88.43** | **88.48** | **88.38** | **85.21** | **92.06** | **92.05** | **85.06** | |\n| **Std** | | **0.74** | **0.67** | **0.83** | | | | | |\n\n**Code World Model (CWM) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | cwm-baseline | 87.51 | 87.71 | 87.31 | 83.53 | 92.32 | 92.06 | 83.03 | 84.02 | 3439s |\n| 123 | cwm-seed123 | 87.20 | 87.44 | 86.95 | — | — | — | — | 84.44 | 5096s |\n| 456 | cwm-seed456 | 86.98 | 87.29 | 86.66 | 82.52 | 92.65 | 92.26 | 81.70 | 84.02 | 3440s |\n| 789 | cwm-seed789 | 86.67 | 86.60 | 86.74 | 84.09 | 89.25 | 89.37 | 84.25 | 83.97 | 5158s |\n| 0 | cwm-seed0 | 87.57 | 87.93 | 87.18 | 82.71 | 93.86 | 93.45 | 81.70 | 84.29 | 3586s |\n| **Mean** | | **87.19** | **87.39** | **86.97** | **83.21** | **92.02** | **91.79** | **82.67** | **84.15** | |\n| **Std** | | **0.38** | **0.52** | **0.27** | | | | | | |\n\n**4B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 87.83 | 87.51 | +0.32 |\n| 123 | 89.52 | 87.20 | +2.32 |\n| 456 | 87.88 | 86.98 | +0.90 |\n| 789 | 89.00 | 86.67 | +2.33 |\n| 0 | 87.94 | 87.57 | +0.37 |\n| **Mean** | **88.43** | **87.19** | **+1.25** |\n\n### 1.2 8B Function-Level: CLS vs CWM (3 seeds each)\n\n**Classification (CLS) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | model-size-scaling-cls8b | 90.48 | 90.06 | 90.86 | 90.76 | 89.36 | 90.22 | 91.51 | 5614s |\n| 123 | cls8b-seed123 | 89.40 | 89.20 | 89.50 | 87.50 | 90.90 | 91.20 | 87.90 | 5666s |\n| 456 | cls8b-seed456 | 88.31 | 88.41 | 88.20 | 84.72 | 92.43 | 92.29 | 84.46 | 5481s |\n| **Mean** | | **89.40** | **89.22** | **89.52** | **87.66** | **90.90** | **91.24** | **87.96** | |\n\n**Code World Model (CWM) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | model-size-scaling-cwm8b | 87.67 | 87.77 | 87.57 | 84.19 | 91.67 | 91.53 | 83.95 | 84.39 | 5570s |\n| 123 | cwm8b-seed123 | 86.98 | 87.13 | 86.83 | — | — | — | — | 84.13 | 5948s |\n| 456 | cwm8b-seed456 | 86.24 | 86.51 | 85.96 | 82.09 | 91.45 | 91.08 | 81.39 | 82.80 | 6071s |\n| **Mean** | | **86.96** | **87.14** | **86.79** | **83.14** | **91.56** | **91.31** | **82.67** | **83.77** | |\n\n**8B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 90.48 | 87.67 | +2.81 |\n| 123 | 89.40 | 86.98 | +2.42 |\n| 456 | 88.31 | 86.24 | +2.07 |\n| **Mean** | **89.40** | **86.96** | **+2.43** |\n\n**Scaling Summary: CLS-CWM Gap Widens with Model Size**\n\n| Model Size | CLS Mean Acc | CWM Mean Acc | Gap (pp) | Seeds |\n|------------|-------------|-------------|----------|-------|\n| 4B | 88.43 | 87.19 | +1.25 | 5 |\n| 8B | 89.40 | 86.96 | +2.43 | 3 |\n| Gap widening | | | +1.18 | |\n\n### 1.3 Trajectory-Level Baseline (5 seeds, Qwen3-4B)\n\n| Seed | Exp ID | Accuracy | Unresolved F1 | Resolved F1 | Consistency |\n|------|--------|----------|---------------|-------------|-------------|\n| 42 | traj-level-finetuned | 85.66 | 87.50 | 83.18 | 79.94% |\n| 123 | traj-level-seed123 | 85.47 | 87.00 | 83.52 | 78.59% |\n| 456 | traj-level-seed456 | 87.40 | 88.70 | 85.80 | 78.80% |\n| 789 | traj-level-seed789 | 87.31 | 88.27 | 86.17 | 76.74% |\n| 0 | traj-level-seed0 | 85.66 | 87.37 | 83.41 | 79.55% |\n| **Mean** | | **86.30** | **87.77** | **84.42** | **78.72%** |\n\n### 1.4 LLM-Judge Zero-Shot Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec |\n|-------|----------|---------|---------|-----------|----------|-----------|----------|\n| Qwen3-8B zero-shot | 64.40 | 72.20 | 50.50 | 57.90 | 95.80 | 90.00 | 35.10 |\n| Qwen3-32B NF4 zero-shot | 71.69 | 75.91 | 65.68 | 64.40 | 92.43 | 88.12 | 52.35 |\n| Fine-tuned 4B CLS (ref) | 88.43 | 88.48 | 88.38 | 85.21 | 92.06 | 92.05 | 85.06 |\n\nFine-tuning advantage: +24.0pp over 8B zero-shot, +16.7pp over 32B zero-shot.\n\n### 1.5 CLS vs Trajectory — Variant-Level Equivalence (5-Paired Clustered Bootstrap)\n\n| Metric | Value |\n|--------|-------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp |\n| 95% CI | [−1.71, +0.84] |\n| Pooled p-value (gap ≠ 0) | 0.499 |\n| TOST p-value (±2pp margin) | 0.0071 |\n| TOST conclusion | **Equivalent** |\n| ICC (intra-cluster correlation) | 0.191 |\n| Design effect (DEFF) | 3.97 |\n| n_variants | 523 |\n| n_clusters | 114 |\n\nPer-seed variant-level gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29\n\n### 1.6 Oracle / Statistical Analysis\n\n**Oracle F2P Stratification (oracle-f2p-stratified)**\n\n| T bucket | % of instances | Block-corr advantage (pp) | Contribution to overall |\n|----------|---------------|--------------------------|------------------------|\n| T=1 | 68.7% | −0.09 | negligible |\n| T=2 | 19.1% | 31.69 | 55.3% |\n| T=3–5 | 7.1% | 40.74 | — |\n| T≥6 | 5.1% | 40.06 | — |\n| **Overall** | 100% | **10.93** | |\n\n**P2P Regression Rate (p2p-regression-rate) — NEGATIVE**\n- Mean regression rate: 1.04%, median: 0%\n- 77% of incorrect patches break zero P2P tests\n- Falls in <5% zone → P2P signal weak for this dataset\n\n**Block Correlation (block-corr-empirical)**\n\n| Metric | Value |\n|--------|-------|\n| ICC | 0.191 |\n| ICC p-value | 0.000 |\n| Design effect | 3.97 |\n| Overall error rate | 12.49% |\n| All-correct problems (observed) | 46 |\n| All-correct problems (expected i.i.d.) | 16.35 |\n| Ratio (observed/expected) | 2.81× |\n| Error std observed | 0.153 |\n| Error std expected i.i.d. | 0.081 |\n\n**Matched-Seed Error Overlap**\n- CLS dominant error: miss bugs (FN) — 75.5% of CLS errors\n- CWM dominant error: false alarms (FP) — 83.1% of CWM errors\n- Oracle ensemble accuracy: 90.63%\n- Complementary error patterns → formulation diversity as verification strategy\n\n### 1.7 Per-Test Diagnostic Analysis\n\n**Precision-Recall by Mutation Type (per-test-precision-recall)**\n\n| Mutation Type | Accuracy | F1 |\n|---------------|----------|----|\n| return_value | 97.26% | 98.6% (easiest) |\n| off_by_one | 82.56% | 80.8% (hardest) |\n\n- 114 problems, 48 (42.1%) perfect prediction\n- Median problem fail-F1: 94.12%\n- Worst problems: MBPP/397 (40%), HumanEval/130 (46%)\n- Bucket 6–10 tests: 96.3% accuracy; 11+ tests: 87.1%\n\n**Majority Voting K=3 (per-test-majority-voting) — NEGATIVE**\n\n| Metric | Greedy | Majority Vote K=3 | Delta |\n|--------|--------|-------------------|-------|\n| Accuracy | 87.51 | 86.83 | −0.69 |\n| Fail F1 | 87.86 | 87.29 | −0.57 |\n| Pass F1 | 87.15 | 86.33 | −0.82 |\n\n- Unanimous rate: 93.3%\n- Net flips: −13 (28 correct→wrong, 15 wrong→correct)\n\n### 1.8 Dataset Statistics (mvp-b-data-prep)\n\n| Metric | Value |\n|--------|-------|\n| Total samples | 19,076 |\n| HumanEval | 5,575 |\n| MBPP | 13,501 |\n| Class balance | pass 52.0% / fail 48.0% |\n| Train/Val/Test | 15,290 / 1,896 / 1,890 |\n| Majority baseline | 52.0% |\n| Label verification | All verified by execution (5s timeout) |\n\n### 1.9 Training Hyperparameters\n\n| Param | 4B CLS/CWM | 8B CLS/CWM |\n|-------|-----------|-----------|\n| Base model | Qwen/Qwen3-4B | Qwen/Qwen3-8B |\n| Method | LoRA | LoRA |\n| Batch size | 2 | 2 |\n| Grad accumulation | 16 | 16 |\n| Learning rate | 2e-4 | 2e-4 |\n| Epochs | 3 | 3 |\n| Trainable params | ~0.19% | ~0.19% (15.3M/8.2B) |\n| GPU hours per seed | ~1.0–1.5h | ~1.5–1.7h |\n\n---\n\n## 2. Paper Framing 证据审查\n\n### Claim 1: Complexity-Dependent Reformulation Advantage\n\n> CLS and CWM equivalent on simple function-level code; CLS scales better with model size and to repo-level complexity.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| 4B function-level CLS≈CWM | ✅ 充足 | 5 seeds each | Gap=+1.25pp mean, std overlap |\n| 8B scaling gap widens | ✅ 充足 | 3 seeds each | Gap=+2.43pp mean (2.07–2.81) |\n| LLM-judge far below fine-tuned | ✅ 充足 | 2 baselines | 8B: 64.4%, 32B: 71.7% vs ft-4B: 88.4% |\n| Repo-level CLS > CWM | ❌ 缺失 | v3 均 SIGKILL | 训练中，预计 14–20h |\n| CWM failure modes 定性分析 | ⚠️ 间接 | EM rate ~84% | 需 repo-level 数据直接展示 |\n\n**统计检验缺口：**\n- ❌ 4B CLS vs CWM paired bootstrap 检验（5 seeds 数据已有，未跑）\n- ❌ 8B CLS vs CWM paired bootstrap 检验（3 seeds 数据已有，未跑）\n- ❌ Scaling interaction test（gap widening 显著性）\n- ⚠️ 需 effect size (Cohen's d)\n\n**判定：** 函数级证据方向正确但统计力度不足（5 seeds paired t-test power 低）。Repo-level 是核心缺失。\n\n### Claim 2: Diagnostic Granularity At Equivalent Accuracy\n\n> Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| Variant-level equivalence | ✅ 充足 | 5-paired-clustered-bootstrap | TOST p=0.007, gap=−0.45pp |\n| Cluster structure | ✅ 充足 | block-corr-empirical | ICC=0.191, DEFF=3.97 |\n| Diagnostic granularity | ✅ 部分 | per-test-precision-recall | Per-mutation breakdown |\n| Downstream re-repair | ❌ 缺失 | — | 未实验 |\n\n**统计检验：** ✅ 完整。\n\n**注意：** Seeds 789/0 使用 4-bit quantization，论文需说明。±2pp TOST margin 需 justification。\n\n**判定：** 证据最充分，可直接写入论文。\n\n### Claim 3: Accuracy-Utility Frontier Characterization\n\n> Per-test advantage depends on test distribution; concentrates in multi-F2P instances.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| T distribution sensitivity | ✅ 充足 | oracle-f2p-stratified | T=1 无优势, T≥2 +30–41pp |\n| P2P regression rare | ✅ 充足 | p2p-regression-rate | 1.04% mean (negative) |\n| Block correlation | ✅ 充足 | block-corr-empirical | ICC=0.191, ratio 2.81× |\n| Error complementarity | ✅ 充足 | matched-seed overlap | Oracle 90.63% |\n| Majority voting | ✅ 充足 | per-test-majority-voting | K=3 hurts −0.69pp (negative) |\n| Oracle frontier | ✅ 部分 | mvp-a-oracle-sim | 基于模拟，非真实模型 |\n\n**判定：** 证据丰富，但 oracle frontier 基于模拟——需论文明确说明。\n\n---\n\n## 3. 缺失清单\n\n### 3.1 缺失的实验/数据\n\n| 优先级 | 缺失项 | 依赖 | 备注 |\n|--------|--------|------|------|\n| **P0** | Repo-level CLS 训练结果 | v4 训练完成 (~14–20h) | Claim 1 核心 |\n| **P0** | Repo-level CWM 训练结果 | v4 训练完成 | Claim 1 核心 |\n| **P0** | Repo-level paired bootstrap | 两个训练完成后 | Go/No-Go 决策 |\n| **P1** | 4B CLS vs CWM paired bootstrap (5 seeds) | 数据已有 | 统计完善 |\n| **P1** | 8B CLS vs CWM paired bootstrap (3 seeds) | 数据已有 | 统计完善 |\n| **P1** | Scaling interaction test | 数据已有 | Gap widening 显著性 |\n| **P2** | CLS vs CWM effect size (Cohen's d) | 数据已有 | 补充统计 |\n| **P2** | Diagnostic re-repair experiment | 需新实验或 future work | Claim 2 downstream |\n| **P3** | Oracle frontier with real model | precision-recall 数据可用 | Claim 3 加强 |\n\n### 3.2 缺失的图表\n\n| Figure | 描述 | 数据来源 | 优先级 |\n|--------|------|----------|--------|\n| Fig 1 | 方法概览图：CLS vs CWM formulation 对比示意 | 手绘/设计 | P0 |\n| Fig 2 | 主结果柱状图：4B/8B CLS vs CWM accuracy + error bars | §1.1 + §1.2 | P0 |\n| Fig 3 | Scaling plot：Model size × Formulation accuracy 折线图 | §1.1 + §1.2 | P0 |\n| Fig 4 | CLS vs TRAJ 等价性：TOST 可视化 / forest plot | §1.5 | P0 |\n| Fig 5 | LLM-judge baseline 对比 bar chart | §1.4 | P1 |\n| Fig 6 | Oracle frontier：resolve rate vs precision curves | §1.6 oracle-sim | P1 |\n| Fig 7 | F2P 分层分析：per-test advantage by T bucket | §1.6 stratified | P1 |\n| Fig 8 | Error complementarity：CLS vs CWM 错误模式对比 | matched-seed overlap | P1 |\n| Fig 9 | Block correlation：observed vs expected error distribution | §1.6 block-corr | P2 |\n| Fig 10 | Per-test precision-recall by mutation type | §1.7 | P2 |\n| Fig 11 | Repo-level 结果（待训练完成） | — | P0 (blocked) |\n\n### 3.3 Repo-Level 完成后需要的后续分析\n\n1. Repo-level eval on SWE-bench Verified subset\n2. Paired bootstrap: CLS vs CWM (n≥200)\n3. Go/No-Go decision per ROADMAP D008\n4. CWM failure mode qualitative analysis (token exhaustion, string mismatch cases)\n5. Repo-level oracle frontier with real model precision/recall\n6. Update scaling plot with repo-level data point\n7. (Stretch) End-to-end re-ranking demo for resolve rate\n\n### 3.4 可立即执行的 CPU 任务\n\n| 任务 | 优先级 | 输入数据 |\n|------|--------|----------|\n| 4B CLS vs CWM 5-seed paired bootstrap | P1 | 已有 eval predictions |\n| 8B CLS vs CWM 3-seed paired bootstrap | P1 | 已有 eval predictions |\n| Scaling interaction effect | P1 | 已有 mean/std |\n| Cohen's d effect sizes | P2 | 已有 mean/std |\n| 画 Fig 2–10 | P0 | 本文档数据 |\n| Paper Agent 写已完成 pillars 章节 | P0 | paper_framing + 本文档 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/paper_materials.md",
    "content": "# Paper Materials — exec-sim-repair-verifier\n\n> 生成时间: 2026-05-12 | 基于 registry 中 35 个 DONE 实验\n\n---\n\n## 1. 结构化指标表格\n\n### 1.1 4B Function-Level: CLS vs CWM (5 seeds each)\n\n**Classification (CLS) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | multi-seed-core | 87.83 | 87.59 | 88.06 | 86.20 | 89.04 | 89.45 | 86.71 | 17298s (3-seed batch) |\n| 123 | multi-seed-core | 89.52 | 89.40 | 89.64 | 87.34 | 91.56 | 91.76 | 87.63 | (same batch) |\n| 456 | multi-seed-core | 87.88 | 88.21 | 87.53 | 83.12 | 93.97 | 93.60 | 82.21 | (same batch) |\n| 789 | cls-seed789 | 89.00 | 89.10 | 88.90 | 85.20 | 93.40 | 93.30 | 84.90 | 3849s |\n| 0 | cls-seed0 | 87.94 | 88.08 | 87.79 | 84.20 | 92.32 | 92.13 | 83.84 | 4977s |\n| **Mean** | | **88.43** | **88.48** | **88.38** | **85.21** | **92.06** | **92.05** | **85.06** | |\n| **Std** | | **0.74** | **0.67** | **0.83** | | | | | |\n\n**Code World Model (CWM) — Qwen3-4B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | cwm-baseline | 87.51 | 87.71 | 87.31 | 83.53 | 92.32 | 92.06 | 83.03 | 84.02 | 3439s |\n| 123 | cwm-seed123 | 87.20 | 87.44 | 86.95 | — | — | — | — | 84.44 | 5096s |\n| 456 | cwm-seed456 | 86.98 | 87.29 | 86.66 | 82.52 | 92.65 | 92.26 | 81.70 | 84.02 | 3440s |\n| 789 | cwm-seed789 | 86.67 | 86.60 | 86.74 | 84.09 | 89.25 | 89.37 | 84.25 | 83.97 | 5158s |\n| 0 | cwm-seed0 | 87.57 | 87.93 | 87.18 | 82.71 | 93.86 | 93.45 | 81.70 | 84.29 | 3586s |\n| **Mean** | | **87.19** | **87.39** | **86.97** | **83.21** | **92.02** | **91.79** | **82.67** | **84.15** | |\n| **Std** | | **0.38** | **0.52** | **0.27** | | | | | | |\n\n**4B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 87.83 | 87.51 | +0.32 |\n| 123 | 89.52 | 87.20 | +2.32 |\n| 456 | 87.88 | 86.98 | +0.90 |\n| 789 | 89.00 | 86.67 | +2.33 |\n| 0 | 87.94 | 87.57 | +0.37 |\n| **Mean** | **88.43** | **87.19** | **+1.25** |\n\n### 1.2 8B Function-Level: CLS vs CWM (3 seeds each)\n\n**Classification (CLS) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|\n| 42 | model-size-scaling-cls8b | 90.48 | 90.06 | 90.86 | 90.76 | 89.36 | 90.22 | 91.51 | 5614s |\n| 123 | cls8b-seed123 | 89.40 | 89.20 | 89.50 | 87.50 | 90.90 | 91.20 | 87.90 | 5666s |\n| 456 | cls8b-seed456 | 88.31 | 88.41 | 88.20 | 84.72 | 92.43 | 92.29 | 84.46 | 5481s |\n| **Mean** | | **89.40** | **89.22** | **89.52** | **87.66** | **90.90** | **91.24** | **87.96** | |\n\n**Code World Model (CWM) — Qwen3-8B + LoRA**\n\n| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |\n|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|\n| 42 | model-size-scaling-cwm8b | 87.67 | 87.77 | 87.57 | 84.19 | 91.67 | 91.53 | 83.95 | 84.39 | 5570s |\n| 123 | cwm8b-seed123 | 86.98 | 87.13 | 86.83 | — | — | — | — | 84.13 | 5948s |\n| 456 | cwm8b-seed456 | 86.24 | 86.51 | 85.96 | 82.09 | 91.45 | 91.08 | 81.39 | 82.80 | 6071s |\n| **Mean** | | **86.96** | **87.14** | **86.79** | **83.14** | **91.56** | **91.31** | **82.67** | **83.77** | |\n\n**8B CLS vs CWM Per-Seed Gap (Accuracy)**\n\n| Seed | CLS | CWM | Gap (pp) |\n|------|-----|-----|----------|\n| 42 | 90.48 | 87.67 | +2.81 |\n| 123 | 89.40 | 86.98 | +2.42 |\n| 456 | 88.31 | 86.24 | +2.07 |\n| **Mean** | **89.40** | **86.96** | **+2.43** |\n\n**Scaling Summary: CLS-CWM Gap Widens with Model Size**\n\n| Model Size | CLS Mean Acc | CWM Mean Acc | Gap (pp) | Seeds |\n|------------|-------------|-------------|----------|-------|\n| 4B | 88.43 | 87.19 | +1.25 | 5 |\n| 8B | 89.40 | 86.96 | +2.43 | 3 |\n| Gap widening | | | +1.18 | |\n\n### 1.3 Trajectory-Level Baseline (5 seeds, Qwen3-4B)\n\n| Seed | Exp ID | Accuracy | Unresolved F1 | Resolved F1 | Consistency |\n|------|--------|----------|---------------|-------------|-------------|\n| 42 | traj-level-finetuned | 85.66 | 87.50 | 83.18 | 79.94% |\n| 123 | traj-level-seed123 | 85.47 | 87.00 | 83.52 | 78.59% |\n| 456 | traj-level-seed456 | 87.40 | 88.70 | 85.80 | 78.80% |\n| 789 | traj-level-seed789 | 87.31 | 88.27 | 86.17 | 76.74% |\n| 0 | traj-level-seed0 | 85.66 | 87.37 | 83.41 | 79.55% |\n| **Mean** | | **86.30** | **87.77** | **84.42** | **78.72%** |\n\n### 1.4 LLM-Judge Zero-Shot Baselines\n\n| Model | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec |\n|-------|----------|---------|---------|-----------|----------|-----------|----------|\n| Qwen3-8B zero-shot | 64.40 | 72.20 | 50.50 | 57.90 | 95.80 | 90.00 | 35.10 |\n| Qwen3-32B NF4 zero-shot | 71.69 | 75.91 | 65.68 | 64.40 | 92.43 | 88.12 | 52.35 |\n| Fine-tuned 4B CLS (ref) | 88.43 | 88.48 | 88.38 | 85.21 | 92.06 | 92.05 | 85.06 |\n\nFine-tuning advantage: +24.0pp over 8B zero-shot, +16.7pp over 32B zero-shot.\n\n### 1.5 CLS vs Trajectory — Variant-Level Equivalence (5-Paired Clustered Bootstrap)\n\n| Metric | Value |\n|--------|-------|\n| Pooled gap (CLS − TRAJ) | −0.45 pp |\n| 95% CI | [−1.71, +0.84] |\n| Pooled p-value (gap ≠ 0) | 0.499 |\n| TOST p-value (±2pp margin) | 0.0071 |\n| TOST conclusion | **Equivalent** |\n| ICC (intra-cluster correlation) | 0.191 |\n| Design effect (DEFF) | 3.97 |\n| n_variants | 523 |\n| n_clusters | 114 |\n\nPer-seed variant-level gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29\n\n### 1.6 Oracle / Statistical Analysis\n\n**Oracle F2P Stratification (oracle-f2p-stratified)**\n\n| T bucket | % of instances | Block-corr advantage (pp) | Contribution to overall |\n|----------|---------------|--------------------------|------------------------|\n| T=1 | 68.7% | −0.09 | negligible |\n| T=2 | 19.1% | 31.69 | 55.3% |\n| T=3–5 | 7.1% | 40.74 | — |\n| T≥6 | 5.1% | 40.06 | — |\n| **Overall** | 100% | **10.93** | |\n\n**P2P Regression Rate (p2p-regression-rate) — NEGATIVE**\n- Mean regression rate: 1.04%, median: 0%\n- 77% of incorrect patches break zero P2P tests\n- Falls in <5% zone → P2P signal weak for this dataset\n\n**Block Correlation (block-corr-empirical)**\n\n| Metric | Value |\n|--------|-------|\n| ICC | 0.191 |\n| ICC p-value | 0.000 |\n| Design effect | 3.97 |\n| Overall error rate | 12.49% |\n| All-correct problems (observed) | 46 |\n| All-correct problems (expected i.i.d.) | 16.35 |\n| Ratio (observed/expected) | 2.81× |\n| Error std observed | 0.153 |\n| Error std expected i.i.d. | 0.081 |\n\n**Matched-Seed Error Overlap**\n- CLS dominant error: miss bugs (FN) — 75.5% of CLS errors\n- CWM dominant error: false alarms (FP) — 83.1% of CWM errors\n- Oracle ensemble accuracy: 90.63%\n- Complementary error patterns → formulation diversity as verification strategy\n\n### 1.7 Per-Test Diagnostic Analysis\n\n**Precision-Recall by Mutation Type (per-test-precision-recall)**\n\n| Mutation Type | Accuracy | F1 |\n|---------------|----------|----|\n| return_value | 97.26% | 98.6% (easiest) |\n| off_by_one | 82.56% | 80.8% (hardest) |\n\n- 114 problems, 48 (42.1%) perfect prediction\n- Median problem fail-F1: 94.12%\n- Worst problems: MBPP/397 (40%), HumanEval/130 (46%)\n- Bucket 6–10 tests: 96.3% accuracy; 11+ tests: 87.1%\n\n**Majority Voting K=3 (per-test-majority-voting) — NEGATIVE**\n\n| Metric | Greedy | Majority Vote K=3 | Delta |\n|--------|--------|-------------------|-------|\n| Accuracy | 87.51 | 86.83 | −0.69 |\n| Fail F1 | 87.86 | 87.29 | −0.57 |\n| Pass F1 | 87.15 | 86.33 | −0.82 |\n\n- Unanimous rate: 93.3%\n- Net flips: −13 (28 correct→wrong, 15 wrong→correct)\n\n### 1.8 Dataset Statistics (mvp-b-data-prep)\n\n| Metric | Value |\n|--------|-------|\n| Total samples | 19,076 |\n| HumanEval | 5,575 |\n| MBPP | 13,501 |\n| Class balance | pass 52.0% / fail 48.0% |\n| Train/Val/Test | 15,290 / 1,896 / 1,890 |\n| Majority baseline | 52.0% |\n| Label verification | All verified by execution (5s timeout) |\n\n### 1.9 Training Hyperparameters\n\n| Param | 4B CLS/CWM | 8B CLS/CWM |\n|-------|-----------|-----------|\n| Base model | Qwen/Qwen3-4B | Qwen/Qwen3-8B |\n| Method | LoRA | LoRA |\n| Batch size | 2 | 2 |\n| Grad accumulation | 16 | 16 |\n| Learning rate | 2e-4 | 2e-4 |\n| Epochs | 3 | 3 |\n| Trainable params | ~0.19% | ~0.19% (15.3M/8.2B) |\n| GPU hours per seed | ~1.0–1.5h | ~1.5–1.7h |\n\n---\n\n## 2. Paper Framing 证据审查\n\n### Claim 1: Complexity-Dependent Reformulation Advantage\n\n> CLS and CWM equivalent on simple function-level code; CLS scales better with model size and to repo-level complexity.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| 4B function-level CLS≈CWM | ✅ 充足 | 5 seeds each | Gap=+1.25pp mean, std overlap |\n| 8B scaling gap widens | ✅ 充足 | 3 seeds each | Gap=+2.43pp mean (2.07–2.81) |\n| LLM-judge far below fine-tuned | ✅ 充足 | 2 baselines | 8B: 64.4%, 32B: 71.7% vs ft-4B: 88.4% |\n| Repo-level CLS > CWM | ❌ 缺失 | v3 均 SIGKILL | 训练中，预计 14–20h |\n| CWM failure modes 定性分析 | ⚠️ 间接 | EM rate ~84% | 需 repo-level 数据直接展示 |\n\n**统计检验缺口：**\n- ❌ 4B CLS vs CWM paired bootstrap 检验（5 seeds 数据已有，未跑）\n- ❌ 8B CLS vs CWM paired bootstrap 检验（3 seeds 数据已有，未跑）\n- ❌ Scaling interaction test（gap widening 显著性）\n- ⚠️ 需 effect size (Cohen's d)\n\n**判定：** 函数级证据方向正确但统计力度不足（5 seeds paired t-test power 低）。Repo-level 是核心缺失。\n\n### Claim 2: Diagnostic Granularity At Equivalent Accuracy\n\n> Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| Variant-level equivalence | ✅ 充足 | 5-paired-clustered-bootstrap | TOST p=0.007, gap=−0.45pp |\n| Cluster structure | ✅ 充足 | block-corr-empirical | ICC=0.191, DEFF=3.97 |\n| Diagnostic granularity | ✅ 部分 | per-test-precision-recall | Per-mutation breakdown |\n| Downstream re-repair | ❌ 缺失 | — | 未实验 |\n\n**统计检验：** ✅ 完整。\n\n**注意：** Seeds 789/0 使用 4-bit quantization，论文需说明。±2pp TOST margin 需 justification。\n\n**判定：** 证据最充分，可直接写入论文。\n\n### Claim 3: Accuracy-Utility Frontier Characterization\n\n> Per-test advantage depends on test distribution; concentrates in multi-F2P instances.\n\n| 证据点 | 状态 | 实验 | 数据 |\n|--------|------|------|------|\n| T distribution sensitivity | ✅ 充足 | oracle-f2p-stratified | T=1 无优势, T≥2 +30–41pp |\n| P2P regression rare | ✅ 充足 | p2p-regression-rate | 1.04% mean (negative) |\n| Block correlation | ✅ 充足 | block-corr-empirical | ICC=0.191, ratio 2.81× |\n| Error complementarity | ✅ 充足 | matched-seed overlap | Oracle 90.63% |\n| Majority voting | ✅ 充足 | per-test-majority-voting | K=3 hurts −0.69pp (negative) |\n| Oracle frontier | ✅ 部分 | mvp-a-oracle-sim | 基于模拟，非真实模型 |\n\n**判定：** 证据丰富，但 oracle frontier 基于模拟——需论文明确说明。\n\n---\n\n## 3. 缺失清单\n\n### 3.1 缺失的实验/数据\n\n| 优先级 | 缺失项 | 依赖 | 备注 |\n|--------|--------|------|------|\n| **P0** | Repo-level CLS 训练结果 | v4 训练完成 (~14–20h) | Claim 1 核心 |\n| **P0** | Repo-level CWM 训练结果 | v4 训练完成 | Claim 1 核心 |\n| **P0** | Repo-level paired bootstrap | 两个训练完成后 | Go/No-Go 决策 |\n| **P1** | 4B CLS vs CWM paired bootstrap (5 seeds) | 数据已有 | 统计完善 |\n| **P1** | 8B CLS vs CWM paired bootstrap (3 seeds) | 数据已有 | 统计完善 |\n| **P1** | Scaling interaction test | 数据已有 | Gap widening 显著性 |\n| **P2** | CLS vs CWM effect size (Cohen's d) | 数据已有 | 补充统计 |\n| **P2** | Diagnostic re-repair experiment | 需新实验或 future work | Claim 2 downstream |\n| **P3** | Oracle frontier with real model | precision-recall 数据可用 | Claim 3 加强 |\n\n### 3.2 缺失的图表\n\n| Figure | 描述 | 数据来源 | 优先级 |\n|--------|------|----------|--------|\n| Fig 1 | 方法概览图：CLS vs CWM formulation 对比示意 | 手绘/设计 | P0 |\n| Fig 2 | 主结果柱状图：4B/8B CLS vs CWM accuracy + error bars | §1.1 + §1.2 | P0 |\n| Fig 3 | Scaling plot：Model size × Formulation accuracy 折线图 | §1.1 + §1.2 | P0 |\n| Fig 4 | CLS vs TRAJ 等价性：TOST 可视化 / forest plot | §1.5 | P0 |\n| Fig 5 | LLM-judge baseline 对比 bar chart | §1.4 | P1 |\n| Fig 6 | Oracle frontier：resolve rate vs precision curves | §1.6 oracle-sim | P1 |\n| Fig 7 | F2P 分层分析：per-test advantage by T bucket | §1.6 stratified | P1 |\n| Fig 8 | Error complementarity：CLS vs CWM 错误模式对比 | matched-seed overlap | P1 |\n| Fig 9 | Block correlation：observed vs expected error distribution | §1.6 block-corr | P2 |\n| Fig 10 | Per-test precision-recall by mutation type | §1.7 | P2 |\n| Fig 11 | Repo-level 结果（待训练完成） | — | P0 (blocked) |\n\n### 3.3 Repo-Level 完成后需要的后续分析\n\n1. Repo-level eval on SWE-bench Verified subset\n2. Paired bootstrap: CLS vs CWM (n≥200)\n3. Go/No-Go decision per ROADMAP D008\n4. CWM failure mode qualitative analysis (token exhaustion, string mismatch cases)\n5. Repo-level oracle frontier with real model precision/recall\n6. Update scaling plot with repo-level data point\n7. (Stretch) End-to-end re-ranking demo for resolve rate\n\n### 3.4 可立即执行的 CPU 任务\n\n| 任务 | 优先级 | 输入数据 |\n|------|--------|----------|\n| 4B CLS vs CWM 5-seed paired bootstrap | P1 | 已有 eval predictions |\n| 8B CLS vs CWM 3-seed paired bootstrap | P1 | 已有 eval predictions |\n| Scaling interaction effect | P1 | 已有 mean/std |\n| Cohen's d effect sizes | P2 | 已有 mean/std |\n| 画 Fig 2–10 | P0 | 本文档数据 |\n| Paper Agent 写已完成 pillars 章节 | P0 | paper_framing + 本文档 |\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T17:32:27.184597+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/paper_materials.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-12T17:32:27.184741+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_materials",
  "type": "report",
  "description": "论文素材汇总：35个实验的结构化指标表格 + 3个Claim证据审查 + 缺失清单（图表/统计/repo-level）",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/paper_materials.md",
  "tags": "['paper', 'metrics', 'evidence-review']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_materials",
    "type": "report",
    "description": "论文素材汇总：35个实验的结构化指标表格 + 3个Claim证据审查 + 缺失清单（图表/统计/repo-level）",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/paper_materials.md",
    "tags": "['paper', 'metrics', 'evidence-review']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T17:32:27.184922+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_66363a\", \"name\": \"paper_materials\", \"type\": \"report\", \"description\": \"论文素材汇总：35个实验的结构化指标表格 + 3个Claim证据审查 + 缺失清单（图表/统计/repo-level）\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/paper_materials.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T17:32:20.302919+00:00\", \"tags\": [\"paper\", \"metrics\", \"evidence-review\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-materials_20260512T172304",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-12T17:32:27.185093+00:00_

已完成，产出保存在 `artifacts/_project/report/paper_materials.md`。

关键发现：
- **Claim 2（per-test ≈ trajectory 等价性）证据最充分**，TOST + clustered bootstrap + ICC 齐全，可直接写
- **Claim 1（complexity-dependent advantage）函数级方向正确但统计力度不足**——缺 CLS vs CWM paired bootstrap（数据已有未跑），repo-level 是决胜关键
- **Claim 3（oracle frontier）证据丰富但 oracle 分析基于模拟**，需明确标注
- **最大阻塞项**：repo-level 训练结果（P0），所有其他缺失项（paired bootstrap、effect size、图表）都可立即推进

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper-materials_20260512T172304"
}
```

</details>

---
