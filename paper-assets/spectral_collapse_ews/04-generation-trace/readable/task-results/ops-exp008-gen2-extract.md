# ops exp008 gen2 extract

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp008-gen2-extract_20260518T145552_result.json`
- **Structured JSON:** [`55ba832cfd876936f7ba.json`](../../sessions/55/55ba832cfd876936f7ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_008 (r=0.3, seed42) 所有已完成 generation 的指标：

| gen | log_det | eff_rank | ppl | distinct_4 | train_loss |
|-----|---------|----------|-----|------------|------------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 | — |
| 1 | 2366.13 | 476.91 | 10.193 | 0.6894 | 1.8359 |
| 2 | 2372.45 | 484.17 | 10.589 | 0.4892 | 1.7744 |

共 3 个 generation (0–2)。Gen 0 无 train_loss（baseline）。

趋势：log_det 基本持平（gen2 略升），eff_rank 持续上升，ppl 逐代增长，d4 从 0.74 下降到 0.49（多样性显著衰减），train_loss 略降。

---
