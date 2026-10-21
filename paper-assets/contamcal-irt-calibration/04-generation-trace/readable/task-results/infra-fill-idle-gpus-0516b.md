# infra fill idle gpus 0516b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fill-idle-gpus-0516b_20260516T150520_result.json`
- **Structured JSON:** [`7bfd98764571278b09c8.json`](../../sessions/7b/7bfd98764571278b09c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:3 已占用 17847 MiB，训练正在运行。

## 总结

**GPU 状态**:
| GPU | 状态 | 任务 |
|-----|------|------|
| cuda:0 | 占用 (6.6GB) | 3B signals s4 mmlu (PID 780943) |
| cuda:1 | 占用 (8.3GB) | Llama-3.2-3B d000 aligned eval (PID 800570) |
| cuda:2 | 占用 (1.5GB) | 0.5B-Instruct eval (PID 797754) |
| cuda:3 | **已提交** (17.8GB) | **Llama-3.2-3B d025 SFT** (PID 801761) |
| cuda:4 | 占用 (8.3GB) | Llama-3.2-3B d000 aligned eval (PID 796493) |
| cuda:5 | 占用 (3.9GB) | 1.5B-Instruct para_aligned eval (PID 799315) |

**已提交**:
- `exp_001_sft_llama32_3B_d025_s42` → cuda:3, tmux session `exp_001_sft_llama32_3B_d025_s42`, PID 801761

**注意事项**:
- cuda:1 和 cuda:4 同时跑相同的 Llama-3.2-3B d000_s42 aligned eval（输出到同一目录）。这是重复提交，可能导致数据污染。建议 kill 其中一个（PID 800570 较新）。
- d005 SFT 无法提交，因为没有空闲 GPU。等 cuda:0 或 cuda:5 释放后再提交。

---
