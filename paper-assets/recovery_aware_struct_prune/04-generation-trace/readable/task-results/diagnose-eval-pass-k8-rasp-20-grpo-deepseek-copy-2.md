# diagnose eval pass k8 rasp 20 grpo deepseek

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pass_k8_rasp_20_grpo_deepseek_20260517T004128_result.json`
- **Structured JSON:** [`58f785eeedd7b3a84113.json`](../../sessions/58/58f785eeedd7b3a84113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，未失败。**

进程 PID 61473 活跃中（114% CPU，已运行 44 分钟）。Cron 误判原因：eval 脚本不写 W&B 也不写 sentinel，进程检查逻辑无法识别正在运行的 eval job。

当前状态：
- 进度：63/200 (32%)，中间 pass@8 = 0.84（50 题时的 checkpoint）
- 启动时间：08:03，log 最后更新：08:38
- 速度：多数 14-25s/it，但 items 35-40 有异常减速（125-171s/it），之后恢复正常
- 预计剩余：约 60-80 分钟完成

JSON 尚未生成是正常的，脚本在全部 200 题评完后才写入。无需干预，等待自然完成即可。

---
