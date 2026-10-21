# analysis sft gemma2 s0 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_gemma2_s0_sweep_20260520T220102_result.json`
- **Structured JSON:** [`8d9a452e4ad011a41231.json`](../../sessions/8d/8d9a452e4ad011a41231.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

| Dosage | MMLU Acc | Δ from d000 |
|--------|----------|-------------|
| d000 | 0.6488 | — |
| d005 | 0.6414 | -0.74pp |
| d025 | 0.6491 | +0.03pp |
| d050 | 0.6309 | -1.79pp |
| d100 | **MISSING** | — |

**关键问题**: d100 训练在 step 1618/4159 (39%) 崩溃，错误为 `RuntimeError: Pin memory thread exited unexpectedly`。lora_adapter 目录为空，eval 被跳过。delta_d100 无法计算。

**跨 seed 对比**: s42 delta_d100=+3.76pp, s123 delta_d100=+1.49pp, s0 无法判断。

**下一步**: 需单独重跑 d100 seed=0 训练 + eval。d000-d050 的 checkpoint 和 eval 结果均完好，无需重跑。

---
