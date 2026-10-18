# analysis r16 w1 routing variance

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203_result.json`
- **Structured JSON:** [`2f5b5e122f263e777936.json`](../../sessions/2f/2f5b5e122f263e777936.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Routing Variance Report

**数据来源**: `artifacts/_project/data/e1_confidence_selection.json`
**方法**: rescue_threshold routing vs majority vote, 50/50 split × 10 repeats, 3 architectures (GDN, RetNet, HGRN2), h3-1

### 限制

本地仅有聚合统计量（各策略跨 10 splits 的 mean/std），**无 per-split paired data**。因此 SD_gain 和 paired t-test 需要假设 splits 间 routing 与 MV accuracy 的相关系数 r。下面报告 conservative bound (r=0, 等效 unpaired Welch test)：

### Conservative Report (r=0, worst case)

```
LAMBADA:   mean=+5.3pp, SD=0.77pp, 95% CI=[+4.8, +5.9], p<0.0001
ARC-Easy:  mean=+1.0pp, SD=0.92pp, 95% CI=[+0.4, +1.7], p=0.0065
HellaSwag: mean=-0.0pp, SD=0.68pp, 95% CI=[-0.5, +0.5], p=0.9275
PIQA:      mean=-0.6pp, SD=1.47pp, 95% CI=[-1.7, +0.4], p=0.2239
```

### 关键结论

- **LAMBADA**: 即使用最保守的 unpaired 假设，p < 0.0001，gain 高度显著
- **ARC-Easy**: p = 0.0065，显著（实际 paired test 的 p 会更小）
- **HellaSwag**: gain ≈ 0，无显著差异
- **PIQA**: 实际 gain = -0.6pp（论文报告为 0），无显著差异（p=0.22）

### 精确计算需要的数据

per-split paired data（10 组 routing acc 和 MV acc 配对值）不在本地。可能在 westb-48145 服务器上的以下路径：
- `/root/entrainment_gated_ft/analysis/` 或 `/root/entrainment_gated_ft/results/`
- 生成 `e1_confidence_selection.json` 的分析脚本的中间输出

如果需要精确 paired t-test，需 SSH 到服务器提取 per-split 数据，或重新运行分析脚本保存 per-split 结果。

---
