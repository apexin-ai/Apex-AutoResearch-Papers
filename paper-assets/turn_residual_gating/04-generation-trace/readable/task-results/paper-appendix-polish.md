# paper appendix polish

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_polish_20260523T150117_result.json`
- **Structured JSON:** [`2c9415fc09c3e37fcdaf.json`](../../sessions/2c/2c9415fc09c3e37fcdaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary:

## 修复项

1. **Line 180 — 事实错误**: "Llama's larger intermediate dimension (14336 vs. 18944)" → "Llama's larger layer count (32 vs. 28 layers)"。原文自相矛盾：14336 < 18944，Llama 的 intermediate dim 更小。Llama 训练更慢的原因是层数多（32 vs 28）。

2. **Line 273 — 附录内部重复**: Per-Layer Gate Profile 节末尾的 cross-model comparison 段落与同一附录 §6.2 (Cross-Model Gate Profile Comparison) 大段重复。改为引用 §6.2 + Figure ref，保留一句结论。

3. **Line 337 — 与主文/附录重复**: Qualitative Steering Examples 末段重复了 discussion.tex 和 appendix §IR 的 content/format constraint 对比。缩减为引用 §analysis + Table ref。

## 引用完整性
- 无 `??`、`\cite{TODO}` 或空引用
- `sec:appendix-steering` label 在 `table_steering_full.tex`（\input 引入），正常

## 格式一致性
- 变量均在 math mode，数字精度统一，表格格式一致，无问题

## 未修复的问题（需讨论）

- **Line 283**: "Training time increases approximately 60%" 与 cost table 不符——s42 是 +8% (6.5h vs 6.0h)，s123 是 +80% (10.8h vs 6.0h)，60% 与两者均不匹配。需要确认作者意图后再改。

---
