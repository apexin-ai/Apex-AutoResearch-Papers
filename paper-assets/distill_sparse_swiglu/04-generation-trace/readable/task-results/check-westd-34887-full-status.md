# check westd 34887 full status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_34887_full_status_20260520T124435_result.json`
- **Structured JSON:** [`47e9d948da3604be14c2.json`](../../sessions/47/47e9d948da3604be14c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34887 状态汇总

### 1. GPU 状态
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| cuda:0 | 54025 MiB | 97887 MiB | 82% |
| cuda:1 | 3 MiB | 97887 MiB | 0% |

### 2. Python 进程
- **PID 212478** — `python -u src/train.py` (Mistral KL30 s123)，CPU 100%，运行中，占用 cuda:0

### 3. tmux sessions
tmux 不在 ssh_read_only 白名单内无法查询。但从 ps 输出看，无 tmux 进程。训练通过 nohup 启动，符合 C002 约束。

### 4. 40% global eval v2（PID 205789）— **已完成**
PID 不存在。结果已保存到 `results/benchmark/kl_sparsity40_s42_global_eval_v2/results.json`：

| Task | 指标 | 值 |
|------|------|----|
| wikitext2 | PPL | **10.1361** |
| arc_challenge | acc / acc_norm | 0.3729 / 0.3951 |
| winogrande | acc | 0.6748 |
| mmlu | acc | 0.3947 |
| gsm8k | exact_match | 0.0660 |
| hellaswag | acc / acc_norm | 0.4883 / 0.6779 |
| piqa | acc / acc_norm | 0.7144 / 0.7269 |

配置：LLaMA-3.1-8B，sparsity=0.4，allocation=global_topk，完成时间 2026-05-20 18:53:29。

### 5. Mistral KL30 s123（PID 212471）— **训练中**
PID 存在，当前进度 **Step 740/1000**（74%）。checkpoint 目录已创建但尚无文件。

训练指标趋势（最近几步）：
- loss: ~0.085–0.110，稳步下降
- sparsity: 0.285–0.297，围绕目标 0.30
- constraint: 基本为 0（偶尔微小波动后 lambda 自适应调整）
- tau: 0.334（持续退火中）

训练完成后会自动启动 benchmark_eval。预计剩余 ~260 步训练 + eval 时间。

### 6. 磁盘使用
| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 19G | 12G | 61% |
| /root/autodl-tmp | 250G | 70G | 181G | 28% |

---
