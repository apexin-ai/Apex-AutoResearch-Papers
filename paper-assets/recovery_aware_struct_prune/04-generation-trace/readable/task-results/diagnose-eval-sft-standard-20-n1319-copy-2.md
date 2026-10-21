# diagnose eval sft standard 20 n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_standard_20_n1319_20260517T010711_result.json`
- **Structured JSON:** [`22de647ff2105b76aa81.json`](../../sessions/22/22de647ff2105b76aa81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已在之前的 session 中删除或未创建），无需处理。

---

## 结果汇报

**eval_sft_standard_20_n1319 — 成功完成 ✓**

| 指标 | 值 |
|------|------|
| Accuracy | **59.29%** |
| N samples | 1319 (full GSM8K test) |
| N correct | 782 |
| Stderr | ±1.35% |
| EOS rate | 98.0% |
| 设置 | greedy (T=0, do_sample=False) |

**Paper Table 1 数据点**: Standard 20% pruning + SFT → **59.29% ± 1.35%**

对比 N=100 快速评估的 64%，full eval 下降约 5pp，这是正常的小样本波动修正。Registry 已更新为 success + 完整 metrics。

---
