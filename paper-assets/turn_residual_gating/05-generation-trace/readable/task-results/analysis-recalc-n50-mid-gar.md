# analysis recalc n50 mid gar

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recalc_n50_mid_gar_20260520T195705_result.json`
- **Structured JSON:** [`f7f4b69fbb26ef998ba7.json`](../../sessions/f7/f7f4b69fbb26ef998ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据表：

### Corrected N=50 Gen Steering Results

| β | GAR mean (corrected) | GAR std | PPL mean | PPL std | N_valid | GAR mean (old/buggy) | N=5 GAR ref |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | **0.0641** | 0.0809 | 1.4324 | 0.1029 | 39 | 0.1011 | 0.028 |
| 2.0 | **0.1280** | 0.1101 | 1.4822 | 0.1385 | 39 | 0.2068 | 0.062 |
| 3.0 | **0.5558** | 0.0601 | 1.5605 | 0.1719 | 39 | 0.6662 | 0.441 |
| 4.0 | **0.6439** | 0.0607 | 1.6674 | 0.2241 | 39 | 0.7579 | 0.598 |
| 5.0 | **0.7271** | 0.0605 | 1.7723 | 0.2693 | 38 | 0.8315 | 0.680 |
| 10.0 | **0.9612** | 0.0152 | 3.4517 | 1.7813 | 39 | 0.9806 | 0.959 |

### Per-conversation mid_gar 分布

| β | n | mean | std | min | max | median |
|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 39 | 0.0641 | 0.0809 | 0.0070 | 0.3620 | 0.0307 |
| 2.0 | 39 | 0.1280 | 0.1101 | 0.0320 | 0.5373 | 0.0872 |
| 3.0 | 39 | 0.5558 | 0.0601 | 0.4333 | 0.7113 | 0.5516 |
| 4.0 | 39 | 0.6439 | 0.0607 | 0.5465 | 0.7919 | 0.6500 |
| 5.0 | 38 | 0.7271 | 0.0605 | 0.6033 | 0.8616 | 0.7254 |
| 10.0 | 39 | 0.9612 | 0.0152 | 0.9323 | 0.9870 | 0.9611 |

### 结论

修正后 baseline GAR (β=0) 从 0.101 降到 **0.064**，更接近 N=5 的 0.028，但仍高出约 2.3x。这符合预期——N=50 生成更多 turns，中间 turns 的 GAR 方差更大（std=0.081，median 仅 0.031 与 N=5 接近），被少数高 GAR 对话拉高了均值。

高 β 端，修正后 β=10.0 的 0.961 与 N=5 的 0.959 高度一致（delta=0.002），确认 steering 效果在大 N 下稳定。所有 β 的修正值都比旧值低 0.02-0.11，旧逻辑的 min_turns 截断 bug 确实系统性地高估了 mid_gar。

---
