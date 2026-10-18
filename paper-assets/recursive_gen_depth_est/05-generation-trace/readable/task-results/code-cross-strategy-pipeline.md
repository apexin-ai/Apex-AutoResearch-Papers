# code cross strategy pipeline

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_strategy_pipeline_20260517T084621_result.json`
- **Structured JSON:** [`7d563d1d70bd25e1db99.json`](../../sessions/7d/7d563d1d70bd25e1db99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `cross_strategy_pipeline_001` 完成，已注册 registry 和 artifact。

**结果摘要：**

| | Pipeline | Oracle | LOO Baseline | 提升 |
|---|---|---|---|---|
| Pythia-1.4B | 69.3% | 74.6% | 61.2% | +8.0pp |
| OLMo-1B | 69.4% | 78.4% | 59.5% | +9.9pp |
| GPT-2 XL | 73.0% | 81.9% | 56.6% | +16.4pp |
| **Mean** | **70.5%** | **78.3%** | **59.1%** | **+11.5pp** |

**策略分类器**：RF 57.8% / LR 52.9%（远低于 90% 假设）
**关键发现**：即使策略分类只有 ~58%，pipeline 仍有效，因为误路由的样本在"相邻"策略的深度分类器上仍能获得合理预测。策略分类错误时深度准确率仍有 64-72%。

---
