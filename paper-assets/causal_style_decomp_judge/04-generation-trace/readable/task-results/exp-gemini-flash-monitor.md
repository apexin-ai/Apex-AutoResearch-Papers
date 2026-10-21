# exp gemini flash monitor

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemini_flash_monitor_20260521T221922_result.json`
- **Structured JSON:** [`067835adab0004c6554c.json`](../../sessions/06/067835adab0004c6554c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gemini Flash 实验完成，registry 已更新为 DONE/success。

## 结果汇总

| 指标 | Formality (88 pairs) | Verbosity (86 pairs) |
|------|---------------------|---------------------|
| **BT win%** | 57.4% [50.0, 64.8] | 70.8% [63.5, 77.8] |
| **BT p-value** | 0.0448 ✓ | <0.0001 ✓ |
| **Likert ATE** | -0.239 | 0.151 |
| **Likert p-value** | 0.1953 (NS) | 0.4821 (NS) |
| **GEE Style OR** | 1.64 [0.91, 2.98] | 9.16 [3.75, 22.38] |
| **GEE Orig OR** | 2.51 [1.39, 4.54] | 0.45 [0.20, 1.02] |
| **Blindspot** | **YES** | **YES** |

两个轴均检出 Blindspot（BT 显著但 Likert 不显著），与 GPT-4o、Qwen-32B、Llama-70B、Claude 的结果一致，进一步确认 style blindspot 是 judge-universal 现象。

Verbosity 的 GEE Style OR=9.16 尤其突出，说明 Gemini Flash 在 pairwise 中对 verbose 回复的偏好极强，但在 Likert 打分中完全无法体现。

---
