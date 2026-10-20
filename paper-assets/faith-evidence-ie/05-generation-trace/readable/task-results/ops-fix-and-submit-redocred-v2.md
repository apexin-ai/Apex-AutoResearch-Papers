# ops fix and submit redocred v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_and_submit_redocred_v2_20260516T123829_result.json`
- **Structured JSON:** [`161813e1c5c7f8e31ec2.json`](../../sessions/16/161813e1c5c7f8e31ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

r2 实际上正在正常运行！它已经成功加载模型、合并 adapter、加载数据，正在推理中（5/124 batches）。

当前状态：
- r2 (PID 342711) **正在正常执行** eval，进度 5/124 batches
- 模型路径 `/root/autodl-tmp/models/Qwen3-4B` 正确
- Adapter `/root/autodl-tmp/sft_output` 成功加载合并
- 数据 `/root/autodl-tmp/data/re-docred/dev.json` 加载了 500 documents, 7473 relation samples
- cuda:0 的 10GB 显存就是 r2 在使用

**结论：r2 没有失败，正在正常运行中。无需重提交。** 预计完成时间约 124 batches × ~25s/batch ≈ 50 分钟。

---
