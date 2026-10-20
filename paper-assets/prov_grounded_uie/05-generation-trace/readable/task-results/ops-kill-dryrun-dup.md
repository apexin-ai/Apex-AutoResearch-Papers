# ops kill dryrun dup

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_dryrun_dup_20260513T002843_result.json`
- **Structured JSON:** [`ad3b0422a29044f10b2a.json`](../../sessions/ad/ad3b0422a29044f10b2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

- PID 70349、70829 两个 grpo_pilot_v2 dryrun 进程已终止，释放了 ~64GB 显存
- GPU 0 现在只剩 PID 71816（sft_eval_v5），占用 26618MiB
- 另有一个 `merge_grpo_lora.py`（PID 72501）在 CPU 上运行（`CUDA_VISIBLE_DEVICES=""`），不占 GPU

---
