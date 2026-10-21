# analysis w4 relaxed matching

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w4_relaxed_matching_20260520T105305_result.json`
- **Structured JSON:** [`59ec3e136ea4691c7709.json`](../../sessions/59/59ec3e136ea4691c7709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

## BCS vs F1 相关性对比（N=450 batches, 3 seeds × 6 count levels × 25 batches）

| Match Mode | Pearson r | p-value | Spearman ρ | p-value | Mean F1 |
|---|---|---|---|---|---|
| **Exact text** | 0.0144 | 0.760 | -0.1005 | 0.033 | 0.304 |
| **Relaxed text** (substring) | 0.0032 | 0.946 | -0.1100 | 0.020 | 0.346 |
| **Token overlap** | 0.0038 | 0.936 | -0.1127 | 0.017 | 0.349 |
| **Type-ignored relaxed** | 0.0234 | 0.621 | -0.0974 | 0.039 | 0.425 |

## F1 增益

Relaxed matching 平均提升 F1 +4.2pp（98.4% 的 batch 都有改善），说明 boundary error 确实存在且普遍。但 **BCS 相关性完全没有变化**——从 r=0.014 变成 r=0.003，都在零附近。

## 结论

**假说被证伪。** Boundary error 虽然拉低了绝对 F1，但它们均匀地影响所有 batch，不会选择性掩盖 BCS 信号。NER 中 BCS 与 F1 无关的根本原因不是 exact-match 评估方式，而是其他因素（如 NER 的 type confusion 模式与 embedding similarity 衡量的 schema confusion 存在本质差异）。

结果已保存至：
- 服务器：`/root/schema-dag-extraction/artifacts/w4_relaxed_matching/results.json`（含完整 per-batch 数据）
- 本地：`artifacts/w4_relaxed_matching_results.json`（精简版）

---
