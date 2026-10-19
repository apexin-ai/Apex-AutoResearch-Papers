# diag eval v6 batch failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-v6-batch-failure_20260513T233517_result.json`
- **Structured JSON:** [`8b5e7c97dd80e2017f51.json`](../../sessions/8b/8b5e7c97dd80e2017f51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：三个实验同一原因 — `evaluate.py:203` 的 warm-up 循环 `env.step(np.zeros(7))` 在 robosuite 环境处于 terminated 状态时未做保护，直接抛出 `ValueError: executing action in terminated episode`。

**原因细节**：`set_init_state()` 不清除 robosuite 的 `done` 标志。首次 rollout 时 env 创建后未 reset（vla_only 和 reconvla 在第一个 rollout 就崩）；后续 rollout 时前一轮的 `done=True` 残留（acr_vla 在第 6 个 rollout 崩）。

**修复**：`evaluate.py` 第 201 行，在 `set_init_state()` 前加一行 `env.reset()`。

报告已保存到 `artifacts/diag-eval-v6-batch-failure.md`。

---
