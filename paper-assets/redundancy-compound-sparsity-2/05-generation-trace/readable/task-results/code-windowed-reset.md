# code windowed reset

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_windowed_reset_20260512T093300_result.json`
- **Structured JSON:** [`574fbf8319932cd3d3ab.json`](../../sessions/57/574fbf8319932cd3d3ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。修改摘要：

**新增构造参数**：`enable_reset=False`, `window_size=16`, `tau_reset=0.3`, `n_reset=5`

**核心逻辑**（concat 和 per-head 两种模式均实现）：
- 每个 token 处理后写入 circular buffer（模运算 `ptr = (ptr+1) % W`）
- 跟踪 `low_score_streak`：score 均值 < `tau_reset` 时递增，否则归零
- 当 streak >= `n_reset` 且 buffer 已满时：用 buffer 均值重置 anchor_k/anchor_v，同时重置 Welford variance 统计
- `reset()` 通过 `state.clear()` 自动清理所有新增 state

**Buffer shapes**：
- concat: `(W, batch, dim)`
- per-head: `(W, batch, H, head_dim)`

**向后兼容**：`enable_reset=False` 时无任何额外开销，行为与原实现完全一致。

两处文件（`_project/intermediate/` 和 `artifacts/`）已同步。本地无 PyTorch 无法跑运行时测试，语法和静态结构验证通过。

---
