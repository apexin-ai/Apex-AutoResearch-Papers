# code c2 n500 analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c2_n500_analysis_prep_20260514T184028_result.json`
- **Structured JSON:** [`27ac033bfb6bb714fb0c.json`](../../sessions/27/27ac033bfb6bb714fb0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

干净通过，16/16 conditions 加载，统计输出正确。

脚本已部署到 `/root/autodl-tmp/pacs/scripts/analyze_c2_n500.py`，dry-run 验证通过。功能：

- **D054 合规**：median + median bootstrap 95% CI 为主指标，mean 仅作参考
- **完整性检查**：n=500 验证、problem_idx 单调性（检测重复进程污染）、duplicate problem_id、null II 统计
- **统计量**：median D, median CI, mean D, Cohen's d_z + CI, Wilcoxon signed-rank (双侧) + Bonferroni 校正
- **paired imp vs rand**：按 problem_id 配对，计算 importance - random 梯度差
- **预注册判断**：自动检查 Qwen s015 CI 是否跨零
- **输出**：`c2_n500_results.json` + `c2_n500_report.md`

实验完成后运行：
```bash
python /root/autodl-tmp/pacs/scripts/analyze_c2_n500.py
```

---
