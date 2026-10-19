# code acib v5 stopgrad entropy

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib_v5_stopgrad_entropy_20260516T013100_result.json`
- **Structured JSON:** [`5089a9a53f2fc2d749c7.json`](../../sessions/50/5089a9a53f2fc2d749c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改确认完成。

---

### 改动摘要

**1. `/root/acib/acib/losses.py`**
- 新增 `entropy_regularizer(logits)` 静态方法（第65-70行）：计算 sigmoid(logits) 的 binary entropy 均值，最小化此 loss 推动 scorer 输出趋向 0/1
- 保留了 `diversity_regularizer`

**2. `/root/acib/acib/acib_policy.py`**
- 删除 `self.stop_grad_task = False` 初始化
- `_connector_hook` 中 `apply_weights(output, weights_for_task)` 的条件分支简化为硬编码 `apply_weights(output, weights.detach())`（第46行），彻底切断 task loss → scorer 梯度

**3. `/root/acib/scripts/train_acib.py`**
- 新增 `--lambda_ent` 参数（default=0.1）
- 训练循环中计算 `ent_loss = ACIBLoss.entropy_regularizer(scorer_logits)` 并加入 total_loss
- logging 的 print 和 wandb log_dict 中均添加 `ent_loss`
- 配置打印中 `Stop-grad task` 替换为 `Lambda entropy`

### Dry-run 输出（2 步）
```
Loading base model: lerobot/smolvla_libero
Parameters: 450,169,185 total, 100,004,001 trainable (22.2%)
Dataset: 273465 frames, fps=10.0, chunk_size=50
Starting ACIB-SOFT training
  Hidden dim: 64, Alpha: 0.01, Beta: 0.01, Diversity lambda: 0.0
  Lambda entropy: 0.1    ← 新参数
  Steps: 2, Batch size: 4, Device: cuda:0
  Saved checkpoint to /tmp/acib_v5_dryrun/checkpoint-2
Training complete: 2 steps in 0.0h
```

### 验证结果
- entropy_regularizer 返回 0.6071（接近 ln(2)≈0.693 最大值，符合随机 logits 预期）
- 梯度正常回传到 logits（grad_norm=0.0135）
- `weights.detach()` 确认阻断 task loss 梯度（backward 无法穿透 detach）
- 2 步训练无报错，checkpoint 正常保存

---
