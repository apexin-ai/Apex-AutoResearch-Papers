# code deberta cross transfer prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deberta-cross-transfer-prep_20260519T174654_result.json`
- **Structured JSON:** [`9b3f1731879eaa46ce7f.json`](../../sessions/9b/9b3f1731879eaa46ce7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，脚本就绪。

## 报告

### 1. 可用 generator model 数据

| Model | 路径 | 样本量 |
|-------|------|--------|
| wiki_pythia | `data/exp_wiki_pythia/` | 6 depths × 5000 = 30,000 |
| wiki_olmo | `data/exp_wiki_olmo/` | 6 depths × 5000 = 30,000 |
| wiki_qwen7b | `data/exp_wiki_qwen7b/` | 6 depths × 5000 = 30,000 |
| wiki_llama8b | `data/exp_wiki_llama8b/` | 6 depths × 5000 = 30,000 |
| wiki_mistral7b | `data/exp_wiki_mistral7b/` | 6 depths × 5000 = 30,000 |

数据格式：`depth_{0..5}.jsonl`，每行 `{"text": "...", "doc_id": N}`。

### 2. 脚本与运行命令

**脚本**：`/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_cross_transfer.py`

```bash
# 单对
python scripts/run_deberta_cross_transfer.py \
    --train_model wiki_pythia --test_model wiki_qwen7b --gpu 2

# 全 N×N matrix (5×4=20 对)
python scripts/run_deberta_cross_transfer.py --all_pairs --gpu 2
```

**设计**：在 train_model 数据上 5-fold GroupKFold 训练 5 个 DeBERTa 模型，ensemble 预测 test_model 全量数据，输出每个 depth pair 的 AUC (bootstrap CI) + F1@0.50 + K*。

### 3. 预估运行时间 (RTX 4090D)

- 单对 ≈ 20~30 min（5 fold × 3 epoch × ~24k 训练样本 + 5 次 30k 推理）
- 全 matrix 20 对 ≈ **7~10 小时**

---
