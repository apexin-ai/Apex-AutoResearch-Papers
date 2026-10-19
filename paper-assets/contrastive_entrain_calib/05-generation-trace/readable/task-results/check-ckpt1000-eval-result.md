# check ckpt1000 eval result

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ckpt1000-eval-result_20260520T002220_result.json`
- **Structured JSON:** [`9017e4801f3e1a0ed0ef.json`](../../sessions/90/9017e4801f3e1a0ed0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Eval 仍在运行，尚未产出结果。**

- **进程 171048**：仍存活，已运行 **2小时41分钟**
- **进度**：日志只有 15 行，模型和 NLI 已加载完毕，进入 "Running eval on 362 pairs..." 阶段，但日志中未输出逐条进度（没有 pair 级别的 log），无法确认具体跑到了第几条
- **结果目录** `exp008v3_ckpt1000_eval/` 存在但为空，`default_preset_summary.txt` 尚未生成

**GPU 状态**：

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 76% | 31,376 MiB |
| 1 | 48% | 16,726 MiB |
| 2 | 0% | 5 MiB |
| 3 | 86% | 30,614 MiB |

GPU 0 和 1 有负载，说明 eval 进程在工作中。2小时41分钟跑 362 条偏慢——可能是生成长度较大或单条推理时间长。需要继续等待。

---
