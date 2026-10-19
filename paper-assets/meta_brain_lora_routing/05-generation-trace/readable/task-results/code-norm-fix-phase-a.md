# code norm fix phase a

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_norm_fix_phase_a_20260516T101700_result.json`
- **Structured JSON:** [`24482dda61af43dba17e.json`](../../sessions/24/24482dda61af43dba17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The code only exists on the remote server. I have all the information needed for the final report. Let me compile the results.

---

## Phase A 完成报告：pi0_libero State/Action Normalization Fix

### Step 1: 归一化参数

**`policy_preprocessor.json`** — 使用 `normalizer_processor`，`norm_map: {STATE: MEAN_STD, ACTION: MEAN_STD}`，`features: {}`（空，实际均值/标准差来自 norm_stats.json）

**`policy_postprocessor.json`** — 使用 `unnormalizer_processor`，同样的 `norm_map`

**norm_stats.json**（openpi 官方，32D padded，delta-transformed actions）：

| | mean (first 8/7D) | std (first 8/7D) |
|---|---|---|
| **State** | [-0.0465, 0.0344, 0.7646, 2.9723, -0.2205, -0.1256, 0.0269, -0.0272] | [0.1049, 0.1518, 0.3785, 0.3439, 0.9069, 0.3254, 0.0142, 0.0141] |
| **Action** | [0.0667, 0.0640, -0.8050, -2.9717, 0.2274, 0.1192, -0.0349] | [0.3285, 0.4196, 0.6165, 0.3506, 0.9101, 0.3437, 0.9994] |

来源：`/root/.cache/openpi/openpi-assets/checkpoints/pi0_libero.partial/assets/physical-intelligence/libero/norm_stats.json`，已复制到 `/root/autodl-tmp/checkpoints/pi0_libero/norm_stats.json`

### Step 2 & 3: 代码修改

**`meta_brain_assembly.py`** 修改：
- 新增 `_load_norm_stats(checkpoint_dir, device)` — 从 norm_stats.json 加载 state/action 的 mean/std（32D tensors）
- `__init__` 接受 `norm_stats` 参数
- `infer()` 中：
  - **输入侧**：`inputs["state"] = (state - mean[:8]) / (std[:8] + 1e-6)` 归一化 8D state
  - **输出侧**：`actions = actions * (a_std + 1e-6) + a_mean` 反归一化 32D actions，然后 `actions[:,:,:6] += raw_state[:,:6]` delta-to-absolute 转换
- `from_checkpoints` 和 `from_dummy` 调用 `_load_norm_stats` 并传入构造函数

**`data_loader.py`** 修改：
- 新增 `_load_norm_stats_np()` — numpy 版本的加载函数
- `LiberoLeRobotDataset.__init__` 加载 `self._norm_stats`
- `__getitem__` 中：
  - State：先归一化 8D → 再 pad 到 32D
  - Action：先 delta transform (`actions[:,:6] -= state[:6]`) → 再归一化 32D

### Step 4: Dry Run 结果

**使用 pi0_base checkpoint（openpi 格式）dry run 通过。**

```
Actions shape: torch.Size([1, 50, 32])
Routing weights: [0.118, 0.793, 0.089]

Action stats (7D LIBERO dims across 50 steps):
  actions[0, :7]  = [-0.094, 0.318, 0.514, 1.293, -0.079, -0.166, 0.028]
  actions[-1, :7] = [-0.027, 0.276, 0.731, 1.169, -0.109, -0.266, 0.011]
  min  = -0.2697
  max  = 1.3016
  mean = 0.2651
  std  = 0.4863

Padding dims (7-31): max(abs) = 0.3046, mean = -0.0124
Gripper (dim 6): [0.0024, 0.0279]
Position dims (0-5): [-0.2697, 1.3016]

All routing modes (none/random/universal/oracle): PASSED
```

### 已知问题

**pi0_libero checkpoint（LeRobot 格式）无法直接用于 dry run。** 该 checkpoint 的 key 有 `model.` 前缀，且包含归一化 buffer tensors（`normalize_inputs.*`, `normalize_targets.*`, `unnormalize_outputs.*`），与 openpi 的 `PI0Pytorch` model 不兼容。`from_dummy` 默认使用 pi0_base（openpi 格式），dry run 通过。

**如果需要使用 pi0_libero checkpoint**，需要做 key mapping：strip `model.` prefix + 忽略 normalization buffer keys。这个问题不属于 normalization fix 范畴，是 checkpoint 格式兼容问题。

---
