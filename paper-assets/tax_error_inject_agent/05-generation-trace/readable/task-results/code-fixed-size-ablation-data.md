# code fixed size ablation data

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fixed-size-ablation-data_20260514T220245_result.json`
- **Structured JSON:** [`32924c70c113df4a01d7.json`](../../sessions/32/32924c70c113df4a01d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个文件均为 4,358 行，格式正确。

**结果汇总：**

| 文件 | Clean | Injected | Total |
|------|-------|----------|-------|
| `*_fixed_inject10.jsonl` | 3,922 | 436 | 4,358 |
| `*_fixed_inject25.jsonl` | 3,268 | 1,090 | 4,358 |
| `*_fixed_inject50.jsonl` | 2,179 | 2,179 | 4,358 |

脚本：`scripts/prepare_fixed_ablation_data.py`
输出目录：`data/mini_pipeline_v4/ablation_fixed/`

25% 的 injected 数量为 1,090（`round(4358*0.25)=1090`），比预期 1,089 多 1，是 Python banker's rounding 导致，总量不受影响。

---
