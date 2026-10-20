# analysis metrics aggregation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metrics-aggregation_20260515T043938_result.json`
- **Structured JSON:** [`c15b175e09f6746fb408.json`](../../sessions/c1/c15b175e09f6746fb408.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存并注册: `artifacts/metrics_summary_table.md` (art_20260515_0414dc)

内容包含:
- **Table 1a**: 8个实验的逐实验对比（eval_return + nve @ 35K/55K/65K/85K/105K + collapse判定）
- **Table 1b**: Config级别 mean±std（008d 2 seeds, 008f 2 seeds）
- **Table 1c**: Config描述与关键问题
- **Table 2**: RSSM fidelity analysis（baseline/008d/008f 的 obs_MSE 和 reward_MAE）
- **Table 3**: 补充实验（008c, 007, 005, 003）
- **Causal claims summary**: C2/C6/B+ 证据状态

注意事项:
- baseline 早期 eval_return（35K-65K）来自其他实验的交叉引用，非 exp_001 registry 直接记录，已标注 †
- 008d config 的 mean±std 在 65K+ 仅有 seed 2 数据（seed 1 在 55K 因 collapse 停止），已标注 ‡
- exp_008e_v3 seed 2 和 exp_009a baseline seed 2 仍在 RUNNING，表格完成后可补充

---
