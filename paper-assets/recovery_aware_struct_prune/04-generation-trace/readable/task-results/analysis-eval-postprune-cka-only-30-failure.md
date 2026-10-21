# analysis eval postprune cka only 30 failure

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849_result.json`
- **Structured JSON:** [`c66f2d711d17b6f5c2a6.json`](../../sessions/c6/c66f2d711d17b6f5c2a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### 1. eval_postprune_cka_only_30 — 未失败，仍在运行

进程仍活跃 (PID 59408, 105% CPU, cuda:2)，当前进度 **56/200**。

日志中 sample 35 处出现 `Terminated` 字样，但进程并未退出，eval 继续运行到了 56。可能是同 GPU 上之前的某个进程被 kill。

关键指标（50/200 中间报告）：
- **acc = 0.0000**（零准确率）
- eos_rate = 4.00%
- avg_len = 4024（几乎全部 max out）

CKA-only 30% 剪枝后模型在 GSM8K 上完全丧失数学能力。

### 2. eval_math500_grpo_unpruned — 运行中

- 在 westd-11672 cuda:2 上运行（PID 64472, 07:09 启动）
- 当前进度 **11/500**
- 模型 `grpo_unpruned_v2/` 加载成功
- 结果文件尚未生成

### ⚠️ GPU 冲突

eval_postprune_cka_only_30 和 eval_math500_grpo_unpruned **都在 cuda:2 上**。这解释了 cka_only_30 在 sample 35 后速度从 ~95s/it 骤降到 ~48-90s/it。两个 eval 互相争抢显存和算力，都会变慢。

---
