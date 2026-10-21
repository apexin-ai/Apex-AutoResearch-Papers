# urgent westd 27271 registry update

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd-27271-registry-update_20260525T224051_result.json`
- **Structured JSON:** [`10842d109a7f17aebe5e.json`](../../sessions/10/10842d109a7f17aebe5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-27271 状态

| GPU | 实验 | 进度 | 已完成 task SR |
|-----|------|------|---------------|
| GPU0 | eval_openvla_random_k07_goal_seed42 | Task 3/10 (~20%) | T1=0.0%, T2=0.0% |
| GPU1 | eval_openvla_l2norm_k09_goal_seed43 | Task 5/10 (~45%) | T1=66%, T2=92%, T3=82%, T4=38% (avg 69.5%) |

两张卡都在跑，utilization 71%/77%，registry 已有记录且状态正确（RUNNING），无需更新。

**值得注意**：GPU0 Random k=0.7 Goal 前两个 task 全部 0%，说明 Goal 在 30% 压缩下 random pruning 完全崩溃。这与 k=0.9 时 Goal method-indifferent 的结论形成对比——method-indifference 只在低压缩率成立，激进压缩下 random 远逊于 structured pruning。

GPU1 L2norm k=0.9 Goal seed43 avg 69.5%（4 tasks），与 seed42 的 74.8% 在合理范围内，cross-seed 一致性良好。

**无空闲 GPU**，L2norm k=0.7 Goal seed42 需等实验完成后部署。

---
