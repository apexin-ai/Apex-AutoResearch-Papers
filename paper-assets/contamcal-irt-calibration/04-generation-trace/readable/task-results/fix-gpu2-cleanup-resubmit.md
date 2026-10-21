# fix gpu2 cleanup resubmit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu2_cleanup_resubmit_20260514T023435_result.json`
- **Structured JSON:** [`6f3651e774d57e4c6991.json`](../../sessions/6f/6f3651e774d57e4c6991.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

### 汇报

**1. GPU 2 清理前后**
- 清理前：6 个重复 evaluate.py 进程（PID 262857/263538/264255/262940/263794/264334）
- 清理后：kill 全部 → nvidia-smi 确认 GPU 2 显存占用为 0

**2. 两个实验 PID**

| 实验 | exp_id | PID |
|------|--------|-----|
| d000_s42 | exp_001_eval_05B_d000_s42_v4 | 265362 (GPU 子进程 265372) |
| d100_s42 | exp_001_eval_05B_d100_v4 | 265684 (GPU 子进程 265694) |

**3. GPU 2 最终状态：2 个进程**
- PID 265372: 3658 MiB (d000_s42 eval)
- PID 265694: 1492 MiB (d100_s42 eval)

**4. 无重复进程确认**：严格串行提交——先提交 d000_s42 并验证 GPU 2 仅 1 个进程后，才提交 d100_s42。最终 GPU 2 恰好 2 个进程，无重复。

---
