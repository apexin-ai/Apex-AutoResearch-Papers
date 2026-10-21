# analysis action divergence rate

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action-divergence-rate_20260513T171027_result.json`
- **Structured JSON:** [`370d02a6e9428c0b8829.json`](../../sessions/37/370d02a6e9428c0b8829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键结果：

## Action Divergence Analysis

| Task | Steps | Divergence Rate |
|------|-------|----------------|
| boil | 548 | **77.2%** |
| change-the-state-of-matter-of | 600 | **73.0%** |
| chemistry-mix-paint | 600 | **73.5%** |
| grow-plant | 600 | **72.7%** |
| melt | 600 | **69.3%** |
| **Overall** | **2948** | **73.1%** |

Phase 分布基本均匀（66%–80%），没有明显的 early/late 趋势。

## GPU 成本估算

73.1% divergence rate 意味着 9000 步中有 **6576 个 fork 点**，每个 fork 续跑 20 步：

- 基础 episode 采集：10.0h
- Fork continuations：146.1h
- **双卡并行总时长：78.1h**
- **预估费用：¥403**（2×A6000）

73% 的 divergence rate 远高于预期——几乎每步都要 fork。这意味着 episode-terminal labeling 的 GPU 开销约是基础采集的 **15.6 倍**。可能需要考虑降低 K 值或引入 fork 采样策略来控制成本。

---
