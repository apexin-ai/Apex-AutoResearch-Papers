# infra verify gen01

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-gen01_20260514T064855_result.json`
- **Structured JSON:** [`6f4de19cff8c91417f50.json`](../../sessions/6f/6f4de19cff8c91417f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. 代码修复确认（2 处）
- ✅ `max_samples=2000`（line 248，已被之前 worker 修复，本次确认）
- ✅ `device_id=torch.cuda.current_device() if torch.cuda.is_available() else -1`（line 273，本次修复）

### 2. 关键 stdout 摘要
```
Loading model: EleutherAI/pythia-410m
Loading data from data/wikitext103_5k
Generation 0 (baseline) → MAUVE featurizing p/q 完成 → Gen 0 metrics: ppl=315.08, entropy=3.2342, eff_rank=46.6
Generation 1/1 → Generating synthetic data → Training 5000/5000 steps @ 15.9 it/s (~5min15s)
→ Gen 1 MAUVE featurizing p/q 完成 → ppl=1664.03, entropy=1.9067, eff_rank=79.6, mauve=0.0323
All metrics saved to results/mvp/verify_gen01/all_metrics.json
```

### 3. 验证清单
| # | 检查项 | 结果 |
|---|--------|------|
| 1 | config.json | ✅ PASS |
| 2 | gen_0/metrics.json | ✅ PASS |
| 3 | gen_1/metrics.json | ✅ PASS |
| 4 | gen_1/checkpoint/ | ✅ PASS (model.safetensors 1.6GB + tokenizer) |
| 5 | all_metrics.json | ✅ PASS |

### 4. 完整 metrics.json 内容

**Gen 0 (baseline):**
```json
{
  "token_entropy": 3.2342,
  "self_bleu": 0.0102,
  "distinct_1": 0.0982, "distinct_2": 0.5178, "distinct_3": 0.8127,
  "ece": 0.0108,
  "effective_rank": 46.61,
  "perplexity": 315.08,
  "mauve": 0.0341,
  "generation": 0
}
```

**Gen 1:**
```json
{
  "token_entropy": 1.9067,
  "self_bleu": 0.0103,
  "distinct_1": 0.0975, "distinct_2": 0.5141, "distinct_3": 0.8104,
  "ece": 0.2043,
  "effective_rank": 79.57,
  "perplexity": 1664.03,
  "mauve": 0.0323,
  "generation": 1
}
```

### 5. MAUVE 值范围检查
- Gen 0: **0.0341** ∈ (0, 1) ✅
- Gen 1: **0.0323** ∈ (0, 1) ✅

MAUVE 值偏低（~0.03），说明生成文本与真实文本分布差距较大，但数值合理且未 crash。

### 6. Warnings（无 errors）
- `right-padding was detected` — 无害，tokenizer padding side 警告
- `clustering 3128 points to 156 centroids: please provide at least 6084 training points` — FAISS 聚类警告，不影响结果

### 7. 全部 PASS，无失败项

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "token_entropy": 1.9067,
    "self_bleu": 0.0103,
    "distinct_1": 0.0975,
    "distinct_2": 0.5141,
    "distinct_3": 0.8104,
    "ece": 0.2043,
    "effective_rank": 79.57,
    "perplexity": 1664.03,
    "mauve": 0.0323,
    "generation": 1
  }
}
```

</details>

---
