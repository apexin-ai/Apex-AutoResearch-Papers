# research smolvla architecture

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla-architecture_20260513T094515_result.json`
- **Structured JSON:** [`8db12af70cbdb5e6a8b6.json`](../../sessions/8d/8db12af70cbdb5e6a8b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是完整调研结果。

---

## 调研结果

### 1. Action Head 架构

SmolVLA 的 action head 在 `VLAFlowMatching` 类中（`modeling_smolvla.py:556`）：

```
state_proj:         Linear(32 → vlm_hidden_size)       # 状态投影
action_in_proj:     Linear(32 → expert_hidden_size)     # action 输入投影
action_out_proj:    Linear(expert_hidden_size → 32)     # action 输出投影
action_time_mlp_in: Linear(expert_hidden_size*2 → expert_hidden_size)  # 时间+action 融合
action_time_mlp_out:Linear(expert_hidden_size → expert_hidden_size)
```

**关键：action_dim 不是 hardcoded 为 6**。内部统一使用 `max_action_dim=32` 维度，输入时 pad 到 32D，输出时 slice 回 `config.action_feature.shape[0]`：
- 训练：`losses = losses[:, :, :original_action_dim]`（line 381）
- 推理：`actions = actions[:, :, :original_action_dim]`（line 295）

**改为 7D 无需任何架构修改**，只需 dataset 的 `output_features` 指定 `shape=(7,)` 即可。

### 2. Flow Matching Head

- **训练**：`x_t = t * noise + (1-t) * actions`，`u_t = noise - actions`，loss = MSE(u_t, v_t)
- **推理**：10 步 iterative denoising（`num_steps=10`），`x_t = x_t + dt * v_t`
- 时间采样：Beta(1.5, 1.0) * 0.999 + 0.001
- Suffix 编码：`cat(action_emb, time_emb)` → 2 层 MLP（SiLU 激活）→ 送入 expert transformer
- Expert transformer 输出经 `action_out_proj` 得到 velocity field v_t
- 使用 VLM 前缀的 KV cache 做条件生成

### 3. LeRobot 训练 Pipeline

入口：`lerobot-train` CLI → `lerobot/scripts/lerobot_train.py`

Fine-tune 预训练 SmolVLA 命令：
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=&lt;USER>/libero_spatial_lerobot \
  --batch_size=64 \
  --steps=200000
```

默认训练策略：
- `freeze_vision_encoder=True`
- `train_expert_only=True`（只训练 action expert，冻结 VLM backbone）
- `train_state_proj=True`
- lr=1e-4, AdamW, cosine warmup 1000 steps → decay 30000 steps
- 使用 Accelerate 分布式训练

### 4. LIBERO Demo 数据格式

```
data/demo_N/actions:            (T, 7) float64   ← 6 DOF + 1 gripper
data/demo_N/obs/agentview_rgb:  (T, 128, 128, 3) uint8
data/demo_N/obs/eye_in_hand_rgb:(T, 128, 128, 3) uint8
data/demo_N/obs/ee_pos:         (T, 3) float64
data/demo_N/obs/ee_ori:         (T, 3) float64
data/demo_N/obs/ee_states:      (T, 6) float64
data/demo_N/obs/gripper_states: (T, 2) float64
data/demo_N/obs/joint_states:   (T, 7) float64
data/demo_N/obs/robot_states:   (T, 9) float64
data/demo_N/rewards:            (T,) uint8
data/demo_N/dones:              (T,) uint8
```
50 demos/task，~80-134 timesteps/demo。

**需要转换为 LeRobot dataset 格式**（`LeRobotDataset` 使用 HuggingFace datasets + parquet）。

### 5. LoRA Fine-tuning：原生支持

LeRobot 0.5.1 **内建 PEFT/LoRA**，无需自己写：

- `PeftConfig` in `configs/default.py`：method_type="LORA"，r=16
- SmolVLA 的 `_get_default_peft_targets()` 预设了 target modules：
  - `model.vlm_with_expert.lm_expert.*.(q|v)_proj`（expert transformer 的 attention）
  - `model.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out)`（所有 projection layers）

LoRA 训练命令：
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=&lt;USER>/libero_spatial_lerobot \
  --batch_size=32 \
  --steps=100000 \
  --peft.r=16 \
  --peft.method_type=LORA
```

### 6. 推荐方案

1. **数据转换**：LIBERO HDF5 → LeRobot dataset 格式（需写转换脚本，mapping: actions(7D), agentview_rgb, eye_in_hand_rgb, ee_states(6D) as state）
2. **LoRA fine-tune**：直接用 LeRobot 内建 PEFT，default targets 已覆盖 action head + expert attention
3. **action_dim=7 自动生效**：dataset `output_features` 指定 `shape=(7,)` 后，模型内部 pad 到 32D 训练，输出 slice 回 7D
4. **显存预估**：SmolVLM2-500M backbone + LoRA r=16，单张 4090 24GB 应该足够 batch_size=32

---
