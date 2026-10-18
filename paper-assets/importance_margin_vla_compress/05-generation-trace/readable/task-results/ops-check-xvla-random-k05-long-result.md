# ops check xvla random k05 long result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_xvla_random_k05_long_result_20260523T074732_result.json`
- **Structured JSON:** [`ba1a5efcd5989783e5f4.json`](../../sessions/ba/ba1a5efcd5989783e5f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No crons in this session (they were created in a prior session).

## 结果汇总

### 已完成 (2/4)

| 实验 | SR | Episodes | Registry |
|---|---|---|---|
| **eval_xvla_random_k05_long_seed42** | **61.6%** (308/500), CI [57.3%, 65.8%] | 500/500 | DONE ✓ |
| **eval_xvla_random_k07_long_seed42** | **53.0%** (265/500), CI [48.6%, 57.3%] | 500/500 | DONE ✓ |

Per-task SR:

| Task | Random k=0.5 | Random k=0.7 |
|---|---|---|
| T0 alphabet soup + tomato sauce | 68% | 10% |
| T1 cream cheese + butter | 0% | 8% |
| T2 stove + moka pot | 64% | 66% |
| T3 bowl in drawer | 94% | 98% |
| T4 mugs on plates | 70% | 82% |
| T5 book in caddy | 90% | 100% |
| T6 mug + pudding | 84% | 82% |
| T7 soup + cream cheese | 86% | 70% |
| T8 two moka pots | 46% | 4% |
| T9 mug in microwave | 14% | 10% |

### 仍在运行 (2/4)

| 实验 | 进度 | 预估剩余 |
|---|---|---|
| eval_xvla_l2norm_k07_long_seed42 | Task 9, ep 38/50 | ~15 min |
| eval_xvla_l2norm_k05_long_seed42 | Task 9, ep 17/50 | ~30 min |

### 观察

Random pruning 在 X-VLA Long 上呈非单调行为：k=0.95=48.2% < k=0.7=53.0% < k=0.5=61.6%。这符合随机剪枝特性——不同 keep_ratio 使用完全独立的随机 mask，无一致退化趋势。与 L2 norm 的有序退化形成对比（待 l2norm 结果确认）。

Cron 不在本 session 中，无法删除。

---
