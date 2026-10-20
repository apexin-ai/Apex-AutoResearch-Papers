# ops read irt v3 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read_irt_v3_results_20260517T003535_result.json`
- **Structured JSON:** [`39875096e50e4fa6257c.json`](../../sessions/39/39875096e50e4fa6257c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## 1. Cross-Family IRT v3 结果

**Config:** 2PL+γ, scales=[0.5B, 1.5B, 3B], exposure=rrf_signal  
**Note:** "v3: fixed d025 Llama MMLU RRF (3/3 signals), excluded alpha16, excluded d100 MMLU, added Llama 3B MMLU"

| Benchmark | N_models | PPP | raw_MAE | cal_MAE | ΔMAE | γ mean | γ CI excl 0 |
|-----------|----------|------|---------|---------|------|--------|-------------|
| gsm8k | 28 | 0.832 | 0.1792 | 0.0078 | 0.1714 | -0.110 | No |
| arc_challenge | 20 | 0.449 | 0.0698 | 0.0150 | 0.0548 | 0.002 | No |
| mmlu | 14 | 0.457 | 0.0449 | 0.0076 | 0.0373 | 0.710 | No |

**Diagnostics (all benchmarks):** all_ok=true, divergent=0, max_rhat≤1.010, min_ess≥1312

**Gamma details:**
- gsm8k: mean=-0.1099, sd=0.2029, 95%CI=[-0.521, 0.280]
- arc_challenge: mean=0.0016, sd=0.2965, 95%CI=[-0.568, 0.595]
- mmlu: mean=0.7095, sd=0.5575, 95%CI=[-0.378, 1.822]

---

## 2. Qwen-Only Baseline (N=24 for gsm8k)

**Config:** 2PL+γ, scales=[0.5B, 1.5B, Qwen2.5-3B], exposure=rrf_signal

| Benchmark | N_models | PPP | raw_MAE | cal_MAE | ΔMAE | γ mean | γ CI excl 0 |
|-----------|----------|------|---------|---------|------|--------|-------------|
| mmlu | 16 | 0.192 | 0.0155 | 0.0070 | 0.0085 | 0.655 | No |
| arc_challenge | 16 | 0.003 | 0.0338 | 0.0201 | 0.0136 | 0.727 | **Yes** |
| gsm8k | 24 | 0.541 | 0.1694 | 0.0062 | 0.1632 | 0.064 | No |

**Diagnostics (all benchmarks):** all_ok=true, divergent=0, max_rhat≤1.008, min_ess≥1313

---

## 3. Cross-Family v3 RRF Respondent List (33 models)

```
Llama-3.2-3B_d000_s42
Llama-3.2-3B_d005_s42
Llama-3.2-3B_d025_s42
Llama-3.2-3B_d100_s42
Qwen2.5-0.5B-Instruct
Qwen2.5-0.5B_d000_s123
Qwen2.5-0.5B_d000_s42
Qwen2.5-0.5B_d005_s123
Qwen2.5-0.5B_d005_s42
Qwen2.5-0.5B_d025_s123
Qwen2.5-0.5B_d025_s42
Qwen2.5-0.5B_d100_s123
Qwen2.5-0.5B_d100_s42
Qwen2.5-1.5B-Instruct
Qwen2.5-1.5B_d000_s123
Qwen2.5-1.5B_d000_s42
Qwen2.5-1.5B_d005_s123
Qwen2.5-1.5B_d005_s42
Qwen2.5-1.5B_d025_s123
Qwen2.5-1.5B_d025_s42
Qwen2.5-1.5B_d100_s123
Qwen2.5-1.5B_d100_s42
Qwen2.5-3B_d000_a32_s42
Qwen2.5-3B_d000_s123
Qwen2.5-3B_d000_s123_a32
Qwen2.5-3B_d000_s42_a32
Qwen2.5-3B_d005_a32_s42
Qwen2.5-3B_d005_s123
Qwen2.5-3B_d005_s42_a32
Qwen2.5-3B_d025_s123
Qwen2.5-3B_d025_v3_s42
Qwen2.5-3B_d100_a32_s123
Qwen2.5-3B_d100_a32_s42
```

---

## 4. d025 RRF v2 Respondent List (7 models, 0 alpha16)

```
Llama-3.2-3B_d025_s42
Qwen2.5-0.5B_d025_s123
Qwen2.5-0.5B_d025_s42
Qwen2.5-1.5B_d025_s123
Qwen2.5-1.5B_d025_s42
Qwen2.5-3B_d025_s123
Qwen2.5-3B_d025_v3_s42
```

**Alpha16 entries: 0** (confirmed clean)

---
