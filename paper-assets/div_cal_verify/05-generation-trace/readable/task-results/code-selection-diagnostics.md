# code selection diagnostics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_selection_diagnostics_20260513T031937_result.json`
- **Structured JSON:** [`fcc7ebf4bd3e3a4eca4a.json`](../../sessions/fc/fcc7ebf4bd3e3a4eca4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

### 修改的文件

**1. `evaluate.py` — 末尾新增函数 `compute_rare_ngram_ratio_per_sample`**
- 复用 `compute_rare_ngram_survival` 的 rare n-gram 集合构建逻辑（参考语料 3-gram 频次 ≤ 10th percentile）
- 对每个样本计算其 n-gram 中 rare n-gram 的占比（`rare_count / total_ngrams`），返回 per-sample score 列表

**2. `run_mvp.py` — 3 处修改**
- **L13**: 新增 `import numpy as np`
- **L28**: import 中新增 `compute_rare_ngram_ratio_per_sample`
- **L262-289**: 在 selection 完成后（`torch.save(selected_indices)` 之后、训练开始之前），新增诊断代码块：
  - `method != "uncurated"` 且确实有 rejection 时：decode 参考语料和合成样本为文本，调用 `compute_rare_ngram_ratio_per_sample` 计算每个样本的 rare n-gram ratio，按 selected/rejected 分组取均值，计算比值
  - `uncurated` 方法或无 rejection 时：三个字段设为 NaN
- **L312**: `metrics.update(selection_diag)` 将三个诊断字段写入 metrics.json

### 验证结果
- `py_compile run_mvp.py` — SYNTAX OK
- `py_compile evaluate.py` — SYNTAX OK
- `python3 run_mvp.py --help` — 正常输出

### 注意事项
- `json.dump` 对 `float("nan")` 会输出 `NaN`（非标准 JSON），但 Python `json.load` 可以读回。如果下游有严格 JSON parser，需要后处理为 `null`。现有代码已在用同样方式处理其他指标，保持一致。

---
