# ops fix westd eval v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-westd-eval-v2_20260515T192432_result.json`
- **Structured JSON:** [`2a0aeacc77d45b898124.json`](../../sessions/2a/2a0aeacc77d45b898124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡 eval 运行正常：

| 实验 | GPU | 显存占用 | 状态 |
|------|-----|---------|------|
| eval_sft_rasp_20_westd_n100 | cuda:0 | 12497 MiB | 加载 GSM8K，即将开始推理 |
| eval_sft_standard_20_westd_n100 | cuda:1 | 12689 MiB | 已在推理中（1/100, ~2.3s/it, 预计 ~4 分钟） |

**修复内容**：前两次失败分别因 `apply_chat_template` 缺失和 `src/eval_gsm8k.py not found`。这次根因是 westd-11672 上 conda 环境的 `python` 不在 PATH 中（只有 `/root/miniconda3/bin/python`），改用绝对路径 + 显式 `cd /root/recovery_aware_struct_prune` 解决。

Registry 已更新为 RUNNING，retry_count=2。

---
