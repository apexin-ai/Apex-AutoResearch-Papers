# exp random50 baseline gpu0

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_random50_baseline_gpu0_20260513T112457_result.json`
- **Structured JSON:** [`40b81d0133a061a6daa2.json`](../../sessions/40/40b81d0133a061a6daa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，运行 1 分 14 秒，RSS ~5GB，正在加载数据/模型。输出缓冲还未 flush 到 tmux。

---

## 产出报告

### 1. seed123 external_only 完整 8 代 metrics

| Gen | PPL | RankMe | k-NN | Rare n-gram | Rank Corr | Sel. Ratio |
|-----|--------|--------|-------|-------------|-----------|------------|
| 0 | 36.66 | 273.12 | 0.988 | 0.0293 | -0.0034 | 1.0843 |
| 1 | 44.75 | 292.34 | 0.988 | 0.0205 | -0.0409 | 1.1015 |
| 2 | 52.21 | 298.54 | 0.988 | 0.0146 | -0.0338 | 1.1547 |
| 3 | 58.40 | 299.05 | 0.988 | 0.0122 | -0.0124 | 1.1577 |
| 4 | 54.89 | 299.42 | 0.988 | 0.0114 | 0.0033 | 1.1395 |
| 5 | 51.71 | 294.95 | 0.988 | 0.0108 | -0.0026 | 1.0942 |
| 6 | 49.17 | 293.70 | 0.988 | 0.0105 | 0.0000 | 1.2248 |
| 7 | 49.66 | 290.82 | 0.988 | 0.0104 | 0.0111 | 1.1299 |

Registry 已更新：status=DONE, conclusion=success，含完整 metrics。

### 2. GPU 0 Reset

`nvidia-smi --gpu-reset` 不支持此硬件（"Not Supported"）。nvidia-smi 仍显示 ~49GB ghost memory，但无 compute 进程绑定 GPU 0。实测 `torch.cuda` 可正常分配 4GB tensor，GPU 0 可用。

### 3. random_50 代码修改

三处修改：
- **L8**: 添加 `import random`
- **L37**: argparse choices 增加 `"random_50"`
- **L118-128**: `run_selection()` 新增 `random_50` 分支 — 用 `random.Random(seed + gen)` 做可复现随机选择，选 50% candidates，返回 sorted indices

启动脚本 `run_random50.sh` 超参数与 Phase 2 seed=42 一致（lr=1e-4, epochs=5, gen_tokens=1M, 8 代, self_iterate, gpt2）。

### 4. 新实验

- **PID**: 215364
- **tmux session**: `phase2_random50`
- **exp_id**: `phase2_random50_baseline` (RUNNING)
- GPU 0, 正在加载数据/模型

### 5. 问题

无失败步骤。唯一注意点：`submit_training_job` 工具不可用，改用 tmux 手动启动。

---
