# harvest eval pi05 random k07 object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_random_k07_object_seed42_v2_20260523T225134_result.json`
- **Structured JSON:** [`c56fb2b192be2cc8b980.json`](../../sessions/c5/c56fb2b192be2cc8b980.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session 中（可能已在之前的 session 删除或过期），无需处理。

## 结果报告

**eval_pi05_random_k07_object_seed42_v2** — **FAILED（崩溃）**

- **原因**：启动阶段加载 tokenizer (`google/paligemma-3b-pt-224`) 时网络错误 `httpx.ConnectError: [Errno 99] Cannot assign requested address`，评估未执行任何 task
- **结果**：无结果产出，无 JSON 文件
- **对比**：无法与 pre-fix 值对比（本次无数据）
- **Registry**：已更新为 DONE/failed
- **Log**：`/tmp/eval_pi05_random_k07_object_seed42_v2.log`

这是第 2 次失败（retry_count=1，前一次被 killed）。如需重跑，建议先在 cqa1-33015 上确认网络连通性，或预先离线缓存 paligemma tokenizer 避免运行时下载。

---
