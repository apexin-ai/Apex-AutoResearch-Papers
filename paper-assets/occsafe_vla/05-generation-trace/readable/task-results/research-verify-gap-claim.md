# research verify gap claim

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-gap-claim_20260522T183045_result.json`
- **Structured JSON:** [`00c10a34fd8c14830370.json`](../../sessions/00/00c10a34fd8c14830370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完毕。以下是逐篇结果和最终结论。

---

## 1. SpatialForcing (li2026spatialforcing)

- **Venue**: arXiv 2510.12276
- **是否评估碰撞避免**: **NO**
- **评估内容**: 仅 success rate (SR)
- **Benchmarks**: LIBERO (标准版, 非 SafeLIBERO)、RoboTwin、真实机器人
- **证据**: *"We report the success rates (SR) as evaluation metrics for these two benchmarks."* 全文无 collision/safety 相关指标。

## 2. DepthVLA (yuan2025depthvla)

- **Venue**: arXiv 2510.13375
- **是否评估碰撞避免**: **NO**（仅定性提及，无量化指标）
- **评估内容**: success rate、progress score
- **Benchmarks**: Simpler WidowX、LIBERO (标准版)、真实机器人
- **证据**: 论文定性提及 *"DepthVLA demonstrates improved collision avoidance when handling the door and plate"*，但这是基于 task success 推断的，**未使用 collision rate 或任何安全专项指标**。无 SafeLIBERO。

## 3. OccVLA (liu2025occvla)

- **Venue**: arXiv 2509.05578 / OpenReview
- **是否评估碰撞避免**: **NO**
- **重要说明**: **这是自动驾驶论文，不是机器人操作 VLA**。评估 nuScenes 上的 trajectory planning (L2 distance)、VQA (accuracy)、occupancy (mIoU)。
- **证据**: 全文搜索 "collision" 一词，**出现次数为零**。即使在自动驾驶规划评估中也未报告 collision rate。

## 4. SpatialVLA (wu2025spatialvla)

- **Venue**: arXiv 2501.15830
- **是否评估碰撞避免**: **NO**
- **评估内容**: 仅 success rate
- **Benchmarks**: SimplerEnv、LIBERO (标准版)、BridgeData V2、Google Fractal、真实机器人 (16 tasks)
- **证据**: 评估覆盖 7 个场景、16 个真实任务、48 个仿真设置，**全部使用 task success rate，无 collision/safety 指标**。无 SafeLIBERO。

---

## 结论

**Gap claim 成立。** 4 篇 spatial VLA 论文中：

- **0/4** 使用了碰撞避免的量化指标（collision rate / CAR / safety metric）
- **0/4** 在 SafeLIBERO 或任何含障碍物的安全 benchmark 上评估
- **4/4** 仅使用 task success rate 作为核心指标

**DepthVLA 的细微之处**：它定性提及了 collision avoidance 的改善，但没有用专门的 metric 量化。你的 claim 如果写成 "no spatial VLA method **quantitatively evaluates** collision avoidance" 是完全站得住脚的。建议避免写成绝对的 "no method considers collision avoidance"，因为 DepthVLA 至少在叙述中提到了。

**OccVLA 的注意事项**：它是自动驾驶论文而非机器人操作 VLA。如果你的 Introduction 将其列为 "spatial VLA for manipulation"，需要确认措辞是否准确，或改为更宽泛的 "spatial VLA" 分类。

Sources:
- [SpatialForcing](https://arxiv.org/abs/2510.12276)
- [DepthVLA](https://arxiv.org/abs/2510.13375)
- [OccVLA](https://arxiv.org/abs/2509.05578)
- [SpatialVLA](https://arxiv.org/abs/2501.15830)

---
