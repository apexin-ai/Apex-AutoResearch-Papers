# ssh diagnose 10894 and precheck ckpt

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_10894_and_precheck_ckpt_20260525T195143_result.json`
- **Structured JSON:** [`af00aca7b40441eaca24.json`](../../sessions/af/af00aca7b40441eaca24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实际命令已确认。现在汇总结果。

## 10894 诊断结果

| 实验 | GPU | 状态 | 当前 local step | log_step | 目标 log_step | 速度 | 下一个 checkpoint ETA |
|------|-----|------|----------------|----------|-------------|------|----------------------|
| cutoff_45k_s2_v2 | 0 | 训练中 | 8565/50005 | 8565 | 50000 | ~1.08 it/s | step 10000 → ~22min |
| mvp_occ_s3_v2 | 1 | 训练中 | 8163/50005 | 28163 | 50000 | ~1.09 it/s | step 30000 → ~28min |
| full_occ_ln_s3_v2 | 2 | 训练中 | 8349/50005 | 28349 | 50000 | ~1.08 it/s | step 30000 → ~25min |
| ablation_occ_detach_s3_v2 | 3 | 训练中 | 8364/50005 | 28364 | 50000 | ~1.08 it/s | step 30000 → ~25min |

**GPU**: 4× RTX PRO 6000 Blackwell (98GB)，全部 96-99% 利用率

### Checkpoint 命名规则

代码确认 (finetune.py:675):
```
checkpoint_dir = Path(str(run_dir) + f"--{log_step}_chkpt")
```

**Resume 实验** (`--resume True --resume_step 20000`):
- `log_step = 20000 + gradient_step_idx`（用 global step，不是 local）
- save_freq=10000，下次保存在 **log_step 30000**（gradient_step_idx=10000）
- 训练自动结束于 log_step=50005（gradient_step_idx=30005）

### 确切 Checkpoint 路径

**step 30000 checkpoint**（resume 实验下一个保存点，~25-28min 后）：
```
/root/autodl-tmp/checkpoints/mvp_occ_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s3--30000_chkpt
/root/autodl-tmp/checkpoints/full_occ_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3--30000_chkpt
/root/autodl-tmp/checkpoints/ablation_occ_detach_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3--30000_chkpt
```

**step 50000 checkpoint**（resume 实验最终保存点，gradient_step_idx=30000，~5.5h 后）：
同上路径，后缀改为 `--50000_chkpt`

**cutoff step 10000**（下一个，~22min 后）：
```
/root/autodl-tmp/checkpoints/cutoff_45k_s2_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_45k_s2_v2--10000_chkpt
```

**cutoff step 50000**（最终，~10.7h 后）：同上路径，后缀 `--50000_chkpt`

### 磁盘 — 红色警报

```
/root/autodl-tmp: 231G / 250G (93%),  仅剩 20GB
/（根分区）:       22G / 30G  (71%),  仅剩 9GB
```

**每个 checkpoint ≈ 14.4GB。25-28 分钟内 4 个实验同时要保存 checkpoint（cutoff 的 10K + 3个 resume 的 30K），总计约 58GB，但只有 20GB 可用。第一个 checkpoint 保存成功后，后续 3 个将因磁盘满而失败，训练可能崩溃。**

### "local step 30000" 的歧义

代码中 progress bar 显示的是 `gradient_step_idx`（从 0 开始），但 checkpoint 用 `log_step`（= 20000 + gradient_step_idx）。

- 如果 Director 说的 "local step 30000" = gradient_step_idx 30000 → 对应 log_step=50000，training 自动结束，无需 kill
- 如果指 log_step 30000 → gradient_step_idx=10000，约 25 min 后到达，需要手动 kill

请确认 Director 的意图，以及是否需要立即清理磁盘空间以避免 checkpoint 保存失败。

---
