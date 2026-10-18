# diagnose westd41074 cuda01

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd41074_cuda01_20260522T155209_result.json`
- **Structured JSON:** [`859b81c6a49498552e25.json`](../../sessions/85/859b81c6a49498552e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正在推进（T0 ep=30, 67%）。现在情况清楚了，汇报如下：

---

## 诊断结果

### 1. cuda:1 "崩溃"原因
**进程没有崩溃 — 它跑在了 cuda:0 上。** PID 723360 的命令是 `--gpu 1`，但启动时**没有设 CUDA_VISIBLE_DEVICES**，PyTorch 模型加载默认落到了 cuda:0。cuda:1 从未被真正使用（3 MiB）。

### 2. cuda:0 实验身份
就是这个 l2norm k0.5 eval 本身：
```
python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_goal --n_episodes 50 --seed 42 --gpu 1
```
PID 723360, 10430 MiB on cuda:0, Running 状态，日志正常输出到 T0 ep=30 (20/30=67%)。

### 3. 四卡 GPU 状态
| GPU | Memory | 实验 |
|-----|--------|------|
| cuda:0 | 10430 MiB, 32% | **eval_pi05_l2norm_k05_goal_seed42** (误跑在此) |
| cuda:1 | 3 MiB, 0% | 空闲 |
| cuda:2 | 10667 MiB, 45% | pi05 attention k0.9 object s42 (正常) |
| cuda:3 | 27535 MiB, 0% | train_openvla_sc_m64_seed42_v6 (正常) |

### 4. 已完成的 session
- `smolvla_spatial` — 已完成（official_libero_spatial_baseline）
- `xvla_long` — 已完成（xvla_long_l2norm_k09）

### 决策点
进程已在 cuda:0 上跑了 ~8 分钟，T0 进度 30/50。全 10 个 task 预计还需 ~1.5 小时。两个选择：

**A)** 让它在 cuda:0 上跑完（cuda:0 此时无冲突，cuda:1 闲置）
**B)** Kill 掉，用正确的 `CUDA_VISIBLE_DEVICES=1` 重新部署到 cuda:1

要哪个？

---
