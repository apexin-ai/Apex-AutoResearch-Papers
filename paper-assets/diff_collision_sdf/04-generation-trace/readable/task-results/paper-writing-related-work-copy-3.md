# paper writing related work

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260524T185835_result.json`
- **Structured JSON:** [`24ecd4880f3a39410f30.json`](../../sessions/24/24ecd4880f3a39410f30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/drafts/related_work_v2.tex`。

**结构概要：**

- **§3.1 Collision-Safe VLA Methods** (~240 words): 按 post-hoc correction (AEGIS, iKinQP-RL, CoFreeVLA)、constrained optimization (SafeVLA)、inference-time guidance (Li et al., CAPE) 三类组织。Positioning: 所有方法共享 CAR 作为评估指标，无一检验 metric validity。
- **§3.2 SDF in Robot Manipulation** (~210 words): DeepSDF → iSDF → DiffCo → VoxPoser。Positioning: SDF 在经典规划中有效，但 oracle 实验揭示 EE-only refinement 的结构性缺陷。
- **§3.3 Evaluation Reliability in Robot Learning** (~220 words): 从 NLP benchmark saturation / Goodhart's law 引入 metric contamination lens，连接 action collapse 与 mode collapse，指出 CAR 的 construct validity 缺失。Positioning: 现有文献未识别 action collapse 对 CAR 的污染。

**待后续处理：**
- 3 个 `%[CITE-CHECK]` 标记（CoFreeVLA, SafeVLA, chi2023diffusionpolicy）
- 2 个占位引用（`placeholder_metric_reliability`, `placeholder_goodhart_rl`）需 reference audit 补充真实 bib 条目

---
