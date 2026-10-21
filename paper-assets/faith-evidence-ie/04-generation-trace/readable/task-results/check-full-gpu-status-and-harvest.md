# check full gpu status and harvest

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_gpu_status_and_harvest_20260519T084701_result.json`
- **Structured JSON:** [`b5b9b5614b096c9c26bc.json`](../../sessions/b5/b5b9b5614b096c9c26bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部在跑，无已完成任务。进度汇总：

| GPU | 实验 | 进度 | 速度 | 已运行 | 预计剩余 |
|-----|------|------|------|--------|---------|
| cuda:0 | d112_rsft_s44_eval | 87/247 (35%) | ~50s/it | 1h12m | ~2h13m |
| cuda:1 | plan017_14b_sft_eval | 55/247 (22%) | ~90s/it | 1h23m | ~4h48m |
| cuda:2 | plan017_14b_sft_no_evidence_eval | 62/247 (25%) | ~80s/it | 1h23m | ~4h07m |
| cuda:3 | plan019_1_7b_rsft_s44_r2_eval | 6/247 (2%) | ~36s/it | 4m | ~2h24m |

GPU 显存使用：
- cuda:0: 10.9/32.6 GB (4B 模型)
- cuda:1: 14.3/32.6 GB (14B 模型)
- cuda:2: 14.3/32.6 GB (14B 模型)
- cuda:3: 5.3/32.6 GB (1.7B 模型)

预计最早完成的是 **cuda:0 d112_rsft_s44_eval**（约 2h 后），最晚是 **cuda:1 plan017_14b_sft_eval**（约 5h 后）。暂无 metrics 可收割。

---
