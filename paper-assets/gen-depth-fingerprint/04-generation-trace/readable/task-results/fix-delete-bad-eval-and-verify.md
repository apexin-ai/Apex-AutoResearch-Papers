# fix delete bad eval and verify

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_delete-bad-eval-and-verify_20260518T192928_result.json`
- **Structured JSON:** [`5a1718f0d01ddf5e1cf1.json`](../../sessions/5a/5a1718f0d01ddf5e1cf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. 废弃文件已删除
`temp_olmo-2-1b_t0.5_eval.json` 已删除。剩余 OLMo 文件：
- `temp_olmo-2-1b_t05_eval.json`
- `temp_olmo-2-1b_t09_eval.json`

### 2. Monitor eval 代码：确认使用 LOGO
**是，使用 LOGO。** 证据：
- 第86行：`"""Run feature extraction then LOGO classification for one target."""`
- 训练集构建方式（第188行）：`train_df = baseline[baseline["model_name"] != model_name]` — 排除当前模型的所有数据作为训练集，用当前模型数据作为测试集，这就是 **Leave-One-Generator-Out**
- 不是 train_test_split，分类器在其他 generator 数据上训练，在目标 generator 上测试

Qwen t=0.9 触发 pipeline 时会走完全相同的 `run_pipeline()` → `build_eval_script()` 路径。

### 3. Qwen t=0.9 进度
**Lines=3845, Seeds=850** — 生成仍在进行中（每个 seed 约 4.5 条，全量 seed 数取决于数据集大小）。

### 4. 现存结果文件摘要

| 文件 | model | binary_f1 | three_class_f1 |
|---|---|---|---|
| `temp_curve_binary_logo.json` | N/A (汇总格式不同) | — | — |
| `temp_olmo-2-1b_t05_eval.json` | olmo-2-1b | 0.7826 | 0.8425 |
| `temp_olmo-2-1b_t09_eval.json` | olmo-2-1b | 0.4532 | 0.5631 |
| `temp_qwen3-0.6b_t05_eval.json` | qwen3-0.6b | 0.7111 | 0.8019 |

Qwen t=0.9 的 eval 结果尚未生成，等生成完成后 monitor 会自动触发 pipeline 产出 `temp_qwen3-0.6b_t09_eval.json`。

---
