# code c5b pilot impl v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c5b_pilot_impl_v2_20260514T150043_result.json`
- **Structured JSON:** [`e6a945a5f44f01866f20.json`](../../sessions/e6/e6a945a5f44f01866f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

**修复 3 处与设计文档的偏差：**

1. **`compute_phase_aware_sparsity` cap 逻辑** — 原代码将 surplus 分配到 s_reas，改为设计文档的 rescale 方案：`δ_effective = (0.50 - s) × (n_trans / n_exec)`，`s_exec = s - δ_effective`，`s_reas = s` 不变。

2. **`eval_condition` head/KV 分离** — 新增 `head_sparsity` 参数，head pruning 全程使用 uniform `target_s`，仅 KV eviction 使用 phase-aware sparsity。

3. **`n_trans=0` 边界** — 原代码 s_exec 仍减 δ 但无 transition tokens 补偿导致 compute-match 失败，改为直接 fallback to uniform。

**Dry-run 结果：** 6 项测试全部通过（no-cap / cap / s=0.30 cap / n_trans=0 / n_total=0 / marginal cap），compute-match 精确验证。Registry 已更新。

---
