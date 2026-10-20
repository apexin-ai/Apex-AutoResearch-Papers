# fix repo level sample weight

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_repo-level-sample-weight_20260512T112716_result.json`
- **Structured JSON:** [`eab982af2c4c045cba83.json`](../../sessions/ea/eab982af2c4c045cba83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**CWM dry-run 也完成了！** 3 step 全部成功：
- Step 1: loss=0.6214
- Step 2: loss=0.6200
- Step 3: loss=0.4330

两个脚本都没有 KeyError，修复验证通过。

现在需要重启旧的崩溃训练进程（PID 34681, 34762），它们还在跑旧代码。但这些进程是由 tmux session 管理的，需要 kill 旧进程后重启。不过这超出了 bug 修复的范围——旧进程加载的是修复前的代码，需要重启才能用上新代码。

---

## 修复报告

**Root cause**: `DataCollatorForSeq2Seq` 内部调用 `tokenizer.pad()` 只处理标准 tokenizer 字段（`input_ids`、`attention_mask`、`labels`），`sample_weight` 列虽然在 Dataset 中存在且 `remove_unused_columns=False` 保留了它，但 collator 在 padding 时丢弃了它。`compute_loss` 从 collated batch 中 `pop("sample_weight")` 时触发 KeyError。

**修复内容**（两个文件完全相同的改法）：

1. **新增 `WeightedDataCollator` 类**（`train_repo_verifier.py:120`，`train_repo_cwm.py:118`）：
   - 在 `__call__` 中先从每个 feature dict 中 pop `sample_weight`
   - 调用底层 `DataCollatorForSeq2Seq` 做 padding
   - 将 `sample_weight` 作为 float tensor 加回 batch

2. **修改 collator 初始化**（`train_repo_verifier.py:234`，`train_repo_cwm.py:232`）：
   - `DataCollatorForSeq2Seq(...)` → `WeightedDataCollator(DataCollatorForSeq2Seq(...))`

**未修改**：class weighting 逻辑、hyperparameters、compute_loss 方法。

**Dry-run 结果**：两个脚本均在 GPU 上完成 3 step 训练，loss 正常下降，无任何 error。

**注意**：旧的训练进程（PID 34681, 34762）加载的是修复前的代码，需要 kill 并重启才能生效。

---
