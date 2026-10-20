# ops check exp004 status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp004-status_20260518T085116_result.json`
- **Structured JSON:** [`02eb7c2f3f5ff7eef47d.json`](../../sessions/02/02eb7c2f3f5ff7eef47d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_004 尚未完成。**

- PID 135411 仍在运行，已运行 14h55m，cuda:1 占用 25GB，GPU 利用率 95%
- 结果文件包含 Gen 0–9（共 10 条），Gen 10 尚未写入，正在训练中

当前已完成的 Gen 0–9 metrics：

| Gen | eff_rank | log_det | perplexity | distinct_4 | train_loss |
|-----|----------|---------|------------|------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.741 | — |
| 1 | 477.89 | 2366.58 | 10.08 | 0.669 | 1.984 |
| 2 | 487.92 | 2395.36 | 10.41 | 0.582 | 1.894 |
| 3 | 496.57 | 2425.64 | 10.76 | 0.456 | 1.733 |
| 4 | 502.05 | 2451.72 | 11.14 | 0.328 | 1.536 |
| 5 | 512.78 | 2486.34 | 11.65 | 0.235 | 1.343 |
| 6 | 519.78 | 2507.62 | 12.16 | 0.220 | 1.194 |
| 7 | 527.47 | 2525.55 | 12.77 | 0.193 | 1.144 |
| 8 | 536.39 | 2544.03 | 13.46 | 0.168 | 1.060 |
| 9 | 545.73 | 2562.13 | 14.23 | 0.102 | 0.985 |

**cuda:1 当前被 exp_004 占用（PID 135411）。** cuda:0 被 exp_007（real_ratio=0.2 实验）占用。两卡均忙。

---
