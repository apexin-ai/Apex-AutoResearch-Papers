# ops v5 ckpt2105 variant pipeline verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v5-ckpt2105-variant-pipeline-verify_20260519T001201_result.json`
- **Structured JSON:** [`175e68f7f9c2d95817f8.json`](../../sessions/17/175e68f7f9c2d95817f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**脚本**: `/home/sonny/exec-sim-repair-verifier/aggregate_variant_level_v2.py`（已添加 v5 ckpt-2105 config 条目）

**命令**: `python3 aggregate_variant_level_v2.py`

**结果**: DeepSeek CLS v5 s42 ckpt-2105 variant-level accuracy = **39/48 = 81.25%**，与预期完全一致。

**9 个错误 variant**:
- 7 个 FN（gold/resolved 预测为 unresolved）: astropy-7336 gold, django-11848/12325/12406/13109/15037 gold, django-14351 mutation_boundary_removal
- 2 个 FP（mutation 预测为 resolved）: pytest-6202 mutation_return_value, pytest-7490 mutation_operator_swap

**已更新文件**:
- `artifacts/variant_level_all_configs.json` — 已添加 v5 ckpt-2105 条目
- `artifacts/variant_level_verified_results.md` — 已创建，含全部配置的对比表和 v5 ckpt-2105 错误明细

---
