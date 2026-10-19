# code fix transfer eval and rerun

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_transfer_eval_and_rerun_20260520T203930_result.json`
- **Structured JSON:** [`f6dc5bbad0d5520b01f3.json`](../../sessions/f6/f6dc5bbad0d5520b01f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the complete output:

---

```
=== transfer_eval.py Fix ===
修改: evaluate_probe() 中 AUROC/permutation test 改用 decision_function (logits)
验证: zh@L31 ZS AUROC = 0.6156, MS AUROC = 0.6156, Δ = 0.00pp
      (所有 lang×layer ZS≡MS，因 mean-shift 对线性 logits 仅加常数偏移，不改变 ranking)

=== mvp_003 修正后完整结果 ===

EN Probe per layer (AUROC / ECE):
  L0:  0.6498 / 0.1481
  L4:  0.6349 / 0.2214
  L8:  0.6331 / 0.2287
  L12: 0.6563 / 0.2630
  L16: 0.7026 / 0.2579
  L20: 0.7229 / 0.2257
  L24: 0.7235 / 0.2421
  L28: 0.7129 / 0.2438
  L31: 0.7284 / 0.2052  ← best

ZS Transfer best per language:
  zh: 0.6400 @L20 (p=0.001)
  ar: 0.6146 @L31 (p=0.001)
  hi: 0.5935 @L31 (p=0.001)
  ko: 0.6481 @L31 (p=0.001)
  sw: 0.5838 @L16 (p=0.001)

Gate:
  P1: FAIL (AUROC=0.7284 ok, ECE=0.2052 > 0.15)
  P2: PASS (5/5 langs ≥ 0.58)
  P3: PASS (9.53pp layer-depth delta)
  P4: FAIL (0/5, mean-shift Δ=0 — expected: rank-invariant for linear logits)

=== Llama CKA with ko (5 langs × 9 layers) ===

Layer    zh      ar      hi      sw      ko
    0  0.8805  0.6785  0.1978  0.2654  0.7675
    4  0.9302  0.9237  0.5313  0.7124  0.9096
    8  0.8913  0.8798  0.5534  0.7459  0.8791
   12  0.9224  0.9050  0.6236  0.7047  0.8932
   16  0.8573  0.8300  0.5108  0.6715  0.8409
   20  0.6365  0.5675  0.3496  0.3874  0.5755
   24  0.6069  0.5266  0.2752  0.3000  0.5420
   28  0.5806  0.4820  0.2213  0.2561  0.5030
   31  0.4686  0.3055  0.1615  0.2661  0.3815

Spearman(CKA, degradation):
  Overall: rho=-0.3982, p=0.0068 **
  ar: rho=-0.2833, p=0.4600
  hi: rho=-0.6667, p=0.0499 *
  ko: rho=+0.2500, p=0.5165
  sw: rho=-0.5833, p=0.0992
  zh: rho=-0.4833, p=0.1875
```

---
