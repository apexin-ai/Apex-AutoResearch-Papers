# ops check gpu eval status

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-eval-status_20260523T161229_result.json`
- **Structured JSON:** [`e811580c385aa486550d.json`](../../sessions/e8/e811580c385aa486550d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 状态
| GPU | 型号 | 显存占用 | GPU-Util | 状态 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 0 MiB | 0% | **空闲** |
| 1 | RTX PRO 6000 Blackwell (96GB) | 0 MiB | 0% | **空闲** |
| 2 | RTX PRO 6000 Blackwell (96GB) | 0 MiB | 0% | **空闲** |
| 3 | RTX PRO 6000 Blackwell (96GB) | 0 MiB | 0% | **空闲** |

### 实验状态
所有 4 个实验均已完成，PID 156476/157677/158192 均不存在，无 GPU 进程。

### 结果汇总

| 实验 | lz* | lz*_seen | lz*_unseen | acc_overall | acc_seen | acc_unseen |
|------|-----|----------|------------|-------------|----------|------------|
| **contam_15 s1** | **-2.9922** | -2.3342 | -2.2668 | 0.6654 | 0.6676 | 0.6650 |
| **contam_50 s1** | **-3.3313** | -1.9171 | -2.8092 | 0.6983 | 0.6914 | 0.7053 |
| **contam_5 s3** | **-1.9517** | -1.0768 | -1.5064 | 0.6353 | 0.7821 | 0.6276 |
| **contam_25 s3** | **-3.1966** | -0.4560 | -2.7199 | 0.6758 | 0.7675 | 0.6453 |

### 关键观察

- **s3 系列** (contam_5/25) 的 seen vs unseen 差距明显大于 s1 系列：
  - contam_25 s3: lz\*\_seen=-0.46 vs lz\*\_unseen=-2.72（差值 2.26）
  - contam_5 s3: acc\_seen=0.78 vs acc\_unseen=0.63（差值 0.15）
- **s1 系列** (contam_15/50) 的 seen/unseen 差距较小，contam_15 几乎无差异
- contam_50 s1 的整体 lz\* 最低（-3.33），但 unseen 的 acc 反而高于 seen（0.705 > 0.691），提示 s1 的 contamination 信号弱

---
