# monitor exp 002 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp-002-signals_20260514T123003_result.json`
- **Structured JSON:** [`64924191e515eec84cec.json`](../../sessions/64/64924191e515eec84cec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 Signal Computation 状态报告

**当前任务：1/9** — `Qwen2.5-0.5B_d000_s42/mmlu`

**Signal 完成情况（d000/mmlu）：**
- embedding: ✅ (18:50)
- minkpp: ✅ (18:55)
- selfcritique: ⏳ 运行中（已 ~95 min）

**其他已有文件（前次残留）：**
- d000: embedding_gsm8k ✅, embedding_arc_challenge ✅
- d005: embedding_mmlu ✅
- d100: 空

**BATCH_SIZE=32 热修复状态：** 代码已生效（`signal_selfcritique.py` 第 34 行 `BATCH_SIZE = 32`）。但 selfcritique 仍然慢——因为 MMLU 有 ~14K items，每个 item 需要 **生成** 最多 256 tokens 再做 critique forward pass。batch=32 只并行化 forward pass，不减少总 token 数。GPU 0 利用率 34%/2.2GB，说明受 generation 瓶颈限制。

**ETA 估算：**
- 当前 task 剩余：~0-20 min（selfcritique_mmlu 可能接近完成）
- 剩余 8 tasks 中，2 个 mmlu 任务各需 ~100 min（selfcritique 瓶颈），6 个小 benchmark 任务各 ~20 min
- **总剩余：~5-6 小时**

**关键问题：** selfcritique "~60min→~5min" 的预期不准确。瓶颈是 autoregressive generation（14K items × 256 tokens），batch 只帮了 forward pass 部分。要真正加速需要减少 `max_answer_tokens` 或跳过 answer generation（直接用 benchmark 的 ground truth answer 做 critique）。

---
