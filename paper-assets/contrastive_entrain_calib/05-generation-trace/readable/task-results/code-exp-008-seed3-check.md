# code exp 008 seed3 check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-seed3-check_20260525T001807_result.json`
- **Structured JSON:** [`271ef60df0f416af7a1b.json`](../../sessions/27/271ef60df0f416af7a1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**exp-008-seed3 训练结果：**
- 2000/2000 步完成，checkpoints: 500/1000/1500/2000/final
- 最终 loss=-0.0675, sft=0.0003, R3=0.6775, **S(t)=0.0000**（step ~50 后崩塌为 0）
- Probe 每次 retrain 都达到 acc=1.0 / auroc=1.0 — 与 seed2 一致，probe 被 gaming
- cuda:0 空闲，cuda:1 仍被 exp-003-len512-v3 占用

**已执行操作：**
1. Registry 更新为 ANALYZING，写入 metrics 和 checkpoint_path
2. 删除 exp-008-seed3 训练监控 cron
3. 启动 seed2+seed3 联合全量 eval（PID 736353, 10 个 checkpoint × preset + entropy）
4. 设置每小时 :48 监控 cron 检查 eval 完成状态

---
