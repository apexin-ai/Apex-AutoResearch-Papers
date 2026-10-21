# eval 28034 collect heldout chain

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-collect-heldout-chain_20260523T072123_result.json`
- **Structured JSON:** [`17e47f8866bec6b9fc53.json`](../../sessions/17/17e47f8866bec6b9fc53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three evals complete. ACT s1 ckpt-8000 eval already at 60/70 — very fast. Here's the summary:

## 汇总

| Eval | GPU | SYCONScore | ToF | NoF | 数据 | 状态 |
|------|-----|-----------|------|------|------|------|
| rl-ckpt-7000 (362 pairs) | 0 | **0.3257** | 0.2044 | 0.8011 | sycophancy_bench | 完成 |
| vanilla held-out (70 pairs) | 2 | **0.0556** | 0.0286 | 1.0000 | eval_held_out | 完成 |
| R3-only ckpt-6500 held-out (70 pairs) | 3 | **0.1079** | 0.0571 | 0.9714 | eval_held_out | 完成 |
| ACT s1 ckpt-8000 held-out (70 pairs) | 2 | — | — | — | eval_held_out | 运行中 (PID 58089, 60/70) |

**ACT s1 ckpt-8000 信息：**
- Checkpoint 路径: `/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-8000`
- PID: 58089 (GPU 2)
- 预计几分钟内完成

**对比 vanilla baseline (sycophancy_bench = 0.1335)：**
- rl-ckpt-7000 在 sycophancy_bench 上 SYCONScore 0.3257，是 vanilla 的 2.44x
- held-out 上 vanilla baseline 降到 0.0556（样本更小，70 vs 362）
- R3-only ckpt-6500 held-out 0.1079，比 held-out vanilla 高约 2x

---
