# paper experiment section draft

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiment_section_draft_20260523T092013_result.json`
- **Structured JSON:** [`5269ac31e8ed879a60dd.json`](../../sessions/52/5269ac31e8ed879a60dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处编辑全部到位：

1. **experiments.tex** (line 26): 添加了 factorial design rationale 段落，逐一说明每个 pairwise comparison 隔离的单一变量（gradient flow / label content / spatial reference frame / temporal duration）。

2. **discussion.tex §5.2** (line 28): 在 BN interference 机制和 TSR instability 之间插入梯度分析证据段落。包含：gradient-flow 条件的 action gradient norm 与 Vanilla 可比、Detach 条件 substantially lower、action/OCC 梯度正交（cosine≈0）、Detach+LN 实验作为 ongoing work。措辞用 "at convergence"，未用具体倍数。

3. **discussion.tex §5.3** (line 41): 添加 dose-response 框架段落，描述 Cutoff@25K 和 reverse cutoff 两个计划实验，末尾用 `\textit{[Results to be added]}` 占位。

---
