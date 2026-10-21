# data registry nve step matched fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_registry_nve_step_matched_fix_20260524T085146_result.json`
- **Structured JSON:** [`f7d4c9f7aee01852e278.json`](../../sessions/f7/f7d4c9f7aee01852e278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部更新成功。也清除了 `nve_sustained_window` 的 backfill_error（整个 metrics 已替换）。

### NVE 修正结果

| 实验 | NVE peak | 分类 | 来源 |
|------|----------|------|------|
| `exp_009e_008d_walker_s1` (s1) | **2.09×** | onset_collapse | 论文 step-matched baseline |
| `exp_009b_008d_walker_s2` (s2) | **1.62×** | onset_self_correcting | 论文 step-matched baseline |
| `exp_008d_civo_trigger_s4` (s4) | **1.53×** | onset_collapse | 论文 step-matched baseline |

所有三个实验的 `backfill_error` 标记已清除，NVE 值已写入 registry。

---
