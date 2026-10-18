# diag full server survey 20260523

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full-server-survey-20260523_20260523T191423_result.json`
- **Structured JSON:** [`a2a3c0ce695226621a29.json`](../../sessions/a2/a2a3c0ce695226621a29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux ls 被 read-only 模式阻止，不影响核心信息。以下是完整报告：

---

## GPU 进程巡检报告（2026-05-23）

### 总览表

| 服务器 | GPU | PID | 实验名 | 状态 | 内存占用 |
|--------|-----|-----|--------|------|----------|
| **westd-38929** | 0 | 179279 | xvla_l2norm_k0.5_spatial | 运行中 | 4920/97887 MiB |
| westd-38929 | 1 | 179514 | xvla_l2norm_k0.5_goal | 运行中 | 4838/97887 MiB |
| westd-38929 | 2 | 224430 | xvla_l2norm_k0.3_spatial | 运行中 | 4920/97887 MiB |
| westd-38929 | 3 | 367660 | xvla_l2norm_k0.3_goal | 运行中 | 4838/97887 MiB |
| **westd-27271** | 0 | 380590 | openvla_l2norm_k0.5_goal | 运行中 | 15946/97887 MiB |
| westd-27271 | 1 | 291098 | openvla_baseline_libero10 | 运行中 | 16375/97887 MiB |
| **westd-41074** | 0 | 728249 | pi05_l2norm_k0.925_goal_s43 | 运行中 | 10526/97887 MiB |
| westd-41074 | 1 | 763841 | pi05_l2norm_k0.5_libero10 | 运行中 | 10651/97887 MiB |
| westd-41074 | 2 | 781247 | pi05_random_k0.925_spatial | 运行中 | 10608/97887 MiB |
| westd-41074 | 3 | 764088 | pi05_random_k0.5_libero10 | 运行中 | 9952/97887 MiB |
| **cqa1-33015** | 0 | 88440 | pi05_random_k0.5_goal | 运行中 | 10178/24564 MiB |
| cqa1-33015 | 1 | 88538 | pi05_random_k0.85_goal | 运行中 | 10274/24564 MiB |
| cqa1-33015 | 2 | 88688 | pi05_l2norm_k0.85_goal | 运行中 | 10276/24564 MiB |
| cqa1-33015 | 3 | 97992 | pi05_random_k0.3_goal_s43 | 运行中 | 10122/24564 MiB |

### 1. 空闲 GPU

**无。** 所有 14 张 GPU 均有进程占用（westd-38929 × 4, westd-27271 × 2, westd-41074 × 4, cqa1-33015 × 4）。

### 2. cqa1-33015 上 4 个 π0.5 实验状态

全部仍在运行，PID 和实验详情：

| PID | prune_mode | keep_ratio | suite | seed |
|-----|-----------|------------|-------|------|
| 88440 | random | 0.5 | libero_goal | 42 |
| 88538 | random | 0.85 | libero_goal | 42 |
| 88688 | l2norm | 0.85 | libero_goal | 42 |
| 97992 | random | 0.3 | libero_goal | 43 |

### 3. 异常

- **westd-38929 GPU 分配异常**：4 个进程的 `--gpu 0` 参数均指定 GPU 0，但实际通过 CUDA_VISIBLE_DEVICES 分别映射到了 4 张不同的物理 GPU（每张各 1 个进程，无 stacking）。这是正常的——说明启动脚本通过环境变量隔离了 GPU。
- **无 stacking**：所有服务器每张 GPU 上均只有 1 个进程。
- **无连接失败**：4 台服务器全部正常连接。
- **westd-38929 内存占用极低**（~5GB/98GB），X-VLA 评估显存需求远小于 π0.5。

---
