# ops verify logo results consistency

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-logo-results-consistency_20260516T125816_result.json`
- **Structured JSON:** [`620e5b8307552e0ba15b.json`](../../sessions/62/620e5b8307552e0ba15b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the complete analysis:

---

## 验证报告

### 1. 文件列表 + 时间戳

| 文件 | 修改时间 | 大小 |
|------|----------|------|
| `8gen_logo_unfiltered.json` | May 16 20:42:35 | 2025B |
| `8gen_logo_results_BUGGY_DO_NOT_USE.json` (原名 `8gen_logo_results.json`) | May 16 20:51:34 | 2869B |

注意：`8gen_logo_results.json` 已被重命名为 `8gen_logo_results_BUGGY_DO_NOT_USE.json`（rename 发生在 21:00:08）。

### 2. 两文件中的关键指标

| 指标 | `8gen_logo_unfiltered.json` | `8gen_logo_results_BUGGY` |
|------|-----|-----|
| Overall binary F1 | **0.6944** | 0.6851 |
| Mistral binary F1 | **0.6327** | 0.4876 |
| Overall 3-class F1 | 0.762 | 0.7638 |
| n_samples (total) | 37058 (3class) | 34131 |

### 3. tail_decay 值的实际量级

当前磁盘上所有特征文件中的 tail_decay 均为**修正后的格式**：

- Mistral: tail_decay ≈ **-0.0023** (负数，log-prob slope)
- Llama: tail_decay ≈ **-0.0024** (负数，log-prob slope)  
- Pythia-2.8b (6-gen baseline): tail_decay ≈ **-0.0023** (负数，log-prob slope)

全部一致，均为修正后的公式（slope of sorted avg log-probs, ranks 100-1000）。旧公式（NLL proportion）的特征为正数、量级 0.05~0.9，磁盘上不存在。

### 4. 结论

**`8gen_logo_unfiltered.json` 是修复后的正确结果**（binary F1=0.694, Mistral=0.633）。

原因：
- 由 `fix_tail_decay_and_eval.py`（20:41:29 编写）产出，该脚本**重新提取**了特征并立即评估
- 样本数 37058 = 27529 (features_all_models.csv) + 9529 (新JSONL)，与当前文件行数完全一致
- 生成时间紧跟 JSONL 特征文件更新（20:41-42）

**`8gen_logo_results_BUGGY` 是有问题的结果**（binary F1=0.685, Mistral=0.488）：
- Birth time 20:18:35，早于特征修复（20:41），首次运行用的是修复前的旧 JSONL（仅 6602 行 → 总行数 34131 vs 37058）
- Mistral F1 异常低（0.488）正是因为旧 JSONL 中 tail_decay 用了 NLL proportion 格式，与其他 6 generator 的 slope 格式不一致，导致特征空间错配
- 已被标记为 BUGGY 并重命名

**Director 此前汇报的 binary F1=0.694, Mistral=0.633 是正确数字。最新 artifacts Worker 读到了旧的 `8gen_logo_results.json`（现已重命名），那是修复前的残留文件。**

---
