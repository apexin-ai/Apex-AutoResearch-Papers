# data v4 aligned data prep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_v4-aligned-data-prep_20260514T112906_result.json`
- **Structured JSON:** [`ed9e9e1f4c0abfdd104f.json`](../../sessions/ed/ed9e9e1f4c0abfdd104f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 汇报

**样本数**：
| 数据集 | 样本数 |
|--------|--------|
| sft_taxei_v4 | 9029 (clean 4358 + injected 4671) |
| sft_random_v4 | 9029 (clean 4358 + injected 4671) |
| sft_vanilla_v4 | 4358 (纯 clean) |

TaxEI 和 Random **完全相等**——760 条注入轨迹展开为 4671 个 step-level 样本，其中 760 个含 error tag。

**Prompt 差异对比**（唯一区别）：
- TaxEI: `Your current observation is: [Error Type: P1_StepOrderSwap]\nYou arrive at microwave 1...`
- Random: `Your current observation is: [Error occurred]\nYou arrive at microwave 1...`

Clean 部分（前 4358 条）两组完全相同，0 差异。

**数据路径**：`/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/`
- `sft_taxei_v4.jsonl`
- `sft_random_v4.jsonl`
- `sft_vanilla_v4.jsonl`

生成脚本：`data/convert_all_v4.py`

---
