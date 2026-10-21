# debug matched ablation check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_matched_ablation_check_20260519T040046_result.json`
- **Structured JSON:** [`9afe1f4026d2b7399bc9.json`](../../sessions/9a/9afe1f4026d2b7399bc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 监控不在当前 session，无需删除。

## 实验结果

10,500 forward passes，3 tasks × 10 demos × 50 timesteps，模型 openvla-7b。

| 消融条件 | traj_d | token_d |
|---|---|---|
| **Instruction-dominant 24 heads** | **0.650** | — (reference) |
| Random 24 heads (5 seeds) | 0.601 ± 0.021 | 3.056 ± 0.305 |
| Image-dominant 24 heads | 0.580 | 2.169 |

**关键发现**：消融 instruction-dominant heads 造成的轨迹偏离（0.650）显著高于消融同等数量的 random heads（0.601）和 image-dominant heads（0.580）。instruction-dominant 与 random 的差值 ~0.049，约 2.4 个标准差（0.021），说明 instruction-dominant heads 的功能不可被其他 heads 替代。Image-dominant heads 消融影响最小，进一步支持 instruction-dominant heads 承载了独特的语言-动作 grounding 信号。

---
