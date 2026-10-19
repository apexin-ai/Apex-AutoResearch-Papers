# diagnose seed4 seed5 failures

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed4_seed5_failures_20260521T073747_result.json`
- **Structured JSON:** [`219a6bf7e0d3794eee34.json`](../../sessions/21/219a6bf7e0d3794eee34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### Seed 4 (bjb1-17606)

| 项目 | 状态 |
|------|------|
| **训练进度** | 完成 8 个 training step（step 0 val + step 1-8 train），在 step 9 rollout 阶段崩溃 |
| **崩溃点** | `env.reset()` → `fast_downward.load_lib()` → 复制 `libdownward.so` 到 `/root/autodl-tmp/tmp/` 时 ENOSPC |
| **Checkpoint** | `global_step_5` 存在（21GB），包含完整的 actor model + optimizer（2 ranks），**可用于恢复** |
| **磁盘** | 250G 总量，231G 已用，**仅剩 20G（93%）** |

bjb1 磁盘明细（checkpoints 共 187G）：

| 目录 | 大小 | 备注 |
|------|------|------|
| hsweep-h2 | 41G | 旧实验 |
| qwen3_8b_sft_v1 | 31G | SFT 模型 |
| exp021_ragen_sft_v4 | 23G | 旧实验 |
| exp029 | 21G | Seed 1 |
| exp029-seed3 | 21G | Seed 3 |
| exp029-seed4 | 21G | 本次（仅 1 个 ckpt） |
| hsweep-h20 | 21G | 旧实验 |
| exp029_hf | 3.8G | HF 格式 |
| scienceworld_sft | 7.6G | 旧实验 |

---

### Seed 5 (westd-47453)

| 项目 | 状态 |
|------|------|
| **训练进度** | 仅完成 step 0（validation eval），**未完成任何 training step** |
| **崩溃点** | 第 1 个 training step 的 `loss.backward()`（`update_actor` 阶段），尝试分配 9.25 GiB 时 OOM |
| **OOM 原因** | Seed 6 进程（PID 704924/704925）泄漏到 GPU 0，占用 37.7 GiB；Seed 5 自身占 49 GiB；GPU 0 总共 95 GiB，仅剩 8.25 GiB |
| **Checkpoint** | **无**。`exp029-seed5` 目录不存在 |
| **GPU 当前状态** | 4 张 GPU 全部空闲（0 MiB），无运行进程 |
| **磁盘** | 250G 总量，184G 已用，67G 可用（74%） |

westd 磁盘明细（checkpoints 共 131G）：

| 目录 | 大小 |
|------|------|
| exp029-seed3 | 66G |
| exp029-seed6 | 55G |
| qwen3_scienceworld_sft | 7.6G |
| qwen3_exp021_ragen_sft_v4 | 3.3G |
| 其余（空目录） | 0 |

---

### 可恢复性总结

- **Seed 4**: 可从 `global_step_5` 恢复，但需先清理 bjb1 磁盘。可回收候选：`hsweep-h2`（41G）、`hsweep-h20`（21G）、`qwen3_8b_sft_v1`（31G）、`exp021_ragen_sft_v4`（23G）= 最多回收 ~116G。
- **Seed 5**: 不可恢复，必须从头重跑。GPU 冲突问题（Seed 6 泄漏到 GPU 0）已自行解决（当前无进程），但重跑时需确保 `CUDA_VISIBLE_DEVICES` 隔离正确。

---
