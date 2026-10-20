# diag deepseek cwm repo s42 epoch2 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_deepseek-cwm-repo-s42-epoch2-eval_20260519T034702_result.json`
- **Structured JSON:** [`3638d28cb16bb7809b62.json`](../../sessions/36/3638d28cb16bb7809b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇报：

**退出原因：** 被手动 kill 为 `cwm-s42-e3-seq2048` eval 腾 GPU。最后日志 21:50:22，新 session 创建于 21:51:12。

**部分结果（可回收）：**
- 3050/9784 样本（31.2%），running_acc = **66.8-66.9%**
- 增量结果保存在 `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_epoch2/results_incremental.jsonl`

**过拟合假设初步信号：** epoch 2 partial 66.9% vs epoch 3 的 58.7%，差 ~8pp，方向上支持 epoch 3 过拟合。但仅 31% 测试集覆盖率，不够 conclusive。

**已清理：** cron 已删除，registry 标记为 DONE/killed。

**建议下一步：**
1. 如果 epoch 3 seq2048 eval 完成后仍需 epoch 2 完整结果，可用 `results_incremental.jsonl` 做断点续跑（已有 3050 条，只需跑剩余 6734 条）
2. 也可直接用 3050 条部分结果做统计检验（bootstrap CI），如果 CI 下界仍 >> 58.7% 就足够 conclusive，不需要跑满

---
