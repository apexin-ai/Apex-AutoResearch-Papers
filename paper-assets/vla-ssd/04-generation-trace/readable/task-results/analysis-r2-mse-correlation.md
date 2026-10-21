# analysis r2 mse correlation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r2_mse_correlation_20260520T123229_result.json`
- **Structured JSON:** [`08b95e5498f3d36a8c42.json`](../../sessions/08/08b95e5498f3d36a8c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 数据盘点

| 数据类型 | 来源文件 | Task 覆盖 |
|---------|---------|----------|
| **Per-task R² (probe)** | `per_task_r2_distribution.json`, `unified_action_probe.json`, `action_probe_50demos.json` | **10 tasks** (LIBERO-Goal 全部) |
| **Per-task paired MSE (ablation行为偏移)** | `action_trajectory_analysis.json` | **5 tasks** |
| **Per-task model-vs-GT MSE** | `groundtruth_action_error.json` | **3 tasks** |
| **Per-task success rate** | `sr_corrected_3ep.json` | **1 task** |

**核心限制：behavioral outcome 数据最多只有 5 个 task。**

### Correlation 结果 (n=5 tasks)

**0/11 correlations 在 p<0.05 显著。**

| Representational Metric | Behavioral Metric | Spearman ρ | p-value |
|------------------------|-------------------|-----------|---------|
| R²_L1 (5-demo) | paired_mse | -0.10 | 0.873 |
| R²_L8 (5-demo) | paired_mse | -0.50 | 0.391 |
| R²_L13 (5-demo) | paired_mse | -0.60 | 0.285 |
| R²_projector (50-demo) | paired_mse | +0.30 | 0.624 |
| R²_dino (50-demo) | paired_mse | +0.60 | 0.285 |
| R²_vla_last_L19 (50-demo) | paired_mse | +0.40 | 0.505 |
| R²_L1 (5-demo) | Cohen's d | -0.10 | 0.873 |
| R²_projector | Cohen's d | +0.30 | 0.624 |
| R²_vla_last_L19 | Cohen's d | +0.40 | 0.505 |
| ΔR²_L1 (ablation) | paired_mse | +0.20 | 0.747 |
| ΔR²_L8 (ablation) | paired_mse | -0.60 | 0.285 |

### 10-task 交叉验证（representational only）

唯一显著结果：**R²_projector vs R²_vla_last_L19: ρ=+0.83, p=0.003** — 不同 probe readout 对 task 难度排序高度一致。

### 3-task model-vs-GT MSE（仅展示数据）

| Task | Model MSE | R²_L1 | R²_proj | R²_vla |
|------|-----------|-------|---------|--------|
| open middle drawer | 0.562 | 0.197 | 0.497 | 0.601 |
| top drawer + bowl | 0.548 | 0.265 | 0.750 | 0.752 |
| push plate | 0.383 | 0.190 | 0.586 | 0.710 |

MSE 最低的 push_plate 有中等 R² — 方向符合预期（低 MSE ↔ 高 R²），但 n=3 无法统计检验。

### 结论

**不能支持 "representational metrics predict behavioral outcomes" 的 claim。**

- n=5 tasks 时，Spearman 检验需要 |ρ|≥0.9 才能达到 p<0.05，统计功效极低
- 点估计在 -0.6 到 +0.6 之间摇摆，取决于选哪层/哪种 probe，无一致模式
- 跨 representation 的一致性（ρ=0.83）表明 probe 本身可靠，但缺少足够的 behavioral 数据来做闭环

### 要使这个分析可行

需要 **per-task behavioral data 覆盖全部 10 个 task**。两个方案：
1. **在全部 10 个 LIBERO-Goal task 上跑 `action_trajectory_analysis`**（当前只跑了 5 个）
2. **扩展到 LIBERO-Long**（再加 10 个 task，提高 n 到 20）

结果已保存至 `/root/autodl-tmp/vla-ssd/results/probe_r2_vs_behavioral_rank_correlation.json`。

---
