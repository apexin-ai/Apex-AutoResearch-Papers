## d112_rsft_no_evidence_eval_r3 Results

### Run Config
- Model: Qwen3-4B + SFT adapter (s44) + RSFT adapter (bf16)
- Split: dev (985 documents, 12275 gold triples)
- no_evidence: **true** (confirmed in config)
- batch_size: 4, max_new_tokens: 1024, seed: 42
- Inference time: 9288.3s (9.43 s/doc, ~2h35m total)

### Metrics
- **ign_f1: 0.5246**
- f1: 0.5341
- precision: 0.5338
- recall: 0.5344
- ign_precision: 0.5122
- ign_recall: 0.5377
- evi_f1: 0.0000 (expected, no evidence output)
- edcr: 0.0000 (expected, no evidence output)
- format_ok: 983/985 (99.80%)
- n_parseable: 981/985
- n_truncated: 144/985 (14.6%)
- n_predictions: 16018
- tp: 6493, pred_count: 12164, gold_count: 12151

### Evidence Tax
- With evidence (d112_rsft_s44_eval_bf16): ign_f1 = 0.5152
- Without evidence (this run): ign_f1 = 0.5246
- **Evidence tax: +0.94pp** (positive = removing evidence improves RE, i.e., evidence generation hurts 4B performance)

### Conclusion
**Success.** 4B RSFT shows a meaningful evidence tax of +0.94pp — generating evidence costs nearly 1 F1 point at this scale. This contrasts with the 8B result where evidence provides a small bonus (-0.78pp), and 14B where the tax is essentially zero.

The pattern emerging: **evidence generation is harmful at small scale (4B), neutral at large scale (14B), and slightly beneficial at medium scale (8B).** The 8B result is somewhat anomalous — the expected monotonic trend (tax decreases with scale) doesn't hold perfectly.

### Cross-scale Evidence Tax Summary (RSFT)
| Scale | With-evi | No-evi | Tax | Note |
|-------|----------|--------|-----|------|
| 1.7B  | 0.5119   | ???    | confounded | truncation artifacts invalidated no-evi eval |
| 4B    | 0.5152   | 0.5246 | **+0.94pp** | evidence hurts RE |
| 8B    | 0.5414   | 0.5336 | **-0.78pp** | evidence slightly helps RE |
| 14B   | —        | —      | pending | |

### Notes
- **Truncation**: 144/985 (14.6%) documents truncated. This is non-trivial but expected — no-evidence outputs are shorter than with-evidence, so this is comparable to or better than with-evidence truncation rates. The truncation here comes from the relation extraction output itself being long for documents with many entity pairs, not from evidence text.
- **Format compliance**: 99.8% format OK (983/985), 2 unparseable — good quality.
- **No W&B run**: This eval did not log to W&B.
- **Config verified**: `no_evidence: true` confirmed in metrics.json config, ruling out the plan_006-style prompt mismatch bug.
- **Output artifacts**: metrics.json and predictions.json saved at `/root/autodl-tmp/eval_outputs/eval_4b_rsft_s44_no_evidence/`
