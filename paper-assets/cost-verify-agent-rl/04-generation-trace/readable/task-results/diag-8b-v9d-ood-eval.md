# diag 8b v9d ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_8b_v9d_ood_eval_20260520T095705_result.json`
- **Structured JSON:** [`f1703671de8849d71ffc.json`](../../sessions/f1/f1703671de8849d71ffc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**: 配置问题，非代码 bug。OOD eval 是 `val_only: True` 模式，但 `train.py:163` 的 config validation 不区分 val-only，仍校验 train batch size 约束：

- `es_manager.train.env_groups(1) × group_size(2) × effective_ratio(1.0) = 2.0`
- `ppo_mini_batch_size = 4`
- `2.0 < 4` → assertion 失败

**修复**: 在 `_alfworld_8b_v9d_ood_eval.yaml` 中设 `ppo_mini_batch_size: 2`（val-only 模式下该值无实际影响）。报告已写入 `artifacts/8b_v9d_ood_eval/diag_failure.md`。

---
