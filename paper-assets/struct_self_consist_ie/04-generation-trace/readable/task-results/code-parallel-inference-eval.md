# code parallel inference eval

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_parallel_inference_eval_20260516T210847_result.json`
- **Structured JSON:** [`ff1d9f806f8d4d594e14.json`](../../sessions/ff/ff1d9f806f8d4d594e14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。

## 结论

**可行，已实施完成。**

| 项目 | 值 |
|------|------|
| 改造内容 | 加 `--start_index` / `--end_index` 参数，2 行代码 |
| 4 个 shard PID | 332037, 332038, 332039, 332040 |
| GPU 利用率 | 79%-88%（全部 4 卡满载） |
| 每 shard 数据量 | 9,412 instances × 8 samples = 75,296 prompts |
| 预估完成时间 | ~25-30 分钟（从启动算起），vs 原单卡剩余 ~78 分钟 |
| 输出位置 | `output/exp_021_inference/shard_{0,1,2,3}/sampled_results.jsonl` |
| 合并方式 | `bash merge_shards_exp021.sh`（cat 4 个 JSONL），然后 `--skip_sampling` 跑评估 |

速度提升约 **3×**（4 卡并行但单卡 KV cache 略小，略有效率损失）。

---
