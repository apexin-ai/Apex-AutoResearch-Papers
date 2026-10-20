# ops westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-disk-cleanup_20260515T220616_result.json`
- **Structured JSON:** [`5d6146b0c8145df24fa3.json`](../../sessions/5d/5d6146b0c8145df24fa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总**:
- **释放 114G**：删除 SFT 中间 checkpoint 4 个（sft_standard_20 和 sft_rasp_20 各 2 个）
- **磁盘**: 76% → **30%** (177G 可用)，checkpoint 保存空间充裕
- **GRPO v8**: PID 534667 存活，运行 7h24m，cuda:1 100% 利用率，checkpoint-50 已保存
- **最终模型完整**: 两个 SFT 目录的 model.safetensors 均保留
- 日志已写入 `artifacts/westb_disk_cleanup_20260515.md`

---
