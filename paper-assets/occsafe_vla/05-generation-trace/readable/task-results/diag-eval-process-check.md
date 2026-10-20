# diag eval process check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-process-check_20260522T013732_result.json`
- **Structured JSON:** [`b3376ad853501294668f.json`](../../sessions/b3/b3376ad853501294668f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Checkpoint 状态
4 个 ablation 的 `50000_chkpt` **全部存在**：

| Ablation | 50000_chkpt | 创建时间 |
|---|---|---|
| ablation_occ_detach_s0 | ✅ | 09:34 |
| ablation_random_occ_s0 | ✅ | 09:32 |
| ablation_occ_detach_s1 | ✅ | 09:32 |
| ablation_random_occ_s1 | ✅ | 09:32 |

### GPU 进程状态 — **GPU 0 和 GPU 1 有冲突**

| GPU | 内存占用 | 进程 | 问题 |
|---|---|---|---|
| **GPU 0** | 33553/97887 MiB | **2 个 eval 进程** | ⚠️ 冲突 |
| **GPU 1** | 32986/97887 MiB | **2 个 eval 进程** | ⚠️ 冲突 |
| GPU 2 | 16778/97887 MiB | 1 个 eval 进程 | ✅ 正常 |
| GPU 3 | 16778/97887 MiB | 1 个 eval 进程 | ✅ 正常 |

### 冲突详情

**两批 eval 同时在跑：**

**Batch 1**（20 rollouts，09:31 启动，4 GPU 各 1 个）— 来自 `eval:ablation-4gpu-parallel`：
- PID 614640 (GPU 0): `ablation_occ_detach_s0`, 20 rollouts → `/root/occsafe_vla/eval_results/`
- PID 614641 (GPU 1): `ablation_random_occ_s0`, 20 rollouts
- PID 614642 (GPU 2): `ablation_occ_detach_s1`, 20 rollouts
- PID 614643 (GPU 3): `ablation_random_occ_s1`, 20 rollouts
- 进度：都在 Task 3/10，约 50-90% rollouts

**Batch 2**（50 rollouts，09:32-09:34 启动）— 来自 `eval:ablation-batch-4`：
- PID 632709 (GPU 0): `ablation_occ_detach_s0`, **50 rollouts**, seed 42 → `/root/autodl-tmp/checkpoints/ablation_occ_detach_s0/eval_results.json`
- PID 615702 (GPU 1): `ablation_random_occ_s0`, **50 rollouts** → `/root/autodl-tmp/checkpoints/ablation_random_occ_s0/eval_results.json`
- GPU 2、3 的 s1 eval 尚未被 Batch 2 启动

**Batch 2 进度**：
- GPU 0 (detach_s0, 50r): Task 0 刚完成 (TSR=0.980)，开始 Task 1
- GPU 1 (random_s0, 50r): Task 1 进行中 (40%)

### 关键问题

1. **GPU 0、1 双重占用**：每张卡上同时跑着 20r 和 50r 两个 eval，两个进程争抢同一 GPU。虽然 98GB 显存暂时够用（~33GB/卡），但会互相拖慢。
2. **结果冲突风险**：两批 eval 对同一 checkpoint 产出不同 rollout 数的结果文件（20r vs 50r），输出路径不同所以文件不会覆盖，但分析时需要区分。
3. **Batch 2 不完整**：只启动了 s0 的两个 eval（GPU 0、1），s1 的两个（GPU 2、3）还没启动。如果后续 Batch 2 worker 再启动 s1 eval，GPU 2、3 也会出现同样的双重占用。

### 建议处置
- 如果 50 rollouts 才是最终需要的结果，可以 kill Batch 1 的 4 个进程（PID 614640-614643）释放资源
- 如果 20 rollouts 足够，kill Batch 2 的 2 个进程（PID 632709, 615702）并阻止后续 s1 启动

---
