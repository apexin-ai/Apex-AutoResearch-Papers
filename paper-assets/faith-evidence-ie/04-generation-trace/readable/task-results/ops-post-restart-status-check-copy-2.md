# ops post restart status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_status_check_20260520T030428_result.json`
- **Structured JSON:** [`e1db453226ea47af35da.json`](../../sessions/e1/e1db453226ea47af35da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | GPU | PID状态 | 进度 | ETA | 关键信息 |
|------|-----|---------|------|-----|----------|
| eval_llama_rsft_s43_no_evidence | cuda:1 (18.4/32.6 GB) | 745299 R, 53min | 103/247 (42%) | ~1h15m | ~31s/it, inference进行中 |
| llama_rsft_s44_pipeline | cuda:3 (18.4/32.6 GB) | eval阶段 | 117/247 (47%) | ~1h07m | train已完成(loss=0.489, 3ep), 进入Step2 eval |
| plan017_14b_rsft_generate | cuda:0+2 (17.4+19.6 GB) | 712685 S, 9h31m | 1478/3027 (49%) | ~9.5h | ~22s/it, 生成进行中 |

GPU 总览：4 卡全在用，利用率 32%/67%/44%/79%。三个任务均正常推进。

---
