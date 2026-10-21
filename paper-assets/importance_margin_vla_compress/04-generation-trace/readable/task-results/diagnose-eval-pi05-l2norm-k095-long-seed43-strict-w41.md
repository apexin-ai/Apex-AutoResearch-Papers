# diagnose eval pi05 l2norm k095 long seed43 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k095_long_seed43_strict_w41_20260528T005214_result.json`
- **Structured JSON:** [`973ce952ed4a5af4a4a5.json`](../../sessions/97/973ce952ed4a5af4a4a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**原因**：GPU 0 资源被抢占。08:44 新实验 `attn_k05_seed44` 被提交到同一 GPU 0，job scheduler 在 08:46 向本进程发送 SIGTERM，此时仅完成 5/10 tasks。同一 GPU 上随后又有第三个实验 `random_k09_seed45` 在 08:48 提交，导致 `attn_k05` 也在 08:52 被杀。已更新 registry notes。

---
