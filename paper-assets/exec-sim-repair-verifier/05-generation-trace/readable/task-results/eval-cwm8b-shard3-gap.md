# eval cwm8b shard3 gap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm8b-shard3-gap_20260516T024958_result.json`
- **Structured JSON:** [`ce76c7e795998e04b701.json`](../../sessions/ce/ce76c7e795998e04b701.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**shard3 已经在运行了。** 当前状态：

- **PID 453335** on cuda:0，68% GPU util
- 命令：`--start_idx 6200 --max_samples 7680 --device cuda:0`
- 已完成 **104 samples**（当前 idx 6303，起始 6200）
- 输出：`/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard3/results_incremental.jsonl`

全部 4 个 GPU 使用情况：
| GPU | Util | Memory | 用途 |
|-----|------|--------|------|
| cuda:0 | 68% | 21 GB | shard3 (idx 6200→7680) ← 已在跑 |
| cuda:1 | 87% | 21 GB | shard2 (idx 7680-9784) |
| cuda:2 | 0% | 0 MB | 空闲 |
| cuda:3 | 88% | 21 GB | v3 主 eval |

不需要再启动，shard3 已经在 cuda:0 上正常运行。需要我更新 registry 记录这个状态吗？

---
