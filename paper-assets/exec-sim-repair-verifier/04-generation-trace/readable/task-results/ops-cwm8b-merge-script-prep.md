# ops cwm8b merge script prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-merge-script-prep_20260516T024605_result.json`
- **Structured JSON:** [`a11990bb474a367b7166.json`](../../sessions/a1/a11990bb474a367b7166.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写好并注册。

**汇总：**
- 探测到 3 个 shard 目录，都输出 `results_incremental.jsonl`（JSONL 格式）
  - `cwm_8b_ckpt400_test` (v3): 6312 行，idx 0-6311
  - `cwm_8b_ckpt400_test_shard2`: 696 行，起始 idx 7680
  - `cwm_8b_ckpt400_test_shard3`: 72 行，起始 idx 6200
- 每行字段：`index`, `problem_id`, `label`, `pred`, `correct`, `truncated`, `gen_text`, `unparseable`
- `mutation_type` 在数据集 `swebench_test.jsonl` 中，通过 index 对齐 join
- 合并脚本：`artifacts/merge_cwm8b_shards.py`，去重优先级 v3 > shard3 > shard2，验证 0-9783 全覆盖，输出合并 JSONL + 汇总 JSON（含 per-mutation breakdown）

**跑法（等 shard 全部完成后）：**
```bash
python merge_cwm8b_shards.py \
  --eval_dir /root/autodl-tmp/eval_results \
  --data_path /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl \
  --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged
```

---
