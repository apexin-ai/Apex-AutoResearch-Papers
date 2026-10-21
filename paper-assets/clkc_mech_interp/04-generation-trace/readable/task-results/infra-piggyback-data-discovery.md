# infra piggyback data discovery

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_piggyback-data-discovery_20260523T072645_result.json`
- **Structured JSON:** [`053c98d7a91a05b986a8.json`](../../sessions/05/053c98d7a91a05b986a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已确认。汇报如下：

---

## Piggyback 实验数据路径确认

### 1. Conflict 探针权重

**⚠️ 不存在。** `train_probe.py` 使用 sklearn `LogisticRegression`，仅保存结果 JSON（`json.dump`），**不保存模型权重**（无 joblib/pickle/torch.save）。需要时须从激活文件重新训练。

### 2. XNLI 探针权重

**⚠️ 同上，不存在。**

### 3. Conflict 激活文件

| 模型 | en | zh | de | 路径前缀 |
|------|:---:|:---:|:---:|------|
| Llama3.1 | ✅ 342MB | ✅ 342MB | ✅ 342MB | `data/llama31/` |
| Qwen3 | ✅ 272MB | ✅ 272MB | **❌ 缺失** | `data/qwen3/` |
| Gemma2 | ✅ 457MB | ✅ 457MB | **❌ 缺失** | `data/gemma2/` |

注意：**目录名是 `qwen3`**，不是 `qwen`。Qwen3 和 Gemma2 缺少德语 (`de_activations.pt`)。

### 4. XNLI 激活文件

| 模型 | en | zh | 路径前缀 |
|------|:---:|:---:|------|
| Llama3.1 | ✅ 250MB | ✅ 250MB | `data/xnli/llama31/` |
| Qwen3 | ✅ 281MB | ✅ 281MB | `data/xnli/qwen3/` |
| Gemma2 | ✅ 287MB | ✅ 287MB | `data/xnli/gemma2/` |

全部齐全。

### 5. Bootstrap n=2000 结果

| 任务 | 模型 | 状态 | 路径 |
|------|------|:---:|------|
| Conflict | Llama3.1 | ✅ | `data/llama31/probe_results_bootstrap_n2000.json` |
| Conflict | Qwen3 | ✅ | `data/qwen3/probe_results_bootstrap_n2000.json` |
| Conflict | Gemma2 | ✅ | `data/gemma2/probe_results_bootstrap_n2000.json` |
| Conflict(de) | Llama3.1 | ✅ | `data/llama31/de_bootstrap_n2000_results.json` |
| XNLI | Gemma2 | ✅ | `data/xnli/gemma2/probe_results_bootstrap_n2000.json` |
| XNLI | Llama3.1 | **❌ 缺失** | — |
| XNLI | Qwen3 | **❌ 缺失** | — |

### 6. Bootstrap JSON 格式（TOST 关键）

**两种格式，都不保存原始 bootstrap Δ 分布：**

- **Conflict 格式**（llama31/qwen3）：`per_layer` → `{en_en, en_zh, ...}` → `layer_N` → `{mean, std, ci_lower, ci_upper}` + `asymmetry_per_layer` → `layer_N` → `{mean_diff, ci_lower, ci_upper}` + `config: {n_seeds, n_jobs}`
- **XNLI/de 格式**（gemma2、de）：`directions` → `{EN->EN, ...}` → `{balanced_accuracy_mean, std, ci_lo, ci_hi, f1_mean, f1_std, peak_layers: [2000个值]}`

**⚠️ 如果 TOST 检验需要原始 per-bootstrap-sample 的 Δ 值，必须从激活文件重跑 bootstrap 并保存完整分布。**

### 7. 缺失项汇总

| # | 缺失 | 影响 |
|---|------|------|
| 1 | Qwen3 `de_activations.pt` | Conflict 德语三模型对比不齐 |
| 2 | Gemma2 `de_activations.pt` | 同上 |
| 3 | XNLI Llama3.1 bootstrap n=2000 | TOST 需重跑 |
| 4 | XNLI Qwen3 bootstrap n=2000 | TOST 需重跑 |
| 5 | 探针权重文件（全部模型） | piggyback 需从激活重新训练探针 |
| 6 | 原始 bootstrap Δ 分布 | TOST 需修改 bootstrap 脚本保存 raw samples |

---
