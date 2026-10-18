# analysis k5 panel selection bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-panel-selection-bootstrap_20260523T061740_result.json`
- **Structured JSON:** [`a9ead4ba376d6f351a83.json`](../../sessions/a9/a9ead4ba376d6f351a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap 分析完成。结果摘要：

**Pairwise 显著性（B=9999, 95% CI）：**
| 对比 | 显著 conditions |
|---|---|
| min(η_max) vs random | **10/12** |
| min(K_eff) vs random | **10/12** |
| min(η_max) vs max(K_eff) | **11/12** |

**不显著的 2 个 condition** 均为 `arc_challenge×position_bias` 和 `arc_challenge×verbosity_bias`——这两个 condition 下所有策略的 ASR 都很高（~0.47），min(η_max) 选出的 panel 也无法有效抵抗，导致策略间差异不显著。

**Strategy-level bootstrap**（模拟 panel pool 不确定性）也确认 min(η_max) 策略稳定，CI 非常窄（大多数 condition 下 strategy bootstrap CI 几乎是点估计），说明该策略对 panel pool 的扰动不敏感。

---
