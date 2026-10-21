# diagnose adaptive fix seed42 slow

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_adaptive_fix_seed42_slow_20260514T162405_result.json`
- **Structured JSON:** [`089868e075957f1c3757.json`](../../sessions/08/089868e075957f1c3757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因。eval_runtime = **2629.7 秒**（44 分钟），每 500 步触发一次。这就是速度"异常"的来源。

---

## 排查结论

### 速度异常：**假阳性，非真实慢速**

**根因：评估阶段污染 tqdm EMA 速度估计。**

| 指标 | seed42 (cuda:1) | seed456 (cuda:3) |
|------|-----------------|-------------------|
| **实际 s/it** | ~2.23-2.33 | ~2.20-2.25 |
| 当前步数 | 1135/6103 | 655/6103 |
| 总耗时 | 2:10:09 | 1:08:24 |

两者训练速度**基本一致**。用户观察到的 4.8-6.0 s/it 来源有两个：

1. **eval 阶段（主因）**：每 500 步触发一次 eval（67823 samples），耗时 **2629.7 秒 ≈ 44 分钟**。eval 结束后 tqdm EMA 被污染至 791s/it，需要约 15-20 步才收敛回 ~2.3s/it。在 step 514-516 附近，tqdm 会显示 ~4.8-6.0 s/it。
2. **CUDA warmup（次因）**：seed42 首步 5.50s/it，seed456 首步 2.76s/it（seed42 可能先启动，GPU 冷启动更慢）。

### b 值分布对比

| | seed42 | seed456 |
|--|--------|---------|
| max b | **11.16** | **20.0**（两次） |
| 极端值 | 10.51, 9.18, 5.84 | 20.0, 10.94, 10.80, 8.92 |

**seed456 的极端 b 值远大于 seed42**，但 seed456 速度完全正常。极端 b 值 **不是速度瓶颈**。

### ESS 分析

两个实验的 ESS 都频繁在 ~2.0 附近（n_min=2 的地板值）。alpha_eff=0.8（上限）时 ESS 可达 2.5-3.9。这是 n_min=2 配置下的**预期行为**，不是过度约束。

### 硬件排除

| GPU | util | 进程数 | 显存使用 |
|-----|------|--------|---------|
| 0 | 99% | 1 (PID 112475) | 46514 MiB |
| **1** | **99%** | **1 (PID 108213, seed42)** | **74998 MiB** |
| 2 | 71% | 1 (PID 109362, seed123) | 74998 MiB |
| 3 | 99% | 1 (PID 115071, seed456) | 74998 MiB |

- cuda:1 无竞争，GPU 利用率 99%，无 NaN/Inf
- 无 I/O 竞争

### 结论

**没有速度异常。** 观察到的"慢速"是 eval 阶段（每 500 步，每次 44 分钟）对 tqdm 速度估计的干扰。所有 seed 的实际训练速度都在 ~2.2-2.3 s/it。

如需消除此干扰，可在下次实验中：设 `eval_strategy="no"` 或增大 `eval_steps` 间隔。

---
