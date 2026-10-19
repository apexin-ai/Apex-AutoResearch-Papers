# analysis plan 005 v1v2 diff

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_005_v1v2_diff_20260514T203611_result.json`
- **Structured JSON:** [`586bcb46b6712cefb5e1.json`](../../sessions/58/586bcb46b6712cefb5e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

changelog 已写入 `artifacts/v1_v2_changelog.md`。

**根因**：`mock_predictions()` 第 271 行使用 `hash(strategy)` 构造 RNG seed。Python 3 的字符串 hash 每次进程启动都不同（PEP 456 hash randomization），导致 v1 和 v2 两次运行产生完全不同的 mock rank 序列。

**关键证据**：
- 所有 stratum 样本数（count）完全一致 → 数据、分层逻辑、bin 边界未变
- 所有维度所有策略都有偏移 → 全局性 RNG 漂移，非局部逻辑变更
- v2 新增的 2 个维度（dataflow, neg_difficulty）不影响已有维度的计算

**v2 为 ground truth**：两次都是合成 mock 数据，无"更正确"之分；v2 是最终版脚本（含完整 5 维分析），以 v2 为基准即可。

---
