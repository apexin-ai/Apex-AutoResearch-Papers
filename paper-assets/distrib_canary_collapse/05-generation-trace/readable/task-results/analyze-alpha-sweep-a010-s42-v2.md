# analyze alpha sweep a010 s42 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_alpha_sweep_a010_s42_v2_20260518T193614_result.json`
- **Structured JSON:** [`96d142437df48e1ea277.json`](../../sessions/96/96d142437df48e1ea277.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入并注册。核心发现：

**α=0.10 揭示了 canary 与 collapse 的关键脱钩：**

| 维度 | α=0.00 (null) | α=0.10 | α=0.25 | α=0.50+ |
|------|-------------|--------|--------|---------|
| token_entropy gen10 | 3.069 | 3.064 | 3.072 | 2.63↓ |
| distinct_1 Δ% | -13.8% | **-39.7%** | -40.5% | - |
| PermG (diff.) | 0 sig | 0 sig | 0 sig | boundary+ |

1. **Diversity collapse 在 α=0.10 已饱和**：distinct_1 下降 39.7%，与 α=0.25 的 40% 几乎一致，远超 null 的 13.8%。
2. **Entropy canary 完全无感**：gen10 entropy 与 null 仅差 0.17%，PermG 0/16 显著。
3. **检测阈值在 α=0.25 到 α=0.50 之间**：canary 只在损害已经严重时才响应。

结论定性为 **informative negative**：实验成功填补了 regime map 中 α=0.00 到 α=0.25 的空白，发现 diversity collapse 非线性饱和效应。

---
