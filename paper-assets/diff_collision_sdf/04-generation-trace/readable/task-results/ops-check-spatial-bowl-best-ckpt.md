# ops check spatial bowl best ckpt

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_spatial_bowl_best_ckpt_20260525T140840_result.json`
- **Structured JSON:** [`8bffe04ecb03bfb7d1c8.json`](../../sessions/8b/8bffe04ecb03bfb7d1c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. spatial_bowl 当前 checkpoint 目录

```
/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/a1_sdf_pi05_spatial_bowl_seed0_l005/
├── 4000/
├── 6000/
├── best/          ← 存在，step 6000 的副本
├── best_loss.txt  ← "0.030538175255060196 6000"
└── wandb_id.txt
```

### 2. best checkpoint 保存逻辑：存在且正确

实际生效的文件是 `/root/autodl-tmp/openpi/scripts/train_pytorch.py`（通过 symlink `/root/colliforce-vla/openpi -> /root/autodl-tmp/openpi` 解析），第 222-237 行：

- 每个 `save_interval` 步保存时，将当前 `loss` 与 `best_loss.txt` 中的记录比较
- 如果 `loss < best_loss`，`shutil.copytree` 将该步 checkpoint 复制到 `best/`
- 更新 `best_loss.txt`（格式 `"{loss} {step}"`）
- `save_checkpoint()` 在 train_loop 第 702 行被调用，传入了 `loss=loss.item()`

### 3. 训练日志中有 best 记录

`best_loss.txt` 内容 `0.030538175255060196 6000` 证实 best checkpoint 已在 step 6000 保存。训练 ~20%，后续 loss 下降时会自动更新。

### 4. s0_l005/s0_l01 (object_pudding seed0) 问题原因

- `seed0_l005` 和 `seed0_l01` 目录下 **没有 best_loss.txt 和 best/**
- 但 `seed1_l005`、`seed1_l01`、`seed2_l005`、`seed2_l01` **都有 best/**
- **原因**：seed0 实验在 best checkpoint 逻辑被添加到 `/root/autodl-tmp/openpi/scripts/train_pytorch.py` 之前就已完成。之前使用的 `vlsa-aegis/scripts/train_pytorch.py`（632 行）没有 best 逻辑。

### 5. 总结

**spatial_bowl 不需要修复。** best checkpoint 逻辑已正常工作。s0_l005/s0_l01 缺失 best/ 是历史问题（代码升级前完成的训练），不影响当前运行。

---
