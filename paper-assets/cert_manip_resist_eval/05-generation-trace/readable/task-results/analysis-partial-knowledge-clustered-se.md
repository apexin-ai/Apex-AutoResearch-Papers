# analysis partial knowledge clustered se

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partial-knowledge-clustered-se_20260523T012338_result.json`
- **Structured JSON:** [`62bd77c0137704225cf7.json`](../../sessions/62/62bd77c0137704225cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。四方对比表：

| Method | η_max FDR sig | K_eff FDR sig | η_β mean | K_β mean |
|---|---|---|---|---|
| Oracle OLS | 11/12 | 8/12 | 0.387 | 0.164 |
| Oracle Clustered SE | 8/12 | 0/12 | — | — |
| **Partial OLS** | 12/12 | 5/12 | 0.589 | -0.011 |
| **Partial Clustered SE** | **12/12** | **0/12** | **0.589** | **-0.011** |

Partial-knowledge + clustered SE 结果：η_max **12/12** 全部显著（甚至比 oracle clustered SE 的 8/12 更强），K_eff **0/12**。η_max 平均 β=0.589，SE inflation 均值 2.55x。

核心结论：η_max 在最保守的双重条件下（不完整信息 + clustered SE 推断）仍是唯一显著预测因子，partial knowledge 下的 averaging 平滑了噪声反而增强了 η_max 的信号。

---
