# research v9d wandb analysis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_v9d_wandb_analysis_20260520T063004_result.json`
- **Structured JSON:** [`830bda22b3da4fe949e6.json`](../../sessions/83/830bda22b3da4fe949e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**训练指标（积极）**：v9d 在 step 7 达到 91.4% 训练成功率，远超 1.7B 最好成绩（Cell A seed2 的 55.5% @ step 15）。8B 规模优势显著。

**训练稳定性（积极）**：KL 近零（-0.034），grad_norm 低且稳定（0.38-0.57），无 collapse 迹象。对比 1.7B Cell B seed1 在 step 4 就崩溃。

**值得关注**：
- **Entropy 过低**（0.047-0.060），比 1.7B 实验低 ~7 倍。策略已极度确定性，可能 premature convergence。
- **pg_loss 和 clipfrac 接近零**，剩余 23 步可能收益递减。
- **OOD 泛化完全未知**——这是论文的关键问题。Step 10 eval（test_freq=5）将是决定性数据。
- **磁盘风险**：step 5 checkpoint 仍 92GB，需确认 step 10 不会溢出。

报告路径：`artifacts/v9d_step8_analysis.md`

---
