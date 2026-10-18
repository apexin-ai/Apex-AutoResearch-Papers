# ops r6 paper corrections

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r6-paper-corrections_20260525T080649_result.json`
- **Structured JSON:** [`9de9075484216ba174f7.json`](../../sessions/9d/9de9075484216ba174f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修正报告

### 1. Adaptive R² "0.275" → "0.256"

论文中 adaptive R² **已经是 0.256**，无需修改：
- `results.tex:66` — `$R^2{=}0.256$ at $K{=}5$`
- `introduction.tex:16` — `$R^2 = 0.256$`

.tex 文件中唯一的 "0.275" 出现在 `appendix.tex:94`：
```
Weighted   & 2/12  & 7/12 & 0.275 \\
```
这是 **K=5 加权投票聚合的 R²**（Table aggregation_k5），不是 adaptive R²。两个是不同指标，不应修改。

### 2. CRVE 数字核对

`appendix.tex:39-41` 的 Crossed RE 表格数字与实际结果**完全一致**：

| K | K_eff FDR sig | η_max FDR sig | 论文 | 状态 |
|---|---|---|---|---|
| 3 | 0/12 | 1/12 | 0/12, 1/12 | ✓ |
| 5 | 8/12 | 3/12 | 8/12, 3/12 | ✓ |
| 7 | 8/12 | 2/12 | 8/12, 2/12 | ✓ |

Caption 中的描述也正确（"8/12 significance under crossed RE", "attenuation to 0/12"）。无需修改。

### 3. Fractional Logit 数字核对

**K_eff sig = 9/12 across all K — 论文已正确**：
- `results.tex:24` — K=3 表格：K_eff 9/12 ✓
- `results.tex:43` — "fractional logit giving 9/12" ✓
- `results.tex:99` — "9/12 across all panel sizes ($K{=}3,5,7$)" ✓
- `appendix.tex:159` — K=5 表格：K_eff 9/12 ✓
- `analysis.tex:15` — "fractional logit confirms the positive association (9/12 at all $K$)" ✓

**未发现旧值 11/12 或 12/12**（fractional logit K_eff）。

**η_max sig 存在差异**（需 Director 确认是否修改）：

| K | V2 确认值 | 论文当前值 | 位置 |
|---|---|---|---|
| 3 | 7/12 | 6/12 | `results.tex:24` |
| 5 | 6/12 | 4/12 | `appendix.tex:159` |
| 7 | 4/12 | 未出现在表格中 | — |

---

**结论：所有三项检查中，.tex 文件的目标数字均已正确或不适用，零改动。** Fractional logit 的 η_max sig 值与 V2 确认值有差异，需要 Director 判断是否属于需要修正的范围。

---
