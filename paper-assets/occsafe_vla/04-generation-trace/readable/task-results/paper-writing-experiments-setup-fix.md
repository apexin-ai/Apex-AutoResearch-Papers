# paper writing experiments setup fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_setup_fix_20260520T204105_result.json`
- **Structured JSON:** [`94045dc4a4a4190323bb.json`](../../sessions/94/94045dc4a4a4190323bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Edit applied. Here's the report:

## 代码提取值（逐项）
1. occ_loss_weight: **0.01** (finetune.py:L93)
2. focal_alpha: **0.25** (occ_head.py:L47 FocalLoss default)
3. focal_gamma: **2.0** (occ_head.py:L47 FocalLoss default)
4. occ_grid_size: **64** (finetune.py:L96 `occ_resolution`)
5. lora_rank: **32** (finetune.py:L119)
6. learning_rate: **5e-4** (finetune.py:L101)
7. lr_scheduler: **MultiStepLR**, milestone=[100K], gamma=0.1 (finetune.py:L1007-L1011); max_steps=50K so decay never fires → effectively constant LR
8. max_steps: **200K default** (finetune.py:L105), overridden to **50K** in actual runs (training log tqdm: `13701/50005`)
9. batch_size: **8** (finetune.py:L99)
10. occ_loss_decay_steps: **50000** (finetune.py:L94); formula: `occ_loss_weight * exp(-step/50000)` (finetune.py:L1110)
11. occ_head 架构: Linear(in_dim→256) → reshape(B,256,16,16) → ConvTranspose2d(256→128,k4s2p1) → BN → GELU → ConvTranspose2d(128→64,k4s2p1) → BN → GELU → Conv2d(64→1,k1) (occ_head.py:L18-L28)
12. GPU: **NVIDIA RTX PRO 6000 Blackwell Server Edition, 98GB** (nvidia-smi)
13. 训练时间: **~13h** (training log: ~1.09 it/s × 50K steps ≈ 12.7h)

## 6 处修正对照

| # | 参数 | 旧值(错误) | 新值(代码) | 代码行号 |
|---|------|-----------|-----------|---------|
| 1 | occ_loss_weight | 0.1 | 0.01 | finetune.py:L93 |
| 2 | focal_alpha | 0.75 | 0.25 | occ_head.py:L47 |
| 3 | occ_head arch | two-layer MLP (256 hidden) | Conv decoder: Linear→reshape→2×ConvTranspose2d→Conv2d | occ_head.py:L18-L28 |
| 4 | GPU | A100 | NVIDIA RTX PRO 6000 | nvidia-smi |
| 5 | training time | 17h | ~13h | training log (1.09 it/s) |
| 6 | lr_schedule | cosine decay | fixed (MultiStepLR milestone at 100K, beyond 50K max_steps) | finetune.py:L1007-L1011 |

额外补充：添加了 occ loss 指数衰减描述（$\lambda_\text{occ}$ 从 0.01 起，时间常数 τ=50K），原稿完全遗漏。

---
