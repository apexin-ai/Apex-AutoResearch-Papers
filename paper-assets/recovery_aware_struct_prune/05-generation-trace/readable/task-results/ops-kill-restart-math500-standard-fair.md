# ops kill restart math500 standard fair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_restart_math500_standard_fair_20260518T175109_result.json`
- **Structured JSON:** [`04f2dce28fdd878d208d.json`](../../sessions/04/04f2dce28fdd878d208d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**执行摘要：**
- **Killed**: PID 2261 + tmux session `math500_standard_grpo_fair`（v1 默认 `max_new_tokens=4096`，126/500 花了 4h44m）
- **Interim 数据**: Acc@100 = 36%
- **Restarted**: PID 19616，tmux `math500_standard_grpo_fair`，westd-29022 cuda:1
  - 新增 `--max_new_tokens 2048`，输出 `math500_grpo_standard_20_fair_v2.json`
  - 日志: `~/runs/recovery_aware_struct_prune/math500_standard_grpo_fair_v2.log`
- **Registry** 已更新为 RUNNING，notes 记录了 interim 数据和重启信息

---
