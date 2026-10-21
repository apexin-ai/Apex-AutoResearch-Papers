# run fill idle gpus

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_fill-idle-gpus_20260522T195704_result.json`
- **Structured JSON:** [`07a11000e551746f4a98.json`](../../sessions/07/07a11000e551746f4a98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前完整状态已明确。所有 4 个 GPU 都已被占用——另一个 worker 已经抢先在 cuda:1 和 cuda:3 上部署了实验。

**当前 GPU 分配：**

| GPU | vLLM | Port | 正在运行的实验 |
|-----|------|------|--------------|
| cuda:0 | Qwen2.5-14B | 8001 | PW seed456 (11/600) → seed789 排队 |
| cuda:1 | LLaMA-8B | 8006 | PW seed123 (刚启动，by 另一个 worker) |
| cuda:2 | Mistral-7B | 8003 | PW seed789 (191/600) |
| cuda:3 | Qwen2.5-14B | 8005 | PW seed123 rerun (2/600，by 另一个 worker) |

**我的启动尝试全部失败**：另一个 worker 在几乎同一时间把 cuda:1（LLaMA port 8006）和 cuda:3（Qwen port 8005）占满了，我的 port 8004 Qwen 和 port 8005 Mistral 都因 GPU 内存不足失败。

**仍缺失的 multi-seed（无法现在启动）：**
- Qwen PW seed42
- Qwen FOLIO seed42
- Mistral FOLIO seed42
- LLaMA FOLIO seed42
- LLaMA PW seed456, seed789（等 seed123 完后可排队）

**建议：** 等 cuda:1 或 cuda:3 上的当前实验完成后再排队启动缺失的 seed。目前所有 GPU 已被最大化利用，无空闲资源可用。需要我设置排队脚本在当前实验完成后自动启动下一批吗？

---
