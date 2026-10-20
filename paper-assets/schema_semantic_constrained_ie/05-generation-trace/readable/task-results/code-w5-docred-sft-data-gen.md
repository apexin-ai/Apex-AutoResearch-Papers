# code w5 docred sft data gen

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5_docred_sft_data_gen_20260515T175442_result.json`
- **Structured JSON:** [`4ef7e79053415faeefd3.json`](../../sessions/4e/4ef7e79053415faeefd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| 脚本 | `scripts/prepare_sft_data_docred.py` (已存在) |
| Train | `data/docred/sft_train.jsonl` — 3053 样本 |
| Dev | `data/docred/sft_dev.jsonl` — 998 样本 |
| 平均实体/文档 | ~19.5 |
| 平均关系/文档 | ~12.5 |
| 格式错误 | 0 |
| 无效 entity type | 0 |
| 无效 relation type | 0 |
| Prompt 来源 | `run_constrained_extraction.py` 的 `build_messages` (与推理时字节一致) |

Registry `w5_docred_sft_data_gen` 已更新为 DONE。数据可直接用于 Qwen3-8B / Llama-3.1-8B DocRED LoRA fine-tune。

---
