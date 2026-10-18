# ops r6 collect previous results

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r6-collect-previous-results_20260525T064822_result.json`
- **Structured JSON:** [`8eb9860f3b2ccfe0b2c0.json`](../../sessions/8e/8eb9860f3b2ccfe0b2c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 7 项分析结果已收集并汇总到 `r6_previous_results_summary.md`。核心发现：

**MC 校准 (PID 18494)**: 已完成，耗时 9.2h。WCB 在所有 36 条件下均不 over-reject（最坏仅 1.6%，远低于 α=0.05），检验保守可信。

**跨分析一致性**:
- K_eff 效应 robust：fractional logit V2 稳定 9/9/9，crossed RE K5/K7 达 8/8
- K=3 crossed RE 全灭 (0/12) 是 SE inflation 问题（仅 15 clusters, df=14），不是效应消失
- β_std(K_eff) 非单调轨迹 (0.349→0.437→0.401) 已由 Bayesian posterior entropy 的双重压缩机制完整解释
- API-only 子集效应量反而更大 (1.8x)，但 panel 数不足导致功效归零
- quant_frac 交互项仅 K=3 有信号且 VIF 极高，不 robust

**缺失**: Adaptive R² 数据未找到；crossed RE 使用了旧模型名称

---
