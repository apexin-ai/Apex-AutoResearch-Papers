# fix transformers patch and eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_transformers_patch_and_eval_20260516T132432_result.json`
- **Structured JSON:** [`1aac954b41452385d304.json`](../../sessions/1a/1aac954b41452385d304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果：

**nominal (routing=none, openpi wrapper): 0/5 = 0.0%**

每个 episode 都跑满 220 步后 FAIL。所有 5 个 episode 全部失败。

这表明 openpi wrapper 推理有问题 — 模型加载成功了，但 action 输出可能不正确（norm stats 缺失警告、或 action 格式/delta 问题）。

关键线索：
1. `Norm stats not found in .../physical-intelligence/libero, skipping` — 可能缺少关键的 norm stats
2. 每个 episode 恰好跑满 max_steps=220 — 说明 action 在输出但没有实际让机器人完成任务

需要排查：是否需要加 `--no_delta_actions` 参数，或者 norm stats 路径配置问题。要继续调试吗？

---
