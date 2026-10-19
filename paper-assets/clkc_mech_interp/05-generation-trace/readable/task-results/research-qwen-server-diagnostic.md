# research qwen server diagnostic

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen-server-diagnostic_20260524T112908_result.json`
- **Structured JSON:** [`45ea7a2d80aaccc7095b.json`](../../sessions/45/45ea7a2d80aaccc7095b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. Qwen 模型状态

| 路径 | 大小 | 状态 |
|------|------|------|
| `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/` | **1.7MB** | **未完成** — 只有 config.json、tokenizer 等元数据文件，**没有 model.safetensors 权重文件** |

对比：Llama-3.1-8B-Instruct 占 15GB，Gemma-2-9b-it 占 18GB。Qwen2.5-7B-Instruct 完整应约 15GB。

**其他已下载模型：**
- `Meta-Llama-3.1-8B-Instruct` — 15GB ✓
- `gemma-2-9b-it` (AI-ModelScope) — 18GB ✓

### 2. Qwen 数据

**不存在。** `data/` 下只有三个目录：`llama31`、`gemma2`、`gemma2_v2`。没有 `qwen*` 目录。

### 3. 已有数据概览

| 模型 | 文件 | 行数 | 大小 | conflict | no_conflict |
|------|------|------|------|----------|-------------|
| llama31 | train_verified | 1200 | 979KB | — | — |
| llama31 | test_verified | 400 | 325KB | 201 | 199 |
| llama31 | activations.pt | — | 400MB | — | — |
| gemma2 | train_verified | 528 | 392KB | — | — |
| gemma2 | test_verified | 176 | 131KB | 88 | 88 |
| gemma2 | activations.pt | — | 202MB | — | — |
| gemma2_v2 | train_verified | 1026 | 764KB | — | — |
| gemma2_v2 | test_verified | 342 | 256KB | 171 | 171 |
| gemma2_v2 | activations.pt | — | 393MB | — | — |

数据均已完成 steering 实验（每个目录有多个 `steering_results_L*.json`）。

### 4. 可用脚本

关键脚本（`/root/clkc_mech_interp/src/`）：

- **数据准备**: `prepare_gemma_data.py`, `prepare_gemma_data_v2.py`, `prepare_xnli.py`
- **验证**: `verify_parametric_knowledge.py`
- **Activations**: `collect_activations.py`
- **Steering**: `steering_experiment.py`
- **Probe**: `train_probe.py`, `train_probe_fast.py`, `train_mlp_probe.py`
- **分析**: `bootstrap_*.py`, `compute_cka.py`, `cross_task_transfer*.py`, `token_overlap*.py`

**注意：没有 `prepare_qwen_data.py`** — 需要新建或改编现有脚本。

### 5. 服务器环境

| 项目 | 值 |
|------|-----|
| GPU | **NVIDIA RTX PRO 6000 Blackwell Server Edition** |
| 显存 | **97,887 MiB (~96GB)** |
| GPU 占用 | **空闲**（无进程运行） |

### 总结

- **Qwen2.5-7B-Instruct 模型下载未完成**，只拉了元数据，需要重新下载权重
- **没有任何 Qwen 数据**，需要准备 prepare_qwen_data.py 脚本并跑完整 pipeline
- GPU 空闲，96GB 显存足够运行 Qwen-7B

---
