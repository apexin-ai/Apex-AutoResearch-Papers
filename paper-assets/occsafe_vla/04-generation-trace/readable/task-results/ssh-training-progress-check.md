# ssh training progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-progress-check_20260526T095810_result.json`
- **Structured JSON:** [`6cce91654484dc540d6c.json`](../../sessions/6c/6cce91654484dc540d6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the summary:

---

## 训练实验进度总览 (2026-05-26)

### westd-10894 (4×RTX PRO 6000)

| exp_id | GPU | 当前 step / 50005 | 速度 | 预估剩余 | GPU 利用率 | 状态 |
|--------|-----|-------------------|------|----------|-----------|------|
| reverse_cutoff_s2_v2 | cuda:0 | ~3,000 (估) | ~0.95 it/s | **~13.8h** | 68% | 刚启动57min，无日志文件，前次运行昨日exit code=1 |
| mvp_occ_s3_v2 | cuda:1 | ~46,000 (估) | ~0.95 it/s | **~1h 10min** | 32% | 运行13h+，40k ckpt已保存，无日志 |
| full_occ_ln_s3_v2 | cuda:2 | ~45,900 (估) | ~0.95 it/s | **~1h 12min** | 99% | 运行13h+，40k ckpt已保存，无日志 |
| ablation_occ_detach_s3_v2 | cuda:3 | ~45,800 (估) | ~0.95 it/s | **~1h 14min** | 79% | 运行13h+，40k ckpt已保存，无日志 |

> 10894 的 mvp/full_occ/ablation 三个实验**无日志文件**（/tmp 和 logs/ 均无），step 数由 30k→40k checkpoint 时间差推算（10559s/10k steps）加上当前时间差估算。

### westd-34685 (4×RTX PRO 6000)

| exp_id | GPU | 当前 step / 50005 | 速度 | 预估剩余 | GPU 利用率 | 状态 |
|--------|-----|-------------------|------|----------|-----------|------|
| vanilla_v2_s1 | cuda:0 | **4,473** | ~1.06 it/s | **~11.9h** | 99% | 正常 |
| vanilla_v2_s2 | cuda:1 | **4,484** | ~1.06 it/s | **~11.9h** | 99% | 正常 |
| detach_ln_s3 | cuda:2 | **4,448** | ~1.06 it/s | **~11.9h** | 85% | 正常，occ_loss=0.0147, action_loss=0.1533 @step4400 |
| cutoff_25k_s1_v2 | cuda:3 | ~2,700 (估) | ~0.95 it/s | **~13.8h** | 99% | 刚启动50min，无日志文件，前次运行有exit记录 |

### 磁盘

| 服务器 | 根分区 | 数据盘 |
|--------|--------|--------|
| westd-10894 | 15G/30G (48%) | 156G/250G (63%) |
| westd-34685 | 12G/30G (39%) | 142G/350G (41%) |

### 需关注

1. **reverse_cutoff_s2_v2 / cutoff_25k_s1_v2**：均为新启动（<1h），前次运行 exit code=1。当前无日志文件输出，无法确认 loss 是否正常。建议确认日志重定向是否正确。
2. **westd-10894 三个长跑实验无日志文件**：可能 stdout/stderr 未重定向到文件。约 1h 后即将完成（50005 steps），无法实时监控 loss 曲线。
3. **mvp_occ_s3_v2 GPU 利用率 32%**：可能是快照瞬时波动，也可能在做 checkpoint saving 或 data loading。
4. **10894 数据盘 63%**：尚可，但 3 个实验即将完成时会再保存 50k checkpoint，需留意空间。

---
