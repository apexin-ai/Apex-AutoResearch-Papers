# audit evaluate git and no trace check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_evaluate_git_and_no_trace_check_20260516T022615_result.json`
- **Structured JSON:** [`de109d438e9655d3c4a3.json`](../../sessions/de/de109d438e9655d3c4a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## 任务 A: evaluate.py git 历史分析

### 3 次 commit 汇总

| Commit | 时间 | 改动 |
|--------|------|------|
| `42bad40` | May 16 01:10 | **初始创建** evaluate.py，`predict()` 中使用 `tokenizer(..., truncation=True, max_length=2048)` 截断输入 |
| `0836dd4` | May 16 01:25 | **修改截断方式**：v1 的右截断会砍掉 chat template 的 generation prompt（导致 full_trace 5.88%），改为 content-aware 截断——先截原始 input_text 再重建 chat template。VOTA sanity check 99.41% 预测不变 |
| `e404237` | May 16 07:32 | **仅加 CLI 选项**：`--condition` choices 增加 5 个 debugbench 条件名。零逻辑变更 |

### 核心逻辑是否变化？

**没有。** 以下从未改动：
- 推理：greedy decoding, `max_new_tokens=1, do_sample=False`
- 答案分类：`classify_prediction()` — `"pass" in pred` / `"fail" in pred`
- 指标计算：`compute_metrics()` + `bootstrap_ci()`

两次 fix 只改了 `predict()` 里的 **输入截断策略**。

### registry 中 `reeval_with_fixed_script` 的 16% 怎么回事？

corrected evaluate.py 默认 `max_length=2048`，而 VOTA condition 91.7% 样本超过 2048 tokens。截断后 question suffix 丢失 → 模型几乎全预测 fail → accuracy 16%。

后续 **confirmatory 评估**（`eval_results_confirmatory.json`，May 16 07:01）用 `max_length=16384` 不截断 → **accuracy=84.45%**，与原始完全一致。

**结论：原始 84.45% 可靠。"corrected" script 的低分是截断参数问题，不是核心逻辑变更。**

---

## 任务 B: deepseek_no_trace predictions.jsonl 状态

### 文件清单与时间线

| 文件 | 创建时间 | 说明 |
|------|----------|------|
| `adapter_model.safetensors` | May 15 21:34:22 | 训练完成 |
| `eval_results.json` | May 15 21:35:19 | 原始自动评估（紧随训练） |
| `eval_results_strict.json` | May 16 06:50:45 | 后续 re-eval（内容与原始 100% 相同） |
| `predictions.jsonl` | May 16 06:50:45 | re-eval 时 `--save_predictions` 生成 |

### Accuracy 验证

| 来源 | accuracy | n |
|------|----------|---|
| eval_results.json (原始) | **73.36%** | 1190 |
| eval_results_strict.json (re-eval) | **73.36%** | 1190 |
| predictions.jsonl 逐行重算 | **73.36%** | 1190 |
| registry.yaml 记录 | **73.36%** | 1190 |

四处完全一致。

### 是否被 run_missing_predictions.sh 污染？

**否。** `run_missing_predictions.sh` 只处理 `deepseek_full_trace_seed42_v3` 和 `debugbench_vota`，不涉及 deepseek_no_trace。

### 是否需要 re-eval？

**不需要。** predictions.jsonl 虽由后续 re-eval 生成（非原始产物），但 accuracy 与原始 eval_results.json 完全一致，结果可复现。

### 注意

`results/predictions/no_trace_predictions.json`（accuracy=75.13%）是 **Qwen-based** no_trace 模型的结果，与 DeepSeek no_trace 无关。

---
