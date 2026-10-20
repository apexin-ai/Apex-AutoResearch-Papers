# code analysis prep n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_prep_n500_20260514T204203_result.json`
- **Structured JSON:** [`6a3cb3e2cae8eaca0789.json`](../../sessions/6a/6a3cb3e2cae8eaca0789.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，16/16 conditions 全部正确加载，输出符合预期：

- **Median D + bootstrap CI**: importance 条件下 D 显著 > 0，random 条件多数 CI 跨零
- **Within-importance d_z**: importance 家族所有 sparsity 对比均 Bonferroni 显著（medium~large），random 家族大部分 ns
- JSON 和 markdown report 均已输出到 `analysis_output/`

脚本位于 `/root/autodl-tmp/pacs/analyze_n500.py`，n=500 数据就绪后直接运行：
```bash
python analyze_n500.py          # 正式分析
python analyze_n500.py --model deepseek  # 单模型
```

---
