# fix d041 rollback constraint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d041-rollback-constraint_20260515T022107_result.json`
- **Structured JSON:** [`d88bcf41654a9ed65bbb.json`](../../sessions/d8/d88bcf41654a9ed65bbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，验证结果：

| 检查项 | 状态 |
|--------|------|
| `f ∈ R_G` 作为 negative 选择约束 | 已消除（改为 `f \notin R_G(q)`） |
| "structurally connected" 作为 negative 描述 | 已改为 "structurally disconnected"（3个文件共5处） |
| BM25 排序 | 保留不变（无 `sim(E_θ0)` 回退） |
| D041 标记追加 | 3个文件均已追加 `回滚约束方向 2026-05-15` |

注：`introduction_v2.md:23` 中 "structurally connected non-gold rate" 是 Z% 统计指标（描述 connected 文件中 non-gold 的比例），不是 negative 选择方向，无需修改。

---
