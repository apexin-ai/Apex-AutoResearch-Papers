# ops cleanup gpu check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_gpu_check_20260516T003438_result.json`
- **Structured JSON:** [`b6c74363c6108576a824.json`](../../sessions/b6/b6c74363c6108576a824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### Kill 结果
- PID 182573 (diag_hflm.py) — **已 kill**
- PID 182747 (diag_hflm.py) — **已 kill**
- PID 184120 (debug_mask_verify.py) — **已 kill**

### GPU 当前状态

| GPU | 显存占用 | 显存总量 | GPU 利用率 | 运行进程 |
|-----|---------|---------|-----------|---------|
| cuda:0 | 21,255 MiB | 97,887 MiB | 90% | PID 181121 — `eval_benchmark.py --condition mistral_dense` (21,246 MiB) |
| cuda:1 | 37,660 MiB | 97,887 MiB | 94% | PID 174850 — `eval_benchmark.py --condition mistral_kl_s42` (21,280 MiB) + PID 179918 — `lm_eval_sparse.py` kl_s42 rerun (16,364 MiB) |

### lm_eval 进程状态
三个评估任务正在运行：

1. **PID 179918** — `lm_eval_sparse.py` (kl_s42, arc/wino/mmlu/gsm8k, sparsity=0.5) — **仍在跑**，cuda:1，CPU 95.3%
2. **PID 174850** — `eval_benchmark.py --condition mistral_kl_s42` — cuda:1，CPU 100%
3. **PID 181121** — `eval_benchmark.py --condition mistral_dense` — cuda:0，CPU 100%

### tmux sessions
- `lm_eval_kl_s42` (07:52)
- `lm_eval_mistral_dense` (08:04)
- `lm_eval_mistral_downstream` (07:34)

另有一个 `lm_dense` tmux session (PID 163716) 也在 ps 中出现，但未占用 GPU 显存（可能已完成或在等待）。

### GPU 空闲情况
- **cuda:0**: 占用 ~21 GB / 98 GB，剩余 ~76 GB — **有空间安排新实验**
- **cuda:1**: 占用 ~38 GB / 98 GB，剩余 ~60 GB — **有空间但当前跑着两个评估任务**

两张卡都有充足剩余显存，但 GPU 利用率都在 90%+ 。建议等当前评估任务完成后再安排新的计算密集型实验，或者如果新实验显存需求不大（<60 GB），可以与现有任务共存。

---
