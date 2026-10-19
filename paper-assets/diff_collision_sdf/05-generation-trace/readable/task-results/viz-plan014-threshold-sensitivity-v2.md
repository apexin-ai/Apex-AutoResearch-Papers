# viz plan014 threshold sensitivity v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_plan014_threshold_sensitivity_v2_20260526T150421_result.json`
- **Structured JSON:** [`1df1a9bdd9e32c3d65f1.json`](../../sessions/1d/1df1a9bdd9e32c3d65f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完毕，验证结果：

- **λ 标签正确**：LoRA (λ=0)、SDF (λ=0.005)、SDF (λ=0.01)
- **dfCAR 在 2–200mm 几乎完全 flat**，仅 300mm 处有极微小波动（个别 episode 的 max_ee_displacement < 300mm 被过滤掉）
- **数值与 CSV 一致**：SDF λ=0.01 s0 = 57.0%，LoRA s0 = 56.5% 等
- 竖线标注 δ=100mm Paper threshold
- 粗实线为 per-λ 均值，细虚线为个体 seed
- All Pooled 线（蓝色方块）居中

结论不变：dfCAR 对 displacement threshold 不敏感，选择 δ=100mm 不影响结论。输出已覆盖旧版 `fig_threshold_sensitivity.pdf` 和 `.png`。

---
