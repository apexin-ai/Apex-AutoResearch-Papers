# analysis e1 confidence selection

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e1_confidence_selection_20260522T095139_result.json`
- **Structured JSON:** [`9dca8ecf4c4ae85681f0.json`](../../sessions/9d/9dca8ecf4c4ae85681f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

E1 完成。结果总结：

| Benchmark | MV | Best Single | Max-Conf | Rescue-Thresh | CW-Vote | Oracle |
|-----------|-----|-------------|----------|---------------|---------|--------|
| LAMBADA | .5090 | .5089 | .5254(+1.6) | **.5623(+5.3)** | .5272(+1.8) | .6546 |
| HellaSwag | .5952 | .6008 | .5964(+0.1) | .5950(-0.0) | .5952(+0.0) | .6686 |
| PIQA | .7402 | .7317 | .7289(-1.1) | .7341(-0.6) | .7307(-0.9) | .7956 |
| ARC-Easy | .7062 | .7133 | .7109(+0.5) | **.7164(+1.0)** | .7141(+0.8) | .8084 |

核心发现：

1. **Rescue-threshold routing 在 LAMBADA 上大幅领先**：+5.33pp vs MV，阈值稳定在 |logp|=1.72±0.17，与 A2 的 rescue threshold（~3.3）不同——E1 用的是跨架构 routing（per-arch pure/hybrid 决策再 MV），而 A2 是 within-arch 预测
2. **ARC-Easy** 也有中等改善（rescue +1.0pp，CW +0.8pp）
3. **HellaSwag/PIQA 无改善**——与 A2 中这两个 benchmark 的低 AUC（0.51-0.56）一致，confidence signal 太弱无法支持 routing
4. Oracle upper bound（任一架构答对即算对）显示 LAMBADA 有 65.5%、ARC-Easy 有 80.8% 的潜力，说明架构间的互补性很强

分析脚本: `/root/entrainment_gated_ft/analysis/e1_confidence_selection.py`
结果 JSON: 已注册为 artifact `art_20260522_e4231e`

---
