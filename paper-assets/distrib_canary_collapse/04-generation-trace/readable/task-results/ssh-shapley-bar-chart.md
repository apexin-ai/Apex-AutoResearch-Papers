# ssh shapley bar chart

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_shapley_bar_chart_20260517T093022_result.json`
- **Structured JSON:** [`90ab4abc8b65b2c0ac68.json`](../../sessions/90/90ab4abc8b65b2c0ac68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出

1. **PDF/PNG**: `docs/paper/figures/shapley_method_contribution.pdf` (服务器) + 本地 artifacts 已注册

2. **ΔFPR / ΔFNR 数值** (baseline FPR=25.0%, FNR=0.0%):

| Method | ΔFPR | ΔFNR |
|---|---|---|
| Naive XCorr | **-25.0%** | +25.0% |
| Diff XCorr | **-25.0%** | +25.0% |
| Threshold Onset | -6.2% | +25.0% |
| Perm Granger | -18.8% | **0.0%** |
| TY Granger | 0.0% | 0.0% |

3. **关键发现**:
   - **Naive XCorr & Diff XCorr** 是双刃剑：同时驱动 FP 和 sensitivity，移除任一方法 FPR 降 25% 但 FNR 升 25%
   - **Perm Granger** 是纯 FP 过滤器：移除后 FPR 降 18.8%，FNR 不受影响
   - **Threshold Onset** 主要贡献 sensitivity（+25% ΔFNR），FPR 贡献较小（-6.2%）
   - **TY Granger** 对 consensus 决策零边际贡献（移除无影响）

---
