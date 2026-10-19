# analysis m022 partial failure

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m022_partial_failure_20260522T152429_result.json`
- **Structured JSON:** [`c597dd7c62527baffc60.json`](../../sessions/c5/c597dd7c62527baffc60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结论如下：

## A3 v11 Displacement 分布分析

### 总览
- **200 个 episodes 中 149 个 (74.5%) 是 near-zero displacement**
- 所有 near-zero episodes 的 `refine_count=0` 且 `collided=False`
- 所有 normal episodes 都有碰撞（`collided=True`）

### M022 失效是**系统性的**，不是随机的

**证据 1：displacement 只有 4 个离散值**

| 值 | 出现次数 |
|---|---|
| 5.58e-10 | 43 |
| 2.05e-09 | 23 |
| 4.98e-09 | 44 |
| 1.16e-06 | 36 |

这不是连续分布，是几个固定的数值常量在重复出现——说明 norm_stats 修复后，某些 code path 仍然输出固定的极小 gradient，导致 displacement 被钉死在浮点噪声级别。

**证据 2：跨 task 高度一致**

| Task | Near-zero 比例 |
|---|---|
| orange_juice | 84% (42/50) |
| bbq_sauce | 84% (42/50) |
| milk | 82% (41/50) |
| chocolate_pudding | 48% (24/50) |

前 3 个 task 比例几乎相同（82-84%），chocolate_pudding 明显低（48%）。17 个 episodes 在**全部 4 个 task** 中都是 near-zero，36 个 episodes 在至少 3 个 task 中 near-zero。

**证据 3：near-zero = 完全没动，normal = 碰撞**

- 149 个 near-zero episodes：**全部** `refine_count=0`，**全部** `collided=False`
- 51 个 normal episodes：**全部** `collided=True`

这意味着 displacement 不是"有时大有时小"——而是二元的：要么机械臂完全没被 refine 推动（gradient 失效），要么碰撞产生了物理位移。**refine 模块在这些 episode 里实质上没有工作。**

### 结论

M022 norm_stats 修复**不完全**。失效模式是系统性的：
1. ~75% 的 episodes 中 refine gradient 被压缩到浮点噪声级别（4 个离散常量值）
2. chocolate_pudding 失效率较低（48% vs 82-84%），可能因为其场景布局更容易触发碰撞，从而产生真实位移
3. **refine 从未真正工作过**——所有 "normal" displacement 都来自碰撞，而非 refine 推动

需要排查的方向：norm_stats 修复可能只修了部分分支（如 action norm），而 SDF gradient → displacement 的路径上还有其他 normalization 或 scaling 问题导致 gradient 被压到 ~0。

---
