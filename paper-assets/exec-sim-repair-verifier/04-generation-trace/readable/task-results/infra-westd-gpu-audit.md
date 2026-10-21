# infra westd gpu audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-gpu-audit_20260514T193722_result.json`
- **Structured JSON:** [`9cc366e46b29d38668e3.json`](../../sessions/9c/9cc366e46b29d38668e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告

### GPU 状态总览

| GPU | 型号 | 显存占用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| cuda:0 | RTX 5090 | 0 / 32607 MiB | 0% | **空闲** |
| cuda:1 | RTX 5090 | 0 / 32607 MiB | 0% | **空闲** |
| cuda:2 | RTX 5090 | 30733 / 32607 MiB | 98% | **CWM 8B 训练中** |
| cuda:3 | RTX 5090 | 30913 / 32607 MiB | 94% | **CLS 8B seed123 训练中** |

### GPU 进程详情

| GPU | PID | 进程 | 启动时间 | 已运行 | 恢复自 | 最新 checkpoint |
|-----|-----|------|---------|--------|--------|----------------|
| cuda:2 | 266816 | `train_repo_cwm.py` (Qwen3-8B, seed=42) | 01:44:39 | ~1h54m | checkpoint-1600 | **checkpoint-1800** (03:09) |
| cuda:3 | 266449 | `train_repo_verifier.py` (Qwen3-8B, seed=123) | 01:43:50 | ~1h54m | checkpoint-3000 | **checkpoint-3400** (03:10) |

### 训练进度

- **CWM 8B** (`cwm_8b_restart.log`): 当前 epoch **2%** (180/9335), ~7.6 it/s
- **CLS 8B seed123** (`cls_8b_s123_ckpt2400_resume.log`): 当前 epoch **71%** (6653/9335), ~9.6 it/s

### Eval 结果（已完成）

**CWM v12 eval** — 完成于 02:13

| 指标 | 值 |
|------|-----|
| Accuracy | 58.04% (majority baseline 73.0%, gap -14.9pp) |
| F1 macro | 51.67% |
| fail F1 | 34.1% (P=29.6%, R=40.2%) |
| pass F1 | 69.2% (P=74.5%, R=64.7%) |
| Unparseable | 5255 / 9784 |
| 结果路径 | `/root/autodl-tmp/results/repo_cwm_v12_conda_eval/` |

**CWM seed123 eval** — 完成于 02:25

| 指标 | 值 |
|------|-----|
| Accuracy | 59.09% (majority baseline 73.0%, gap -13.9pp) |
| F1 macro | 43.43% |
| fail F1 | 13.7% (P=15.9%, R=12.0%) |
| pass F1 | 73.2% (P=70.1%, R=76.5%) |
| Unparseable | 6574 / 9784 |
| 结果路径 | `/root/autodl-tmp/results/repo_cwm_seed123_conda_eval/` |

### 关键观察

1. **cuda:0 和 cuda:1 完全空闲**，可用于新任务
2. 两个 8B 训练正常运行中；CLS seed123 当前 epoch 快结束（71%），CWM 刚进入新 epoch（2%）
3. 两个 CWM eval 均已完成，但**准确率都低于 majority baseline**（58%/59% vs 73%），且 unparseable 比例极高（53%/67%），说明模型输出格式问题严重
4. tmux 命令在 read-only 模式下被拦截，无法查看 session 列表和 pane 内容

---
