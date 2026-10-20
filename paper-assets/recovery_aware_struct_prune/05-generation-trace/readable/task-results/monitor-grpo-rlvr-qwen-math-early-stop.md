# monitor grpo rlvr qwen math early stop

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo_rlvr_qwen_math_early_stop_20260516T185324_result.json`
- **Structured JSON:** [`b2d97e77fa01d0621faf.json`](../../sessions/b2/b2d97e77fa01d0621faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已提取。总结如下：

**当前进度**: Step 57/100（基于进度条），最新完整指标在 step 50。

**frac_reward_zero_std 趋势**:
| Step | frac_zero_std | reward | KL |
|------|--------------|--------|-----|
| 10 | 0.650 | 0.084 | 0.006 |
| 20 | **0.825** | 0.057 | 0.029 |
| 30 | **0.750** | 0.065 | 0.059 |
| 40 | **0.875** | 0.026 | 0.396 |
| 50 | 0.575 | 0.105 | 0.008 |

**判定**: 不满足自动 kill 条件（最新 step 50 的 frac_zero_std = 0.575 < 0.7），但也不满足"继续等"条件。

**需 Director 决策的关键信号**:
1. 5 次记录中有 3 次 frac_zero_std > 0.7（step 20/30/40），均值 0.735
2. reward 始终极低（0.026–0.105），无明显上升趋势
3. Step 40 出现 KL 飙升（0.396）后 step 50 突然回落到 0.008，同时 frac_zero_std 也从 0.875 降到 0.575 — 可能是一次偶然的 lucky batch
4. 实际速度 ~27s/step（非 400s），预计还剩 ~20min 完成全部 100 steps

**建议交由 Director**：整体信号偏 negative（reward 不涨，frac_zero_std 多数时候 > 0.7），但最新一步有所改善，且距离训练结束仅剩 ~43 steps ≈ 20min。

---
