# analysis bootstrap block check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_block_check_20260517T191334_result.json`
- **Structured JSON:** [`b66e3054a47befde7026.json`](../../sessions/b6/b66e3054a47befde7026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键代码已找到。让我确认核心逻辑：

**Bootstrap resample 单位：task-level（per-task RSA values）**

具体证据（`/root/vla-ssd/scripts/rsa_definitive.py`）：

1. **Line 155-166**: `compute_task_rsa()` — 对每个 task 内所有 demo pairs 计算一个单一的 Spearman ρ（RSA 值）。pairing 是 within-task demo combinations。

2. **Line 237-255**: `compute_single_model()` — 对 10 个 tasks 各得到一个 RSA 值，存入 `rsa_values` 列表（长度 = task 数，最多 10）。

3. **Line 203-207**: `bootstrap_ci(values)` — bootstrap 的输入是 `rsa_values`（per-task RSA 值数组）。resample 操作是：
   ```python
   means = [np.mean(rng.choice(values, size=n, replace=True)) for _ in range(n_boot)]
   ```
   即从 10 个 task-level RSA 值中 resample with replacement。

**结论：已正确处理。**

Bootstrap resample 单位是 **task**（每个 task 产生一个 RSA 值，bootstrap 在这 10 个 task-level 值上 resample）。这比 demo-level block bootstrap 更保守。Within-task 的 temporal autocorrelation 完全不影响 CI，因为：
- 每个 task 内部先将所有 demo pairs 聚合为单个 Spearman ρ
- Bootstrap 只在 task 之间 resample，不触及 timestep 或 demo 内部结构

---
