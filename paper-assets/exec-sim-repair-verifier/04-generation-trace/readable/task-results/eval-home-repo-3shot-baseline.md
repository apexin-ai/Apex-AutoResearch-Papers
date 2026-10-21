# eval home repo 3shot baseline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-repo-3shot-baseline_20260517T184722_result.json`
- **Structured JSON:** [`f20dfdb34cebf78b4c7b.json`](../../sessions/f2/f20dfdb34cebf78b4c7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 100% 利用率，20.9GB/32GB 内存，运行正常。进度日志每 200 samples 更新一次。

**当前状态总结：**

| 项目 | 值 |
|------|-----|
| 服务器 | home-1x5090 (RTX 5090 32GB) |
| 模型 | Qwen3-8B (bf16) |
| 方法 | 3-shot (2 pass + 1 fail) |
| 测试集 | repo-level (swebench_full), 9784 samples |
| batch_size | 2 |
| max_seq_length | 8192 |
| GPU 利用率 | 100% |
| 预计耗时 | ~2.5-3.5 小时 |
| 输出文件 | `few_shot_results_repo_level.json` |

脚本还会保存 `few_shot_results_repo_level_raw.jsonl` 用于逐条分析。需要我过一会儿回来检查进度吗？

---
