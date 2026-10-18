# analysis mdd computation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mdd_computation_20260519T070039_result.json`
- **Structured JSON:** [`d071fa0f86a696235d51.json`](../../sessions/d0/d071fa0f86a696235d51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/mdd_computation/mdd_results.md`。

核心结论：**MDD = EDD 在所有 12 个 profile 上成立**。所有 AUC profile 严格单调递减，不存在非单调（U 型）pattern，因此 MDD 相对 EDD 没有额外信息。

具体数据：
- 9-cell atlas (T=0.70)：8/9 cells EDD=MDD=3，唯一例外是 Pythia top-k (d2v3=0.692 < 0.70, EDD=MDD=2)
- 深度扩展：3 个模型均 EDD=MDD=4，d4v5 AUC 收敛到 0.681-0.684 (跨模型 range 仅 0.003)
- 唯一非单调 profile 出现在 atlas 外的 Qwen2.5-1.5B-Instruct (d1v2=0.620 < d2v3=0.664)，但该模型所有 pairs < 0.70，MDD=EDD=0

---
