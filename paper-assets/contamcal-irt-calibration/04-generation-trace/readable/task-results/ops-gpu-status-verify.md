# ops gpu status verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_verify_20260514T040412_result.json`
- **Structured JSON:** [`ed6a52bc46608dee6b8f.json`](../../sessions/ed/ed6a52bc46608dee6b8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 利用率报告 — cqa1-21977

| GPU | 利用率 | 显存 | PID | 实验 | 运行时间 |
|-----|--------|------|-----|------|----------|
| **cuda:0** | 6% | 10055/24564 MiB | 251924 | `exp_001_sft_d100_15B_v2` (train_sft, Qwen2.5-1.5B_d100_s42) | 2h56m |
| **cuda:1** | 51% | 12620/24564 MiB | 249294 | `exp_001_eval_3B_d000_s42` (eval, Qwen2.5-3B_d000_s42) | 3h10m |
| | | | 255322 | `exp_001_eval_05B_d005` (eval, Qwen2.5-0.5B_d005_s42) | 2h36m |
| **cuda:2** | 53% | 7330/24564 MiB | 266521 | `exp_001_eval_05B_d000_s42_v5` (eval, Qwen2.5-0.5B_d000_s42) | 1h25m |
| | | | 266790 | `exp_001_eval_05B_d100_v5` (eval, Qwen2.5-0.5B_d100_s42) | 1h24m |
| **cuda:3** | 19% | 13493/24564 MiB | 242591 | `exp_001_eval_3B_d000_s123` (eval, Qwen2.5-3B_d000_s123) | 3h46m |
| **cuda:4** | **30%** | **18538/24564 MiB** | 271921 | `exp_001_sft_d005_15B` (train_sft, Qwen2.5-1.5B_d005_s42) | **52m** |
| **cuda:5** | 12% | 10365/24564 MiB | 250610 | `exp_001_eval_15B_d000_s123` (eval, Qwen2.5-1.5B_d000_s123) | 3h05m |

**cuda:4 状态：正常运行中。** `exp_001_sft_d005_15B` 已启动 52 分钟，占用 18.5GB 显存，GPU 利用率 30%。之前 report 显示空闲是因为该任务后来才提交。

**全部 6 张 GPU 均在工作，共 8 个进程，无空闲 GPU。**

### 磁盘
| 分区 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| / (根) | 17G | 14G | 56% |
| /root/autodl-tmp | 104G | 66G | 62% |

备注：nvidia-smi 报告的实际 python 子进程 PID 与预期的 bash 包装器 PID 略有偏差（如 266511→266521），这是正常的父子进程关系。所有 8 个任务均确认在运行。

---
