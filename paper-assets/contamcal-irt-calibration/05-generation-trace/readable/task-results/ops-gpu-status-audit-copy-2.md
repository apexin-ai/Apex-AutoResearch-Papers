# ops gpu status audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-audit_20260516T035815_result.json`
- **Structured JSON:** [`d9008c16904bb6a3a360.json`](../../sessions/d9/d9008c16904bb6a3a360.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both d000_s42 和 d005_s42 的 adapter 确认 lora_alpha=32，合规。汇总如下：

## GPU 运行状态

| GPU | PID | 进程命令（关键参数） | 进度估计 | 显存占用 |
|-----|-----|---------------------|---------|---------|
| **0** | 691033 | `evaluate.py` 3B d025_v3_s42 → para_aligned (mmlu/gsm8k/arc/humaneval) | 运行中，输出目录无 eval_results.json | 9008 MiB |
| **0** | 691887 | `compute_signals.py` **1.5B d000_s123** mmlu signal=all | s1✅ s2✅，当前推测在跑 s3/s4 | 3996 MiB |
| **1** | 676497 | `evaluate.py` 3B d000_s42 → a32_aligned (mmlu/gsm8k/arc/humaneval) | 运行中，输出目录无 eval_results.json | 8976 MiB |
| **2** | 679190 | `evaluate.py` 3B d005_s42 → a32_aligned (mmlu/gsm8k/arc/humaneval) | 运行中，输出目录无 eval_results.json | 8976 MiB |
| **3** | 687347 | `evaluate.py` 3B d100_a32_s42_v3 → a32_aligned (mmlu/gsm8k/arc/humaneval) | 运行中，输出目录无 eval_results.json | 8976 MiB |
| **4** | 689315 | `compute_signals.py` **3B d100_a32_s123** mmlu signal=**s4** (ref=d000_s123) | s1✅ s2✅ s4 进行中 (3/? chunks) | 6566 MiB |
| **5** | 687036 | `compute_signals.py` **0.5B d000_s123** mmlu signal=all | s1✅ s2✅ s4 进行中 (5 chunks) | 1728 MiB |

**总显存**: 56897 / 147384 MiB (全部 6 卡均在用)

---

## Signals 完成状态

| 模型 | s1_embedding | s2_minkpp | s3 | s4_logit_diff |
|------|-------------|-----------|-----|---------------|
| **0.5B d000_s123** (cuda:5) | ✅ | ✅ | 未见文件 | 进行中 (5 chunks: 0-5000) |
| **1.5B d000_s123** (cuda:0) | ✅ | ✅ | 未见文件 | 未见文件 |
| **3B d100_a32_s123** (cuda:4) | ✅ | ✅ | 未见文件 | 进行中 (3 chunks: 0-3000) |

## Eval 完成状态

当前 4 个 eval 进程 **均未产出** eval_results.json（d025_v3_s42_para_aligned、d000_s42_a32_aligned、d005_s42_a32_aligned、d100_a32_s42_aligned 目录下均无结果文件），全部仍在运行。

已完成的 eval 结果（部分关键条目）：
- 3B d025_v3_s42_aligned ✅ / d000_s42_para_aligned ✅ / d005_s42_para_aligned ✅ / d100_a32_s123_aligned ✅ / d100_a32_s123_para_aligned ✅

## 异常与注意事项

1. **无僵尸进程** — 所有 7 个进程都在活跃运行，无已完成仍占 GPU 的情况
2. **C006 合规** — d000_s42 和 d005_s42 的 adapter 已确认 lora_alpha=32
3. **C007 优先级** — 0.5B s123 (cuda:5) 和 1.5B s123 (cuda:0) 正在跑，d100_a32_s123 (cuda:4) 排第三，符合优先级
4. **cuda:0 双进程共存** — eval (9008 MiB) + signals 1.5B (3996 MiB) 共占 13018/24564 MiB，GPU-Util 96%，可能互相拖慢

---
