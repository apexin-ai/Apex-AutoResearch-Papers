# analysis sft qwen14b s0 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_qwen14b_s0_sweep_20260521T020512_result.json`
- **Structured JSON:** [`e1588a048b40b5cdd775.json`](../../sessions/e1/e1588a048b40b5cdd775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

## sft_qwen14b_s0_sweep 结果

| Dosage | 训练 | Train Loss | MMLU | Δ from d000 |
|--------|------|-----------|------|-------------|
| d000 | ✅ | 0.9095 | 68.84% | — |
| d005 | ✅ | 0.9134 | 68.86% | +0.02pp |
| d025 | ✅ | 0.9261 | 65.05% | -3.79pp |
| d050 | ❌ | — | — | — |
| d100 | ✅ | 0.9695 | 43.85% | -24.99pp |

**d050 崩溃原因**: `RuntimeError: Pin memory thread exited unexpectedly`，在 52%（step 1902/3642）处中断。Adapter 目录为空，无输出。这是已知的同一 bug 模式。

**关键发现**: s0 的 MMLU 崩溃幅度（d100: -24.99pp）远超 s42（-9.37pp），说明 seed 间方差很大，triple-seed CI 确实必要。

**状态**: Registry 已更新为 DONE/negative。报告已注册为 artifact。**d050 需要单独重训。**

---
