# analysis k5 panel selection

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-panel-selection_20260523T030919_result.json`
- **Structured JSON:** [`fd021a8eee1d2111a258.json`](../../sessions/fd/fd021a8eee1d2111a258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**K=5 下 min(η_max) 和 min(K_eff) 完全收敛，假设不成立。**

| 策略 | Avg ASR | Wins |
|------|---------|------|
| min(η_max) | 0.0767 | 0 (tie) |
| min(K_eff) | 0.0767 | 0 (tie) |
| random | 0.1092 | — |
| max(K_eff) | 0.1940 | — |

核心发现：
- **12/12 条件全是 tie**：min(η_max) 和 min(K_eff) 在大多数条件下选中**完全相同的 panel**（均选择 API frontier models: claude-opus, gpt-5.5, gemini-3.1-pro, gpt-4.1, gemini-3.5-flash）
- 原因：低 η_max（个体鲁棒）和低 K_eff（高一致性/低多样性）在 K=5 下是**正相关**的——强模型既个体鲁棒又彼此一致
- max(K_eff) 始终最差（选弱模型 panel），验证了 K_eff 正方向 = harmful 的判断
- position_bias 条件下所有策略 ASR 都高（~0.47），majority vote 无法修复

---
