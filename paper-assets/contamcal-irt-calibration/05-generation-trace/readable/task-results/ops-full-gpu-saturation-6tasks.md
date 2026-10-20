# ops full gpu saturation 6tasks

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-saturation-6tasks_20260515T110444_result.json`
- **Structured JSON:** [`761a2d09097b91e79f52.json`](../../sessions/76/761a2d09097b91e79f52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**3 个 GPU 被占用，停止提交。**

| GPU | PID | 运行时间 | 进程 |
|-----|--------|---------|------|
| **0** | 549516 | 42 min | `train_sft.py` 1.5B d025 s123 → `checkpoints/Qwen2.5-1.5B_d025_s123` — **正是本次要提交的任务** |
| **2** | 530893 | 2h20m | `evaluate.py` 0.5B base pretrained → `eval_results/Qwen2.5-0.5B_base_pretrained`（无 `_aligned` 后缀，与本次请求的 `_aligned` 目录不同） |
| **4** | 530975 | 2h20m | `evaluate.py` 1.5B base pretrained → `eval_results/Qwen2.5-1.5B_base_pretrained`（同上，无 `_aligned`） |

**空闲 GPU：1、3、5**

需要确认：
1. **GPU 0**：已在跑完全相同的 SFT 任务，是否跳过不再重复提交？
2. **GPU 2/4**：正在跑的 eval 输出到不带 `_aligned` 的目录。要等它们完成后再提交 `_aligned` 版本？还是 kill 后重新提交？
3. 是否先用空闲的 GPU 1/3/5 提交 3 个任务（d005 s123 SFT + GPU 4/5 的 checkpoint eval）？

---
