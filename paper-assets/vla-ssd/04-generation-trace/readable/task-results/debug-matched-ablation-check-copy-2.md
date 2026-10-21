# debug matched ablation check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_matched_ablation_check_20260519T040251_result.json`
- **Structured JSON:** [`7c2a1836d36208839dbd.json`](../../sessions/7c/7c2a1836d36208839dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被清除或未在本 session 创建），无需处理。

**实验结果：成功**

| Condition | traj_d | token_d |
|---|---|---|
| **Instruction-dominant 24** (ref) | **0.650** | — |
| **Random 24** (5 seeds mean±std) | 0.601 ± 0.021 | 3.056 ± 0.305 |
| **Image-dominant 24** | 0.580 | 2.169 |

Instruction-dominant heads 的 ablation 造成的轨迹偏移 (0.650) 大于 random 控制组 (0.601) 和 image-dominant 控制组 (0.580)，且 random 控制组 5 seeds 的标准差仅 0.021，instruction-dominant 的 0.650 落在 random 分布的 ~2.4σ 之外。

---
