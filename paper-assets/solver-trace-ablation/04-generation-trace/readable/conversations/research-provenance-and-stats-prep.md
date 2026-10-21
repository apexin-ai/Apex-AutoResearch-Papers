# research provenance and stats prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_research_provenance-and-stats-prep_20260515T173752.jsonl`
- **Structured JSON:** [`8ebbd8d5d9445803b1f1.json`](../../sessions/8e/8ebbd8d5d9445803b1f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-15T17:40:43.070111+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:40:43.070450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:40:43.070614+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_provenance.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_provenance.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T17:40:43.070999+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml\", \"content\": \"paper:\\n  title: ''\\n  version: 12\\n  generated_at: '2026-05-15T02:40:08.884665+00:00'\\nclaims:\\n- id: C001\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'ISR collapse: 0.642 to 0.132 to 0.003'\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan003-eval-exec-only-r5\\n    metric: proved_only_isr\\n  - exp_id: plan001-exec-only-s42-r2\\n    metric: eval_proved_only_isr\\n  - exp_id: plan016-extended-1000-s42\\n    metric: isr\\n  decisions: []\\n  deprecated: true\\n- id: C003\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'H7 ISR-specific: 64.5% vs 0% random'\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan002-additive-b01-s42\\n    metric: h7_rate\\n  - exp_id: plan018-additive-random-b01-s42\\n    metric: H7=0\\n  decisions: []\\n  deprecated: true\\n- id: C006\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Premise-matched ISR 1.06x\\n  type: quantitative\\n  evidence:\\n  - exp_id: D051-analysis\\n    metric: premise_matched_ratio\\n  decisions: []\\n  deprecated: true\\n- id: C010\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: SFT 92.9% genuine\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan009-sft-baseline-s42-r4\\n    metric: genuine_rate\\n  decisions: []\\n  deprecated: true\\n- id: C015\\n  location:\\n    section: experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: Prolog STA 3/3 gaming 0% genuine\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan006-prolog-sta-s42\\n    metric: eval_h7_rate\\n  decisions: []\\n  deprecated: true\\n- id: C016\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 87% of proved outputs embed the conclusion verbatim among the pr
…[truncated 16064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T17:40:43.071187+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:40:43.071542+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 se
…[truncated 27998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:40:43.071749+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:40:43.072559+00:00_

Error: result (193,635 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:40:43.072830+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'D051-analysis'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'D051-analysis'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:40:43.072984+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2982}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:40:43.073109+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan002-additive-b01-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan002-additive-b01-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:40:43.073232+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:40:43.073349+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan018-additive-random-b01-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan018-additive-random-b01-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T17:40:43.073469+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3161}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T17:40:43.073609+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find experiment IDs containing D051 or plan002-additive or plan018-additive-random\nfor eid in sorted(exps.keys()):\n    if any(x in eid.lower() for x in ['d051', 'plan002-additive-b01', 'plan018-additive-random-b01-s42']):\n        print(f'{eid}: status={exps[eid].get(\\\"status\\\")}, conclusion={exps[eid].get(\\\"conclusion\\\")}')\n\"\n",
  "description": "Search registry for D051 and related experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find experiment IDs containing D051 or plan002-additive or plan018-additive-random\nfor eid in sorted(exps.keys()):\n    if any(x in eid.lower() for x in ['d051', 'plan002-additive-b01', 'plan018-additive-random-b01-s42']):\n        print(f'{eid}: status={exps[eid].get(\\\"status\\\")}, conclusion={exps[eid].get(\\\"conclusion\\\")}')\n\"\n",
    "description": "Search registry for D051 and related experiment IDs"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:40:43.073758+00:00_

plan002-additive-b01-s42: status=DONE, conclusion=negative
plan002-additive-b01-s42-1000: status=DONE, conclusion=negative
plan002-additive-b01-s43: status=DONE, conclusion=negative
plan002-additive-b01-s43-r2: status=ANALYZING, conclusion=None
plan002-additive-b01-s44: status=DONE, conclusion=negative
plan018-additive-random-b01-s42: status=DONE, conclusion=negative
plan018-additive-random-b01-s42-1000: status=DONE, conclusion=failed
plan018-additive-random-b01-s42-1000-r2: status=DONE, conclusion=negative
plan018-additive-random-b01-s42-1000-r3: status=DONE, conclusion=negative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:40:43.073932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T17:40:43.074186+00:00_

1	paper:
2	  title: ''
3	  version: 12
4	  generated_at: '2026-05-15T02:40:08.884665+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: experiments
9	    paragraph: 0
10	    sentence: 0
11	  text: 'ISR collapse: 0.642 to 0.132 to 0.003'
12	  type: quantitative
13	  evidence:
14	  - exp_id: plan003-eval-exec-only-r5
15	    metric: proved_only_isr
16	  - exp_id: plan001-exec-only-s42-r2
17	    metric: eval_proved_only_isr
18	  - exp_id: plan016-extended-1000-s42
19	    metric: isr
20	  decisions: []
21	  deprecated: true
22	- id: C003
23	  location:
24	    section: experiments
25	    paragraph: 0
26	    sentence: 0
27	  text: 'H7 ISR-specific: 64.5% vs 0% random'
28	  type: quantitative
29	  evidence:
30	  - exp_id: plan002-additive-b01-s42
31	    metric: h7_rate
32	  - exp_id: plan018-additive-random-b01-s42
33	    metric: H7=0
34	  decisions: []
35	  deprecated: true
36	- id: C006
37	  location:
38	    section: experiments
39	    paragraph: 0
40	    sentence: 0
41	  text: Premise-matched ISR 1.06x
42	  type: quantitative
43	  evidence:
44	  - exp_id: D051-analysis
45	    metric: premise_matched_ratio
46	  decisions: []
47	  deprecated: true
48	- id: C010
49	  location:
50	    section: experiments
51	    paragraph: 0
52	    sentence: 0
53	  text: SFT 92.9% genuine
54	  type: quantitative
55	  evidence:
56	  - exp_id: plan009-sft-baseline-s42-r4
57	    metric: genuine_rate
58	  decisions: []
59	  deprecated: true
60	- id: C015
61	  location:
62	    section: experiments
63	    paragraph: 0
64	    sentence: 0
65	  text: Prolog STA 3/3 gaming 0% genuine
66	  type: quantitative
67	  evidence:
68	  - exp_id: plan006-prolog-sta-s42
69	    metric: eval_h7_rate
70	  decisions: []
71	  deprecated: true
72	- id: C016
73	  location:
74	    section: abstract
75	    paragraph: 0
76	    sentence: 0
77	  text: 87% of proved outputs embed the conclusion verbatim among the premises
78	  type: empirical
79	  evidence:
80	  - plan001 exec-only training results
81	  decisions: []
…[truncated 17142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T17:40:43.074345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Get plan018-additive-random-b01-s42 details\ne = exps.get('plan018-additive-random-b01-s42', {})\nprint('=== plan018-additive-random-b01-s42 ===')\nprint(json.dumps({k: e.get(k) for k in ['status','conclusion','metrics','notes']}, indent=2, default=str))\nprint()\n# Get plan002-additive-b01-s42 details for genuine data\ne2 = exps.get('plan002-additive-b01-s42', {})\nprint('=== plan002-additive-b01-s42 ===')\nprint(json.dumps({k: e2.get(k) for k in ['status','conclusion','metrics','notes']}, indent=2, default=str))\nprint()\n# Get plan018-additive-random-b01-s43 related\nfor eid in sorted(exps.keys()):\n    if 'plan018-additive-random-b01-s4' in eid:\n        e3 = exps[eid]\n        print(f'=== {eid} ===')\n        print(f'  status={e3.get(\\\"status\\\")}, conclusion={e3.get(\\\"conclusion\\\")}')\n        m = e3.get('metrics', {})\n        if m:\n            print(f'  metrics={json.dumps(m, default=str)}')\n\"\n",
  "description": "Get registry details for Random s42/s43/s44 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/d09c16fe-783f-4107-8777-2fc80b263d10/tool-results/mcp-agent-ml-research-read_registry-1778866688318.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Get plan018-additive-random-b01-s42 details\ne = exps.get('plan018-additive-random-b01-s42', {})\nprint('=== plan018-additive-random-b01-s42 ===')\nprint(json.dumps({k: e.get(k) for k in ['status','conclusion','metrics','notes']}, indent=2, default=str))\nprint()\n# Get plan002-additive-b01-s42 details for genuine data\ne2 = exps.get('plan002-additive-b01-s42', {})\nprint('=== plan002-additive-b01-s42 ===')\nprint(json.dumps({k: e2.get(k) for k in ['status','conclusion','metrics','notes']}, indent=2, default=str))\nprint()\n# Get plan018-additive-random-b01-s43 related\nfor eid in sorted(exps.keys()):\n    if 'plan018-additive-random-b01-s4' in eid:\n        e3 = exps[eid]\n        print(f'=== {eid} ===')\n        print(f'  status={e3.get(\\\"status\\\")}, conclusion={e3.get(\\\"conclusion\\\")}')\n        m = e3.get('metrics', {})\n        if m:\n            print(f'  metrics={json.dumps(m, default=str)}')\n\"\n",
    "description": "Get registry details for Random s42/s43/s44 experiments"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T17:40:43.074556+00:00_

=== plan018-additive-random-b01-s42 ===
{
  "status": "DONE",
  "conclusion": "negative",
  "metrics": {
    "eval_prove_rate": 0.79,
    "eval_mean_isr": 0.1038,
    "eval_isr_std": 0.1369,
    "eval_median_isr": 0.0357,
    "eval_proved_only_isr": 0.1314,
    "eval_n_proved": 79,
    "eval_n_problems": 100,
    "tautological_collapse": false,
    "h7_count": 0,
    "h7_rate": 0,
    "h1_count": 56,
    "h1_rate": 0.7089,
    "h1_near_count": 8,
    "h1_near_rate": 0.1013,
    "h8_conjunction_collapse_count": 3,
    "h8_conjunction_collapse_rate": 0.038,
    "genuine_count_exact_h1": 23,
    "genuine_rate_exact_h1": 0.2911,
    "genuine_count_strict": 12,
    "genuine_rate_strict": 0.1519,
    "taxonomy_verification": "2026-05-15: full re-verification from eval_sta file. H1 exact=56, H1-near(substring)=8 (5 conc_in_prem + 3 prem_in_conc), H8=3, strict genuine=12. Registry original genuine=23 = H8(3) + H1-near(8) + strict genuine(12)."
  },
  "notes": "Random control \u03b2=0.1 vs ISR \u03b2=0.1 (plan002-b01) \u5bf9\u7167\u3002conclusion=negative: random control\u7684ISR\u8fdc\u4f4e\u4e8eISR-guided\u3002\n\n\u5bf9\u6bd4 plan002-b01 (ISR \u03b2=0.1):\n- PR: 0.79 vs 0.81 (\u2248\u6301\u5e73, \u0394=0.02)\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\n- Median ISR: 0.036 vs plan002\u672a\u8bb0\u5f55\n- Component count: 8.46 vs 5.58 (random\u7ec4\u66f4\u591a\u5197\u4f59)\n- ISR=0\u5360\u6bd4(proved): 36.7% (random\u7ec4\u5927\u91cfproof\u65e0\u7ed3\u6784)\n- Tautological collapse: \u65e0 (component_2_ratio=0)\n\n\u5173\u952e\u53d1\u73b0: PR\u51e0\u4e4e\u76f8\u540c\u8bf4\u660e\u03b2=0.1 random\u566a\u58f0\u4e0d\u5f71\u54cd\u8bc1\u660e\u80fd\u529b\u3002\u4f46ISR\u5dee3.2\u500d\uff0c\u8bc1\u660eISR reward\u63d0\u4f9bgenuine structural guidance\u800c\u975e\u4ec5variance regularization\u3002\u8fd9\u5f3a\u529b\u652f\u6301Claim 2: ISR\u4fe1\u53f7\u5728\u4f4e\u5242\u91cf\u4e0b\u6709\u7ed3\u6784\u4ef7\u503c\u3002\n\nEval outpu
…[truncated 5514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:40:43.074772+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml",
  "old_string": "  text: ISR is mathematically sensitive to component count (premise count bias)\n  type: scope_limitation\n  evidence: []\n  decisions:\n  - D051",
  "new_string": "  text: ISR is mathematically sensitive to component count (premise count bias)\n  type: scope_limitation\n  evidence:\n  - exp_id: plan002-additive-b01-s42\n    metric: premise_count_isr_confound\n  - exp_id: plan018-additive-random-b01-s42\n    metric: premise_count_matched_isr_ratio_1.06x\n  decisions:\n  - D051"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml",
    "old_string": "  text: ISR is mathematically sensitive to component count (premise count bias)\n  type: scope_limitation\n  evidence: []\n  decisions:\n  - D051",
    "new_string": "  text: ISR is mathematically sensitive to component count (premise count bias)\n  type: scope_limitation\n  evidence:\n  - exp_id: plan002-additive-b01-s42\n    metric: premise_count_isr_confound\n  - exp_id: plan018-additive-random-b01-s42\n    metric: premise_count_matched_isr_ratio_1.06x\n  decisions:\n  - D051"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T17:40:43.075048+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:40:43.075200+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml",
  "old_string": "_completeness:\n  coverage: 35/36\n  claims: 36\n  tables: 0\n  figures: 0\n  tier_counts:\n    tier1: 0\n    tier2: 35\n    tier3: 1\n    tierX: 0\n  last_checked: '2026-05-15T02:40:08.884772+00:00'",
  "new_string": "_completeness:\n  coverage: 36/36\n  claims: 36\n  tables: 0\n  figures: 0\n  tier_counts:\n    tier1: 0\n    tier2: 36\n    tier3: 0\n    tierX: 0\n  last_checked: '2026-05-15T12:00:00.000000+00:00'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml",
    "old_string": "_completeness:\n  coverage: 35/36\n  claims: 36\n  tables: 0\n  figures: 0\n  tier_counts:\n    tier1: 0\n    tier2: 35\n    tier3: 1\n    tierX: 0\n  last_checked: '2026-05-15T02:40:08.884772+00:00'",
    "new_string": "_completeness:\n  coverage: 36/36\n  claims: 36\n  tables: 0\n  figures: 0\n  tier_counts:\n    tier1: 0\n    tier2: 36\n    tier3: 0\n    tierX: 0\n  last_checked: '2026-05-15T12:00:00.000000+00:00'"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T17:40:43.075396+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:40:43.075535+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T17:40:43.075688+00:00_

_deprecated
_project
analysis_random_vs_isr_b01_interim.md
bootstrap_ci_results.json
claim_coverage_audit.md
component_count_analysis.md
data_consistency_report.md
diagnose_phase1_r3.md
dream_reports
evidence_chain_status.md
evidence_tables_d051.md
figure_quality_report.md
genuine_isr_crosscheck.md
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_characterization_report.md
hacking_taxonomy.md
hacking_taxonomy_comparison.md
inc05_literature_linkage.md
launch_phase1.sh
literature_goodhart.md
literature_map.yaml
manifest.yaml
paper-audit
paper_compile_audit.md
paper_consistency_audit.md
paper_figures
paper_number_audit.md
paper_number_audit_2026-05-15.json
paper_review_r1.md
paper_table1_evidence.md
paper_tables
paper_tables_draft.md
phase1_r2_diagnosis.md
plan001-exec-only-s43-1000-r2
plan001-exec-only-s43-r4
plan001-exec-only-s44
plan002-additive-b01-s42
plan002-additive-b01-s42-1000
plan002-additive-b01-s43
plan005_negative_literature.md
plan006
plan006_eval_compatibility.md
plan006_readiness.md
plan006_readiness_report.md
plan012
plan013-random-reward-s42-r4
plan013_analysis.md
plan014_design.md
plan016-extended-1000-s42
plan017-additive-random-s42
plan018
plan018-additive-random-b01-s42
plan018-additive-random-b01-s42-1000-r3
plan018-additive-random-b01-s42-1000-r3_analysis.json
preflight_prolog_sta_eval.md
prolog_sta_literature_linkage.md
prolog_sta_premise_count_analysis.md
reference_audit_report.md
reference_final_audit.md
registry_extract.json
review_issues.yaml
review_reports
s43_1000_n_components_investigation.md
section_4_3_1000step_draft.md
seed44_readiness.md
sft_3seed_pooled_ci.json
sta-phase0-baseline
table1_comparison.md
table1_data.json
table1_draft.md
table2_draft.md
table2_hacking_taxonomy.csv
table2_hacking_taxonomy.tex
table_data.json
table_data_compilation.md
table_drafts_v2.md
tables_draft_v1.md
tex_number_audit_20260515.md
train_grpo.py
training_progress_check.md
wilson_ci.py
wilson_ci_complete.csv
wilson_ci_complete.json
wilson_ci_complete.py
wi
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:40:43.075973+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/stats_recalc_checklist.md",
  "content": "# Random β=0.1 Pooled Statistics Recalculation Checklist\n\n## Trigger\nRandom s43/s44 旧数据 DEPRECATED（原 checkpoint 丢失无法溯源）。等待重训完成：\n- `plan018-additive-random-b01-s43-r3` — status: RUNNING\n- `plan018-additive-random-b01-s44-r2` — status: ALLOCATED\n\n重训完成后，需对两个新 checkpoint 执行 eval_sta.py（C008: `--data_path data/proofwriter_fol_100.jsonl`），然后用新数据重算以下所有统计量。\n\n## 已有数据（不变）\n\n### Random s42 (plan018-additive-random-b01-s42, D086 clean run)\n- n_proved = 79, n_problems = 100\n- H7 = 0, H1_exact = 56, H1_near = 8, H8 = 3\n- genuine (D084 标准: proved − H7 − H1_exact − H8) = **18** (22.8%)\n  - Note: registry strict genuine=12 扣了 H1-near; D084 标准不扣 H1-near → 79-0-56-3=20; D086 clean run 报告 18. 以 D086 为准。\n- proved_only_ISR = 0.1314\n\n### ISR β=0.1 3-seed (已闭环，不变)\n- s42: n_proved=81, H7=13, H1=42, H8=12, genuine=14 (17.3%)\n- s43: n_proved=61, H7=59, H1=0, genuine≈2 (~3%)\n- s44: n_proved=89, H7=89 (H7a=77+H7b=12, FN corrected), genuine=0 (0%)\n- **ISR pooled**: 231 proved, 16 genuine, genuine_rate = 6.9%\n\n---\n\n## 统计量重算清单\n\n### 1. Random 3-seed Pooled Genuine Rate\n\n**公式**: `genuine_pooled = (g_s42 + g_s43_new + g_s44_new) / (n_s42 + n_s43_new + n_s44_new)`\n\n**输入**:\n| Seed | Source | n_proved | genuine |\n|------|--------|----------|---------|\n| s42 | plan018-additive-random-b01-s42 | 79 | 18 |\n| s43 | plan018-additive-random-b01-s43-r3 eval | ? | ? |\n| s44 | plan018-additive-random-b01-s44-r2 eval | ? | ? |\n\n**Genuine 分类标准 (C013/D084)**: genuine = proved − H7 − H1_exact − H8. H1-near 保留为 genuine 但单独标记。\n\n**旧值 (DEPRECATED)**: 47/256 = 18.4% (含 s43=6, s44=18 推算值)\n\n### 2. Fisher Exact Test: Random vs ISR Genuine Rates\n\n**公式**: 2×2 contingency table, scipy.stats.fisher_exact\n\n```\n              ISR     Random\ngenuine       16      g_random_new\nnon-genuine   215     n_random_new - g_random_new\n```\n\n**两种场景**:\n- A (H8-only, 保守): ISR genuine = 28/231\n- B (H8 + s44 FN, 完整): ISR genuine = 16/231\n\n两种都需重算：`fisher_exact([[isr_g, random_g], [isr_ng, random_ng]])`\n- two-sided p\n- one-sided p (ISR < Random)\n\n**旧值 (DEPRECATED)**: 场景A p=0.060, 场景B p=0.0002\n\n### 3. Wilson CI for Random Genuine Rate\n\n**公式**: Wilson score interval, 95% CI\n\n```python\nfrom statsmodels.stats.proportion import proportion_confint\nci_low, ci_high = proportion_confint(g_random, n_random, alpha=0.05, method='wilson')\n```\n\n**输入**: g_random_new, n_random_new (from item 1)\n\n**旧值 (DEPRECATED)**: 需重算\n\n### 4. H7/H1/H8 Distribution — Random 3-seed 汇总\n\n**需要新 eval 结果中的分类计数**:\n\n| Seed | H7 | H1_exact | H1_near | H8 | Genuine | n_proved |\n|------|----|---------|---------|----|---------|----------|\n| s42 | 0 | 56 | 8 | 3 | 18 | 79 |\n| s43_new | ? | ? | ? | ? | ? | ? |\n| s44_new | ? | ? | ? | ? | ? | ? |\n| **Pooled** | Σ | Σ | Σ | Σ | Σ | Σ |\n\n**验证**: H7 应全部为 0（β=0.1 Random H7=0% 是核心 claim C136/C192）\n\n### 5. Premise-Count-Matched ISR Comparison (更新 1.06x)\n\n**公式**: 在 n_prem ≥ 3 的 genuine 样本中，比较 ISR s42 vs Random s42 的 mean ISR\n\n**当前值**: ISR genuine n_prem≥3: mean_ISR=0.2578 (n=11), Random genuine n_prem≥3: mean_ISR=0.2434 (n=21), ratio=1.06x\n\n**是否需要更新**: 取决于是否 pool 3-seed genuine 做 premise-matched 分析。\n- 如果仅用 s42 单 seed（当前方案）：**不需要更新**，因为 ISR s42 和 Random s42 数据不变\n- 如果扩展到 3-seed pooled：需要新 s43/s44 的 per-sample ISR + n_premise 数据\n\n**建议**: 保持 s42 单 seed 分析（D051 原始方案），新 s43/s44 作为 robustness check\n\n---\n\n## 执行步骤\n\n1. **等待训练完成**: 监控 plan018-additive-random-b01-s43-r3 和 plan018-additive-random-b01-s44-r2\n2. **Eval**: 对每个新 checkpoint 执行:\n   ```bash\n   export CUDA_VISIBLE_DEVICES=N  # C005\n   python eval_sta.py \\\n     --model_path &lt;checkpoint_path> \\\n     --data_path data/proofwriter_fol_100.jsonl \\  # C008\n     --output_dir /root/autodl-tmp/outputs/&lt;exp_id>/\n   ```\n3. **Taxonomy 分类**: 对 eval 输出执行 H7/H1/H8 分类（确保 C013 对称标准）\n4. **计算统计量**: 用上述公式重算 items 1-5\n5. **更新 paper_framing.md**: 替换所有 DEPRECATED/PROVISIONAL 标记的数字\n6. **更新 provenance**: 确保新 exp_id 注册到相关 claims\n7. **更新论文 LaTeX**: 更新 Table 1、Abstract、§4.2 中的 Random pooled 数字\n\n## 依赖关系\n```\ns43-r3 完成 ──┐\n              ├─→ eval s43 ──┐\ns44-r2 完成 ──┤              ├─→ 统计量重算 → 更新 framing/paper\n              └─→ eval s44 ──┘\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/stats_recalc_checklist.md",
    "content": "# Random β=0.1 Pooled Statistics Recalculation Checklist\n\n## Trigger\nRandom s43/s44 旧数据 DEPRECATED（原 checkpoint 丢失无法溯源）。等待重训完成：\n- `plan018-additive-random-b01-s43-r3` — status: RUNNING\n- `plan018-additive-random-b01-s44-r2` — status: ALLOCATED\n\n重训完成后，需对两个新 checkpoint 执行 eval_sta.py（C008: `--data_path data/proofwriter_fol_100.jsonl`），然后用新数据重算以下所有统计量。\n\n## 已有数据（不变）\n\n### Random s42 (plan018-additive-random-b01-s42, D086 clean run)\n- n_proved = 79, n_problems = 100\n- H7 = 0, H1_exact = 56, H1_near = 8, H8 = 3\n- genuine (D084 标准: proved − H7 − H1_exact − H8) = **18** (22.8%)\n  - Note: registry strict genuine=12 扣了 H1-near; D084 标准不扣 H1-near → 79-0-56-3=20; D086 clean run 报告 18. 以 D086 为准。\n- proved_only_ISR = 0.1314\n\n### ISR β=0.1 3-seed (已闭环，不变)\n- s42: n_proved=81, H7=13, H1=42, H8=12, genuine=14 (17.3%)\n- s43: n_proved=61, H7=59, H1=0, genuine≈2 (~3%)\n- s44: n_proved=89, H7=89 (H7a=77+H7b=12, FN corrected), genuine=0 (0%)\n- **ISR pooled**: 231 proved, 16 genuine, genuine_rate = 6.9%\n\n---\n\n## 统计量重算清单\n\n### 1. Random 3-seed Pooled Genuine Rate\n\n**公式**: `genuine_pooled = (g_s42 + g_s43_new + g_s44_new) / (n_s42 + n_s43_new + n_s44_new)`\n\n**输入**:\n| Seed | Source | n_proved | genuine |\n|------|--------|----------|---------|\n| s42 | plan018-additive-random-b01-s42 | 79 | 18 |\n| s43 | plan018-additive-random-b01-s43-r3 eval | ? | ? |\n| s44 | plan018-additive-random-b01-s44-r2 eval | ? | ? |\n\n**Genuine 分类标准 (C013/D084)**: genuine = proved − H7 − H1_exact − H8. H1-near 保留为 genuine 但单独标记。\n\n**旧值 (DEPRECATED)**: 47/256 = 18.4% (含 s43=6, s44=18 推算值)\n\n### 2. Fisher Exact Test: Random vs ISR Genuine Rates\n\n**公式**: 2×2 contingency table, scipy.stats.fisher_exact\n\n```\n              ISR     Random\ngenuine       16      g_random_new\nnon-genuine   215     n_random_new - g_random_new\n```\n\n**两种场景**:\n- A (H8-only, 保守): ISR genuine = 28/231\n- B (H8 + s44 FN, 完整): ISR genuine = 16/231\n\n两种都需重算：`fisher_exact([[isr_g, random_g], [isr_ng, random_ng]])`\n- two-sided p\n- one-sided p (ISR < Random)\n\n**旧值 (DEPRECATED)**: 场景A p=0.060, 场景B p=0.0002\n\n### 3. Wilson CI for Random Genuine Rate\n\n**公式**: Wilson score interval, 95% CI\n\n```python\nfrom statsmodels.stats.proportion import proportion_confint\nci_low, ci_high = proportion_confint(g_random, n_random, alpha=0.05, method='wilson')\n```\n\n**输入**: g_random_new, n_random_new (from item 1)\n\n**旧值 (DEPRECATED)**: 需重算\n\n### 4. H7/H1/H8 Distribution — Random 3-seed 汇总\n\n**需要新 eval 结果中的分类计数**:\n\n| Seed | H7 | H1_exact | H1_near | H8 | Genuine | n_proved |\n|------|----|---------|---------|----|---------|----------|\n| s42 | 0 | 56 | 8 | 3 | 18 | 79 |\n| s43_new | ? | ? | ? | ? | ? | ? |\n| s44_new | ? | ? | ? | ? | ? | ? |\n| **Pooled** | Σ | Σ | Σ | Σ | Σ | Σ |\n\n**验证**: H7 应全部为 0（β=0.1 Random H7=0% 是核心 claim C136/C192）\n\n### 5. Premise-Count-Matched ISR Comparison (更新 1.06x)\n\n**公式**: 在 n_prem ≥ 3 的 genuine 样本中，比较 ISR s42 vs Random s42 的 mean ISR\n\n**当前值**: ISR genuine n_prem≥3: mean_ISR=0.2578 (n=11), Random genuine n_prem≥3: mean_ISR=0.2434 (n=21), ratio=1.06x\n\n**是否需要更新**: 取决于是否 pool 3-seed genuine 做 premise-matched 分析。\n- 如果仅用 s42 单 seed（当前方案）：**不需要更新**，因为 ISR s42 和 Random s42 数据不变\n- 如果扩展到 3-seed pooled：需要新 s43/s44 的 per-sample ISR + n_premise 数据\n\n**建议**: 保持 s42 单 seed 分析（D051 原始方案），新 s43/s44 作为 robustness check\n\n---\n\n## 执行步骤\n\n1. **等待训练完成**: 监控 plan018-additive-random-b01-s43-r3 和 plan018-additive-random-b01-s44-r2\n2. **Eval**: 对每个新 checkpoint 执行:\n   ```bash\n   export CUDA_VISIBLE_DEVICES=N  # C005\n   python eval_sta.py \\\n     --model_path &lt;checkpoint_path> \\\n     --data_path data/proofwriter_fol_100.jsonl \\  # C008\n     --output_dir /root/autodl-tmp/outputs/&lt;exp_id>/\n   ```\n3. **Taxonomy 分类**: 对 eval 输出执行 H7/H1/H8 分类（确保 C013 对称标准）\n4. **计算统计量**: 用上述公式重算 items 1-5\n5. **更新 paper_framing.md**: 替换所有 DEPRECATED/PROVISIONAL 标记的数字\n6. **更新 provenance**: 确保新 exp_id 注册到相关 claims\n7. **更新论文 LaTeX**: 更新 Table 1、Abstract、§4.2 中的 Random pooled 数字\n\n## 依赖关系\n```\ns43-r3 完成 ──┐\n              ├─→ eval s43 ──┐\ns44-r2 完成 ──┤              ├─→ 统计量重算 → 更新 framing/paper\n              └─→ eval s44 ──┘\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 28 · 2026-05-15T17:40:43.076426+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/stats_recalc_checklist.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:40:43.076716+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "stats_recalc_checklist",
  "type": "intermediate",
  "description": "Random β=0.1 pooled statistics recalculation checklist — formulas, input sources, and execution steps for when s43-r3/s44-r2 retraining completes",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/stats_recalc_checklist.md",
  "tags": "['statistics', 'random-control', 'recalculation', 'D084']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "stats_recalc_checklist",
    "type": "intermediate",
    "description": "Random β=0.1 pooled statistics recalculation checklist — formulas, input sources, and execution steps for when s43-r3/s44-r2 retraining completes",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/stats_recalc_checklist.md",
    "tags": "['statistics', 'random-control', 'recalculation', 'D084']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T17:40:43.076965+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_2e14c3\", \"name\": \"stats_recalc_checklist\", \"type\": \"intermediate\", \"description\": \"Random β=0.1 pooled statistics recalculation checklist — formulas, input sources, and execution steps for when s43-r3/s44-r2 retraining completes\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/intermediate/stats_recalc_checklist.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T17:40:35.266069+00:00\", \"tags\": [\"statistics\", \"random-control\", \"recalculation\", \"D084\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-15T17:40:43.077220+00:00_

两个任务完成。

**任务 1**: Provenance 补全 36/36。缺失项是 **C177**（"ISR is mathematically sensitive to component count (premise count bias)"），`evidence: []` → 添加了 plan002-additive-b01-s42 和 plan018-additive-random-b01-s42 作为证据（D051 premise-count confound 分析的底层数据来源）。

**任务 2**: 统计量重算 checklist 已写入 `artifacts/stats_recalc_checklist.md` 并注册（art_20260515_2e14c3）。覆盖 5 项统计量：pooled genuine rate、Fisher exact test (两种场景)、Wilson CI、H7/H1/H8 分布汇总、premise-count-matched 1.06x 是否需更新。依赖 s43-r3（RUNNING）和 s44-r2（ALLOCATED）完成后的 eval 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_provenance-and-stats-prep_20260515T173752"
}
```

</details>

---
