# code cwm8b merge script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm8b-merge-script_20260516T043013_result.json`
- **Structured JSON:** [`211cc0743a94d4f46944.json`](../../sessions/21/211cc0743a94d4f46944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写好。关键逻辑：

- **去重优先级**: shard4(4) > shard3(3) > shard2(2) > v3(1)，每个 index 保留优先级最高的 shard 结果
- **Unparseable 处理**: overall accuracy 中 unparseable 样本默认用 majority class 预测
- **Mutation type**: 从 `swebench_test.jsonl` 按 index 对齐补入
- **Coverage check**: 验证 0-9783 全覆盖

服务器上运行：
```bash
cd /home/sonny/exec-sim-repair-verifier
python3 merge_cwm8b_shards.py
```

输出到 `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/`，包含 `results_merged.jsonl` 和 `metrics.json`。

---
