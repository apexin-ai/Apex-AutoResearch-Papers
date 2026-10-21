# check cuda1 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda1_status_20260515T190645_result.json`
- **Structured JSON:** [`d2b6db5026f3a1c6c3e7.json`](../../sessions/d2/d2b6db5026f3a1c6c3e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 项目 | 状态 |
|------|------|
| **cuda:1** | **空闲** — 2MiB 显存、0% 利用率，无任何进程 |
| **seed123** | **已完成** — 进程不在，输出目录已存在（`samples.jsonl` 7MB, `ablation_report.json`, `run_summary.json`，最后写入 02:40） |
| **当前占用** | 只有 **cuda:2** 在跑：PID 220580 `run_freeform_inference.py --seed 456 --num_samples 8`，对应 VLLM 引擎 PID 220875（30340MiB，100% 利用率），tmux session `exp_001_n16_seed456` |
| **cuda:1 可分配** | **是**，可立即使用 |

cuda:0 和 cuda:3 也都空闲（均 2MiB / 0%）。

---
