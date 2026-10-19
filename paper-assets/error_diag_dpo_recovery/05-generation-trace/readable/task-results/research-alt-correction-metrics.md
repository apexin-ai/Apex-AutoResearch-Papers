# research alt correction metrics

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alt_correction_metrics_20260512T223951_result.json`
- **Structured JSON:** [`64559c5d77134d0ad907.json`](../../sessions/64/64559c5d77134d0ad907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结论

### 显著结果（p < 0.05）

| 指标 | 条件 | H | p | Ordinal? | 真正含义 |
|------|------|---|---|----------|----------|
| norm_correction_span | FULL/with_override | 16.05 | 0.0003 | NO | 数学伪影 |
| norm_correction_span | FULL/without_override | 29.87 | <0.0001 | YES(trivial) | 数学伪影 |
| divergence_ratio | FULL/without_override | 8.35 | 0.004 | NO(**反序**) | 数学伪影 |
| **model_post_div_diversity** | FULL/with_override | **60.63** | **<0.0001** | NO | **真实发现** |
| **diversity_ratio** | FULL/with_override | 9.95 | 0.007 | NO | **真实发现** |

### 解读

**1. norm_correction_span / divergence_ratio — 数学伪影，非真实发现**

88% 的 failure 在 step 1 diverge → norm_correction_span 恒等于 1.0。显著性完全由 2-4 个 action 样本（diverge 较晚）驱动。这两个指标本质上只在区分"step-1 diverge vs 非 step-1 diverge"。

**2. model_post_div_diversity — 唯一有实质意义的发现**

- verification(median=7.0) > planning(6.0) > action(5.5)
- verification vs planning pairwise: **p < 0.0001**
- 仅在 with_override（含 PCB 82 条 verification）时显著；without_override 完全不显著（p=0.65）

**解释**：PCB 分类的 verification failures 在 diverge 后模型使用了更多种类的 action verbs — 模型在"以为任务完成但实际没完成"时会尝试更多不同类型的动作（探索行为更强）。这是 PCB override 群体的行为签名。

**3. 没有任何指标实现期望的 ordinal ordering（action < verification < planning）并达到统计显著**

### 对 P1 backup 路径的评估

**这不是 backup win。** 原因：
- 真正显著的指标（model_post_div_diversity）方向是 verification > planning，不是我们假设的 action < verification < planning
- 仅在 PCB override 条件下有效，without_override 无效
- action 组太小（n=2），任何涉及三组对比的结果都不可靠

**但有一个可回收的 narrative**：verification failures 确实有结构性不同的行为特征（post-divergence 行动多样性更高），可以支撑"不同错误类型导致不同修正行为模式"的弱版本叙述，只是方向与原假设不同。

### Non-step-1 子集（n=29）

所有指标均不显著（样本太小）。

脚本已保存在 `/root/autodl-tmp/error_diag_dpo_recovery/analyze_alt_metrics.py`。

---
