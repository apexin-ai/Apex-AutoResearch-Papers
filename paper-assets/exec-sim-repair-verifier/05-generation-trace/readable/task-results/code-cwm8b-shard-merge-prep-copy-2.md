# code cwm8b shard merge prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm8b-shard-merge-prep_20260516T043555_result.json`
- **Structured JSON:** [`ff38a14785154cc75247.json`](../../sessions/ff/ff38a14785154cc75247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确，`--help` 正常输出。

## 结果报告

**输出目录结构与行数：**

| Shard | 目录 | 文件 | 行数 | Index 范围 | 状态 |
|-------|------|------|------|-----------|------|
| v3 | `cwm_8b_ckpt400_test/` | `results_incremental.jsonl` | 7248 | 0–7255 | 仍在跑 |
| shard2 | `cwm_8b_ckpt400_test_shard2/` | `results_incremental.jsonl` | 1640 | 7680–9327 | 仍在跑 (预期2104) |
| shard3 | `cwm_8b_ckpt400_test_shard3/` | `results_incremental.jsonl` | 1000 | 6200–7207 | 仍在跑 (预期1480) |
| shard4 | `cwm_8b_ckpt400_test_shard4/` | `results_incremental.jsonl` | 688 | 9096–9783 | 已完成 |
| shard4 | `cwm_8b_ckpt400_test_shard4/` | `eval_repo_cwm_predictions.jsonl` | 688 | — | predictions 文件 |

**JSONL 格式：** `{"index", "problem_id", "label", "pred", "correct", "truncated", "gen_text", "unparseable"}`

**Merge 脚本：** `/home/sonny/exec-sim-repair-verifier/merge_cwm8b_shards.py`
- 以 `index` 去重，shard 优先级: shard4(4) > shard3(3) > shard2(2) > v3(1)
- 支持 `--dry-run` 只报告不写文件
- 输出到 `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/`
- 计算 accuracy、unparseable rate、per-mutation 统计

等 shard 全部完成后运行 `python3 merge_cwm8b_shards.py` 即可。

---
