# infra extract code ground truth

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_extract_code_ground_truth_20260520T202654_result.json`
- **Structured JSON:** [`4f8bf66221c45e41a527.json`](../../sessions/4f/4f8bf66221c45e41a527.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the compiled output:

```
=== finetune.py 超参 ===
occ_loss_weight = 0.01 (finetune.py:L92, default, cmdline未覆盖)
occ_loss_decay_steps = 50000 (finetune.py:L93, default, cmdline未覆盖)
  公式: w(t) = 0.01 * exp(-t / 50000)  (finetune.py:L1109)
occ_detach = False (finetune.py:L94, cmdline传了false)
occ_resolution = 64 (finetune.py:L95)
learning_rate = 5e-4 (finetune.py:L100, cmdline一致)
lr_warmup_steps = 0 (finetune.py:L101, default, 即无warmup)
num_steps_before_decay = 100000 (finetune.py:L102, cmdline一致)
  LR scheduler: MultiStepLR(milestones=[100000], gamma=0.1)  (finetune.py:L1006-1009)
  注意: max_steps=50005 < 100000，所以LR decay从未触发
max_steps = 50005 (cmdline覆盖，default=200000, finetune.py:L104)
save_freq = 2500 (cmdline覆盖，default=10000, finetune.py:L108)
batch_size = 8 (finetune.py:L98, per device, 单GPU训练)
grad_accumulation_steps = 1 (finetune.py:L103, default, cmdline未覆盖)
  有效batch_size = 8 * 1 = 8
LoRA rank = 32 (finetune.py:L118, cmdline一致)
LoRA alpha = min(32, 16) = 16 (finetune.py:L892)
LoRA dropout = 0.0 (finetune.py:L119, default)
optimizer = AdamW(lr=5e-4) (finetune.py:L1000, weight_decay用PyTorch默认0.01)
seed = 42/43/44 for s0/s1/s2 (cmdline)

=== occ_head.py 完整架构 (prismatic/models/occ_head.py) ===
BEVOccupancyHead:
  输入: visual_features (B, N, D), D=vision_embed_dim
  1. 截取前 num_patches_per_image=256 个patch (即16x16第一视角)
  2. Linear(in_dim=2176, hidden_dim=256)                   — project层
  3. reshape → (B, 256, 16, 16)
  4. ConvTranspose2d(256→128, k=4, s=2, p=1)               — 16→32
  5. BatchNorm2d(128)
  6. GELU()
  7. ConvTranspose2d(128→64, k=4, s=2, p=1)                — 32→64
  8. BatchNorm2d(64)
  9. GELU()
  10. Conv2d(64→1, k=1)                                     — 最终logits
  输出: (B, 1, 64, 64) occupancy logits

输入维度 = 2176 (DINOv2-ViT-L 1024 + SigLIP-ViT-So400m 1152, dinosiglip_vit.py:L154-155)
  验证: occ_head参数量 = 1,213,313 (训练日志确认)
输出分辨率 = 64×64

FocalLoss (occ_head.py:L52):
  alpha = 0.25 (default, 实例化时无参数: FocalLoss().to(device_id), finetune.py约L987)
  gamma = 2.0 (default)
  实现: binary CE + focal weight = alpha_t * (1-pt)^gamma

=== 其他训练配置 (cmdline) ===
use_l1_regression = True
use_diffusion = False
use_film = False
num_images_in_input = 2
use_proprio = True
image_aug = True
dataset = libero_spatial_no_noops

可训练参数:
  VLA LoRA: 110,828,288 (1.45% of 7.65B)
  proprio_projector: 16,818,176
  action_head (L1): 151,117,831
  occ_head: 1,213,313
  total: 279,977,608

=== 硬件信息 ===
GPU 型号 = 4× NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB each)
实际使用 = 每个seed用1张GPU (CUDA_VISIBLE_DEVICES=0/1/2)
训练速度 = ~1.08 it/s (稳态)
预估训练时间 = 50005 / 1.08 / 3600 ≈ 12.9 小时
当前进度(occ_s2) = step 14630/50005 (29%), 已跑 ~3h51m
```

---
