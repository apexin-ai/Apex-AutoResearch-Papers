# code plan 012 irt theta

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_012_irt_theta_20260520T215924_result.json`
- **Structured JSON:** [`d70d54d48ead35abafa4.json`](../../sessions/d7/d70d54d48ead35abafa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**成功标准未达成**（temporal cohort，FPR < 0.10 且 TPR > 0.70 @ p=0.5）。

### 核心发现

**Temporal cohort — θ-conditioning 无效**：
| Variant | Baseline FPR | TPR@p=0.5 |
|---------|-------------|-----------|
| external_5 (plan_011) | 0.314 | 0.834 |
| theta_eq_10 | 0.335 | 0.882 |
| theta_qt_20 | 0.312 | 0.876 |

FPR 在 31-35% 范围内，所有 θ 变体与 plan_011 的 total-score 基线无实质差异。原因：logit(p) 与 total score 相关性 0.9986，分层效果几乎等价。

**Ability cohort — quantile θ bins 大幅降低 FPR**：
| Variant | Baseline FPR | TPR@p=0.5 | TPR@p=1.0 |
|---------|-------------|-----------|-----------|
| external_5 | 0.493 | 0.756 | 0.800 |
| theta_qt_10 | **0.093** | 0.206 | 0.544 |
| theta_qt_20 | **0.079** | 0.210 | 0.544 |

FPR 从 49% 降到 8%，但 TPR 也从 76% 降到 21%（p=0.5）。更精确的能力匹配同时消除了 FPR 和 TPR——说明 plan_011 中 ability cohort 的高 TPR 主要来自能力差异的混淆，而非真正的 DIF 检测。

**Enrichment（Li et al.）**：所有变体 enrichment ≈ 0.97-1.00，与 plan_001 的 0.96 一致——Li et al. 标记的污染仍然是 non-differential 的。

### 关键结论

1. Temporal cohort 的 ~31% baseline FPR 是**真实 DIF**（2023 vs 2024 模型在某些 items 上的真实差异），而非能力匹配不精确造成的伪阳性。更精细的 θ 分层无法消除它。
2. 简单的 logit θ 变换与原始总分几乎完全共线，不提供额外的匹配价值。真正的改进需要多维 IRT 或其他非线性能力估计。

---
