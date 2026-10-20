# diag olmo t05 dedup and monitor

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo-t05-dedup-and-monitor_20260518T192856_result.json`
- **Structured JSON:** [`15fde631308a894b71b8.json`](../../sessions/15/15fde631308a894b71b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`temp_olmo-2-1b_t0.5_eval.json` 不存在于服务器上，已经只剩 `t05` 和 `t09` 两份文件。可能之前已被删除。

---

## 汇报

### 1. 两份文件差异分析

| 字段 | `t05` (F1=0.783) | `t0.5` (F1=0.984) |
|---|---|---|
| 字段命名 | `"temp": 0.5` | `"temperature": 0.5` |
| n_seeds/n_train | 无此字段 | 995 / 3886 |
| binary_n_test | **3863** | **972** |
| three_class_n_test | **4858** | **972** |
| 来源 | monitor pipeline (`build_eval_script`) | 其他脚本 |

### 2. 哪份是 LOGO，哪份有 bug

**`t05` (F1=0.783) = 正确，LOGO 评估。**
- 训练集：7 个其他 generator 在 t=0.7 的基准数据
- 测试集：olmo t=0.5 全部数据（binary 排除 depth=0 → 3863 样本，three_class 保留全部 → 4858 样本）
- 数据分布确认：depth 0=995, 1=988, 2=970, 3=957, 4=948，总 4858，995 seeds

**`t0.5` (F1=0.984) = 错误，within-model 80/20 随机 split。** Bug 有两个：
1. **Seed 级数据泄露**：n_train=3886 + n_test=972 = 4858，是单模型内 80/20 随机 split。同一 seed 不同 depth 的样本同时出现在训练集和测试集，分类器学到 seed 特有模式而非 depth 区分特征
2. **Binary 任务未排除 depth=0**：binary_n_test = three_class_n_test = 972，说明 depth=0 没被排除，binary 任务定义也有问题

### 3. 文件状态

`temp_olmo-2-1b_t0.5_eval.json` 服务器上已不存在（可能此前已删除）。仅剩正确的 `temp_olmo-2-1b_t05_eval.json`。

### 4. Qwen t=0.9 进度

- 3912 行 JSONL
- **866 / 990 unique seeds（87.5%）**
- 距离触发 pipeline 还差 ~124 seeds

---
