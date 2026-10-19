# ops verify checkpoint provenance

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_checkpoint_provenance_20260522T090007_result.json`
- **Structured JSON:** [`5ee59be8edd4d8125ed0.json`](../../sessions/5e/5ee59be8edd4d8125ed0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Baseline Checkpoint (eval v10)

| 项目 | 值 |
|------|-----|
| **路径** | `/root/autodl-tmp/checkpoints/baseline_object_pudding_eval/best/` |
| **类型** | LoRA 变体架构（`gemma_2b_lora` + `gemma_300m_lora`），权重**合并保存**为 `model.safetensors` (7.0 GB)，无单独 adapter 文件 |
| **训练配置** | `num_train_steps=30000`, `batch_size=32`, `lr=2.5e-05`, cosine decay |
| **数据集** | `physical-intelligence/libero` (LeRobotLiberoDataConfig) |
| **Norm stats** | 从 checkpoint 自带: `best/assets/physical-intelligence/libero` |
| **Freeze 策略** | 冻结 `.*llm.*`，放开 `.*lora.*` |
| **其他文件** | `optimizer.pt` (12.6 GB), `metadata.pt` (3.2 KB) |
| **训练 output 目录** | `/root/autodl-tmp/colliforce-outputs/baseline_object_pudding_seed0/` **不存在**（可能在其他服务器训练后拷贝过来） |

### 2. A3 Checkpoint (eval v10a)

| 项目 | 值 |
|------|-----|
| **路径** | `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best/` |
| **类型** | 标准架构（`gemma_2b` + `gemma_300m`）+ **外挂 LoRA + SDF 模块** |
| **LoRA** | `lora_params.pt` (134 MB, 504 个 LoRA 参数) |
| **SDF 模块** | `sdf_decoder.pt` (1.6 MB) + `ee_extractor.pt` (1.1 MB) + `aux_metadata.pt` (1.3 KB) |
| **Base model** | `model.safetensors` (7.1 GB) |
| **Best step** | **step 26000** (loss 0.01439) |
| **训练总步数** | 30000（保存了 29999、30000、best 三个 checkpoint） |
| **Norm stats** | 从 **pi0_base** 加载: `/root/autodl-tmp/openpi_weights/pi0_base/assets/physical-intelligence/libero` |
| **SDF GT** | `/root/colliforce-vla/data/sdf_gt_object_chocolate.npz` (4084 points) |
| **WandB** | run ID `3td3jpf8` |

### 3. pi0_base 预训练权重

| 项目 | 值 |
|------|-----|
| **路径** | `/root/autodl-tmp/openpi_weights/pi0_base/` |
| **来源** | HuggingFace `lerobot/pi0_base` — Physical Intelligence 的 π₀ VLA 基础模型 |
| **大小** | `model.safetensors` (14.0 GB) |
| **License** | Gemma |
| **原始训练源** | `gs://openpi-assets/checkpoints/pi0_base/params`（两个 eval log 都引用此路径） |

### 4. 异常发现

1. **Baseline 与 A3 使用不同的模型架构变体**：
   - Baseline: `paligemma_variant='gemma_2b_lora'`, `action_expert_variant='gemma_300m_lora'` — LoRA 层**内建**在模型定义中，权重合并保存
   - A3: `paligemma_variant='gemma_2b'`, `action_expert_variant='gemma_300m'` — 标准架构 + 外部加载 `lora_params.pt`
   - 两者的 LoRA 实现路径不同，可能影响参数量和行为

2. **Norm stats 来源不同**：
   - Baseline: 从自身 checkpoint 的 `assets/` 加载
   - A3: 从 `pi0_base` 的 `assets/` 加载
   - 如果训练时各自用了不同的 norm stats，eval 时也应保持一致，否则会有偏差

3. **模型大小差异**：pi0_base 是 14.0 GB，baseline/A3 的 model.safetensors 约 7.0 GB — 恰好一半，推测是 **float32 → bfloat16** 的差异（训练精度配置为 `bfloat16`）

4. **Baseline 训练日志缺失**：训练 output 目录在 westd-45947 上不存在，无法确认 best checkpoint 对应的具体 step

---
