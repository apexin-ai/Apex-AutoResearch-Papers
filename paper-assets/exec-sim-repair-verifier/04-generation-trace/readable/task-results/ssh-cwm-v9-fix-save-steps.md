# ssh cwm v9 fix save steps

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-v9-fix-save-steps_20260512T230435_result.json`
- **Structured JSON:** [`f1f9e2041cb78ba03dc2.json`](../../sessions/f1/f1f9e2041cb78ba03dc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题**：`save_steps=100` + `eval_steps=500` + `load_best_model_at_end=True` 不兼容。transformers 要求 `save_steps` 必须是 `eval_steps` 的整数倍（100 不是 500 的倍数）。

虽然 eval 每 500 步会有对应的 checkpoint（因为 500 是 100 的倍数），但 transformers 的校验逻辑是 `save_steps % eval_steps == 0`，所以拒绝了。

**可选方案**：

1. **禁用 `load_best_model_at_end`**（推荐）— 保持 save_steps=100 + eval_steps=500，训练结束后手动选最优 checkpoint
2. **eval_steps=100** — 恢复原来的值，但 Director 明确要改成 500
3. **save_steps=500** — 但 Director 说 ratchet 策略不可改

方案 1 影响最小：ratchet 策略不变，eval 频率降低，只是训练结束不会自动加载 best model（可通过 eval loss 手动选）。

是否用方案 1 修改脚本并重启？

---
