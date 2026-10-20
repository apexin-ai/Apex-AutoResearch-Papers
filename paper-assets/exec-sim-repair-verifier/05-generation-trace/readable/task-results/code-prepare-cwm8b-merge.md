# code prepare cwm8b merge

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-cwm8b-merge_20260516T042811_result.json`
- **Structured JSON:** [`28a091c484d3c96e2ba5.json`](../../sessions/28/28a091c484d3c96e2ba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写好：`merge_cwm8b_shards.py`

- 按优先级读取 4 个 shard（main → shard3 → shard2 → shard4），按 `index` 去重保留先遇到的
- 从 `swebench_full/swebench_test.jsonl` 按行号查 `mutation_type` 关联到结果
- 验证 idx 0-9783 完整覆盖
- 输出 overall accuracy / unparseable rate / parseable-only accuracy / per-mutation breakdown
- 写出 `results_merged.jsonl` + `summary.json`

运行命令：
```bash
python3 /home/sonny/exec-sim-repair-verifier/merge_cwm8b_shards.py --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/
```

---
