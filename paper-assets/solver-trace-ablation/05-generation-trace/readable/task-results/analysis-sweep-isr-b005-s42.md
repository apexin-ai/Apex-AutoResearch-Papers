# analysis sweep isr b005 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sweep-isr-b005-s42_20260516T025842_result.json`
- **Structured JSON:** [`80ed17d989f0950236a5.json`](../../sessions/80/80ed17d989f0950236a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**sweep-isr-b005-s42 无法完成分析 — 正在重训中。**

原因链：
1. 原始训练只跑了 **100 步**（`train_grpo.py` 默认值 100，命令行没传 `--num_steps`，config 的 500 没被正确合并）
2. 另一个 worker 发现问题后删除了 checkpoint 并以 **500 步** 重新启动训练
3. 我启动的 eval 在 **97/100 样本处被中断**（模型文件被删除）
4. 新的 500 步训练正在运行（当前 ~step 36/500，预计 ~50 分钟完成）

**已完成操作：**
- Registry 已更新为 RUNNING（retry_count=1）
- 临时分析报告已写入 `artifacts/sweep-isr-b005-s42/analysis_report.md`
- 记录了原始 100 步训练的 partial eval 数据（3/96 proved, prove_rate=3.1%）

**待完成（500步训练完成后）：**
- 用 `eval_sta.py --data_path data/proofwriter_fol_100.jsonl` 重新评估
- 用 `classify_h7.py` 做 hacking taxonomy 分析
- 与 β=0.1/0.3 baselines 对比，判断 dose-response 假设

---
