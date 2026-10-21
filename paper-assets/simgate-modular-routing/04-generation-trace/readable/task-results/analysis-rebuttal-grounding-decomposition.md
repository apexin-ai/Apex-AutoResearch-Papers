# analysis rebuttal grounding decomposition

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rebuttal-grounding-decomposition_20260523T205442_result.json`
- **Structured JSON:** [`4b8df23e8750a0d61f33.json`](../../sessions/4b/4b8df23e8750a0d61f33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/rebuttal_grounding_decomposition.md`。核心结论：

**Grounding prompt 将 internal death rate 从 50.3% 降至 35.0%（−15.3pp），但 death 仍然是压倒性的 routing signal：**

| 指标 | Baseline | Post-Grounding |
|------|----------|----------------|
| DAF | 100.0% | 99.4% |
| Label fraction | 100.0% | 93.2% |
| Δ\_nd (both-alive gap) | 0.00 | 0.09 |
| death\_asymmetry | 65 | 69 (反而增加) |
| score\_comparison | 0 | 5 |

关键机制：grounding 减少 internal 死亡 → both\_dead 减半（32→16）→ 更多不对称死亡 → death\_asymmetry 反增。internal-preferred 从 5→23，因为 internal 存活但 det 死亡的情况增多。

一个异常值：identify-life-stages-2（n=10）grounding 后 death rate 反升至 80%，样本量小需谨慎解读。

---
