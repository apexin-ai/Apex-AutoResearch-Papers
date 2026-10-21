# paper writing analysis claim3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_analysis_claim3_20260524T173905_result.json`
- **Structured JSON:** [`ffe2a2848e4047ddf0e0.json`](../../sessions/ff/ffe2a2848e4047ddf0e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§5.3 已写入 `artifacts/drafts/analysis_claim3.tex`，约 650 words。

**结构总结：**
- **P1** — 实验设计动机：用 GT SDF 构造 oracle，排除预测误差，测试 EE-only refinement 的理论上限
- **Table 3** — 6 行（2 baseline + 3 oracle + A3 learned），含 TSR/CAR/Fake Safe/Refines 四列
- **P2** — 核心发现：3 个 oracle 全部低于 baseline（最佳 76.9% vs 最差 baseline 82.0%），fake safe 率 96.7–98.3%
- **P3** — Per-task 分析：task 1 有微弱改善，task 0/2/3 oracle 反而更差，引出 arm body 碰撞问题
- **P4** — 机制分析：EE-only gradient 推 EE 远离障碍物但可能旋转 arm links 进入障碍物；feature-space oracle 每步都 refine（241.7/ep）但 gradient 极小（0.004–0.006），latent space 与 full-body 几何缺乏直接映射
- **P5** — A3 learned SDF：预测值始终高于阈值，refinement 从未触发，退化为 baseline
- **P6** — 结论：EE-only SDF 是 structural limitation，需要 full-body collision awareness

---
