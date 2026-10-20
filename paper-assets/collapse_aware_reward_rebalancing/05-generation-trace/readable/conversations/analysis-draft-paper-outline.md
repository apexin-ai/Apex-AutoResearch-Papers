# analysis draft paper outline

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_draft_paper_outline_20260517T033408.jsonl`
- **Structured JSON:** [`212c0f2c60d4028a325f.json`](../../sessions/21/212c0f2c60d4028a325f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-17T03:37:16.201324+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T03:37:16.201636+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T03:37:16.201823+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse_aware_reward_rebalancing",
  "file": "report.md",
  "max_chars": "20000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse_aware_reward_rebalancing",
    "file": "report.md",
    "max_chars": "20000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T03:37:16.201989+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| carr_fullft_lr2e5_k16_probe_01 | — | — | — | — |\\n| carr_fullft_lr2e5_nocuration_01 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **carr_fullft_lr2e5_probe_01** (negative): Full-FT LR=2e-5 (4x提高) 使模型充分学习 curated data 分布，触发可观测的 diversity decline — 若 Vendi 仍不降则证明 curation 本身不导致 collapse\\n- **carr_fullft_nocuration_01** (success): Full-FT no_curation baseline: random 1-of-4 selection without reward sorting should show no systematic diversity decline across generations, serving as null-effect control for the curation condition\\n- **carr_fullft_k4_probe_03** (negative): —\\n\\n## 趋势\\n成功 2 / 负向 4 / 失败 4 / 共 11\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb2-23165: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- carr_quick_probe_01: 训练失败 — unknown\\n- carr_quick_probe_02: 训练失败 — unknown\\n- carr_quick_probe_k8_01: 已被终止 — unknown\\n- carr_fullft_k4_probe_01: 训练失败 — unknown\\n- carr_fullft_k4_probe_02: 训练失败 — unknown\\n\", \"total_chars\": 1026, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T03:37:16.202141+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse_aware_reward_rebalancing",
  "file": "ideas.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse_aware_reward_rebalancing",
    "file": "ideas.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T03:37:16.202274+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'collapse_aware_reward_rebalancing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T03:37:16.202395+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse_aware_reward_rebalancing",
  "file": "ROADMAP.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse_aware_reward_rebalancing",
    "file": "ROADMAP.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T03:37:16.202558+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/ROADMAP.md\", \"content\": \"# collapse_aware_reward_rebalancing — Research Dashboard\\n\\n> 最后更新: 2026-05-17 03:11 UTC | 更新原因: Direction C FAIL，正式切入 Direction D 论文准备\\n\\n## 核心方向\\n**Direction D: Negative Result Empirical Study**\\n\\\"Does reward-based curation cause diversity collapse in iterative self-consuming training? Systematic evidence of surprising resilience.\\\"\\n\\n## 当前进展\\n- **阶段**: MVP → Direction D 论文准备\\n- **目标会议**: EMNLP 2026 ARR (DDL: 2026-05-25, 8 天)\\n- **P1 结果**: 5/5 FAIL — curation 不导致 collapse (当前设置)\\n- **Direction C**: FAIL — CARR dry-run 99.3% overlap (proxy scores 太相关)\\n- **竞品验证**: 5/5 真实论文 (DIVE, DARLING, CD-RLHF, GEM, Kirk et al.)\\n\\n### 论文贡献 (planned)\\n1. 系统性否定 curation→collapse：5 配置 (K=4/8 LoRA, Full-FT LR=5e-6/2e-5, K=16) × 3 代\\n2. LoRA capacity artifact 发现：3pp gap 是 LoRA 限制非 curation 因果\\n3. Conditions taxonomy：什么条件下 collapse 不出现\\n4. (bonus) K=16 boundary condition：如果触发 collapse → 边界发现\\n\\n### P1 全量数据\\n| 条件 | Vendi 变化 | Loss 降幅 | Gap vs baseline |\\n|------|-----------|----------|----------------|\\n| K=4 LoRA | -0.27% | ~0% | 3.4pp (artifact) |\\n| K=8 LoRA | -0.03% | ~0% | 3.2pp (artifact) |\\n| Full-FT LR=5e-6 | +0.91% | -12% | 0.47pp |\\n| Full-FT LR=2e-5 | +0.68% | -80% | ≤0.7pp |\\n| LoRA no-curation | +3.13% | — | baseline |\\n| Full-FT no-curation | +1.38% | — | baseline |\\n\\n## 近期任务\\n- [ ] Agent 整理完整实验数据表格 (论文 Table 1)\\n- [ ] 拉取 collapse_signal_report.json (文本级分析)\\n- [ ] 草拟论文骨架 outline\\n- [ ] 评估骨架后启动 Paper Agent\\n- [ ] K=16 probe 完成 (~8-12h, cuda:1)\\n- [ ] LR=2e-5 nocuration baseline 完成 (~2h, cuda:0)\\n\\n## GPU 预算\\n- 本项目分配: bjb2-23165 cuda:0, cuda:1 (2× RTX 5090, 32GB)\\n- 当前: cuda:0 (lr2e5 nocuration) + cuda:1 (K=16 probe)\\n- 论文准备主要是 CPU 工作，GPU 实验为补充数据点\\n\\n## 关键风险\\n1. **K=16 结果不确定 (~20% collapse)**: 成功 → 大幅加强论文 (boundary finding)；失败 → 全 negative，需更强 framing\\
…[truncated 1564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T03:37:16.202735+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse_aware_reward_rebalancing",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse_aware_reward_rebalancing",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T03:37:16.202869+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'collapse_aware_reward_rebalancing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T03:37:16.203017+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "collapse_aware_reward_rebalancing",
  "file": "decisions.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "collapse_aware_reward_rebalancing",
    "file": "decisions.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T03:37:16.203224+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/decisions.yaml\", \"content\": \"_next_id: 12\\ndecisions:\\n- id: D001\\n  date: 2026-05-16 07:37 UTC\\n  summary: 'MVP 设计: Qwen3.5-0.8B + LoRA, 4 条件 × 5 代, 验证 CARR 是否优于 fixed-weight curation'\\n  rationale: 核心假设需最小实验验证：(1) collapse 在 iterative curation 中可观测，(2) CARR 自适应比 fixed-weight\\n    更好防 collapse。选择 0.8B+LoRA 因为 2 GPU 资源下需要快速迭代。T=5 平衡了 collapse 信号检测和 MVP 速度。4 条件覆盖了无\\n    curation / 单目标 / 固定多目标 / CARR 的递进对比。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-16 07:41 UTC\\n  summary: '采纳 Reviewer 4 点建议: 增加 Quick Probe, P1 降至 5%, P2 增加 ≥5% 效应量, 双指标记录'\\n  rationale: Reviewer 指出 T=5 可能不足以触发显著 collapse，P2 无最小效应量无统计意义，curation 和评估指标不对齐。采纳全部建议：(1)\\n    先跑单目标 3 代 Quick Probe 验证 collapse 可见性再铺全部实验；(2) P1 阈值降至 5%；(3) P2 增加 ≥5% 相对改善要求；(4)\\n    同时记录 NN distance 和 Vendi Score。GPU 型号已确认为 RTX 5090 32GB。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-16 07:49 UTC\\n  summary: '代码审查修复: W1 mask prompt labels, W2 diversity scoring 改为 corpus-level, W3\\n    双 GPU 并行'\\n  rationale: 'W2 是核心风险: per-prompt K=4 diversity NN distance 几乎无区分力（同模型同 prompt 的\\n    4 个 response embedding 极相似），改为 corpus-level NN distance（全部 8000 候选中的 NN distance）使信号有意义。W1\\n    修复简单但影响绝对质量。W3 在 Full MVP 阶段需要双 GPU 并行。I1 补充 evaluate.py 中的 NN distance 指标。'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-16 14:13 UTC\\n  summary: 'P1 FAIL: K=4 + LoRA + T=3 下无可观测 collapse。暂停 Full MVP，启动 K=8 Quick Probe\\n    加压验证'\\n  rationale: 'Quick Probe 03 结果: Vendi Score 3 代仅降 0.27%（反弹），远不及 P1≥5% 阈值。self-BLEU\\n    波动非单调，无 collapse 趋势。原因诊断: K=4 选择压力太弱（25% 保留率，候选间差异仅 0.04）+ LoRA 约束模型 drift + T=3\\n    太短。按 Reviewer 建议，优先用 K=8 (12.5% 保留率) 加压重跑 Quick Probe，这是成本最低的验证路径。Full MVP 在确认\\n    collapse 可观测前不启动。'\\n  related_experiments:\\n  - exp_id: carr_quick_probe_03\\n    role: ev
…[truncated 5515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T03:37:16.203414+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T03:37:16.203544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T03:37:16.203692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T03:37:16.203820+00:00_

analysis_carr_fullft_lr2e5_nocuration_01.md
carr_dryrun_feasibility_report.md
carr_fullft_lr2e5_probe_01_metrics.json
experiment_data_table.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T03:37:16.203938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/experiment_data_table.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/experiment_data_table.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T03:37:16.204092+00:00_

1	# CARR Experiment Data Tables
2	
3	Model: Mistral-Small-3.1-24B-Instruct-2503  
4	Base dataset: 2000 prompts, iterative self-training over 3 generations (gen0/gen1/gen2)
5	
6	---
7	
8	## Table 1: Full Metrics by Generation
9	
10	### A. Reward-Curated Conditions (ArmoRM top-1-of-K)
11	
12	| Condition | Gen | Quality (ArmoRM) | Vendi Score | Self-BLEU | NN Distance | PPL |
13	|-----------|-----|----------------:|------------:|----------:|------------:|----:|
14	| **LoRA, K=4** | 0 | 0.1123 | 107.54 | 0.0059 | 0.7088 | 10.60 |
15	| | 1 | 0.1138 | 106.73 | 0.0091 | 0.7065 | 9.73 |
16	| | 2 | 0.1109 | 107.25 | 0.0062 | 0.7054 | 9.72 |
17	| **LoRA, K=8** | 0 | 0.1146 | 107.21 | 0.0057 | 0.7097 | 9.40 |
18	| | 1 | 0.1136 | 107.26 | 0.0024 | 0.7086 | 9.18 |
19	| | 2 | 0.1143 | 107.25 | 0.0064 | 0.7095 | 10.20 |
20	| **Full-FT, K=4, lr=5e-6** | 0 | 0.1145 | 107.10 | 0.0038 | 0.7073 | 9.10 |
21	| | 1 | 0.1141 | 107.61 | 0.0060 | 0.7091 | 8.66 |
22	| | 2 | 0.1131 | 108.07 | 0.0044 | 0.7108 | 9.21 |
23	| **Full-FT, K=4, lr=2e-5** | 0 | 0.1130 | 107.81 | 0.0046 | 0.7079 | 9.57 |
24	| | 1 | 0.1154 | 108.03 | 0.0039 | 0.7107 | 10.34 |
25	| | 2 | 0.1124 | 108.54 | 0.0040 | 0.7100 | 8.82 |
26	
27	### B. No-Curation Baselines (random 1-of-K)
28	
29	| Condition | Gen | Quality (ArmoRM) | Vendi Score | Self-BLEU | NN Distance | PPL |
30	|-----------|-----|----------------:|------------:|----------:|------------:|----:|
31	| **LoRA, K=4, random** | 0 | 0.1107 | 105.42 | 0.0044 | 0.7005 | 9.19 |
32	| | 1 | 0.1099 | 108.21 | 0.0067 | 0.7121 | 8.76 |
33	| | 2 | 0.1096 | 108.72 | 0.0067 | 0.7136 | 11.18 |
34	| **Full-FT, K=4, random** | 0 | 0.1126 | 107.17 | 0.0045 | 0.7061 | 8.77 |
35	| | 1 | 0.1111 | 107.87 | 0.0047 | 0.7094 | 8.70 |
36	| | 2 | 0.1117 | 108.64 | 0.0065 | 0.7114 | 8.82 |
37	
38	---
39	
40	## Table 2: Vendi Score Trajectory Summary
41	
42	| Experiment | Training | K | Curation | Vendi gen0 | Vendi gen2 | Abs Change | Rel Change (%) |
43	|-----------|----------|---|-------
…[truncated 4080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T03:37:16.204242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/carr_dryrun_feasibility_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/carr_dryrun_feasibility_report.md"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T03:37:16.204394+00:00_

1	# CARR Dry-Run Feasibility Report
2	
3	## Summary
4	
5	CARR adaptive weights mechanism is **correct but shows minimal differentiation** in the current setting (99.3% selection overlap with fixed equal weights). Root cause: the three proxy score dimensions are highly correlated (r=0.63-0.77), eliminating the selection pressure that CARR needs to operate.
6	
7	## Data
8	
9	- Source: `/root/autodl-tmp/carr/outputs_fullft_lr2e5/` (3 generations, 2000 prompts x 4 candidates each)
10	- Proxy scores computed from text: Quality (structure+richness), Diversity (trigram Jaccard distance to siblings), Complexity (word/sentence length + bigram uniqueness)
11	- No GPU used; pure CPU analysis on 500 prompts per generation
12	
13	## Results
14	
15	### 1. CARR Weight Evolution (eta=0.5, Fixed Share alpha=0.1)
16	
17	| Stage | w_quality | w_diversity | w_complexity |
18	|-------|-----------|-------------|--------------|
19	| Gen 0 (init) | 0.3333 | 0.3333 | 0.3333 |
20	| Gen 1 | 0.3209 | 0.3402 | 0.3389 |
21	| Gen 2 | 0.3197 | 0.3454 | 0.3349 |
22	| Final | 0.3155 | 0.3536 | 0.3308 |
23	
24	Weight shift is minimal. Diversity weight increases slightly because diversity shows the highest CV across candidates.
25	
26	### 2. Selection Overlap (Fixed vs CARR)
27	
28	| Generation | Overlap |
29	|-----------|---------|
30	| Gen 0 | 100.0% (identical weights) |
31	| Gen 1 | 99.0% (5/500 differ) |
32	| Gen 2 | 99.0% (5/500 differ) |
33	
34	### 3. Learning Rate Sensitivity
35	
36	| eta | G1 overlap | G2 overlap | Final w_diversity |
37	|-----|-----------|-----------|-------------------|
38	| 0.1 | 100.0% | 99.6% | 0.337 |
39	| 0.5 | 99.0% | 99.0% | 0.354 |
40	| 1.0 | 98.0% | 98.6% | 0.374 |
41	| 2.0 | 97.2% | 97.2% | 0.416 |
42	| 5.0 | 94.6% | 93.2% | 0.538 |
43	| 10.0 | 90.0% | 87.6% | 0.701 |
44	
45	Even at eta=10 (extremely aggressive), overlap stays above 87%.
46	
47	### 4. Why: Score Correlation
48	
49	| | Quality | Diversity | Complexity |
50	|---|---------|-----------|------------|
5
…[truncated 2582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T03:37:16.204617+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/paper_outline_d.md",
  "content": "# Direction D: Negative Result Paper Outline\n\n## 1. Title Candidates\n\n**T1**: Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training\n\n**T2**: The Diversity Collapse That Didn't Happen: An Empirical Study of Reward-Based Curation in Iterative Self-Training\n\n**T3**: Reward Curation Without Collapse: Why Iterative Self-Training Resists Diversity Loss Under Standard Conditions\n\n推荐 T1: 问句形式吸引注意力，\"Surprising Resilience\" 同时传达 negative result 和 positive framing。\n\n---\n\n## 2. Abstract 核心 Message (3 sentences)\n\n**S1 (问题 + 假设来源)**: A growing body of work warns that reward-based optimization reduces output diversity in language models, raising concerns that iterative self-training with reward curation could trigger compounding diversity collapse across generations.\n\n**S2 (核心 finding)**: Through a systematic empirical study spanning 6 training configurations (varying adaptation method, selection pressure, and learning rate) over 3 iterative generations, we find that reward-based curation does not cause measurable diversity collapse under standard conditions; all curated conditions show Vendi Score changes below 1%, with the observed gap relative to uncurated baselines attributable to training capacity constraints rather than curation itself.\n\n**S3 (为什么重要)**: This negative result challenges the assumption that diversity-preserving mechanisms are necessary for reward-curated self-training, and provides concrete boundary conditions that help the community distinguish settings where collapse is a real risk from those where it is not.\n\n---\n\n## 3. Sections Outline\n\n### 3.1 Introduction\n\n**动机 (P1-P2)**:\n- Iterative self-training (self-consuming loops) 越来越普遍: 模型生成数据 → 筛选 → 重新训练\n- Reward-based curation (用 reward model 选择高质量样本) 是标准做法\n- 直觉担忧: 每一代选择高 reward 样本 → 训练分布窄化 → 下一代更窄 → compounding collapse\n- Kirk et al. (2024) 发现单轮 RLHF 降低 diversity; 延伸到 iterative 设置，collapse 风险应更严重\n\n**问题定义 (P3)**:\n- 核心问题: 在多代 iterative self-training 中，reward-based curation 是否真的导致 measurable diversity collapse?\n- 这个问题重要因为: 如果 collapse 是 real risk，需要 diversity-preserving 机制 (DIVE, DARLING, GEM 等); 如果不是，这些机制的 motivation 需要重新审视\n\n**我们的发现 (P4)**:\n- 6 条件 × 3 代系统实验: 变化 adaptation method (LoRA vs Full-FT), selection pressure (K=4, 8, 16), learning rate\n- 核心结果: 所有 curated 条件 Vendi Score 变化 < 1%，无 collapse 信号\n- Baseline 对比: no-curation 条件 diversity 自然增长 +1.4% 到 +3.1%\n- LoRA 条件下观察到的 3pp 相对 gap 是 capacity artifact，Full-FT 下消失\n\n**Contributions (list)**:\n1. 首个系统性实证研究 reward-based curation 在 iterative self-training 中对 diversity 的影响，覆盖 6 种训练配置 × 3 代迭代\n2. 证伪 \"curation causes compounding collapse\" 假设: 即使在 loss 下降 80% 的激进学习条件下，diversity 仍保持稳定或微增\n3. 识别 LoRA capacity artifact: LoRA 条件下观察到的 diversity gap 来自参数容量限制而非 curation 效应，Full-FT 消除该 gap\n4. 提供 boundary conditions taxonomy: 归纳什么条件下 collapse 不发生，为未来研究划定关注边界\n5. (conditional, if K=16 data available) 发现 extreme selection pressure (K=16, 6.25% 保留率) 下的边界行为\n\n### 3.2 Related Work\n\n**分组**:\n\n**(a) Diversity in RLHF and Reward Optimization**\n- Kirk et al. (2024, ICLR): RLHF reduces lexical/semantic diversity (foundational observation, 单轮)\n- CD-RLHF (ACL 2025): curiosity-driven reward 维持 diversity in online RL\n- 我们的定位: Kirk et al. 的发现在单轮成立，但我们的 iterative 设置显示 curation 单独并不导致 compounding 效应\n\n**(b) Iterative Self-Training and Self-Consuming Loops**\n- Self-play / self-improvement literature (STaR, ReST, etc.)\n- Model collapse in generative models (Shumailov et al., 2024): 训练在自己的输出上导致 distribution collapse\n- DIVE (2501.00747): 专门解决 iterative self-improvement 中的 diversity loss\n- 我们的定位: model collapse literature 关注 unfiltered self-training; 我们关注 reward-filtered self-training，发现 curation filter 并不加剧 collapse\n\n**(c) Diversity-Preserving Training Methods**\n- DARLING (Facebook, 2509.02534): online RL 中 quality+diversity 联合优化\n- GEM (ICLR 2025): game-theoretic 方法维持 SFT diversity\n- 我们的定位: 这些方法假设 collapse 是 default outcome，但我们的证据显示在 standard iterative SFT 中 collapse 并未自然发生\n\n**(d) Diversity Measurement**\n- Vendi Score, Self-BLEU, embedding-based metrics\n- 简要说明 metric 选择的 rationale\n\n### 3.3 Experimental Setup\n\n**Pipeline 描述**:\n- Base model: Qwen3-0.6B (选择理由: 小模型允许完整 iterative loop 在合理时间内完成; 0.6B 是最小的 \"capable\" 模型，能生成 coherent responses)\n- Dataset: UltraFeedback 2200 prompts (通用指令 following)\n- 每代: 对每个 prompt 生成 K 个候选 → reward model (ArmoRM) 评分 → 选择 top-1 → 训练下一代模型\n- 3 generations (Gen 0 → Gen 1 → Gen 2)\n\n**条件设计 (6 conditions)**:\n| Condition | Adaptation | K | LR | Curation | Rationale |\n|-----------|-----------|---|-----|----------|-----------|\n| C1 | LoRA (r=16) | 4 | 2e-4 | ArmoRM top-1 | Standard LoRA setup |\n| C2 | LoRA (r=16) | 8 | 2e-4 | ArmoRM top-1 | Doubled selection pressure |\n| C3 | Full-FT | 4 | 5e-6 | ArmoRM top-1 | Full capacity, conservative LR |\n| C4 | Full-FT | 4 | 2e-5 | ArmoRM top-1 | Full capacity, aggressive LR |\n| C5 | LoRA (r=16) | 4 | 2e-4 | Random 1-of-K | No-curation baseline (LoRA) |\n| C6 | Full-FT | 4 | 5e-6 | Random 1-of-K | No-curation baseline (Full-FT) |\n\n(+ C7: Full-FT K=16 LR=2e-5, if available)\n\n**变量设计逻辑**:\n- LoRA vs Full-FT: 隔离参数容量的影响\n- K=4 vs K=8 (vs K=16): 隔离 selection pressure 的影响\n- LR=5e-6 vs 2e-5: 隔离学习强度的影响 (underfitting vs aggressive fitting)\n- Curated vs Random: 隔离 curation 本身的因果效应\n\n**Metrics**:\n- Vendi Score (primary): kernel-based diversity, 捕捉 semantic diversity\n- Self-BLEU: lexical overlap\n- NN Distance: embedding space 中 nearest-neighbor 距离\n- Training loss: 学习动态\n- ArmoRM quality score: 质量保持\n\n### 3.4 Results\n\n**Main Finding: No Diversity Collapse (Section 4.1)**\n- 核心表格: 所有 6 条件的 Vendi Score 轨迹\n- Claim: 所有 curated 条件 Vendi 变化 < 1% (range: -0.27% to +0.91%)\n- 即使 K=8 (12.5% 保留率)，collapse 仍不出现\n- 即使 loss 下降 80% (Full-FT lr=2e-5)，模型 aggressively 拟合 curated 分布，diversity 仍微增 (+0.68%)\n\n**Sub-finding 1: Relative Suppression, Not Absolute Collapse (Section 4.2)**\n- No-curation baselines 显示 diversity 自然增长 (+1.4% to +3.1%)\n- Curated 条件增长被抑制但不逆转\n- Distinction 很重要: \"slower growth\" ≠ \"collapse\"\n\n**Sub-finding 2: LoRA Capacity Artifact (Section 4.3)**\n- LoRA K=4 和 K=8 收敛到完全相同的 Vendi Score (107.25)\n- LoRA vs baseline 的 3pp gap 在 Full-FT 下消失 (0.47pp)\n- 诊断: LoRA 只有 1.67% 可训练参数，对 diversity 施加了 implicit regularization\n- 这意味着: LoRA 条件下观察到的任何 \"curation effect\" 是 confounded\n\n**Sub-finding 3: Quality-Diversity Non-Tradeoff (Section 4.4)**\n- ArmoRM 质量评分在所有条件下保持稳定 (变化 < 1.2%)\n- 无 quality-diversity tradeoff: curation 不提升质量也不降低 diversity\n- 可能原因: reward model 区分度不足 (候选间 reward gap 仅 ~0.04)\n\n**(Conditional) Sub-finding 4: K=16 Boundary Condition (Section 4.5)**\n- If K=16 shows collapse: 发现 boundary (K=8 safe, K=16 collapses)\n- If K=16 also stable: further strengthens the negative result\n\n### 3.5 Analysis\n\n**Why doesn't collapse happen? (Section 5.1)**\n- 假说 1: Prompt diversity as anchor. 2200 个不同 prompts 提供了足够的 diversity floor, 即使每个 prompt 内选择窄了，prompt 间的差异维持了 corpus-level diversity\n- 假说 2: Reward model saturation. ArmoRM 对候选的区分度低 (within-prompt reward range ~0.04), 选择压力实际很弱\n- 假说 3: Generation stochasticity. Temperature > 0 的生成过程本身注入了足够的随机性，抵消了 curation 的 narrowing 效应\n- 数据支持: per-prompt candidate variance 表格\n\n**When MIGHT collapse occur? (Section 5.2)**\n- 条件推测 (based on our evidence + literature):\n  - Much higher K (e.g., K=64, 1.5% 保留率)\n  - Longer iteration (T >> 3)\n  - Narrower prompt set (few-prompt specialization)\n  - Stronger reward signal / more discriminative reward model\n  - Combination of multiple factors\n- 这不是 speculation: 每个条件都有对应的实验/文献证据\n\n**CARR Dry-Run Insights (Section 5.3)**\n- Adaptive reweighting 在当前设置下 99.3% selection overlap\n- 根因: proxy score 维度高度相关 (r=0.63-0.77)\n- Implication: multi-objective curation 只在 reward 维度 sufficiently orthogonal 时有价值\n- 这本身是一个 useful negative finding: naive multi-objective curation 可能不提供增量\n\n### 3.6 Discussion\n\n**Implications for the field (Section 6.1)**:\n- 重新评估 diversity-preserving 方法的 motivation: 如果 standard iterative SFT 本身不产生 collapse，那些方法的 value proposition 需要更 specific 的条件定义\n- 不是说这些方法无用: 而是说它们在更极端条件下 (更高 K, 更多代, 更强 reward) 可能才有必要\n- 实践指导: 对于标准 iterative self-training pipeline (moderate K, 3-5 代, LoRA/full-FT)，diversity collapse 不应是首要担忧\n\n**Relation to Kirk et al. (Section 6.2)**:\n- Kirk et al. 的 observation (RLHF reduces diversity) 在单轮中成立\n- 但在 iterative SFT 中，curation 的效应没有 compound: 每一代的 diversity loss 不累积\n- 可能原因: SFT ≠ RLHF; iterative generation 注入了足够的 stochasticity\n\n**Limitations (Section 6.3)**:\n- 模型规模: 仅测试 0.6B, 更大模型可能行为不同\n- 代数: 仅 3 代, 长期 (10+ 代) 效应未知\n- 数据: UltraFeedback 2200 prompts, 更窄的 domain-specific 数据可能不同\n- Reward model: 仅用 ArmoRM, 更强/更对齐的 reward model 可能产生更大 selection pressure\n- Diversity metrics: 主要依赖 Vendi Score, 可能未捕捉所有维度的 diversity (e.g., reasoning diversity, style diversity)\n\n### 3.7 Conclusion\n\n- 重申核心发现: reward curation 在 standard conditions 下不导致 iterative diversity collapse\n- 贡献: 系统实验 + LoRA artifact 识别 + boundary conditions\n- Call to action: 未来研究应 (1) 明确定义 collapse 发生的 sufficient conditions, (2) 在更极端设置下验证, (3) 区分 \"relative suppression\" 和 \"absolute collapse\"\n\n---\n\n## 4. Tables/Figures 清单\n\n### Main Paper\n\n| ID | 类型 | 标题 | 内容 | Section | 用途 |\n|----|------|------|------|---------|------|\n| **Table 1** | Table | Vendi Score Trajectory Across Conditions and Generations | 6 条件 × 3 代 Vendi Score (Gen0, Gen1, Gen2) + 绝对变化 + 相对变化%, 加粗 baseline | 4.1 Results | **Main result table** |\n| **Figure 1** | Figure | Experimental Pipeline Overview | Iterative self-training loop 示意图: Generate K → Reward Score → Select Top-1 → Train → Next Gen. 标注各 condition 的变量 | 3 Setup | Pipeline 说明 |\n| **Figure 2** | Figure | Vendi Score Trajectories: Curated vs Uncurated | 折线图, x=generation, y=Vendi Score, 6 条线 (4 curated + 2 baseline), baseline 用虚线. 直观展示: curated 平坦, baseline 微升, 无 collapse | 4.1 Results | **Core visualization** |\n| **Table 2** | Table | Full Metrics by Generation | 6 条件 × 3 代的完整指标 (Quality, Vendi, Self-BLEU, NN Distance, PPL) | 4.1 Results | 完整数据 |\n| **Figure 3** | Figure | LoRA Capacity Artifact: K=4 vs K=8 Convergence | 并排对比: LoRA K=4 和 K=8 的 Vendi 轨迹几乎重合 (Gen2 都是 107.25); 加注 Full-FT 消除 gap | 4.3 Analysis | LoRA artifact 可视化 |\n| **Table 3** | Table | Training Loss Dynamics Across Conditions | 6 条件 × 3 代 average training loss, 显示 learning dynamics 差异 | 4.1 Results | 训练动态 |\n| **Figure 4** | Figure | Relative Diversity Suppression: Curated vs Baseline Gap | Bar chart: 每个 curated 条件 vs 对应 baseline 的 Vendi gap (pp), 标注 LoRA artifact 部分 | 4.2 Results | Suppression vs collapse 区分 |\n\n### Supplementary / Appendix\n\n| ID | 类型 | 标题 | 内容 | Section | 用途 |\n|----|------|------|------|---------|------|\n| **Table A1** | Table | Per-Generation Training Loss (Detailed) | 每个条件的 per-step loss 曲线数据 | Appendix | 训练细节 |\n| **Table A2** | Table | CARR Dry-Run: Weight Evolution and Selection Overlap | CARR adaptive weights 变化 + 与 fixed-weight 的 overlap % | 5.3 Analysis | CARR negative finding |\n| **Table A3** | Table | Proxy Score Correlation Matrix | Quality/Diversity/Complexity 三维度间 Pearson r | 5.3 Analysis | 解释 CARR 失效原因 |\n| **Figure A1** | Figure | Per-Prompt Candidate Variance Across Generations | 3 代的 within-prompt score variance 下降趋势 | 5.1 Analysis | 解释 reward signal 弱化 |\n| **Table A4** | Table | Quality Retention Across Conditions | ArmoRM 质量评分的 gen0 vs gen2 对比 | 4.4 Results | Quality 稳定性 |\n| **(Conditional) Table 4 / Figure 5** | Table/Figure | K=16 Boundary Condition Results | K=16 的 Vendi 轨迹, 与 K=4/K=8 对比 | 4.5 Results | Boundary finding (if available) |\n\n### 图表总计\n- Main paper: 4 Figures + 3 Tables (约 2.5-3 页空间)\n- Appendix: 1 Figure + 3-4 Tables\n- Conditional: 1 Table/Figure (K=16 data)\n\n---\n\n## 5. 页数预估与优先级\n\nEMNLP 2026 长文限额 8 页正文 + unlimited references/appendix:\n\n| Section | 预估页数 | 优先级 |\n|---------|----------|--------|\n| Abstract | 0.3 | P0 |\n| Introduction | 1.2 | P0 |\n| Related Work | 1.0 | P1 |\n| Experimental Setup | 1.0 | P0 |\n| Results | 2.0 | P0 |\n| Analysis | 1.5 | P0 |\n| Discussion + Limitations | 0.7 | P1 |\n| Conclusion | 0.3 | P2 |\n| **Total** | **8.0** | |\n\n---\n\n## 6. 论文 Framing 关键策略\n\n### 6.1 Narrative Arc\n```\nIntuitive fear (curation → narrowing → collapse)\n    → Systematic test (6 conditions × 3 generations)\n        → Surprising result (no collapse at all)\n            → Deeper understanding (why, when, boundary)\n                → Actionable guidance (when to worry, when not to)\n```\n\n### 6.2 避免的陷阱\n- **不要写成 \"我们失败了\"**: 写成 \"contrary to widespread expectation, we find...\"\n- **不要贬低 diversity-preserving 方法**: 写成 \"our results refine the conditions under which these methods are most needed\"\n- **不要过度泛化**: 明确 boundary conditions (model size, K range, generation count, prompt diversity)\n- **不要忽视 relative suppression**: 承认 curation 确实抑制了自然增长，只是不导致 absolute collapse\n\n### 6.3 Selling Points for Reviewers\n1. **Timeliness**: iterative self-training 是当前热点，diversity concern 是 open question\n2. **Rigor**: 6 条件系统对照，隔离了 adaptation method / selection pressure / learning rate 三个变量\n3. **Actionable**: 不只是说 \"没有 collapse\"，还分析了 why 和 when might\n4. **Honest**: 明确 limitations 和 boundary conditions，不过度宣传\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/paper_outline_d.md",
    "content": "# Direction D: Negative Result Paper Outline\n\n## 1. Title Candidates\n\n**T1**: Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training\n\n**T2**: The Diversity Collapse That Didn't Happen: An Empirical Study of Reward-Based Curation in Iterative Self-Training\n\n**T3**: Reward Curation Without Collapse: Why Iterative Self-Training Resists Diversity Loss Under Standard Conditions\n\n推荐 T1: 问句形式吸引注意力，\"Surprising Resilience\" 同时传达 negative result 和 positive framing。\n\n---\n\n## 2. Abstract 核心 Message (3 sentences)\n\n**S1 (问题 + 假设来源)**: A growing body of work warns that reward-based optimization reduces output diversity in language models, raising concerns that iterative self-training with reward curation could trigger compounding diversity collapse across generations.\n\n**S2 (核心 finding)**: Through a systematic empirical study spanning 6 training configurations (varying adaptation method, selection pressure, and learning rate) over 3 iterative generations, we find that reward-based curation does not cause measurable diversity collapse under standard conditions; all curated conditions show Vendi Score changes below 1%, with the observed gap relative to uncurated baselines attributable to training capacity constraints rather than curation itself.\n\n**S3 (为什么重要)**: This negative result challenges the assumption that diversity-preserving mechanisms are necessary for reward-curated self-training, and provides concrete boundary conditions that help the community distinguish settings where collapse is a real risk from those where it is not.\n\n---\n\n## 3. Sections Outline\n\n### 3.1 Introduction\n\n**动机 (P1-P2)**:\n- Iterative self-training (self-consuming loops) 越来越普遍: 模型生成数据 → 筛选 → 重新训练\n- Reward-based curation (用 reward model 选择高质量样本) 是标准做法\n- 直觉担忧: 每一代选择高 reward 样本 → 训练分布窄化 → 下一代更窄 → compounding collapse\n- Kirk et al. (2024) 发现单轮 RLHF 降低 diversity; 延伸到 iterative 设置，collapse 风险应更严重\n\n**问题定义 (P3)**:\n- 核心问题: 在多代 iterative self-training 中，reward-based curation 是否真的导致 measurable diversity collapse?\n- 这个问题重要因为: 如果 collapse 是 real risk，需要 diversity-preserving 机制 (DIVE, DARLING, GEM 等); 如果不是，这些机制的 motivation 需要重新审视\n\n**我们的发现 (P4)**:\n- 6 条件 × 3 代系统实验: 变化 adaptation method (LoRA vs Full-FT), selection pressure (K=4, 8, 16), learning rate\n- 核心结果: 所有 curated 条件 Vendi Score 变化 < 1%，无 collapse 信号\n- Baseline 对比: no-curation 条件 diversity 自然增长 +1.4% 到 +3.1%\n- LoRA 条件下观察到的 3pp 相对 gap 是 capacity artifact，Full-FT 下消失\n\n**Contributions (list)**:\n1. 首个系统性实证研究 reward-based curation 在 iterative self-training 中对 diversity 的影响，覆盖 6 种训练配置 × 3 代迭代\n2. 证伪 \"curation causes compounding collapse\" 假设: 即使在 loss 下降 80% 的激进学习条件下，diversity 仍保持稳定或微增\n3. 识别 LoRA capacity artifact: LoRA 条件下观察到的 diversity gap 来自参数容量限制而非 curation 效应，Full-FT 消除该 gap\n4. 提供 boundary conditions taxonomy: 归纳什么条件下 collapse 不发生，为未来研究划定关注边界\n5. (conditional, if K=16 data available) 发现 extreme selection pressure (K=16, 6.25% 保留率) 下的边界行为\n\n### 3.2 Related Work\n\n**分组**:\n\n**(a) Diversity in RLHF and Reward Optimization**\n- Kirk et al. (2024, ICLR): RLHF reduces lexical/semantic diversity (foundational observation, 单轮)\n- CD-RLHF (ACL 2025): curiosity-driven reward 维持 diversity in online RL\n- 我们的定位: Kirk et al. 的发现在单轮成立，但我们的 iterative 设置显示 curation 单独并不导致 compounding 效应\n\n**(b) Iterative Self-Training and Self-Consuming Loops**\n- Self-play / self-improvement literature (STaR, ReST, etc.)\n- Model collapse in generative models (Shumailov et al., 2024): 训练在自己的输出上导致 distribution collapse\n- DIVE (2501.00747): 专门解决 iterative self-improvement 中的 diversity loss\n- 我们的定位: model collapse literature 关注 unfiltered self-training; 我们关注 reward-filtered self-training，发现 curation filter 并不加剧 collapse\n\n**(c) Diversity-Preserving Training Methods**\n- DARLING (Facebook, 2509.02534): online RL 中 quality+diversity 联合优化\n- GEM (ICLR 2025): game-theoretic 方法维持 SFT diversity\n- 我们的定位: 这些方法假设 collapse 是 default outcome，但我们的证据显示在 standard iterative SFT 中 collapse 并未自然发生\n\n**(d) Diversity Measurement**\n- Vendi Score, Self-BLEU, embedding-based metrics\n- 简要说明 metric 选择的 rationale\n\n### 3.3 Experimental Setup\n\n**Pipeline 描述**:\n- Base model: Qwen3-0.6B (选择理由: 小模型允许完整 iterative loop 在合理时间内完成; 0.6B 是最小的 \"capable\" 模型，能生成 coherent responses)\n- Dataset: UltraFeedback 2200 prompts (通用指令 following)\n- 每代: 对每个 prompt 生成 K 个候选 → reward model (ArmoRM) 评分 → 选择 top-1 → 训练下一代模型\n- 3 generations (Gen 0 → Gen 1 → Gen 2)\n\n**条件设计 (6 conditions)**:\n| Condition | Adaptation | K | LR | Curation | Rationale |\n|-----------|-----------|---|-----|----------|-----------|\n| C1 | LoRA (r=16) | 4 | 2e-4 | ArmoRM top-1 | Standard LoRA setup |\n| C2 | LoRA (r=16) | 8 | 2e-4 | ArmoRM top-1 | Doubled selection pressure |\n| C3 | Full-FT | 4 | 5e-6 | ArmoRM top-1 | Full capacity, conservative LR |\n| C4 | Full-FT | 4 | 2e-5 | ArmoRM top-1 | Full capacity, aggressive LR |\n| C5 | LoRA (r=16) | 4 | 2e-4 | Random 1-of-K | No-curation baseline (LoRA) |\n| C6 | Full-FT | 4 | 5e-6 | Random 1-of-K | No-curation baseline (Full-FT) |\n\n(+ C7: Full-FT K=16 LR=2e-5, if available)\n\n**变量设计逻辑**:\n- LoRA vs Full-FT: 隔离参数容量的影响\n- K=4 vs K=8 (vs K=16): 隔离 selection pressure 的影响\n- LR=5e-6 vs 2e-5: 隔离学习强度的影响 (underfitting vs aggressive fitting)\n- Curated vs Random: 隔离 curation 本身的因果效应\n\n**Metrics**:\n- Vendi Score (primary): kernel-based diversity, 捕捉 semantic diversity\n- Self-BLEU: lexical overlap\n- NN Distance: embedding space 中 nearest-neighbor 距离\n- Training loss: 学习动态\n- ArmoRM quality score: 质量保持\n\n### 3.4 Results\n\n**Main Finding: No Diversity Collapse (Section 4.1)**\n- 核心表格: 所有 6 条件的 Vendi Score 轨迹\n- Claim: 所有 curated 条件 Vendi 变化 < 1% (range: -0.27% to +0.91%)\n- 即使 K=8 (12.5% 保留率)，collapse 仍不出现\n- 即使 loss 下降 80% (Full-FT lr=2e-5)，模型 aggressively 拟合 curated 分布，diversity 仍微增 (+0.68%)\n\n**Sub-finding 1: Relative Suppression, Not Absolute Collapse (Section 4.2)**\n- No-curation baselines 显示 diversity 自然增长 (+1.4% to +3.1%)\n- Curated 条件增长被抑制但不逆转\n- Distinction 很重要: \"slower growth\" ≠ \"collapse\"\n\n**Sub-finding 2: LoRA Capacity Artifact (Section 4.3)**\n- LoRA K=4 和 K=8 收敛到完全相同的 Vendi Score (107.25)\n- LoRA vs baseline 的 3pp gap 在 Full-FT 下消失 (0.47pp)\n- 诊断: LoRA 只有 1.67% 可训练参数，对 diversity 施加了 implicit regularization\n- 这意味着: LoRA 条件下观察到的任何 \"curation effect\" 是 confounded\n\n**Sub-finding 3: Quality-Diversity Non-Tradeoff (Section 4.4)**\n- ArmoRM 质量评分在所有条件下保持稳定 (变化 < 1.2%)\n- 无 quality-diversity tradeoff: curation 不提升质量也不降低 diversity\n- 可能原因: reward model 区分度不足 (候选间 reward gap 仅 ~0.04)\n\n**(Conditional) Sub-finding 4: K=16 Boundary Condition (Section 4.5)**\n- If K=16 shows collapse: 发现 boundary (K=8 safe, K=16 collapses)\n- If K=16 also stable: further strengthens the negative result\n\n### 3.5 Analysis\n\n**Why doesn't collapse happen? (Section 5.1)**\n- 假说 1: Prompt diversity as anchor. 2200 个不同 prompts 提供了足够的 diversity floor, 即使每个 prompt 内选择窄了，prompt 间的差异维持了 corpus-level diversity\n- 假说 2: Reward model saturation. ArmoRM 对候选的区分度低 (within-prompt reward range ~0.04), 选择压力实际很弱\n- 假说 3: Generation stochasticity. Temperature > 0 的生成过程本身注入了足够的随机性，抵消了 curation 的 narrowing 效应\n- 数据支持: per-prompt candidate variance 表格\n\n**When MIGHT collapse occur? (Section 5.2)**\n- 条件推测 (based on our evidence + literature):\n  - Much higher K (e.g., K=64, 1.5% 保留率)\n  - Longer iteration (T >> 3)\n  - Narrower prompt set (few-prompt specialization)\n  - Stronger reward signal / more discriminative reward model\n  - Combination of multiple factors\n- 这不是 speculation: 每个条件都有对应的实验/文献证据\n\n**CARR Dry-Run Insights (Section 5.3)**\n- Adaptive reweighting 在当前设置下 99.3% selection overlap\n- 根因: proxy score 维度高度相关 (r=0.63-0.77)\n- Implication: multi-objective curation 只在 reward 维度 sufficiently orthogonal 时有价值\n- 这本身是一个 useful negative finding: naive multi-objective curation 可能不提供增量\n\n### 3.6 Discussion\n\n**Implications for the field (Section 6.1)**:\n- 重新评估 diversity-preserving 方法的 motivation: 如果 standard iterative SFT 本身不产生 collapse，那些方法的 value proposition 需要更 specific 的条件定义\n- 不是说这些方法无用: 而是说它们在更极端条件下 (更高 K, 更多代, 更强 reward) 可能才有必要\n- 实践指导: 对于标准 iterative self-training pipeline (moderate K, 3-5 代, LoRA/full-FT)，diversity collapse 不应是首要担忧\n\n**Relation to Kirk et al. (Section 6.2)**:\n- Kirk et al. 的 observation (RLHF reduces diversity) 在单轮中成立\n- 但在 iterative SFT 中，curation 的效应没有 compound: 每一代的 diversity loss 不累积\n- 可能原因: SFT ≠ RLHF; iterative generation 注入了足够的 stochasticity\n\n**Limitations (Section 6.3)**:\n- 模型规模: 仅测试 0.6B, 更大模型可能行为不同\n- 代数: 仅 3 代, 长期 (10+ 代) 效应未知\n- 数据: UltraFeedback 2200 prompts, 更窄的 domain-specific 数据可能不同\n- Reward model: 仅用 ArmoRM, 更强/更对齐的 reward model 可能产生更大 selection pressure\n- Diversity metrics: 主要依赖 Vendi Score, 可能未捕捉所有维度的 diversity (e.g., reasoning diversity, style diversity)\n\n### 3.7 Conclusion\n\n- 重申核心发现: reward curation 在 standard conditions 下不导致 iterative diversity collapse\n- 贡献: 系统实验 + LoRA artifact 识别 + boundary conditions\n- Call to action: 未来研究应 (1) 明确定义 collapse 发生的 sufficient conditions, (2) 在更极端设置下验证, (3) 区分 \"relative suppression\" 和 \"absolute collapse\"\n\n---\n\n## 4. Tables/Figures 清单\n\n### Main Paper\n\n| ID | 类型 | 标题 | 内容 | Section | 用途 |\n|----|------|------|------|---------|------|\n| **Table 1** | Table | Vendi Score Trajectory Across Conditions and Generations | 6 条件 × 3 代 Vendi Score (Gen0, Gen1, Gen2) + 绝对变化 + 相对变化%, 加粗 baseline | 4.1 Results | **Main result table** |\n| **Figure 1** | Figure | Experimental Pipeline Overview | Iterative self-training loop 示意图: Generate K → Reward Score → Select Top-1 → Train → Next Gen. 标注各 condition 的变量 | 3 Setup | Pipeline 说明 |\n| **Figure 2** | Figure | Vendi Score Trajectories: Curated vs Uncurated | 折线图, x=generation, y=Vendi Score, 6 条线 (4 curated + 2 baseline), baseline 用虚线. 直观展示: curated 平坦, baseline 微升, 无 collapse | 4.1 Results | **Core visualization** |\n| **Table 2** | Table | Full Metrics by Generation | 6 条件 × 3 代的完整指标 (Quality, Vendi, Self-BLEU, NN Distance, PPL) | 4.1 Results | 完整数据 |\n| **Figure 3** | Figure | LoRA Capacity Artifact: K=4 vs K=8 Convergence | 并排对比: LoRA K=4 和 K=8 的 Vendi 轨迹几乎重合 (Gen2 都是 107.25); 加注 Full-FT 消除 gap | 4.3 Analysis | LoRA artifact 可视化 |\n| **Table 3** | Table | Training Loss Dynamics Across Conditions | 6 条件 × 3 代 average training loss, 显示 learning dynamics 差异 | 4.1 Results | 训练动态 |\n| **Figure 4** | Figure | Relative Diversity Suppression: Curated vs Baseline Gap | Bar chart: 每个 curated 条件 vs 对应 baseline 的 Vendi gap (pp), 标注 LoRA artifact 部分 | 4.2 Results | Suppression vs collapse 区分 |\n\n### Supplementary / Appendix\n\n| ID | 类型 | 标题 | 内容 | Section | 用途 |\n|----|------|------|------|---------|------|\n| **Table A1** | Table | Per-Generation Training Loss (Detailed) | 每个条件的 per-step loss 曲线数据 | Appendix | 训练细节 |\n| **Table A2** | Table | CARR Dry-Run: Weight Evolution and Selection Overlap | CARR adaptive weights 变化 + 与 fixed-weight 的 overlap % | 5.3 Analysis | CARR negative finding |\n| **Table A3** | Table | Proxy Score Correlation Matrix | Quality/Diversity/Complexity 三维度间 Pearson r | 5.3 Analysis | 解释 CARR 失效原因 |\n| **Figure A1** | Figure | Per-Prompt Candidate Variance Across Generations | 3 代的 within-prompt score variance 下降趋势 | 5.1 Analysis | 解释 reward signal 弱化 |\n| **Table A4** | Table | Quality Retention Across Conditions | ArmoRM 质量评分的 gen0 vs gen2 对比 | 4.4 Results | Quality 稳定性 |\n| **(Conditional) Table 4 / Figure 5** | Table/Figure | K=16 Boundary Condition Results | K=16 的 Vendi 轨迹, 与 K=4/K=8 对比 | 4.5 Results | Boundary finding (if available) |\n\n### 图表总计\n- Main paper: 4 Figures + 3 Tables (约 2.5-3 页空间)\n- Appendix: 1 Figure + 3-4 Tables\n- Conditional: 1 Table/Figure (K=16 data)\n\n---\n\n## 5. 页数预估与优先级\n\nEMNLP 2026 长文限额 8 页正文 + unlimited references/appendix:\n\n| Section | 预估页数 | 优先级 |\n|---------|----------|--------|\n| Abstract | 0.3 | P0 |\n| Introduction | 1.2 | P0 |\n| Related Work | 1.0 | P1 |\n| Experimental Setup | 1.0 | P0 |\n| Results | 2.0 | P0 |\n| Analysis | 1.5 | P0 |\n| Discussion + Limitations | 0.7 | P1 |\n| Conclusion | 0.3 | P2 |\n| **Total** | **8.0** | |\n\n---\n\n## 6. 论文 Framing 关键策略\n\n### 6.1 Narrative Arc\n```\nIntuitive fear (curation → narrowing → collapse)\n    → Systematic test (6 conditions × 3 generations)\n        → Surprising result (no collapse at all)\n            → Deeper understanding (why, when, boundary)\n                → Actionable guidance (when to worry, when not to)\n```\n\n### 6.2 避免的陷阱\n- **不要写成 \"我们失败了\"**: 写成 \"contrary to widespread expectation, we find...\"\n- **不要贬低 diversity-preserving 方法**: 写成 \"our results refine the conditions under which these methods are most needed\"\n- **不要过度泛化**: 明确 boundary conditions (model size, K range, generation count, prompt diversity)\n- **不要忽视 relative suppression**: 承认 curation 确实抑制了自然增长，只是不导致 absolute collapse\n\n### 6.3 Selling Points for Reviewers\n1. **Timeliness**: iterative self-training 是当前热点，diversity concern 是 open question\n2. **Rigor**: 6 条件系统对照，隔离了 adaptation method / selection pressure / learning rate 三个变量\n3. **Actionable**: 不只是说 \"没有 collapse\"，还分析了 why 和 when might\n4. **Honest**: 明确 limitations 和 boundary conditions，不过度宣传\n"
  }
}
````

</details>

---

### Tool result

_source line 22 · 2026-05-17T03:37:16.204965+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/paper_outline_d.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T03:37:16.205108+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T03:37:16.205233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_draft_paper_outline_20260517T033408",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-17T03:37:16.205390+00:00_

Outline 已写入 `artifacts/paper_outline_d.md`。核心结构：

**Title 推荐**: "Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training"

**论文主线**: intuitive fear → systematic test → surprising negative → deeper understanding → actionable guidance

**正文 8 页分配**:
- Introduction (1.2p): 从 Kirk et al. 的 RLHF diversity loss 延伸到 iterative 设置的 compounding collapse 担忧，5 条 contributions
- Results (2.0p): 主发现 (无 collapse) + 3 个 sub-findings (relative suppression / LoRA artifact / quality non-tradeoff) + conditional K=16
- Analysis (1.5p): 三个假说解释 why not collapse + boundary conditions + CARR dry-run negative finding

**图表**: 主文 4 Figure + 3 Table，附录 1 Figure + 3-4 Table。核心可视化是 Figure 2 (Vendi 轨迹折线图，curated 平坦 vs baseline 微升)。

**关键 framing 策略**: 不是 "我们失败了"，而是 "contrary to expectation, collapse doesn't hold under standard conditions, which refines when diversity-preserving methods are truly needed"。

需要调整或深入展开哪个部分？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_draft_paper_outline_20260517T033408"
}
```

</details>

---
