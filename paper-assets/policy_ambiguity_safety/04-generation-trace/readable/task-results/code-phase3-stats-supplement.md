# code phase3 stats supplement

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase3_stats_supplement_20260520T134401_result.json`
- **Structured JSON:** [`f26a57315f135683bf2d.json`](../../sessions/f2/f26a57315f135683bf2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 和 CLI 均正常。

新增 6 个分析函数已追加到 `run_full_study.py` Phase 3 section：

| # | 函数 | 输出文件 | 对应 Dream |
|---|------|---------|-----------|
| 1 | `run_power_analysis` | `power_analysis.json` | A3 — C2/C3 MDE via non-central chi-square, underpowered 警告 |
| 2 | `run_tost_equivalence` | `tost_equivalence.json` | A4 — 双 margin (±15pp / ±10pp) two one-sided z-tests |
| 3 | `run_bootstrap_ci` | `bootstrap_ci.json` | BCa bootstrap 10k resamples, 全量 pairwise (condition/type/model) |
| 4 | `run_mcnemar_matched` | `mcnemar_matched.json` | C1 主检验 — matched-pair McNemar + MH OR + per-model 分层 |
| 5 | `run_information_delta` | `information_delta.json` | A10 — per-type token delta + logistic regression 控制变量 |
| 6 | `run_fleiss_kappa` | `fleiss_kappa.json` | Inter-model agreement, 支持 2-4 models 动态检测 |

现有函数和 `run_phase3` 签名未修改，6 个新函数在 `run_phase3()` 末尾依次调用。

---
