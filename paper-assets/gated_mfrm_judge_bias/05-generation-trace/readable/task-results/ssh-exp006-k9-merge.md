# ssh exp006 k9 merge

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp006_k9_merge_20260523T003627_result.json`
- **Structured JSON:** [`59a321e5e09814271d95.json`](../../sessions/59/59a321e5e09814271d95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认没有跳过已有 idata 文件的逻辑。

**汇报：**

1. **不需要手动合并 k=9**。主进程 `--judge-counts 2 4 6 9` 已包含 k=9，跑完 k=6 后会自动跑 k=9 并一次性生成 `results_full/sensitivity_results.csv`。

2. **当前进度**：k=6 还在跑（10 subsets 中 sequential 完成 7/10，joint_gmfrm 完成 6/10）。k=9 只有 1 个 subset，估计几分钟就能完成。

3. **k=8 缺失**：启动命令是 `--judge-counts 2 4 6 9`，跳过了 k=8。代码默认值包含 k=8（C(9,8)=9 subsets），如果需要完整的 sensitivity curve，k=8 需要补跑。

4. **`results_k9/` 是冗余的**——可以在主进程完成后删除，或留作对比验证。

需要我做什么？比如补跑 k=8，或者等主进程跑完后再做分析？

---
