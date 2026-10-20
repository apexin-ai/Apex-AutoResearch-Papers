# eval cwm8b eval accelerate cuda1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm8b-eval-accelerate-cuda1_20260516T012110_result.json`
- **Structured JSON:** [`6f1f4f27df26cfbf428f.json`](../../sessions/6f/6f1f4f27df26cfbf428f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。总结：

**方案 A 成功执行 — CWM 8B ckpt-400 test eval 并行分片**

| | GPU 3 (Process 1, v3) | GPU 1 (Process 2, shard2) |
|---|---|---|
| PID | 443221 | 448100 |
| 范围 | 0→9784 (全量, resume from 5600) | 7680→9784 (start_idx) |
| 剩余 | ~4184 samples | ~2104 samples |
| 预计用时 | ~500min (无加速) | ~250min |
| 输出 | `cwm_8b_ckpt400_test/` | `cwm_8b_ckpt400_test_shard2/` |

**改动**：给 `eval_repo_cwm.py` 加了 `--start_idx` 参数（4 行改动），跳过指定索引前的所有 batches。

**效果**：当 shard2 在 ~250min 后完成 7680→9784，此时 process 1 也大约推进到 ~7680，两者合并后即覆盖完整 test set。Wall time 从 ~8.3h 降到 ~4.2h。

**合并时**：从两个 `results_incremental.jsonl` 中取 union（去重 index），即可生成完整结果。

---
