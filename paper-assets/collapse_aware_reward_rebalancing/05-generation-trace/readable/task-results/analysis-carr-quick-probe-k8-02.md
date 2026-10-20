# analysis carr quick probe k8 02

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_quick_probe_k8_02_20260516T195526_result.json`
- **Structured JSON:** [`38b18d3de498a1aca0c1.json`](../../sessions/38/38b18d3de498a1aca0c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 wandb run。结果如下：

```json
{
  "gen0": {"mean_quality": 0.1146, "vendi_score": 107.21, "self_bleu": 0.0057, "perplexity": 9.40, "mean_nn_distance": 0.7097, "complexity_mean": 2.8436},
  "gen1": {"mean_quality": 0.1136, "vendi_score": 107.26, "self_bleu": 0.0024, "perplexity": 9.18, "mean_nn_distance": 0.7086, "complexity_mean": 2.7888},
  "gen2": {"mean_quality": 0.1143, "vendi_score": 107.25, "self_bleu": 0.0064, "perplexity": 10.20, "mean_nn_distance": 0.7095, "complexity_mean": 2.7689},
  "vendi_decline_pct": -0.03,
  "p1_pass": false,
  "checkpoint_path": "/root/autodl-tmp/carr/outputs_k8/gen_2/condition_10/merged",
  "wandb_run_id": null,
  "conclusion": "negative",
  "training_loss_gen2": [0.2059, 0.2042, 0.1669, 0.1322, 0.1288],
  "train_loss_mean_gen2": 0.1676,
  "elapsed_hours": 5.5,
  "summary": "K=8 (12.5%保留率) 3代iterative训练后Vendi Score仅下降0.03%，远未达到P1阈值(≥5%)，与K=4结果一致——单纯提高选择压力不足以在3代内引发可观测的多样性坍缩。"
}
```

**关键发现：**
- Vendi Score 几乎纹丝不动：Gen0=107.21 → Gen2=107.25（变化 -0.03%）
- 与 baseline 对比：no_curation Gen2 Vendi=108.72，K=8 Gen2=107.25，绝对差仅 1.47（1.35%），且这个差距在 Gen0 就已存在（107.21 vs baseline 起始值），并非迭代训练造成的退化
- P1 **未通过**——即使将选择压力从 K=4（25%保留）加倍到 K=8（12.5%保留），3 代内仍无法观测到 ≥5% 的 Vendi 下降
- 这说明当前实验设置（2000 prompts × 3 gens × top-1 selection）对 Mistral-Small-3.1-24B 产生的 collapse 信号极弱，后续需要更多代数或更极端条件才能触发可观测坍缩

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gen0": {
      "mean_quality": 0.1146,
      "vendi_score": 107.21,
      "self_bleu": 0.0057,
      "perplexity": 9.4,
      "mean_nn_distance": 0.7097,
      "complexity_mean": 2.8436
    },
    "gen1": {
      "mean_quality": 0.1136,
      "vendi_score": 107.26,
      "self_bleu": 0.0024,
      "perplexity": 9.18,
      "mean_nn_distance": 0.7086,
      "complexity_mean": 2.7888
    },
    "gen2": {
      "mean_quality": 0.1143,
      "vendi_score": 107.25,
      "self_bleu": 0.0064,
      "perplexity": 10.2,
      "mean_nn_distance": 0.7095,
      "complexity_mean": 2.7689
    },
    "vendi_decline_pct": -0.03,
    "p1_pass": false,
    "checkpoint_path": "/root/autodl-tmp/carr/outputs_k8/gen_2/condition_10/merged",
    "wandb_run_id": null,
    "conclusion": "negative",
    "training_loss_gen2": [
      0.2059,
      0.2042,
      0.1669,
      0.1322,
      0.1288
    ],
    "train_loss_mean_gen2": 0.1676,
    "elapsed_hours": 5.5,
    "summary": "K=8 (12.5%保留率) 3代iterative训练后Vendi Score仅下降0.03%，远未达到P1阈值(≥5%)，与K=4结果一致——单纯提高选择压力不足以在3代内引发可观测的多样性坍缩。"
  }
}
```

</details>

---
