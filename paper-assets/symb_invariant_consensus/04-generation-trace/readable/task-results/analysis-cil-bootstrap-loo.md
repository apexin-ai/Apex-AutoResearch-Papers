# analysis cil bootstrap loo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cil-bootstrap-loo_20260522T012915_result.json`
- **Structured JSON:** [`d9ca7920f22ca8ba9353.json`](../../sessions/d9/d9ca7920f22ca8ba9353.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## CIL Bootstrap CI + LOO (n=10 pairs)

**Point estimate:**
- Spearman ρ = 0.8389, p = 0.0024

**Bootstrap 95% CI (10,000 resamples):**
- 95% CI = [0.3375, 0.9902]
- CI 排除零: **YES**
- Mean ρ = 0.7968, Median ρ = 0.8509

**Leave-one-out:**

| Dropped | ρ | p | Δρ |
|---|---|---|---|
| Mis×DeBERTa/PW | 0.7950 | 0.0104 | -0.044 |
| Mis×RoBERTa/PW | 0.7833 | 0.0125 | -0.056 |
| Mis×BART/PW | 0.7950 | 0.0104 | -0.044 |
| Qw14×DeBERTa/PW | 0.9121 | 0.0006 | +0.073 |
| Qw14×SICA/PW | 0.8285 | 0.0058 | -0.011 |
| LLa8×DeBERTa/PW | 0.7833 | 0.0125 | -0.056 |
| Qw3×DeBERTa/PW | 0.8619 | 0.0028 | +0.023 |
| Mis×DeBERTa/FO | 0.8954 | 0.0011 | +0.057 |
| Mis×SICA/FO | 0.8954 | 0.0011 | +0.057 |
| Mis×SICA/PW | 0.7782 | 0.0135 | -0.061 |

**所有 LOO p < 0.05** — 相关性在移除任意单点后均保持显著。

**最脆弱点:** Mis×SICA/PW（移除后 ρ 降至 0.778，仍 p=0.014 显著）。Qw14×DeBERTa/PW 是 inflating point（移除后 ρ 升至 0.912）。

新增 2 个 pairs 的 CIL：LLaMA-8B = 0.4150, Qwen3-14B = 0.3618（从 westd-16639 的 exp092/D116 complementarity 表直接计算）。n 从 8 升到 10 后，ρ 从 0.8095 升至 0.8389，p 从 0.0149 降至 0.0024。

结果已保存到 `/root/symb_invariant_consensus/results/cil_bootstrap_loo.json`。

---
