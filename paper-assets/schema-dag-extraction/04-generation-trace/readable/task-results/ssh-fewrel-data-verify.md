# ssh fewrel data verify

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-data-verify_20260515T111910_result.json`
- **Structured JSON:** [`906860bb91200a461517.json`](../../sessions/90/906860bb91200a461517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。

---

## FewRel Readiness Checklist

### 1. 数据文件

| 检查项 | 状态 |
|--------|------|
| `data/fewrel/val_wiki.json` (3.5MB) | **PASS** |
| `data/fewrel/train_wiki.json` (14.3MB) | **PASS** |
| `data/fewrel_parquet/val.parquet` (1.2MB) | **PASS** |
| `data/fewrel_parquet/train.parquet` (4.8MB) | **PASS** |
| 数据格式 (tokens, h, t) | **PASS** — JSON 格式正确 |
| 脚本实际使用 parquet 而非 JSON | **PASS** — `fewrel_utils.py` 用 `pd.read_parquet()` |

### 2. 配置文件

| 检查项 | 状态 |
|--------|------|
| `configs/fewrel_relation_types.json` 存在 | **PASS** |
| 包含 80 个 relations | **PASS** — 80 个 PID→name 映射 |
| PID 格式匹配数据 (P177, P931...) | **PASS** |

### 3. MiniLM Embedding 资产

| 检查项 | 状态 |
|--------|------|
| `artifacts/fewrel_formal/relation_sim_matrix.pt` (29KB) | **PASS** — 今日 16:47 生成 |
| `artifacts/fewrel_formal/batch_config_exp1.json` (39KB) | **PASS** — exp1 含全部 7 个 count 级别 (1,4,8,16,32,64,80) |
| `artifacts/fewrel_pilot/relation_sim_matrix.pt` (29KB) | **PASS** — pilot 遗留 |
| 独立 FewRel MiniLM embeddings .pt | **N/A** — 不存在，但脚本会 CPU fallback 自动计算（80 个 relation name，秒级） |

### 4. run_fewrel_formal.py 参数兼容性

| 参数 | 默认值 | 文件存在？ |
|------|--------|-----------|
| `--model_path` | `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/` | **PASS** — 7 shards 完整 |
| `--data_path` | `data/fewrel_parquet/val.parquet` | **PASS** |
| `--types_file` | `configs/fewrel_relation_types.json` | **PASS** |
| `--embeddings_path` | None (CPU fallback) | **PASS** — 可接受 |
| `--output_dir` | `artifacts/fewrel_formal` | **PASS** |
| `--n_samples` | 1000 | **PASS** — 合理 |

注意：`--n_batches_exp1` / `--n_batches_exp2` 不是 CLI 参数，硬编码为 `EXP1_RANDOM_PER_COUNT=5`, `EXP2_RANDOM_PER_COUNT=25`。`--sim_matrix_path` 不存在于脚本中。

### 5. 已有 preprocess 产出

exp1 的 `batch_config_exp1.json` + `relation_sim_matrix.pt` 已存在（来自先前运行）。可以直接 `--stage extract --mode exp1` 跳过 preprocess。

exp2 的 `batch_config_exp2.json` **尚未生成**，需先运行 `--stage preprocess --mode exp2`。

### 结论

**exp1: READY** — 数据、配置、模型、preprocess 产出全部就绪，可直接 `--stage extract --mode exp1`。

**exp2: 差一步** — 需先运行 preprocess 生成 `batch_config_exp2.json`（CPU 操作，无需 GPU）。

---
