# ssh verify all experiments status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_all_experiments_status_20260525T192811_result.json`
- **Structured JSON:** [`b46f21b35e1c72c818eb.json`](../../sessions/b4/b46f21b35e1c72c818eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。关键发现：三个 resume 实验都从 20K checkpoint 加载权重，但 tqdm 从 0 计数，max_steps=50005。

## westd-10894

| exp_id | PID (python) | GPU | current_step/max_steps | 已用时间 | ETA剩余 | 预计完成(UTC) | 异常 |
|--------|-------------|-----|----------------------|---------|---------|-------------|------|
| cutoff_45k_s2_v2 | 4212* | 0 | ~6893/50005 | 1h52m | ~11h12m | ~14:40 | 无 |
| mvp_occ_s3_v2 | 11723 | 1 | ~6488/50005 | 1h45m | ~11h11m | ~14:39 | **max_steps问题** |
| full_occ_ln_s3_v2 | 6947* | 2 | ~6682/50005 | 1h49m | ~11h21m | ~14:49 | **max_steps问题** |
| ablation_occ_detach_s3_v2 | 7161* | 3 | ~6811/50005 | 1h49m | ~11h06m | ~14:34 | **max_steps问题** |

*PID 为 bash wrapper PID，python PID 在截断输出中。所有 GPU 利用率 99%，VRAM ~62GB/98GB，温度 66-67°C。

## westd-34685

| exp_id | PID (python) | GPU | current_step/max_steps | 已用时间 | ETA剩余 | 预计完成(UTC) | 异常 |
|--------|-------------|-----|----------------------|---------|---------|-------------|------|
| detach_bn_v2_s0 | 5086* | 0 | ~6776/50005 | 1h49m | ~11h18m | ~14:46 | 无 |
| detach_bn_v2_s1 | 2786* | 1 | ~6822/50005 | 1h49m | ~11h06m | ~14:34 | 无 |
| detach_bn_v2_s2 | 3003* | 2 | ~6811/50005 | 1h49m | ~11h06m | ~14:34 | 无 |
| full_occ_bn_v2_s1 | 7427 | 3 | ~5279/50005 | 1h25m | ~11h36m | ~15:04 | 无 |

所有 GPU 利用率 98-99%，温度 67-69°C。训练速度均 ~1.08 it/s。

## Resume max_steps 分析

三个 resume 实验均确认存在 max_steps 问题：

- **mvp_occ_s3_v2**: 从 20K checkpoint resume (`--resume True --resume_step 20000`)，vla_path 指向 `mvp_occ_s3--20000_chkpt`。tqdm 显示 6488/**50005**（batch_idx 从 0 重新计数）。实际全局步数 = 20000 + 50005 = **70005 步**，多训练 20K 步。
- **full_occ_ln_s3_v2**: 从 20K checkpoint resume (`--resume True`，无 resume_step)。日志确认加载 `full_occ_ln_s3--20000_chkpt`。tqdm 6682/**50005**。全局步数 = **70005 步**。
- **ablation_occ_detach_s3_v2**: 从 20K checkpoint resume (`--resume True`)。日志确认加载 `ablation_occ_detach_s3--20000_chkpt`。tqdm 6811/**50005**。全局步数 = **70005 步**。

三个实验的 checkpoint 目录均已有 `10000_chkpt` 和 `20000_chkpt`。

## 异常/风险

1. **⚠️ 三个 resume 实验将训练 70K 步而非预期 50K 步** — 这是 M052 记录的同一个 bug（`finetune.py` resume 后 batch_idx 从 0 重新计数）。每个实验多浪费 ~20K 步 ≈ **5.1 小时 GPU 时间**，三个合计浪费 **~15.3 小时**。预计浪费的步数在 step 50005 之后才开始，即大约在 14:30-15:00 UTC 之后。
2. **可提前干预**：如果期望总步数为 50K，可在这些实验跑到 step ~30005 时（即全局 50005 步）手动停止。按当前进度，约在 **08:00-09:00 UTC** 到达 step 30005。
3. 34685 上的 4 个 D051 实验均为从头训练（无 resume），不受此问题影响。

---
