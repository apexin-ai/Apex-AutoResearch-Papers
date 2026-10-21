# ssh alpha4p0 result submit alpha1p0 westd3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_alpha4p0_result_submit_alpha1p0_westd3_20260522T211836_result.json`
- **Structured JSON:** [`12ea097bd39936af48f2.json`](../../sessions/12/12ea097bd39936af48f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Python 进程 79030 正在运行，模型从磁盘加载到 CPU（非均匀 MLP 结构加载较慢），GPU 显存尚未分配。进程状态健康。

```
=== α=4.0 RESULT ===
accuracy=0.266, correct=133, total=500, truncated=190, stderr=0.0198

=== α=1.0 SUBMISSION ===
Status: SUCCESS
PID: 79030 (python), 79021 (bash wrapper)
GPU: westd:3
Log: ~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log
Note: 模型仍在 CPU 加载中（非均匀 MLP, intermediate_size range [8128, 18944]），预计几分钟后开始 GPU 推理
```

---
