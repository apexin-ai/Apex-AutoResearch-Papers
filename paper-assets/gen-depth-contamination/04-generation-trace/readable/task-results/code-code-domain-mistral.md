# code code domain mistral

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_code_domain_mistral_20260524T091917_result.json`
- **Structured JSON:** [`26cf343579fbb484682b.json`](../../sessions/26/26cf343579fbb484682b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完整完成，无需重新运行。结果摘要：

**Mistral-7B Code (Python) — K\* = 2**

| Pair | AUC | 判断 |
|------|-----|------|
| 0 vs 1 | 0.9191 ± 0.0017 | 可区分 |
| 1 vs 2 | 0.6152 ± 0.0120 | 可区分 |
| 2 vs 3 | 0.5293 ± 0.0091 | ~随机 |
| 3 vs 4 | 0.5286 ± 0.0104 | ~随机 |
| 4 vs 5 | 0.5099 ± 0.0060 | ~随机 |

- Seed data 与 Qwen-1.5B Code 实验完全一致（同 `code_py_*` doc_ids）
- Features 用 Qwen2.5-1.5B-Instruct cross-scoring（15D features）
- K\* = 2 确认 Code domain ceiling = 2，与 Qwen-1.5B (K\*=2) 和 LLaMA-8B (K\*=2) 一致
- 数据和结果已在 `data/exp_code_mistral7b/` 和 `results/exp_code_mistral7b/`

---
