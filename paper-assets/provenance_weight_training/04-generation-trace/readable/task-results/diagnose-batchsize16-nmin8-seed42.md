# diagnose batchsize16 nmin8 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batchsize16_nmin8_seed42_20260517T141502_result.json`
- **Structured JSON:** [`0404195739dc8b3dd5d6.json`](../../sessions/04/0404195739dc8b3dd5d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：实验实际已成功完成，是监控系统误判。**

- 训练跑完了全部 6103 步（13小时），final model 已保存
- 误判原因：脚本直接用 bash 启动而非 `submit_training_job`，没有生成 sentinel 文件；`WANDB_MODE=disabled` 又禁用了 W&B 心跳。监控系统找不到任何完成信号，5 次探测进程已退出后自动判定失败
- 当前 lm_eval 已在服务器上评估该模型（arc_easy task, PID 97397）
- 无需重新训练

报告已写入 `artifacts/diagnose_batchsize16_nmin8_seed42.md`。

---
