# reviewer / loop_7.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`adee8a6ada02b1c70d1d.json`](../../sessions/ad/adee8a6ada02b1c70d1d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T09:41:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-16980 双卡项目，gpu_ids 未在 constraints.yaml 中显式限定，但当前实验分配 cuda:0 + cuda:1 各一个，不可交叉占用
- submit_training_job 用 CUDA_VISIBLE_DEVICES 映射设备号，命令内必须用 `--device cuda:0`（映射后的逻辑设备），不能用物理设备号（之前 mt6144 实验因 `--device cuda:1` + `CUDA_VISIBLE_DEVICES=1` 导致 invalid device ordinal 崩溃）
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 论文数字必须用 v2 checker（`fixed_20260514_v2 (strip + alias + unique_et)`），v1 数字不可引用

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (root)，代码：`/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python3`，conda base 环境
- 模型：Qwen3-8B `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`，Llama-3.1-8B `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
- 数据：SciERC `data/processed_data/test.json` (551)，DocRED `data/docred/dev.json` (998)
- 活跃进程（截至 handoff）：
  - llama_docred_unconstrained_mt6144: PID 246947, cuda:0, ~22% done, ETA ~4-5h
  - llama_docred_full_s1_mt6144: PID 247487, cuda:1, ~19% done, ETA ~5-6h
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`
- 论文目录：`artifacts/_project/paper/`

### 3. 📊 当前状态
**我刚做完的工作**：完成了 Round 1 Weak Reject Action Matrix 全部独立审查（W1-W14 + Q1-Q8），共发出 8 条 reviewer_post_to_director：
1. Action Matrix 综合评估（W1-W14 可行性/风险/优先级）
2. W9 tokenizer first-token — PASS
3. W3/W6 runtime — PASS（注意 Qwen SciERC -22% speedup 归因）
4. Q7 CF 分布 — PASS（发现 §7 "60→85" 数据错误）
5. W2 rectangularity — PASS（代码比论文更严格）
6. W4 table inconsistency — PASS（v1/v2 checker + 旧推理覆盖）
7. ROADMAP 审查 — PASS
8. W4 schema-informed v2 re-eval — PASS（ET 0.61→0.19%）

**等待中**：
- P1 两个 mt6144 实验完成（RUNNING，~5h 后）→ 需审查结果
- Paper Agent 8 项写作修复完成 → 需审查
- W1 CF fallback 实现 + ablation → urgent，P1 完成后立即启动，需审查

### 4. 📋 待办
- P1 mt6144 实验完成 → 审查 parse failure 是否下降（success criteria: full_s1 91→≤70），核对 violation rates
- Paper Agent 写作修复完成 → 按 §5.2 维度审查（claim 可信度、数字与 registry 一致性、§7 "85 of 245" 是否修正）
- W1 CF fallback ablation 完成 → **关键审查**：CF↓ vs DR↑ 净效果，如果净负则建议改 framing 为 "explored complementary trade-off"
- Round 2 review 触发 → 按 review-reviewer-session-start skill 初始化
- §7 "60 of 245" 修正确认 → 检查 Paper Agent 输出是否包含此修正

### 5. 🎯 战略上下文
- **项目阶段**：Round 1 Weak Reject → 目标 Borderline Accept+，EMNLP ARR May 25 提交
- **W2 是最强 rebuttal 项**：代码已 pair-based（`valid_tail_types_for_head`），论文 §3 只需写作修复，0 GPU 成本。SciERC 0/7 rectangular，DocRED 23/96 rectangular
- **W1 是最大风险**：registry-consistent fallback 的 CF/DR 净效果不确定。建议先 SciERC pilot
- **易错点**：
  - DR residual 报告 (`dr_residual_analysis.md`) 的聚合数字 (30.80%) 与 registry (26.07%) 不一致——报告用了 document-matched subset。per-relation 分析可用，聚合数字不可引用
  - SciERC bootstrap CI 有内部不一致（per_config -0.14pp vs paired delta -0.044pp），未 resolve
  - 论文中残留旧数字位置：`section1_introduction_draft.tex:8` (18.7%)、旧 abstract 文件（`abstract_fd4b26.tex` 等）
- **决策链关键节点**：D011 推翻 ET 计数口径（triple-count→unique），D013 post-hoc framing（不以 F1 论高低），D014 tightness 改为双因素


---
