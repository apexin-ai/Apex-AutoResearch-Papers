# research ced reranking code search

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ced_reranking_code_search_20260517T045528_result.json`
- **Structured JSON:** [`24d3b779be3785608d89.json`](../../sessions/24/24d3b779be3785608d89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是调研结果：

---

## 调研结果

### 1. 现有可复用代码

| 路径 | 用途 |
|------|------|
| `freige/rewards/ced_reward.py` | **核心 NLI 模块**：`CEDRewardModel` 类，含 `nli_entailment_prob(premises, hypotheses)` 批量推理，`compute_ced_reward()` 和 `compute_flat_nli_reward()` |
| `freige/eval/ced_reranker.py` | **已有完整 CED reranking 实现**：`score_candidate_ced()` 函数，对每个 triple 用 predicted evidence 做 CED scoring |
| `freige/rewards/ced_reward.py::verbalize_triple()` | 将 `(head, Pxxx, tail)` 转为自然语言 claim |
| `freige/eval/ced_reranker.py::verbalize_by_name()` | 用 relation name（而非 Pxxx code）做 verbalization |
| `freige/training/rsft_score_filter.py` | RSFT 打分筛选，`compute_ced_reward_for_record()` |

### 2. Predictions 文件格式

```json
{
  "doc_id": "Skai TV",
  "raw_output": "[{\"head\": \"Skai TV\", ...}]",
  "parsed_triples": [
    {"head": "Skai TV", "relation": "country", "tail": "Greece", "evidence": [0, 4]},
    {"head": "Skai TV", "relation": "headquarters location", "tail": "Piraeus", "evidence": [0]}
  ],
  "gold_triples": [
    {"head": "Piraeus", "tail": "Greece", "relation": "country", "evidence": [0, 4]}
  ],
  "truncated": false,
  "format_ok": true
}
```

**关键发现**：
- `evidence` 字段是 **sentence index 列表**（整数），不是原文
- predictions.json **不含 `sents`**，原文句子需从 `/root/autodl-tmp/data/docred/dev.json` 中按 `doc_id`（即 `title`）匹配获取
- `dev.json` 中句子格式为 `doc["sents"]`（list of list of tokens），需 `" ".join(s)` 转为完整句子

### 3. 关键问题回答

1. **evidence 格式**：sentence index（int list），如 `[0, 4]`
2. **NLI premise/hypothesis**：
   - premise = concat of cited evidence sentences（用 index 从 doc sents 中取出拼接）
   - hypothesis = verbalized triple（用 `verbalize_by_name(head, relation, tail)`）
3. **现有代码可复用？** — **`ced_reranker.py` 已经是你要做的事情的完整实现**。它做的是 candidate-level reranking（选最佳 candidate），而你需要的是 **per-triple evidence filtering**（在单个 candidate 内过滤 evidence sentences）。核心 NLI 调用 `CEDRewardModel.nli_entailment_prob()` 完全可复用。

### 4. 建议的 Evidence Filtering 脚本方案

与已有 `ced_reranker.py`（选最佳 candidate）不同，新脚本做的是 **per-sentence evidence filtering**：

```python
# freige/eval/ced_evidence_filter.py

def filter_evidence_per_triple(
    triple: dict,           # {"head", "relation", "tail", "evidence": [int]}
    sents: list[str],       # document sentences
    ced_model: CEDRewardModel,
    tau: float = 0.5,
) -> dict:
    """对单个 triple 的每条 evidence sentence 独立 scoring，过滤低分句。"""
    claim = verbalize_by_name(triple["head"], triple["relation"], triple["tail"])
    evi_ids = [i for i in triple["evidence"] if 0 <= i < len(sents)]
    
    if not evi_ids:
        return {**triple, "evidence": [], "evi_scores": []}
    
    # 每句独立：premise=single sentence, hypothesis=claim
    premises = [sents[i] for i in evi_ids]
    hypotheses = [claim] * len(evi_ids)
    scores = ced_model.nli_entailment_prob(premises, hypotheses).tolist()
    
    # 过滤
    kept = [(idx, s) for idx, s in zip(evi_ids, scores) if s >= tau]
    return {
        **triple,
        "evidence": [idx for idx, _ in kept],
        "evi_scores": {idx: s for idx, s in zip(evi_ids, scores)},
    }


def main(predictions_path, data_dir, output_dir, taus=[0.3, 0.5, 0.7]):
    # 1. 加载 predictions + dev.json (获取 sents)
    # 2. 按 doc_id 匹配 sents
    # 3. 对每个 doc 的每个 parsed_triple 调用 filter_evidence_per_triple
    # 4. 对每个 tau 输出 filtered_predictions.json
    # 5. 对每个 tau 调用 DocREDEvaluator 计算 metrics
```

**与 `ced_reranker.py` 的区别**：
- `ced_reranker`: 整个 candidate 打分 → 选最佳 candidate（不改 evidence）
- 新脚本: 固定 candidate → 对每个 triple 的每条 evidence sentence 独立 NLI scoring → 删除低质量 evidence

**NLI model 路径**: `/root/autodl-tmp/models/nli-deberta-v3-base` 或 `/root/autodl-tmp/models/deberta-v3-large-zeroshot-v2.0`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "doc_id": "Skai TV",
    "raw_output": "[{\"head\": \"Skai TV\", ...}]",
    "parsed_triples": [
      {
        "head": "Skai TV",
        "relation": "country",
        "tail": "Greece",
        "evidence": [
          0,
          4
        ]
      },
      {
        "head": "Skai TV",
        "relation": "headquarters location",
        "tail": "Piraeus",
        "evidence": [
          0
        ]
      }
    ],
    "gold_triples": [
      {
        "head": "Piraeus",
        "tail": "Greece",
        "relation": "country",
        "evidence": [
          0,
          4
        ]
      }
    ],
    "truncated": false,
    "format_ok": true
  }
}
```

</details>

---
