# ops launch null s46 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_null_s46_19828_20260521T061439_result.json`
- **Structured JSON:** [`c0fe6738ae1598040c26.json`](../../sessions/c0/c0fe6738ae1598040c26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行中（128 线程，886MB RSS，VmSize 11.9GB）。模型加载中属于正常行为。

实验已成功启动：

- **exp_id**: `alpha_sweep_a000_s46_fp32`
- **PID**: 647969 (bash) → 647974 (python)
- **GPU**: cuda:1 @ westd-19828
- **参数**: Pythia-410M, seed=46, α=0.0, fp32, 10 gen × 5000 steps
- **日志**: `/root/autodl-tmp/distrib_canary_collapse/logs/a000_s46_fp32.log`
- **输出**: `results/alpha_sweep/a000_s46_fp32/`

模型正从 HF cache 加载（fp32，CPU 端分配内存中），加载完毕后会占用 cuda:1 显存并开始训练。

---
