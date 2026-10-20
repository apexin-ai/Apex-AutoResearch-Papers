# ssh exp017 progress check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp017_progress_check_20260523T231034_result.json`
- **Structured JSON:** [`8a84916ce24cf4590ea6.json`](../../sessions/8a/8a84916ce24cf4590ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-017 状态报告

### 1. 进程存活
- **PID 318082 存活**，已运行 **16h07m**，CPU 103%，内存 2.5%

### 2. 进度：168 / 800 fits (21%)
- 全部 168 fits 都是 **N=8**（第一个 N 值），seed 0–167
- N=20 / N=50 / N=100 尚未开始

### 3. 严重问题：per-fit 时间 6x 劣化
- 早期 seeds (0–1)：**~63s/fit**
- 最近 seeds (163–167)：**~370s/fit**
- 同一个 N=8 内出现 6 倍速度劣化，可能存在内存泄漏或 MCMC 采样器退化

### 4. 时间估算
- 剩余 N=8：32 fits × 370s ≈ **3.3h**
- N=20/50/100 各 200 fits，且更大 N 意味着更长 fit 时间。按 MCMC 对数据量的线性 scaling 粗估：
  - N=20 ~925s/fit → ~51h
  - N=50 ~2300s/fit → ~128h
  - N=100 ~4600s/fit → ~257h
- **总剩余约 440h（~18天）**，如果劣化趋势持续则更久

### 5. GPU 利用率
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 65% | 73.8 / 97.9 GB |
| 1 | 0% | 0 / 97.9 GB |
| 2 | 0% | 0 / 97.9 GB |
| 3 | 0% | 0 / 97.9 GB |

仅用 1 张卡（cuda:0），其余 3 张空闲。

### 6. 磁盘
| 分区 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| / (根) | 15G | 16G | 49% |
| /root/autodl-tmp | 145G | 106G | 58% |

磁盘充足。

### 建议行动
1. **调查 per-fit 劣化**——370s vs 63s 不正常，先看是否有内存泄漏（RSS 增长）或 MCMC 收敛问题
2. **并行化**——当前只用 1 张卡，4 张 RTX 6000 只用了一张。可以按 N 值分 4 个进程各占一张卡，总时间缩短 ~4x
3. 如果 18 天 ETA 不可接受，需要重构实验脚本

---
