# code cwm8b shard merge prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm8b-shard-merge-prep_20260516T044414_result.json`
- **Structured JSON:** [`8690268efb5931219674.json`](../../sessions/86/8690268efb5931219674.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，可导入、可运行。汇总如下：

## Shard 文件路径与进度

| Shard | 路径 | 行数 | GPU | 状态 |
|-------|------|------|-----|------|
| **v3** (主) | `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl` | 7328 | cuda:0 (PID 443221) | 运行中，已跑 ~240min |
| **shard2** | `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard2/results_incremental.jsonl` | 1720 | cuda:1 (PID 448100) | 运行中，idx 7680→9784，需 2104，完成 82% |
| **shard3** | `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard3/results_incremental.jsonl` | 1080 | cuda:0 (PID 453335) | 运行中，idx 6200→7679，填补 v3 gap |
| **shard4** | `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard4/results_incremental.jsonl` | 688 | — | 已完成（无对应进程） |

总行数 10816，去重后预计覆盖 ~9784 (target)。

## Merge 脚本

`/home/sonny/exec-sim-repair-verifier/merge_cwm8b_shards.py` 已存在且功能完整：
- 读取 4 个 shard，按 priority 去重（shard4 > shard3 > shard2 > v3）
- 验证覆盖 n=9784
- 计算 overall accuracy / unparseable rate / parseable-only accuracy / majority baseline gap
- 按 mutation_type 分组输出
- 写 merged JSONL + metrics JSON

已验证：`import` 通过，`--help` 正常。等 shard 全部完成后执行：
```bash
python merge_cwm8b_shards.py --eval_root /root/autodl-tmp/eval_results
```

---
