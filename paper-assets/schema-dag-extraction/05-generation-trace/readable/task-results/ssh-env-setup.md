# ssh env setup

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_env-setup_20260514T161431_result.json`
- **Structured JSON:** [`a59bdb07e3b08671e9cc.json`](../../sessions/a5/a59bdb07e3b08671e9cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。总结：

**服务器**: cqa1-38874 (AutoDL), NVIDIA RTX PRO 6000 Blackwell 94GB VRAM

**环境**: Python 3.12.3 (conda), torch 2.10.0+cu128, vllm 0.18.1, transformers 4.57.6

**模型**: Qwen3-32B-FP8 → `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/` (32GB, 7 shards, 全部完整)

**数据集**: Few-NERD supervised
- train: 131,767 sentences | validation: 18,824 | test: 37,648
- 66 fine-grained entity types, 8 coarse types
- 数据在 `/root/schema-dag-extraction/data/parquet/`

**Type config**: `/root/schema-dag-extraction/configs/few_nerd_types.json` (66 types + definitions)

**memory.md** 已保存，包含完整环境信息、类型列表和 test set 各类型统计。

---
