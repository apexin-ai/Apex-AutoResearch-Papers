# check westd 34887 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-34887-status_20260518T031858_result.json`
- **Structured JSON:** [`de5ef042ea35c41f376d.json`](../../sessions/de/de5ef042ea35c41f376d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## westd-34887

### GPU 状态
| GPU | 型号 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% | 30C |
| cuda:1 | RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% | 29C |

无运行进程，两卡完全空闲。

### bce_isocompute_v3_s42_eval (PID 91355) -- **已完成**
进程已结束。结果 (sparsity=50%, global_topk, LLaMA-3.1-8B):

| Metric | Value |
|--------|-------|
| **WikiText-2 PPL** | **27.9696** |
| ARC-C acc | 0.2346 |
| ARC-C acc_norm | 0.2765 |
| WinoGrande acc | 0.5162 |
| MMLU acc | 0.2614 |
| GSM8K exact_match | 0.0190 |

这是 BCE loss 训练的 predictor 在 50% sparsity 下的结果，性能极差（基本接近随机）。

### SNR Extended (PID 92073/92074) -- **已完成**
进程已结束。完整 SNR 对比结果 (300 steps, KL vs BCE):

| Step | KL SNR (mean) | KL 95% CI | BCE SNR (mean) | BCE 95% CI |
|------|---------------|-----------|----------------|------------|
| 0 | 0.00001300 | [0.00000739, 0.00001861] | 0.00006991 | [0.00005280, 0.00008701] |
| 50 | 0.00026323 | [0.00015575, 0.00037070] | 0.00000823 | [0.00000582, 0.00001065] |
| 100 | 0.00073106 | [0.00059571, 0.00086642] | 0.00172904 | [0.00066593, 0.00279215] |
| 150 | 0.00059818 | [0.00049438, 0.00070199] | 0.00295003 | [0.00133972, 0.00456035] |
| 200 | 0.00021511 | [0.00016691, 0.00026331] | 0.00135685 | [0.00087027, 0.00184342] |
| 250 | 0.00014465 | [0.00007010, 0.00021919] | 0.00360360 | [0.00202925, 0.00517795] |
| 300 | 0.00587730 | [0.00423155, 0.00752304] | 0.00114449 | [0.00064741, 0.00164156] |

**Final ratio (KL/BCE at step 300): 5.14x**

BCE loss curve (sampled):
| Step | BCE loss | Sparsity |
|------|----------|----------|
| 50 | 0.6424 | 0.103 |
| 100 | 0.6489 | 0.304 |
| 150 | 0.6475 | 0.336 |
| 200 | 0.6423 | 0.296 |
| 250 | 0.6400 | 0.300 |
| 300 | 0.6419 | 0.298 |

KL 训练时间 641s, BCE 训练时间 320s。

### 磁盘
| Filesystem | Size | Used | Avail | Use% |
|------------|------|------|-------|------|
| overlay | 30G | 25G | 5.8G | 81% |

**磁盘偏紧，剩余 5.8G。**

---

## westd-41718

### GPU 状态
| GPU | 型号 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% | 29C |
| cuda:1 | RTX PRO 6000 Blackwell | 0MiB / 97887MiB | 0% | 30C |

无运行进程，两卡完全空闲。

### kl30_8b_s123_eval (PID 37184) -- **已完成**
进程已结束。结果 (KL loss, sparsity=30%, global_topk, LLaMA-3.1-8B, seed=123):

| Metric | Value |
|--------|-------|
| **WikiText-2 PPL** | **8.9267** |
| ARC-C acc | 0.4462 |
| ARC-C acc_norm | 0.4744 |
| WinoGrande acc | 0.7024 |
| MMLU acc | 0.3836 |
| GSM8K exact_match | 0.0917 |

Eval 耗时 6472.7s。

### kl30_8b_s456_eval (PID 37480) -- **已完成**
进程已结束。结果 (KL loss, sparsity=30%, global_topk, LLaMA-3.1-8B, seed=456):

| Metric | Value |
|--------|-------|
| **WikiText-2 PPL** | **8.9614** |
| ARC-C acc | 0.4360 |
| ARC-C acc_norm | 0.4462 |
| WinoGrande acc | 0.7143 |
| MMLU acc | 0.2714 |
| GSM8K exact_match | 0.0887 |

Eval 耗时 6699.6s。

**注意**: s456 的 MMLU 比 s123 低很多（0.2714 vs 0.3836），方差很大。

### 磁盘
| Filesystem | Size | Used | Avail | Use% |
|------------|------|------|-------|------|
| overlay | 30G | 3.4G | 27G | 12% |

磁盘充裕。

---

## 总结
- **4 个任务全部完成**，4 张 GPU 全部空闲
- westd-34887 磁盘 81% 已用（剩 5.8G），需注意
- BCE isocompute v3 在 50% sparsity 下性能极差（PPL 28.0，downstream 接近随机）
- KL30 两个 seed 的 PPL 很接近（8.93 vs 8.96），但 MMLU 方差极大（0.38 vs 0.27）
- SNR 实验显示 KL 在 step 300 的 SNR 是 BCE 的 5.14 倍

---
