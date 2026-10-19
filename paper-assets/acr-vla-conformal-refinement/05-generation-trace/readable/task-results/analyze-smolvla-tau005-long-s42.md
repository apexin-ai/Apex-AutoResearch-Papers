# analyze smolvla tau005 long s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_smolvla-tau005-long-s42_20260528T011421_result.json`
- **Structured JSON:** [`afeee9c4effa5dda77dd.json`](../../sessions/af/afeee9c4effa5dda77dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `smolvla-tau005-long-s42` 分析完成，registry 已更新为 DONE (negative)。

**结果总结**：
- **success_rate**: 44% （低于 Long baseline ~48-50%）
- **trigger_rate**: 97.8% （符合预期，τ=0.05 几乎 always-on）
- **mean_uncertainty**: 0.1299
- 日志无 OOM/CUDA error，EXIT_CODE=0

τ=0.05 时 CRM 几乎每步都触发修正（97.8%），但过度干预反而降低了性能（44% < baseline 48-50%），说明 always-on 修正在 Long suite 上有害。这与τ-sweep 曲线预期一致：过低阈值导致过度修正。

---
