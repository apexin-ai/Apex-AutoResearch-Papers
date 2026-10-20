# infra westd 51268 verify and submit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-51268-verify-and-submit_20260526T030746_result.json`
- **Structured JSON:** [`e10be20ff78f7acc0cb7.json`](../../sessions/e1/e10be20ff78f7acc0cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇报如下：

---

## 汇报

### 1. GPU 型号和数量
**2x NVIDIA RTX PRO 6000 Blackwell Server Edition**, 各 96GB VRAM, Driver 595.58, CUDA 13.2

### 2. 代码版本
从 bjb1-45299 同步，commit `fb56c86` (sync: all local changes for bjb1-40020 setup)。数据盘原已清空，通过 rsync 恢复。

### 3. 磁盘空间
`/root/autodl-tmp`: 250GB 可用（使用量 <2GB）

### 4. exp_094 checkpoint 状态
**不可复用**。数据盘被清空，westd 和 bjb1 均无 exp_094_cheetah_008d_s3 目录。

### 5. exp_097 提交状态
- **状态**: RUNNING
- **PID**: 3794
- **tmux session**: `exp_097_cheetah_008d_s3`
- **GPU**: cuda:0
- **进展**: step ~8000/105000，prefill 完成，正常训练中
- 从头开始（无可复用 checkpoint）

### 6. plan_030 RSSM Fidelity 分析结果

| Model | dt1 obs_MSE | dt2 obs_MSE | Ratio | dt1 rew_MAE | dt2 rew_MAE | Ratio |
|---|---|---|---|---|---|---|
| **baseline** | 15.08 | 23.40 | **1.552x** | 0.046 | 0.063 | **1.363x** |
| **trained_dt_emb** | 12.37 | 17.80 | **1.439x** | 0.055 | 0.083 | **1.495x** |
| **no_dt_emb** | 21.33 | 26.34 | **1.235x** | 0.069 | 0.080 | **1.162x** |
| **frozen_dt_emb** | 17.26 | 24.05 | **1.394x** | 0.066 | 0.091 | **1.368x** |

关键发现：
- **所有模型** dt=2 重建误差均高于 dt=1（1.24-1.55x），确认 RSSM fidelity gap 是结构性的
- **trained_dt_emb** reward 退化最严重（1.495x）——虽然 obs_mse ratio 最低，但 reward 预测更差，支持 delusional critic 假说
- **no_dt_emb** 总体 gap 最小（1.235x obs, 1.162x reward），但绝对误差最高（dt1=21.33 vs baseline dt1=15.08）

### 7. 异常
- 实例重启后数据盘完全清空（`/root/autodl-tmp` 为空），需要重新 clone 代码和安装依赖
- GPU 0 显示 49GB 内存占用但无进程（driver 层面的 context 预留，不影响使用）
- 需要额外安装 `gymnasium`, `dm_control`, `gym`, `tmux`, `libegl1-mesa-dev` 等依赖

---
