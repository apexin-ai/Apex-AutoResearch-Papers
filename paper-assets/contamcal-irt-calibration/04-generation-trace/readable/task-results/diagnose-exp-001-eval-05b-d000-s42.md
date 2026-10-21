# diagnose exp 001 eval 05B d000 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_d000_s42_20260514T013129_result.json`
- **Structured JSON:** [`a7ca67841db3078ada7d.json`](../../sessions/a7/a7ca67841db3078ada7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断与重跑完成。

**根因**：输出目录 `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42` 在 eval 运行 2.5 小时期间被并发进程删除。四个 benchmark 全部计算完成（mmlu=0.4049, gsm8k=0.3647, arc=0.3780, humaneval=0.1098），但写 `eval_results.json` 时目录已不存在。

**已执行**：
- Registry `failure_reason` 已更新
- 清理并重建输出目录
- 在 cuda:2 上以 nohup 重新提交，PID=257029，日志：`exp_001_eval_05B_d000_s42_retry.log`
- Registry 状态已更新为 RUNNING

数据集已在 HF cache 中，这次不会有 HF 连接超时问题，预计 ~30 分钟完成。

---
