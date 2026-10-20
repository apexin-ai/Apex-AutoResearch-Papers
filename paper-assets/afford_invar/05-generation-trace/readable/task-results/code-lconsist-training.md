# code lconsist training

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lconsist-training_20260519T202726_result.json`
- **Structured JSON:** [`42dc4de970d9d19b84c8.json`](../../sessions/42/42dc4de970d9d19b84c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 创建的文件

| 文件 | 功能 |
|------|------|
| `prismatic/training/consistency_loss.py` | L_consist（pairwise symmetric KL）+ H_entropy（负熵正则） |
| `prismatic/models/affordance_decoder.py` | AffordanceDecoder：layer-18 patch features → 128×128 softmax heatmap |
| `vla-scripts/finetune_afford.py` | 含 L_consist 正则的 LoRA fine-tuning 训练脚本 |
| `prismatic/training/train_utils.py` | **修改**：修复 `torch.cumsum(bool)` 在 PyTorch 2.8 的兼容性 |

### 2. L_consist 和 H_entropy 实现

- **L_consist** = `(1/C(N,2)) Σ_{i<j} [KL(h_i‖h_j) + KL(h_j‖h_i)] / 2` — 对 N=K+1 个 heatmap 的 symmetric KL 均值
- **H_entropy** = `-mean(entropy)` — 最小化时最大化 heatmap 熵，防 delta 退化
- 所有 loss 在 float32 下计算（避免 bf16 精度问题），heatmap 经 softmax 归一化为概率分布

### 3. 训练循环关键修改（vs 原始 finetune.py）

- **数据**: `AffordRLDSBatchTransform` 额外返回 `instruction_text`；`AffordCollator` 处理字符串字段
- **前向**: 原始 batch 带梯度前向 → L_action + layer-18 features；K=3 次 paraphrase 前向（`torch.no_grad()`，节省显存）
- **Feature 提取**: `output.hidden_states[18][:, 1:1+NUM_PATCHES, :]` — 256 个 image patch 位置
- **Decoder**: AffordanceDecoder（Linear proj → 3 层 ConvTranspose2d + GroupNorm + ReLU → spatial softmax）
- **Loss**: `L_total = L_action + 0.1 * L_consist + 0.01 * H_entropy`
- **优化器**: 同时训练 LoRA params + action_head + afford_decoder

### 4. Dry-run 5 步输出

```
[Step 0] L_act=0.5312  L_con=0.516035  H_ent=-7.7063  L_tot=0.5058
         lora_gnorm=5.0896  dec_gnorm=4.8746  hm_mean=0.000061  hm_std=0.000390  hm_max=0.017582  hm_ent=7.11
[Step 1] L_act=5.0625  L_con=0.851465  H_ent=-5.9396  L_tot=5.0883
[Step 2] L_act=3.5938  L_con=0.240621  H_ent=-5.2614  L_tot=3.5652
[Step 3] L_act=1.8203  L_con=0.127463  H_ent=-5.3433  L_tot=1.7796
[Step 4] L_act=1.2891  L_con=0.084126  H_ent=-5.3515  L_tot=1.2440
[Step 5] L_act=1.1875  L_con=0.085176  H_ent=-5.3638  L_tot=1.1424
```

- L_action 从 0.53→1.19（正常波动）
- L_consist 从 0.52→0.08（heatmap 快速趋同）
- gradient norms 非零（LoRA 5.09, decoder 4.87）
- heatmap entropy 7.11（max=log(16384)=9.7，分布有一定 spread）

### 5. 超参建议

| 参数 | 当前值 | 说明 |
|------|--------|------|
| `alpha` | 0.1 | L_consist 权重；因 patch features 在 causal LM 中本身 instruction-independent，此 loss 主要正则化 decoder |
| `lambda_H` | 0.01 | 熵权重；防止 heatmap 坍缩为 delta |
| `batch_size` | 2 | 因 4x 前向，等效原始 bs=8 的显存占用 |
| `learning_rate` | 5e-4 | 同原始 OFT 默认值 |
| `layer_idx` | 18 | 中间层特征，兼顾底层空间信息和高层语义 |
| `num_paraphrases` | 3 | K=3，每 sample 4 次前向 |

### 6. OpenVLA-OFT 原始训练配置

| 参数 | 值 |
|------|-----|
| LoRA rank | 32 |
| LoRA alpha | 16 |
| LoRA target | all-linear |
| LR | 5e-4 |
| Batch size | 8 |
| Action head | L1RegressionActionHead (MLPResNet, 2 blocks) |
| Hidden dim | 4096 |
| Action dim | 7 (LIBERO) |
| Chunk size | 8 |
| Total trainable | ~263M (LoRA 111M + action_head 151M + decoder 1.7M) |

---
