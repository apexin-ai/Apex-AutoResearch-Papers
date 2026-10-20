# exp deepseek traj func

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deepseek-traj-func_20260516T120511_result.json`
- **Structured JSON:** [`a746cd6932a9c99b3ddd.json`](../../sessions/a7/a746cd6932a9c99b3ddd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。汇报：

**TRAJ 数据**
- `traj_train_cls.jsonl`: 8052 条（从 `test_summary` 重命名为 `test` 字段）
- `traj_val_cls.jsonl`: 1001 条
- 0% truncation，test 字段 max 930 chars

**训练状态**
- PID: 504483，运行在 cuda:2 (RTX 5090)
- 1512 total steps，~2s/step，预计 **~50 分钟**完成
- 模型加载正常，已开始前向/反向，loss 尚未到打印间隔（默认 500 steps）
- 输出目录：`/root/autodl-tmp/checkpoints_deepseek_traj_func/`
- 日志：`/tmp/deepseek_traj_func.log`

---
