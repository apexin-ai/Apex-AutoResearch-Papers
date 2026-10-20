# research rewrite scan report

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_rewrite_scan_report_20260515T134249.jsonl`
- **Structured JSON:** [`6e5e10cd31a7a723dfd1.json`](../../sessions/6e/6e5e10cd31a7a723dfd1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T13:44:42.290248+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T13:44:42.290690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:44:42.290952+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "trace-verdict-study",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T13:44:42.291210+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| deepseek_exception_only_seed42 | Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence. | — | — | — |\\n\\n## 待处理\\n- vota_seed42_v2（排队等待 GPU）\\n- vota_seed42（排队等待 GPU）\\n- no_trace_seed42_v2（排队等待 GPU）\\n- no_trace_seed42（排队等待 GPU）\\n- vota_seed456: Seed robustness: VOTA with seed=456 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.（准备中）\\n- deepseek_full_trace_seed42: Multi-model comparison: full-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if full_trace also shows intermediate performance on DeepSeek-Coder.（准备中）\\n\\n## 近期结论\\n- **deepseek_no_trace_seed42** (success): Multi-model baseline: no-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Establishes DeepSeek baseline for comparison with VOTA and full_trace conditions.\\n- **deepseek_vota_seed42** (success): Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\\n  [deepseek_vota_seed42_analysis](/api/workspace-files/projects/trace-verdict-study/artifacts/deepseek_vota_seed42/report/analysis.md)\\n- **vota_seed123** (failed): Seed robustness: VOTA with seed=123 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\\n\\n## 趋势\\n成功 13 / 负向 1 / 失败 2 / 共 19\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-11235: 无 GPU 信息\\n\\n## 告警\\n- no_trace_seed42_v3: 已被终止 — unknown\\n- vota_seed42_v3: 已被终止 — unknown\\n- full_trace_seed42: 已被终止 — unknown\\
…[truncated 167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:44:42.291484+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "trace-verdict-study",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:44:42.291960+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        role: m
…[truncated 12949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:44:42.292209+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/scan_report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/scan_report*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:44:42.292419+00:00_

artifacts/_project/report/scan_report.md
artifacts/literature_scan_20260515/scan_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:44:42.292627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:44:42.292873+00:00_

1	# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)
2	
3	**Date**: 2026-05-15  
4	**Target**: EMNLP 2026 Main (ARR May 25 deadline)  
5	**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  
6	
7	## Summary
8	
9	No **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.
10	
11	---
12	
13	## New Papers Found (10 additions, 16→26 total)
14	
15	### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)
16	
17	| # | Paper | Venue | Threat | Relation to VOTA |
18	|---|-------|-------|--------|-----------------|
19	| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |
20	| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |
21	
22	**Differentiation from VOTA**:
23	- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)
24	- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals
25	- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction
26	- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)
27	
28	### LOW Threat — Supporting Evidence & Background
29	
30	| # | Paper | Venue | Category | Why Releva
…[truncated 5089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:44:42.293097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:44:42.293376+00:00_

1	# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)
2	
3	**Date**: 2026-05-15  
4	**Target**: EMNLP 2026 Main (ARR May 25 deadline)  
5	**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  
6	
7	## Summary
8	
9	No **high-threat** direct competitor found. VOTA's core contribution — using fault indicator signals (exception events + assertion comparison points) from execution traces for binary verdict prediction via SFT — remains novel. The closest related works are in **patch correctness prediction**, which overlaps on input signals but differs fundamentally in task definition.
10	
11	---
12	
13	## New Papers Found (10 additions, 16→26 total)
14	
15	### MEDIUM Threat — Patch Correctness Prediction (Closest Competitors)
16	
17	| # | Paper | Venue | Threat | Relation to VOTA |
18	|---|-------|-------|--------|-----------------|
19	| 1 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |
20	| 2 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |
21	
22	**Differentiation from VOTA**:
23	- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)
24	- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals
25	- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA; VOTA = SFT with trace abstraction
26	- **Core finding**: Neither identifies fault indicator signals as near-perfect discriminative features (99.83%)
27	
28	### LOW Threat — Supporting Evidence & Background
29	
30	| # | Paper | Venue | Category | Why Releva
…[truncated 5089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:44:42.293696+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md",
  "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md",
    "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:44:42.294583+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/scan_report.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:44:42.294889+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md",
  "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md",
    "content": "# Literature Scan Report — VOTA (Verdict-Oriented Trace Abstraction)\n\n**Date**: 2026-05-15  \n**Target**: EMNLP 2026 Main (ARR May 25 deadline)  \n**Queries executed**: 16 search groups across arXiv, ACL Anthology, Semantic Scholar, IEEE Xplore  \n\n## Summary\n\nNo direct competitor was found that combines execution trace compression with SFT for binary verdict prediction. However, Wang et al. (EMNLP 2025 Findings) present a significant conceptual challenge: their comprehensive study of 5 trace formats for SFT concludes that semantic information from execution traces has limited usefulness. VOTA's response hinges on the distinction between raw/formatted traces and decision-relevant compression targeting fault indicator signals. The closest methodological neighbors are in **patch correctness prediction**, which shares input signal space but differs in task definition and approach.\n\n---\n\n## New Papers Found (10 additions, 16→26 total)\n\n### MEDIUM-HIGH Threat — Trace SFT Effectiveness\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 1 | **Wang et al. \"Do Code Semantics Help?\"** (Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li) | Findings of EMNLP 2025 | **MEDIUM-HIGH** | Comprehensive study testing 5 trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) for SFT on code generation/repair. Conclusion: \"semantic information has limited usefulness for SFT.\" Conceptually the strongest challenge to any trace-based SFT approach including VOTA. |\n\n**Why MEDIUM-HIGH, not HIGH**: Wang et al.'s study differs from VOTA on three axes:\n- **Task**: They evaluate code generation and repair; VOTA targets verdict prediction (binary classification), a fundamentally different downstream task where trace signals serve as discriminative features rather than generative context\n- **Trace content**: All 5 formats they test preserve execution flow information (variable states, step-by-step traces); none isolates fault indicator signals (exception events, assertion comparison outcomes) — the specific signals VOTA's ablation identifies as carrying nearly all discriminative power\n- **Compression strategy**: Their \"Concise\" format is a syntactic reduction of trace verbosity; VOTA's compression is semantic, retaining only decision-relevant signals for the verdict task\n\n**Implication for VOTA paper**: This paper must be cited and directly addressed. The argument is: \"raw trace ineffective for SFT ≠ compressed fault-indicator signals ineffective for SFT.\" VOTA's component ablation (exception_only achieving 99.83%) provides the empirical counterpoint — the value is not in trace format but in isolating the right signals for the right task.\n\n### MEDIUM Threat — Patch Correctness Prediction\n\n| # | Paper | Venue | Threat | Relation to VOTA |\n|---|-------|-------|--------|-----------------|\n| 2 | **LLM4PatchCorrect** (Xin Zhou et al.) | TSE 2024 | **MEDIUM** | Uses execution traces + test cases as input for patch correctness assessment. Key difference: zero-shot prompting (no SFT), task is patch correctness (not test verdict), no trace compression. |\n| 3 | **APSG + Graph-LoRA** (arXiv 2505.02629) | arXiv 2025 | **LOW-MEDIUM** | PEFT for patch correctness with graph-structured code representation. Key difference: uses static code graph (not runtime trace), no fault indicator signals. |\n\n**Differentiation from VOTA**:\n- **Task**: Patch correctness (is this fix correct?) vs. VOTA's verdict prediction (does this test pass/fail?)\n- **Input**: LLM4PatchCorrect uses raw traces + test info; VOTA uses decision-relevant compressed signals\n- **Method**: LLM4PatchCorrect = zero-shot prompting; APSG = graph-LoRA on static graphs; VOTA = SFT with trace abstraction\n- **Signal identification**: Neither work isolates fault indicator signals or measures their individual contribution\n\n### LOW Threat — Supporting Evidence & Background\n\n| # | Paper | Venue | Category | Why Relevant |\n|---|-------|-------|----------|-------------|\n| 4 | **FuseFL** (Widyasari et al.) | SANER 2024 | code-verdict | Uses test execution outcomes (expected/actual output, errors) for fault localization. Validates that test outcome signals carry discriminative value — same intuition as VOTA, different task. |\n| 5 | **REval** (Junkai Chen et al.) | arXiv 2403.16437 | evaluation | LLM runtime behavior prediction: avg accuracy 44.4%. Supports VOTA's argument that LLMs struggle with raw trace reasoning. |\n| 6 | **CodeMind** (Changshu Liu et al.) | arXiv 2402.09664 | evaluation | Code reasoning drops with complexity (control flow, API calls). Supports trace abstraction motivation. |\n| 7 | **CRUXEval-X** (Ruiyang Xu et al.) | ACL 2025 | evaluation | Multilingual CRUXEval (19 langs). Cross-language generalization reference for VOTA's cross-model experiments. |\n| 8 | **InspectCoder** (arXiv 2510.18327) | arXiv 2025 | trace-compression | Strategic breakpoint placement + runtime state inspection for repair. Selective inspection philosophy aligns with VOTA's fault indicator extraction. |\n| 9 | **MGDebugger** (Yuling Shi et al.) | arXiv 2410.01215 | trace-compression | Hierarchical debugging with LLM-simulated execution tracking key variables. Implicit trace abstraction. |\n| 10 | **UniDebugger** (Cheryl Lee et al.) | EMNLP 2025 | debugging-agents | Multi-agent debugging without execution traces (static analysis). Orthogonal to VOTA. |\n| 11 | **Seeker** (Xuanming Zhang et al.) | ICLR 2025 | debugging-agents | Exception handling with CEE knowledge base. Exception taxonomy provides complementary perspective to VOTA's exception event signals. |\n\n---\n\n## Threat Analysis\n\n### Conceptual Threat: Wang et al. (EMNLP 2025 Findings) — MEDIUM-HIGH\n\nThis is the most important paper for VOTA to address. Their finding that \"execution trace semantic information has limited usefulness for SFT\" could be read as undermining any trace-based SFT approach. VOTA's differentiation rests on three empirical arguments:\n\n1. **Task difference**: Wang et al. study code generation/repair (open-ended generative tasks); VOTA targets binary classification (verdict prediction). Trace signals that fail to improve generation may still serve as strong discriminative features for classification.\n2. **Signal granularity**: Wang et al.'s 5 trace formats all represent execution flow at varying verbosity levels. None isolates fault indicator signals (exception type/message, assertion expected-vs-actual). VOTA's ablation shows the exception signal alone drives 99.83% accuracy — this is a qualitatively different use of trace information.\n3. **Compression semantics**: Their \"Concise\" format reduces trace tokens but preserves the same information type. VOTA's compression is task-driven: it discards execution flow and retains only signals relevant to the pass/fail decision.\n\n**Risk**: A reviewer familiar with Wang et al. may question whether VOTA is \"yet another trace SFT paper.\" The response should preemptively frame VOTA as studying *which* trace signals matter for *which* tasks, not whether traces help generically.\n\n### Methodological Threats\n\n**vs. LLM4PatchCorrect (TSE 2024) — MEDIUM**: The closest work combining execution traces with correctness assessment. Differentiation: (a) VOTA identifies *which parts* of the trace matter (fault indicators), while LLM4PatchCorrect uses uncompressed traces; (b) SFT vs. zero-shot prompting; (c) verdict prediction vs. patch correctness. LLM4PatchCorrect should be cited as evidence that execution traces contain useful signals for correctness tasks, while noting the methodological gap VOTA addresses.\n\n**vs. APSG + Graph-LoRA (arXiv 2025) — LOW-MEDIUM**: Concurrent work on PEFT for code correctness. Differentiation: (a) runtime signals vs. static code graphs; (b) VOTA's finding that 2 signal types suffice, vs. APSG's complex graph construction. The approaches are largely complementary — APSG could potentially benefit from incorporating runtime signals.\n\n### Emerging Trend: Selective Trace\n\nMultiple 2025-2026 papers (InspectCoder, TraceCoder, Runtime Traces + Multi-Agent Debate) converge on the insight that **selective trace information outperforms full traces**. VOTA aligns with this trend; its distinguishing characteristic is that the selection criterion is *decision-relevance for verdict prediction* rather than general debugging utility.\n\n---\n\n## Recommended Citations to Add\n\n1. **Wang et al. \"Do Code Semantics Help?\"** (Findings of EMNLP 2025) — must-cite; primary conceptual challenge to address\n2. **LLM4PatchCorrect** (TSE 2024) — closest work using execution traces for correctness assessment\n3. **REval** (2024) — empirical evidence LLMs struggle with runtime reasoning (avg 44.4%)\n4. **CodeMind** (2024) — code reasoning evaluation showing complexity-dependent degradation\n5. **FuseFL** (SANER 2024) — validates test execution outcomes as discriminative signals\n6. **CRUXEval-X** (ACL 2025) — cross-language generalization methodology reference\n7. **InspectCoder** (2025) — selective runtime inspection trend\n\n---\n\n## Gap Assessment\n\nBased on the current scan, the following gaps appear to hold:\n\n1. **Binary verdict prediction from execution traces**: No identified work directly applies execution trace signals to pass/fail prediction via SFT. The closest (LLM4PatchCorrect) uses zero-shot prompting for a different task (patch correctness).\n2. **Fault indicator signal isolation**: No identified work measures the individual contribution of exception events or assertion comparison signals to classification accuracy. VOTA's ablation results (exception_only at 99.83%) appear to be a novel empirical finding in this space.\n3. **Decision-relevant trace compression for LLM classification**: Existing trace compression/selection work targets program repair or debugging, not binary classification. Whether VOTA's compression strategy generalizes beyond verdict prediction is an open question.\n4. **Cross-model generalization**: Trace-based verdict prediction across different base models (Qwen, DeepSeek) has not been studied elsewhere in the surveyed literature.\n\nThese assessments are based on the 26 papers currently in the literature map. A reviewer with deeper knowledge of the software testing or mutation testing literature may identify additional related work not covered here.\n\n---\n\n## Search Methodology\n\n16 query groups covering:\n- \"execution trace\" + \"fault detection\" / \"verdict prediction\" / \"test prediction\"\n- \"trace compression\" + \"code understanding\" / \"debugging\"\n- \"exception signal\" + \"fault localization\"\n- \"VOTA\" / \"trace abstraction\" / \"verdict oriented\"\n- \"CRUXEval\" + \"execution reasoning\"\n- \"patch correctness prediction\" / \"automated patch assessment\"\n- \"test outcome prediction\" / \"pass fail prediction\"\n- \"selective trace\" + \"debugging\" / \"program repair\"\n- \"code correctness prediction\" / \"classification\"\n- \"error message\" / \"exception\" + \"program repair effectiveness\"\n- Cross-model generalization + code LLM fine-tuning\n- \"code semantics\" + \"execution trace\" + \"SFT\" (added for Wang et al. coverage)\n\nSources: arXiv, ACL Anthology, IEEE Xplore, Semantic Scholar, DBLP, Google Scholar\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:44:42.295467+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/literature_scan_20260515/scan_report.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_rewrite_scan_report_20260515T134249",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T13:44:42.295745+00:00_

两份 scan_report.md 已同步更新。主要变更：

1. **Wang et al. (EMNLP 2025 Findings) 作为 MEDIUM-HIGH threat 加入** — 独立小节详细分析三个差异轴（task/signal granularity/compression semantics），并给出 VOTA paper 的回应策略
2. **APSG 降级为 LOW-MEDIUM**（静态图，非 runtime trace）
3. **所有断言性措辞已替换**：
   - "remains novel" → 删除
   - "fills this gap" → "no identified work directly applies..."
   - "VOTA's core empirical finding" → "appear to be a novel empirical finding"
   - "Key Gaps Confirmed" → "Gap Assessment" + 加了 caveat 说明基于当前 26 篇文献的局限性
4. **Recommended Citations** 首位改为 Wang et al.（must-cite）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_rewrite_scan_report_20260515T134249"
}
```

</details>

---
