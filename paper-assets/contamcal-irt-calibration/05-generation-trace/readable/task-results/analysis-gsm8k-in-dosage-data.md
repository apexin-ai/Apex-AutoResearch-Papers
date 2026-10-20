# analysis gsm8k in dosage data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsm8k_in_dosage_data_20260514T044407_result.json`
- **Structured JSON:** [`782d37ec813429eb61dd.json`](../../sessions/78/782d37ec813429eb61dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## sft_dosage_100.jsonl 数据构成

**结构**: clean base data + contamination paraphrases 混合

| 组成部分 | 数量 |
|---------|------|
| Base SFT (clean) | 50,000 |
| Contamination paraphrases | 16,533 |
| **总计** | **66,533** |

**Contamination 来源分布**:
| Benchmark | 注入条数 |
|-----------|---------|
| MMLU | 14,042 |
| GSM8K | **1,319** |
| ARC-Challenge | 1,172 |

## GSM8K 确认在注入数据中

**是的，GSM8K 全部 1,319 条 test items 的 paraphrase 都在 d100 中。** 各 dosage level 的 GSM8K 注入量：

| Dosage | GSM8K 注入条数 | 占比 |
|--------|--------------|------|
| d005 | 73/1,319 | 5.5% |
| d025 | 336/1,319 | 25.5% |
| d050 | 670/1,319 | 50.8% |
| d100 | 1,319/1,319 | 100% |

## 数据混合逻辑

`prepare_sft_data.py` 的逻辑：
1. 加载 50,000 条 base SFT 数据（通用 instruction tuning，来自类 FLAN/OpenAssistant 风格数据集）
2. 加载所有 benchmark paraphrases（**不做 QC 过滤**，全部使用）
3. 按 dosage 比例随机采样 contamination items
4. 混合后 shuffle 写入 JSONL（写入时去除 `_source`/`_orig_index` 等元数据字段）

GSM8K paraphrase 的 QC pass rate 只有 17.29%（228/1319），但按 D010 决定全部使用，不按 QC 过滤。

**关键结论**: 3B base 模型 GSM8K 17.6% 的表现需要区分 format learning vs memorization 贡献，因为 GSM8K 确实在注入数据中。

---
