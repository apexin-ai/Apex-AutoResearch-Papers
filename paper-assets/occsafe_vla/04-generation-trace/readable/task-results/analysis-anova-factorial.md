# analysis anova factorial

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_anova_factorial_20260526T094253_result.json`
- **Structured JSON:** [`9d810eed49ee68d3fc5c.json`](../../sessions/9d/9d810eed49ee68d3fc5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和结果已保存并注册。核心发现：

**ANOVA 结果**（Type III SS, df=1,7）：
- **Gradient Flow**: F=4.02, p=0.085, η²_p=0.365 — 趋近显著，大效应量
- **Norm Type**: F=1.68, p=0.236, η²_p=0.194 — 不显著，中等效应量
- **交互项**: F=0.74, p=0.419, η²_p=0.095 — 不显著，小效应量

**Effect sizes** 很大（Cohen's d: Grad OFF vs ON = 1.08, LN vs BN = 0.55），但 N=11 统计力不足，p 值均未达 0.05。

**vs Vanilla (0.768)**：所有 OCC cell 均低于 Vanilla，grad_off_ln 最接近（-0.003），grad_on_bn 差距最大（-0.068）。Grand mean 0.745 比 Vanilla 低 0.023。

---
