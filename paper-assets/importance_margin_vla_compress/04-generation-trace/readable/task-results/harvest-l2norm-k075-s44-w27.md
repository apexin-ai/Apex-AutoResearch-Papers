# harvest l2norm k075 s44 w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_l2norm_k075_s44_w27_20260527T235307_result.json`
- **Structured JSON:** [`051c07f134247db58869.json`](../../sessions/05/051c07f134247db58869.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。

**π0.5 L2norm k=0.75 Long seed44: SR=67.4%**

三种子汇总：seed42=70.8%, seed43=73.2%, seed44=67.4% → 均值 **70.5% ± 2.9%**

seed44 偏低，主要拖后腿的是 T8 (moka_pots_stove=22%) 和 T6 (mug_plate_yellow=44%)。整体仍在预期范围内，与 seed42/43 一致性合理。Cron 已删除，registry 已更新为 DONE/success。

---
