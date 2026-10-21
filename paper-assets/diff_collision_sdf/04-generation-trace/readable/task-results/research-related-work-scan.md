# research related work scan

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_scan_20260527T220506_result.json`
- **Structured JSON:** [`dc9f4bf5c1951df55bc9.json`](../../sessions/dc/dc9f4bf5c1951df55bc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the gap report.

---

## 遗漏论文清单

### Tier 1: 高相关性，建议补充

| # | 论文 | 作者 | 年份/会议 | 与本文关系 | 建议引用位置 |
|---|------|------|-----------|-----------|-------------|
| 1 | **SafeDiffuser: Safe Planning with Diffusion Probabilistic Models** | Xiao, Wang et al. | ICLR 2025 (arXiv:2306.00148) | 将 CBF 嵌入 diffusion denoising 过程实现安全规划——与本文"safety imposed externally vs. learned intrinsically"的对比论述直接相关 | §Safety in Robot Learning，与 CAPE/Li2024langguided 并列，作为 diffusion-process 安全约束的代表 |
| 2 | **CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation** | (arXiv:2601.15541, Jan 2026) | 用 VLM 指导变阻抗控制实现 VLA 安全，属于 runtime shield 类方法 | §Safety in Robot Learning，作为 test-time 安全方法的又一变体，紧跟 VLSA/CoFreeVLA 之后 |
| 3 | **SafeBimanual: Diffusion-based Trajectory Optimization for Safe Bimanual Manipulation** | Deng et al. | CoRL 2025 (arXiv:2508.18268) | Test-time trajectory optimization 对 diffusion policy 施加安全约束，与 CAPE 互补 | §Safety in Robot Learning，与 CAPE 并列为 test-time diffusion 安全方法 |
| 4 | **Configuration Space Distance Fields for Manipulation Planning** | Li, Chi, Razmjoo, Calinon | RSS 2024 (arXiv:2406.01137) | C-space SDF 的奠基工作，CSSDF-Net (Chen 2026) 的直接前驱 | §SDF in Robotics，在 CSSDF-Net 之前引用，作为 C-space SDF 的源头 |
| 5 | **Representing Robot Geometry as Distance Fields (RDF)** | Li, Zhang et al. | ICRA 2024 (arXiv:2307.00533) | 学习机器人自身几何的 SDF 用于 whole-body manipulation 和碰撞避免——与本文"full-body collision awareness remains open"直接对话 | §SDF in Robotics，补充 robot-body SDF 方向，与 DeepSDF/iSDF 的 scene SDF 形成对比 |
| 6 | **Neural Configuration-Space Barriers for Manipulation Planning and Control** | Long, Lee et al. (UCSD) | 2025 (arXiv:2503.04929) | 将 C-space SDF 与 CBF 结合实现安全保证——同时横跨 SDF 和 safety 两个 section | §SDF in Robotics 末尾或 §Safety in Robot Learning，作为 SDF+safety 的桥梁工作 |

### Tier 2: 中等相关性，可选补充

| # | 论文 | 作者 | 年份/会议 | 与本文关系 | 建议引用位置 |
|---|------|------|-----------|-----------|-------------|
| 7 | **Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation** | (arXiv:2512.17568, Dec 2025) | 将 full-arm kinematics 引入 diffusion policy，关注 whole-body collision avoidance | §SDF in Robotics 末尾讨论 full-body awareness 时可作为 policy-learning 侧的对应工作 |
| 8 | **PointVLA: Injecting the 3D World into Vision-Language-Action Models** | (arXiv:2503.07511, 2025) | 将 3D 点云注入 VLA，与 DepthVLA/SpatialForcing 同属 3D-aware VLA | §VLA Models，已有 3 篇 3D-aware VLA，此篇为补充但非必须 |

### 总结

**最需要补充的 3 篇**：
1. **SafeDiffuser** (ICLR 2025) — 当前 §Safety 已引用 CAPE 和 Li2024langguided 作为 diffusion-process safety 代表，但 SafeDiffuser 是该方向最有影响力的工作（ICLR oral-level），遗漏明显
2. **CDF** (RSS 2024) — 已引用 CSSDF-Net 却未引用其直接前驱，reviewers 可能注意到
3. **RDF** (ICRA 2024) — related work 末尾写"full-body collision awareness remains open"，但未引用明确做 robot-body SDF 的工作

**现有引用覆盖良好的方面**：VLA 基础模型（RT-2/Pi0/OpenVLA）、SafeLIBERO benchmark、action collapse、评估方法论、VLA 安全综述——这些方面不需要补充。

Sources:
- [SafeDiffuser (ICLR 2025)](https://arxiv.org/abs/2306.00148)
- [CompliantVLA-adaptor](https://arxiv.org/abs/2601.15541)
- [SafeBimanual (CoRL 2025)](https://arxiv.org/abs/2508.18268)
- [CDF (RSS 2024)](https://arxiv.org/abs/2406.01137)
- [RDF (ICRA 2024)](https://arxiv.org/abs/2307.00533)
- [Neural C-Space Barriers](https://arxiv.org/abs/2503.04929)
- [Kinematics-Aware Diffusion Policy](https://arxiv.org/abs/2512.17568)
- [PointVLA](https://arxiv.org/abs/2503.07511)

---
