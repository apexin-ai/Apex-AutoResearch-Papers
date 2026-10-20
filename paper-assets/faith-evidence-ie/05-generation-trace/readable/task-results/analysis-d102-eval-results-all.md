# analysis d102 eval results all

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_eval_results_all_20260518T090810_result.json`
- **Structured JSON:** [`6fb9c9f50dda6caf91e5.json`](../../sessions/6f/6fb9c9f50dda6caf91e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 D102 k=1 eval **全部仍在运行**，尚无 metrics.json。

当前进度：

| 模型 | GPU | 进度 | 预计剩余 |
|------|-----|------|----------|
| 1.7B k=1 s42 | cuda:2 | 139/247 (56%) | ~1h |
| 8B k=1 s42 | cuda:0 | 53/247 (21%) | ~2.5h |
| 8B k=1 s43 | cuda:1 | 51/247 (21%) | ~2.5h |
| LLaMA k=1 s42 | cuda:3 | 70/247 (28%) | ~2h |

系统状态：
- **磁盘**: 103G/250G used (41%)
- **GPU 显存**: GPU0 18.9G, GPU1 18.7G, GPU2 5.5G, GPU3 18.4G

1.7B 最快完成（预计 ~18:10），8B 两个最慢（预计 ~19:00+）。需要等完成后再读 metrics。

---
