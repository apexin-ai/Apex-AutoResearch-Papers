# analysis dedup sensitivity r1n2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dedup_sensitivity_r1n2_20260518T201544_result.json`
- **Structured JSON:** [`33907749b732b92c815d.json`](../../sessions/33/33907749b732b92c815d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**1. Dedup 对 accuracy 无影响**（19 个实验 delta 全为 0.00pp）。原因：数据集每个 problem 恰好 10 条样本，sample-level 和 problem-level averaging 数学等价。

**2. Train-test 零泄漏**：4 个 condition 均验证 problem_id overlap = 0，exact input overlap = 0。训练集 472 problems，测试集 119 problems，按 problem 80/20 划分，完全不交叉。

**3. 对 reviewer 的回应要点**：
- 数据划分在 problem level 执行，无 leakage
- 每个 problem 均匀 10 条样本，无 aggregation bias
- Problem-level macro accuracy 与 sample-level micro accuracy 一致，结论 robust

脚本在服务器 `/root/trace-verdict-study/eval/dedup_sensitivity.py`，artifact 已注册 `art_20260518_af0e34`。

---
