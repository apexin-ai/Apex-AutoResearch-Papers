# infra data rebuild investigation

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_data-rebuild-investigation_20260523T220405_result.json`
- **Structured JSON:** [`002a9fdb66d461c44ba0.json`](../../sessions/00/002a9fdb66d461c44ba0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是调查结果：

---

## collect_activations.py
- **输入**: JSONL 文件，按语言命名规则：
  - EN: `{data_dir}/en_conflict_train_verified.jsonl` + `en_conflict_test_verified.jsonl`
  - ZH: `{data_dir}/zh_conflict_train_validated.jsonl` + `zh_conflict_test_validated.jsonl`
  - DE: `{data_dir}/de_conflict_train.jsonl` + `de_conflict_test.jsonl`
  - 也可通过 `--train_file` / `--test_file` 直接指定路径
- **JSONL 字段**: `question`, `context`, `label`（"conflict" / "no_conflict"）
- **输出**: `{output_dir}/{lang}_activations.pt`，包含 `activations` (N, num_layers, hidden_dim)、`labels` (N,)、`split_sizes`
- **参数**: `--model`（默认 Qwen3-8B-Instruct）、`--lang`、`--batch_size`、`--data_dir`、`--output_dir`

## steering_experiment.py
- **数据加载**:
  - `{data_dir}/en_activations.pt` — 用于训练 probe、提取 steering direction
  - `{data_dir}/en_conflict_test_verified.jsonl` — conflict 子集用于 steering 生成测试
  - `{data_dir}/probe_results.json`（可选）— 读取 peak layer
- **JSONL 格式要求**: `question`, `context`, `label`, `parametric_answer`, `contextual_answer`
- **参数**: `--model`, `--data_dir`, `--alphas`, `--peak_layer`, `--position`, `--output_suffix`

## 数据获取方案
- **ConflictQA HuggingFace**: **可用**。`osunlp/ConflictQA`，子集 `ConflictQA-popQA-chatgpt`。可通过 `load_dataset("osunlp/ConflictQA", "ConflictQA-popQA-chatgpt")` 或 `hf_hub_download("osunlp/ConflictQA", "conflictQA-popQA-chatgpt.json", repo_type="dataset")` 获取
- **翻译脚本**: 存在。`translate_to_zh.py`（Qwen3翻译）、`translate_to_de.py`（Llama翻译）、`validate_translation.py`（COMET back-translation gate）
- **初始采样脚本**: **缺失**。没有独立脚本生成最初的 `raw_sampled_{train,test}.jsonl` 和 `en_conflict_{train,test}.jsonl`。但 `supplement_sampling.py` 中的 `raw_to_en_conflict()` 函数包含了完整的转换逻辑（ConflictQA 原始格式 → en_conflict JSONL 格式），可以复用

## 最短重建路径

1. **下载 ConflictQA**: `hf_hub_download("osunlp/ConflictQA", "conflictQA-popQA-chatgpt.json")`
2. **写一个采样脚本**（复用 `supplement_sampling.py` 中的 `filter_valid()` + `raw_to_en_conflict()` 逻辑）：从原始数据采样 → 生成 `raw_sampled_{train,test}.jsonl` + `en_conflict_{train,test}.jsonl`
3. **运行 `run_mvp.sh` pipeline**: verify → translate → COMET validate → collect activations → train probe
4. **运行 `steering_experiment.py`**

步骤 2 需要确定采样数量（原始采样约 500 条，supplement 加了 1500+1000 = 总计约 3000 条）。

---
