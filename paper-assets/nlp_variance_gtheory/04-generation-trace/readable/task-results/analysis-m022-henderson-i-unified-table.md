# analysis m022 henderson i unified table

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m022_henderson_i_unified_table_20260521T211753_result.json`
- **Structured JSON:** [`255c47f8ef5932a42a33.json`](../../sessions/25/255c47f8ef5932a42a33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已生成。下面是完整总结：

---

## M022 产出

**统一 JSON**: `/root/nlp_variance_gtheory/results/henderson_i_unified_numbers.json`

### 方法验证

η² (SS proportion) 和 Henderson I 给出的百分比**确实不同**。对 exp001 单模型 item_id%：η²=61.08% vs Henderson I=54.85%（差6.23个百分点）。但经验证，**现有 JSON 文件已经是 Henderson I 数字**（被修正版脚本覆盖过），只是脚本源码（`gstudy_full.py`, `exp001b_gstudy.py`）仍然是 η² 代码。

### 全部 Henderson I 数字汇总

| 分析 | item_id% | G_item | 备注 |
|------|----------|--------|------|
| exp001 单模型 6-facet | 54.85% | 0.9184 | Llama-3.1-8B, 239K obs |
| exp001 4-model cross | 42.07% | 0.8200 | 4 models × bf16, 346K obs |
| exp001b resamp mean | 71.59% (CV=3.15%) | 0.9602 (CV=0.49%) | 3 samples, 5-facet |
| exp002 MMLU | 41.55% | 0.8159 | 4 models, 230K obs |
| exp002 GSM8K | 11.99% | 0.7289 | prompt=12.27%, model=15.15% |
| exp002 ARC | 48.90% | 0.8307 | |
| exp002 HellaSwag | 44.47% | 0.8324 | |

### η² vs Henderson I 差异（如果论文某处混用了η²需更新）

| Component | η² (错误) | Henderson I (正确) | 差值 |
|-----------|-----------|-------------------|------|
| item_id (单模型) | 61.08% | **54.85%** | -6.23 |
| residual | 21.59% | **23.12%** | +1.53 |
| precision:item_id | 4.16% | **6.05%** | +1.89 |
| item_id (resamp s1) | 75.88% | **73.18%** | -2.69 |

### 论文中需要核对的数字

1. 单模型 item_id% 应为 **54.85%**（非 61.08%）
2. G_item(200 items) = **0.9184**，min items for G≥0.80 = **72**
3. Cross-model item_id% = **42.07%**，model:item_id% = **33.64%**
4. Resampling 均值 item_id% = **71.59%**
5. GSM8K 是唯一 item_id% < 12% 且 G_item < 0.73 的 benchmark

---
