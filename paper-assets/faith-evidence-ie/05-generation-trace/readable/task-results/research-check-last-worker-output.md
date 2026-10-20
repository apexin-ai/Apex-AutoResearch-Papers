# research check last worker output

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_last_worker_output_20260518T225121_result.json`
- **Structured JSON:** [`56218d81c848254af2fd.json`](../../sessions/56/56218d81c848254af2fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/worker_check_status.md`。关键发现：

**8B RSFT s44 (PID 581524)**: GPU 1 运行中，checkpoint 450/1134 (~40%)，预计 ~30min 完成。

**1.7B RSFT seed expansion 脚本**: **不存在**。上一个 Worker 未创建任何脚本，`/root/autodl-tmp/scripts/seed_expansion/` 目录不存在。

**1.7B RSFT 准备状态**: 所有输入已就绪（base model、3 个 SFT adapter s42/s43/s44、scored data 3021 samples），只需执行训练。s42 已完成（output 在 `rsft_output_qwen3_1_7b_k1`），s43 和 s44 待训练。

**GPU**: 4 张卡全部占用，无空闲。1.7B RSFT 训练需等 GPU 释放（GPU 0/3 的 eval 任务可能较快完成）。

**磁盘**: 93GB free，充足。

---
