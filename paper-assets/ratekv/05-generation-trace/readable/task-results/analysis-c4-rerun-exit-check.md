# analysis c4 rerun exit check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_rerun_exit_check_20260514T110638_result.json`
- **Structured JSON:** [`d0d38cc863ad3d457a36.json`](../../sessions/d0/d0d38cc863ad3d457a36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总如下：

---

## c4_rerun_d032 实验结果

**进程状态**: PID 210299 已退出（EXITED），无 error/traceback

**Conclusion**: **success**（Qwen2.5-7B plan_007 + plan_010 全部完成）

**注意**: 实际只跑了 **Qwen2.5-7B**，未包含 Llama-3.1-8B 和 Mistral-7B-v0.3。

### Qwen2.5-7B 关键 Metrics

**Plan 007 — C4 calibration → WT2 eval**:

| 指标 | 值 |
|---|---|
| Cal samples | 18 (from 100 C4 entries) |
| Cal baseline PPL | 12.6505 |
| bf16 WT2 PPL | 9.8106 |
| **C4-MCKP WT2 PPL** | **11.2942** |
| Uniform 4-bit WT2 PPL | 15.4454 |
| Delta (uniform - MCKP) | +4.1512 |
| Bit distribution | {8bit: 4, 4bit: 100, 2bit: 8} |
| Agreement w/ WT2-cal | **96.4%** (108/112) |
| Old contaminated PPL | 11.3285 (agree 98.2%) |

**Plan 010 — Cross-domain robustness**:

| 指标 | A (C4→WT2) | B (WT2→C4) |
|---|---|---|
| bf16 PPL | 9.8106 | 15.3246 |
| MCKP PPL | 11.2942 | 20.5601 |
| Uniform 4-bit PPL | 15.4454 | 35.4232 |
| A↔B agreement | **96.4%** (108/112) | — |

**核心发现**: 真实 C4 数据重跑 PPL=11.2942 vs 旧污染数据 PPL=11.3285，差异仅 0.03，说明之前的 C4 数据污染对 Qwen 结果影响极小。跨域 agreement 96.4% 表明分配方案对 calibration 数据源鲁棒。

---
