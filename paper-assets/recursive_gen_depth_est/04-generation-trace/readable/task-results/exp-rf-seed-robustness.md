# exp rf seed robustness

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_rf_seed_robustness_20260517T203625_result.json`
- **Structured JSON:** [`b98c3e7d0cc641c3fdb7.json`](../../sessions/b9/b98c3e7d0cc641c3fdb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**RF 种子鲁棒性 (leave-one-model-out CV, n_estimators=200)**

| Seed | Pythia-1.4B | OLMo-1B | GPT-2 XL | Mean |
|------|-------------|---------|----------|------|
| 42   | 0.6242      | 0.6921  | 0.6756   | 0.6640 |
| 123  | 0.6262      | 0.6928  | 0.6758   | 0.6650 |
| 456  | 0.6250      | 0.6937  | 0.6776   | 0.6655 |

**4-class accuracy: 0.6648 ± 0.0006**

Std 仅 0.06%，种子对结果几乎无影响。结果已保存至 `results/rf_seed_robustness.json`。

---
