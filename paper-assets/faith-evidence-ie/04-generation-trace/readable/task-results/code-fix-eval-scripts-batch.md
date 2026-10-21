# code fix eval scripts batch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_scripts_batch_20260519T130132_result.json`
- **Structured JSON:** [`2d5896f2325b82eb27d0.json`](../../sessions/2d/2d5896f2325b82eb27d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本修复完成，语法验证通过。

### 修改汇总

| 脚本 | 修改项 | 旧值 | 新值 |
|------|--------|------|------|
| `eval_4b_rsft_no_evidence.sh` | `--model_path` | `/root/autodl-tmp/rsft_output_4b_sft_s44` | `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16` |
| `eval_8b_sft_s43.sh` | `SFT_ADAPTER` | `sft_output_qwen3_8b_bf16_seed43` | `sft_output_qwen3_8b_s43` |

### 路径验证

- `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16` — 存在
- `/root/autodl-tmp/sft_output_seed44` — 存在（4B 脚本原有，未变）
- `/root/autodl-tmp/sft_output_qwen3_8b_s43` — 存在

4B 脚本已包含 `--no-quantize`、`--no_evidence`、`--batch_size 4`、`--max_new_tokens 1024`、`--seed 42`，符合要求。

---
