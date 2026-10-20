# ops gpu status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260516T040752_result.json`
- **Structured JSON:** [`2fb9fd067359503095b5.json`](../../sessions/2f/2fb9fd067359503095b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

## GPU 状态总览（2026-05-16 12:08 UTC）

| GPU | 显存 | 利用率 | 温度 | 进程 | 任务 |
|-----|------|--------|------|------|------|
| **0** | 24.8/97.9 GB (25%) | 89% | 61°C | PID 315057 | c8 importance_s025 |
| **1** | 16.2/97.9 GB (17%) | 71% | 50°C | PID 312143 | c10 lang s020/s025 |
| **2** | 73.3/97.9 GB (75%) | 99% | 63°C | PID 310735 | c8 importance_s015 |
| **3** | 73.3/97.9 GB (75%) | 78% | 59°C | PID 310736 | c8 importance_s020 |

4 块 GPU RTX PRO 6000 Black (98GB) 全部在用。

---

## 1. c8_llama_n250_fixed（GPU 2+3 主脚本，GPU 0 额外补跑）

脚本 `run_c8_llama_n250_fixed.sh` 共 4 轮 8 个 condition，每轮 GPU 2+3 并行。当前是 **Round 1**：

| 条件 | GPU | 进度 | 运行时间 | 预估 |
|------|-----|------|----------|------|
| importance_s015 | 2 | **31/250** (12%) | 48 min | ~6.5h 剩余 |
| importance_s020 | 3 | **33/250** (13%) | 48 min | ~6h 剩余 |
| importance_s025 | 0 (nohup) | **5/250** (2%) | 3 min | 刚启动，预计 ~7h |

三个输出目录均为空（尚未写入结果，profiling 完成后一次性写入）。dryrun 已完成（有 profiling_results.json）。

Round 1 完成后还有 Round 2-4（importance_s025/s030 + random s015/s020/s025/s030），**总计还需约 24-28h**（假设 GPU 0 的 s025 独立完成可减少 1 轮时间）。

---

## 2. c10 lang s020/s025（GPU 1）

- 进度：**15/50** (30%)，已运行 29 min
- 使用 Qwen 模型，每 problem 跑 s020 和 s025 两个条件
- 有些 problem 很快（7-8s），有些很慢（178s 截断到 max tokens）
- 预估剩余：~1-1.5h

---

## 3. c4_v2 think validation（PID 308759）

**已结束**，进程不存在。

---

## 关键风险

- GPU 0 上的 s025 是单独 nohup 启动的，不在 `run_c8_llama_n250_fixed.sh` 脚本里。脚本 Round 2 也会跑 importance_s025（在 GPU 2 上），如果 nohup 的先完成，脚本会检测到 `profiling_results.json` 存在而 SKIP，不会冲突。
- Round 1 按当前速度约 ~1.6 min/problem，250 题约 6.5h。4 轮串行总计约 26h。

---
