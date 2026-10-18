# analysis confidence margin within category

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_confidence-margin-within-category_20260520T035123_result.json`
- **Structured JSON:** [`4e175053a421d6181836.json`](../../sessions/4e/4e175053a421d6181836.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**结论：`within_category_significant`** — 类内对照消除定义性混淆后，confidence margin 仍然显著预测 attention 效果。

### Control 1: Pure-correct 内部（hurt vs stayed-right）

| 架构 | hurt n | stayed-right n | hurt mean |loglik| | stayed-right mean |loglik| | Cohen's d | p |
|------|--------|----------------|-----------|-----------|-----------|---|
| GDN | 519 | 2281 | 1.049 | 0.576 | 0.87 | 1.4e-66 |
| RetNet | 497 | 2169 | 1.293 | 0.785 | 0.83 | 5.6e-60 |
| HGRN2 | 392 | 2102 | 1.481 | 0.899 | 0.92 | 8.4e-55 |

Hurt 样本的 |loglik| 显著更高（target 概率更低 = 勉强答对），确认弱正确答案更容易被 attention 翻转。

### Control 2: Pure-wrong 内部（helped vs stayed-wrong）

| 架构 | helped n | stayed-wrong n | helped mean |loglik| | stayed-wrong mean |loglik| | Cohen's d | p |
|------|----------|----------------|-------------|-------------|-----------|---|
| GDN | 480 | 1873 | 2.459 | 4.189 | -0.75 | 1.9e-67 |
| RetNet | 420 | 2067 | 2.478 | 4.103 | -0.73 | 1.8e-60 |
| HGRN2 | 548 | 2111 | 2.500 | 4.112 | -0.77 | 1.1e-81 |

Helped 样本的 |loglik| 显著更低（target 概率更高 = 差一点就对），确认 near-miss 错误答案更容易被 attention 拯救。

两个对照组在 3 个架构上方向完全一致、效应量大（|d| = 0.73–0.92），原始 across-category 效应不是定义性 artifact。

---
