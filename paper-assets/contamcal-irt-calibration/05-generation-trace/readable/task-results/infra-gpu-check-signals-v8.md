# infra gpu check signals v8

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-signals-v8_20260515T234155_result.json`
- **Structured JSON:** [`ee529e69452ad34e90f7.json`](../../sessions/ee/ee529e69452ad34e90f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. GPU 占用情况
| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 23258/24564 MiB | 95% | PID 642763 (eval d100_a32_s123), PID 643167 |
| 1 | 13341/24564 MiB | 74% | PID 628668 |
| 2 | 7537/24564 MiB | 59% | PID 652259 (signals d005_s123, v7) |
| 3 | 8985/24564 MiB | 69% | PID 655989 (eval d025_v3_s42) |
| **4** | **0/24564 MiB** | **0%** | **空闲 → 已提交 v8** |
| 5 | 18665/24564 MiB | 64% | PID 633041 |

### 2. cuda:3 d025_v3_s42 eval 进程
**活着**。PID 655989，tmux session `exp_001_eval_3B_d025_v3_s42_batch`，07:22 启动，正在跑 aligned eval（mmlu gsm8k arc_challenge）。

### 3. s123 checkpoint 验证
| Checkpoint | 存在 | lora_alpha | 可用 |
|-----------|------|-----------|------|
| d000_s123 | ✓ | 32 | ✓ |
| d025_s123 | ✓ | 32 | ✓ |
| d100_s123 | ✓ | **16** | **✗ C006 禁止** |
| d100_a32_s123 | ✓ | 32 | ✓ (替代使用) |

### 4. signals v8 提交结果
**成功**。PID 659053，cuda:4，tmux session `exp_002_signals_3B_v8`。

覆盖 dose：d025_s123 + d100_a32_s123 × {mmlu, gsm8k, arc_challenge}，ref=d000_s123。Registry 已更新为 RUNNING。

---
