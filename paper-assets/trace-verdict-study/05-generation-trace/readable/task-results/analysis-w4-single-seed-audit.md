# analysis w4 single seed audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w4_single_seed_audit_20260521T061454_result.json`
- **Structured JSON:** [`cda56f21b30fdde50a4c.json`](../../sessions/cd/cda56f21b30fdde50a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计结果：

**Table 1 (Cross-Model, 20 cells) 中 single-seed 共 3 个：**
- Qwen-7B × no_trace (seed 42, 75.13%)
- CodeLlama-13B × no_trace (seed 42, 76.47%)
- DeepSeek-6.7B × no_trace (seed 42, 73.36%)

另有 6 个 two-seed cells：ae_only 和 VOTA 各在 Qwen-1.5B / CL-13B / DS-6.7B 上只有 2 seeds。

**Table 2 (Ablation, Qwen-7B) 中 single-seed 共 3 个：**
- full_trace (seed 42, 81.76%)
- no_trace (seed 42, 75.13%)
- VOTA_no_ae (seed 42, 99.41%)

**风险判断：** 没有 single-seed cell 直接支撑可被推翻的核心 claim。最高风险项是 **full_trace 的 single-seed**——C2 密度分解的 "24% gradient dilution" 锚点依赖它。Qwen-1.5B no_trace (3 seeds, σ=4.48pp) 表明 no_trace 可以有较大 seed 方差，但 Tier 边界间距 >12pp，seed 方差无法关闭。

如果 reviewer 质疑，优先补跑 Qwen-7B full_trace seed 123/456（验证 C2 分解比例）。

---
