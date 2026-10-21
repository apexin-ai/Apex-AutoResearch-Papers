# analysis grpo standard 20 fair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_standard_20_fair_20260518T020305_result.json`
- **Structured JSON:** [`4f295a9e52fe94d27fee.json`](../../sessions/4f/4f295a9e52fe94d27fee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## grpo_standard_20_fair 结果

**Pattern: dip_then_partial_recovery** (success)

| 指标 | 值 |
|------|-----|
| Peak reward | 0.081 @ step 40 |
| Dip | 0.019 @ step 50 |
| Final reward | 0.054 @ step 100 |
| frac_zero_std | 0.50-0.625 (稳定，未 collapse) |
| 训练时间 | 50min, 100 steps |

**与 RASP fair 对比：** Standard 明显更好。RASP peak 仅 0.061，最终 collapse 到 0.01，frac_zero_std 飙升至 0.85。Standard peak 更高 (0.081)，dip 后恢复到 0.054，frac_zero_std 从未超过 0.625。

**与旧 Standard (v8) 对比：** 同样的 dip-recovery 模式。旧版 peak 0.096@40, dip@60, recovery 0.065@90。Fair v5 config 略微压低幅度但保留了相同的动力学形态。

**D058 fair 4-way comparison 完成，recovery capacity gradient 确认：**
- CKA-only: active learning (reward 持续上升, frac_zero_std ~0.125)
- Random: plateau (缓慢上升, frac_zero_std ~0.30-0.35)
- Standard: dip then partial recovery (peak 0.081, dip 0.019, recovery ~0.05)
- RASP: permanent collapse (peak 0.061, final 0.01, frac_zero_std 0.85)

Registry 已更新为 DONE(success)，memory.md 已追加分析。

---
