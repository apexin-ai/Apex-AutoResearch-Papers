# computation entropy breakdown crossmodel

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_entropy-breakdown-crossmodel_20260519T055418_result.json`
- **Structured JSON:** [`2cabc33b8f073200e8cb.json`](../../sessions/2c/2cabc33b8f073200e8cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。合并结果表：

| Exp | Model | Dataset | Group | n | SC% | SICA% | Δpp |
|-----|-------|---------|-------|--:|----:|------:|----:|
| **exp033** | Mistral-7B | FOLIO (s42) | high_entropy | 78 | 35.9 | 48.7 | **+12.8** |
| | | | low_entropy | 126 | 65.9 | 65.9 | +0.0 |
| **exp052** | Mistral-7B | FOLIO (s123) | high_entropy | 77 | 37.7 | 46.8 | **+9.1** |
| | | | low_entropy | 127 | 63.8 | 63.8 | +0.0 |
| **exp053** | Mistral-7B | FOLIO (s456) | high_entropy | 75 | 41.3 | 40.0 | -1.3 |
| | | | low_entropy | 129 | 65.1 | 65.1 | +0.0 |
| **exp046** | Mistral-7B | PW-600 | high_entropy | 267 | 33.7 | 28.8 | -4.9 |
| | | | low_entropy | 333 | 43.8 | 42.6 | -1.2 |
| **exp036** | Qwen2.5-14B | FOLIO | high_entropy | 37 | 56.8 | 48.6 | -8.2 |
| | | | low_entropy | 167 | 82.0 | 81.4 | -0.6 |
| **exp038** | Qwen2.5-14B | LogiQA | high_entropy | 23 | 65.2 | 60.9 | -4.3 |
| | | | low_entropy | 177 | 80.2 | 80.2 | +0.0 |
| **exp035** | Qwen2.5-7B | FOLIO | high_entropy | 47 | 55.3 | 53.2 | -2.1 |
| | | | low_entropy | 157 | 83.4 | 83.4 | +0.0 |
| **exp048** | LLaMA-8B | PW-600 (partial) | high_entropy | 76 | 61.8 | 57.9 | -3.9 |
| | | | low_entropy | 104 | 77.9 | 76.0 | -1.9 |

**关键发现**：
- SICA 的 high-entropy 优势**仅在 Mistral-7B + FOLIO 的 2/3 seed 上成立**（s42: +12.8pp, s123: +9.1pp），s456 已不显著 (-1.3pp)
- 所有其他模型/数据集组合中，SICA 在 high-entropy 组**均为负** (-2.1 到 -8.2pp)
- low-entropy 组几乎全部 Δ≈0，符合预期（高一致性时 SICA 无额外信息）
- LLaMA-8B FOLIO (exp020/034) 缺失结果 JSON，exp048 (PW-600) 仅有 180/600 条

JSON 已保存并注册为 `art_20260519_3bbd83`。

---
