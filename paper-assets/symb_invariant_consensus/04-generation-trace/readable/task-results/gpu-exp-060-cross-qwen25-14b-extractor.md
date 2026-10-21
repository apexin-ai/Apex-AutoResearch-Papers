# gpu exp 060 cross qwen25 14b extractor

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-060-cross-qwen25-14b-extractor_20260519T063740_result.json`
- **Structured JSON:** [`f16615945188ba6aa354.json`](../../sessions/f1/f16615945188ba6aa354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## EXP-060 完成

**Qwen2.5-14B 跨模型 FOL 提取实验 (FOLIO-204)**

| 方法 | 正确 | 准确率 | Δ vs Orig |
|------|------|--------|-----------|
| Orig SICA (Mistral self-extraction) | 121/204 | **59.31%** | — |
| Cross SICA (Qwen2.5-14B extractor) | 119/204 | **58.33%** | **-0.98pp** |
| SC@K baseline | 114/204 | **55.88%** | -3.43pp |

- 分歧点: 12/204 (5.9%)
- 结论: **negative** — Qwen2.5-14B 跨模型提取比 Mistral 自提取略差约 1pp，但仍然比 SC baseline 高 2.45pp
- SICA 的 extraction quality 对最终准确率影响较小，绝大多数情况下 (192/204=94%) cross-extraction 与 self-extraction 给出相同答案
- Wall time: 106.1 min, vLLM 已停止，GPU 已释放

---
