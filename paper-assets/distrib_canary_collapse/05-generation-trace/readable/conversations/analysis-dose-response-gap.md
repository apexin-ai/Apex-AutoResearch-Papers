# analysis dose response gap

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_analysis_dose-response-gap_20260519T071655.jsonl`
- **Structured JSON:** [`807ad50bdecac005f5fe.json`](../../sessions/80/807ad50bdecac005f5fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-19T07:24:06.447111+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T07:24:06.447418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T07:24:06.447594+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "experiment_plan",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "experiment_plan",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T07:24:06.447727+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T07:24:06.447871+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "experiment_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "experiment_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T07:24:06.448013+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T07:24:06.448135+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T07:24:06.448321+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:39 UTC | 更新原因: Reviewer 确认 8/8 GPU 满载 + dose-response 表补入 a005/a010/a060 已完成数据\\n\\n> **阶段**: 8 卡冲刺 Day 2 — D091 fp32 修复中 + D092 bf16/fp32 反转 + Paper Agent 写作中\\n\\n## 核心方向\\n**D067 升级**: analysis → method paper。核心贡献：\\n1. **MMCT** — FPR=0, dose-response (fp32 重算中)，跨架构 7/7 泛化\\n2. **Regime map + 盲区 (D075)** — 8 点 α-sweep, permG step function, canary 盲区 α≤0.10\\n3. **Downstream 指标选择 (D085)** — perplexity 极端 collapse 下丧失 lag structure\\n\\n**Target**: EMNLP 2026 main track（ARR June cycle, DDL ~June 15, ~27 days）\\n\\n## 当前进展\\n- 43+ 成功 / 8 RUNNING (8/8 GPU 满载确认)\\n- **D091**: α=0.50 fp32 × 3 seeds 05:31 UTC 提交，~5h 完成\\n- **D092**: MMCT α=0.10 矛盾已解（4/8 为误标），bf16/fp32 PermG 反转→step function 必须纯 fp32\\n- Paper Agent: Intro ✅ + patches, Method/RW 写作中\\n- Lag sensitivity + intervention 5-method + dual-track figure ✅ Reviewer PASS\\n- a005 fp32 盲区延伸至 α=0.05 ✅ | a060 fp32 transitional ✅\\n\\n## GPU 分配（8/8 满载 ✅）\\n| Server:GPU | exp_id | 精度 | 目的 | 状态 |\\n|------------|--------|------|------|------|\\n| 17855:cuda:0 | scale_69b | bf16 | 6.9B scale claim | gen 9/10, ~1h |\\n| 17855:cuda:1 | qwen35_v2 | fp32 | 新架构 Table 7 | 运行中 |\\n| 17855:cuda:2 | a050_s42_fp32 | fp32 | D091 修复 | 05:31 提交, ~5h |\\n| 17855:cuda:3 | a050_s43_fp32 | fp32 | D091 修复 | 05:31 提交, ~5h |\\n| 17855:cuda:4 | a050_s44_fp32 | fp32 | D091 修复 | 05:31 提交, ~5h |\\n| 17855:cuda:5 | a010_s42_fp32 | fp32 | blind zone 双 seed | 运行中, ~5h |\\n| 19828:cuda:0 | gpt2m_s43_fp32 | fp32 | GPT-2m Table 7 | 运行中 |\\n| 19828:cuda:1 | smollm3_v3 | fp32 | SmolLM3 Table 7 | 运行中, ~14h |\\n\\n## fp32 Dose-Response Map（D091+D092: 纯 fp32 mandatory）\\n| α | PermG | MMCT wpair | d1 drift | Regime | provenance |\\n|---|-------|------------|----------|--------|------------|\\n| 0.00 | 0/24 (0%) | 0/24 (0%
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T07:24:06.448489+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T07:24:06.448977+00:00_

Error: result (103,668 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T07:24:06.449158+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/experiment_plan.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T07:24:06.449316+00:00_

experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T07:24:06.449471+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total DONE experiments: {len(exps)}')\nprint()\nfor e in exps:\n    eid = e.get('experiment_id','')\n    status = e.get('status','')\n    conclusion = e.get('conclusion','')[:120] if e.get('conclusion') else ''\n    prec = ''\n    if e.get('config'):\n        prec = e['config'].get('precision','') or e['config'].get('dtype','')\n    alpha = ''\n    if e.get('config'):\n        alpha = e['config'].get('alpha','')\n    seeds = ''\n    if e.get('config'):\n        seeds = e['config'].get('seed','') or e['config'].get('seeds','')\n    metrics_keys = list(e.get('metrics',{}).keys())[:5] if e.get('metrics') else []\n    print(f'{eid} | alpha={alpha} | prec={prec} | seed={seeds} | conclusion={conclusion}')\n\" 2>&1 | head -80",
  "description": "Parse registry DONE experiments summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total DONE experiments: {len(exps)}')\nprint()\nfor e in exps:\n    eid = e.get('experiment_id','')\n    status = e.get('status','')\n    conclusion = e.get('conclusion','')[:120] if e.get('conclusion') else ''\n    prec = ''\n    if e.get('config'):\n        prec = e['config'].get('precision','') or e['config'].get('dtype','')\n    alpha = ''\n    if e.get('config'):\n        alpha = e['config'].get('alpha','')\n    seeds = ''\n    if e.get('config'):\n        seeds = e['config'].get('seed','') or e['config'].get('seeds','')\n    metrics_keys = list(e.get('metrics',{}).keys())[:5] if e.get('metrics') else []\n    print(f'{eid} | alpha={alpha} | prec={prec} | seed={seeds} | conclusion={conclusion}')\n\" 2>&1 | head -80",
    "description": "Parse registry DONE experiments summary"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T07:24:06.449609+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    eid = e.get('experiment_id','')
          ^^^^^
AttributeError: 'str' object has no attribute 'get'
Total DONE experiments: 50

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T07:24:06.449725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T07:24:06.449934+00:00_

1	experiments:
2	- id: plan_001
3	  claim: 2
4	  description: 'α-sweep anchor: Pythia-410M × WikiText-103 × α=0.25 × 10 gen × seed=42'
5	  priority: P0
6	  gpu_budget_hours: 4
7	  deps: []
8	  notes: α-sweep 基准实验。D025 统一参数。
9	  registry_id: alpha_sweep_a025_s42_v3
10	- id: plan_001b
11	  claim: 3
12	  description: 'α=0.0 null control: Pythia-410M × WikiText-103 × α=0.0 × 10 gen ×
13	    seed=42。FPR ground truth'
14	  priority: P0
15	  gpu_budget_hours: 4
16	  deps: []
17	  notes: 'D028: perm_granger/TY 0% FPR，naive 100% FPR'
18	  registry_id: alpha_sweep_a000_s42
19	- id: plan_001c
20	  claim: 2
21	  description: 'α=0.50 sweep: Pythia-410M × WikiText-103 × α=0.50 × 10 gen × seed=42'
22	  priority: P0
23	  gpu_budget_hours: 4
24	  deps: []
25	  notes: 'D025: 所有严格方法 FDR 后归零（0/8），仅 naive 8/8。α=0.50 是 method×regime interaction
26	    最极端例证'
27	  registry_id: alpha_sweep_a050_s42
28	- id: plan_001d
29	  claim: 1
30	  description: 'α=0.75 sweep: Pythia-410M × WikiText-103 × α=0.75 × 10 gen × seed=42'
31	  priority: P0
32	  gpu_budget_hours: 4
33	  deps: []
34	  notes: 'D037: 3/4 FDR-sig forward, 0/4 reverse, consensus 11/16 robust'
35	  registry_id: alpha_sweep_a075_s42
36	- id: plan_045
37	  claim: 2
38	  description: 'α=0.05 sweep: Pythia-410M × WikiText-103 × α=0.05 × 10 gen × seed=42。定位
39	    diversity 悬崖精确位置（α=0.00 d1=-14% → α=0.10 d1=-40% 之间的断崖）'
40	  priority: P0
41	  gpu_budget_hours: 4
42	  deps: []
43	  notes: 'D076: HIGH ROI。如果 α=0.05 d1≈-40% → 5% 污染即全损；如果 d1 在 -14% 和 -40% 之间 → 存在明确阈值'
44	  registry_id: alpha_sweep_a005_s42_v3
45	- id: plan_025
46	  claim: 2
47	  description: 'α=0.10 sweep: Pythia-410M × WikiText-103 × α=0.10 × 10 gen × seed=42。Regime
48	    map 下界，验证极低污染下 signal 是否存在'
49	  priority: P0
50	  gpu_budget_hours: 4
51	  deps: []
52	  notes: 'D061: regime map 5→7 点，精确刻画低端 boundary。D075: canary blind zone confirmed'
53	  registry_id: alpha_sweep_a010_s42_fp32
54	- id: plan_026
55	  claim: 2
56	  description: 'α=0.60 sweep: Pythia-410M × WikiText-103
…[truncated 12371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T07:24:06.450091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total DONE experiments: {len(exps)}')\nprint()\n# exps is a dict\nif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status','')\n        conclusion = (e.get('conclusion','') or '')[:120]\n        prec = ''\n        if e.get('config'):\n            prec = e['config'].get('precision','') or e['config'].get('dtype','')\n        alpha = ''\n        if e.get('config'):\n            alpha = e['config'].get('alpha','')\n        seeds = ''\n        if e.get('config'):\n            seeds = e['config'].get('seed','') or e['config'].get('seeds','')\n        print(f'{eid} | alpha={alpha} | prec={prec} | seed={seeds} | {conclusion}')\nelif isinstance(exps, list):\n    for e in exps:\n        if isinstance(e, dict):\n            eid = e.get('experiment_id','')\n            conclusion = (e.get('conclusion','') or '')[:120]\n            prec = ''\n            if e.get('config'):\n                prec = e['config'].get('precision','') or e['config'].get('dtype','')\n            alpha = ''\n            if e.get('config'):\n                alpha = e['config'].get('alpha','')\n            seeds = ''\n            if e.get('config'):\n                seeds = e['config'].get('seed','') or e['config'].get('seeds','')\n            print(f'{eid} | alpha={alpha} | prec={prec} | seed={seeds} | {conclusion}')\n        else:\n            print(f'Element: {e}')\n\" 2>&1 | head -80",
  "description": "Parse registry data with type handling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total DONE experiments: {len(exps)}')\nprint()\n# exps is a dict\nif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status','')\n        conclusion = (e.get('conclusion','') or '')[:120]\n        prec = ''\n        if e.get('config'):\n            prec = e['config'].get('precision','') or e['config'].get('dtype','')\n        alpha = ''\n        if e.get('config'):\n            alpha = e['config'].get('alpha','')\n        seeds = ''\n        if e.get('config'):\n            seeds = e['config'].get('seed','') or e['config'].get('seeds','')\n        print(f'{eid} | alpha={alpha} | prec={prec} | seed={seeds} | {conclusion}')\nelif isinstance(exps, list):\n    for e in exps:\n        if isinstance(e, dict):\n            eid = e.get('experiment_id','')\n            conclusion = (e.get('conclusion','') or '')[:120]\n            prec = ''\n            if e.get('config'):\n                prec = e['config'].get('precision','') or e['config'].get('dtype','')\n            alpha = ''\n            if e.get('config'):\n                alpha = e['config'].get('alpha','')\n            seeds = ''\n            if e.get('config'):\n                seeds = e['config'].get('seed','') or e['config'].get('seeds','')\n            print(f'{eid} | alpha={alpha} | prec={prec} | seed={seeds} | {conclusion}')\n        else:\n            print(f'Element: {e}')\n\" 2>&1 | head -80",
    "description": "Parse registry data with type handling"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T07:24:06.450248+00:00_

Total DONE experiments: 50

interv_pred_a075_s42_fp32_v4 | alpha= | prec= | seed= | success
alpha_sweep_a060_s42_fp32_v3 | alpha= | prec= | seed= | success
alpha_sweep_a005_s42_v3 | alpha= | prec= | seed= | success
alpha_sweep_a010_s43_fp32 | alpha= | prec= | seed= | success
alpha_sweep_a005_s42 | alpha= | prec= | seed= | failed
alpha_sweep_a060_s42_fp32_v2 | alpha= | prec= | seed= | killed
alpha_sweep_a010_s43 | alpha= | prec= | seed= | success
qwen35_08b_wiki_a100_s42 | alpha= | prec= | seed= | killed
smollm3_3b_wiki_a100_s42_v2 | alpha= | prec= | seed= | failed
interv_pred_a075_s42_fp32 | alpha= | prec= | seed= | failed
alpha_sweep_a060_s42_fp32 | alpha= | prec= | seed= | failed
scale_14b_a050_s42 | alpha= | prec= | seed= | success
conditional_granger_d061 | alpha= | prec= | seed= | success
method_ablation_phase3 | alpha= | prec= | seed= | success
interv_pred_a075_s42_fp32_v2 | alpha= | prec= | seed= | killed
interv_pred_s43_bf16 | alpha= | prec= | seed= | success
smollm3_3b_wiki_a100_s42 | alpha= | prec= | seed= | killed
interv_react_s43_bf16 | alpha= | prec= | seed= | success
gen_gpt2m_a100_s43_bf16 | alpha= | prec= | seed= | success
alpha_sweep_a060_s42_bf16 | alpha= | prec= | seed= | success
alpha_sweep_c4_a050_s42_bf16 | alpha= | prec= | seed= | success
gen_opt13b_a100_s43_bf16 | alpha= | prec= | seed= | killed
alpha_sweep_a010_s42_v2 | alpha= | prec= | seed= | negative
interv_pred_s43 | alpha= | prec= | seed= | killed
alpha_sweep_c4_a050_s42 | alpha= | prec= | seed= | killed
alpha_sweep_a060_s42_v2 | alpha= | prec= | seed= | killed
intervention_predictive_s42 | alpha= | prec= | seed= | success
intervention_reactive_s42 | alpha= | prec= | seed= | success
gen_wiki_gpt2m_a100_s42_v4 | alpha= | prec= | seed= | success
generalize_pythia14b_wiki_a100_s42 | alpha= | prec= | seed= | success
generalize_pythia410m_wiki_a100_s42 | alpha= | prec= | seed= | success
generalize_pythia1b_c4_a100_s43 | alpha= | prec= | seed= | success
generalize_opt1b_wiki_a100_s42 | alpha=
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T07:24:06.450480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get all alpha sweep experiments\nfor eid, e in exps.items():\n    if 'alpha' in eid or 'a0' in eid or 'a1' in eid or 'sweep' in eid:\n        status = e.get('status','')\n        conclusion = (e.get('conclusion','') or '')[:200]\n        config = e.get('config', {})\n        metrics = e.get('metrics', {})\n        created = e.get('created_at','')[:10]\n        updated = e.get('updated_at','')[:10]\n        print(f'=== {eid} ===')\n        print(f'  status: {status} | conclusion: {conclusion}')\n        print(f'  config: {json.dumps(config)[:300]}')\n        print(f'  metrics keys: {list(metrics.keys())[:10]}')\n        print(f'  created: {created} | updated: {updated}')\n        print()\n\" 2>&1",
  "description": "Extract alpha sweep experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get all alpha sweep experiments\nfor eid, e in exps.items():\n    if 'alpha' in eid or 'a0' in eid or 'a1' in eid or 'sweep' in eid:\n        status = e.get('status','')\n        conclusion = (e.get('conclusion','') or '')[:200]\n        config = e.get('config', {})\n        metrics = e.get('metrics', {})\n        created = e.get('created_at','')[:10]\n        updated = e.get('updated_at','')[:10]\n        print(f'=== {eid} ===')\n        print(f'  status: {status} | conclusion: {conclusion}')\n        print(f'  config: {json.dumps(config)[:300]}')\n        print(f'  metrics keys: {list(metrics.keys())[:10]}')\n        print(f'  created: {created} | updated: {updated}')\n        print()\n\" 2>&1",
    "description": "Extract alpha sweep experiment details from registry"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T07:24:06.450664+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 19, in &lt;module>
    print(f'  metrics keys: {list(metrics.keys())[:10]}')
                                  ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'keys'
=== interv_pred_a075_s42_fp32_v4 ===
  status: DONE | conclusion: success
  config: {}
  metrics keys: ['final_ppl', 'final_entropy', 'final_eff_rank', 'final_mauve', 'precision', 'intervention_trigger_gen', 'recovery_gen', 'token_entropy_drift', 'ece_drift', 'perplexity_drift']
  created: 2026-05-19 | updated: 2026-05-19

=== alpha_sweep_a060_s42_fp32_v3 ===
  status: DONE | conclusion: success
  config: {}
  metrics keys: ['final_ppl', 'final_entropy', 'final_eff_rank', 'final_mauve', 'precision', 'token_entropy_drift', 'ece_drift', 'perplexity_drift', 'distinct_1_drift', 'distinct_2_drift']
  created: 2026-05-19 | updated: 2026-05-19

=== alpha_sweep_a005_s42_v3 ===
  status: DONE | conclusion: success
  config: {}
  metrics keys: ['final_ppl', 'final_entropy', 'final_eff_rank', 'final_mauve', 'precision', 'token_entropy_drift', 'ece_drift', 'perplexity_drift', 'distinct_1_drift', 'distinct_2_drift']
  created: 2026-05-19 | updated: 2026-05-19

=== alpha_sweep_a010_s43_fp32 ===
  status: DONE | conclusion: success
  config: {}
  metrics keys: ['token_entropy_drift', 'distinct_1_drift', 'distinct_2_drift', 'distinct_3_drift', 'perplexity_drift', 'perm_granger_fwd', 'perm_granger_rev', 'ty_granger_fwd', 'threshold_onset_fwd', 'consensus_k4']
  created: 2026-05-19 | updated: 2026-05-19

=== alpha_sweep_a005_s42 ===
  status: DONE | conclusion: failed
  config: {}
  metrics keys: []
  created: 2026-05-18 | updated: 2026-05-19

=== alpha_sweep_a060_s42_fp32_v2 ===
  status: DONE | conclusion: killed
  config: {}
  metrics keys: []
  created: 2026-05-18 | updated: 2026-05-19

=== alpha_sweep_a010_s43 ===
  status: DONE | conclusion: success
  config: {}
  metrics keys: ['token_entropy_drift', 'ece_drift', 'perplexity_drift', 'di
…[truncated 5600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T07:24:06.450825+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Focus on alpha sweep + dose-response relevant experiments\n# Check precision in metrics\nrelevant = []\nfor eid, e in exps.items():\n    if 'alpha' in eid or 'a0' in eid or 'a1' in eid or 'sweep' in eid or 'mvp' in eid:\n        metrics = e.get('metrics', {})\n        if isinstance(metrics, str):\n            metrics = {}\n        prec = metrics.get('precision', 'N/A')\n        status = e.get('status','')\n        conclusion = e.get('conclusion','')\n        d1_drift = metrics.get('distinct_1_drift', metrics.get('distinct_1_drift_pct', metrics.get('distinct_1_delta_pct', 'N/A')))\n        permg_fwd = metrics.get('perm_granger_fwd', metrics.get('pg_fwd', 'N/A'))\n        mmct = metrics.get('mmct_wpair', metrics.get('mmct', 'N/A'))\n        print(f'{eid} | prec={prec} | status={status}/{conclusion} | d1={d1_drift} | permg={permg_fwd} | mmct={mmct}')\n\n# Also check a000 experiments\nprint()\nprint('--- All a000/a025/a050/a075/a100 experiments ---')\nfor eid, e in exps.items():\n    metrics = e.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = {}\n    prec = metrics.get('precision', '')\n    conclusion = e.get('conclusion','')\n    if any(x in eid for x in ['a000', 'a025', 'a050', 'a075', 'a100']):\n        print(f'{eid} | prec={prec} | conclusion={conclusion}')\n\" 2>&1",
  "description": "Extract precision and key metrics for dose-response experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Focus on alpha sweep + dose-response relevant experiments\n# Check precision in metrics\nrelevant = []\nfor eid, e in exps.items():\n    if 'alpha' in eid or 'a0' in eid or 'a1' in eid or 'sweep' in eid or 'mvp' in eid:\n        metrics = e.get('metrics', {})\n        if isinstance(metrics, str):\n            metrics = {}\n        prec = metrics.get('precision', 'N/A')\n        status = e.get('status','')\n        conclusion = e.get('conclusion','')\n        d1_drift = metrics.get('distinct_1_drift', metrics.get('distinct_1_drift_pct', metrics.get('distinct_1_delta_pct', 'N/A')))\n        permg_fwd = metrics.get('perm_granger_fwd', metrics.get('pg_fwd', 'N/A'))\n        mmct = metrics.get('mmct_wpair', metrics.get('mmct', 'N/A'))\n        print(f'{eid} | prec={prec} | status={status}/{conclusion} | d1={d1_drift} | permg={permg_fwd} | mmct={mmct}')\n\n# Also check a000 experiments\nprint()\nprint('--- All a000/a025/a050/a075/a100 experiments ---')\nfor eid, e in exps.items():\n    metrics = e.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = {}\n    prec = metrics.get('precision', '')\n    conclusion = e.get('conclusion','')\n    if any(x in eid for x in ['a000', 'a025', 'a050', 'a075', 'a100']):\n        print(f'{eid} | prec={prec} | conclusion={conclusion}')\n\" 2>&1",
    "description": "Extract precision and key metrics for dose-response experiments"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T07:24:06.450988+00:00_

interv_pred_a075_s42_fp32_v4 | prec=fp32 | status=DONE/success | d1=-7.97 | permg=6/8 | mmct=N/A
alpha_sweep_a060_s42_fp32_v3 | prec=fp32 | status=DONE/success | d1=-28.17 | permg=3/8 | mmct=N/A
alpha_sweep_a005_s42_v3 | prec=fp32 | status=DONE/success | d1=-24.86 | permg=0/8 | mmct=N/A
alpha_sweep_a010_s43_fp32 | prec=fp32 | status=DONE/success | d1=-22.08 | permg=0/8 | mmct=N/A
alpha_sweep_a005_s42 | prec=N/A | status=DONE/failed | d1=N/A | permg=N/A | mmct=N/A
alpha_sweep_a060_s42_fp32_v2 | prec=N/A | status=DONE/killed | d1=N/A | permg=N/A | mmct=N/A
alpha_sweep_a010_s43 | prec=N/A | status=DONE/success | d1=-29.1 | permg=0/8 | mmct=N/A
qwen35_08b_wiki_a100_s42 | prec=N/A | status=DONE/killed | d1=N/A | permg=N/A | mmct=N/A
smollm3_3b_wiki_a100_s42_v2 | prec=N/A | status=DONE/failed | d1=N/A | permg=N/A | mmct=N/A
interv_pred_a075_s42_fp32 | prec=N/A | status=DONE/failed | d1=N/A | permg=N/A | mmct=N/A
alpha_sweep_a060_s42_fp32 | prec=N/A | status=DONE/failed | d1=N/A | permg=N/A | mmct=N/A
scale_14b_a050_s42 | prec=N/A | status=DONE/success | d1=-36 | permg=N/A | mmct=N/A
interv_pred_a075_s42_fp32_v2 | prec=N/A | status=DONE/killed | d1=N/A | permg=N/A | mmct=N/A
smollm3_3b_wiki_a100_s42 | prec=N/A | status=DONE/killed | d1=N/A | permg=N/A | mmct=N/A
gen_gpt2m_a100_s43_bf16 | prec=N/A | status=DONE/success | d1=-33.7 | permg=1/8 | mmct=N/A
alpha_sweep_a060_s42_bf16 | prec=N/A | status=DONE/success | d1=N/A | permg=N/A | mmct={'uniform_forward': '0/8', 'uniform_bidirectional': '0/8', 'weighted_pair_forward': '6/8', 'weighted_pair_bidirectional': '6/8', 'weighted_global_forward': '0/8', 'weighted_global_bidirectional': '0/8'}
alpha_sweep_c4_a050_s42_bf16 | prec=N/A | status=DONE/success | d1=-20.3 | permg=N/A | mmct=N/A
gen_opt13b_a100_s43_bf16 | prec=N/A | status=DONE/killed | d1=N/A | permg=N/A | mmct=N/A
alpha_sweep_a010_s42_v2 | prec=N/A | status=DONE/negative | d1=N/A | permg=N/A | mmct=N/A
alpha_sweep_c4_a050_s42 | prec=N/A | status=DONE/killed | d1=N/A | p
…[truncated 3664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T07:24:06.451168+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T07:24:06.451476+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"alpha_sweep_a050_s44_fp32\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:31:02.887Z\", \"updated_at\": \"2026-05-19T05:31:51.211Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:4\"], \"pid\": \"96734\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s44_fp32.log\", \"submitted_at\": \"2026-05-19T05:31:02.665Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 44, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\"}, \"hypothesis\": \"D091: α=0.50 fp32 s44 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s42/s43.\"}, \"alpha_sweep_a050_s43_fp32\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:31:00.885Z\", \"updated_at\": \"2026-05-19T05:31:48.974Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:3\"], \"pid\": \"96593\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43_fp32.log\", \"submitted_at\": \"2026-05-19T05:31:00.668Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\"}, \"hypothesis\": \"D091: α=0.50 fp32 s43 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s42
…[truncated 7919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T07:24:06.451658+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Plan registry_ids to check\nplan_ids = {\n    'plan_001': 'alpha_sweep_a025_s42_v3',\n    'plan_001b': 'alpha_sweep_a000_s42',\n    'plan_001c': 'alpha_sweep_a050_s42',\n    'plan_001d': 'alpha_sweep_a075_s42',\n    'plan_045': 'alpha_sweep_a005_s42_v3',\n    'plan_025': 'alpha_sweep_a010_s42_fp32',\n    'plan_026': 'alpha_sweep_a060_s42_fp32_v3',\n    'plan_011': 'alpha_sweep_a025_s43',\n    'plan_012': 'alpha_sweep_a050_s43',\n    'plan_013': 'alpha_sweep_a025_s44',\n    'plan_014': 'alpha_sweep_a050_s44',\n    'plan_002': 'method_ablation_phase1',\n    'plan_002b': 'method_ablation_phase2',\n    'plan_003': 'mvp_v4_rep42',\n    'plan_006': 'plan_006_s42',\n    'plan_009': 'plan_009_bootstrap_ty',\n    'plan_015': 'generalize_pythia410m_wiki_a100_s42',\n    'plan_016': 'generalize_opt1b_wiki_a100_s42',\n    'plan_010': 'gen_wiki_gpt2m_a100_s42_v3',\n    'plan_021': 'gen_wiki_gpt2m_a100_s42_v4',\n    'plan_034': 'gen_gpt2m_a100_s43_bf16',\n    'plan_030': 'gen_opt13b_a100_s43_bf16',\n    'plan_017': 'generalize_pythia14b_wiki_a100_s42',\n    'plan_018': 'generalize_pythia14b_wiki_a100_s43',\n    'plan_027': 'scale_69b_a100_s42',\n    'plan_019': 'generalize_pythia1b_c4_a100_s42_v2',\n    'plan_020': 'generalize_pythia1b_c4_a100_s43',\n    'plan_023': 'intervention_predictive_s42',\n    'plan_024': 'intervention_reactive_s42',\n    'plan_031': 'interv_pred_s43_bf16',\n    'plan_032': 'interv_react_s43_bf16',\n    'plan_033': 'interv_pred_a075_s42_fp32_v4',\n    'plan_038': 'method_ablation_phase3',  # note: no registry_id in plan\n    'plan_039': 'alpha_sweep_a010_s43',\n    'plan_004': 'alpha_sweep_c4_a050_s42_bf16',\n    'plan_005': 'scale_14b_a050_s42',\n    'plan_041': 'smollm3_3b_wiki_a100_s42_v3',\n    'plan_042': 'qwen35_08b_wiki_a100_s42_v2',\n}\n\nprint('=== Plan registry_id status check ===')\nfor plan_id, reg_id in plan_ids.items():\n    if reg_id in exps:\n        e = exps[reg_id]\n        conclusion = e.get('conclusion','')\n        status = e.get('status','')\n        flag = ''\n        if conclusion in ('killed', 'failed', 'negative'):\n            flag = ' *** EXPIRED ***'\n        print(f'{plan_id}: {reg_id} -> {status}/{conclusion}{flag}')\n    else:\n        print(f'{plan_id}: {reg_id} -> NOT IN REGISTRY')\n\" 2>&1",
  "description": "Check plan registry_ids against registry status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Plan registry_ids to check\nplan_ids = {\n    'plan_001': 'alpha_sweep_a025_s42_v3',\n    'plan_001b': 'alpha_sweep_a000_s42',\n    'plan_001c': 'alpha_sweep_a050_s42',\n    'plan_001d': 'alpha_sweep_a075_s42',\n    'plan_045': 'alpha_sweep_a005_s42_v3',\n    'plan_025': 'alpha_sweep_a010_s42_fp32',\n    'plan_026': 'alpha_sweep_a060_s42_fp32_v3',\n    'plan_011': 'alpha_sweep_a025_s43',\n    'plan_012': 'alpha_sweep_a050_s43',\n    'plan_013': 'alpha_sweep_a025_s44',\n    'plan_014': 'alpha_sweep_a050_s44',\n    'plan_002': 'method_ablation_phase1',\n    'plan_002b': 'method_ablation_phase2',\n    'plan_003': 'mvp_v4_rep42',\n    'plan_006': 'plan_006_s42',\n    'plan_009': 'plan_009_bootstrap_ty',\n    'plan_015': 'generalize_pythia410m_wiki_a100_s42',\n    'plan_016': 'generalize_opt1b_wiki_a100_s42',\n    'plan_010': 'gen_wiki_gpt2m_a100_s42_v3',\n    'plan_021': 'gen_wiki_gpt2m_a100_s42_v4',\n    'plan_034': 'gen_gpt2m_a100_s43_bf16',\n    'plan_030': 'gen_opt13b_a100_s43_bf16',\n    'plan_017': 'generalize_pythia14b_wiki_a100_s42',\n    'plan_018': 'generalize_pythia14b_wiki_a100_s43',\n    'plan_027': 'scale_69b_a100_s42',\n    'plan_019': 'generalize_pythia1b_c4_a100_s42_v2',\n    'plan_020': 'generalize_pythia1b_c4_a100_s43',\n    'plan_023': 'intervention_predictive_s42',\n    'plan_024': 'intervention_reactive_s42',\n    'plan_031': 'interv_pred_s43_bf16',\n    'plan_032': 'interv_react_s43_bf16',\n    'plan_033': 'interv_pred_a075_s42_fp32_v4',\n    'plan_038': 'method_ablation_phase3',  # note: no registry_id in plan\n    'plan_039': 'alpha_sweep_a010_s43',\n    'plan_004': 'alpha_sweep_c4_a050_s42_bf16',\n    'plan_005': 'scale_14b_a050_s42',\n    'plan_041': 'smollm3_3b_wiki_a100_s42_v3',\n    'plan_042': 'qwen35_08b_wiki_a100_s42_v2',\n}\n\nprint('=== Plan registry_id status check ===')\nfor plan_id, reg_id in plan_ids.items():\n    if reg_id in exps:\n        e = exps[reg_id]\n        conclusion = e.get('conclusion','')\n        status = e.get('status','')\n        flag = ''\n        if conclusion in ('killed', 'failed', 'negative'):\n            flag = ' *** EXPIRED ***'\n        print(f'{plan_id}: {reg_id} -> {status}/{conclusion}{flag}')\n    else:\n        print(f'{plan_id}: {reg_id} -> NOT IN REGISTRY')\n\" 2>&1",
    "description": "Check plan registry_ids against registry status"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T07:24:06.451821+00:00_

=== Plan registry_id status check ===
plan_001: alpha_sweep_a025_s42_v3 -> NOT IN REGISTRY
plan_001b: alpha_sweep_a000_s42 -> NOT IN REGISTRY
plan_001c: alpha_sweep_a050_s42 -> NOT IN REGISTRY
plan_001d: alpha_sweep_a075_s42 -> NOT IN REGISTRY
plan_045: alpha_sweep_a005_s42_v3 -> DONE/success
plan_025: alpha_sweep_a010_s42_fp32 -> NOT IN REGISTRY
plan_026: alpha_sweep_a060_s42_fp32_v3 -> DONE/success
plan_011: alpha_sweep_a025_s43 -> DONE/success
plan_012: alpha_sweep_a050_s43 -> DONE/success
plan_013: alpha_sweep_a025_s44 -> DONE/success
plan_014: alpha_sweep_a050_s44 -> DONE/success
plan_002: method_ablation_phase1 -> NOT IN REGISTRY
plan_002b: method_ablation_phase2 -> NOT IN REGISTRY
plan_003: mvp_v4_rep42 -> DONE/success
plan_006: plan_006_s42 -> NOT IN REGISTRY
plan_009: plan_009_bootstrap_ty -> NOT IN REGISTRY
plan_015: generalize_pythia410m_wiki_a100_s42 -> DONE/success
plan_016: generalize_opt1b_wiki_a100_s42 -> DONE/success
plan_010: gen_wiki_gpt2m_a100_s42_v3 -> NOT IN REGISTRY
plan_021: gen_wiki_gpt2m_a100_s42_v4 -> DONE/success
plan_034: gen_gpt2m_a100_s43_bf16 -> DONE/success
plan_030: gen_opt13b_a100_s43_bf16 -> DONE/killed *** EXPIRED ***
plan_017: generalize_pythia14b_wiki_a100_s42 -> DONE/success
plan_018: generalize_pythia14b_wiki_a100_s43 -> DONE/success
plan_027: scale_69b_a100_s42 -> NOT IN REGISTRY
plan_019: generalize_pythia1b_c4_a100_s42_v2 -> DONE/success
plan_020: generalize_pythia1b_c4_a100_s43 -> DONE/success
plan_023: intervention_predictive_s42 -> DONE/success
plan_024: intervention_reactive_s42 -> DONE/success
plan_031: interv_pred_s43_bf16 -> DONE/success
plan_032: interv_react_s43_bf16 -> DONE/success
plan_033: interv_pred_a075_s42_fp32_v4 -> DONE/success
plan_038: method_ablation_phase3 -> DONE/success
plan_039: alpha_sweep_a010_s43 -> DONE/success
plan_004: alpha_sweep_c4_a050_s42_bf16 -> DONE/success
plan_005: scale_14b_a050_s42 -> DONE/success
plan_041: smollm3_3b_wiki_a100_s42_v3 -> NOT IN REGISTRY
plan_042: qwen35_08b_wiki_a10
…[truncated 27 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T07:24:06.452044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get detailed metrics for a000/a025 experiments (the fp16 gap)\ntargets = ['alpha_sweep_a000_s43', 'alpha_sweep_a000_s44', \n           'alpha_sweep_a025_s43', 'alpha_sweep_a025_s44',\n           'alpha_sweep_a075_s43', 'alpha_sweep_a075_s44',\n           'alpha_sweep_a050_s43', 'alpha_sweep_a050_s44']\nfor eid in targets:\n    if eid in exps:\n        e = exps[eid]\n        metrics = e.get('metrics', {})\n        conclusion = e.get('conclusion','')\n        hypothesis = (e.get('hypothesis','') or '')[:200]\n        created = e.get('created_at','')[:10]\n        print(f'=== {eid} ({conclusion}, {created}) ===')\n        print(f'  hypothesis: {hypothesis}')\n        if isinstance(metrics, dict):\n            for k,v in metrics.items():\n                print(f'  {k}: {v}')\n        print()\n\" 2>&1",
  "description": "Get detailed metrics for fp16 gap experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/03d5af73-1683-4f7f-b98e-711760aaa332/tool-results/mcp-agent-ml-research-read_registry-1779175042961.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get detailed metrics for a000/a025 experiments (the fp16 gap)\ntargets = ['alpha_sweep_a000_s43', 'alpha_sweep_a000_s44', \n           'alpha_sweep_a025_s43', 'alpha_sweep_a025_s44',\n           'alpha_sweep_a075_s43', 'alpha_sweep_a075_s44',\n           'alpha_sweep_a050_s43', 'alpha_sweep_a050_s44']\nfor eid in targets:\n    if eid in exps:\n        e = exps[eid]\n        metrics = e.get('metrics', {})\n        conclusion = e.get('conclusion','')\n        hypothesis = (e.get('hypothesis','') or '')[:200]\n        created = e.get('created_at','')[:10]\n        print(f'=== {eid} ({conclusion}, {created}) ===')\n        print(f'  hypothesis: {hypothesis}')\n        if isinstance(metrics, dict):\n            for k,v in metrics.items():\n                print(f'  {k}: {v}')\n        print()\n\" 2>&1",
    "description": "Get detailed metrics for fp16 gap experiments"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T07:24:06.452216+00:00_

=== alpha_sweep_a000_s43 (success, 2026-05-16) ===
  hypothesis: α=0.0 null control multi-seed: 无合成数据再训练在跨 seed 复现下仍不产生 spurious causal signal（PermG FDR 0/8），证实 signal 源于合成污染而非训练随机性
  gen0: {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.0983, 'distinct_2': 0.5132, 'distinct_3': 0.8057, 'effective_rank': 46.613}
  gen10: {'token_entropy': 3.0907, 'ece': 0.0148, 'perplexity': 21.469, 'distinct_1': 0.0847, 'distinct_2': 0.4631, 'distinct_3': 0.7672, 'effective_rank': 43.72}
  drift_pct: {'token_entropy': -4.4, 'ece': 37.2, 'perplexity': -20.3, 'distinct_1': -13.9, 'distinct_2': -9.8, 'distinct_3': -4.8, 'effective_rank': -6.2}
  five_method: {'perm_granger_fdr_sig': '0/8', 'ty_sig': '1/8 (df_resid=1 unreliable)', 'robust_pairs_ge3': '0/8', 'fpr_controlled': True}

=== alpha_sweep_a000_s44 (success, 2026-05-16) ===
  hypothesis: α=0.0 null control multi-seed: 无合成数据再训练在跨 seed 复现下仍不产生 spurious causal signal（PermG FDR 0/8），证实 signal 源于合成污染而非训练随机性
  gen0: {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.0981, 'distinct_2': 0.5132, 'distinct_3': 0.8058, 'effective_rank': 46.613}
  gen10: {'token_entropy': 3.0957, 'ece': 0.0134, 'perplexity': 21.616, 'distinct_1': 0.0838, 'distinct_2': 0.4665, 'distinct_3': 0.7749, 'effective_rank': 44.498}
  drift_pct: {'token_entropy': -4.3, 'ece': 24, 'perplexity': -19.8, 'distinct_1': -14.6, 'distinct_2': -9.1, 'distinct_3': -3.8, 'effective_rank': -4.5}
  five_method: {'perm_granger_fdr_sig': '0/8', 'ty_sig': '0/8', 'robust_pairs_ge3': '0/8', 'fpr_controlled': True}

=== alpha_sweep_a025_s43 (success, 2026-05-15) ===
  hypothesis: α=0.25 multi-seed 复现: 低污染下 diversity collapse (40-59%) 但无 Granger causal signal (0/8 PermG) 的模式跨种子稳定，定义 sub-threshold regime 下界
  gen0: {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.09833, 'distinct_2': 0.5132, 'distinct_3': 0.8057, 'effective_rank': 46.61, 'mauve': 0.03351}
  gen10: {'token_entropy': 3.0723, 'ece': 0
…[truncated 3262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T07:24:06.452466+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "distrib_canary_collapse",
  "file": "report.md",
  "content": "# Dose-Response Map fp32 缺口分析报告\n\n> 生成时间: 2026-05-19 ~06:00 UTC\n\n## 1. Dose-Response Map 逐 α Provenance 状态\n\n| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |\n|---|-----------|-------------------|-------|----------|--------|-------------|\n| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |\n| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |\n| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |\n| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |\n| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |\n| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |\n| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |\n| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |\n\n## 2. fp16 缺口详情\n\n### α=0.25 (P0 — dose-response 主轴 gap)\n- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)\n- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。\n- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点，fp16 provenance 削弱可信度。\n\n### α=0.00 (P0 — FPR ground truth)\n- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)\n- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。\n- **影响**: Claim 3 (FPR control) 的基础数据，fp16 provenance 使 FPR=0 claim 有精度争议风险。\n\n### α=0.75 (P2 — 低优先)\n- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%, PermG 高), alpha_sweep_a075_s44 (d1=-31.8%)\n- **信号强度**: PermG ~83%、drift ~32%，信号足够强，fp16→fp32 不太可能翻转结论。\n- **建议**: 如果 GPU 资源在 α=0.00/0.25 fp32 完成后仍有余裕，可补跑。\n\n## 3. α=0.25 fp32 重跑建议\n\n**3 seeds × ~4h each = ~12 GPU-hours**\n\n```bash\n# seed=42\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.25 \\\n  --output_dir results/alpha_sweep/a025_s42_fp32\n\n# seed=43\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.25 \\\n  --output_dir results/alpha_sweep/a025_s43_fp32\n\n# seed=44\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.25 \\\n  --output_dir results/alpha_sweep/a025_s44_fp32\n```\n\n- **预估时间**: ~4-5h/seed (Pythia-410M, 10 gen, 5k steps/gen)\n- **GPU**: 3 空闲 GPU 并行 → ~5h 全部完成\n- **Registry ID**: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32\n- **前置**: 需等 α=0.50 fp32 × 3 完成释放 GPU (~10:30 UTC)\n\n## 4. α=0.00 fp32 重跑建议\n\n**3 seeds × ~4h each = ~12 GPU-hours**\n\n```bash\n# seed=42\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.00 \\\n  --output_dir results/alpha_sweep/a000_s42_fp32\n\n# seed=43\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.00 \\\n  --output_dir results/alpha_sweep/a000_s43_fp32\n\n# seed=44\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.00 \\\n  --output_dir results/alpha_sweep/a000_s44_fp32\n```\n\n- **预估时间**: ~4-5h/seed\n- **Registry ID**: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32\n- **可与 α=0.25 并行**: 共需 6 GPU，可在 α=0.50 fp32 + a010_s42 + scale_69b 完成后启动\n\n## 5. experiment_plan.yaml 过期 registry_id（6 条）\n\n| Plan ID | 当前 registry_id | 状态 | 建议修复 |\n|---------|-----------------|------|----------|\n| plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a025_s42_fp32 |\n| plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a000_s42_fp32 |\n| plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | 更新为 alpha_sweep_a050_s42_fp32 (RUNNING) |\n| plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |\n| plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded) | ✅ 更新为 gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |\n| plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 OPT-1.3B s43 实验 |\n\n## 6. GPU 调度建议\n\n当前 8/8 满载。释放顺序预估：\n1. **~07:00 UTC**: scale_69b (cuda:0) 完成 → 1 GPU 释放\n2. **~10:30 UTC**: a050 fp32 × 3 (cuda:2/3/4) + a010_s42 (cuda:5) 完成 → 4 GPU 释放\n3. **qwen35/gpt2m_s43/smollm3**: 时间不确定，但预计 05-19 内完成\n\nα=0.25 + α=0.00 共 6 seeds → 需 6 GPU 并行。最早可在 ~10:30 UTC（a050 完成后）启动全部 6 个。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "report.md",
    "content": "# Dose-Response Map fp32 缺口分析报告\n\n> 生成时间: 2026-05-19 ~06:00 UTC\n\n## 1. Dose-Response Map 逐 α Provenance 状态\n\n| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |\n|---|-----------|-------------------|-------|----------|--------|-------------|\n| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |\n| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |\n| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |\n| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |\n| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |\n| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |\n| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |\n| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |\n\n## 2. fp16 缺口详情\n\n### α=0.25 (P0 — dose-response 主轴 gap)\n- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)\n- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。\n- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点，fp16 provenance 削弱可信度。\n\n### α=0.00 (P0 — FPR ground truth)\n- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)\n- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。\n- **影响**: Claim 3 (FPR control) 的基础数据，fp16 provenance 使 FPR=0 claim 有精度争议风险。\n\n### α=0.75 (P2 — 低优先)\n- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%, PermG 高), alpha_sweep_a075_s44 (d1=-31.8%)\n- **信号强度**: PermG ~83%、drift ~32%，信号足够强，fp16→fp32 不太可能翻转结论。\n- **建议**: 如果 GPU 资源在 α=0.00/0.25 fp32 完成后仍有余裕，可补跑。\n\n## 3. α=0.25 fp32 重跑建议\n\n**3 seeds × ~4h each = ~12 GPU-hours**\n\n```bash\n# seed=42\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.25 \\\n  --output_dir results/alpha_sweep/a025_s42_fp32\n\n# seed=43\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.25 \\\n  --output_dir results/alpha_sweep/a025_s43_fp32\n\n# seed=44\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.25 \\\n  --output_dir results/alpha_sweep/a025_s44_fp32\n```\n\n- **预估时间**: ~4-5h/seed (Pythia-410M, 10 gen, 5k steps/gen)\n- **GPU**: 3 空闲 GPU 并行 → ~5h 全部完成\n- **Registry ID**: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32\n- **前置**: 需等 α=0.50 fp32 × 3 完成释放 GPU (~10:30 UTC)\n\n## 4. α=0.00 fp32 重跑建议\n\n**3 seeds × ~4h each = ~12 GPU-hours**\n\n```bash\n# seed=42\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.00 \\\n  --output_dir results/alpha_sweep/a000_s42_fp32\n\n# seed=43\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.00 \\\n  --output_dir results/alpha_sweep/a000_s43_fp32\n\n# seed=44\npython -u iterative_train.py \\\n  --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 \\\n  --num_generations 10 --synthetic_ratio 0.00 \\\n  --output_dir results/alpha_sweep/a000_s44_fp32\n```\n\n- **预估时间**: ~4-5h/seed\n- **Registry ID**: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32\n- **可与 α=0.25 并行**: 共需 6 GPU，可在 α=0.50 fp32 + a010_s42 + scale_69b 完成后启动\n\n## 5. experiment_plan.yaml 过期 registry_id（6 条）\n\n| Plan ID | 当前 registry_id | 状态 | 建议修复 |\n|---------|-----------------|------|----------|\n| plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a025_s42_fp32 |\n| plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a000_s42_fp32 |\n| plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | 更新为 alpha_sweep_a050_s42_fp32 (RUNNING) |\n| plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |\n| plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded) | ✅ 更新为 gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |\n| plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 OPT-1.3B s43 实验 |\n\n## 6. GPU 调度建议\n\n当前 8/8 满载。释放顺序预估：\n1. **~07:00 UTC**: scale_69b (cuda:0) 完成 → 1 GPU 释放\n2. **~10:30 UTC**: a050 fp32 × 3 (cuda:2/3/4) + a010_s42 (cuda:5) 完成 → 4 GPU 释放\n3. **qwen35/gpt2m_s43/smollm3**: 时间不确定，但预计 05-19 内完成\n\nα=0.25 + α=0.00 共 6 seeds → 需 6 GPU 并行。最早可在 ~10:30 UTC（a050 完成后）启动全部 6 个。\n"
  }
}
````

</details>

---

### Tool result

_source line 30 · 2026-05-19T07:24:06.452663+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'report.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use (auto-generated, not manually writable) instead.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T07:24:06.452822+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "distrib_canary_collapse",
  "file": "report_dose_response_gaps.md",
  "content": "# Dose-Response Map fp32 缺口分析报告\n\n> 生成时间: 2026-05-19 ~06:00 UTC\n\n## 1. Dose-Response Map 逐 α Provenance 状态\n\n| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |\n|---|-----------|-------------------|-------|----------|--------|-------------|\n| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |\n| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |\n| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |\n| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |\n| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |\n| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |\n| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |\n| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |\n\n## 2. fp16 缺口详情\n\n### α=0.25 (P0)\n- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)\n- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。\n- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点。\n\n### α=0.00 (P0)\n- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)\n- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。\n- **影响**: Claim 3 (FPR control) 的基础数据。\n\n### α=0.75 (P2)\n- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%), alpha_sweep_a075_s44 (d1=-31.8%)\n- **信号强度**: PermG ~83%，drift ~32%，fp16→fp32 不太可能翻转结论。低优先。\n\n## 3. α=0.25 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32\n\n## 4. α=0.00 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32\n\n最早启动时间: ~10:30 UTC（a050 fp32 × 3 完成释放 cuda:2/3/4 后），6 seeds 并行 ~5h 完成。\n\n## 5. experiment_plan.yaml 过期 registry_id（6 条）\n\n| Plan ID | 当前 registry_id | 状态 | 修复动作 |\n|---------|-----------------|------|----------|\n| plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑 |\n| plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑 |\n| plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | → alpha_sweep_a050_s42_fp32 (RUNNING) |\n| plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |\n| plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded) | → gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |\n| plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "report_dose_response_gaps.md",
    "content": "# Dose-Response Map fp32 缺口分析报告\n\n> 生成时间: 2026-05-19 ~06:00 UTC\n\n## 1. Dose-Response Map 逐 α Provenance 状态\n\n| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |\n|---|-----------|-------------------|-------|----------|--------|-------------|\n| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |\n| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |\n| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |\n| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |\n| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |\n| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |\n| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |\n| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |\n\n## 2. fp16 缺口详情\n\n### α=0.25 (P0)\n- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)\n- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。\n- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点。\n\n### α=0.00 (P0)\n- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)\n- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。\n- **影响**: Claim 3 (FPR control) 的基础数据。\n\n### α=0.75 (P2)\n- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%), alpha_sweep_a075_s44 (d1=-31.8%)\n- **信号强度**: PermG ~83%，drift ~32%，fp16→fp32 不太可能翻转结论。低优先。\n\n## 3. α=0.25 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32\n\n## 4. α=0.00 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32\n\n最早启动时间: ~10:30 UTC（a050 fp32 × 3 完成释放 cuda:2/3/4 后），6 seeds 并行 ~5h 完成。\n\n## 5. experiment_plan.yaml 过期 registry_id（6 条）\n\n| Plan ID | 当前 registry_id | 状态 | 修复动作 |\n|---------|-----------------|------|----------|\n| plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑 |\n| plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑 |\n| plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | → alpha_sweep_a050_s42_fp32 (RUNNING) |\n| plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |\n| plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded) | → gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |\n| plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 |\n"
  }
}
````

</details>

---

### Tool result

_source line 32 · 2026-05-19T07:24:06.452996+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'report_dose_response_gaps.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T07:24:06.453141+00:00_

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
  "session": "worker_analysis_dose-response-gap_20260519T071655",
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

_source line 34 · 2026-05-19T07:24:06.453280+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T07:24:06.453440+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

````json
{
  "name": "report_dose_response_gaps",
  "type": "report",
  "description": "Dose-response map fp32 缺口分析：逐 α provenance 状态、fp16 缺口详情、α=0.00/0.25 fp32 重跑规格、experiment_plan.yaml 6 条过期 registry_id 清单",
  "project": "distrib_canary_collapse",
  "content": "# Dose-Response Map fp32 缺口分析报告\n\n> 生成时间: 2026-05-19 ~06:00 UTC\n\n## 1. Dose-Response Map 逐 α Provenance 状态\n\n| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |\n|---|-----------|-------------------|-------|----------|--------|-------------|\n| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |\n| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |\n| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |\n| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |\n| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |\n| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |\n| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |\n| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |\n\n**fp32 覆盖率**: 8 点中 3 点 ✅ fp32 (0.05, 0.60, 1.00)，1 点部分 fp32 (0.10)，1 点 RUNNING (0.50)，3 点 fp16 (0.00, 0.25, 0.75)。\n\n## 2. fp16 缺口详情\n\n### α=0.25 (P0 — dose-response 主轴 gap)\n- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)\n- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。\n- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点。\n\n### α=0.00 (P0 — FPR ground truth)\n- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)\n- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。\n- **影响**: Claim 3 (FPR control) 的基础数据。\n\n### α=0.75 (P2 — 低优先)\n- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%), alpha_sweep_a075_s44 (d1=-31.8%)\n- **信号强度**: PermG ~83%，drift ~32%，fp16→fp32 不太可能翻转结论。低优先。\n\n## 3. α=0.25 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32\n\n## 4. α=0.00 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32\n\n最早启动时间: ~10:30 UTC（a050 fp32 × 3 完成释放 cuda:2/3/4 后），6 seeds 并行 ~5h 完成。\n\n## 5. experiment_plan.yaml 过期 registry_id（6 条）\n\n| # | Plan ID | 当前 registry_id | 状态 | 修复动作 |\n|---|---------|-----------------|------|----------|\n| 1 | plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a025_s42_fp32 |\n| 2 | plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a000_s42_fp32 |\n| 3 | plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | → alpha_sweep_a050_s42_fp32 (RUNNING) |\n| 4 | plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |\n| 5 | plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded by v4) | ✅ → gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |\n| 6 | plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 OPT-1.3B s43 |\n\n## 6. GPU 调度建议\n\n当前 8/8 满载。释放顺序预估：\n1. **~07:00 UTC**: scale_69b (cuda:0) 完成 → 1 GPU 释放\n2. **~10:30 UTC**: a050 fp32 × 3 (cuda:2/3/4) + a010_s42 (cuda:5) 完成 → 4 GPU 释放\n3. **qwen35/gpt2m_s43/smollm3**: 时间不确定，预计 05-19 内完成\n\nα=0.25 + α=0.00 共 6 seeds → 需 6 GPU 并行。最早 ~10:30 UTC 启动全部。~15:30 UTC 全部完成后 dose-response map 达到 7/8 fp32 覆盖（仅 α=0.75 仍 fp16）。",
  "content_filename": "report_dose_response_gaps.md",
  "tags": "['dose-response', 'fp32', 'gap-analysis', 'D091', 'D092']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "report_dose_response_gaps",
    "type": "report",
    "description": "Dose-response map fp32 缺口分析：逐 α provenance 状态、fp16 缺口详情、α=0.00/0.25 fp32 重跑规格、experiment_plan.yaml 6 条过期 registry_id 清单",
    "project": "distrib_canary_collapse",
    "content": "# Dose-Response Map fp32 缺口分析报告\n\n> 生成时间: 2026-05-19 ~06:00 UTC\n\n## 1. Dose-Response Map 逐 α Provenance 状态\n\n| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |\n|---|-----------|-------------------|-------|----------|--------|-------------|\n| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |\n| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |\n| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |\n| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |\n| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |\n| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |\n| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |\n| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |\n\n**fp32 覆盖率**: 8 点中 3 点 ✅ fp32 (0.05, 0.60, 1.00)，1 点部分 fp32 (0.10)，1 点 RUNNING (0.50)，3 点 fp16 (0.00, 0.25, 0.75)。\n\n## 2. fp16 缺口详情\n\n### α=0.25 (P0 — dose-response 主轴 gap)\n- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)\n- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。\n- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点。\n\n### α=0.00 (P0 — FPR ground truth)\n- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)\n- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。\n- **影响**: Claim 3 (FPR control) 的基础数据。\n\n### α=0.75 (P2 — 低优先)\n- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%), alpha_sweep_a075_s44 (d1=-31.8%)\n- **信号强度**: PermG ~83%，drift ~32%，fp16→fp32 不太可能翻转结论。低优先。\n\n## 3. α=0.25 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32\n\n## 4. α=0.00 fp32 重跑建议\n\n3 seeds × ~4-5h = ~12-15 GPU-hours\n\n```bash\n# seed=42\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s42_fp32\n\n# seed=43\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s43_fp32\n\n# seed=44\npython -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \\\n  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \\\n  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s44_fp32\n```\n\nRegistry ID: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32\n\n最早启动时间: ~10:30 UTC（a050 fp32 × 3 完成释放 cuda:2/3/4 后），6 seeds 并行 ~5h 完成。\n\n## 5. experiment_plan.yaml 过期 registry_id（6 条）\n\n| # | Plan ID | 当前 registry_id | 状态 | 修复动作 |\n|---|---------|-----------------|------|----------|\n| 1 | plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a025_s42_fp32 |\n| 2 | plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a000_s42_fp32 |\n| 3 | plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | → alpha_sweep_a050_s42_fp32 (RUNNING) |\n| 4 | plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |\n| 5 | plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded by v4) | ✅ → gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |\n| 6 | plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 OPT-1.3B s43 |\n\n## 6. GPU 调度建议\n\n当前 8/8 满载。释放顺序预估：\n1. **~07:00 UTC**: scale_69b (cuda:0) 完成 → 1 GPU 释放\n2. **~10:30 UTC**: a050 fp32 × 3 (cuda:2/3/4) + a010_s42 (cuda:5) 完成 → 4 GPU 释放\n3. **qwen35/gpt2m_s43/smollm3**: 时间不确定，预计 05-19 内完成\n\nα=0.25 + α=0.00 共 6 seeds → 需 6 GPU 并行。最早 ~10:30 UTC 启动全部。~15:30 UTC 全部完成后 dose-response map 达到 7/8 fp32 覆盖（仅 α=0.75 仍 fp16）。",
    "content_filename": "report_dose_response_gaps.md",
    "tags": "['dose-response', 'fp32', 'gap-analysis', 'D091', 'D092']"
  }
}
````

</details>

---

### Tool result

_source line 36 · 2026-05-19T07:24:06.453653+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_4b0a1a\", \"name\": \"report_dose_response_gaps\", \"type\": \"report\", \"description\": \"Dose-response map fp32 缺口分析：逐 α provenance 状态、fp16 缺口详情、α=0.00/0.25 fp32 重跑规格、experiment_plan.yaml 6 条过期 registry_id 清单\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/report_dose_response_gaps.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T07:23:11.152660+00:00\", \"tags\": [\"dose-response\", \"fp32\", \"gap-analysis\", \"D091\", \"D092\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T07:24:06.453810+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "old_string": "  registry_id: alpha_sweep_a025_s42_v3\n- id: plan_001b\n  claim: 3\n  description: 'α=0.0 null control: Pythia-410M × WikiText-103 × α=0.0 × 10 gen ×\n    seed=42。FPR ground truth'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  notes: 'D028: perm_granger/TY 0% FPR，naive 100% FPR'\n  registry_id: alpha_sweep_a000_s42",
  "new_string": "  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a025_s42_fp32\n- id: plan_001b\n  claim: 3\n  description: 'α=0.0 null control: Pythia-410M × WikiText-103 × α=0.0 × 10 gen ×\n    seed=42。FPR ground truth'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  notes: 'D028: perm_granger/TY 0% FPR，naive 100% FPR'\n  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a000_s42_fp32"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "old_string": "  registry_id: alpha_sweep_a025_s42_v3\n- id: plan_001b\n  claim: 3\n  description: 'α=0.0 null control: Pythia-410M × WikiText-103 × α=0.0 × 10 gen ×\n    seed=42。FPR ground truth'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  notes: 'D028: perm_granger/TY 0% FPR，naive 100% FPR'\n  registry_id: alpha_sweep_a000_s42",
    "new_string": "  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a025_s42_fp32\n- id: plan_001b\n  claim: 3\n  description: 'α=0.0 null control: Pythia-410M × WikiText-103 × α=0.0 × 10 gen ×\n    seed=42。FPR ground truth'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  notes: 'D028: perm_granger/TY 0% FPR，naive 100% FPR'\n  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a000_s42_fp32"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T07:24:06.453995+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T07:24:06.454125+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "old_string": "  registry_id: alpha_sweep_a050_s42",
  "new_string": "  registry_id: alpha_sweep_a050_s42_fp32  # fp16→fp32 RUNNING (D091)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "old_string": "  registry_id: alpha_sweep_a050_s42",
    "new_string": "  registry_id: alpha_sweep_a050_s42_fp32  # fp16→fp32 RUNNING (D091)"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T07:24:06.454317+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T07:24:06.454462+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "old_string": "  registry_id: alpha_sweep_a075_s42",
  "new_string": "  registry_id: null  # fp16 expired; 低优先 fp32 重跑"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "old_string": "  registry_id: alpha_sweep_a075_s42",
    "new_string": "  registry_id: null  # fp16 expired; 低优先 fp32 重跑"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T07:24:06.454628+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T07:24:06.454751+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "old_string": "  registry_id: gen_wiki_gpt2m_a100_s42_v3",
  "new_string": "  registry_id: gen_wiki_gpt2m_a100_s42_v4  # v3→v4 统一参数重跑 (DONE/success)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "old_string": "  registry_id: gen_wiki_gpt2m_a100_s42_v3",
    "new_string": "  registry_id: gen_wiki_gpt2m_a100_s42_v4  # v3→v4 统一参数重跑 (DONE/success)"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T07:24:06.454911+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T07:24:06.455032+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "old_string": "  registry_id: gen_opt13b_a100_s43_bf16",
  "new_string": "  registry_id: null  # killed; 需重新安排 OPT-1.3B s43"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "old_string": "  registry_id: gen_opt13b_a100_s43_bf16",
    "new_string": "  registry_id: null  # killed; 需重新安排 OPT-1.3B s43"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T07:24:06.455191+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T07:24:06.455362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T07:24:06.455509+00:00_

1	experiments:
2	- id: plan_001
3	  claim: 2
4	  description: 'α-sweep anchor: Pythia-410M × WikiText-103 × α=0.25 × 10 gen × seed=42'
5	  priority: P0
6	  gpu_budget_hours: 4
7	  deps: []
8	  notes: α-sweep 基准实验。D025 统一参数。
9	  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a025_s42_fp32
10	- id: plan_001b
11	  claim: 3
12	  description: 'α=0.0 null control: Pythia-410M × WikiText-103 × α=0.0 × 10 gen ×
13	    seed=42。FPR ground truth'
14	  priority: P0
15	  gpu_budget_hours: 4
16	  deps: []
17	  notes: 'D028: perm_granger/TY 0% FPR，naive 100% FPR'
18	  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a000_s42_fp32
19	- id: plan_001c
20	  claim: 2
21	  description: 'α=0.50 sweep: Pythia-410M × WikiText-103 × α=0.50 × 10 gen × seed=42'
22	  priority: P0
23	  gpu_budget_hours: 4
24	  deps: []
25	  notes: 'D025: 所有严格方法 FDR 后归零（0/8），仅 naive 8/8。α=0.50 是 method×regime interaction
26	    最极端例证'
27	  registry_id: alpha_sweep_a050_s42_fp32  # fp16→fp32 RUNNING (D091)
28	- id: plan_001d
29	  claim: 1
30	  description: 'α=0.75 sweep: Pythia-410M × WikiText-103 × α=0.75 × 10 gen × seed=42'
31	  priority: P0
32	  gpu_budget_hours: 4
33	  deps: []
34	  notes: 'D037: 3/4 FDR-sig forward, 0/4 reverse, consensus 11/16 robust'
35	  registry_id: null  # fp16 expired; 低优先 fp32 重跑
36	- id: plan_045
37	  claim: 2
38	  description: 'α=0.05 sweep: Pythia-410M × WikiText-103 × α=0.05 × 10 gen × seed=42。定位
39	    diversity 悬崖精确位置（α=0.00 d1=-14% → α=0.10 d1=-40% 之间的断崖）'
40	  priority: P0
41	  gpu_budget_hours: 4
42	  deps: []
43	  notes: 'D076: HIGH ROI。如果 α=0.05 d1≈-40% → 5% 污染即全损；如果 d1 在 -14% 和 -40% 之间 → 存在明确阈值'
44	  registry_id: alpha_sweep_a005_s42_v3
45	- id: plan_025
46	  claim: 2
47	  description: 'α=0.10 sweep: Pythia-410M × WikiText-103 × α=0.10 × 10 gen × seed=42。Regime
48	    map 下界，验证极低污染下 signal 是否存在'
49	  priority: P0
50	  gpu_budget_hours: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T07:24:06.455657+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'registry_id' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
  "description": "Verify all registry_id entries in experiment plan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'registry_id' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml",
    "description": "Verify all registry_id entries in experiment plan"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T07:24:06.455789+00:00_

9:  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a025_s42_fp32
18:  registry_id: null  # fp16 expired; 待 fp32 重跑 → alpha_sweep_a000_s42_fp32
27:  registry_id: alpha_sweep_a050_s42_fp32  # fp16→fp32 RUNNING (D091)
35:  registry_id: null  # fp16 expired; 低优先 fp32 重跑
44:  registry_id: alpha_sweep_a005_s42_v3
53:  registry_id: alpha_sweep_a010_s42_fp32
62:  registry_id: alpha_sweep_a060_s42_fp32_v3
72:  registry_id: alpha_sweep_a025_s43
82:  registry_id: alpha_sweep_a050_s43
90:  registry_id: alpha_sweep_a025_s44
100:  registry_id: alpha_sweep_a050_s44
109:  registry_id: method_ablation_phase1
123:  registry_id: method_ablation_phase2
130:  registry_id: mvp_v4_rep42
139:  registry_id: plan_006_s42
148:  registry_id: plan_009_bootstrap_ty
157:  registry_id: generalize_pythia410m_wiki_a100_s42
165:  registry_id: generalize_opt1b_wiki_a100_s42
174:  registry_id: gen_wiki_gpt2m_a100_s42_v4  # v3→v4 统一参数重跑 (DONE/success)
184:  registry_id: gen_wiki_gpt2m_a100_s42_v4
194:  registry_id: gen_gpt2m_a100_s43_bf16
203:  registry_id: null  # killed; 需重新安排 OPT-1.3B s43
211:  registry_id: generalize_pythia14b_wiki_a100_s42
220:  registry_id: generalize_pythia14b_wiki_a100_s43
232:  registry_id: scale_69b_a100_s42
264:  registry_id: generalize_pythia1b_c4_a100_s42_v2
273:  registry_id: generalize_pythia1b_c4_a100_s43
301:  registry_id: intervention_predictive_s42
311:  registry_id: intervention_reactive_s42
320:  registry_id: interv_pred_s43_bf16
329:  registry_id: interv_react_s43_bf16
340:  registry_id: interv_pred_a075_s42_fp32_v4
378:  registry_id: alpha_sweep_a010_s43
395:  registry_id: alpha_sweep_c4_a050_s42_bf16
404:  registry_id: scale_14b_a050_s42
424:  registry_id: smollm3_3b_wiki_a100_s42_v3
433:  registry_id: qwen35_08b_wiki_a100_s42_v2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_dose-response-gap_20260519T071655",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-19T07:24:06.455991+00:00_

全部完成。

## 汇总

### 报告已注册
`art_20260519_4b0a1a` → `artifacts/_project/report/report_dose_response_gaps.md`

### Dose-Response Map fp32 状态
- **✅ fp32 完成**: α=0.05, 0.60, 1.00（3/8 点）
- **部分 fp32**: α=0.10（s43 done, s42 RUNNING）
- **RUNNING**: α=0.50（3 seeds fp32, ~10:30 UTC 完成）
- **fp16 缺口**: α=0.00（3 seeds）、α=0.25（3 seeds）、α=0.75（低优先）

### experiment_plan.yaml 6 条过期指针已修复
| Plan ID | 修复 |
|---------|------|
| plan_001 (α=0.25 s42) | `alpha_sweep_a025_s42_v3` → `null`（待 fp32 重跑）|
| plan_001b (α=0.00 s42) | `alpha_sweep_a000_s42` → `null`（待 fp32 重跑）|
| plan_001c (α=0.50 s42) | `alpha_sweep_a050_s42` → `alpha_sweep_a050_s42_fp32`（RUNNING）|
| plan_001d (α=0.75 s42) | `alpha_sweep_a075_s42` → `null`（低优先）|
| plan_010 (GPT-2m) | `gen_wiki_gpt2m_a100_s42_v3` → `gen_wiki_gpt2m_a100_s42_v4`（success）|
| plan_030 (OPT-1.3B s43) | `gen_opt13b_a100_s43_bf16` → `null`（killed，需重排）|

### 下一步
α=0.00 + α=0.25 共 6 seeds fp32 重跑，最早 ~10:30 UTC（a050 完成释放 GPU 后）启动，~15:30 UTC 完成。完成后 map 达 7/8 fp32 覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_dose-response-gap_20260519T071655"
}
```

</details>

---
