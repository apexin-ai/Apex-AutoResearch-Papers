# ops verify eval pids westd34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_eval_pids_westd34685_20260523T203727_result.json`
- **Structured JSON:** [`9dfb239e446a3160700e.json`](../../sessions/9d/9dfb239e446a3160700e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 eval 都在正常运行，但日志写到了 `/tmp/` 而非 `/root/runs/`**（`/root/runs/` 下的日志是启动时参数报错的旧日志）。

| Eval | 父 PID | Python PID | GPU | 进度 |
|------|--------|-----------|-----|------|
| **cutoff_25k_s0** | 463144 | **463150** | GPU 3 | T2: 40% (20/50), ~4.6s/it |
| **reverse_cutoff_s0** | 464449 | **464454** | GPU 2 | T2: 16% (8/50), ~4.9s/it |

**GPU 状态**:
- GPU 0: 99% util, 63GB/98GB — 有其他任务占用
- GPU 1: 53% util, 63GB/98GB — 有其他任务占用
- GPU 2: 1% util, 17GB/98GB — reverse_cutoff eval（GPU 利用率低是因为 LIBERO 仿真 CPU-bound）
- GPU 3: 0% util, 16GB/98GB — cutoff_25k eval

两个 eval 均已正常启动（去掉了 `--num_trials_per_task 50` 参数），正在跑 Task 2 的 rollouts。实际日志路径是 `/tmp/cutoff_25k_s0_eval.log` 和 `/tmp/reverse_cutoff_s0_eval.log`。

---
