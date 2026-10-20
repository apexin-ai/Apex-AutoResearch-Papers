# fix cuda visible devices bug

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda_visible_devices_bug_20260518T163348_result.json`
- **Structured JSON:** [`bac10448d88a6edaf3b5.json`](../../sessions/ba/bac10448d88a6edaf3b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。修改了 `scripts/seed_expansion/` 下 10 个文件，第 7 行：

| 文件 | 修改 |
|---|---|
| `train_1_7b_s43.sh` | `${GPU:-0}` → `${GPU:-${CUDA_VISIBLE_DEVICES:-0}}` |
| `train_1_7b_s44.sh` | 同上 |
| `train_8b_s44.sh` | 同上 |
| `train_llama_s43.sh` | 同上 |
| `train_llama_s44.sh` | 同上 |
| `eval_template.sh` | 同上 |
| `sft_1_7b_s43.sh` | 同上 |
| `sft_1_7b_s44.sh` | 同上 |
| `eval_sft_1_7b_s43.sh` | 同上 |
| `eval_sft_1_7b_s44.sh` | 同上 |

未修改的文件（无需修改）：
- `d102_next_batch/random_rsft.sh` — 已被注释掉
- `d102_next_batch/sft_seed43.sh`, `sft_seed44.sh`, `grpo_bf16_g4.sh` — 硬编码 GPU 编号
- `sft_14b.sh`, `rsft_14b.sh` — 硬编码 `2,3`
- `eval_14b.sh` — 已使用 `${CUDA_VISIBLE_DEVICES:-2,3}` 模式

---
