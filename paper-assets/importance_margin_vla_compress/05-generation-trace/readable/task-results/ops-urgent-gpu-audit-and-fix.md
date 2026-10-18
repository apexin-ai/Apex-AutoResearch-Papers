# ops urgent gpu audit and fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-audit-and-fix_20260521T054336_result.json`
- **Structured JSON:** [`e51ff9cf0630af10707e.json`](../../sessions/e5/e51ff9cf0630af10707e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 仍在 CPU 端加载模型（π0.5 较大，需 3-5 分钟才会分配 GPU 显存）。进程 PID 838823 正常运行（99% CPU）。

以下是完整报告：

---

## 全服务器 GPU 实况

| 服务器 | GPU | Util% | Mem | PID | 实验 |
|--------|-----|-------|-----|-----|------|
| **westd-41074** | 0 | 0% | 3MiB/98GB | 838823 | **π0.5 l2norm k=0.5** (刚启动，模型加载中) |
| | 1 | 41% | 10.6GB/98GB | 818531 | **π0.5 baseline** (Task 4, 98.0% SR, 进行中) |
| | 2 | 0%* | 28.5GB/98GB | 68539 | **M96 训练** (since May 20) |
| | 3 | 0%* | 27.5GB/98GB | 738642 | **M64 v4 训练** (since 10:44) |
| **westd-38929** | 0 | 64% | 16.0GB/98GB | 568225 | OpenVLA l2norm k=0.5 |
| | 1 | 83% | 16.1GB/98GB | 568905 | OpenVLA random k=0.3 |
| | 2 | 87% | 16.0GB/98GB | 569611 | OpenVLA l2norm k=0.7 |
| | 3 | 69% | 16.1GB/98GB | 570309 | OpenVLA l2norm k=0.3 |
| **cqa1-33015** | 0 | 0%* | 4.0GB/24GB | 118463 | X-VLA random k=0.5 spatial s42 |
| | 1 | 0% | 1MiB/24GB | — | **空闲** |
| | 2 | 29% | 4.5GB/24GB | 60485 | X-VLA random k=0.3 object s42 |
| | 3 | 0%* | 4.3GB/24GB | 61785 | X-VLA random k=0.5 object s43 |
| **westd-27271** | 0 | 0%* | 36.3GB/98GB | 176320 | **eval SC M128** object s42 |
| | 1 | 0%* | 42.2GB/98GB | 921279 | **M32 训练** (since May 20) |

*\* GPU util 瞬时为 0% 但进程活跃（高 CPU），属正常波动。*

## ⚠️ 关键纠正：PID 818531 不是死进程

用户预判 PID 818531 是死进程，**实际它是正在运行的 π0.5 baseline eval**（429% CPU, 41% GPU util, 10.6GB 显存）。正在 Task 4，已完成 4/10 tasks，当前 SR=98.0%。**未 kill**。

## π0.5 baseline eval 进度 (westd-41074:GPU1)
- PID: 818531
- 进度: Task 4/10, ep 20/50
- 当前总 SR: 98.0% (196/200)
- per_task: T0=96%, T1=98%, T2=98%, T3=100%
- GPU util: 41%

## π0.5 l2norm k=0.5 启动结果 (westd-41074:GPU0)
- Shell PID: 838817 → 实际 Python PID: 838823
- 状态: 模型加载中（99% CPU，GPU 显存尚未分配，预计 3-5 min 后开始 eval）
- 脚本确认已修复: `hidden_size` 无匹配 = 无缩放 bug
- 参数: `--prune_mode l2norm --keep_ratio 0.5 --seed 42 --n_episodes 50`
- 日志: `logs/eval_pi05_l2norm_k05_object_seed42.log`

## OpenVLA random k=0.5 结果
- **SR: 35.8%** (179/500)
- per_task: [56%, 2%, 40%, 58%, 60%, 26%, 0%, 12%, 30%, 74%]
- 源文件: `eval_results/openvla_random_k05_seed42.json`
- 耗时: 291 min, seed=42

## 空闲 GPU
- **cqa1-33015:GPU1** — 完全空闲（1MiB），但该服务器没有 `eval_pi05_pruning_libero.py`（只有 `eval_pi05_libero.py`）

---
