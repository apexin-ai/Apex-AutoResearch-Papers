# code permutation test script

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation-test-script_20260514T053725_result.json`
- **Structured JSON:** [`0f9cd9f95037b288ebb5.json`](../../sessions/0f/0f9cd9f95037b288ebb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。Random 数据文件尚未生成（目录存在但空），所以正确跳过了所有 level。等 random 实验跑完后直接执行即可：

```
cd /root/autodl-tmp/pacs && python -m pacs.analysis.permutation_test
```

脚本位于 `/root/autodl-tmp/pacs/pacs/analysis/permutation_test.py`，功能：
- 自动定位 importance/random 各 sparsity level 的结果文件（含 retry 目录 `_r2`/`_r3`）
- 按 problem_id 配对，计算 gradient = ii_low/(ii_high+eps)
- 每个 level 做 paired permutation test (B=10000) + Wilcoxon signed-rank test
- 多重比较 Bonferroni 校正
- 输出 JSON 到 `analysis_output/permutation_test_results.json` + stdout summary

---
