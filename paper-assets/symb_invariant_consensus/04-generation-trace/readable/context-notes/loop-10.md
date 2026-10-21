# reviewer / loop_10.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`a017874fb8ebfa7f6c5e.json`](../../sessions/a0/a017874fb8ebfa7f6c5e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-21T01:30:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- FOLIO SC baseline 必须用 alphabetical tiebreaking 后的 114/204=55.88%，不是旧的 111/204=54.41%。任何分析/论文引用旧值即为错误。
- Table 3 已移除（DeBERTa model confound D116）。NLI combo 数据现在在 §6 正文 + appendix Table 20。
- 论文 Table 3 统一用 w=3（Mistral +3.50pp, LLaMA +4.17pp, Qwen2.5 +0.83pp, Qwen3 +1.00pp）。Scatter 用 8-point 含 LLaMA。不要混用 w 值。
- Process-κ "ProcessSim > κ" 只在 Mistral-7B 上成立。论文主文已 scope 到 Mistral，appendix 承认 regime dependence。不要声称 universal。
- Mistral PW NLI combo 用的是 DeBERTa-**large**-mnli（非 base）。论文标注必须正确。

### 2. 🖥️ 基础设施快照
- **westd-16639**: 4× RTX PRO 6000 Blackwell (98GB each)，全部空闲。代码 `/root/symb_invariant_consensus/`
- **westd-25068**: SSH key 当前被拒（AutoDL 端口可能已变），需用户去控制台确认端口
- 论文 tex 文件在本地 `projects/symb_invariant_consensus/docs/paper/`（diagnosis.tex, solutions.tex, appendix.tex, related_work.tex, limitations_content.tex）
- 实验结果在 westd-16639:`/root/symb_invariant_consensus/results/` 各子目录
- 无活跃进程、无 cron、无 tmux session

### 3. 📊 当前状态
**论文 V11+ 已可提交**，等 R9 审稿结果。所有实验完成。

刚完成的工作：
- LLaMA-8B PW NLI combo（第 2 个 significant positive family，w=1 p=0.0001, w=3 p=0.004）
- 8-point capability gap scatter 更新（ρ=0.970, p<0.001）
- Process-κ 跨模型验证 → CRITICAL→INFO（论文已正确 scope）
- Sub-population 分析（corrected tiebreaking）→ mid-constraint tertile +9.4pp p=0.031
- BH m=12 全表（4/12 显著：Mistral w=3/w=5, LLaMA w=1/w=3）
- Dir-N Oracle Qwen3-T N=204 重算（Oracle Gap 6.0→4.90pp）

Registry: 无 RUNNING/PREPARING 实验。全部 DONE。
等待: R9 审稿结果。

### 4. 📋 待办
- R9 审稿结果到达 → 逐条核实 severity，交叉验证数据 claim，按 §5 审查维度审查
- 如果 R9 提出新实验需求 → 评估 GPU-hours vs DDL 可行性（8 卡全空，4 天余量）
- 如果 R9 要求章节重写 → 按 §5/§7 审查维度做对抗审查（先 Read paper-quality-lessons skill）
- Paper Agent 提交 V12 定稿审查 → 全文 claim-evidence 对齐检查，特别关注：
  - SC baseline 数字统一（55.88% not 54.41%）
  - NLI escape 从 "one model" 升级为 "two model families" 的 contribution bullet
  - Scatter 图与 Table 3 的 w 值一致性
  - Qwen3-T Oracle Gap 使用 N=204 版本（4.90pp not 6.0pp）

### 5. 🎯 战略上下文
**核心结论**：LLM 自提取 symbolic constraints（FOL→Z3 MAX-SAT）不能独立验证推理——约束是 bias projection，不是 independent verification。BR=4.97×, 25+ remediation 全败。唯一 escape：cross-architecture NLI verifier（DeBERTa），但仅在 generator SC ≤ 70% 时有效（sigmoid decay）。

**D116 pivot**：论文从 "SICA fails" 重新 framing 为 "Aggregation Ceiling"——test-time aggregation gain 随模型能力 sigmoid 衰减。8-point ρ=0.970。

**易踩的坑**：
1. FOLIO 有两套 SC baseline（pre/post tiebreaking fix）。所有分析必须用 post-fix（55.88%）。Worker 偶尔会从旧数据文件读到 pre-fix 值（54.41%），必须核对。
2. LLaMA-8B SC=70% > DeBERTa 55%，但 NLI combo 仍然显著——"threshold = verifier > generator" 是错的，实际是 sigmoid decay with gap magnitude。
3. 7-point scatter（ρ=0.955）和 8-point scatter（ρ=0.970）是不同版本。论文用 8-point。
4. "九 conditions" vs "十五 conditions" vs "十六 conditions" 的计数在论文不同位置可能不一致——需要全文搜索核对。
5. westd-25068 SSH 断连是 AutoDL 端口变更问题，不是 key 问题。不要反复重试，提示用户查控制台。


---
