# code bce 30pct s42 train

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bce-30pct-s42-train_20260518T151012_result.json`
- **Structured JSON:** [`8da3800b096f0cc8e62c.json`](../../sessions/8d/8da3800b096f0cc8e62c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法提交：westd-41718 两张 GPU 都被占满。**

当前状态：
- **GPU 0** (PID 79351): `train_bce_kl_targets.py` — C1 ablation, 88366 MiB
- **GPU 1** (PID 80126): `train_bce_kl_targets.py` — 同样的 C1 ablation 命令, 88366 MiB

两个进程参数完全一致（同 output_dir、同 seed），看起来是 C1 ablation 被重复提交了两次，分别占了两张卡。

**建议：**
1. 确认是否其中一个是误启动的重复任务，如果是，kill 掉一个释放 GPU 0
2. 或者等其中一个完成后再提交 BCE 30%

需要 kill 其中一个重复进程吗？

---
