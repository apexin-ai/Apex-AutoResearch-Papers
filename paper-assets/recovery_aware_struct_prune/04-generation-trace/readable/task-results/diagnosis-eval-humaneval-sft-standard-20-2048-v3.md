# diagnosis eval humaneval sft standard 20 2048 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_eval_humaneval_sft_standard_20_2048_v3_20260519T135424_result.json`
- **Structured JSON:** [`e9cec51450a4dce7fc13.json`](../../sessions/e9/e9cec51450a4dce7fc13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断摘要：

**实验并未失败，实际已完成。** 进程正常跑完 164 题（耗时 ~4h），结果已写入 JSON 文件，但 eval 脚本没有写 sentinel 文件，导致 cron 监控 5 次检测不到存活信号后误判为 failed。

**结果：pass@1 = 13.41%** (22/164)
- 对比同模型上一轮 v2（不同 checkpoint `sft_standard_20_westd`）：11.59% → 13.41%，略有提升
- median response length = 2048，大量回答撞到 token 上限——模型倾向于输出自然语言推理（"Okay, I need to..."）而非直接写代码，截断后产生 SyntaxError

**根因**：监控误报，非实验本身失败。eval 脚本缺少 sentinel/heartbeat 机制是监控盲区。

---
