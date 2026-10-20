# analysis gemini interim metrics v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemini-interim-metrics-v2_20260521T201425_result.json`
- **Structured JSON:** [`f81529d1d8b494fc8229.json`](../../sessions/f8/f81529d1d8b494fc8229.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Gemini 2.5 Pro 95 题 interim metrics：

| Metric | Gemini-2.5-Pro | o3 (ref) | gpt-5.5 (ref) |
|---|---|---|---|
| **SC accuracy** | **0.8737** (83/95) | 0.8265 | 0.8431 |
| **SICA accuracy** | **0.8632** (82/95) | 0.8265 | 0.8480 |
| **Δ(SICA-SC)** | **-1.05pp** | +0.00pp | +0.49pp |
| **Mean BR** | **2.7895** | 1.6565 | 3.4806 |
| **Weighted BR** | **2.5232** | 1.812 | 3.5735 |
| **n_br_finite** | **8** | 6 | 4 |
| **BR=∞** | **5** | 28 | 27 |
| **Process-κ** | **0.7896** | 0.5964 | 0.5625 |
| **Answer-κ** | **0.7532** | 0.9221 | 0.9581 |

要点：
- SC 准确率最高 (87.4%)，但 SICA 比 SC 低 1.05pp（Delta 为负）
- BR=∞ 仅 5 例（远少于 o3 的 28 和 gpt-5.5 的 27），说明 SICA 错误时 gold 答案通常仍有非零权重
- Process-κ 最高 (0.79)，表明 Gemini CoT traces 之间文本相似度高（推理路径更一致）
- Answer-κ 最低 (0.75)，说明 12 次 sampling 的答案分歧比 o3/gpt-5.5 大

结果已保存到 `gemini_interim_95_metrics.json`。

---
