# train n5 seeds batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_n5_seeds_batch_20260524T044052_result.json`
- **Structured JSON:** [`8eb0ebd0eb6027074ab1.json`](../../sessions/8e/8eb0ebd0eb6027074ab1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部满载运行。汇总：

| GPU | exp_id | method | seed | PID |
|-----|--------|--------|------|-----|
| cuda:0 | adaptive_seed789 | adaptive (τ=0.7, n_min=2) | 789 | 922510 |
| cuda:1 | uniform_seed789 | uniform | 789 | 922589 |
| cuda:2 | adaptive_seed234 | adaptive (τ=0.7, n_min=2) | 234 | 922738 |
| cuda:3 | uniform_seed234 | uniform | 234 | 923155 |

**超参数确认**：B=4, grad_accum=4, effective_batch=16, lr=5e-5, max_steps=6103, 200M tokens, bf16, no eval

**预估完成时间**：adaptive_seed234 初始速度 ~2.87s/step × 6103 steps ≈ **4.9 小时**，预计 UTC ~09:40（北京时间约 17:40）完成。

---
