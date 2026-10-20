# analysis carr feasibility dryrun

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_feasibility_dryrun_20260517T012147_result.json`
- **Structured JSON:** [`1f5aa3da92e1c1f501f6.json`](../../sessions/1f/1f5aa3da92e1c1f501f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/carr_dryrun_feasibility_report.md`。

## 核心结论

**CARR 机制正确但在当前 setting 下几乎无增量**（99.3% selection overlap）。

根本原因：三个 proxy score 维度高度相关（r=0.63-0.77）。候选好就三维都好，改权重几乎不改变 argmax。

| 发现 | 数据 |
|------|------|
| 权重变动 | diversity 从 0.333 漂移到 0.354，太小 |
| 即使 eta=10 | overlap 仍 >87% |
| 极端单维权重 (1,0,0) | overlap 仍 >61%（相关性天花板） |
| 候选内方差逐代下降 | Gen0: 0.0055 → Gen2: 0.0028 |

## CARR 有价值的条件

1. 维度间**弱相关或反相关**（需要真实独立 reward model，不是文本 heuristic）
2. 某维度**主动退化**（collapse scenario）
3. 候选间 score 方差足够大（模型早期 or 高温度采样）

## 建议下一步

- 用真实 ArmoRM per-sample scores + embedding-based diversity + 任务特异 complexity reward 重跑
- 或者设计 collapse 诱导实验（quality-only 训几代后引入 CARR 看能否挽救 diversity）

---
