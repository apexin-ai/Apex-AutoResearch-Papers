# code subsample patch

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_subsample-patch_20260513T040708_result.json`
- **Structured JSON:** [`c19ef8a9b8f83e1819f6.json`](../../sessions/c1/c19ef8a9b8f83e1819f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

补丁已写入 `artifacts/code/subsample_curriculum_patch.py`。

核心变更：

1. **`subsample_variable_dt`** — 新增 `effective_max_dt` 参数（默认 `None`，向后兼容）。当 `effective_max_dt <= 1` 时直接返回原始数据 + 全 1 的 `dt_labels`，等价于不子采样；否则用 `effective_max_dt` 替代 `max_dt` 作为 log-uniform 采样上界。

2. **`WorldModel._train`** — 在调用 `subsample_variable_dt` 前先计算 `gate_scale`（复用已有的 phase1/phase2 curriculum 逻辑），然后传入 `effective_max_dt = 1 + gate_scale * (K - 1)`。Phase 1 时 `effective_max_dt=1`，RSSM 训练数据与 imagination 的 dt=1 完全一致。

部署位置：
- `tools.py` 第 763 行起，整个 `subsample_variable_dt` 函数替换
- `models.py` 第 169-173 行，子采样调用块替换

---
