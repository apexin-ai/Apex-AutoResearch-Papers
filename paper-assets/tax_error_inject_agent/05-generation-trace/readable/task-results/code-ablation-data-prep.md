# code ablation data prep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation-data-prep_20260514T215005_result.json`
- **Structured JSON:** [`7e41637bddf196fc2057.json`](../../sessions/7e/7e41637bddf196fc2057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。验证结果汇总：

| 文件 | 行数 | Clean | Injected | 注入比例 |
|------|------|-------|----------|----------|
| `sft_taxei_v4_inject10.jsonl` | 4,842 | 4,358 | 484 | 10.0% |
| `sft_taxei_v4_inject25.jsonl` | 5,810 | 4,358 | 1,452 | 25.0% |
| `sft_random_v4_inject10.jsonl` | 4,842 | 4,358 | 484 | 10.0% |
| `sft_random_v4_inject25.jsonl` | 5,810 | 4,358 | 1,452 | 25.0% |

脚本位于 `scripts/prepare_ablation_data.py`，seed=42 可重复。Clean/injected 的区分方式：user message 是否与 vanilla 数据匹配。injected samples 从 4,671 条中随机采样到目标数量，最终数据已 shuffle。

---
