# ops feat ablation v1 triage

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feat_ablation_v1_triage_20260515T193355_result.json`
- **Structured JSON:** [`dc34c3fd144e7baf5b01.json`](../../sessions/dc/dc34c3fd144e7baf5b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**feat_ablation_v1 — 成功完成。** Registry 已更新为 DONE/success，cron 已清除。

关键结果：
- 全部 9 cell（pythia/gpt2xl/olmo × nucleus095/temp09/topk50）forward selection 完成
- Top-2 特征 71.5% acc → Top-5 76.8% → Full-19 78.5%，~5 个特征即达 95% 性能
- **Perplexity 类特征全面主导**（76.7% mean acc），远超 surprisal（73.3%）、lexical diversity（46.2%）等
- Forward selection 首选特征：Pythia 选 `var_surprisal`，GPT2-XL 和 OLMo 选 `p90_ppl`

---
