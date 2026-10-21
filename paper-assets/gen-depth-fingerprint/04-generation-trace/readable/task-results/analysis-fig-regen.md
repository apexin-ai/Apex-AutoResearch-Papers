# analysis fig regen

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig-regen_20260515T073125_result.json`
- **Structured JSON:** [`73d8cbf423e1b9b0f5a1.json`](../../sessions/73/73d8cbf423e1b9b0f5a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图已生成并下载到本地。

**Fig1 — Differential Depth Response (Spearman bar chart)**:
从完整数据 (n=27529) 重新计算的 Spearman ρ：

| Feature | 100% 数据 ρ | 论文 82% 值 |
|---------|------------|------------|
| hapax_ratio | **-0.647** | -0.558 |
| TTR | **-0.630** | -0.542 |
| entropy_mean | **-0.610** | -0.475 |
| entropy_std | **-0.200** | 0.076 |
| tail_decay | **-0.040** | 0.089 |
| entropy_min | -0.406 | — |
| entropy_max | 0.050 | — |

注意：entropy_std 在完整数据中 |ρ|=0.200，远大于论文中的 0.076，分类为 "near-stationary" 可能需要重新讨论。

**Fig3 — Baseline Comparison (forest plot)**:
目前只包含 3 个有数据的方法（6-gen LOGO）：
- 7-Feature Ensemble: 0.789 CI=[0.744, 0.828]
- Avg Log-Prob: 0.759 CI=[0.738, 0.785]
- FastDetectGPT: 0.717 CI=[0.691, 0.748]

任务中提到的 LD-Score (0.721) 和 Binoculars (0.579) 在服务器上没有计算数据（detector_baseline_results.json 标记为 skipped）。是否需要将这两个 baseline 用任务提供的固定值加入图中（无 CI/per-generator range）？

---
