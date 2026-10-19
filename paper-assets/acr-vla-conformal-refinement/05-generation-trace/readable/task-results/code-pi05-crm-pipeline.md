# code pi05 crm pipeline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-crm-pipeline_20260521T120702_result.json`
- **Structured JSON:** [`836d55e4ad4e092587b1.json`](../../sessions/83/836d55e4ad4e092587b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成

### 改动 (`/root/acr-vla-conformal-refinement/src/train_crm.py`，备份 `train_crm.py.bak_pre_pi05`)

1. `parse_args()` 新增：
   - `--model {smolvla,pi05}`（默认 `smolvla`）
   - `--pi05_path`（默认 `/root/autodl-tmp/models/pi05_libero_finetuned/`）

2. `precompute_features()`：
   - 删除顶部硬编码的 `from smolvla_wrapper import SmolVLAWrapper`
   - 按 `args.model` 分支加载 `Pi05Wrapper` 或 `SmolVLAWrapper`
   - 加载后写入 `args.obs_dim = wrapper.vlm_hidden_size`（manifest 也会按实际 `obs_features.shape[1]` 自动落盘）

3. Batch 调用兼容：Pi05 没有 `get_obs_features_and_samples_batch`，pi05 分支改成对 `batch_samples` 逐样本调用 `get_obs_features_and_samples(agentview_rgb, task_name, robot_state=ee_states, eye_in_hand_rgb, K)`，再 `torch.cat`。SmolVLA 分支保持 batch 调用不变。

### π0.5 模型路径与维度

- 模型路径：`/root/autodl-tmp/models/pi05_libero_finetuned/` （bjb2-28827 已就绪，含 model.safetensors + 配置 + 归一化器，**无需 rsync**）
- 类名为 `Pi05Wrapper`（不是 `PI05Wrapper`），已按真实命名导入
- `obs_dim` = 2048（`Pi05Wrapper.VLM_HIDDEN_SIZE`），对比 SmolVLA = 960

### 接口兼容性

- Pi05 `get_obs_features_and_samples(agentview_rgb, task_name, robot_state, eye_in_hand_rgb=None, K=10)` 返回 `(obs_feat: (1, 2048), samples: (1, K, chunk_size, FULL_ACTION_DIM))`，与 SmolVLA 单样本接口形状/语义一致；`vlm_hidden_size` 属性两边都有
- `ee_states` (8D = eef_pos+axisangle+gripper_qpos) 同时作为两个 wrapper 的 `robot_state` 输入

### 验证

`python src/train_crm.py --model pi05 --help` 通过，参数 `--model {smolvla,pi05}` / `--pi05_path` 已暴露。

---
