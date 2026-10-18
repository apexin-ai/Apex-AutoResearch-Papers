# ops experiment plan sync

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_experiment-plan-sync_20260523T201917_result.json`
- **Structured JSON:** [`c9dabc400dc053764407.json`](../../sessions/c9/c9dabc400dc053764407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。汇总：

**更新为 done（6 条）：**
| Plan | Registry ID | 说明 |
|------|-------------|------|
| plan_001 | `plan001_step1_full_v4` | 直接匹配，15模型全流水线 |
| plan_003 | `plan001_step1_full_v4` | 子分析 k5_rf_contrast，BFT framing confirmed |
| plan_004 | `plan001_step1_full_v4` | 子分析 capability_matched |
| plan_008 | `plan001_step1_full_v4` | 子分析 cross_k_bootstrap_summary (K3-K7) |
| plan_009 | `plan001_step1_full_v4` | 子分析 VIF/fractional logit/Cinelli-Hazlett |
| plan_010 | `plan001_step1_full_v4` | 子分析 k5_aggregation_bootstrap |

**仍为 planned（6 条）：**
| Plan | 原因 |
|------|------|
| plan_002 | 特定攻击类型（few-shot hijacking, persona manipulation, instruction override）未在 registry 中确认 |
| plan_005 | 两阶段面板设计算法，无对应 registry 实验 |
| plan_006 | Per-judge ASR 集中度分析（Gini/entropy），未完成 |
| plan_007 | Diversity-capability tradeoff 可视化，未完成 |
| plan_011 | Open-ended generation benchmark，未完成 |
| plan_012 | Partial-knowledge adversary model，未完成 |

同时为 3 条 MVP 条目补充了 `status: done` 字段，保持格式一致。

---
