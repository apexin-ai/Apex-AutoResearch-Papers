# diag pi05 normalization

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_pi05-normalization_20260521T032306_result.json`
- **Structured JSON:** [`bd3d958968b88da7308e.json`](../../sessions/bd/bd3d958968b88da7308e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结论。

---

## 诊断结果：**确认存在严重的 normalization mismatch**

### 1. Mismatch 详情

| | 模型训练配置 (config.json) | pi05_wrapper.py 实际使用 |
|---|---|---|
| **State normalization** | `MEAN_STD` | `QUANTILES` (q01/q99) |
| **Action denormalization** | `MEAN_STD` | `QUANTILES` (q01/q99) |

**证据链：**

- `config.json` 第 72-76 行：`"normalization_mapping": {"ACTION": "MEAN_STD", "STATE": "MEAN_STD"}`
- `policy_preprocessor.json` → `"norm_map": {"ACTION": "MEAN_STD", "STATE": "MEAN_STD"}`
- `policy_postprocessor.json` → `"norm_map": {"ACTION": "MEAN_STD"}`
- repo_id 甚至叫 `pepijn223/pi05_libero_31_9_non_q`（**non_q** = non-quantile）

但 `pi05_wrapper.py` 全程用 QUANTILES：
- **第 113-142 行** `_load_normalizer_stats`：加载 `q01`/`q99` 键
- **第 150-157 行** `_normalize_state_quantiles`：`2*(x - q01)/(q99 - q01) - 1`
- **第 158-163 行** `_unnormalize_action`：`(x + 1)*(q99 - q01)/2 + q01`

### 2. 影响：双向错误

**输入错**：robot state 用 QUANTILES 归一化后嵌入 text prompt → 模型收到的 state token 与训练时完全不同。

**输出错**：模型在 MEAN_STD 空间输出 action，被 QUANTILES 反归一化 → 执行的动作幅度和偏移全错。

用 dim 0 举例（假设模型输出 normalized value = 0）：
- MEAN_STD 正确结果：`0 * 0.336 + 0.063 = 0.063`
- QUANTILES 错误结果：`(0+1) * (0.709-(-0.535))/2 + (-0.535) = 0.087`

误差看着不大，但对于 dim 3-6（rotation/gripper，std 极小 ~0.04）scale 差异会更大，且随 normalized value 远离 0 而放大。

### 3. 需要修改的具体行

**`pi05_wrapper.py`：**

| 行号 | 当前（错误） | 应改为 |
|------|-------------|--------|
| 113-142 | 加载 `q01`/`q99` | 加载 `mean`/`std`（参照 smolvla_wrapper.py 第 69-70 行） |
| 150-157 | `_normalize_state_quantiles`：QUANTILES 公式 | `_normalize_state`：`(state - mean) / std` |
| 158-163 | `_unnormalize_action`：QUANTILES 公式 | `action_norm * std + mean`（参照 smolvla_wrapper.py 第 97-99 行） |
| 192-194 | 调用 `_normalize_state_quantiles` | 调用新的 MEAN_STD normalize 方法 |
| 11-12, 89 | 注释/docstring 写 QUANTILES | 更新为 MEAN_STD |

### 4. 其他可能导致 0% SR 的风险点

- **State 维度**：wrapper 用 8D state（eef_pos 3 + axisangle 3 + gripper_qpos 2），config 里 `max_state_dim=32`，需要 padding。SmolVLA wrapper 做了 pad to 32D（第 142 行），但 pi05_wrapper 的 state 是嵌在 text prompt 里的，这部分逻辑需要二次确认 discretization 后的 bin 数量是否正确。
- **Image resolution**：config 里 input image shape 是 `[3, 256, 256]`，但 `image_resolution` 是 `[224, 224]`。wrapper 用 `resize_with_pad` 到 224×224，应该没问题（PI05 内部处理）。
- **Empty camera**：config 有 `empty_cameras: 1`，wrapper 没有显式处理空 camera placeholder，可能需要确认模型内部是否自动处理。

### 5. 建议

**应 kill 当前 eval 并修复后重跑。** normalization mismatch 是双向的（输入 + 输出都错），30 个 rollout 全部 0% SR 完全符合预期，继续跑没有任何价值。

---
