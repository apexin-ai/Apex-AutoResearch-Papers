# exp bjb2 feature extract parallel

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bjb2-feature-extract-parallel_20260518T060151_result.json`
- **Structured JSON:** [`0182226c86a812e28a50.json`](../../sessions/01/0182226c86a812e28a50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总报告：

---

## 服务器状态报告

### nvidia-smi（初始 → 最终）

| GPU | 初始状态 | 最终状态 | 任务 |
|-----|---------|---------|------|
| **cuda:0** | 3977MiB, 42% | 3977MiB, 43% | `exp054_resume` — Llama-3.2-3B-Instruct 生成 (415/995 seeds), PID 2067 |
| **cuda:1** | 空闲 | **2485MiB, 64%** | `feat_t05` — Pythia-2.8b t=0.5 特征提取 → 完成后自动接 t=0.9, PID 4306 |
| **cuda:2** | 6923MiB, 64% | 6923MiB, 64% | `tc_phase3` — 生成任务 (525/996 seeds), PID 3103 |
| **cuda:3** | 空闲 | **623MiB, 启动中** | `feat_qwen_t09` — Qwen3-1.7b t=0.9 特征提取, PID 4405 |

### 模型权重
- **Pythia-410M**: `/root/autodl-tmp/models/pythia-410m/...`, model.safetensors = **870MB** ✓

### 温度曲线数据

| 数据集 | 行数 | 特征提取状态 |
|--------|------|------------|
| pythia-2.8b-t05 | 4708 | **启动中** (cuda:1) |
| pythia-2.8b-t09 | 4536 | 排队中 (cuda:1, 串行在 t05 后) |
| qwen3-1.7b-t05 | **不存在** | — |
| qwen3-1.7b-t09 | 2398 | **启动中** (cuda:3) |

### tmux Sessions
- `exp054_resume` — GPU 0, Llama 生成
- `tc_phase3` — GPU 2, 生成任务
- `feat_t05` — GPU 1, Pythia t=0.5 → t=0.9 特征提取（新建）
- `feat_qwen_t09` — GPU 3, Qwen t=0.9 特征提取（新建）

**注意**: `qwen3-1.7b-t05` 数据目录不存在，已改为提取 `qwen3-1.7b-t09`。如需 t=0.5 数据，需先跑生成。

---
