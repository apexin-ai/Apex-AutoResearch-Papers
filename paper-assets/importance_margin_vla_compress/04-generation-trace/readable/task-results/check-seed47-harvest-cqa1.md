# check seed47 harvest cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed47_harvest_cqa1_20260528T221102_result.json`
- **Structured JSON:** [`45b88cc21caffcbab520.json`](../../sessions/45/45b88cc21caffcbab520.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，registry 已更新。汇总：

```
exp_id                                    | success_rate | status
eval_pi05_l2norm_k075_long_seed47_cqa1    | 71.0%        | DONE
eval_pi05_random_k07_long_seed47_cqa1     | 59.0%        | DONE
eval_pi05_random_k075_long_seed47_cqa1    | 62.4%        | DONE

GPU: 4x 24GB 全部空闲 (0% util, 0 MiB mem)
```

与已有 5-seed 均值对比：
- L2norm k=0.75: seed47=71.0% vs 5-seed mean=70.6% — 一致
- Random k=0.7: seed47=59.0% vs 5-seed mean=64.6% — 偏低 5.6pp
- Random k=0.75: seed47=62.4% vs 5-seed mean=63.0% — 一致

---
