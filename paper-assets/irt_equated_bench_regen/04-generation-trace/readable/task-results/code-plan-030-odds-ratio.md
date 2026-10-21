# code plan 030 odds ratio

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_030_odds_ratio_20260521T100139_result.json`
- **Structured JSON:** [`a677814fd42bc95644ed.json`](../../sessions/a6/a677814fd42bc95644ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 register_artifact 工具可用。任务已完成，总结结果：

**验证通过**: Model 1 coef=4.3928, McFadden R²=0.0007，与 plan_019 完全一致。

**核心发现**:

| | Model 1 (domain Δ) | Model 2 (+item props) | Model 3 (item Δ) | Model 4 (+item props) |
|---|---|---|---|---|
| McFadden R² | 0.0007 | 0.0423 | 0.0012 | **0.0434** |
| Nagelkerke R² | 0.0012 | 0.0720 | 0.0021 | **0.0737** |
| AIC | 15545 | 14902 | 15537 | **14885** |

- **Item-level accuracy change (M3) 比 domain-level delta (M1) 更好**: AIC 15537 vs 15545, Nagelkerke R² 0.0021 vs 0.0012
- **Item properties 是主要驱动力**: 加入 difficulty + discrimination 后 R² 从 ~0.001 跳到 ~0.07 (LR χ² > 646, p ≈ 0)
- **Simpson's paradox 同样出现**: accuracy change 的 OR 在控制 item properties 后反转（M3: OR=2.11 → M4: OR=0.44; M1: OR=80.9 → M2: OR=0.045）
- **OR 在合理范围内**: 以 per 0.10 单位计算，M1 subject_acc_delta OR=1.55 [1.19, 2.03]，无极端值
- **所有模型 Hosmer-Lemeshow p=0.000**: 拟合不佳，但在 N=12508 时 HL test 几乎必然显著

**输出文件**:
- `artifacts/plan_030_odds_ratio/plan_030_odds_ratio.py` — 分析脚本
- `artifacts/plan_030_odds_ratio/odds_ratio_report.md` — 完整统计报告

---
