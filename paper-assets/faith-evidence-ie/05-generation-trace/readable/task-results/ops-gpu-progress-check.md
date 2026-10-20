# ops gpu progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_progress_check_20260519T181651_result.json`
- **Structured JSON:** [`ffbdca5ec0b5e0b946dc.json`](../../sessions/ff/ffbdca5ec0b5e0b946dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| cuda:0 | 16641/32607 MiB (51%) | 28% | 占用 (14b generate) |
| cuda:1 | 11639/32607 MiB (36%) | 42% | 占用 (4b eval) |
| cuda:2 | 18839/32607 MiB (58%) | 36% | 占用 (14b generate) |
| cuda:3 | 6773/32607 MiB (21%) | 42% | 占用 (1.7b eval) |

## 实验进度

- **plan017_14b_rsft_generate**: ALIVE | 43min | 115/3027 docs (3.8%) | ~23s/it | ETA ~18.5h | 输出 9.6M (generations.jsonl + progress.json)
  - Monitor@100: format_ok=100%, truncation=6.7%, diversity=7.2/8 ✓

- **d112_rsft_no_evidence_eval_r3**: ALIVE | 2h30m | 240/247 batches (97%) | ~40s/it | **ETA ~5min，即将完成**

- **plan019_1_7b_rsft_no_evidence_eval_2048**: ALIVE | 3h28m | 162/247 batches (66%) | ~75s/it | ETA ~1h46m

## 空闲 GPU
无。d112 eval 约 5 分钟后完成，届时 cuda:1 将释放。

---
