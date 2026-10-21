# paper related work collision sdf

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_collision_sdf_20260525T074038_result.json`
- **Structured JSON:** [`94700b88fa6fc44fb9ac.json`](../../sessions/94/94700b88fa6fc44fb9ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。以下是补充的 6 篇论文简要分析：

---

### Direction 1: Collision-aware manipulation（3 篇）

| 论文 | Venue | 与 ColliForce 的对比点 |
|------|-------|----------------------|
| **CoFreeVLA** (Zhai et al., 2026) | arXiv | 最新 VLA+碰撞安全工作。外挂风险估计器做 post-hoc 过滤，ColliForce 通过 SDF 辅助损失在训练时嵌入碰撞感知 → internal vs. external 路线对比 |
| **APEX** (Dastider et al., IROS 2024) | IROS 2024 | 潜在扩散模型 + classifier-guidance 碰撞回避。属推理阶段安全注入方法族（同 Lan-o3dp, CAPE），与 ColliForce 训练阶段方法形成 train-time vs. test-time 对比 |
| **Safe Learning Survey** (Zhang et al., 2025) | arXiv | 系统综述，将安全方法分为 constrained RL / CBF / MPC shields 等。可用于 Related Work 中定位 ColliForce 为 "training-time geometric supervision" 路线 |

### Direction 2: SDF in robotics（3 篇）

| 论文 | Venue | 与 ColliForce 的对比点 |
|------|-------|----------------------|
| **Configuration Space Distance Fields** (Li et al., RSS 2024) | RSS 2024 | 将 SDF 从 task-space 扩展到 C-space，天然覆盖全身碰撞。直接回应 ColliForce EE-only SDF 局限 → C-space SDF 是 full-body 方案的代表 |
| **SDF-SC** (Liu et al., 2024) | arXiv | FK 分解全身 SDF + 轻量并行网络 + SVM 自碰撞检测，保持可微性。展示全身 SDF 的工程可行性，为 ColliForce 后续 full-body 扩展提供参考 |
| **Neural NMPC-SDF** (Jacquet et al., IJRR 2025) | IJRR 2025 | 深度图像→神经 SDF→NMPC 约束的端到端集成。SDF 进控制 vs. ColliForce SDF 进 policy loss，两条集成路径互为对照 |

---
