# research corl paper outline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_corl-paper-outline_20260515T190901_result.json`
- **Structured JSON:** [`27d2d1c59b5d3a301512.json`](../../sessions/27/27d2d1c59b5d3a301512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件已生成：

**`paper/outline.md`** — 完整 8-page 论文大纲
- Introduction (1.5p): problem → gap → sample-then-correct pipeline → 3 findings
- Method (2p): conformal selection, CRM architecture (obs_only/perdof/scalar), magnitude control
- Experiments (2.5p): object main story (+7pp), spatial honest negative, magnitude sweep, statistical significance
- Discussion (0.5p): why obs_only works, limitations, future work
- 每个定量 claim 标注了 exp_id

**`paper/sections/related_work.md`** — ~1.5 页 Related Work 初稿
- (a) VLA Robustness & Inference-Time Adaptation: ReconVLA, SC-VLA, VLA-Pilot, A2C2, SAFE, training-time methods (SRPO, RobustVLA, DiG-Flow, etc.)
- (b) Conformal Prediction in Robotics: CP foundations, CGS/CQR, robotics applications (Zhao RSS'24, Wang'25, Zhou ICRA'25), VLA-specific UQ
- (c) Residual Correction & Learned Action Refinement: Silver'18 → PLD/DAWN/DRC, supervised correction (DAgger, CR-DAgger), conditioning feature comparison as novel angle

**`paper/figure_plan.md`** — 5 main figures + 3 tables + 5 supplementary figures
- Fig 1: Pipeline overview (abstract figure)
- Fig 2-3: Object/spatial bar charts (main results)
- Fig 4: Magnitude sensitivity curve (key contribution)
- Fig 5: Per-task heatmap
- Tables 1-3 with exp_id sources, color scheme, production specs

Seed=43 结果到后可直接补入 Table 1 的 combined 列和 Fisher p-value。

---
