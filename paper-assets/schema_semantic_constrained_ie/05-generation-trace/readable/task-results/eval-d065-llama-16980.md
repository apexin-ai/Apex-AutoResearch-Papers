# eval d065 llama 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d065-llama-16980_20260520T082049_result.json`
- **Structured JSON:** [`60acaad4b40bd778703f.json`](../../sessions/60/60acaad4b40bd778703f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

```
Llama unc 4096: E-F1=84.77, R-F1=44.55, DR=0.49%, CF=0.08%, ET=0.00%, RV=0.15%
Llama con 4096: E-F1=84.71, R-F1=44.70, DR=0.00%, CF=0.26%, ET=0.00%, RV=0.00%
```

### Table 2 w5 对比

| 指标 | w5 unc | d065 unc 4096 | Δ | w5 con | d065 con 4096 | Δ |
|------|--------|---------------|---|--------|---------------|---|
| E-F1 | 83.45 | **84.77** | +1.32 | 83.40 | **84.71** | +1.31 |
| R-F1 | 44.70 | 44.55 | −0.15 | 44.83 | 44.70 | −0.13 |
| DR% | 0.30 | 0.49 | +0.19 | 0.00 | **0.00** | = |
| CF% | 0.07 | 0.08 | +0.01 | 0.16 | 0.26 | +0.10 |
| RV% | 0.11 | 0.15 | +0.04 | 0.00 | **0.00** | = |
| PF% | 4.80 | **2.30** | −2.50 | 5.01 | **2.61** | −2.40 |

**关键发现**：
- **PF% 大幅下降**（4.8→2.3%, 5.0→2.6%）：4096 token 上限显著减少截断导致的 parse failure
- **E-F1 提升 ~1.3 点**：更少 PF 意味着更少 entity FN（PF-as-FN 方法下直接受益）
- **R-F1 基本持平**（差 <0.2）：更多成功解析的文档中有些关系预测不够准确，抵消了 PF 减少的收益
- **Con 约束效果一致**：RV 和 DR 均为 0，约束解码完全消除了 vocabulary 和 domain-range violation
- **CF 略升**（con 0.16→0.26%）：更长输出中实体出现次数更多，跨字段一致性违反相应增加

---
