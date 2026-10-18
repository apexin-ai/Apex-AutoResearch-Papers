# debug imm eval same sr bug

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_imm_eval_same_sr_bug_20260517T010135_result.json`
- **Structured JSON:** [`9143bc7f8f050f9a12fc.json`](../../sessions/91/9143bc7f8f050f9a12fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

---

## 诊断结果

### CHECKPOINT 路径确认

| | 路径 | 大小 |
|---|---|---|
| IMM v2 | `checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt` | 920 MB |
| IMM 100K | `checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt` | 920 MB |
| **是否相同文件** | **YES — 完全相同的路径** | |

从 `ps aux` 直接确认，当前正在运行的 "IMM 100K" eval 命令：
```
python eval_success_rate_libero.py \
  --checkpoint checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt \
  --config configs/libero_imm_twostage_fullft.yaml \
  --mode acis_prune \
  --output eval_results/imm_fullft_100k_libero_spatial.json
```

与 IMM v2 eval 使用的 checkpoint 和 config **完全一致**。

### PER-TASK SR 对比

由于用的是同一个 checkpoint，结果必然相同：`[0%, 14%, 48%, 10%, 14%, 46%, 0%, 20%, 2%, 0%]` = 77/500 = 15.4%

### ACIS 加载诊断

| 项目 | 结果 |
|---|---|
| Checkpoint 包含 ACIS keys | **YES** (20 keys, trained weights) |
| ACIS 权重在两个 eval 中相同 | **YES** (同一文件) |
| Eval 脚本如何加载 ACIS | **from_checkpoint** (`wrapper.load_state_dict(ckpt["model_state_dict"], strict=False)`) |

### BUG 根因

**不是 eval 代码 bug，是 launch 错误。**

`libero_imm_twostage_fullft` 这个 checkpoint 是基于 **50K baseline** 训练的 IMM 模型（config 中 `baseline_checkpoint: "checkpoints/libero_full_ft_50k/checkpoint.pt"`）。不存在独立的 "IMM 100K" 模型或 config。

"IMM 100K" eval 被错误地启动为指向同一个 checkpoint，输出文件名 `imm_fullft_100k_*` 纯属误导命名。当前 tmux 中运行的 `imm_100k_eval_goal` 和 `imm_100k_eval_spatial` 也会产出相同的（无意义的）结果。

### 下一步

要获得真正的 "IMM 100K" 结果，需要：
1. 创建 `configs/libero_imm_twostage_fullft_100k.yaml`，将 `baseline_checkpoint` 改为 `checkpoints/libero_full_ft_100k/checkpoint.pt`
2. 训练该模型（stage1 10K + stage2 20K）
3. 用新 checkpoint 跑 eval

或者，如果意图是评估现有 `libero_full_ft_100k` baseline 在 `acis_prune` mode 下的表现，那需要一个包含 ACIS 权重的 checkpoint（当前 `libero_full_ft_100k/checkpoint.pt` 是纯 baseline，不含 ACIS）。

---
