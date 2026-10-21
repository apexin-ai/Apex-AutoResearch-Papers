# diagnose exp 002v3 failure

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-002v3-failure_20260519T180703_result.json`
- **Structured JSON:** [`c63d65e3ce39c7874e82.json`](../../sessions/c6/c63d65e3ce39c7874e82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断总结：

**错误**: `TypeError: DCGRPOTrainer.compute_rewards() takes 5 positional arguments but 7 were given`

**根因**: `run_exp002v3_dcgrpo_scaled_cosine.py:77` 的 `Exp002v3Trainer.compute_rewards()` 在调用 `super().compute_rewards()` 时传了 `r1_ema` 和 `ema_alpha` 两个额外参数，但服务器上的 `dcgrpo_trainer.py` 已移除了这两个参数。代码版本不同步，第一个训练步就崩溃。

**修复**: 修改 `run_exp002v3_dcgrpo_scaled_cosine.py:77`，将 `super().compute_rewards(completions, conditions, pair_ids, batch_activations, r1_ema, ema_alpha)` 改为 `super().compute_rewards(completions, conditions, pair_ids, batch_activations)`。同时检查 `dcgrpo_trainer.py:185` 的 `_DCRewardCallable.__call__` 是否也传了多余参数。

**不可直接重试，需修代码后重新部署。**

---
