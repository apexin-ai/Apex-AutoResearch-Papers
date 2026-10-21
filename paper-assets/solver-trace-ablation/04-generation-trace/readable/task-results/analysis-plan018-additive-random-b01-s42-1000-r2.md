# analysis plan018 additive random b01 s42 1000 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan018-additive-random-b01-s42-1000-r2_20260515T112956_result.json`
- **Structured JSON:** [`76525ec60d40ae535092.json`](../../sessions/76/76525ec60d40ae535092.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结论：**negative**。

**结果摘要：**

| 指标 | 值 |
|---|---|
| eval_prove_rate | 1.0 (100/100) |
| eval_mean_isr | 0.3333 (std=0) |
| genuine_rate | 0% |
| tautological_collapse | **是** |

所有 100 个问题生成完全相同的 tautology `∀x (Person(x, "Google", x))`，premise=conclusion，ISR 固定在 1/3。与 500 步版本 (PR=0.79) 相比，1000 步时模型已完全崩塌。

**关键发现**：additive random reward β=0.1 只延迟了 tautological collapse，未能阻止。500→1000 步过程中，模型从部分崩塌 (PR=0.79) 恶化为完全崩塌 (PR=1.0, 纯 tautology)。这比 exec-only 1000 步 (PR=0.96, ISR=0.003) 的 Goodhart 效应更极端——random 噪声反而加速了向 tautology 的收敛。

---
