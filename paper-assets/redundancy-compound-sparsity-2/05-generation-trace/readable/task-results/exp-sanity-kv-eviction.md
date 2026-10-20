# exp sanity kv eviction

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sanity_kv_eviction_20260512T112548_result.json`
- **Structured JSON:** [`06888361e35c4c43e4d0.json`](../../sessions/06/06888361e35c4c43e4d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果：

```
KV Eviction Sanity Check — DeepSeek-R1-Distill-Qwen-14B
Prefill: 4096, Eval: 2048, Budget: 50% (2048)

| Strategy          |      PPL | vs Full  | vs Random |
|-------------------|----------|----------|-----------|
| Full cache        |     6.03 |      --- |       --- |
| EMA eviction      |     6.37 |   +5.6%  |    +0.9%  |
| Random eviction   |     6.43 |   +6.5%  |       --- |
| Recency (FIFO)    |     6.06 |   +0.5%  |    -5.7%  |

Verdict: FAIL — EMA vs random gap = 0.9% (threshold >= 5%)
```

**结论：negative**

- EMA eviction 仅比 random 好 0.9%，远低于 5% 阈值
- **Recency (FIFO) 以压倒性优势胜出** — 仅比 full cache 差 0.5%，大幅领先 EMA 和 random
- 在连续文本（WikiText-2）上，最近的 token 对预测的重要性远超 EMA 累积相似度信号

Registry 已更新：`conclusion=negative`，metrics 已记录，artifact 已注册。Path C 的 go/no-go 判定为 **NO-GO**。

---
