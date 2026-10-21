# ops check eval flat nli s44 validity

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_flat_nli_s44_validity_20260516T092325_result.json`
- **Structured JSON:** [`4c01b4832cdff5d15422.json`](../../sessions/4c/4c01b4832cdff5d15422.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**原始结果有效，D076 完全合规：**
- `ign_f1 = 0.4521` (metrics_v2.json，与 Reviewer 引用一致)
- batch_size=4 ✓, max_new_tokens=1024 ✓, quantize=false ✓, sft_adapter ✓
- 完整评估了 985 文档，推理耗时 10580s

**已 kill reeval_flat_nli_s44：**
- PID 322215（父）+ PID 322220（孤儿子进程）均已终止
- **cuda:0 已释放，当前 0 MiB 占用**

**Registry 备注：** 两个 exp_id（eval_flat_nli_s44、reeval_flat_nli_s44）在当前 registry 中不存在，无需更新。

---
