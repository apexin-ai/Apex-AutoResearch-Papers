# fix gemma2 s0 dedup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gemma2-s0-dedup_20260520T095141_result.json`
- **Structured JSON:** [`f92152286c3e89310042.json`](../../sessions/f9/f92152286c3e89310042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇报：

| 项目 | 状态 |
|------|------|
| **PID 315220** | 已杀（原重复进程） |
| **PID 317029** | 已杀（额外发现的 d025_s0 进程，PPID 315214，来自 `sft_gemma2_s0_sweep_v2` tmux session） |
| **tmux `sft_gemma2_s0_sweep_v2`** | 已杀 |
| **PID 314035** | 存活，GPU 1 独占，95234MiB / 97887MiB，Util 94% |
| **训练进度** | step 81/3125（~2.6%），~2.7s/it，LoRA r=16 alpha=32，d000_s0 |
| **checkpoint 目录** | `gemma-2-9b_d000_s0/lora_adapter/` 已创建，无异常 |

GPU 1 现在只有 314035 一个进程，训练正常推进。

---
