# infra crm train gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_crm-train-gpu-check_20260513T210737_result.json`
- **Structured JSON:** [`1d00b7f82079dc514878.json`](../../sessions/1d/1d00b7f82079dc514878.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 原始输出

### 1. cuda:1 GPU 利用率
```
10 %, 0 %, 555 MiB
```

### 2. CRM 训练进程
```
PID 92185/92186  0.8% CPU  ~1.5GB RSS
python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42
```
GPU 1 上实际 CUDA 进程为 PID 78520，占用 546MiB。

### 3. 训练日志（crm-train-v1.log）
```
[train_crm] args: batch_size=32, K=10, obs_dim=960, hidden_dim=256
[train] Total: 26737 samples from 2 benchmark(s)
[train] CRM parameters: 337,438
...
Epoch 19/50  train_loss=0.017262  val_loss=0.010287  lr=6.84e-04
  → New best val_loss: 0.010287
  epoch 20 batch 450/752 loss=0.011704  (当前位置)
```

val_loss 趋势（每 epoch 连续下降）：
```
E1:  0.015636 → E5:  0.012686 → E10: 0.011442 → E15: 0.011114 → E19: 0.010287
```

### 4. 完整 nvidia-smi
```
GPU 0: RTX 4090  1423MiB  9%   (evaluate.py spatial)
GPU 1: RTX 4090   555MiB  10%  (train_crm.py ← 目标)
GPU 2: RTX 4090  1423MiB  18%  (evaluate.py reconvla)
GPU 3: RTX 4090  1541MiB  23%  (train_crm.py precompute K5)
```

---

## 分析

**GPU 利用率：10%，严重低效。** 555MiB / 24564MiB VRAM（2.3%），功耗 56W / 450W。RTX 4090 基本在空转。

**原因：模型太小 + batch 太小。** 337K 参数的 MLP 在 RTX 4090 上计算量微不足道。batch_size=32 时每个 forward/backward pass 在微秒级完成，大部分时间消耗在 Python 循环开销和 CPU↔GPU 数据搬运上。

**Epoch 速度：** 日志创建于 04:10，当前 05:08，约 58 分钟完成 19.6 个 epoch → **~3 分钟/epoch**。752 batches/epoch × 32 = 24064 samples/epoch（含 val split）。对一个 337K MLP 来说 3 分钟太慢了。

**建议增大 batch_size：**

| batch_size | batches/epoch | 预估 epoch 时间 | GPU 利用率预期 |
|------------|---------------|-----------------|---------------|
| 32（当前） | 752 | ~3 min | ~10% |
| 256 | 94 | ~30s | ~30-40% |
| 512 | 47 | ~20s | ~50% |
| 1024 | 24 | ~15s | ~60% |

建议直接改到 **512 或 1024**。337K 参数 MLP + 960 维输入，bs=1024 也只占几十 MB 显存，4090 完全吃得下。总训练时间可以从 ~2.5 小时压缩到 ~15 分钟。

**Loss 趋势正常**，val_loss 19 个 epoch 每轮都在降，还没饱和。增大 batch_size 后需相应调大 lr（线性缩放法则：bs 翻 N 倍，lr 翻 N 倍，但上限大约 0.01）。

---
