# ops status check loop10

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-loop10_20260515T005500_result.json`
- **Structured JSON:** [`bbb6bc1474f77a2c71b1.json`](../../sessions/bb/bbb6bc1474f77a2c71b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 训练进程
- **状态**: 存活，PID 51297，CPU 101%，GPU 1 占用 80.3GB/97.9GB，利用率 92%
- **进度**: step 87/500，最新日志时间 `00:55:24 UTC`（刚刚）
- **近期指标** (step 80-87): prove_rate 波动大 (0~1.0)，reward_mean 间歇为 0，parse_rate 稳定 1.0
- **速率**: 近 20 步约 6 秒/步，按此速率剩余 413 步 ≈ **41 分钟**

### GPU 使用
| GPU | 进程 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | PID 54436 (python3) | 16.3GB/97.9GB | 69% |
| 1 | PID 51297 (exp1-random-b03-s44-r2) | 80.3GB/97.9GB | 92% |

注意：GPU 0 有未知进程 PID 54436。

### 磁盘
- **数据盘**: 82G/250G (33%) — 比上次 96% 大幅改善

### outputs 目录明细

| 目录 | 大小 | 状态 | 可清理 |
|------|------|------|--------|
| exp1_isr_b03_s44_r2 | 31G | 已完成 | **是** |
| exp1_random_b03_s44 | 15G | 已完成 | **是** |
| exp1_random_b03_s44_r2 | 15G | **训练中** | 否 |
| exp1_isr_b03_s43_eval | 228K | eval 结果 | 可选 |
| exp1_isr_b03_s44_r2_eval | 168K | eval 结果 | 可选 |
| exp1_random_b03_s43_eval | 0 | 空 | 可选 |

**可清理 checkpoint 合计 ~46G**（exp1_isr_b03_s44_r2 + exp1_random_b03_s44），前提是这两个实验的 eval 已完成且不再需要权重。

---
