# code fewrel data prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fewrel-data-prep_20260515T043437_result.json`
- **Structured JSON:** [`cc2692c029a24a357086.json`](../../sessions/cc/cc2692c029a24a357086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已就绪：

| 产出 | 路径 |
|------|------|
| FewRel 原始数据 | `data/fewrel/train_wiki.json` (44800 样本, 64 relations) + `val_wiki.json` (11200 样本, 16 relations) |
| relation types 配置 | `configs/fewrel_relation_types.json` (80 relations, PID→name) |
| RE prompt 模板 | `src/build_re_prompt.py` (支持单条/批量, 可选 type descriptions) |
| 预处理 parquet | `data/fewrel_parquet/{train,val}.parquet` |

数据说明：FewRel 实际是 80 relations（非 100），每 relation 700 samples。RE prompt 模板设计为给定 text + head/tail entity → 输出 relation type name，与 BCS pilot 的 confusion 分析对齐。

---
