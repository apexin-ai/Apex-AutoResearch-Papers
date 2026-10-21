# ops full gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_gpu_status_check_20260514T020340_result.json`
- **Structured JSON:** [`1ad12e238ba9a22e6bfe.json`](../../sessions/1a/1ad12e238ba9a22e6bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整状态报告

### GPU 状态 (6x A5000 24GB)

| GPU | 显存使用 | 利用率 | 主要进程 |
|-----|---------|--------|---------|
| 0 | 13716/24564 MiB | 78% | SFT train (251924) + eval 0.5B rerun (257853) |
| 1 | 12620/24564 MiB | 100% | eval 3B_d000_s42 (249294) + 另一python进程 |
| 2 | 10993/24564 MiB | 99% | eval 0.5B_d000_s42 (257034) + 其他2个python进程 |
| 3 | 8957/24564 MiB | 62% | eval 3B_d000_s123 (242591) |
| 4 | 9492/24564 MiB | 99% | eval 1.5B_d000_s42 (243300) + 另一python进程 |
| 5 | 5829/24564 MiB | 47% | eval 1.5B_d000_s123 (250610) |

### 进程状态 — 全部 ALIVE

| PID | 实验 | 运行时间 | 当前进度 | 预计剩余 |
|-----|------|---------|---------|---------|
| 251924 | **SFT 1.5B d100 v2** (cuda:0) | 55min | step 1022/4159 (25%), loss=1.30 | ~2h47m |
| 249294 | eval 3B_d000_s42 (cuda:1) | 1h10m | GSM8K 460/1319 (35%) | ~2.5h |
| 242581 | eval 3B_d000_s123 (cuda:3) | 1h46m | GSM8K 752/1319 (57%) | ~2h |
| 243290 | eval 1.5B_d000_s42_v2 (cuda:4) | 1h41m | GSM8K 920/1319 (70%) | ~1.5h |
| 250600 | eval 1.5B_d000_s123 (cuda:5) | 1h05m | GSM8K 236/1319 (18%) | ~3h |
| 257848 | eval 0.5B_d000_s42 rerun (nohup, cuda:0) | 24min | GSM8K 223/1319 (17%) | ~2.5h |

额外发现的 evaluate.py 进程：
- **PID 257034** (cuda:2): 0.5B_d000_s42 第二个实例，已跑 30min
- **PID 255078**: 0.5B_d100_s42，已跑 31min

### 结果文件状态

| 配置 | 结果文件 | 状态 |
|------|---------|------|
| **Qwen2.5-0.5B_d000_s123** | eval_results.json | **已完成** |
| Qwen2.5-0.5B_d000_s42 | 空目录 | 运行中（2个重复进程） |
| Qwen2.5-0.5B_d100_s42 | 空目录 | 运行中 |
| Qwen2.5-0.5B_d005_s42 | 空目录 | **未发现运行进程** |
| Qwen2.5-3B_d000_s42 | 空目录 | 运行中 |
| Qwen2.5-3B_d000_s123 | 空目录 | 运行中 |
| Qwen2.5-1.5B_d000_s42 | 空目录 | 运行中 |
| Qwen2.5-1.5B_d000_s123 | 空目录 | 运行中 |

### 已完成 Eval Metrics — Qwen2.5-0.5B_d000_s123

| Benchmark | Score |
|-----------|-------|
| MMLU | **0.4182** |
| GSM8K | **0.3404** |
| ARC-Challenge | **0.3976** |
| HumanEval (pass@1) | **0.1037** |

### 问题提示

1. **0.5B_d000_s42 有两个重复的 eval 进程**（PID 257034 on cuda:2 和 PID 257853 on cuda:0），会写入同一 output-dir，存在冲突风险
2. **0.5B_d005_s42 目录存在但无运行进程**，需要确认是否需要启动
3. **GPU 0 同时跑 SFT 训练和 eval**，可能互相影响性能（78% vs 其他 GPU 99-100%）
4. 所有进程的 bitsandbytes 报 `libnvJitLink.so.13` 错误（非致命，不影响 eval）

---
