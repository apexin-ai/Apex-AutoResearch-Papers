# code reviewer fixes

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reviewer-fixes_20260516T075032_result.json`
- **Structured JSON:** [`2482c5232a1324fcab5d.json`](../../sessions/24/2482c5232a1324fcab5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部导入成功，验证通过。

---

### 修改总结

| 文件 | 修复 | 具体变更 |
|------|------|----------|
| **train_sft.py** | W1 | `_build_dataset()`: 先单独 tokenize prompt（含 `add_generation_prompt=True`）得到 `prompt_len`，labels 中前 `prompt_len` 个 token 设为 `-100`，只在 response tokens 上算 loss |
| **score.py** | W2 | 删除原 `score_diversity()`，新增 `score_diversity_corpus(all_responses, device, k_neighbors=5)`：对全部 N×K 个 response 计算 sentence embeddings，用 sklearn `NearestNeighbors(metric='cosine')` 找 k=5 最近邻，diversity_score = 平均 cosine distance。`score_all()` 中先 flatten 所有 responses，调用 corpus-level 函数后 reshape 为 (N, K) |
| **evaluate.py** | I1 | `compute_mean_nn_distance()` 改为 k=5 corpus-level NN distance（用 sklearn `NearestNeighbors`），与 score.py 逻辑一致 |

---
