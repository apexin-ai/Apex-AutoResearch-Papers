# analysis component count compare

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_component-count-compare_20260514T033913_result.json`
- **Structured JSON:** [`cf956b1ad15209d95404.json`](../../sessions/cf/cf956b1ad15209d95404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Artifact 已写入 `artifacts/component_count_analysis.md`。

核心结论：

**D017 假设完全成立。plan013 random reward 的 ISR≈0.5 是退化行为，不是结构质量。**

关键数据：

| | plan001 (exec-only) | plan013 (random reward) |
|---|---|---|
| mean n_components | **6.58** | **2.04** |
| std n_components | 3.15 | **0.20** |
| 分布 | 4-12 范围，正常多前提 formalization | **100% 在 1-3 bucket**，几乎全是恰好 2 个组件 |
| prove rate | 93% | 100% |
| mean ISR | 0.123 | 0.535 |

机制：random reward 无梯度信号指导 formalization 质量，模型收敛到最短合法输出（1 premise + 1 conclusion = 2 组件）。Solver 可轻松证明这种退化 formalization → prove_rate=100%。ISR = 1 necessary / 2 total = 0.5，纯粹是分母缩小的结果。

93/100 样本中 plan013 组件数少于 plan001（Wilcoxon p<0.0001）。这是典型的 **reward hacking via output length minimization**。

---
