# ops gpu status confirm

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-confirm_20260514T062929_result.json`
- **Structured JSON:** [`9647de4cd5cbc5593732.json`](../../sessions/96/9647de4cd5cbc5593732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU→进程映射表

| GPU | 进程 | 显存 | 利用率 |
|-----|------|------|--------|
| **0** | PID 251924 (1.5B d100 SFT, 10046 MiB) + PID 291380 (3B d100 SFT, 13322 MiB) | **23382 / 24564 MiB (95%)** | 50% |
| **1** | — | 0 MiB | 0% |
| **2** | PID 266521 (0.5B d000 eval, 3658 MiB) + PID 266790 (0.5B d100 eval, 3658 MiB) | 7330 / 24564 MiB | 53% |
| **3** | — | **0 MiB (空闲)** | 0% |
| **4** | PID 271921 (1.5B d005 SFT, 18538 MiB) | 18547 / 24564 MiB | 11% |
| **5** | — | 0 MiB | 0% |

## 3B SFT 确认跑错 GPU

**是的，确认跑错了。** 实际在 GPU 0，不在 GPU 3。

根因：PID 291373 wrapper 设了 `export CUDA_VISIBLE_DEVICES=3`，但 train_sft.py 脚本内部用 `--gpu 0` 参数重新覆盖了 `CUDA_VISIBLE_DEVICES="0"`，导致实际绑定物理 GPU 0。

证据链：
1. `/proc/291373/environ` → 初始 `CUDA_VISIBLE_DEVICES=3`
2. 命令参数 → `--gpu 0`
3. nvidia-smi → PID 291380 在 GPU 0 占用 13322 MiB
4. GPU 3 完全空闲 0 MiB

## PID 存活状态

| Registry PID | 实际状态 |
|---|---|
| 251924 | ✅ ALIVE（wrapper PID，python child 也是 251924） |
| 249294 | ❌ DEAD |
| 255322 | ❌ DEAD |
| 266511 → child 266521 | ✅ ALIVE |
| 266780 → child 266790 | ✅ ALIVE |
| 271916 → child 271921 | ✅ ALIVE |
| 291373 → child 291380 | ✅ ALIVE |

## 3B SFT 训练进度

- Step 508/4159 (12%)，已运行 ~2h05m
- 速度 ~14s/step，预计剩余 ~14h
- loss 稳定下降中 (1.12-1.20)，训练本身正常

## 影响

GPU 0 两个 SFT 进程抢 VRAM（95% 占满），可能互相降速。GPU 3 白白空闲。

---
