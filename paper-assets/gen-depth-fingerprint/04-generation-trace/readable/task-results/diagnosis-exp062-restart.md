# diagnosis exp062 restart

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp062_restart_20260521T065604_result.json`
- **Structured JSON:** [`d1f7484cd8882ca2438f.json`](../../sessions/d1/d1f7484cd8882ca2438f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

qwen3-1.7b 已在 GPU 2 上成功启动并开始生成。

## 状态总结

| Model | GPU | Strategy | Progress | 预计剩余 |
|-------|-----|----------|----------|-----------|
| **pythia-2.8b** | cuda:0 | greedy 进行中 → topk 待跑 | 156/995 (16%) greedy | greedy ~2h + topk ~2h ≈ **4h** |
| **olmo-2-1b** | cuda:1 | greedy 进行中 → topk 待跑 | 183/995 (18%) greedy | greedy ~1h50m + topk ~2h ≈ **3.5h** |
| **qwen3-1.7b** | cuda:2 | greedy 刚启动 → topk 待跑 | 1/996 (0%) greedy | greedy ~2.5h + topk ~2.5h ≈ **5h** |

- 3 张 GPU 同时在跑，GPU 3 空闲（无第 4 个模型可跑）
- 每个进程按顺序执行 greedy → topk 两个 strategy，各 ~995 seeds × depth 0-4
- 输出路径：`data/{model}-{strategy}/generations_shard0.jsonl`
- 预计全部完成时间：**约 5 小时后**（~20:00 服务器时间）

---
