# ssh verify gpu and dcol

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_gpu_and_dcol_20260515T024659_result.json`
- **Structured JSON:** [`9e218ad926d078adb03d.json`](../../sessions/9e/9e218ad926d078adb03d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌已清晰。

---

## 结果汇总

### 1. nvidia-smi (10:47:18)

| GPU | PID | 进程 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 280347 | `extract_features.py` (gpt2xl_topk50) | 9026 MiB / 97887 MiB | 63% |
| 1 | 278173 | `extract_features.py` (gpt2xl_topk50) | 9026 MiB / 97887 MiB | 62% |

### 2. dcol_deberta_004 状态：**已死亡并被替换**

- 原 PID 277577：**不存在**
- 曾在 10:41 被重启到 cuda:0，跑到 step 220/3937 后被 kill
- **已被新实验 `dcol_lora_v5` 替代**（PID 283196，10:47:36 启动）
  - 命令：`python src/dcol_trainer.py ... --output_dir checkpoints/dcol_lora_v5/ --margin_lr 1e-4 --gpu 0`
  - 当前进度：Epoch 1, step 20/3937, loss=1.9047, ce=1.3883, cl=0.5164, acc=0.2547
  - 与旧版区别：`margin_lr` 从 `0.001` → `0.0001`，output 从 `dcol_lora/` → `dcol_lora_v5/`

### 3. cuda:0 状态：**双进程共享**
- `extract_features.py` (PID 280347, 运行 ~4min)
- `dcol_lora_v5` (PID 283196, 刚启动) — 在 nvidia-smi 快照时还未加载上 GPU，现在应该已经在跑了

### 4. cuda:1 状态：**占用**
- `extract_features.py` (PID 278173, 运行 ~6min)

### 结论
双 GPU 并非空闲——两块都在跑 gpt2xl_topk50 feature extraction，同时 cuda:0 上还叠加了新的 dcol_lora_v5 训练。dcol_deberta_004 这个实验名已不存在，被新参数版本 v5 替代。

---
