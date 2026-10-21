# analysis cliff curve data aggregation

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cliff_curve_data_aggregation_20260527T102205_result.json`
- **Structured JSON:** [`13afdaf7126759516b52.json`](../../sessions/13/13afdaf7126759516b52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/cliff_curve_data.md` 并注册。

汇总：
- **58/72** 数据点有值，**12 个 RUNNING**，**9 个完全缺失**
- **OpenVLA Object**: 13/18 done，缺 L2norm k=0.75、Attn k=0.50、Random k=0.85/0.50
- **OpenVLA Goal**: 16/18 done，最完整，仅缺 Attn k=0.70 和 Random k=0.95
- **OpenVLA Long**: 11/18 done，最稀疏——k=0.95 全行在跑（westd-38929），k=0.50 行缺 L2norm 和 Random
- **π0.5 Long strict**: 全部 18 格有值但仅 5 个确认 strict，6 个 strict 重跑正在进行，7 个仍用近似值（postfix/non-tag，误差 ~1-3pp）

---
