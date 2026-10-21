# paper writing related work

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260513T173628_result.json`
- **Structured JSON:** [`26f7801c40f4a9253459.json`](../../sessions/26/26f7801c40f4a9253459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work section 已写入 `artifacts/_project/paper/related_work.tex`，共 4 段约 870 words：

1. **VLA Robustness Methods** — 覆盖 SRPO/RobustVLA/DiG-Flow/SnapFlow/TT-VLA/VLA-GSE/Cosmos-Policy，强调 training-time 与 ACR-VLA inference-time 的正交互补性
2. **Uncertainty Quantification for Robot Learning** — 覆盖 Deep Ensembles/MC-Dropout/Diffusion Policy/DiU，区分 scalar vs per-DOF、aleatoric vs epistemic、single-pass vs multi-sample
3. **Conformal Prediction in Robotics** — 覆盖 CP 基础理论（Angelopoulos/Romano CQR/Gibbs ACI/Barber）和应用（CP-in-the-Loop/Conformalized Teleoperation/UPS/SAFE/Braun CGS），论点：CP 作为 binary decision vs 作为 continuous features for learned correction
4. **Inference-Time Action Correction** — 与 A2C2（generic residual, no uncertainty conditioning）和 ReconVLA（scalar distance, sample selection only）做精确对比

所有引用严格使用提供的 bibtex_key 列表，未编造任何引用。

---
