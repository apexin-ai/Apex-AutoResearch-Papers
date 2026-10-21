# code fix analyze results d002

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-analyze-results-d002_20260515T121152_result.json`
- **Structured JSON:** [`9d28ea13697c05d2a224.json`](../../sessions/9d/9d28ea13697c05d2a224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。变更摘要：

**新增** `extract_per_task_mean_rho(data)` — 从每层的 `per_task_rho` 字段计算 mean ρ

**`compute_judgment` 三处改动**：
1. **ρ > 0.5 下限**：改用 per-task mean ρ（无 per_task_rho 时 fallback 到 pooled）
2. **VLA ≥ DINO gate**：从 pooled max (0.833) 改为 per-task mean max (0.554)
3. **Δρ bootstrap**：已确认原本就是 task-level bootstrap，无需修改

**输出保留 pooled ρ**：`best_pooled_rho` 字段仍在 criteria 和 summary 中，仅用于参考。

---
