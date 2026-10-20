# ops taxei rp progress check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_taxei-rp-progress-check_20260516T032657_result.json`
- **Structured JSON:** [`2204d4948f5d9d7285dc.json`](../../sessions/22/2204d4948f5d9d7285dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## TaxEI-RP 4-seed 训练状态

所有 4 个训练正常运行，进程存活 ~1h10m。

| Seed | GPU | Step | 进度 | Loss | Token Acc | 显存 | GPU利用率 |
|------|-----|------|------|------|-----------|------|-----------|
| s42 | cuda:0 | **1671**/5415 | **30.9%** | 0.449 | 0.851 | 29.7/32.6 GiB | 99% |
| s0 | cuda:1 | **1636**/5415 | **30.2%** | 0.474 | 0.847 | 30.7/32.6 GiB | 99% |
| s123 | cuda:2 | **1671**/5415 | **30.9%** | 0.461 | 0.846 | 30.9/32.6 GiB | 93% |
| s1 | cuda:3 | **1634**/5415 | **30.2%** | 0.472 | 0.840 | 30.4/32.6 GiB | 99% |

**预估剩余时间**（基于 ~2.5 s/step）：

| Seed | 已用时间 | 剩余步数 | 预计剩余 | 预计完成 |
|------|---------|---------|---------|---------|
| s42 | 1h10m | 3744 | **~2h 37m** | ~14:04 |
| s0 | 1h10m | 3779 | **~2h 41m** | ~14:08 |
| s123 | 1h10m | 3744 | **~2h 36m** | ~14:03 |
| s1 | 1h08m | 3781 | **~2h 38m** | ~14:05 |

**训练趋势**：4 个 seed 的 loss 在 step 1260→1540 区间稳定在 0.44-0.55 之间，token accuracy 稳定在 0.83-0.86，收敛正常。所有 GPU 温度 65-75°C，功耗接近满载（558-571W/575W），状态健康。

---
