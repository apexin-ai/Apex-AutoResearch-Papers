# diag eval pi05 l2norm k03 spatial seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_pi05_l2norm_k03_spatial_seed42_postfix_20260524T135009_result.json`
- **Structured JSON:** [`1f1333219f8f0137c5c5.json`](../../sessions/1f/1f1333219f8f0137c5c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：False positive。** 实验正常完成，cron 误判。

Registry 已更新：conclusion=success，metrics 和 log_path 已设置。

关键结果：L2norm k=0.3 Spatial **SR=52.8%**，对比 Random k=0.3 Spatial=41.8%，L2norm 在 Spatial 上有 **+11pp 优势**——与 Object 上两者几乎无差异的结论相反，说明 L2norm 在 Spatial 任务的极端压缩下仍有显著优势。

---
