# diagnose eval mbpp grpo shortgpt 20 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mbpp_grpo_shortgpt_20_v2_20260519T223652_result.json`
- **Structured JSON:** [`15028bdcbe9bd315fb54.json`](../../sessions/15/15028bdcbe9bd315fb54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因：工作目录错误。**

提交命令用相对路径 `src/eval_mbpp.py`，但 cwd 是数据盘 `/root/autodl-tmp/recovery_aware_struct_prune/`，Python 找不到 `/root/autodl-tmp/recovery_aware_struct_prune/src/eval_mbpp.py`。实际脚本在 `/root/recovery_aware_struct_prune/src/eval_mbpp.py`。

**修复**：命令中加 `cd /root/recovery_aware_struct_prune &&`，或将 `src/eval_mbpp.py` 改为绝对路径 `/root/recovery_aware_struct_prune/src/eval_mbpp.py`。

诊断报告已写入 `artifacts/diagnose_eval_mbpp_grpo_shortgpt_20_v2.md`。

---
