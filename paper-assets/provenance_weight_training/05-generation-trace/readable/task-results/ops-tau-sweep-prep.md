# ops tau sweep prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tau-sweep-prep_20260515T124047_result.json`
- **Structured JSON:** [`999c31f691d3632fe5f7.json`](../../sessions/99/999c31f691d3632fe5f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**当前训练进度**：4 个实验全部正常运行。
- ess_only_seed42 (cuda:1): **96%**，~9 min 后完成
- golden_ratio_seed42 (cuda:0): **82%**，~38 min
- tau_06_seed42 (cuda:3): **71%**，~65 min
- nmin1_seed42 (cuda:2): **64%**，~81 min

**τ sweep 就绪状态**：**全部就绪。** 无需独立脚本，通过 submit_training_job 提交即可。完整训练命令已从运行中 tau_06 进程提取并适配 4 个 τ 值 (0.5/0.7/0.9/0.95)。关键参数 (contamination_ratio=0.4, WANDB_MODE=disabled, 无 inline eval, bf16) 均已确认。

**磁盘**：数据盘 147G 可用，新增 ~12G，充足。

报告写入 `artifacts/tau_sweep_readiness.md`。

---
