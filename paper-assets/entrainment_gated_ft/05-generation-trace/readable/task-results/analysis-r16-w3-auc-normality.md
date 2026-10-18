# analysis r16 w3 auc normality

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16-w3-auc-normality_20260523T141158_result.json`
- **Structured JSON:** [`1c9b24aae98f03d99fd1.json`](../../sessions/1c/1c9b24aae98f03d99fd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## R16-W3 AUC Normality 验证

**方法**：用 Mann-Whitney U 的 rank-biserial correlation 计算 empirical AUC（AUC_emp = (1+|r_rb|)/2，非参数），与 parametric AUC = Φ(|d|/√2) 对比。正态性用 quantile-based 指标评估（Shapiro-Wilk 需要原始数据，服务器 SSH 连接失败无法获取）。

### 结果

```
Arch     Task         |d|     AUC_par  AUC_emp   Bias    Status
─────────────────────────────────────────────────────────────────
GDN      Disruption   0.8744  0.7318   0.7420   -1.4%   parametric estimate 可信
GDN      Rescue       0.7462  0.7011   0.7563   -7.3%   偏差适中
RetNet   Disruption   0.8306  0.7215   0.7346   -1.8%   parametric estimate 可信
RetNet   Rescue       0.7262  0.6962   0.7535   -7.6%   偏差适中
HGRN2    Disruption   0.9228  0.7430   0.7477   -0.6%   parametric estimate 可信
HGRN2    Rescue       0.7730  0.7077   0.7650   -7.5%   偏差适中
```

### 关键发现

1. **Disruption 预测**（hurt vs stayed-right）：偏差 0.6–1.8%，parametric estimate 可信。hurt 组 |log p| 近似正态（Bowley skewness < 0.12, IQR/std ≈ 1.35–1.41）。

2. **Rescue 预测**（helped vs stayed-wrong）：偏差 ~7.5%，但方向是**保守的**（parametric 低估真实 AUC）。stayed_wrong 组有中等右偏（Bowley 0.19–0.22, IQR/std 1.10–1.16 vs 正态理论值 1.349）。

3. **所有偏差 < 10%**，无结果改变方向或跨越显著性阈值。

### 建议

Rebuttal 可这样回应 R16：
- Disruption AUC：parametric 估计偏差 <2%，正态假设成立
- Rescue AUC：|log p| 有轻微右偏导致 ~7.5% 偏差，但 parametric 估计是**保守的**（实际 AUC 更高），不影响任何结论
- 建议在修订稿中同时报告 empirical AUC 以增强透明度

### 待补充

Shapiro-Wilk 正式检验需要原始 per-example |log p| 值（位于 `westb-48145:/root/entrainment_gated_ft/lm_eval_clean/`），当前 SSH 连接被拒。服务器恢复后可补充。

---
