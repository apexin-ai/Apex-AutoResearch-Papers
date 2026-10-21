# analysis rssm v3 cheetah corrected

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm_v3_cheetah_corrected_20260526T055335_result.json`
- **Structured JSON:** [`70a5b0b329a42228c829.json`](../../sessions/70/70a5b0b329a42228c829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题比预期的更复杂：

**exp_091** (trained_dt_emb, 105K) — **不存在**于 westd-51268，整台机器搜不到。可能在已宕机的 bjb1 上。

**exp_097** (cheetah_008d_s3) — 当前 52K/105K 步训练中，但它是 **fixed_dt=2** 模型（`--gate_fixed_dt 2`），不是 trained_dt_emb。从 metrics 看 `gate_dt_mean=2.0, gate_dt_std=0.0`——dt 固定为 2，无自适应。

**可用的 Cheetah checkpoint**：
| 实验 | 类型 | 状态 |
|------|------|------|
| exp_092 | no_dt_emb | 完成 ✓ |
| exp_093 | no_dt_emb | 完成 ✓ |
| exp_097 | fixed_dt=2 (非 trained_dt_emb) | 训练中 52K/105K |

**结论**：westd-51268 上没有 Cheetah trained_dt_emb 的完整 checkpoint。exp_091 可能在 bjb1 上（已宕机）。exp_097 是 fixed_dt=2 变体，不等同于 trained_dt_emb。

**可选方案**：
1. 等 exp_097 训练完成（~50K steps 剩余，按当前速度约 2-3 小时），用它做 fixed_dt=2 vs no_dt_emb 对比
2. 如果能从 bjb1 恢复或有备份，获取 exp_091
3. 在 westd-51268 上重新启动一个 trained_dt_emb Cheetah 实验（需要等 GPU 空出）

需要你决定怎么处理。

---
