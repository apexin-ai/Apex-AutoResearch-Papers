# analysis unified rho n8 seed123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_unified_rho_n8_seed123_20260515T145442_result.json`
- **Structured JSON:** [`545260d465e6b71e4ec7.json`](../../sessions/54/545260d465e6b71e4ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成，3 个配置已追加到 JSON。交叉验证与 report.json 一致（如 qwen_n8_seed123 SJ=0.3878 匹配 report 的 0.38784，FK=0.2628 匹配 0.26281）。

**新增结果汇总：**

| 配置 | SJ | FK | VC | EM | LP | auroc_SJ | auroc_FK | auroc_VC | auroc_EM | auroc_LP |
|---|---|---|---|---|---|---|---|---|---|---|
| **qwen_scierc_n8_seed42** | 0.3599 | 0.2665 | 0.3792 | 0.2945 | 0.2052 | 0.6500 | 0.6019 | 0.6627 | 0.6138 | 0.5778 |
| **qwen_scierc_n8_seed123** | 0.3878 | 0.2628 | 0.4133 | 0.3135 | 0.2341 | 0.6813 | 0.6183 | 0.6898 | 0.6439 | 0.5898 |
| **llama_scierc_n8_seed123** | 0.3552 | 0.2897 | 0.4193 | 0.2844 | 0.1970 | 0.6399 | 0.5974 | 0.6715 | 0.6027 | 0.5722 |

**RE metrics（joint subtask, n=397）：**

| 配置 | re_FK | re_SJ |
|---|---|---|
| qwen_scierc_n8_seed42 | 0.2752 | 0.2503 |
| qwen_scierc_n8_seed123 | 0.2908 | 0.2486 |
| llama_scierc_n8_seed123 | 0.2555 | 0.2462 |

验证通过：
- 所有配置 n_valid=529（551-22 gold-empty）
- ρ 值范围合理，与 seed42 同配置差异在正常 seed 波动内
- 已追加到 `output/analysis_unified_rho_full.json`

---
