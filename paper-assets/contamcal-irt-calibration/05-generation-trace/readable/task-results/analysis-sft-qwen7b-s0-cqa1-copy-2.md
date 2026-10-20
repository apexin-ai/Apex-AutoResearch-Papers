# analysis sft qwen7b s0 cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_qwen7b_s0_cqa1_20260520T224342_result.json`
- **Structured JSON:** [`6682380d47fd384cc5db.json`](../../sessions/66/6682380d47fd384cc5db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练验证完成。

**结论：SUCCESS** — 5 个 dosage (d000-d100) 全部正常完成，checkpoint 完整。

| Dosage | Train Loss | Token Acc | Runtime |
|--------|-----------|-----------|---------|
| d000   | 0.926     | 0.789     | 3.7h    |
| d005   | 0.930     | 0.777     | 3.9h    |
| d025   | 0.943     | 0.771     | 3.9h    |
| d050   | 0.960     | 0.778     | 4.1h    |
| d100   | 0.988     | 0.761     | 4.3h    |

Loss 随 dosage 单调递增，符合预期。lora_alpha=32 确认。Registry 已更新为 DONE/success，分析报告已注册。

下一步：对 5 个 checkpoint 跑 eval，与 s42/s123 结果对比构建 triple-seed bootstrap CI。

---
