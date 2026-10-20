# ops westd34685 post completion

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd34685_post_completion_20260523T172945_result.json`
- **Structured JSON:** [`c72d7e21ffad1dfeacde.json`](../../sessions/c7/c72d7e21ffad1dfeacde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码确认 cutoff 语义（finetune.py:94-95, 1165-1170）：

```python
# "after": zero occ loss after cutoff_step
# "before": zero before, enable after
if cfg.occ_loss_cutoff_mode == "before":
    occ_weight_now = 0.0 if batch_idx < cfg.occ_loss_cutoff_step else base_weight
else:  # "after"
    occ_weight_now = base_weight if batch_idx < cfg.occ_loss_cutoff_step else 0.0
```

`after` = 在 cutoff_step **之后** occ_loss 权重归零（前 N 步有 occ，之后无）。用户命令中 `--occ_loss_cutoff_mode after` 对 cutoff_15k_s0 是正确的。

cutoff_25k_s0 在 step 41800 显示 occ_loss=0.0118 是因为 OCC head 仍在前向传播计算 loss 值并记录，但 weight=0.0 不参与反向传播。

---

## 报告

### 1. 实验状态：全部仍在运行，无完成/崩溃

| 实验 | 进度 | GPU | 预计剩余 |
|------|------|-----|----------|
| vanilla_retrain_s0 | 48647/50005 (97%) | 0 | ~21 min |
| full_occ_retrain_s0 | 48421/50005 (97%) | 1 | ~24 min |
| reverse_cutoff_s0 | 41751/50005 (83%) | 2 | ~2.2 h |
| cutoff_25k_s0 | 41829/50005 (84%) | 3 | ~2.1 h |

GPU util=0% 是瞬时采样误差，17 个 finetune 进程活跃。

### 2. Registry 更新：无需操作
无实验完成，无需更新。

### 3. Eval 提交：等待完成
reverse_cutoff_s0 和 cutoff_25k_s0 均在 83-84%，约 2 小时后完成。

### 4. 梯度分析：等待完成
vanilla_retrain_s0 和 full_occ_retrain_s0 约 20-25 分钟后完成，完成后可启动。

### 5. cutoff_15k_s0：等待 GPU 释放
GPU 1 被 full_occ_retrain_s0 占用，~24 min 后释放。`--occ_loss_cutoff_mode after` 语义已确认正确（前 15K 步有 occ loss，之后归零）。

### Checkpoint 路径（当前最高 40K）
- `/root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+...--40000_chkpt`
- `/root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+...--40000_chkpt`
- `/root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+...--40000_chkpt`
- `/root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+...--40000_chkpt`

**建议：** ~25 分钟后重新检查 vanilla_retrain_s0 和 full_occ_retrain_s0 完成状态，启动梯度分析和 cutoff_15k_s0。~2.5 小时后检查 reverse_cutoff_s0 和 cutoff_25k_s0 完成状态，提交 eval。

---
