# ops 008f fresh metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_008f_fresh_metrics_20260514T071350_result.json`
- **Structured JSON:** [`b38cb2fd9564d0c279aa.json`](../../sessions/b3/b38cb2fd9564d0c279aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**exp_008f @55K: STABLE — Dream collapse prediction NOT confirmed**

| Step | eval_return | norm. v/e | status |
|------|-------------|-----------|--------|
| 25K  | 196.78      | 1.02x     | OK (noise) |
| 35K  | 206.67      | **0.73x** | ✓ healthy |
| 45K  | 194.08      | **0.83x** | ✓ stable |
| 55K  | 173.45      | **0.97x** | ✓ stable (<1.0x) |

**因果论证加强**：没有 dt_embedding 条件输入的 008f 在 45K-55K 区间 normalized v/e 始终 <1.0x，而有 dt_embedding 的 008d 在同区间已经 collapse（v/e 69.3%+）。这强烈支持 dt_embedding 是 delusional critic 的直接原因。

**需关注**：eval_return 从 35K 峰值 206.67 下滑到 55K 的 173.45（−16%），且 normalized v/e 以 ~+0.12x/10K 速率上升。按此趋势 65K 可能触及 1.0x。建议在 65K checkpoint 再次检查。

---
