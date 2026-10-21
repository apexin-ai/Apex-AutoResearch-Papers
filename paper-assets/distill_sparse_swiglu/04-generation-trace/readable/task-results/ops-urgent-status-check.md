# ops urgent status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260516T193709_result.json`
- **Structured JSON:** [`cfbe56aaf7008275d3c8.json`](../../sessions/cf/cfbe56aaf7008275d3c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 检查 1: GPU 进程状态

| GPU | 状态 | 进程 |
|-----|------|------|
| **GPU 0** | 空闲 | 0MiB 占用，无进程 |
| **GPU 1** | 满载 | PID 257933，68538MiB/97887MiB，GPU-Util 100%，`python src/train_bce_gumbel.py` |

### 检查 2: Python 训练进程

PID 257933 正在跑 BCE+Gumbel+Lagrangian 训练：
```
python -u src/train_bce_gumbel.py --lr 1e-3 --num_steps 1000 --sparsity_target 0.5
  --output_dir checkpoints/bce_framework_lr1e3 --gpu 0 (CUDA_VISIBLE_DEVICES=1)
```

这是 `run_bce_iso.sh` 的 **Run 2/3 (lr=1e-3)**，Run 1/3 (lr=1e-4) 已完成。当前进度约 step 50/1000，刚进入训练（模型加载完毕）。

脚本结构：3 轮 sequential 训练 (lr=1e-4 → 1e-3 → 3e-3)，用 nohup 启动，日志写 `/root/runs/bce_iso_framework.log`。

### 检查 3: BCE clean isolation 输出

- **Run 1 (lr=1e-4)**: 已完成，checkpoint 存在 `bce_framework_lr1e4/predictor_bce_gumbel.pt` (145MB, 03:35)
- **Run 2 (lr=1e-3)**: 正在训练中，`bce_framework_lr1e3/` 目录为空（尚未保存 checkpoint）
- **Run 3 (lr=3e-3)**: 未开始，`bce_framework_lr3e3/` 目录为空
- 先前的 isocompute 实验 (v1/v2/v3) 的 checkpoint 和 log 也都存在

### 检查 4: C4 OOD eval 结果

**存在**，位于 `/root/distill_sparse_swiglu/results/c4_ood_ppl.json`：

| 方法 | PPL | 时间(s) |
|------|-----|---------|
| Dense | **9.2075** | 14.6 |
| KL predictor 50% | **18.401** | 15.4 |
| TEAL vanilla 50% | **38.7503** | 14.5 |

与预期数字一致 (dense=9.21, KL=18.40, TEAL=38.75)。

### 检查 5: tmux sessions

ssh_read_only 不允许 tmux 命令。但从 ps 输出看，**没有 tmux 进程**。训练是通过 nohup 启动的（符合 C002 约束）。

---

### 结论

- **GPU 0**: 空闲，可用
- **GPU 1**: BCE+Gumbel+Lagrangian framework ablation 正在跑 (Run 2/3, lr=1e-3, ~step 50/1000)
- **BCE clean isolation**: Run 1 完成，Run 2 进行中，Run 3 待启动，预计还需较长时间完成全部 3 轮
- **C4 OOD eval**: 已完成，数据确认无误
- **无 tmux session**，训练用 nohup 后台运行

---
