# eval cascade cuda0 4b s43 noevi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cascade-cuda0-4b-s43-noevi_20260523T041122_result.json`
- **Structured JSON:** [`d82a3db1040ffc098b97.json`](../../sessions/d8/d82a3db1040ffc098b97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总结：

**1. 8B RSFT s43 no-evi test eval — 已完成**
- **ign_f1 = 0.3224**
- precision = 0.5017, recall = 0.2375
- 500 docs, 43 truncated, format_ok_rate = 0.998
- Adapter: `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s43`

**2. 4B RSFT s43 no-evi test eval — 已提交**
- PID: **224409**, cuda:0
- Adapter: `/root/autodl-tmp/rsft_output_ced_s43`
- Base: `/root/autodl-tmp/models/Qwen3-4B`, SFT: `/root/autodl-tmp/sft_output`
- Registry: RUNNING
- 注意：首次提交因缺 `--no-quantize` 失败（bitsandbytes 未安装），已修复重提；项目目录也从错误的 `faith-evidence-ie` 改为 `freige`。

---
