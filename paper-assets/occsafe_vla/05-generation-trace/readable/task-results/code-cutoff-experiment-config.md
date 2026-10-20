# code cutoff experiment config

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cutoff-experiment-config_20260521T132507_result.json`
- **Structured JSON:** [`6a6c0ae1a8381ff10e9f.json`](../../sessions/6a/6a6c0ae1a8381ff10e9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/root/occsafe_vla/scripts/cutoff_experiments.sh`，语法检查通过。

**3 个 cutoff 配置的关键差异：**

| 配置 | `occ_loss_cutoff_step` | `run_root_dir` | 设计意图 |
|------|----------------------|----------------|----------|
| cutoff_25K | 25000 | `cutoff_25K_s0` | 最早关闭，OCC 暴露 25K 步（总训练的 50%），剩余 25K 步专注恢复 TSR。测试最小暴露量下限 |
| cutoff_35K | 35000 | `cutoff_35K_s0` | CAR 开始追赶 vanilla 的拐点处关闭，OCC 暴露 70%，留 15K 步恢复 TSR |
| cutoff_40K | 40000 | `cutoff_40K_s0` | CAR 追平 vanilla 的时间点关闭，OCC 暴露 80%，最大化空间感知学习，仅留 10K 步恢复 TSR |

其余参数完全相同：`occ_loss_weight=0.01`（默认恒定）、`occ_detach=false`、`max_steps=50005`、`seed=42`。每个命令预留了 `CUDA_VISIBLE_DEVICES={GPU}` 占位。

---
