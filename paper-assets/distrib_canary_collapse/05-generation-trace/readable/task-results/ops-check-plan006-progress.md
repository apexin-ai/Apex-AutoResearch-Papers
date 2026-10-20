# ops check plan006 progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-plan006-progress_20260515T020720_result.json`
- **Structured JSON:** [`e5253ce6799b34e0e006.json`](../../sessions/e5/e5253ce6799b34e0e006.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_006_s42 进度

**进度**: 5/20 gen 完成 (gen_0–gen_4)，当前正在执行 gen_5（生成阶段）

### Metrics 表格

| gen | entropy | ece | perplexity | distinct_1 | distinct_2 |
|----:|--------:|----:|-----------:|-----------:|-----------:|
| 0 | 3.2342 | 0.0108 | 26.95 | 0.0982 | 0.5178 |
| 1 | 1.5253 | 0.3268 | 185.68 | 0.0975 | 0.5141 |
| 2 | 1.2962 | 0.3781 | 380.41 | 0.0846 | 0.4390 |
| 3 | 1.2141 | 0.3986 | 568.76 | 0.0798 | 0.4025 |
| 4 | 1.2192 | 0.4093 | 734.41 | 0.0782 | 0.3890 |

### Collapse 趋势分析

**Entropy**: gen_0→1 暴跌 52.8%（3.23→1.53），之后持续下降但速率放缓，gen_3→4 基本稳定（1.214→1.219），可能接近下界。

**ECE (calibration)**: gen_0→1 跳涨 30×（0.011→0.327），之后缓慢恶化（gen_4 = 0.409）。校准崩溃在第一代就已基本完成。

**Perplexity**: 持续指数级上升——26.9 → 185.7 → 380.4 → 568.8 → 734.4。每代增幅在收窄（6.9x → 2.0x → 1.5x → 1.3x），但绝对值仍在快速攀升。

**Diversity (distinct_1/2)**: 稳定下降。distinct_1 从 0.098 降至 0.078（-20%），distinct_2 从 0.518 降至 0.389（-25%）。下降近似线性，未见加速。

**结论**: canary collapse 在 gen_0→1 就剧烈触发（entropy/ECE/ppl），后续是持续恶化但速率递减。diversity 下降相对温和且线性。当前没有"加速崩溃"迹象，更像是渐进式退化。

### 时间估算

- gen_0→gen_4: 6846 秒，约 **28.5 分钟/gen**
- gen_0 完成: ~May 14 23:57 UTC，gen_4 完成: ~May 15 01:50 UTC
- 剩余 15 gen × 28.5 min ≈ **7.1 小时**
- **预估完成: May 15 ~09:00 UTC**

---
