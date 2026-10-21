# analyze precompute k5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_precompute-k5_20260513T221027_result.json`
- **Structured JSON:** [`736e1500938e063df5db.json`](../../sessions/73/736e1500938e063df5db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

precompute-k5 分析完成。

**结果：SUCCESS**
- spatial 12,167 + object 14,570 = 总计 26,737 样本，与 K=10 一致
- Cache 总大小 233MB（K=10 为 264MB，88%）
- `k_samples.pt` 约为 K=10 的 50%，符合预期（存 5 vs 10 个候选动作）
- `obs_features.pt` / `expert_actions.pt` 与 K=10 完全相同（不依赖 K）
- 无任何 error/warning，总耗时 ~107min

Registry 已更新为 DONE/success，checkpoint_path 设为 `/root/autodl-tmp/crm_cache_k5/`。分析报告已注册为 artifact。

---
