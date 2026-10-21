# eval smolvla libero checkpoint

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla-libero-checkpoint_20260513T100459_result.json`
- **Structured JSON:** [`075ae0a02b8d1bb7ffb7.json`](../../sessions/07/075ae0a02b8d1bb7ffb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果如预期：**0/3 = 0.0% 成功率**。

---

## 完整交付汇总

### 1. Model Card 信息
- **模型**: `lerobot/smolvla_libero` (SmolVLA, 450M 参数)
- **VLM backbone**: HuggingFaceTB/SmolVLM2-500M-Video-Instruct (16 层)
- **基础模型**: lerobot/smolvla_base
- **训练方式**: 全参数微调 (use_peft=false, freeze_vision_encoder=false)
- **训练数据**: lerobot/libero (libero_spatial)
- **训练步数**: 25,000 步, batch_size=32, lr=1e-4
- **动作生成**: Flow matching, 10 denoising steps, chunk_size=50

### 2. Config 关键字段
- `observation.state` shape = [6]
- `action` shape = [7] (6D pose + 1D gripper)
- `normalization_mode` = MEAN_STD
- 3 cameras @ 256×256 (camera1=agentview, camera2=eye_in_hand, camera3 空)
- `max_action_dim` = 32, `max_state_dim` = 32

### 3. action_dim 确认
**action_dim = 7** (6D 位姿 + 1D gripper)

### 4. Quick Eval 结果
**libero_spatial task 0: 0/3 = 0% 成功率**

所有 3 个 rollout 均 300 步耗尽失败。机器人有运动但无法完成任务。

### 5. 失败原因分析

**核心问题——state 表示不匹配**:
- 模型训练时 `observation.state` = eef_pos(3) + eef_quat 分量(3) = 6D
- normalizer 的 state stats 有 8D: eef_pos(3) + eef_quat(4) + gripper(1)
- 我们的 wrapper 喂入的是 `robot0_joint_pos` (7D 关节角)，和 eef_pos+quat 完全不同的物理量
- 这导致 state 归一化后数值完全错误，模型收到的 state 信号是垃圾

**次要问题**:
- 图像分辨率不匹配：env 渲染 128×128，模型训练用 256×256
- 只用了 1 个摄像头 (agentview)，模型训练用了 2 个 (agentview + eye_in_hand)
- 绕过了 lerobot 官方的 pre/post processor pipeline，手动归一化可能有遗漏

### 修正方向

要让 smolvla_libero 正常工作，`smolvla_wrapper.py` 需要：
1. 从 env 取 `eef_pos` (3D) + `eef_quat` (4D) 拼接为 state，而非 `joint_pos`
2. 图像 resize 到 256×256
3. 使用双摄像头 (agentview + eye_in_hand)
4. 或者直接走 lerobot 官方的 `SmolVLAPolicy` 推理管线（含完整 preprocessor/postprocessor）

---
