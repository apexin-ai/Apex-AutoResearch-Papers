# code registry degen update

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_registry_degen_update_20260518T204527_result.json`
- **Structured JSON:** [`04dfdee64d2d86a73e83.json`](../../sessions/04/04dfdee64d2d86a73e83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 22 个实验更新完成。汇报如下：

## 更新汇总（22 个实验）

### Qwen3-8B SciERC T=1.0
| exp_id | seed | 旧值 | 新值 (unified) |
|--------|------|------|----------------|
| exp_012_rerun_1024 | 42 | 无(12.59% sample_f1) | **17.77%** |
| exp_018_qwen_scierc_seed123 | 123 | null(11.67%) | **17.20%** |
| exp_018_qwen_scierc_seed456 | 456 | null(13.26%) | **20.42%** |

### Qwen3-8B CoNLL T=1.0 N=16
| exp_id | seed | 旧值 | 新值 |
|--------|------|------|------|
| exp_002_conll_n16 | 42 | 无(7.58%) | **48.44%** |

### LLaMA3.1-8B SciERC T=1.0
| exp_id | seed | 旧值 | 新值 |
|--------|------|------|------|
| exp_018_llama_scierc_seed42_r1024 | 42 | 无(11.44%) | **24.95%** |
| exp_018_llama_scierc_seed123 | 123 | null(11.11%) | **26.65%** |
| exp_018_llama_scierc_seed456_r1024 | 456 | 无(11.65%) | **27.41%** |
| exp_007_llama_scierc_seed123 | 123 | degen_pct=26.7 | **26.65%** |
| exp_llama_scierc_seed456 | 456 | degen_pct=27.6 | **27.41%** |

### LLaMA3.1-8B CoNLL T=1.0 N=16
| exp_id | seed | 旧值 | 新值 |
|--------|------|------|------|
| exp_017_llama_conll_n16_r1024 | 42 | 无(4.29%) | **86.47%** |
| exp_017_llama_conll_n16_s123_r1024 | 123 | null(4.30%) | **86.36%** |
| exp_017_llama_conll_n16_s456_r1024 | 456 | 无(4.29%) | **86.72%** |

### T 消融 (SciERC, Qwen3-8B)
| exp_id | T | 旧值 | 新值 |
|--------|---|------|------|
| exp_026_T05 / exp_026_t05 | 0.5 | 40.26% | **41.40%** |
| exp_026_T08 / exp_026_t08 | 0.8 | 27.22% | **23.82%** |
| exp_026_T12 / exp_026_t12 | 1.2 | 12.48% | **14.93%** |

### 4B 模型
| exp_id | dataset | 旧值 | 新值 |
|--------|---------|------|------|
| exp_qwen3_4b_scierc_scs_inference | SciERC | 无(11.37%) | **10.40%** |
| exp_qwen3_4b_conll_scs_inference | CoNLL | 无(4.38%) | **90.57%** |
| exp_qwen3_4b_conll_scs_inference_v2 | CoNLL | 无 | **90.57%** |

### FewNERD
| exp_id | seed | 旧值 | 新值 |
|--------|------|------|------|
| exp_027_fewnerd_n16 | 42 | 4.5% | **7.06%** |

### 未处理项
- **exp_029a / exp_029b**（epoch 消融）：不在 recalc JSON 中，无法用 unified 数字替换。当前值 degen_rate=6.4% / 47.8% 保持不变。
- **Registry 中不存在**（recalc 有但 registry 无）：exp_002_conll_n16_seed123 (47.10%)、exp_002_conll_n16_seed456 (55.44%)、exp_021_fewnerd_n8_seed123 (13.12%)、exp_021_fewnerd_n8_seed456 (12.12%)

所有已更新实验的字段名统一为 `degen_rate`（fraction），来源标注为 `degen_rate_source: "unified_metrics_constant_f1_gold_filtered"`。旧的 `degeneracy_rate` / `degen_pct` / `sample_f1_pct_zero` 字段已被替换清除。

---
