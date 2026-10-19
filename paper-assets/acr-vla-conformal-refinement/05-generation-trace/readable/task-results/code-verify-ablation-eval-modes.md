# code verify ablation eval modes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-ablation-eval-modes_20260514T212546_result.json`
- **Structured JSON:** [`a70860afcbe5a5c2ef63.json`](../../sessions/a7/a70860afcbe5a5c2ef63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。结论：

**evaluate.py 中 `crm_obs_only` 和 `crm_scalar` 两个 mode 已完整实现，无需修改。** 具体验证：

- `--mode` choices 已包含两者
- CRM 加载时 `uncertainty_dim` 映射与 train_crm.py 完全一致（obs_only→0, scalar→3, full→40）
- `select_action_crm()` 中根据 mode 正确处理 uf：obs_only 传 None，scalar 调 `_to_scalar_uf()` 压缩为 3D
- CRM forward 的 None 分支（跳过 uncertainty 拼接）与训练时行为一致

三个可直接执行的 eval 命令已写入 `artifacts/ablation_eval_commands.md`。

---
