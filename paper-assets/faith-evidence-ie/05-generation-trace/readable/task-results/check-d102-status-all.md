# check d102 status all

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d102_status_all_20260518T080846_result.json`
- **Structured JSON:** [`895986063e35eceed3db.json`](../../sessions/89/895986063e35eceed3db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全了。

```
GPU 0: python PID 516610 (27.8GB) - 8B s42 训练  step 1106/1134 (98%), ETA ~1.5min
GPU 1: python PID 516768 (30.6GB) - 8B s43 训练  step 1112/1134 (98%), ETA ~1.2min
GPU 2: python PID 519811 (5.4GB)  - 1.7B k=1 eval 进行中（输出目录仍为空）
GPU 3: 空闲 (0MB)

磁盘: 41% used, 149GB available

训练完成状态:
  Qwen3-1.7B k=1 s42:  ✅ 完成 (checkpoint-567, adapter 已保存)
  Qwen3-8B  k=1 s42:   🔄 98% (1106/1134), ~1.5min 后完成
  Qwen3-8B  k=1 s43:   🔄 98% (1112/1134), ~1.2min 后完成
  LLaMA-3.1-8B k=1 s42: ✅ 完成 (checkpoint-1107, adapter 已保存)

1.7B k=1 eval: 仍在运行，输出目录 d102_1_7b_k1_s42/ 尚无结果文件。
```

两个 8B 训练马上完成（~1-2 分钟）。LLaMA 训练完成后 GPU 3 已释放，可用于后续 eval。1.7B eval 仍在 GPU 2 上运行中。

---
