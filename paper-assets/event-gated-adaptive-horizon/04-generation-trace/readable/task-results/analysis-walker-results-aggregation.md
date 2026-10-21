# analysis walker results aggregation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_walker-results-aggregation_20260514T185728_result.json`
- **Structured JSON:** [`0cc4bd49a71a506cb4ec.json`](../../sessions/0c/0cc4bd49a71a506cb4ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出**:
- 服务器：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/paper_data_walker_walk.json`（73KB, 11 个实验全部聚合）
- 已注册 artifact: `art_20260514_fdb09b`

**聚合结果摘要**:

| 实验 | Peak Eval | @Step | Final Eval | Max V/E | nVE@45K | vs BL% |
|---|---|---|---|---|---|---|
| baseline | 970.41 | 505K | 970.41 | 0.728 | 1.00 | — |
| event_gated_v4 | 541.18 | 55K | 342.27 | 2.83 | 1.02 | -62.0 |
| fixed_dt2 | 485.33 | 35K | 132.86 | 2.72 | 1.61 | -78.4 |
| fixed_dt4 | 176.95 | 25K | 152.49 | 0.20 | 0.38 | -75.6 |
| **008a** no_sub dt2 h15 | **777.66** | 105K | 777.66 | 0.54 | 0.71 | **-15.1** |
| 008c no_sub dt2 h8 | 241.87 | 55K | 240.86 | 0.33 | 0.77 | -60.9 |
| 008d sub_on h8 | 167.22 | 25K | 82.75 | 1.67 | 2.09 | -86.8 |
| **008e_v3** sub dt1 h15 | **869.88** | 105K | 869.88 | 0.53 | 0.87 | **-5.0** |
| 008f no_embed h8 | 503.21 | 105K | 503.21 | 0.45 | 0.83 | -45.0 |
| 009b (008d s2) | 278.54 | 95K | 267.93 | 0.57 | 1.62 | -70.7 |
| 009c (008f s2) | 359.14 | 75K | 148.34 | 0.75 | 0.72 | -83.8 |

注意：baseline 没有 gate metrics（符合预期）；exp_008e_v3 是最接近 baseline 的变体（仅 -5.0%），exp_008a 次之（-15.1%）。

---
