# eval d154 8b exec s42 k8

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d154-8b-exec-s42-k8_20260522T063110_result.json`
- **Structured JSON:** [`1dcac0d0e0c645fe91a2.json`](../../sessions/1d/1dcac0d0e0c645fe91a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**d154-8b-exec-s42-k8 Eval 结果**

| Metric | Value |
|--------|-------|
| Prove Rate | 14.0% (14/100) |
| Mean ISR | 0.0802 ± 0.2220 |
| ISR* (proved-only) | 0.573 |
| Genuine | 13/14 (92.9%) |
| CE (H1) | 1/14 (7.1%) |
| TS (H7) | 0 |
| PG (H8) | 0 |
| CI (H9) | 0 |

结论 **negative**：K=8 未能挽救 8B exec-only 的收敛问题。训练后期 reward 归零、grad_norm=0（frac_reward_zero_std=1.0），模型在 500 步内陷入完全停滞。14% PR 基本是 base model Qwen3-8B 的 pre-training 残余能力，非 GRPO 训练所得。

---
