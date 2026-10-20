# code checkpoint and protect

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_checkpoint-and-protect_20260516T104905_result.json`
- **Structured JSON:** [`d33aa672ae47c64516dd.json`](../../sessions/d3/d33aa672ae47c64516dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **pipeline.py** — 添加了 `save_generation_checkpoint` / `load_generation_checkpoint`，`run_condition()` 循环中生成后保存 checkpoint，重跑时自动恢复
2. **score.py** — `score_diversity_corpus()` 添加了空 response 过滤、embedding 失败 fallback（返回 0.5）、结果映射回原始索引
3. **score.py** — `score_complexity()` 已有 `total == 0` 保护，无需额外修改
4. import 验证通过

---
