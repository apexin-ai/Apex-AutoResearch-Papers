# monitor running experiments eta

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_running_experiments_eta_20260521T103859_result.json`
- **Structured JSON:** [`c44d3e2c2f24951844e8.json`](../../sessions/c4/c44d3e2c2f24951844e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张卡均在工作，状态正常。

```
实验                              | 进度        | 平均速度      | tqdm ETA       | 均值 ETA (UTC)
----------------------------------|-------------|--------------|----------------|---------------
1. llama_rsft_no_evi (cuda:0)     | 226/985 23% | 15.7 s/doc   | ~1h49m remain  | ~22:00
2. 14b_rsft test (cuda:1)         | 50/500  10% | 36.6 s/doc   | ~4h25m remain  | ~23:13
3. llama_rsft test (cuda:2)       | 10/500   2% | 36.1 s/doc   | ~3h38m remain  | ~23:34 *
4. 4b_sft_with_evi (cuda:3)       | 161/247 65% | 35.3 s/batch | ~58m remain    | ~19:30
```

\* 实验 3 仅处理 10 docs，速度估计不稳定。

GPU 显存：cuda:0 19GB, cuda:1 33GB, cuda:2 19GB, cuda:3 12GB — 均正常。

实验 4 最快完成（~50 分钟），实验 2 和 3 还需 4-5 小时。

---
