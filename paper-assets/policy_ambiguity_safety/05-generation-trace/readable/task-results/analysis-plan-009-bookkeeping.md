# analysis plan 009 bookkeeping

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_bookkeeping_20260522T005954_result.json`
- **Structured JSON:** [`b3a652b2a89a517906bb.json`](../../sessions/b3/b3a652b2a89a517906bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 数据完整性评估: **PASS**

两个文件均存在且结构完整：

| 文件 | n | 关键指标 | 支持 hypothesis |
|------|---|---------|----------------|
| `llm_agreement.json` | 100 | κ_w=0.685, exact=76%, binary κ=0.740 | ✓ (≥0.60) |
| `agreement_results.json` | 100 | inter-annotator κ_w=0.762, human-LLM pooled κ_w=0.807 | ✓ |

Hypothesis confirmed: cross-judge weighted κ = 0.685 > 0.60 threshold. Human-LLM agreement (0.807) even exceeds cross-judge agreement, validating the dual-judge design.

### 2. 建议的 Registry Metrics

```json
{
  "conclusion": "success",
  "cross_judge_kappa_weighted": 0.685,
  "cross_judge_exact_agreement": 0.76,
  "cross_judge_binary_kappa": 0.740,
  "human_llm_pooled_kappa_weighted": 0.807,
  "human_inter_annotator_kappa_weighted": 0.762,
  "n_episodes": 100,
  "hypothesis_supported": true
}
```

### 3. 额外发现（论文可能未使用）

**plan_009 文件包含论文 `dual_judge_calibration.json`(κ=0.6528, κ_w=0.7752) 之外的信息：**

1. **Confusion matrix 揭示系统性偏差**：当 gpt-5.4 判定 moderate 时，gpt-4.1 在 9/19 cases 升级为 critical。gpt-4.1 在 moderate/critical 边界更严格。

2. **Per-type agreement 差异显著**：
   - 最低：authorization_scope (exact=58.8%, calibration κ=0.38)
   - 最高：lexical (exact=93.8%, calibration κ=0.71)
   - 这与 A3 judge-group ranking 相关——如果某些 type 的 judge disagreement 更高，该 type 的 violation rate 估计可信度更低。

3. **Human-LLM 一致性数据**（agreement_results.json 独有）：
   - annotator1 与 LLM: κ_w=0.868（很高）
   - annotator2 与 LLM: κ_w=0.745
   - annotator2 标注极度保守（83/100 标为 none），annotator1 更敏感（58/100 为 none）

4. **Per-model κ（calibration 文件）**：gpt-5.4 agent 的 episodes judge agreement 最低(0.54)，gpt-4.1 agent 的 episodes 完美一致(1.0)——暗示 gpt-5.4 的行为更 borderline，更难判定。

5. **McNemar test**（p=0.61）确认两个 judge 无系统性方向偏差，仅在 severity 粒度上有分歧。

**值得补充进论文的**：per-type agreement 差异（authorization_scope 和 coreferential 低 agreement）可以在 discussion/limitations 中作为 judge reliability varies by type 的 nuance 提及。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "conclusion": "success",
    "cross_judge_kappa_weighted": 0.685,
    "cross_judge_exact_agreement": 0.76,
    "cross_judge_binary_kappa": 0.74,
    "human_llm_pooled_kappa_weighted": 0.807,
    "human_inter_annotator_kappa_weighted": 0.762,
    "n_episodes": 100,
    "hypothesis_supported": true
  }
}
```

</details>

---
