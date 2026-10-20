# ops disk cleanup approved

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-approved_20260515T124641_result.json`
- **Structured JSON:** [`2f1ed14c2dfccafe7a0e.json`](../../sessions/2f/2f1ed14c2dfccafe7a0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成

**磁盘使用量对比：**
| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 217G | 34G | 87% |
| 清理后 | 174G | 77G | 70% |
| **释放** | **43G** | | |

**删除清单：**

| 文件/目录 | 大小 | 原因 |
|---|---|---|
| `plan009_sft_baseline_s42_1000/checkpoint-1000/optimizer.pt` | 15G | eval 不需要 optimizer |
| `plan009_sft_baseline_s42_1000/checkpoint-1000/scheduler.pt` | 1.5K | eval 不需要 |
| `plan009_sft_baseline_s42_1000/checkpoint-1000/rng_state.pth` | 15K | eval 不需要 |
| `plan018_additive_random_b01_s42_1000_r3/checkpoint-1000/` (整目录) | ~16G | 顶层已有完全相同的模型权重 |
| 4 个空目录 (exp1_isr_b03_s43_r4, exp1_random_b03_s43_eval, exp1_random_b03_s43_r3, plan015_linear_s42) | 0 | 空 |

**保留完好：** 所有 model.safetensors、eval 结果、plan002 checkpoint（re-eval）、plan009 checkpoint 模型权重（eval）、基础模型 Qwen3-4B。

**注意：** 发现两个新目录 `plan009_sft_baseline_s43_1000` (23G) 和 `plan009_sft_baseline_s44_1000` (0)，清理前不存在，可能是其他进程创建的。

---
