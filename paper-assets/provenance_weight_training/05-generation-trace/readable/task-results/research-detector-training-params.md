# research detector training params

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_detector_training_params_20260519T045501_result.json`
- **Structured JSON:** [`6f4d0e2db57e21065c77.json`](../../sessions/6f/6f4d0e2db57e21065c77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有已训练的输出。以下是从代码中提取的全部参数配置：

---

## 1. TF-IDF 参数

| 参数 | 值 | 来源 |
|------|-----|------|
| `ngram_range` | `(1, 2)` (unigram + bigram) | baseline 配置；消融实验中也测了 `(1, 1)` |
| `max_features` | `50000` | baseline 配置；消融实验中也测了 `10000` |
| `sublinear_tf` | `True` | 代码 docstring 明确注明 |
| `analyzer` | sklearn 默认 `"word"` | 未显式设置 |
| `lowercase` | 代码手动 `.lower()` 预处理 | 在 vectorizer 外部执行 |

注：代码中 `TfidfVectorizer` 实例化部分被截断，但 docstring 和 `run_experiment` 函数的 config 字典明确了以上参数。

## 2. Logistic Regression 参数

| 参数 | 值 | 来源 |
|------|-----|------|
| `C` | `1.0` | baseline 配置；消融实验中也测了 `0.01` |
| `solver` | `lbfgs` | docstring 明确注明 |
| `max_iter` | sklearn 默认 `100` | 未显式设置 |
| `penalty` | sklearn 默认 `l2` | 未显式设置 |
| `random_state` | 未显式设置（全局 `SEED=42` 用于 train_test_split） | |

## 3. Calibration 参数

| 参数 | 值 |
|------|-----|
| **Validation set size** | `test_size=0.2`（80/20 split，`train_test_split` with `stratify`） |
| **Calibration method** | **Temperature scaling**（自实现，非 `CalibratedClassifierCV`） |
| **触发条件** | 仅在 `ECE > 0.05` 时才应用 temperature scaling |
| **Temperature 搜索** | `scipy.optimize.minimize_scalar`，bounds `(0.1, 10.0)`，method `"bounded"` |
| **ECE bins** | `n_bins=15` |
| **目标** | NLL 最小化：$-\mathbb{E}[y\log\sigma(z/T) + (1-y)\log(1-\sigma(z/T))]$ |

未使用 Platt scaling 或 isotonic regression；而是直接在 LR 的 raw logits 上做 single-parameter temperature scaling。

## 4. 合成数据生成参数（`generate_synthetic.py`）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `model_name` | `Qwen/Qwen3-0.6B` | 基座生成模型 |
| `temperature` | `0.8` | 采样温度 |
| `top_p` | `0.95` | nucleus sampling |
| `top_k` | 未设置 | 不使用 top-k |
| `max_length` | `512` | prompt + generation 总长度 |
| `prompt_length` | `128` | 从源文本截取的 prompt token 数 |
| `max_new_tokens` | `512 - 128 = 384` | 实际生成长度 |
| `num_tokens` | `100,000,000` (100M) | 目标总 token 数 |
| `batch_size` | `16` | 生成批次大小 |
| `prompt format` | 无特殊 prompt template | 直接截取源文本前 128 tokens 作为 prompt，让模型续写 |
| `fineweb_subset` | `sample-10BT` | FineWeb 子集 |
| `seed` | `42` | |
| `do_sample` | `True` | |
| `depth` | 支持 1/2/3 | depth>1 时使用上一轮 fine-tuned 模型 |

## 5. 消融实验配置（`train_tfidf_detector.py` 的 `configs`）

代码依次尝试 6 种配置，选第一个满足 AUC∈[0.85, 0.98] 且 mid-range ratio≥5% 的：

| Label | max_features | ngram_range | C | max_words |
|-------|-------------|-------------|-----|-----------|
| baseline | 50000 | (1,2) | 1.0 | None |
| fewer_features | 10000 | (1,2) | 1.0 | None |
| unigram_only | 50000 | (1,1) | 1.0 | None |
| strong_reg | 50000 | (1,2) | 0.01 | None |
| truncate_100w | 50000 | (1,2) | 1.0 | 100 |
| combo_degrade | 10000 | (1,1) | 0.01 | 100 |

## 6. Scoring 阶段（`score_data.py`）

- 文本截断至前 **100 words**，小写化
- 使用保存的 `tfidf_vectorizer.joblib` + `lr_model.joblib`
- q_score = `sigmoid(logit / T)`，T 从 `calibration_results.json` 读取

---
