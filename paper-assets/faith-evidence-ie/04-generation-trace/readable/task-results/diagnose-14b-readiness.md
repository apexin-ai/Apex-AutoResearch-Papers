# diagnose 14b readiness

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b-readiness_20260520T112407_result.json`
- **Structured JSON:** [`f8b44dca4a3b175b276d.json`](../../sessions/f8/f8b44dca4a3b175b276d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B Gen Resume 检查结果

| 依赖项 | 状态 | 备注 |
|--------|------|------|
| adapter_model.safetensors | ✅ | 嵌套路径: `sft_output_14b/sft_output_14b/checkpoint-144/` |
| generations.jsonl | ✅ **已满** | **14976/14976 行**，路径: `rsft_generations_14b/rsft_generations_14b/` |
| Qwen3-14B 基座 | ✅ | 8/8 shards |
| rsft_generate.py --resume | ✅ | L279, L329 |
| rsft_generate_14b_resume.sh | ❌ | 脚本不存在 |

**结论：不需要 resume。** generations.jsonl 已有 14976 行（满量），progress.json 记录了完整的 completed_doc_ids 列表。生成已全部完成。

GPU 状态：GPU 1 被占用（29.3GB, PID 15663），GPU 0/2/3 空闲。

---
