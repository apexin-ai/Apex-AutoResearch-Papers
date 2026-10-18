# code verify evaluate compat

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-evaluate-compat_20260515T132440_result.json`
- **Structured JSON:** [`6bb592afb39864ce87f4.json`](../../sessions/6b/6bb592afb39864ce87f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 兼容性检查结果

所有 5 个文件均与 14D action / 1-camera 配置**完全兼容**，无需修改。

### 逐文件分析

| 文件 | 状态 | 说明 |
|------|------|------|
| `evaluate.py` | **OK** | 无硬编码维度 |
| `imm/metrics.py` | **OK** | 纯 `(B, N)` 操作 |
| `imm/acis.py` | **OK** | 维度由构造函数参数决定 |
| `imm/token_selection.py` | **OK** | 动态获取 `B, N, D` |
| `imm/losses.py` | **OK** | 纯 `(B, N)` + 标量操作 |

### 关键检查点

1. **`compute_importance_scores()`** — 直接委托给 `model.compute_importance_scores(batch)`，无 token 数量或 action 维度假设。

2. **`estimate_lipschitz()`** — 所有形状动态获取：`B = actions.shape[0]`，`sample_noise(actions.shape, ...)`，`time[:, None, None]` 广播兼容任意 action 维度。`prepare_images(batch)` 和 `_get_visual_tokens(images)` 由 wrapper 处理 1-camera 逻辑。

3. **`perturb_images()`** — 遍历 batch 所有 key，用 `"image" in key.lower()` 自动发现图像键。1-camera 只会匹配到 1 个 image key，逻辑正确。

4. **所有 metrics 函数** — 操作对象是 `(B, N)` importance scores，其中 N 是 visual token 数量（由模型决定，非硬编码）。margin、preservation rate、Kendall tau、certified bound 全部自适应。

5. **ACIS** — `visual_dim=960, action_dim=720` 只是默认值，实际由 config 传入构造函数。forward 中 `B, N, _` 和 `Q = a_query.shape[1]` 均动态获取。

---
