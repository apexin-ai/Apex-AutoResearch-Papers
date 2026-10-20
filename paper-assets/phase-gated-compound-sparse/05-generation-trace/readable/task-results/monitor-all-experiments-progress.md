# monitor all experiments progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_all-experiments-progress_20260514T144222_result.json`
- **Structured JSON:** [`4707e9889111211beb89.json`](../../sessions/47/4707e9889111211beb89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. c3_llama — RUNNING (刚启动)

| 项 | 值 |
|---|---|
| 进程 | PID 137204 alive, 启动 22:36:45 (~8 min ago) |
| GPU | cuda:2+3, importance (GPU2) + random (GPU3) 并行 |
| 当前 | 第 1/4 组 sparsity (s015), 两 GPU 都在 ~[11/50] |
| 速率 | ~0.7 min/problem → 每组 ~36 min |
| 预计总时长 | 4 组 × 36 min ≈ 2.5 小时 → ~01:00 完成 |
| 输出目录 | `profiling_output_c3_llama_importance_s000`, `profiling_output_c3_llama_random_s000`, `profiling_output_c3_llama_dryrun` |

**⚠️ 问题：`bc` 未安装，sparsity 计算失败**
脚本 `run_c3_llama_full.sh` 报 `bc: command not found`，导致所有 sparsity 目录名都是 `s000` 而非 `s015/s020/s025/s030`。虽然不影响实际运行（sparsity 值可能通过 Python 参数正确传入），但**输出目录会互相覆盖** — 4 组 sparsity 的结果都写入同一对 `s000` 目录。需要确认脚本逻辑。

---

### 2. c2_n500_deepseek — RUNNING (1 小时)

| GPU | 方法 | 当前 condition | 进度 | 速率 | 预计 |
|-----|------|---------------|------|------|------|
| GPU0 | importance | s015 (1/4) | 105/500 (21%) | ~0.6 min/prob | 本 condition ~4 min 后的 ~5h；全部 4 conditions ~19h (明天 ~17:45) |
| GPU1 | random | s015 (1/4) | 127/500 (25%) | ~0.5 min/prob | 本 condition ~3.1h；全部 4 conditions ~15.6h (明天 ~14:20) |

模型：DeepSeek-R1-Distill-Qwen-7B，n=500，tmux sessions `c2_n500_gpu0/gpu1` (tmux 无法通过 read_only 验证)。所有输出目录目前为空（结果在一个 condition 完成后才写入 JSON）。

---

### 3. c2_qw_n500 — RUNNING (51 min)，有并发问题

| GPU | 方法 | s015 进度 | s020 进度 |
|-----|------|----------|----------|
| GPU2 | importance | 103/500 | 1/500 (几乎停滞) |
| GPU3 | random | 107/500 | 1/500 (几乎停滞) |

模型：Qwen2.5-7B-Instruct，PID 131864 + 132002 (100% CPU, 51 min)。

**⚠️ 问题：s015 和 s020 同时运行在同一 GPU 上**
Wrapper 脚本在 s015 完成前就启动了 s020（s015 只跑了 9 个问题就 fork 出 s020）。每个 GPU 上同时有两个模型。s020 进程 44 分钟只处理了 1 个 problem，基本被 s015 进程阻塞。按当前速度（s015 ~0.5 min/prob），s015 还需 ~3.3h 完成，之后 s020 才能正常推进。总完成时间难以准确估计，但可能 **20+ 小时**。

---

### 总览

| 实验 | 状态 | 进度 | 预计完成 | 问题 |
|------|------|------|---------|------|
| c3_llama | 🟢 Running | ~22% of condition 1/4 | ~01:00 今晚 | `bc` 未装，目录名 s000 可能导致覆盖 |
| c2_n500_deepseek | 🟢 Running | condition 1/4, 21-25% | 明天 14:00-18:00 | 无 |
| c2_qw_n500 | 🟡 Running (degraded) | condition 1/4, 20% | 20+ 小时 | s015/s020 并发竞争 GPU |

---
