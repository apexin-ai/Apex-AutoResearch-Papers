# analyze eval xvla l2norm k05 spatial seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v3_20260523T200627_result.json`
- **Structured JSON:** [`74b463de8a9a189c4ad6.json`](../../sessions/74/74b463de8a9a189c4ad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析摘要：

## X-VLA L2norm k=0.5 Spatial 结果

**Overall SR: 58.8%** (294/500), 95% CI [54.4%, 63.0%]

### 对比

| Method | Spatial SR | vs Random Δ |
|--------|-----------|-------------|
| **L2norm k=0.5** | **58.8%** | **-12.6pp** |
| Random k=0.5 | 71.4% | — |
| Attention k=0.5 | ≥92.8% | +21.4pp |
| Baseline (full) | ~90%+ | — |

### 跨套件 L2norm 一致性

| Suite | L2norm | Random | Δ |
|-------|--------|--------|---|
| Object | 43.4% | 70.6% | -27.2pp |
| Long | 45.0% | 61.6% | -16.6pp |
| **Spatial** | **58.8%** | **71.4%** | **-12.6pp** |

三个套件 L2norm 全部低于 Random，确认 **L2 在 X-VLA BART connector 上全面不可靠**。

### Per-task variance

极端分化：Task 0=92%, Task 5=0%, 标准差约 30pp。L2 不仅整体差，且 task 间 variance 极高——说明 L2 norm 在 BART connector 中不能区分 informative vs uninformative tokens，导致部分 task 恰好保留了关键 token（高 SR）而另一些恰好丢弃（接近 0%）。

### 叙事确认

Spatial 数据完成了第三个独立证据点：L2 在 entangling connector（BART）上**全面反信息性**（三套件均劣于 random），而 attention scoring 全面有效（三套件均 ≥92%）。核心叙事 "architecture-dependent validity of importance scoring" 得到强化。

---
