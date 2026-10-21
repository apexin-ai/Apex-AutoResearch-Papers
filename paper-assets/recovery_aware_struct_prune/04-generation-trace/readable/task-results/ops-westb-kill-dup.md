# ops westb kill dup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-kill-dup_20260515T144402_result.json`
- **Structured JSON:** [`0c51f5640780e8828e62.json`](../../sessions/0c/0c51f5640780e8828e62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 534974 已 kill，但 PID 534667 也不在了——GPU 1 上现在**零进程**，只有 GPU 0 的 RASP v8（PID 532861）在跑。

状态：
- **GPU 0**: PID 532861 (RASP v8), 76.8GB/97.9GB, 99% util — 正常运行
- **GPU 1**: 3MiB, 空闲 — 534667 和 534974 都已退出
- Standard v8 日志显示刚开始加载 pruned model（`Loading pruned model from /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20`），说明 534667 可能因 534974 的 OOM 竞争已经崩了，或者两个进程绑定了同一个 PID group 被一起终止

Standard v8 需要在 GPU 1 上重新启动。

---
