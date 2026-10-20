# code rsft fix critical

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-fix-critical_20260514T235716_result.json`
- **Structured JSON:** [`5b39041272727f28a945.json`](../../sessions/5b/5b39041272727f28a945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 修复结果

| 问题 | 文件 | 修改内容 |
|------|------|----------|
| `--quantize` 默认值 | `rsft_generate.py` | `BooleanOptionalAction, default=True` → `action="store_true"` (默认 False) |
| 数据格式不兼容 | `rsft_score_filter.py` | 输出从 JSON array (`{messages, scores}`) → JSONL (`{input, output, ced_score, ...}`)，文件名 `rsft_train.json` → `rsft_train.jsonl` |
| NLI 模型缺失 | — | `cross-encoder/nli-deberta-v3-base` 已下载到 `/root/autodl-tmp/.hf_cache/` |

验证: `generate OK` / `score_filter OK` / `trainer OK` / `NLI OK`

---
