# ops session16 gpu diag

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_session16_gpu_diag_20260516T040904_result.json`
- **Structured JSON:** [`70dd9add9e77dac84183.json`](../../sessions/70/70dd9add9e77dac84183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. c4_v2 Think Validation 结果

**PID 308765 已结束。** 结果文件已生成：

| 指标 | DS (DeepSeek) | QW (Qwen) |
|------|--------------|------------|
| κ (adaptive) | **0.880** | N/A (无 think tags) |
| κ (phase_low / high) | 0.513 / 0.521 | — |
| thinking_in_low | 0.816 (pooled 0.578) | — |
| answer_in_high | 0.655 (pooled 0.627) | — |
| temporal_ordering (MATH-500) | 0.576 | 0.479 |
| pct_positive (MATH-500) | — | 98.0% |
| 样本数 | 48 problems, 32055 tokens | 50 checked |

**Success criteria: ALL MET** (κ≥0.8 ✓, thinking_in_low≥0.5 ✓, answer_in_high≥0.5 ✓)

QW 没有 `&lt;think>` 标签，只做了 phase temporal ordering 分析（0.479，接近随机）。

---

## 2. GPU 全局状态

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 24.8 / 97.9 GB | 76% |
| 1 | 15.3 / 97.9 GB | 68% |
| 2 | 73.3 / 97.9 GB | 71% |
| 3 | 73.3 / 97.9 GB | 75% |

型号：NVIDIA RTX PRO 6000 Blackwell Server Edition × 4

---

## 3. c8_llama_n250_fixed 进度

- **PID 310712** (主调度 bash): 运行中，elapsed 48:45，使用 GPU 2+3
- **PID 315052** (GPU 0 单独跑 s025 importance): 运行中，elapsed 4:39，当前 **[8/250]**
- 已完成条件目录：`s015/`, `s020/`, `s025/` 都已创建，但 **s015 和 s020 的 profiling_results.json 为空（0 行）**，s025 目录刚建还没输出
- 主日志显示 Round 1 已启动（s015 on GPU2, s020 on GPU3），11:20 开始

---

## 4. c10 s020/s025 进度

- tmux session `c10-lang-s020-s025`: **ALIVE**
- 无 `results_c10_lang_s020_s025.json` 输出文件（只有之前的 `results_c10_lang_cpu.json`）
- 日志显示当前在 **[Problem 18/50]**，同时跑 importance_s020 和 importance_s025 两个稀疏度
- 用的是 Qwen 模型（pad_token_id=151643）

---
