# code exp multi source detection

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_multi_source_detection_20260520T065243_result.json`
- **Structured JSON:** [`61d8f521b0ea19fd6733.json`](../../sessions/61/61d8f521b0ea19fd6733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Mixed-source K\* = 2**，与所有单源 K\*=2 完全一致。

| Pair | No Label AUC | No Label 95% CI | With Label AUC | With Label 95% CI |
|------|-------------|-----------------|----------------|-------------------|
| 0v1 | 0.9929 | [0.9915, 0.9942] | 0.9948 | [0.9937, 0.9958] |
| 1v2 | **0.7007** | **[0.6874, 0.7142]** | **0.7015** | **[0.6880, 0.7149]** |
| 2v3 | 0.5128 | [0.4988, 0.5268] | 0.5174 | [0.5033, 0.5316] |
| 3v4 | 0.4958 | [0.4816, 0.5100] | 0.4950 | [0.4808, 0.5093] |
| 4v5 | 0.5049 | [0.4908, 0.5189] | 0.5018 | [0.4877, 0.5157] |

关键发现：

1. **K\* 不受多源混合影响**：mixed-source K\*=2，与 Qwen/Pythia/OLMo 单源 K\*=2 完全相同
2. **Generator label 几乎无用**：加 generator_id 作为第 16 维特征后，AUC 变化 < 0.005，K\* 不变
3. **Depth 2+ 均为 chance level**：2v3 及之后的 pairwise AUC 均在 0.49-0.52 范围，CI 跨 0.50

数据来源：Qwen-1.5B (`data_exp016_qwen_base`)、Pythia-1.4B (`data_exp020_pythia_greedy`)、OLMo-1B (`data/olmo_c4_cont`)，各 1000 docs，合计 3000 docs × 6 depths = 18000 rows。Registry 已更新为 DONE(success)。

---
