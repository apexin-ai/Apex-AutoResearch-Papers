# code phase2 experiment framework

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_experiment_framework_20260512T220705_result.json`
- **Structured JSON:** [`712e05c6df59a7a24122.json`](../../sessions/71/712e05c6df59a7a24122.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇报

### 1. 核心接口设计

| 函数 | 职责 |
|------|------|
| `ExperimentConfig` | dataclass，封装单实验全部参数，`to_run_circus_config()` 转换为 `run_circus.run_pipeline()` 入参 |
| `load_experiment_matrix(yaml)` | 从 YAML 加载实验矩阵，defaults 与每个实验合并 |
| `run_single_experiment(exp)` | 调用 `run_circus.run_pipeline()`，带缓存检查和断点续跑 |
| `run_analysis_for_experiment(exp)` | 实验完成后调用 `analyze_mvp_results.run_analysis()` |
| `run_batch(experiments, names, max_priority)` | 按 priority 排序批量执行，输出 `phase2_batch_summary.json` |
| `check_cache(exp)` / `load_cached_scores()` / `save_cached_scores()` | 缓存管理，key 绑定 `CANONICAL_VERSION` + 超参哈希 |

### 2. 实验矩阵

**4 模型 × 4 任务 = 16 个实验**

| 模型 | 任务 | 方法 | Backend |
|------|------|------|---------|
| GPT-2 Small | IOI, Greater-Than, Docstring | EAP-IG + EP + ACDC | TransformerLens |
| Qwen-2.5 0.5B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |
| Gemma-2 2B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |
| Llama-3.1 8B | IOI, Greater-Than, Docstring, IOI-variant | EAP-IG + EP + IFR | HuggingFace |

### 3. Priority 分布

| Priority | 数量 | 说明 |
|----------|------|------|
| P1 | **1** | `gpt2_ioi`（MVP 已在跑） |
| P2 | **5** | GPT-2 另外 2 task + Qwen-2.5 的 3 task |
| P3 | **10** | Gemma-2 全部 4 task + Llama-3.1 全部 4 task + Qwen IOI-variant |

### 4. 预估全量运行时间

| 模型 | 单 task 耗时 | task 数 | 小计 |
|------|-------------|---------|------|
| GPT-2 Small | ~20min | 3 | ~60min |
| Qwen-2.5 0.5B | ~25min | 4 | ~100min |
| Gemma-2 2B | ~65min | 4 | ~260min |
| Llama-3.1 8B | ~150min | 4 | ~600min |
| **合计** | | **16** | **~1020min (~17h)** |

P1+P2 子集（6 个实验）约 **2.5h**，可在 MVP 通过后当天完成。P3 的 10 个实验约 **14.5h**，需安排过夜跑。Llama-3.1 8B 需 >=24GB VRAM，config 中已降低 `num_samples=20` 和 `edge_pruning_epochs=60` 控制显存。

---
