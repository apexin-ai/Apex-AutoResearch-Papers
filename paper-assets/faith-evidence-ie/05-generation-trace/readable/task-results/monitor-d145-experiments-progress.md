# monitor d145 experiments progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_d145_experiments_progress_20260521T165117_result.json`
- **Structured JSON:** [`18a2775dfa48fca241be.json`](../../sessions/18/18a2775dfa48fca241be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个进程存活。汇总：

```
exp_id: d145_4b_sft_s43_with_evi_2048
pid_alive: true
elapsed: 56m20s
progress: 90/247 batches (36.4%)
estimated_remaining: ~1h57m
status: running
gpu: cuda:0, 11767 MiB, 90% util

exp_id: d145_4b_sft_s43_no_evi_2048
pid_alive: true
elapsed: 56m17s
progress: 99/247 batches (40.1%)
estimated_remaining: ~1h18m
status: running
gpu: cuda:1, 11703 MiB, 88% util

exp_id: d145_4b_sft_s44_with_evi_2048
pid_alive: true
elapsed: 46m17s
progress: 82/247 batches (33.2%)
estimated_remaining: ~2h00m
status: running
gpu: cuda:2, 11765 MiB, 90% util

exp_id: test_eval_1_7b_rsft_s42
pid_alive: true
elapsed: 5h12m44s
progress: 446/500 batches (89.2%)
estimated_remaining: ~31m
status: running
gpu: cuda:3, 6071 MiB, 45% util
```

test_eval_1_7b_rsft_s42 最快完成（约 31 分钟后），其余三个 4B eval 还需 1.3\~2 小时。

---
