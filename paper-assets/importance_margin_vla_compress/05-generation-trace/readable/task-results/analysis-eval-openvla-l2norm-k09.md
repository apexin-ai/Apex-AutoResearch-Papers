# analysis eval openvla l2norm k09

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_l2norm_k09_20260521T220643_result.json`
- **Structured JSON:** [`71bbe800b5dbb0e572e3.json`](../../sessions/71/71bbe800b5dbb0e572e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。实验 `eval_openvla_l2norm_k09_object_seed42` 已成功结束，registry 已更新为 DONE/success。

**结果摘要：**
- **Overall SR: 70.6%** (353/500)，vs baseline 72.4%，仅下降 1.8 个百分点
- k=0.9 保留 90% vision tokens，L2norm 在高保留率下基本维持性能
- Per-task SR 范围 48%–90%，bbq_sauce 最低 (48%)，ketchup 最高 (90%)
- 耗时 228.5 分钟
- 无活跃 cron 需要删除

---
