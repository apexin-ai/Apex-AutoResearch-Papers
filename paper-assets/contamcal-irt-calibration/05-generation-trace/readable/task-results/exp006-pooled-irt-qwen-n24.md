# exp006 pooled irt qwen n24

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp006_pooled-irt-qwen-n24_20260516T190113_result.json`
- **Structured JSON:** [`389776b880aa60d9098a.json`](../../sessions/38/389776b880aa60d9098a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Pooled IRT Results (2PL+γ, Qwen-only, RRF signal exposure)

| Benchmark | N | Items | γ̂ (mean) | 95% CI | R̂ | ESS | PPP | raw_MAE | cal_MAE | ΔMAE |
|-----------|---|-------|-----------|--------|-----|-----|-----|---------|---------|------|
| **mmlu** | 16 | 300 | 0.6551 | [-0.4056, 1.7366] | 1.0069 | 1453 | 0.1920 | 0.0155 | 0.0070 | 0.0085 |
| **arc_challenge** | 16 | 300 | 0.7269 | [0.0207, 1.4433] | 1.0072 | 1449 | 0.0030 | 0.0338 | 0.0201 | 0.0136 |
| **gsm8k** | 24 | 300 | 0.0639 | [-0.3636, 0.4902] | 1.0078 | 1313 | 0.5413 | 0.1694 | 0.0062 | 0.1632 |

关键发现：
- **MMLU/ARC (N=16)**: γ 估计正值 (~0.65-0.73)，D045 排除 0.5B 生效。ARC 的 95% CI 不跨 0 (0.02-1.44)，显著；MMLU 的 CI 跨 0
- **GSM8K (N=24)**: γ≈0 且 CI 完全跨 0 → 无显著 contamination signal。但 cal_MAE 大幅下降 (0.169→0.006)，ΔMAE=0.163
- **收敛正常**: 所有 benchmark R̂<1.01, ESS>1300, divergences=0
- **ARC PPP=0.003 偏低**, 模型拟合可能有问题（过拟合或 model misspecification）；MMLU PPP=0.19 可接受；GSM8K PPP=0.54 良好

输出目录: `/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/`

---
