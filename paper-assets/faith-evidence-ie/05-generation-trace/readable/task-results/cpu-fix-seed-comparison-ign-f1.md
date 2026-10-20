# cpu fix seed comparison ign f1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_fix_seed_comparison_ign_f1_20260516T052536_result.json`
- **Structured JSON:** [`9f0d2cea45ca2e2c1cd1.json`](../../sessions/9f/9f0d2cea45ca2e2c1cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

干净。结果汇报：

**方案**：B — 修改 `seed_comparison.py` 的 `load_metrics()`

**改动**（第57-59行）：从 `metrics.json` 读取时，不再无条件 strip `ign_f1`，而是只在 `ign_f1 ≈ f1`（旧 buggy 输出特征）时才 strip。`metrics_v2.json` 路径不受影响。

**dry-run 结果**：
- 4 个已完成的 seed（CED s43/s45, flatNLI s44/s45）全部正确加载，`ign_f1` 均有值且 ≠ f1
- 4 个 re-eval（CED s42/s44, flatNLI s42/s43）尚未完成，显示 NOT FOUND — 它们完成后将只有 `metrics.json`（无 `metrics_v2.json`），修复后的逻辑会正确保留其有效 `ign_f1`

---
