# analysis plan009 vif multicollinearity

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan009-vif-multicollinearity_20260522T070002_result.json`
- **Structured JSON:** [`9b5715835ff950875a27.json`](../../sessions/9b/9b5715835ff950875a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 输出完整（271 行）。以下是完整结果摘要：

---

## Plan 009 VIF 多重共线性分析结果

### Summary

| 指标 | 值 |
|---|---|
| Mean VIF(K_eff) | 2.9943 (range: 1.01–10.02) |
| K_eff residualized 显著 | **1/12** |
| η_max Bonferroni 显著 | **3/12** |
| η_max FDR 显著 | **6/12** |
| Beta vs OLS concordance | **11/12** |

### 关键发现

**1. VIF 共线性程度**
- 大多数条件 VIF 在 1.0–5.4，共线性温和（≤5 可接受）
- `arc_challenge__position_bias` VIF=10.02，严重共线性
- `mmlu__score_manipulation` VIF=5.43，边缘

**2. Residualized K_eff → 真实效应检验**
- 12 个条件中仅 `arc_challenge__sycophancy` 的 residualized K_eff 显著（β=-2.85, p=0.013）
- 其余 11 个条件中，去除 η_max 后 K_eff 对 ASR 无独立解释力
- 结论：**K_eff 的 non-significance 不是共线性伪影，而是真的不重要**（仅 1 个例外）

**3. η_max 多重校正**
- Bonferroni 校正后仍显著 3/12：`mmlu__sycophancy` (p=0.046), `arc_challenge__sycophancy` (p=0.011), `arc_challenge__authority_bias` (p=0.037)
- FDR 校正后显著 6/12，新增：`arc_challenge__prompt_injection`, `mmlu__verbosity_bias`, `arc_challenge__verbosity_bias`
- η_max 效应在严格校正后仍部分存活

**4. Beta regression vs OLS**
- 11/12 条件两种方法结论一致
- 唯一不一致：`arc_challenge__position_bias`（OLS 两个都不显著，Beta reg 两个都显著 — 受 VIF=10 影响最大的条件）
- OLS 结论总体稳健

**5. 特殊条件**
- `arc_challenge__sycophancy`：唯一 K_eff 显著的条件（partial r=-0.64, p=0.002），K_eff 有独立负效应
- `mmlu__position_bias`：partial r=0.49 (p=0.03) 但 residualized β 不显著（p=0.10），边缘

---
