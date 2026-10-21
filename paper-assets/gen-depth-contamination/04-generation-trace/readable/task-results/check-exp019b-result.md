# check exp019b result

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp019b_result_20260516T115406_result.json`
- **Structured JSON:** [`34d5613427f04f86baf3.json`](../../sessions/34/34d5613427f04f86baf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。汇总如下：

---

## 产出总结

### 1. GPU 状态（4x RTX 4090D）

| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | 忙 (PID 10403) | 15.9/24.6 GB | 96% |
| **cuda:1** | **空闲** | **0/24.6 GB** | **0%** |
| cuda:2 | 忙 (PID 38725) | 4.5/24.6 GB | 90% |
| cuda:3 | 忙 (PID 32175) | 4.0/24.6 GB | 88% |

**cuda:1 完全空闲，可用。**

### 2. exp-019b: 已完成 (EXIT_CODE=0)

进程 36365 已退出，结果文件齐全。

### 3. 结果 & 对比

**Pairwise AUC + Bootstrap 95% CI:**

| Pair | exp-019 Self-scorer | exp-019b Cross-scorer | Cross CI | 判定 |
|------|--------------------|-----------------------|----------|------|
| 0v1 | 0.9843 | 0.9209 | [0.9189, 0.9229] | PASS |
| 1v2 | 0.5935 | 0.5695 | [0.5645, 0.5746] | FAIL (< 0.60) |
| 2v3 | 0.5402 | 0.5335 | [0.5283, 0.5382] | FAIL |
| 3v4 | 0.5232 | 0.5140 | [0.5063, 0.5213] | FAIL |
| 4v5 | 0.5181 | 0.5184 | [0.5128, 0.5244] | FAIL |

**K\* = 1**（两个实验一致）

**关键结论：Mistral K\*=1 是 genuine，不是 self-scorer artifact。** Cross-scorer AUC 全线低于 self-scorer（1v2: 0.5695 < 0.5935），说明换 scorer 后区分度反而下降。如果 K\*=1 是 self-scoring 造成的虚高，cross-scorer 应该更高才对——实际相反。

其他指标：
- JSD 模式一致（0v1 远大于其余）
- Ordinal MAE: 1.37 (cross) vs 1.23 (self)，cross 更差
- Top-3 features 完全相同：freq_entropy, surp_d1_skew, surp_d1_mean

---
