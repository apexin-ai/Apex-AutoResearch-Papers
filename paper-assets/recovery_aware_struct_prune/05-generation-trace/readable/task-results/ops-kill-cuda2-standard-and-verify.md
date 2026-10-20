# ops kill cuda2 standard and verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_cuda2_standard_and_verify_20260519T064331_result.json`
- **Structured JSON:** [`07a2cc8aae7c86a9e9d8.json`](../../sessions/07/07a2cc8aae7c86a9e9d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 中不存在 `eval_humaneval_grpo_standard_20_fair_2048_v2`，无需更新。

---

## 最终状态确认

4 张 GPU 全部正常，无冲突：

| GPU | PID | 任务 | 模型路径 | 状态 |
|-----|-----|------|---------|------|
| cuda:0 | 56151 | MATH-500 SFT Standard | `sft_standard_20` | 98% util, 正常 |
| cuda:1 | 66531 | HumanEval GRPO CKA-only | `grpo_cka_only_20` | 99% util, 正常 |
| cuda:2 | 63783 | HumanEval SFT CKA-only | `sft_cka_only_20` | 96% util, 正常（无冲突） |
| cuda:3 | 74303 | HumanEval GRPO RASP fair | `grpo_stage2_rasp_20_fair` | 91% util, 正常 |

**RASP fair 路径验证**: 使用的是 `grpo_stage2_rasp_20_fair`（正确路径），不是 `grpo_rasp_20_fair`。

**冲突处理**: tmux session `eval_humaneval_standard_fair` 已不存在（可能已被提前杀掉或未以 tmux 启动），cuda:2 当前仅有 SFT CKA-only 一个进程，冲突已解除。

**Registry**: `eval_humaneval_grpo_standard_20_fair_2048_v2` 不在 registry 中，无需标记。

---
