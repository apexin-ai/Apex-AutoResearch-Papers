# code disable quality filter

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_disable_quality_filter_20260513T032329_result.json`
- **Structured JSON:** [`1abd8396011e8bd6060e.json`](../../sessions/1a/1abd8396011e8bd6060e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。以下是修改总结：

---

## 1. Quality filter 原始实现逻辑

`diversity_selection.py:quality_filter()` — 用 student model 计算 reference set 所有样本的 PPL，取 90th percentile 作为阈值，再计算 candidate 的 PPL，保留 `ppl ≤ threshold` 的样本。在 self-iterate 模式下，student 对自身"典型输出"给低 PPL，对稀有/多样内容给高 PPL，导致 quality filter 系统性移除多样性样本。

## 2. 修改的文件

**`diversity_selection.py`**（4 处）:
- `select_data()` 签名新增 `no_quality_filter=False` 参数
- 质量过滤后计算 `qf_info` 诊断字典（`would_remove_set`, `ppl_threshold`）
- `no_quality_filter=True` 时 `quality_mask` 设为全 True（不实际移除），否则行为不变
- 返回值从 `selected` 改为 `(selected, qf_info)`

**`run_mvp.py`**（6 处）:
- `parse_args()` 新增 `--no_quality_filter` 参数
- `run_selection()` uncurated 分支返回 `(indices, qf_info_nan)` 
- `run_selection()` 的 `select_data` 调用传入 `no_quality_filter=args.no_quality_filter`，返回 tuple
- main loop 解包 `selected_indices, qf_info = run_selection(...)`
- selection_diag if 分支后新增 qf_diag 计算（利用已有的 `all_rare_scores`）
- else 分支（uncurated）qf_diag 全设 NaN
- `metrics.update(qf_diag)` 写入 metrics.json

**`run_phase2.sh`**（1 处）:
- COMMON_ARGS 末尾加 `--no_quality_filter`

## 3. 诊断指标计算方式

每代 metrics.json 新增 3 个字段：
- **`qf_would_remove_count`**：quality filter 仍然运行，计算 PPL > 90th percentile 的样本数，但不实际移除
- **`qf_removed_rare_ngram_mean`**：这些 "会被移除" 样本的 rare n-gram ratio 均值（复用 main loop 已有的 `all_rare_scores`）
- **`qf_kept_rare_ngram_mean`**：剩余样本的 rare n-gram ratio 均值

uncurated 方法不走 quality filter，三个字段均为 NaN。

## 4. 验证结果

- `py_compile diversity_selection.py` ✅
- `py_compile run_mvp.py` ✅
- `python run_mvp.py --help` 显示 `--no_quality_filter` ✅
- `run_phase2.sh` 包含 `--no_quality_filter` ✅

## 5. 更新后的 run_phase2.sh 启动命令

```bash
bash /root/div_cal_verify/run_phase2.sh 0   # GPU 0
```

COMMON_ARGS 现在包含 `--self_iterate --no_quality_filter`，3 个方法（uncurated / rgds / external_only）均使用。

---
