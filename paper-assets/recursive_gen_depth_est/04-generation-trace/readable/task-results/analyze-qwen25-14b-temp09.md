# analyze qwen25 14b temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen25_14b_temp09_20260520T040138_result.json`
- **Structured JSON:** [`040ee90ae5cd3cc74fe6.json`](../../sessions/04/040ee90ae5cd3cc74fe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Registry 已更新为 DONE/success，artifact 已注册。

**结果摘要**：

| Metric | Value |
|--------|-------|
| RF 4-class acc | **50.5%** (CI: 49.8–51.2%) — 2× chance |
| LR 4-class acc | 48.65% (CI: 48.0–49.4%) |
| RF 3-class (d1-d3) | 52.44% (CI: 51.6–53.2%) |
| d0v1 AUC | 0.632 |
| d1v2 AUC | **0.726** (最强 adjacent pair) |
| d2v3 AUC | 0.618 |
| Top features | p90_ppl, skew_ppl, kurt_ppl, p90_surprisal, var_surprisal |

**未计算的 metrics**: per-depth recall, confusion matrix, MAE, QWK, EDD_{0.70}——该 pipeline 不输出这些。

**评估**: 50.5% 显著超过 25% chance，depth signal 在 14B temp=0.9 下持续存在。但低于小模型同 setting（pythia ~73%, gpt2xl ~83%），符合 scaling 预期——14B 生成文本更连贯，depth 区分更难。

---
