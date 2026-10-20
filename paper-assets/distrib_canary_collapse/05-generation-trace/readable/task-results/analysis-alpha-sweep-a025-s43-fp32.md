# analysis alpha sweep a025 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a025_s43_fp32_20260519T114343_result.json`
- **Structured JSON:** [`c7900f21a80ec4aab08c.json`](../../sessions/c7/c7900f21a80ec4aab08c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验 `alpha_sweep_a025_s43_fp32` 尚未完成。**

**当前状态：** Generation 4/10，训练步骤 575/5000，进程 PID 123809 活跃中（18:06 启动，已运行 ~100 分钟）。预计还需 ~80-90 分钟完成（约 21:10 CST）。

**已完成的 gen 0-3 部分 metrics：**

| Metric | gen_0 | gen_1 | gen_2 | gen_3 | 趋势 |
|---|---|---|---|---|---|
| token_entropy | 3.2342 | 2.9792 | 3.0118 | 3.0480 | 先降后回升 |
| ece | 0.0108 | 0.0092 | 0.0118 | 0.0090 | 稳定 |
| perplexity | 26.95 | 19.45 | 20.26 | 20.74 | 初降后缓升 |
| distinct_1 | 0.0983 | 0.0966 | 0.0814 | 0.0746 | **持续下降 ↓** |
| distinct_2 | 0.5146 | 0.5112 | 0.4349 | 0.3835 | **持续下降 ↓** |
| distinct_3 | 0.8140 | 0.8110 | 0.7291 | 0.6545 | **持续下降 ↓** |
| effective_rank | 46.61 | 49.44 | 50.03 | 50.91 | 缓升 |
| mauve | 0.0315 | 0.0313 | 0.0330 | 0.0309 | 稳定 ~0.031 |

**初步观察（gen_0→gen_3）：**
- distinct_1 已从 0.0983 降至 0.0746（**-24.1%**），diversity collapse 趋势明显
- distinct_2/3 同步下降，模式与 bf16 run 一致
- 需等 gen_10 完成才能计算最终 drift_pct 和 lead-lag analysis（PermG/MMCT/TY 需要完整时间序列）

**无法完成的分析项：** 最终 metrics JSON、lead-lag analysis、与 bf16 的完整对比、dose-response map 结论，均需实验运行至 gen_10。

需要我在实验完成后再分析，还是先用 s42_fp32（已完成 gen_0-9）做参考？

---
