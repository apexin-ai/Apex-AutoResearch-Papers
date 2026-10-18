# ssh code preflight

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_code-preflight_20260514T173030_result.json`
- **Structured JSON:** [`a3808493158ab98d2e1c.json`](../../sessions/a3/a3808493158ab98d2e1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现关键问题：本地 parquet 的 `ner_tags` 是粗粒度（9类），而 `fine_ner_tags` 才是细粒度（66+1类）。代码 `load_few_nerd` 使用的是 `ner_tags`。需要确认从 HF 加载时该字段的实际内容。

## 预检结果汇总

### 检查 1: Syntax & Import — **PASS**
全部 8 个 .py 文件语法正确，5 个核心模块 import 正常：
```
analyze_results.py, compute_bcs.py, compute_type_embeddings.py, evaluate.py,
few_nerd_utils.py, run_experiment.py, run_extraction.py, select_type_batches.py
```

### 检查 2: Few-NERD 数据加载 — **FAIL**
- `load_few_nerd()` 硬编码 `load_dataset("DFKI-SLT/few-nerd", "supervised", ...)` 从 HF Hub 加载
- HF Hub 网络不通（AutoDL 环境），且无本地 HF 缓存
- 本地已有 parquet 文件：`/root/schema-dag-extraction/data/parquet/{train,test,validation}.parquet`（test 有 37648 行）
- **额外发现**：本地 parquet 中 `ner_tags` 是粗粒度 9 类（O/art/building/...），`fine_ner_tags` 才是细粒度 67 类（O + 66 fine types）。当前代码使用 `ner_tags`，改用本地 parquet 后必须切换到 `fine_ner_tags`

**修复建议**：修改 `few_nerd_utils.py` 的 `load_few_nerd`，优先从本地 parquet 加载，使用 `fine_ner_tags` 列：
```python
ds = load_dataset('parquet', data_files=f'{data_dir}/{split}.parquet', split='train')
tag_names = ds.features["fine_ner_tags"].feature.names
# 遍历时用 example["fine_ner_tags"] 替代 example["ner_tags"]
```

### 检查 3: Type definitions — **PASS**
66 个 type，所有 definition 长度 > 10 字符。

### 检查 4: Type stats — **PASS**
- 66 types，96902 instances，无 insufficient types
- type definitions 和 type stats 的 type 集合完全匹配

### 检查 5: CLI — **PASS**
`run_experiment.py --help` 正常输出，参数包括 `--mode {dry_run,exp1,exp2}`、`--embeddings_path`、`--types_file` 等。

### 检查 6: Solo baseline (count=1) 逻辑 — **PASS**
`run_experiment.py` 第 83-85 行：
```python
if count == 1:
    solo_batches = [{"types": [t], "bcs": 0.0} for t in active_types]
    batch_config["count_1"] = {"random": solo_batches}
```
每个 active type 单独一个 batch，BCS=0.0，符合设计。

### 检查 7: ΔF1 逻辑 — **PASS**
`analyze_results.py` 逻辑正确：
1. 从 exp1 `count_1` 结果提取 `per_type_f1` → `solo_f1` 字典
2. `delta_f1 = solo_F1[t] - batch_F1[t]`（正值 = batching 导致退化）
3. 当所有 entry 都有 `delta_f1` 时，用 Pearson r(BCS, mean_Δ)；否则 fallback 到 r(BCS, raw_F1)

---

**唯一阻塞项**：检查 2 — `few_nerd_utils.py` 需要修改为从本地 parquet 加载并使用 `fine_ner_tags`。是否现在修复？

---
