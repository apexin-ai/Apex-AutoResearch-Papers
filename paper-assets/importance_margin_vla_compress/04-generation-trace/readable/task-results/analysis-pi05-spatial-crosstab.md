# analysis pi05 spatial crosstab

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05_spatial_crosstab_20260521T205726_result.json`
- **Structured JSON:** [`1a92839aa93a70557405.json`](../../sessions/1a/1a92839aa93a70557405.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 memory.md。以下是分析结论：

## π0.5 跨 suite 对比总结

**已完成数据点**: Object 24 个实验（19 个有效 metrics），Spatial 2 个（baseline + random k=0.5）

### Cross-suite 一致性
- **Random k=0.5**: Object **68.9%** vs Spatial **71.6%** — delta 仅 **2.7pp**，高度一致。π0.5 的 vision token 冗余结构不依赖于 task 类型。

### 关键差异/异常
1. **L2norm V-shape 非单调**（Object）：k=0.5 是谷底(33.5%)，k=0.3 反弹到 53.2%——L2 norm 对 CV=0.055 的均匀分布模型几乎无区分力
2. **Random k=0.9 崩塌至 ~10.8%**（双 seed 确认）——仅移除 10% random token 即摧毁模型，而 L2norm k=0.9 正常(98.2%)。说明存在少量关键 token，random 删除几乎必然命中
3. **k=0.5-0.7 区间 Random >> L2norm**：random 靠"保留多样性"优于 L2norm 的"盲选"

### 待补充
Spatial suite 的 L2norm k=0.3/k=0.5（运行中）和 Random k=0.3/k=0.7（已提交）完成后可做完整 cross-suite 对比。

---
