# analysis lf temporal dynamics

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lf-temporal-dynamics_20260514T150420_result.json`
- **Structured JSON:** [`e4757771e50afe73ae49.json`](../../sessions/e4/e4757771e50afe73ae49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

### LF 时序角色分类（59,496 windows / 5,000 trajectories / 1,939 有明确 onset）

| LF | 角色 | 平均 lead/lag | 领先% | 精确% | 滞后% |
|---|---|---|---|---|---|
| **command_repetition** | Leading | **-1.87 windows** | 36.1% | 41.4% | 22.5% |
| **file_diff_delta** | Leading/Concurrent | -1.20 windows | 17.1% | 78.8% | 4.2% |
| **outcome_backpropagation** | Lagging | **+6.70 windows** | 20.5% | 31.1% | 48.4% |

### 统计检验
- **Kruskal-Wallis**: H=274.3, p=2.74e-60 — 三个 LF 时序分布显著不同
- 所有 pairwise Wilcoxon 检验在 Bonferroni 校正后均显著（p < 1.67e-2），效应量极大（r > 0.86）
- Paired comparison 中 file_diff_delta 比 command_repetition 实际更早（diff=+3.83），但 command_repetition 覆盖更广、高方差

### Agreement dynamics
- Onset 前（-2 到 -1）：平均 0.21-0.32 个 LF 投 stagnation
- Onset 时（0）：跳升至 1.22，100% 窗口至少 1 个 LF 投 stagnation
- Onset 后逐渐下降至 ~0.8（+7 到 +10）

### 对 temporal-label-model 的启示
假设得到确认：naive majority voting 是次优的。temporal-aware 权重分配（onset 阶段加权 leading indicators，确认阶段加权 lagging indicators）有统计基础。

输出保存在 `artifacts/lf-temporal-dynamics/lf_temporal_summary.json`，实验已注册为 `lf-temporal-dynamics` (DONE/success)。

---
