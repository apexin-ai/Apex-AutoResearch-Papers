# ssh westb gpu0 reset

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_gpu0_reset_20260522T205341_result.json`
- **Structured JSON:** [`1f0ab32294d5a48a7974.json`](../../sessions/1f/1f0ab32294d5a48a7974.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU:0 reset: FAILED (nvidia-smi --gpu-reset -i 0 返回 "Not Supported"，该 GPU 硬件/驱动不支持在线 reset)
GPU:1 MF3 status: OK (PID 220343, eval_gsm8k.py, 运行 5h45m, 16538 MiB, 状态 Rl)
Post-reset GPU state: 未变化
  GPU:0: 100% util, 0 MiB, 无进程 (异常持续)
  GPU:1: 99% util, 16547 MiB, PID 220343 (正常)
```

GPU:0 的 `nvidia-smi --gpu-reset` 在这台机器上不被支持（所有 PCIe 地址的 GPU 均返回 "Not Supported"）。这是 AutoDL 虚拟化/驱动层的限制，非权限问题。

要恢复 GPU:0，可能需要**重启实例**（但会中断 GPU:1 上的 eval 任务）或**联系 AutoDL 客服**请求 GPU 级别 reset。建议等 GPU:1 的 eval_gsm8k.py 跑完后再重启。

---
