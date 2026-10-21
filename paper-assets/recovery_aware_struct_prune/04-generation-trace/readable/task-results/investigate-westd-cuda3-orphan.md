# investigate westd cuda3 orphan

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_westd_cuda3_orphan_20260519T024658_result.json`
- **Structured JSON:** [`7fe031d0b495b6d3b5b8.json`](../../sessions/7f/7fe031d0b495b6d3b5b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

**结论：有效实验，非 orphan。**

- PID 59413 正在 cuda:3 上运行 GSM8K 评估（grpo_standard_20_extended_300 模型），29610 MiB 显存，99% GPU 利用率
- 在 tmux session `eval_gsm8k_standard_300` 中运行，启动于 10:18
- 进度 207/1319 (16%)，accuracy 0.63，预计还需 ~74 min
- 仅因未注册到 registry 被 reconcile_crons 标记

建议保留，让评估自然完成后补录 registry。报告已写入 `artifacts/westd_cuda3_investigation.md`。

---
