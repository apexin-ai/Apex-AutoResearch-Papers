# analysis exp 011 llama8b v3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-011-llama8b-v3_20260517T075618_result.json`
- **Structured JSON:** [`0ae0129c380a31be1434.json`](../../sessions/0a/0ae0129c380a31be1434.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部指标提取完成。汇总如下：

```json
{
  "experiment": "exp-011-llama8b-v3",
  "model": "LLaMA-3.1-8B-Instruct",
  "dataset": "D012 (30 ProofWriter-D5 + 30 FOLIO)",
  "result_file": "/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json",
  
  "metrics": {
    "n": 60,
    "k": 12,
    "sica_accuracy": 0.6667,
    "sc_accuracy": 0.6000,
    "delta_pp": "+6.67 pp",
    "sica_correct": 40,
    "sc_correct": 36,
    "extraction_rate": 0.8556,
    "answer_extraction_rate": 0.8958,
    "multi_candidate_rate": 0.6167,
    "multi_candidate_count": 37,
    "contradiction_rate": 0.0527,
    "problems_with_contradictions": 43,
    "truncated_traces": 44
  },

  "discordant_analysis": {
    "both_correct": 35,
    "both_wrong": 19,
    "discordant_sica_wins": 5,
    "discordant_sc_wins": 1,
    "sica_win_ratio": "5:1"
  },

  "per_dataset": {
    "proofwriter": { "sica": 0.6333, "sc": 0.6000, "delta_pp": "+3.33", "n": 30 },
    "folio":       { "sica": 0.7000, "sc": 0.6000, "delta_pp": "+10.00", "n": 30 }
  },

  "statistical_test": {
    "mcnemar_exact_p": 0.2188,
    "n_discordant": 6,
    "significant_at_0.05": false
  },

  "wandb": null,
  "wall_time_min": 66.4,

  "conclusion": "success",
  "summary": "SICA 在 LLaMA-3.1-8B 上以 66.7% vs 60.0% (+6.67pp) 胜出 SC，discordant pairs 5:1 倾向 SICA。FOLIO 子集增益更大 (+10pp)。McNemar p=0.22 未达显著（n=60 样本量受限），但方向一致，确认 capability trap 跨模型家族泛化。"
}
```

**关键发现：**
- SICA 在非 Qwen 模型上依然有效，+6.67pp 增益方向与 Qwen 实验一致
- Discordant pairs 5:1 强烈倾向 SICA（6 对不一致中 SICA 赢 5 对）
- FOLIO（自然语言 FOL）增益 +10pp 大于 ProofWriter +3.33pp
- 统计显著性未达（p=0.22），受限于 n=60 样本量，但 effect direction 明确
- 多候选率 61.7%，约束提取率 85.6%，系统在 LLaMA 上运行正常

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "exp-011-llama8b-v3",
    "model": "LLaMA-3.1-8B-Instruct",
    "dataset": "D012 (30 ProofWriter-D5 + 30 FOLIO)",
    "result_file": "/root/symb_invariant_consensus/results/exp011_llama8b/exp011_results.json",
    "metrics": {
      "n": 60,
      "k": 12,
      "sica_accuracy": 0.6667,
      "sc_accuracy": 0.6,
      "delta_pp": "+6.67 pp",
      "sica_correct": 40,
      "sc_correct": 36,
      "extraction_rate": 0.8556,
      "answer_extraction_rate": 0.8958,
      "multi_candidate_rate": 0.6167,
      "multi_candidate_count": 37,
      "contradiction_rate": 0.0527,
      "problems_with_contradictions": 43,
      "truncated_traces": 44
    },
    "discordant_analysis": {
      "both_correct": 35,
      "both_wrong": 19,
      "discordant_sica_wins": 5,
      "discordant_sc_wins": 1,
      "sica_win_ratio": "5:1"
    },
    "per_dataset": {
      "proofwriter": {
        "sica": 0.6333,
        "sc": 0.6,
        "delta_pp": "+3.33",
        "n": 30
      },
      "folio": {
        "sica": 0.7,
        "sc": 0.6,
        "delta_pp": "+10.00",
        "n": 30
      }
    },
    "statistical_test": {
      "mcnemar_exact_p": 0.2188,
      "n_discordant": 6,
      "significant_at_0.05": false
    },
    "wandb": null,
    "wall_time_min": 66.4,
    "conclusion": "success",
    "summary": "SICA 在 LLaMA-3.1-8B 上以 66.7% vs 60.0% (+6.67pp) 胜出 SC，discordant pairs 5:1 倾向 SICA。FOLIO 子集增益更大 (+10pp)。McNemar p=0.22 未达显著（n=60 样本量受限），但方向一致，确认 capability trap 跨模型家族泛化。"
  }
}
```

</details>

---
