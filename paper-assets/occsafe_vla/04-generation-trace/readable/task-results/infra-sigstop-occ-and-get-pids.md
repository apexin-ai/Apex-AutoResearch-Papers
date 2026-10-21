# infra sigstop occ and get pids

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_sigstop_occ_and_get_pids_20260520T092742_result.json`
- **Structured JSON:** [`c1a8894fbec43502d4bf.json`](../../sessions/c1/c1a8894fbec43502d4bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. SIGSTOP — 成功

全部 10 个 `extract_occupancy.py` 进程已暂停，状态均为 `Tl`（stopped）：

| PID | 状态 |
|-----|------|
| 50744, 51032, 51482, 51931, 52381 | Tl |
| 52769, 53280, 53636, 53988, 72346 | Tl |

**速度恢复**：vanilla_s0（GPU 0）当前 **1.09 it/s**（≈0.92 s/it），相比之前的 1.8 s/it 已大幅恢复，接近原始 1.02 s/it。注意 occ 进程仍占用 ~5.5GB VRAM（SIGSTOP 只暂停计算，不释放显存）。

### 2. 训练进程信息

| Session | GPU | Worker PID | Seed | 当前 Step | 速度 | Checkpoint 目录 |
|---------|-----|-----------|------|-----------|------|----------------|
| `vanilla_s0` | 0 | 100203 | 42 | 310/50005 | 1.09 it/s | `/root/autodl-tmp/checkpoints/vanilla_s0` |
| `vanilla_s1` | 1 | 97847 | 43 | 408/50005 | 1.09 it/s | `/root/autodl-tmp/checkpoints/vanilla_s1` |
| `vanilla_s2` | 2 | 98174 | 44 | 403/50005 | 1.06 it/s | `/root/autodl-tmp/checkpoints/vanilla_s2` |

三个训练均正常运行，无 timeout wrapper，配置一致（openvla-7b, libero_spatial_no_noops, batch_size=8, lr=5e-4, lora_rank=32, max_steps=50005）。

### 3. GPU 3 — 完全空闲

- 显存：1MiB / 97887MiB
- 利用率：0%
- 无任何进程占用

---
