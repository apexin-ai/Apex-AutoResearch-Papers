# ops gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check_20260514T062600_result.json`
- **Structured JSON:** [`43522144e1ef8a3fd42e.json`](../../sessions/43/43522144e1ef8a3fd42e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 (2026-05-14 14:26 UTC)

```
GPU 0: 利用率 46%, 显存 23382/24564 MiB (95.2%), 进程:
  - PID 251924, SFT Qwen2.5-1.5B_d100_s42,  10046 MiB, 运行 5h18m
  - PID 291380, SFT Qwen2.5-3B_d100_s42,     13322 MiB, 运行 1h44m

GPU 1: 利用率 53%, 显存 21692/24564 MiB (88.3%), 进程:
  - PID 249294, eval Qwen2.5-3B_d000_s42,    13484 MiB, 运行 5h32m
  - PID 255322, eval Qwen2.5-0.5B_d005_s42,   8194 MiB, 运行 4h58m

GPU 2: 利用率 55%, 显存 7330/24564 MiB (29.8%), 进程:
  - PID 266521, eval Qwen2.5-0.5B_d000_s42,   3658 MiB, 运行 3h47m
  - PID 266790, eval Qwen2.5-0.5B_d100_s42,   3658 MiB, 运行 3h47m

GPU 3: 利用率 0%, 显存 0/24564 MiB (0%) ✅ 完全空闲
  - 无任何进程

GPU 4: 利用率 18%, 显存 18547/24564 MiB (75.5%), 进程:
  - PID 271921, SFT Qwen2.5-1.5B_d005_s42,  18538 MiB, 运行 3h14m

GPU 5: 利用率 0%, 显存 0/24564 MiB (0%) ✅ 完全空闲
  - 无任何进程
```

### 重点标注

**GPU 3 确认完全空闲** — 0% 利用率，0 MiB 显存，无任何进程。注意：tmux session `exp_001_sft_d100_3B` 的 wrapper 设了 `CUDA_VISIBLE_DEVICES=3`，但其实际训练进程 PID 291380 跑在了 **物理 GPU 0** 上（nvidia-smi UUID 确认）。可能是脚本内部 `--gpu 0` 参数覆盖了环境变量。

**GPU 0 显存压力极高** — 95.2% 已用（23382/24564 MiB），两个 SFT 同时跑：
- 1.5B d100 (10046 MiB) — 已跑 5h18m
- 3B d100 (13322 MiB) — 已跑 1h44m，本应在 GPU 3 上

### Tmux Sessions (5个)

| Session | 创建时间 |
|---------|---------|
| exp_001_eval_3B_d000_s42 | 08:54 |
| exp_001_sft_d100_15B_v2 | 09:08 |
| exp_001_eval_05B_d000_s42_v5 | 10:39 |
| exp_001_eval_05B_d100_v5 | 10:39 |
| exp_001_sft_d100_3B | 12:42 |

### 补充发现

后台还有 3 个非实验的 python 进程在跑（无 GPU 占用）：`test_dryrun.py` ×2、`test_dryrun_v2.py` ×1，CPU 占用极高（1994%/2614%/2568%）。另外 `exp_001_sft_d100_3B` 的 SFT 训练还 fork 了 4 个子进程（PID 292651-292656），虽然没出现在 nvidia-smi 中，但占用大量内存。

---
