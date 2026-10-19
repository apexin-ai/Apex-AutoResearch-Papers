# check bjb2 servers d021

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-servers-d021_20260515T020536_result.json`
- **Structured JSON:** [`df627347d6a8dc2e2b9b.json`](../../sessions/df/df627347d6a8dc2e2b9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-40593
- **GPU 0**: 占用（99% util, 11.8GB/24.6GB VRAM）
- **运行中的实验**:
  1. `eval-reconvla-object` — ReconVLA baseline, object benchmark, K=10, n_rollouts=20（刚启动，正在加载环境）
  2. `eval-acr-spatial-v4-default-r3` — ACR-VLA, spatial benchmark, K=10, n_rollouts=10, CRM perdof（刚启动，正在加载环境）
- **已有结果**: `eval-vla-mean-spatial-t10.json` — VLA mean baseline spatial, success_rate=0.1
- **可用于新任务**: NO

## bjb2-28827
- **SSH**: OK
- **PyTorch**: torch=2.10.0+cu128, CUDA OK
- **GPUs**: 6 × RTX 4090（全部空闲，0MB VRAM 占用）
- **Code synced**: NO（`/root/acr-vla-conformal-refinement/` 不存在）
- **Checkpoints**: NO
- **Precompute cache v5**: NO
- **LIBERO data**: NO
- **SmolVLA model**: NO
- **autodl-tmp**: 存在但为空
- **Ready for experiments**: NO
- **Blockers**:
  1. 项目代码未同步
  2. 无 checkpoints / cache / LIBERO 数据 / SmolVLA 模型
  3. 需要从 bjb2-40593 或远程拉取全部数据

---
