# diag bjb2 server status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-server-status_20260518T114144_result.json`
- **Structured JSON:** [`9cdd7dc3393ee571c082.json`](../../sessions/9c/9cdd7dc3393ee571c082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告 — bjb2-18868

### 1. GPU 状态

| GPU | 型号 | 显存使用 | 利用率 | 温度 |
|-----|------|----------|--------|------|
| 0 | RTX 5090 32GB | 0 / 32607 MiB | 0% | 27°C |
| 1 | RTX 5090 32GB | 0 / 32607 MiB | 0% | 27°C |
| 2 | RTX 5090 32GB | 0 / 32607 MiB | 0% | 27°C |
| 3 | RTX 5090 32GB | 0 / 32607 MiB | 0% | 30°C |

**无运行中的 GPU 进程。** 全部空闲。

### 2. 磁盘占用

| 路径 | 大小 |
|------|------|
| 项目总计 | 831M |
| data/ | 307M |
| results/ | 1.6M |
| **根分区** | **9.5G / 30G (32%)** |

磁盘充裕，无压力。

### 3. 实验完成状态

**exp_049 (Pythia t=0.5)** — ✅ 完成
- 生成数据: `pythia-2.8b-t05/generations_shard0.jsonl` (5.4MB)
- 特征提取: `features_pythia-2.8b-t05.csv` (639KB)

**exp_050 (t=0.9)** — ✅ 生成+特征提取完成
- `pythia-2.8b-t09/generations_shard0.jsonl` (4.8MB) → `features_pythia-2.8b-t09.csv` (615KB, 4536 samples)
- `qwen3-1.7b-t09/generations_shard0.jsonl` (5.1MB) → `features_qwen3-1.7b-t09.csv` (623KB, 4558 samples)

**exp_051 (independent seed)** — ✅ 完成
- 结果在 `results/independent_seed_results.json`（无独立子目录）
- 平均 binary F1 = **0.680**, 与共享种子 delta = **-0.014**（几乎无差异）

**exp_054 (instruct Llama)** — ✅ 完成
- `results/exp054_instruct_llama_eval.json`, binary F1 = 0.838, 3-class F1 = 0.544

### 4. Tmux 会话

4 个会话存在，**全部已执行完毕**（均回到 shell 提示符）：

| 会话 | 状态 | 完成内容 |
|------|------|----------|
| `feat_t05` | ✅ idle | Pythia t=0.9 特征提取完成 |
| `feat_qwen_t09` | ✅ idle | Qwen t=0.9 特征提取完成 |
| `exp054_resume` | ✅ idle | Llama instruct 评估完成 |
| `tc_phase3` | ✅ idle | Qwen t=0.9 特征提取完成 |

可安全清理所有 tmux 会话。

### 5. Qwen3-1.7b t=0.9 评估结果

`temp_curve_binary_logo.json` 已有评估：

| 模型 | 温度 | LOGO Binary F1 | 95% CI |
|------|------|----------------|--------|
| qwen3-1.7b | 0.5 | 0.751 | [0.735, 0.766] |
| qwen3-1.7b | 0.7 | 0.751 | [0.735, 0.766] |
| qwen3-1.7b | **0.9** | **0.566** | [0.550, 0.583] |
| qwen3-1.7b | 1.0 | 0.367 | [0.353, 0.381] |

**Spearman ρ**: `temp_curve_binary_logo.json` 中未包含 Spearman 指标。结果文件中没有找到专门针对 t=0.9 条件的 Spearman ρ 评估。如需此指标，需额外运行评估脚本。

---
