# recon seed expansion

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_seed-expansion_20260521T210855_result.json`
- **Structured JSON:** [`68b8617b6e2ffa8d5685.json`](../../sessions/68/68b8617b6e2ffa8d5685.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 服务器状态汇总

### 1. GPU
- **1 块 GPU**：NVIDIA RTX PRO 6000 Blackwell Server Edition, 98GB VRAM
- 当前 **0 MiB 占用**，完全空闲
- **无 cuda:1**（单卡机器）

### 2. 磁盘空间
| 分区 | 总容量 | 已用 | 可用 | 使用率 |
|------|--------|------|------|--------|
| `/root/autodl-tmp/` | 250G | 223G | **28G** | 90% |
| `/root/` | 30G | 18G | 13G | 59% |

**磁盘紧张**，数据盘只剩 28G。每个 Qwen3-4B 训练实验约 16-48GB，最多跑 1 个实验需要先清理空间。

### 3. Exec-only 已有 seeds（Qwen3-4B, 主线实验）
从 eval 结果和 output 目录推断：
- **s42** — eval 存在 (`eval_sta_plan001_exec_only_s42.json`)，checkpoint 目录已清理
- **s43** — eval 存在 (`eval_sta_plan001_exec_only_s43_r4.json`)，checkpoint 目录已清理
- **s44** — eval 存在 + checkpoint 目录保留 (`plan001_exec_only_s44_1000_r2`)
- **s45** — eval 存在 (`eval_sta_sweep_exec_only_s45.json`)，checkpoint 目录已清理
- **s46** — eval 存在 (`eval_sta_sweep_exec_only_s46.json`)，checkpoint 目录已清理

**已有 seeds: 42, 43, 44, 45, 46**（共 5 个）

### 4. ISR β=0.1 已有 seeds（Qwen3-4B, 主线实验）
- **d134 系列 (4B, β=0.1)**: s47, s48, s49, s50, s51（目录存在，每个约 16M = checkpoint 已清理只剩 log）
- 另有 1.7B 和 8B 的 ISR 实验（不同模型规模，非主线）
- **sweeps**: sweep_isr_b005 (β=0.05, 不是 β=0.1) s43, s44

**ISR β=0.1 (4B) 已有 seeds: 47, 48, 49, 50, 51**（共 5 个，都在 d134 批次里）

### 5. 训练/eval 脚本
- `train_grpo.py` — 存在 (28,971 bytes, 今天更新)
- `eval_sta.py` — 存在 (12,190 bytes, 今天更新)
- `classify_h7.py` — 存在

**全部就绪。**

### 6. Exec-only 标准配置 (`grpo_exec_only.yaml`)
```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: execution_only
num_steps: 100          # ← 注意：基础版只 100 步
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
seed: 42
solver: prover9
```

更新版的 `sweep_exec_only_s46.yaml` 用 **500 步**, `batch_size: 2`, `save_total_limit: 1`。

### 7. Qwen3-8B 模型
- **已下载**：`/root/autodl-tmp/models/Qwen3-8B/config.json` 存在
- HF cache 中无（直接下载到 models 目录）

### 8. 当前运行进程
- **无训练进程在跑**（无 `train_grpo` 或 `python.*grpo`）
- 有一个 `d134-pipeline` 的 tmux session 残留（仅跑清理脚本的 sleep 循环，无实际计算）
- 系统服务：supervisord, sshd, tensorboard, jupyter, autopanel

---

**关键约束**：磁盘只剩 28G，新实验前需要清理旧 checkpoint 目录或大文件。GPU 完全空闲可以立即开始训练。

---
