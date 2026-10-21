# experiment wave3 dir f blind fol

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wave3-dir-f-blind-fol_20260520T092551_result.json`
- **Structured JSON:** [`790f00ef29325f35c528.json`](../../sessions/79/790f00ef29325f35c528.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行稳定进行中。第 2 题刚完成（99.7 秒），与 dry-run 一致。

**运行状态总结**:
- PID: 378776 (python -u direction_f_blind_fol.py)
- 速度: ~90-100 秒/题
- 预计总耗时: ~5-5.5 小时
- 日志: `/tmp/direction_f_full.log`
- 结果: 每 10 题自动 checkpoint 到 `results/direction_f_blind_fol/results.json`
- 初步趋势: 全部预测 Unknown（blind FOL 约束不足以让 Z3 判定 entailment）

可以随时用 `tail /tmp/direction_f_full.log` 查看进度。

---
