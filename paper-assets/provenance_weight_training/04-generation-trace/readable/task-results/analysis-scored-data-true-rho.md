# analysis scored data true rho

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scored_data_true_rho_20260518T071018_result.json`
- **Structured JSON:** [`0ce824d1384baa519d05.json`](../../sessions/0c/0ce824d1384baa519d05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。结果如下：

```json
{
  "scored_data.jsonl": {
    "n_lines": 371499,
    "n_real": 164889,
    "n_synthetic": 206610,
    "real_doc_ratio": 0.4438,
    "synthetic_doc_ratio": 0.5562,
    "real_avg_words": 560.2,
    "synthetic_avg_words": 304.1,
    "real_total_words": 92364962,
    "synthetic_total_words": 62825549,
    "synthetic_TOKEN_ratio": 0.4048,
    "q_score_mean": 0.5987,
    "q_score_median": 0.7049,
    "q_score_min": 0.0002,
    "q_score_max": 1.0000
  },
  "scored_data_60.jsonl": {
    "n_lines": 371499,
    "n_real": 148599,
    "n_synthetic": 222900,
    "real_doc_ratio": 0.4000,
    "synthetic_doc_ratio": 0.6000,
    "real_avg_words": 562.4,
    "synthetic_avg_words": 304.0,
    "real_total_words": 83566003,
    "synthetic_total_words": 67769444,
    "synthetic_TOKEN_ratio": 0.4478,
    "q_score_mean": 0.6243,
    "q_score_median": 0.7753,
    "q_score_min": 0.0002,
    "q_score_max": 1.0000
  },
  "contamination_ratio_definition": "run_mvp.sh 中 CONTAMINATION_RATIO=0.4 是 TOKEN 级别的比例：生成 80M synthetic tokens + 120M human tokens，然后拼接所有文档。pretrain_weighted.py 中 --contamination_ratio 仅作为 metadata 记录，不参与权重计算。prepare_rho06_data.py 中 RHO=0.6 则是 DOCUMENT 级别的比例：按 ceil(371499*0.6) 采样文档。两种脚本对 ρ 的定义不同。",
  "conclusion": "ρ=0.4 标称值与实际值一致——在 TOKEN 级别。scored_data.jsonl 的 synthetic token 占比 = 40.48%，符合标称 ρ=0.4。但 synthetic DOC 占比 = 55.62%，因为 synthetic 文档平均长度（304 words）远短于 human 文档（560 words），同样的 token 预算需要更多 synthetic 文档。之前 α_eff 分析报告的 'true_contamination_ratio=0.556' 是正确的文档级比例，不存在数据错误——只是 ρ 的定义层级不同（token vs document）。"
}
```

**根因总结**：没有数据错误，也没有读错文件。差异来自 ρ 的定义层级：

| 指标 | scored_data.jsonl | scored_data_60.jsonl |
|------|-------------------|----------------------|
| ρ 定义层级 | token 级 (run_mvp.sh) | document 级 (prepare_rho06_data.py) |
| synthetic doc 比例 | 55.62% | 60.00% |
| synthetic token 比例 | 40.48% | 44.78% |
| 标称 ρ | 0.4 (token) | 0.6 (doc) |

synthetic 文档平均 304 words，human 文档平均 560 words（1.84x），这个长度差导致了 token 级和 document 级比例的分离。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "scored_data.jsonl": {
      "n_lines": 371499,
      "n_real": 164889,
      "n_synthetic": 206610,
      "real_doc_ratio": 0.4438,
      "synthetic_doc_ratio": 0.5562,
      "real_avg_words": 560.2,
      "synthetic_avg_words": 304.1,
      "real_total_words": 92364962,
      "synthetic_total_words": 62825549,
      "synthetic_TOKEN_ratio": 0.4048,
      "q_score_mean": 0.5987,
      "q_score_median": 0.7049,
      "q_score_min": 0.0002,
      "q_score_max": 1.0
    },
    "scored_data_60.jsonl": {
      "n_lines": 371499,
      "n_real": 148599,
      "n_synthetic": 222900,
      "real_doc_ratio": 0.4,
      "synthetic_doc_ratio": 0.6,
      "real_avg_words": 562.4,
      "synthetic_avg_words": 304.0,
      "real_total_words": 83566003,
      "synthetic_total_words": 67769444,
      "synthetic_TOKEN_ratio": 0.4478,
      "q_score_mean": 0.6243,
      "q_score_median": 0.7753,
      "q_score_min": 0.0002,
      "q_score_max": 1.0
    },
    "contamination_ratio_definition": "run_mvp.sh 中 CONTAMINATION_RATIO=0.4 是 TOKEN 级别的比例：生成 80M synthetic tokens + 120M human tokens，然后拼接所有文档。pretrain_weighted.py 中 --contamination_ratio 仅作为 metadata 记录，不参与权重计算。prepare_rho06_data.py 中 RHO=0.6 则是 DOCUMENT 级别的比例：按 ceil(371499*0.6) 采样文档。两种脚本对 ρ 的定义不同。",
    "conclusion": "ρ=0.4 标称值与实际值一致——在 TOKEN 级别。scored_data.jsonl 的 synthetic token 占比 = 40.48%，符合标称 ρ=0.4。但 synthetic DOC 占比 = 55.62%，因为 synthetic 文档平均长度（304 words）远短于 human 文档（560 words），同样的 token 预算需要更多 synthetic 文档。之前 α_eff 分析报告的 'true_contamination_ratio=0.556' 是正确的文档级比例，不存在数据错误——只是 ρ 的定义层级不同（token vs document）。"
  }
}
```

</details>

---
